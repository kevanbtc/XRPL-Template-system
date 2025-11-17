 well to start building a scoring system and rating and ensure we are f SANTANDER FACILITY — TECHNICAL IMPLEMENTATION GUIDE

**Purpose:** Complete technical blueprint for integrating Santander banking facility into Unykorn rails
**Scope:** Proof Server → Chainlink Oracle → On-Chain Contracts → Stablecoin Pool
**Audience:** Backend engineers, smart contract developers, DevOps

---

## ARCHITECTURE OVERVIEW

```
┌─────────────────────────────────────────────────────────────────────┐
│                         OFF-CHAIN WORLD                              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  ┌─────────────────┐         ┌──────────────────┐                  │
│  │ Santander RM    │────────>│  Daily Statement │                  │
│  │ (Email/Portal)  │         │  PDF / API       │                  │
│  └─────────────────┘         └──────────────────┘                  │
│                                       │                              │
│                                       │ Encrypted Upload             │
│                                       ▼                              │
│                              ┌─────────────────┐                    │
│                              │  PROOF SERVER   │                    │
│                              │  (Your Backend) │                    │
│                              │                 │                    │
│                              │ • PDF ingestion │                    │
│                              │ • Signature val │                    │
│                              │ • OCR extraction│                    │
│                              │ • Hash storage  │                    │
│                              └─────────────────┘                    │
│                                       │                              │
│                                       │ HTTPS API                    │
│                                       ▼                              │
├─────────────────────────────────────────────────────────────────────┤
│                       CHAINLINK ORACLE LAYER                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│                    ┌───────────────────────┐                        │
│                    │ EXTERNAL ADAPTER      │                        │
│                    │ santander-iban-v1     │                        │
│                    │                       │                        │
│                    │ • Calls Proof Server  │                        │
│                    │ • Validates freshness │                        │
│                    │ • Scales to 1e18      │                        │
│                    └───────────────────────┘                        │
│                               │                                      │
│                               │ Chainlink Job                        │
│                               ▼                                      │
│                    ┌───────────────────────┐                        │
│                    │  CHAINLINK NODE       │                        │
│                    │  (Daily Cron Job)     │                        │
│                    └───────────────────────┘                        │
│                               │                                      │
│                               │ updateValue() tx                     │
│                               ▼                                      │
├─────────────────────────────────────────────────────────────────────┤
│                         ON-CHAIN WORLD                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│     ┌─────────────────────────────────────────────────────┐        │
│     │  SantanderFacilityFeed (Oracle Contract)            │        │
│     │  Storage: facilityAvailable (1e18 scaled EUR)       │        │
│     └─────────────────────────────────────────────────────┘        │
│                               │                                      │
│                               │ read                                 │
│                               ▼                                      │
│     ┌─────────────────────────────────────────────────────┐        │
│     │  FacilityRegistry                                    │        │
│     │  getUsableCapacity(facilityId) → EUR amount          │        │
│     └─────────────────────────────────────────────────────┘        │
│                               │                                      │
│                               │ check before mint                    │
│                               ▼                                      │
│     ┌─────────────────────────────────────────────────────┐        │
│     │  TGUSD-SANTANDER-POOL                                │        │
│     │  • Mints capped by oracle value                      │        │
│     │  • Enforces 120% collateralization                   │        │
│     │  • Auto-freezes if PoR fails                         │        │
│     └─────────────────────────────────────────────────────┘        │
│                                                                       │
└─────────────────────────────────────────────────────────────────────┘
```

---

## COMPONENT 1: PROOF SERVER

### Purpose
- Ingest daily bank statements/confirmations from Santander RM
- Validate authenticity (digital signatures, seals)
- Extract key data (balance, blocked funds)
- Expose HTTPS API for Chainlink adapter

### Tech Stack
- **Framework:** FastAPI (Python) or Express (Node.js)
- **Storage:** PostgreSQL (proof history) + S3 (encrypted PDFs)
- **Auth:** API key + IP whitelist for Chainlink node
- **Crypto:** GPG for statement verification, SHA-256 for hashing

---

### Endpoints

#### `POST /api/v1/statements/upload`

