# System Architecture

**XRPL Sovereign Bank Rack System** – Technical Deep Dive

*Version 1.0 | Last Updated: November 17, 2025*

---

## Table of Contents

1. [Overview](#overview)
2. [System Philosophy](#system-philosophy)
3. [3-Node XRPL Topology](#3-node-xrpl-topology)
4. [EVM Control Plane](#evm-control-plane)
5. [Service Layer Architecture](#service-layer-architecture)
6. [Data Models](#data-models)
7. [Integration Flows](#integration-flows)
8. [Security Architecture](#security-architecture)
9. [Deployment Strategy](#deployment-strategy)
10. [Scalability & Performance](#scalability--performance)

---

## Overview

This system architecture document describes the **technical implementation** of a US-regulated, institutional-grade XRPL stablecoin issuer platform.

**Core Design Principles:**

- **XRPL = Payment Rail**: Fast, cheap money movement (balance sheet)
- **EVM = Control Plane**: Authorization logic, safety constraints (rules engine)
- **PostgreSQL = Source of Truth**: Customer data, compliance records, audit logs
- **Smart Contracts = Enforcement**: Mathematical invariants (`supply <= reserves`)
- **Multi-Sig Everywhere**: No single point of failure for critical operations

---

## System Philosophy

### Separation of Concerns

```
┌─────────────────────────────────────────────────────────────┐
│  XRPL Layer (What CAN happen)                               │
│  - Trustlines, payments, balances                           │
│  - NFT minting/burning                                      │
│  - Fast finality (~3-5 seconds)                             │
│  - No smart contracts, just protocol rules                  │
└─────────────────────────────────────────────────────────────┘
                            ↕
┌─────────────────────────────────────────────────────────────┐
│  EVM Layer (What SHOULD happen)                             │
│  - ComplianceRegistry: who is allowed                       │
│  - MintGuard: how much can be minted                        │
│  - ReserveRegistry: what reserves exist                     │
│  - SystemGuard: emergency pause controls                    │
└─────────────────────────────────────────────────────────────┘
                            ↕
┌─────────────────────────────────────────────────────────────┐
│  Off-Chain Layer (What WILL happen)                         │
│  - Bots read EVM events, execute XRPL transactions          │
│  - Backend services bridge bank ↔ XRPL                      │
│  - PostgreSQL stores customer data, KYC, audit logs         │
│  - Redis caches wallet state, session data                  │
└─────────────────────────────────────────────────────────────┘
                            ↕
┌─────────────────────────────────────────────────────────────┐
│  Bank Layer (What IS REAL)                                  │
│  - USD reserves in US banks (FDIC-insured)                  │
│  - Wire/ACH in/out                                          │
│  - Daily balance pulls for PoR reconciliation               │
└─────────────────────────────────────────────────────────────┘
```

**Key Insight**: XRPL can do anything you sign. EVM decides what you're *willing* to sign. PostgreSQL remembers what you *actually* signed.

---

## 3-Node XRPL Topology

### Node Roles

| Node | Purpose | Exposure | Key Access |
|------|---------|----------|------------|
| **Core Node** | Analytics, bots, monitoring | Public (rate-limited) | None |
| **Treasury Node** | Issuer operations (mint/burn ONLY) | Private (VPN + IP whitelist) | Warm treasury keys (online HSM, multi-sig 2-of-3) |
| **Member API Node** | Client-facing reads, quotes, balances | Public (rate-limited) | None |

### Network Topology

```
                      ┌───────────────────────────┐
                      │   Internet (Public)       │
                      └──────────┬────────────────┘
                                 │
                      ┌──────────▼────────────┐
                      │   CloudFlare / WAF    │
                      │   (DDoS protection)   │
                      └──────────┬────────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              │                  │                  │
         ┌────▼────┐       ┌────▼────┐       ┌─────▼─────┐
         │  Core   │       │ Member  │       │   Admin   │
         │  Node   │       │   API   │       │    VPN    │
         │ (XRPL)  │       │  Node   │       │           │
         │         │       │ (XRPL)  │       └─────┬─────┘
         │ Port:   │       │         │             │
         │ :5005   │       │ Port:   │             │
         │ :6006   │       │ :5006   │             │
         └─────────┘       │ :6007   │             │
                           └─────────┘             │
                                                   │
                           ┌─────────────────────────┘
                           │
                     ┌─────▼──────┐
                     │  Treasury  │
                     │    Node    │
                     │   (XRPL)   │
                     │            │
                     │  Private   │
                     │  RPC only  │
                     │  :5007     │
                     └─────┬──────┘
                           │
                ┌──────────┴──────────┐
                │   Internal Network  │
                │   (VPC, Private)    │
                ├─────────────────────┤
                │ - Backend services  │
                │ - PostgreSQL        │
                │ - Redis             │
                │ - HSM (warm keys)   │
                └─────────────────────┘
```

### Node Configuration

#### Core Node (Public Analytics)

```yaml
# rippled.cfg (simplified)
[server]
port_rpc_admin_local
port_peer
port_ws_admin_local

[port_rpc_admin_local]
port = 5005
ip = 0.0.0.0
admin = 127.0.0.1
protocol = http

[port_peer]
port = 51235
ip = 0.0.0.0
protocol = peer

[port_ws_admin_local]
port = 6006
ip = 0.0.0.0
admin = 127.0.0.1
protocol = ws

[node_size]
huge  # For analytics workloads

[database_path]
/var/lib/rippled/db

[historical_shard_path]
/var/lib/rippled/shards
```

**Purpose**: Heavy analytics queries, bot listeners, historical data access. Can be DDoS'd without affecting issuer operations.

---

#### Treasury Node (Private Operations)

```yaml
# rippled.cfg (simplified)
[server]
port_rpc_admin_local

[port_rpc_admin_local]
port = 5007
ip = 127.0.0.1  # localhost only
admin = 127.0.0.1
protocol = http

[node_size]
medium

# No public-facing ports
# No peer discovery (runs in cluster mode with Core/Member nodes)
```

**Purpose**: **ONLY** for issuer operations. Backend services connect via internal VPC. Keys stored in HSM accessible only from this node.

**Access Control**:
- VPN required
- IP whitelist (backend service IPs only)
- Multi-factor authentication for admin access
- Audit logging of all RPC calls

---

#### Member API Node (Public Client Access)

```yaml
# rippled.cfg (simplified)
[server]
port_rpc_admin_local
port_ws_public

[port_rpc_admin_local]
port = 5006
ip = 127.0.0.1
admin = 127.0.0.1
protocol = http

[port_ws_public]
port = 6007
ip = 0.0.0.0
protocol = ws

[node_size]
large  # Handle many client connections

[rate_limit]
account_info = 1000  # requests/second
submit = 100
```

**Purpose**: Client-facing WebSocket/RPC for wallet apps, member portals. Rate-limited per IP/wallet.

---

## EVM Control Plane

### Smart Contract Architecture

The EVM layer acts as a **policy enforcement engine** for XRPL operations. All contracts deployed on Ethereum/Polygon/Base (configurable).

```
┌───────────────────────────────────────────────────────────┐
│                   EVM Control Plane                        │
├───────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────┐     ┌──────────────────┐            │
│  │ ComplianceReg   │────▶│  MintGuard       │            │
│  │ (Whitelist)     │     │  (Mint/Burn)     │            │
│  └─────────────────┘     └────────┬─────────┘            │
│           │                       │                        │
│           │                       │                        │
│           ▼                       ▼                        │
│  ┌─────────────────┐     ┌──────────────────┐            │
│  │ MembershipNFT   │     │ ReserveRegistry  │            │
│  │ Registry        │     │ (PoR Tracking)   │            │
│  └─────────────────┘     └────────┬─────────┘            │
│                                   │                        │
│                          ┌────────▼─────────┐             │
│                          │  SystemGuard     │             │
│                          │  (Emergency      │             │
│                          │   Pause)         │             │
│                          └──────────────────┘             │
│                                                             │
└───────────────────────────────────────────────────────────┘
```

---

### Contract Specifications

#### 1. ComplianceRegistry.sol

**Purpose**: On-chain whitelist of approved wallets/addresses.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts-upgradeable/access/AccessControlUpgradeable.sol";
import "@openzeppelin/contracts-upgradeable/proxy/utils/UUPSUpgradeable.sol";

contract ComplianceRegistry is AccessControlUpgradeable, UUPSUpgradeable {
    bytes32 public constant COMPLIANCE_ROLE = keccak256("COMPLIANCE_ROLE");
    
    enum RiskTier { Unknown, Low, Medium, High, Blocked }
    
    struct CustomerRecord {
        bool whitelisted;
        RiskTier tier;
        bytes32 kycId;        // Off-chain KYC reference (hash)
        uint256 approvedAt;
        uint256 expiresAt;    // Optional KYC expiry
    }
    
    // XRPL address (string) or EVM address → Customer record
    mapping(address => CustomerRecord) public customers;
    mapping(bytes32 => address) public kycIdToAddress;
    
    event CustomerWhitelisted(
        address indexed customer,
        bytes32 indexed kycId,
        RiskTier tier,
        uint256 expiresAt
    );
    
    event CustomerBlocked(
        address indexed customer,
        bytes32 indexed kycId,
        string reason
    );
    
    function initialize() public initializer {
        __AccessControl_init();
        __UUPSUpgradeable_init();
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _grantRole(COMPLIANCE_ROLE, msg.sender);
    }
    
    function whitelistCustomer(
        address customer,
        bytes32 kycId,
        RiskTier tier,
        uint256 expiresAt
    ) external onlyRole(COMPLIANCE_ROLE) {
        require(tier != RiskTier.Blocked, "Use blockCustomer()");
        
        customers[customer] = CustomerRecord({
            whitelisted: true,
            tier: tier,
            kycId: kycId,
            approvedAt: block.timestamp,
            expiresAt: expiresAt
        });
        
        kycIdToAddress[kycId] = customer;
        
        emit CustomerWhitelisted(customer, kycId, tier, expiresAt);
    }
    
    function blockCustomer(
        address customer,
        bytes32 kycId,
        string calldata reason
    ) external onlyRole(COMPLIANCE_ROLE) {
        customers[customer].whitelisted = false;
        customers[customer].tier = RiskTier.Blocked;
        
        emit CustomerBlocked(customer, kycId, reason);
    }
    
    function isWhitelisted(address customer) external view returns (bool) {
        CustomerRecord memory record = customers[customer];
        if (!record.whitelisted) return false;
        if (record.tier == RiskTier.Blocked) return false;
        if (record.expiresAt > 0 && block.timestamp > record.expiresAt) return false;
        return true;
    }
    
    function riskTierOf(address customer) external view returns (RiskTier) {
        return customers[customer].tier;
    }
    
    function _authorizeUpgrade(address newImplementation)
        internal
        override
        onlyRole(DEFAULT_ADMIN_ROLE)
    {}
}
```

---

#### 2. MintGuard.sol

**Purpose**: Enforce mint/burn rules, rate limits, supply caps.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts-upgradeable/access/AccessControlUpgradeable.sol";
import "@openzeppelin/contracts-upgradeable/proxy/utils/UUPSUpgradeable.sol";
import "./interfaces/ISystemGuard.sol";
import "./interfaces/IReserveRegistry.sol";

contract MintGuard is AccessControlUpgradeable, UUPSUpgradeable {
    bytes32 public constant OPERATOR_ROLE = keccak256("OPERATOR_ROLE");
    
    ISystemGuard public systemGuard;
    IReserveRegistry public reserveRegistry;
    
    uint256 public globalCap;           // Max total supply
    uint256 public dailyMintLimit;      // Max mints per day
    uint256 public totalNetMinted;      // Current net supply (minted - burned)
    
    uint256 public dailyMintedToday;
    uint256 public lastDayReset;
    
    event MintApproved(
        address indexed operator,
        uint256 amount,
        bytes32 reasonCode,
        uint256 timestamp
    );
    
    event MintExecuted(
        address indexed operator,
        uint256 amount,
        string xrplTxHash,
        uint256 timestamp
    );
    
    event BurnRecorded(
        address indexed operator,
        uint256 amount,
        string xrplTxHash,
        uint256 timestamp
    );
    
    function initialize(
        address _systemGuard,
        address _reserveRegistry,
        uint256 _globalCap,
        uint256 _dailyMintLimit
    ) public initializer {
        __AccessControl_init();
        __UUPSUpgradeable_init();
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _grantRole(OPERATOR_ROLE, msg.sender);
        
        systemGuard = ISystemGuard(_systemGuard);
        reserveRegistry = IReserveRegistry(_reserveRegistry);
        globalCap = _globalCap;
        dailyMintLimit = _dailyMintLimit;
        lastDayReset = block.timestamp / 1 days;
    }
    
    function canMint(uint256 amount) external view returns (bool, string memory) {
        if (systemGuard.isPaused()) {
            return (false, "SYSTEM_PAUSED");
        }
        
        if (totalNetMinted + amount > globalCap) {
            return (false, "EXCEEDS_GLOBAL_CAP");
        }
        
        uint256 maxAllowed = reserveRegistry.maxAllowedSupply();
        if (totalNetMinted + amount > maxAllowed) {
            return (false, "EXCEEDS_RESERVE_CAP");
        }
        
        // Reset daily counter if new day
        uint256 currentDay = block.timestamp / 1 days;
        uint256 todayMinted = (currentDay == lastDayReset) ? dailyMintedToday : 0;
        
        if (todayMinted + amount > dailyMintLimit) {
            return (false, "EXCEEDS_DAILY_LIMIT");
        }
        
        return (true, "OK");
    }
    
    function requestMint(
        uint256 amount,
        bytes32 reasonCode
    ) external onlyRole(OPERATOR_ROLE) {
        (bool allowed, string memory reason) = this.canMint(amount);
        require(allowed, reason);
        
        // Update daily counter
        uint256 currentDay = block.timestamp / 1 days;
        if (currentDay != lastDayReset) {
            dailyMintedToday = 0;
            lastDayReset = currentDay;
        }
        dailyMintedToday += amount;
        
        emit MintApproved(msg.sender, amount, reasonCode, block.timestamp);
    }
    
    function confirmMint(
        uint256 amount,
        string calldata xrplTxHash
    ) external onlyRole(OPERATOR_ROLE) {
        totalNetMinted += amount;
        
        emit MintExecuted(msg.sender, amount, xrplTxHash, block.timestamp);
    }
    
    function recordBurn(
        uint256 amount,
        string calldata xrplTxHash
    ) external onlyRole(OPERATOR_ROLE) {
        require(totalNetMinted >= amount, "UNDERFLOW");
        totalNetMinted -= amount;
        
        emit BurnRecorded(msg.sender, amount, xrplTxHash, block.timestamp);
    }
    
    function _authorizeUpgrade(address newImplementation)
        internal
        override
        onlyRole(DEFAULT_ADMIN_ROLE)
    {}
}
```

---

#### 3. ReserveRegistry.sol

**Purpose**: Track USD reserves, provide `maxAllowedSupply()` for MintGuard.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts-upgradeable/access/AccessControlUpgradeable.sol";
import "@openzeppelin/contracts-upgradeable/proxy/utils/UUPSUpgradeable.sol";

contract ReserveRegistry is AccessControlUpgradeable, UUPSUpgradeable {
    bytes32 public constant ORACLE_ROLE = keccak256("ORACLE_ROLE");
    
    struct Reserve {
        uint256 amountUsd;    // Amount in USD (scaled by 1e6 for 6 decimals)
        uint256 lastUpdated;
        string source;        // "BANK_ACCOUNT_A", "T_BILLS", etc.
    }
    
    mapping(bytes32 => Reserve) public reserves;  // assetId => Reserve
    bytes32[] public assetIds;
    
    event ReserveUpdated(
        bytes32 indexed assetId,
        uint256 amountUsd,
        string source,
        uint256 timestamp
    );
    
    function initialize() public initializer {
        __AccessControl_init();
        __UUPSUpgradeable_init();
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _grantRole(ORACLE_ROLE, msg.sender);
    }
    
    function updateReserve(
        bytes32 assetId,
        uint256 amountUsd,
        string calldata source
    ) external onlyRole(ORACLE_ROLE) {
        if (reserves[assetId].lastUpdated == 0) {
            assetIds.push(assetId);
        }
        
        reserves[assetId] = Reserve({
            amountUsd: amountUsd,
            lastUpdated: block.timestamp,
            source: source
        });
        
        emit ReserveUpdated(assetId, amountUsd, source, block.timestamp);
    }
    
    function totalReservesUsd() external view returns (uint256) {
        uint256 total = 0;
        for (uint256 i = 0; i < assetIds.length; i++) {
            total += reserves[assetIds[i]].amountUsd;
        }
        return total;
    }
    
    function maxAllowedSupply() external view returns (uint256) {
        // Simple 1:1 backing: supply cannot exceed reserves
        // (Scaled by 1e6 to match USD decimals)
        return this.totalReservesUsd();
    }
    
    function _authorizeUpgrade(address newImplementation)
        internal
        override
        onlyRole(DEFAULT_ADMIN_ROLE)
    {}
}
```

---

#### 4. SystemGuard.sol

**Purpose**: Circuit breaker, global pause/unpause.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts-upgradeable/access/AccessControlUpgradeable.sol";
import "@openzeppelin/contracts-upgradeable/proxy/utils/UUPSUpgradeable.sol";

contract SystemGuard is AccessControlUpgradeable, UUPSUpgradeable {
    bytes32 public constant GUARDIAN_ROLE = keccak256("GUARDIAN_ROLE");
    
    bool private _paused;
    
    event Paused(address indexed by, uint256 timestamp, string reason);
    event Unpaused(address indexed by, uint256 timestamp);
    
    function initialize() public initializer {
        __AccessControl_init();
        __UUPSUpgradeable_init();
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _grantRole(GUARDIAN_ROLE, msg.sender);
        _paused = false;
    }
    
    function isPaused() external view returns (bool) {
        return _paused;
    }
    
    function pause(string calldata reason) external onlyRole(GUARDIAN_ROLE) {
        require(!_paused, "ALREADY_PAUSED");
        _paused = true;
        emit Paused(msg.sender, block.timestamp, reason);
    }
    
    function unpause() external onlyRole(GUARDIAN_ROLE) {
        require(_paused, "NOT_PAUSED");
        _paused = false;
        emit Unpaused(msg.sender, block.timestamp);
    }
    
    function _authorizeUpgrade(address newImplementation)
        internal
        override
        onlyRole(DEFAULT_ADMIN_ROLE)
    {}
}
```

---

### Contract Deployment

```bash
# Deploy to Polygon (example)
forge create --rpc-url $POLYGON_RPC \
    --private-key $DEPLOYER_KEY \
    --constructor-args \
    src/SystemGuard.sol:SystemGuard

forge create --rpc-url $POLYGON_RPC \
    --private-key $DEPLOYER_KEY \
    --constructor-args \
    src/ReserveRegistry.sol:ReserveRegistry

# Deploy proxies (UUPS pattern)
# Initialize with multi-sig as admin (Gnosis Safe recommended)
```

---

## Service Layer Architecture

### 5-Service Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                    Backend Services                           │
├──────────────────────────────────────────────────────────────┤
│                                                                │
│  1. XRPL Core API                                             │
│     - Direct node interface (Payment, Trustline, NFT)         │
│     - Internal only (VPN)                                     │
│     - FastAPI/Express.js                                      │
│                                                                │
│  2. Compliance & KYC Service                                  │
│     - Customer verification (Sumsub/Onfido integration)       │
│     - Sanctions screening (OFAC, EU, UN)                      │
│     - Risk scoring (Low/Medium/High)                          │
│     - PostgreSQL: customers, kyc_verifications, risk_profiles │
│                                                                │
│  3. Membership / NFT Service                                  │
│     - NFT minting/burning (XRPL NFTs)                         │
│     - Wallet access control (tier-based limits)               │
│     - PostgreSQL: wallets, membership_nfts, access_flags      │
│                                                                │
│  4. Treasury & Token Service                                  │
│     - Bank-to-XRPL bridge                                     │
│     - FTHUSD/USDF supply management                           │
│     - Reconciliation (bank vs. XRPL)                          │
│     - PostgreSQL: fiat_accounts, token_issuances, balances    │
│                                                                │
│  5. Bank Gateway Service                                      │
│     - US bank integration (Plaid / Synapse / direct API)      │
│     - Wire/ACH tracking (in/out)                              │
│     - Mint/redeem triggers                                    │
│     - PostgreSQL: fiat_transactions, reconciliations          │
│                                                                │
└──────────────────────────────────────────────────────────────┘
```

---

## Data Models

### PostgreSQL Schema

#### Identity & KYC

```sql
-- customers table
CREATE TABLE customers (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    type VARCHAR(50) NOT NULL CHECK (type IN ('individual', 'entity')),
    legal_name VARCHAR(255) NOT NULL,
    dob DATE,  -- For individuals
    registration_number VARCHAR(100),  -- For entities
    country_code CHAR(2) NOT NULL,
    email VARCHAR(255),
    phone VARCHAR(50),
    status VARCHAR(50) DEFAULT 'active' CHECK (status IN ('active', 'suspended', 'closed')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- kyc_verifications table
CREATE TABLE kyc_verifications (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    customer_id UUID NOT NULL REFERENCES customers(id),
    provider VARCHAR(50) NOT NULL,  -- 'sumsub', 'onfido', etc.
    verification_id VARCHAR(255),   -- Provider's verification ID
    status VARCHAR(50) NOT NULL CHECK (status IN ('pending', 'approved', 'rejected', 'expired')),
    risk_score NUMERIC(5,2),
    pep_flag BOOLEAN DEFAULT FALSE,
    sanctions_flag BOOLEAN DEFAULT FALSE,
    submitted_at TIMESTAMP WITH TIME ZONE,
    completed_at TIMESTAMP WITH TIME ZONE,
    expires_at TIMESTAMP WITH TIME ZONE,
    rejection_reason TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- wallets table
CREATE TABLE wallets (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    customer_id UUID NOT NULL REFERENCES customers(id),
    xrpl_address VARCHAR(50) NOT NULL UNIQUE,
    label VARCHAR(100) DEFAULT 'primary',
    status VARCHAR(50) DEFAULT 'active' CHECK (status IN ('active', 'suspended', 'closed')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_wallets_customer ON wallets(customer_id);
CREATE INDEX idx_wallets_xrpl_address ON wallets(xrpl_address);
```

#### NFTs & Access

```sql
-- membership_nfts table
CREATE TABLE membership_nfts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    wallet_id UUID NOT NULL REFERENCES wallets(id),
    xrpl_nft_id VARCHAR(100) NOT NULL UNIQUE,
    tier VARCHAR(50) NOT NULL CHECK (tier IN ('basic', 'pro', 'otc', 'internal')),
    status VARCHAR(50) DEFAULT 'active' CHECK (status IN ('active', 'revoked', 'expired')),
    issued_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    expires_at TIMESTAMP WITH TIME ZONE,
    metadata_uri TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- node_access_nfts table (optional, for future)
CREATE TABLE node_access_nfts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    wallet_id UUID NOT NULL REFERENCES wallets(id),
    xrpl_nft_id VARCHAR(100) NOT NULL UNIQUE,
    plan VARCHAR(50) NOT NULL CHECK (plan IN ('infra-basic', 'infra-premium')),
    status VARCHAR(50) DEFAULT 'active',
    issued_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    expires_at TIMESTAMP WITH TIME ZONE
);
```

#### Fiat & Token Ledgers

```sql
-- fiat_accounts table
CREATE TABLE fiat_accounts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    account_name VARCHAR(255) NOT NULL,
    bank_name VARCHAR(255) NOT NULL,
    account_number_masked VARCHAR(50),  -- Last 4 digits only
    account_type VARCHAR(50) CHECK (account_type IN ('operating', 'reserve')),
    currency CHAR(3) DEFAULT 'USD',
    status VARCHAR(50) DEFAULT 'active',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- fiat_transactions table
CREATE TABLE fiat_transactions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    fiat_account_id UUID NOT NULL REFERENCES fiat_accounts(id),
    direction VARCHAR(10) NOT NULL CHECK (direction IN ('in', 'out')),
    amount NUMERIC(18,6) NOT NULL,
    currency CHAR(3) DEFAULT 'USD',
    bank_reference VARCHAR(255),
    customer_id UUID REFERENCES customers(id),
    status VARCHAR(50) DEFAULT 'pending' CHECK (status IN ('pending', 'confirmed', 'failed')),
    value_date DATE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    confirmed_at TIMESTAMP WITH TIME ZONE
);

-- token_issuances table
CREATE TABLE token_issuances (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    asset VARCHAR(20) NOT NULL CHECK (asset IN ('FTHUSD', 'USDF')),
    direction VARCHAR(10) NOT NULL CHECK (direction IN ('mint', 'burn')),
    amount NUMERIC(18,6) NOT NULL,
    xrpl_tx_hash VARCHAR(100) NOT NULL,
    issuer_account VARCHAR(50) NOT NULL,
    wallet_id UUID REFERENCES wallets(id),
    linked_fiat_tx_id UUID REFERENCES fiat_transactions(id),
    reason_code VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- token_balances_offchain table (cached from XRPL)
CREATE TABLE token_balances_offchain (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    wallet_id UUID NOT NULL REFERENCES wallets(id),
    asset VARCHAR(20) NOT NULL,
    balance NUMERIC(18,6) NOT NULL DEFAULT 0,
    last_synced_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE(wallet_id, asset)
);
```

---

## Integration Flows

### Flow 1: Customer Onboarding (KYC)

```
┌────────────┐
│   Client   │
│  (Portal)  │
└──────┬─────┘
       │ 1. Submit KYC docs
       ▼
┌────────────────┐
│  Compliance    │
│  & KYC Service │
└───────┬────────┘
        │ 2. Forward to Sumsub/Onfido
        ▼
┌────────────────┐
│  KYC Provider  │
│  (Sumsub)      │
└───────┬────────┘
        │ 3. Verification complete (webhook)
        ▼
┌────────────────┐
│  Compliance    │
│  Service       │
│  - Store result│
│  - Risk score  │
└───────┬────────┘
        │ 4. If approved: call ComplianceRegistry.whitelistCustomer()
        ▼
┌────────────────┐
│ ComplianceReg  │
│ (EVM contract) │
└───────┬────────┘
        │ 5. Emit CustomerWhitelisted event
        ▼
┌────────────────┐
│  Membership    │
│  NFT Service   │
│  - Mint NFT    │
└───────┬────────┘
        │ 6. Mint KYC Membership NFT on XRPL (via Treasury Node)
        ▼
┌────────────────┐
│  XRPL (NFT)    │
│  - NFT minted  │
│  - Wallet now  │
│    "KYC'd"     │
└────────────────┘
```

---

### Flow 2: Mint FTHUSD (USD → XRPL)

```
┌────────────┐
│   Client   │
│ (Wire USD) │
└──────┬─────┘
       │ 1. Wire $X to US bank account
       ▼
┌────────────────┐
│  US Bank       │
│  (Reserve Acc) │
└───────┬────────┘
        │ 2. Credit appears in account
        ▼
┌────────────────┐
│  Bank Gateway  │
│  Service       │
│  - Poll bank   │
│  - Log fiat_tx │
└───────┬────────┘
        │ 3. Notify Treasury Service
        ▼
┌────────────────┐
│  Treasury &    │
│  Token Service │
└───────┬────────┘
        │ 4. Check ComplianceRegistry.isWhitelisted(customer)
        ▼
┌────────────────┐
│ ComplianceReg  │
│ (EVM)          │
└───────┬────────┘
        │ 5. If whitelisted: check MintGuard.canMint(amount)
        ▼
┌────────────────┐
│  MintGuard     │
│  (EVM)         │
│  - Check caps  │
│  - Check PoR   │
└───────┬────────┘
        │ 6. If approved: call requestMint() → emit MintApproved
        ▼
┌────────────────┐
│  Mint Bot      │
│  (Listener)    │
└───────┬────────┘
        │ 7. Read MintApproved event from EVM
        │ 8. Submit XRPL Payment: FTHUSD_Issuer → Customer wallet
        ▼
┌────────────────┐
│  Treasury Node │
│  (XRPL)        │
│  - Sign tx     │
│  - Submit      │
└───────┬────────┘
        │ 9. Wait for validation
        ▼
┌────────────────┐
│  XRPL Ledger   │
│  - Payment     │
│    validated   │
└───────┬────────┘
        │ 10. Mint bot calls MintGuard.confirmMint(amount, txHash)
        ▼
┌────────────────┐
│  MintGuard     │
│  (EVM)         │
│  - Increment   │
│    totalNet    │
│    Minted      │
└───────┬────────┘
        │ 11. Log token_issuance in PostgreSQL
        ▼
┌────────────────┐
│  Treasury      │
│  Service       │
│  - Update DB   │
└────────────────┘
```

---

### Flow 3: Burn/Redeem FTHUSD (XRPL → USD)

```
┌────────────┐
│   Client   │
└──────┬─────┘
       │ 1. Request redemption in portal
       ▼
┌────────────────┐
│  Treasury      │
│  Service       │
│  - Check KYC   │
│  - Check limits│
└───────┬────────┘
        │ 2. Show XRPL redemption address
        ▼
┌────────────┐
│   Client   │
│  (XRPL tx) │
└──────┬─────┘
       │ 3. Send FTHUSD to Redemption_Wallet
       ▼
┌────────────────┐
│  Burn Bot      │
│  (Listener)    │
└───────┬────────┘
        │ 4. Detect inbound payment to Redemption_Wallet
        │ 5. Burn FTHUSD (Payment back to Issuer)
        ▼
┌────────────────┐
│  Treasury Node │
│  (XRPL)        │
└───────┬────────┘
        │ 6. Burn validated on XRPL
        │ 7. Call MintGuard.recordBurn(amount, txHash)
        ▼
┌────────────────┐
│  MintGuard     │
│  (EVM)         │
│  - Decrement   │
│    totalNet    │
│    Minted      │
└───────┬────────┘
        │ 8. Notify Bank Gateway to send USD
        ▼
┌────────────────┐
│  Bank Gateway  │
│  Service       │
│  - Initiate    │
│    wire/ACH    │
└───────┬────────┘
        │ 9. USD sent to customer's bank
        ▼
┌────────────────┐
│  US Bank       │
│  (Customer's)  │
└────────────────┘
```

---

## Security Architecture

### Multi-Sig Configuration

| Operation | Multi-Sig Requirement | Threshold | Key Holders |
|-----------|----------------------|-----------|-------------|
| Issuer key (FTHUSD, USDF) | Cold storage, 3-of-5 | 3 | CEO, CFO, COO, Head of Compliance, CISO |
| Treasury key (FTHUSD_Treasury) | Warm storage, 2-of-3 | 2 | Treasury Ops, CFO, COO |
| EVM contract admin (upgrade) | Gnosis Safe, 3-of-5 | 3 | CEO, CTO, CISO, Head of Compliance, External Advisor |
| EVM Guardian (pause) | Gnosis Safe, 2-of-3 | 2 | CEO, CTO, CISO |
| EVM Compliance (whitelist) | 1-of-2 | 1 | Head of Compliance, Compliance Analyst |

### Key Storage

```
┌───────────────────────────────────────────────────────────┐
│                   Key Management Topology                  │
├───────────────────────────────────────────────────────────┤
│                                                             │
│  COLD STORAGE (Air-Gapped, Hardware Wallets)              │
│  ├─ FTHUSD_Issuer Master Key (3-of-5 multi-sig)          │
│  ├─ USDF_Issuer Master Key (3-of-5 multi-sig)            │
│  └─ EVM Contract Admin Key (Gnosis Safe, 3-of-5)         │
│                                                             │
│  WARM STORAGE (Online HSM, Treasury Node Only)            │
│  ├─ FTHUSD_Treasury Key (2-of-3 multi-sig)               │
│  ├─ USDF_Treasury Key (2-of-3 multi-sig)                 │
│  └─ Redemption_Wallet Key (2-of-3 multi-sig)             │
│                                                             │
│  HOT STORAGE (Backend Services, Encrypted at Rest)        │
│  ├─ Bot wallet keys (for listening, not signing)         │
│  ├─ API keys (KYC providers, analytics)                  │
│  └─ Database encryption keys (AWS KMS)                    │
│                                                             │
└───────────────────────────────────────────────────────────┘
```

### Network Security

- **VPC Isolation**: All internal services in private subnets (no direct internet access)
- **VPN Required**: All admin access via VPN + MFA
- **IP Whitelist**: Treasury Node RPC accessible only from backend service IPs
- **DDoS Protection**: CloudFlare (or AWS Shield Advanced) on public-facing nodes
- **Rate Limiting**: Per-IP, per-wallet limits on Member API Node
- **TLS Everywhere**: All RPC/WebSocket traffic over TLS 1.3
- **Secrets Management**: AWS Secrets Manager or HashiCorp Vault

---

## Deployment Strategy

### Infrastructure as Code (Terraform)

```hcl
# main.tf (simplified)
module "xrpl_core_node" {
  source = "./modules/xrpl-node"
  
  node_name    = "core-node"
  instance_type = "c5.4xlarge"
  node_size    = "huge"
  public_facing = true
  enable_shards = true
}

module "xrpl_treasury_node" {
  source = "./modules/xrpl-node"
  
  node_name    = "treasury-node"
  instance_type = "c5.2xlarge"
  node_size    = "medium"
  public_facing = false  # VPN only
  enable_hsm   = true
}

module "xrpl_member_node" {
  source = "./modules/xrpl-node"
  
  node_name    = "member-node"
  instance_type = "c5.2xlarge"
  node_size    = "large"
  public_facing = true
  rate_limit    = true
}

module "evm_control_plane" {
  source = "./modules/evm-contracts"
  
  chain_id = 137  # Polygon
  deployer_key = var.deployer_key
  multi_sig_address = var.gnosis_safe_address
}

module "backend_services" {
  source = "./modules/backend"
  
  services = [
    "xrpl-core-api",
    "compliance-kyc",
    "membership-nft",
    "treasury-token",
    "bank-gateway"
  ]
  
  database_url = module.rds_postgres.connection_string
  redis_url    = module.elasticache_redis.endpoint
}
```

### CI/CD Pipeline

```yaml
# .github/workflows/deploy.yml
name: Deploy to Production

on:
  push:
    branches: [main]
    paths:
      - 'backend/**'
      - 'contracts/**'
      - 'terraform/**'

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run unit tests
        run: pytest tests/
      - name: Run contract tests
        run: forge test
  
  deploy-contracts:
    needs: test
    runs-on: ubuntu-latest
    if: contains(github.event.head_commit.message, '[deploy-contracts]')
    steps:
      - name: Deploy to Polygon
        run: forge script script/Deploy.s.sol --rpc-url $POLYGON_RPC --broadcast
  
  deploy-backend:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - name: Build Docker images
        run: docker-compose build
      - name: Push to ECR
        run: |
          aws ecr get-login-password | docker login --username AWS --password-stdin $ECR_REGISTRY
          docker-compose push
      - name: Deploy to ECS
        run: terraform apply -auto-approve
```

---

## Scalability & Performance

### Performance Targets

| Metric | Target | Current | Strategy |
|--------|--------|---------|----------|
| **XRPL TPS** | 1,500 tx/s | ~50 tx/s (typical) | Horizontal scaling of Member API nodes |
| **Mint latency** | <30s end-to-end | N/A | Optimistic UX, background processing |
| **KYC onboarding** | <24h | N/A | Auto-approval for low-risk, parallel verification |
| **Database writes** | 10,000/s | N/A | PostgreSQL with read replicas, write sharding |
| **API response time** | <200ms p95 | N/A | Redis caching, CDN for static assets |

### Scaling Strategy

- **XRPL Nodes**: Add more Member API nodes behind load balancer as read traffic grows
- **Backend Services**: Containerized (ECS/Kubernetes), auto-scaling based on CPU/memory
- **Database**: Primary-replica setup, consider Aurora PostgreSQL for automatic scaling
- **Redis**: ElastiCache cluster mode for distributed caching
- **EVM Contracts**: No scaling needed (L2 gas is cheap); use batch operations where possible

---

## Summary

This architecture provides:

✅ **3-node XRPL topology** with clear separation of concerns (analytics, operations, client access)  
✅ **EVM control plane** enforcing mathematical invariants and safety constraints  
✅ **Multi-layer security** (cold/warm keys, VPN, HSM, multi-sig everywhere)  
✅ **Compliance-first data models** (KYC, wallets, fiat transactions, audit logs)  
✅ **End-to-end mint/burn flows** bridging US banks → EVM → XRPL  
✅ **Production-ready infrastructure** (Terraform, CI/CD, monitoring)

This is the architecture you show to engineers, CTOs, and technical due diligence teams.

---

**Document Version**: 1.0  
**Last Updated**: November 17, 2025  
**Owner**: Engineering & Architecture Team  
**Review Cycle**: Quarterly or when major changes occur

---

For questions or technical discussions, open an issue on GitHub or contact: engineering@[domain].com