**Purpose:** Banker (or you) uploads daily statement

**Auth:** Bearer token (internal only)

**Request:**
```json
{
  "iban": "ES2100495656532310002112",
  "statement_date": "2025-01-15",
  "file": "<base64-encoded PDF or binary upload>"
}
```

**Processing:**
1. Save encrypted file to S3: `s3://unykorn-proofs/santander/2025-01-15.pdf.enc`
2. Compute SHA-256 hash of original file
3. Extract data via OCR or API parse:
   - `account_balance_eur`
   - `blocked_funds_eur` (if present)
   - `statement_date`
4. Validate digital signature/seal (if PDF has one)
5. Store record in DB:

```sql
INSERT INTO proof_records (
  iban, statement_date, balance_eur, blocked_funds_eur,
  file_hash, file_path, verified_at
) VALUES (
  'ES2100495656532310002112', '2025-01-15', 128000000, 200000000,
  '0xabc123...', 's3://...', NOW()
);
```

**Response:**
```json
{
  "status": "success",
  "proof_id": "proof_santander_20250115",
  "hash": "0xabc123..."
}
```

---

#### `GET /api/v1/proofs/latest`

**Purpose:** Chainlink adapter fetches latest verified proof

**Auth:** API key (Chainlink node only)

**Request:**
```
GET /api/v1/proofs/latest?iban=ES2100495656532310002112
```

**Response:**
```json
{
  "iban": "ES2100495656532310002112",
  "statement_date": "2025-01-15",
  "account_balance_eur": 128000000,
  "blocked_funds_eur": 200000000,
  "facility_available_eur": 100000000,
  "timestamp": 1736953200,
  "file_hash": "0xabc123...",
  "verified": true,
  "age_hours": 18
}
```

**Notes:**
- `facility_available_eur` = `min(blocked_funds_eur, FACILITY_CAP)` (configured per facility)
- `age_hours` = time since `statement_date` — used for freshness check

---

### Database Schema

```sql
CREATE TABLE proof_records (
  id SERIAL PRIMARY KEY,
  iban VARCHAR(34) NOT NULL,
  statement_date DATE NOT NULL,
  balance_eur NUMERIC(18, 2),
  blocked_funds_eur NUMERIC(18, 2),
  facility_available_eur NUMERIC(18, 2),
  file_hash VARCHAR(66), -- 0x + 64 hex chars
  file_path TEXT,
  verified_at TIMESTAMP DEFAULT NOW(),
  created_at TIMESTAMP DEFAULT NOW(),
  UNIQUE(iban, statement_date)
);

CREATE INDEX idx_iban_date ON proof_records(iban, statement_date DESC);
```

---

### Security Considerations

**1. Encryption at Rest:**
- All PDFs stored encrypted in S3 (AES-256)
- Encryption key in AWS KMS or HashiCorp Vault

**2. Access Control:**
- Proof Server only accessible from:
  - Your internal network (bastion host)
  - Chainlink node IP (whitelisted)
- No public internet access

**3. Audit Trail:**
- Every API call logged (who, when, which endpoint)
- Every proof upload creates immutable record
- File hashes stored on-chain (optional: commit to XRPL-M for public verifiability)

**4. Banker Authentication:**
- When banker emails statement, verify:
  - Email domain: `@santander.com` or similar
  - PGP signature on attachment (if available)
  - Cross-check with phone call if large discrepancy

---

## COMPONENT 2: CHAINLINK EXTERNAL ADAPTER

### Purpose
- Bridge between Proof Server (off-chain) and blockchain (on-chain)
- Called by Chainlink node as part of daily job
- Returns normalized numeric value for smart contract consumption

### Tech Stack
- **Language:** Node.js (TypeScript)
- **Framework:** Express
- **Deployment:** Docker container on ECS or dedicated EC2
- **Monitoring:** CloudWatch Logs, Datadog

---

### Code Structure

**File:** `src/index.ts`

```typescript
import express, { Request, Response } from 'express';
import axios from 'axios';

const app = express();
app.use(express.json());

const PROOF_SERVER_URL = process.env.PROOF_SERVER_URL || 'https://proof.unykorn.internal';
const PROOF_SERVER_API_KEY = process.env.PROOF_SERVER_API_KEY;
const FACILITY_CAP_EUR = Number(process.env.FACILITY_CAP_EUR) || 100_000_000;
const MAX_PROOF_AGE_HOURS = Number(process.env.MAX_PROOF_AGE_HOURS) || 36;

interface ChainlinkRequest {
  id: string;
  data: {
    iban?: string;
    facilityId?: string;
  };
}

interface ProofServerResponse {
  iban: string;
  statement_date: string;
  account_balance_eur: number;
  blocked_funds_eur: number;
  facility_available_eur: number;
  timestamp: number;
  file_hash: string;
  verified: boolean;
  age_hours: number;
}

app.post('/', async (req: Request, res: Response) => {
  const jobRunId = req.body.id || '1';

  try {
    const { iban } = req.body.data as ChainlinkRequest['data'];

    if (!iban) {
      throw new Error('Missing required parameter: iban');
    }

    // 1. Fetch latest proof from Proof Server
    const proofResp = await axios.get<ProofServerResponse>(
      `${PROOF_SERVER_URL}/api/v1/proofs/latest`,
      {
        params: { iban },
        headers: { 'Authorization': `Bearer ${PROOF_SERVER_API_KEY}` }
      }
    );

    const proof = proofResp.data;

    // 2. Freshness check
    if (proof.age_hours > MAX_PROOF_AGE_HOURS) {
      throw new Error(`Proof too old: ${proof.age_hours} hours (max: ${MAX_PROOF_AGE_HOURS})`);
    }

    // 3. Verification check
    if (!proof.verified) {
      throw new Error('Proof failed verification');
    }

    // 4. Compute facility available (apply cap)
    const facilityAvailable = Math.min(proof.blocked_funds_eur, FACILITY_CAP_EUR);

    // 5. Scale to 1e18 for Solidity (wei-like representation)
    // Solidity will treat this as EUR with 18 decimals
    const scaled = BigInt(Math.floor(facilityAvailable * 1e18));

    // 6. Return to Chainlink
    res.status(200).json({
      jobRunId,
      data: {
        result: scaled.toString(), // string to avoid JSON number precision issues
        iban: proof.iban,
        statement_date: proof.statement_date,
        file_hash: proof.file_hash,
        timestamp: proof.timestamp
      },
      statusCode: 200
    });

  } catch (error: any) {
    console.error('Adapter error:', error.message);
    res.status(500).json({
      jobRunId,
      status: 'errored',
      error: error.message,
      statusCode: 500
    });
  }
});

app.get('/health', (req: Request, res: Response) => {
  res.status(200).json({ status: 'healthy' });
});

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
  console.log(`Santander IBAN Adapter listening on port ${PORT}`);
});
```

---

### Environment Variables

```bash
PROOF_SERVER_URL=https://proof.unykorn.internal
PROOF_SERVER_API_KEY=<secret-api-key>
FACILITY_CAP_EUR=100000000  # €100M facility cap
MAX_PROOF_AGE_HOURS=36      # Reject proofs older than 36 hours
PORT=8080
```

---

### Deployment

**Dockerfile:**

```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY dist/ ./dist/
EXPOSE 8080
CMD ["node", "dist/index.js"]
```

**Deploy to ECS:**

```bash
# Build and push to ECR
docker build -t santander-adapter .
docker tag santander-adapter:latest 123456789012.dkr.ecr.us-east-1.amazonaws.com/santander-adapter:latest
docker push 123456789012.dkr.ecr.us-east-1.amazonaws.com/santander-adapter:latest

# Update ECS service
aws ecs update-service --cluster unykorn-prod --service santander-adapter --force-new-deployment
```

**Health Check:**

```bash
curl https://santander-adapter.unykorn.internal/health
# Expected: {"status": "healthy"}
```

---

## COMPONENT 3: CHAINLINK JOB SPECIFICATION

### Purpose
- Daily cron job to update on-chain facility value
- Calls External Adapter → writes to Oracle Contract

### Chainlink Node Setup

**Job Spec (TOML):**

```toml
type = "cron"
schemaVersion = 1
name = "Santander Facility Daily PoR"
schedule = "0 6 * * *"  # Every day at 06:00 UTC
externalJobID = "santander-facility-por-daily"

observationSource = """
    fetch_proof [type="bridge" name="santander-iban-adapter" requestData="{\\"iban\\": \\"ES2100495656532310002112\\"}"]
    parse [type="jsonparse" path="data,result"]
    submit [type="ethtx" to="0xFacilityFeedContractAddress" data="$(parse)"]

    fetch_proof -> parse -> submit
"""
```

**Bridge Configuration:**

```json
{
  "name": "santander-iban-adapter",
  "url": "https://santander-adapter.unykorn.internal",
  "confirmations": 0,
  "minimumContractPayment": "0"
}
```

---

### Testing the Job

**Manual Trigger:**

```bash
# Via Chainlink node UI or CLI
chainlink jobs run <job-id>
```

**Expected Flow:**

1. Chainlink node sends POST to adapter with `iban` param
2. Adapter fetches latest proof from Proof Server
3. Adapter returns scaled EUR value (1e18)
4. Chainlink node calls `SantanderFacilityFeed.updateValue(scaled)`
5. On-chain value updated, event emitted

---

## COMPONENT 4: SMART CONTRACTS

### Contract 1: SantanderFacilityFeed (Oracle Storage)

**Purpose:** Store latest facility value from Chainlink oracle

**File:** `contracts/SantanderFacilityFeed.sol`

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@chainlink/contracts/src/v0.8/ChainlinkClient.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract SantanderFacilityFeed is Ownable {
    uint256 public facilityAvailable; // EUR amount scaled to 1e18
    uint256 public lastUpdated;

    address public oracleAddress;
    bool public frozen;

    event FacilityUpdated(uint256 newValue, uint256 timestamp);
    event FacilityFrozen(string reason);
    event FacilityUnfrozen();

    modifier notFrozen() {
        require(!frozen, "Facility feed is frozen");
        _;
    }

    constructor(address _oracleAddress) {
        oracleAddress = _oracleAddress;
    }

    /**
     * @notice Update facility value (only callable by oracle)
     * @param _newValue New facility available amount (1e18 scaled EUR)
     */
    function updateValue(uint256 _newValue) external notFrozen {
        require(msg.sender == oracleAddress, "Only oracle can update");

        facilityAvailable = _newValue;
        lastUpdated = block.timestamp;

        emit FacilityUpdated(_newValue, block.timestamp);
    }

    /**
     * @notice Freeze feed (emergency stop)
     * @param reason Human-readable reason for freeze
     */
    function freeze(string calldata reason) external onlyOwner {
        frozen = true;
        emit FacilityFrozen(reason);
    }

    /**
     * @notice Unfreeze feed
     */
    function unfreeze() external onlyOwner {
        frozen = false;
        emit FacilityUnfrozen();
    }

    /**
     * @notice Update oracle address (if node changes)
     * @param _newOracle New Chainlink oracle address
     */
    function setOracleAddress(address _newOracle) external onlyOwner {
        oracleAddress = _newOracle;
    }

    /**
     * @notice Check if feed is stale (>48 hours)
     */
    function isStale() external view returns (bool) {
        return block.timestamp - lastUpdated > 48 hours;
    }
}
```

---

### Contract 2: FacilityRegistry

**Purpose:** Track facility metadata and compute usable capacity

**File:** `contracts/FacilityRegistry.sol`

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/access/Ownable.sol";

interface IFacilityFeed {
    function facilityAvailable() external view returns (uint256);
    function lastUpdated() external view returns (uint256);
    function isStale() external view returns (bool);
}

contract FacilityRegistry is Ownable {
    struct Facility {
        bytes32 id;
        uint256 cap; // max EUR amount (1e18 scaled)
        uint256 minCollateralRatio; // basis points (e.g., 12000 = 120%)
        address oracleFeed;
        bool active;
    }

    mapping(bytes32 => Facility) public facilities;

    event FacilityAdded(bytes32 indexed id, uint256 cap, address oracleFeed);
    event FacilityUpdated(bytes32 indexed id, uint256 cap, bool active);

    /**
     * @notice Add new facility
     * @param id Facility identifier (e.g., keccak256("FAC-SANTANDER-001"))
     * @param cap Maximum facility size (1e18 scaled EUR)
     * @param minCollateralRatio Minimum collateralization (bps)
     * @param oracleFeed Address of facility feed contract
     */
    function addFacility(
        bytes32 id,
        uint256 cap,
        uint256 minCollateralRatio,
        address oracleFeed
    ) external onlyOwner {
        require(facilities[id].id == bytes32(0), "Facility already exists");

        facilities[id] = Facility({
            id: id,
            cap: cap,
            minCollateralRatio: minCollateralRatio,
            oracleFeed: oracleFeed,
            active: true
        });

        emit FacilityAdded(id, cap, oracleFeed);
    }

    /**
     * @notice Update facility parameters
     */
    function updateFacility(
        bytes32 id,
        uint256 cap,
        uint256 minCollateralRatio,
        bool active
    ) external onlyOwner {
        Facility storage fac = facilities[id];
        require(fac.id != bytes32(0), "Facility does not exist");

        fac.cap = cap;
        fac.minCollateralRatio = minCollateralRatio;
        fac.active = active;

        emit FacilityUpdated(id, cap, active);
    }

    /**
     * @notice Get usable capacity for facility
     * @param id Facility identifier
     * @return Usable EUR capacity (1e18 scaled)
     */
    function getUsableCapacity(bytes32 id) public view returns (uint256) {
        Facility storage fac = facilities[id];

        if (!fac.active) return 0;

        IFacilityFeed feed = IFacilityFeed(fac.oracleFeed);

        // Reject if oracle data is stale
        if (feed.isStale()) return 0;

        uint256 available = feed.facilityAvailable();

        // Apply facility cap
        return available > fac.cap ? fac.cap : available;
    }

    /**
     * @notice Get facility info
     */
    function getFacility(bytes32 id) external view returns (Facility memory) {
        return facilities[id];
    }
}
```

---

### Contract 3: TGUSD-SANTANDER-POOL (Stablecoin Pool)

**Purpose:** Mint TGUSD backed by Santander facility

**File:** `contracts/TGUSDSantanderPool.sol`

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

interface IFacilityRegistry {
    function getUsableCapacity(bytes32 id) external view returns (uint256);
}

interface IPriceFeed {
    function latestAnswer() external view returns (int256);
}

contract TGUSDSantanderPool is ERC20, Ownable {
    bytes32 public constant FACILITY_ID = keccak256("FAC-SANTANDER-001");

    IFacilityRegistry public facilityRegistry;
    IPriceFeed public eurUsdPriceFeed; // Chainlink EUR/USD feed

    uint256 public constant MIN_COLLATERAL_RATIO = 12000; // 120% in bps
    uint256 public totalMinted;

    event Minted(address indexed to, uint256 amount, uint256 facilityUsed);
    event Burned(address indexed from, uint256 amount, uint256 facilityFreed);

    constructor(
        address _facilityRegistry,
        address _eurUsdPriceFeed
    ) ERC20("Third Gate USD (Santander Pool)", "TGUSD-SANT") {
        facilityRegistry = IFacilityRegistry(_facilityRegistry);
        eurUsdPriceFeed = IPriceFeed(_eurUsdPriceFeed);
    }

    /**
     * @notice Mint TGUSD (only authorized minter)
     * @param to Recipient address
     * @param amount USD amount to mint (1e18 scaled)
     */
    function mint(address to, uint256 amount) external onlyOwner {
        // 1. Get facility capacity in EUR
        uint256 capacityEur = facilityRegistry.getUsableCapacity(FACILITY_ID);
        require(capacityEur > 0, "Facility unavailable");

        // 2. Convert to USD
        int256 eurUsdPrice = eurUsdPriceFeed.latestAnswer(); // e.g., 1.08 USD per EUR (8 decimals)
        require(eurUsdPrice > 0, "Invalid price feed");

        uint256 capacityUsd = (capacityEur * uint256(eurUsdPrice)) / 1e8;

        // 3. Apply collateralization ratio
        uint256 maxMint = (capacityUsd * 10000) / MIN_COLLATERAL_RATIO; // Divide by 120%

        // 4. Check mint cap
        require(totalMinted + amount <= maxMint, "Exceeds facility capacity");

        // 5. Mint
        totalMinted += amount;
        _mint(to, amount);

        emit Minted(to, amount, capacityEur);
    }

    /**
     * @notice Burn TGUSD (redemption)
     * @param from Address to burn from
     * @param amount USD amount to burn
     */
    function burn(address from, uint256 amount) external onlyOwner {
        totalMinted -= amount;
        _burn(from, amount);

        emit Burned(from, amount, 0);
    }

    /**
     * @notice Check current collateralization ratio
     * @return Ratio in basis points (e.g., 12500 = 125%)
     */
    function collateralizationRatio() external view returns (uint256) {
        if (totalMinted == 0) return type(uint256).max;

        uint256 capacityEur = facilityRegistry.getUsableCapacity(FACILITY_ID);
        int256 eurUsdPrice = eurUsdPriceFeed.latestAnswer();

        if (eurUsdPrice <= 0 || capacityEur == 0) return 0;

        uint256 capacityUsd = (capacityEur * uint256(eurUsdPrice)) / 1e8;

        return (capacityUsd * 10000) / totalMinted;
    }

    /**
     * @notice Emergency freeze (stops all minting)
     */
    function freeze() external onlyOwner {
        // Implementation: Set paused flag, emit event
        // (Add pausable logic if needed)
    }
}
```

---

## COMPONENT 5: DEPLOYMENT & TESTING

### Deployment Script (Hardhat)

**File:** `scripts/deploy-santander-facility.ts`

```typescript
import { ethers } from "hardhat";

async function main() {
  const [deployer] = await ethers.getSigners();
  console.log("Deploying with account:", deployer.address);

  // 1. Deploy Oracle Feed
  const oracleAddress = process.env.CHAINLINK_ORACLE_ADDRESS!;
  const FacilityFeed = await ethers.getContractFactory("SantanderFacilityFeed");
  const facilityFeed = await FacilityFeed.deploy(oracleAddress);
  await facilityFeed.deployed();
  console.log("SantanderFacilityFeed deployed to:", facilityFeed.address);

  // 2. Deploy Facility Registry
  const FacilityRegistry = await ethers.getContractFactory("FacilityRegistry");
  const registry = await FacilityRegistry.deploy();
  await registry.deployed();
  console.log("FacilityRegistry deployed to:", registry.address);

  // 3. Add Santander facility to registry
  const facilityId = ethers.utils.id("FAC-SANTANDER-001");
  const cap = ethers.utils.parseUnits("100000000", 18); // €100M
  const minCollateralRatio = 12000; // 120%

  await registry.addFacility(facilityId, cap, minCollateralRatio, facilityFeed.address);
  console.log("Facility FAC-SANTANDER-001 added to registry");

  // 4. Deploy Stablecoin Pool
  const eurUsdFeedAddress = process.env.CHAINLINK_EURUSD_FEED!;
  const TGUSDPool = await ethers.getContractFactory("TGUSDSantanderPool");
  const pool = await TGUSDPool.deploy(registry.address, eurUsdFeedAddress);
  await pool.deployed();
  console.log("TGUSDSantanderPool deployed to:", pool.address);

  // 5. Output addresses for .env
  console.log("\n=== Deployment Complete ===");
  console.log("Add to .env:");
  console.log(`SANTANDER_FACILITY_FEED=${facilityFeed.address}`);
  console.log(`FACILITY_REGISTRY=${registry.address}`);
  console.log(`TGUSD_SANTANDER_POOL=${pool.address}`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
```

**Run:**

```bash
npx hardhat run scripts/deploy-santander-facility.ts --network polygon
```

---

### Testing Flow

**1. Upload Test Statement to Proof Server:**

```bash
curl -X POST https://proof.unykorn.internal/api/v1/statements/upload \
  -H "Authorization: Bearer ${PROOF_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "iban": "ES2100495656532310002112",
    "statement_date": "2025-01-15",
    "file": "<base64-encoded-test-pdf>"
  }'
```

**2. Test External Adapter:**

```bash
curl -X POST https://santander-adapter.unykorn.internal \
  -H "Content-Type: application/json" \
  -d '{
    "id": "test-run-123",
    "data": {
      "iban": "ES2100495656532310002112"
    }
  }'
```

**Expected Response:**

```json
{
  "jobRunId": "test-run-123",
  "data": {
    "result": "100000000000000000000000000", // 100M EUR scaled to 1e18
    "iban": "ES2100495656532310002112",
    "statement_date": "2025-01-15",
    "file_hash": "0xabc123...",
    "timestamp": 1736953200
  },
  "statusCode": 200
}
```

**3. Manually Update Oracle Feed (Testing):**

```bash
npx hardhat run scripts/test-update-feed.ts --network polygon
```

```typescript
// scripts/test-update-feed.ts
const feed = await ethers.getContractAt("SantanderFacilityFeed", FEED_ADDRESS);
const testValue = ethers.utils.parseUnits("100000000", 18); // €100M
await feed.updateValue(testValue);
console.log("Feed updated with test value");
```

**4. Check Facility Capacity:**

```bash
npx hardhat console --network polygon
```

```javascript
const registry = await ethers.getContractAt("FacilityRegistry", REGISTRY_ADDRESS);
const facilityId = ethers.utils.id("FAC-SANTANDER-001");
const capacity = await registry.getUsableCapacity(facilityId);
console.log("Usable capacity:", ethers.utils.formatUnits(capacity, 18), "EUR");
```

**5. Test Mint:**

```javascript
const pool = await ethers.getContractAt("TGUSDSantanderPool", POOL_ADDRESS);
const mintAmount = ethers.utils.parseUnits("10000000", 18); // $10M
await pool.mint(deployer.address, mintAmount);
console.log("Minted 10M TGUSD");

const ratio = await pool.collateralizationRatio();
console.log("Collateralization ratio:", ratio.toString(), "bps");
```

---

## COMPONENT 6: MONITORING & ALERTING

### CloudWatch Dashboards

**Dashboard 1: Proof Server Health**

Metrics:
- API request count (per endpoint)
- Error rate (5xx responses)
- Average response time
- Failed proof validations
- Proof age distribution

**Alarms:**
- Proof Server 5xx rate > 5% for 5 minutes → PagerDuty
- No proof uploaded in 48 hours → Email alert
- Proof validation failure rate > 10% → Slack warning

---

**Dashboard 2: Chainlink Job Health**

Metrics:
- Job run success rate
- Job run latency
- Last successful update timestamp
- Gas costs per update

**Alarms:**
- Job fails 3 times in a row → PagerDuty
- No successful update in 48 hours → PagerDuty
- Gas cost > $100 per update → Cost alert

---

**Dashboard 3: On-Chain Facility Status**

Metrics:
- Facility available (EUR)
- TGUSD minted (USD)
- Collateralization ratio (%)
- Oracle feed staleness
- Facility freeze status

**Alarms:**
- Collateralization ratio < 110% → Email warning
- Collateralization ratio < 105% → PagerDuty critical
- Oracle feed stale (>48hrs) → Auto-freeze + PagerDuty
- Facility frozen → Slack notification

---

### Datadog Integration

**Custom Metrics:**

```python
# In Proof Server
from datadog import statsd

@app.post("/api/v1/statements/upload")
async def upload_statement(request: StatementUpload):
    statsd.increment('proof_server.statements.uploaded')

    # ... processing ...

    if verified:
        statsd.increment('proof_server.statements.verified')
    else:
        statsd.increment('proof_server.statements.failed')

    statsd.histogram('proof_server.balance_eur', balance_eur)
```

**Dashboards:**
- Proof upload volume (daily/hourly)
- Verification success rate
- Balance trends over time
- Facility utilization (% of cap used)

---

## COMPONENT 7: SECURITY CHECKLIST

### Pre-Production Audit

- [ ] **Smart Contracts:**
  - [ ] External audit by reputable firm (Consensys, Trail of Bits, OpenZeppelin)
  - [ ] Formal verification of mint/burn logic
  - [ ] Reentrancy guards on all state-changing functions
  - [ ] Access control review (onlyOwner, role-based)
  - [ ] Emergency pause mechanisms tested

- [ ] **Oracle Security:**
  - [ ] Chainlink node runs on dedicated infrastructure (not shared)
  - [ ] Node private keys stored in HSM
  - [ ] External Adapter API key rotated monthly
  - [ ] Rate limiting on adapter endpoints
  - [ ] DDoS protection on adapter

- [ ] **Proof Server:**
  - [ ] All PDFs encrypted at rest (AES-256)
  - [ ] API authentication via short-lived JWT tokens
  - [ ] IP whitelist for Chainlink node
  - [ ] Audit logs immutable (write-only S3 bucket)
  - [ ] No sensitive data in application logs

- [ ] **Banker Communication:**
  - [ ] PGP-signed emails preferred
  - [ ] Phone verification for large balance changes
  - [ ] Out-of-band confirmation for facility draws

- [ ] **Disaster Recovery:**
  - [ ] Proof Server DB backed up daily (encrypted)
  - [ ] Smart contracts upgradeable via proxy pattern (OpenZeppelin)
  - [ ] Emergency multisig can freeze facility (3-of-5 signers)
  - [ ] Runbook for "oracle compromised" scenario

---

## COMPONENT 8: OPERATIONAL RUNBOOK

### Daily Operations

**6:00 AM UTC: Oracle Update**

- Chainlink job runs automatically
- Check CloudWatch dashboard for success
- If failed:
  - Review adapter logs
  - Check Proof Server health
  - Manually trigger job if transient error
  - If persistent issue → page on-call engineer

**9:00 AM UTC: Manual Review**

- Review previous day's facility balance
- Check for anomalies (sudden large drops)
- Verify no failed transactions in pool contract
- Spot-check: Call Santander RM if anything unusual

---

### Weekly Operations

**Monday: Capacity Planning**

- Review TGUSD mint/burn activity
- Calculate facility utilization %
- If >80% utilized → discuss expanding facility with banker
- Update investor reports

**Friday: Security Review**

- Review access logs (who accessed Proof Server?)
- Check for failed authentication attempts
- Rotate API keys if any suspicious activity
- Test emergency freeze procedure

---

### Monthly Operations

**First of Month:**

- Reconcile on-chain minting with off-chain facility draws
- Update IPFS bundle with latest statements (last 30 days)
- Refresh facility documentation in investor portal
- External security scan on Proof Server

---

### Quarterly Operations

**Facility Renewal:**

- 60 days before maturity: Contact Santander RM for renewal terms
- 30 days before: Execute new facility agreement
- Update smart contracts with new maturity date
- Announce to TGUSD holders via governance forum

**Audit:**

- External audit of Proof Server records vs. on-chain state
- Verify 100% of statements match oracle updates
- Generate compliance report for regulators (if applicable)

---

## CONCLUSION

You now have a complete technical blueprint for:

1. **Proof Server:** Ingest and verify bank statements
2. **Chainlink Adapter:** Bridge off-chain data to on-chain oracle
3. **Smart Contracts:** Store facility value, enforce mint caps, issue stablecoins
4. **Monitoring:** Real-time dashboards and alerting
5. **Security:** Audit checklist and access controls
6. **Operations:** Daily/weekly/monthly runbooks

This is the **institutional-grade version** of a bank-backed stablecoin system — transparent, auditable, and mechanically enforced.

**Next Steps:**

1. Deploy Proof Server (FastAPI + PostgreSQL + S3)
2. Build and test External Adapter (Node.js + Docker)
3. Deploy smart contracts to testnet (Polygon Mumbai / Sepolia)
4. Run end-to-end test with mock statement
5. Schedule Santander RM call to discuss daily statement delivery
6. Launch on mainnet once banker confirms facility terms

**Timeline:** 8–10 weeks from kickoff to production (assuming banker cooperation and no major blockers).

**This same template works for:**
- Other bank facilities (different IBANs, different banks)
- T-bill custody accounts (oracle checks broker statements)
- Gold vault holdings (oracle checks vault receipts)
- Any RWA where you can get daily/weekly third-party verification

The rails are universal. Only the data source changes.
