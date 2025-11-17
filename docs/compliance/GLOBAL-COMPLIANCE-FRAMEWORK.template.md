# [COMPANY / PLATFORM NAME]  
## GLOBAL COMPLIANCE, SECURITY & REGULATORY FRAMEWORK

**Version:** 1.0  
**Last Updated:** [DATE]  
**Approved By:** [BOARD / CEO / COMPLIANCE COMMITTEE]

---

## 0. DOCUMENT MAP

This document sits above and references:

- `KYC-AML-PROGRAM-[VERSION].md`
- `ASSET-REGULATORY-PROFILE-[ASSET].md` (one per asset)
- `SECURITY-CONTROLS-[SCOPE].md`
- `JURISDICTION-ANNEX-[COUNTRY/REGION].md`
- `ISSUER-WALLET-CREATION-GUIDE.md`
- `PROOF-OF-RESERVES-POLICY.md`
- `MINT-BURN-WORKFLOWS.md`

---

## 1. SCOPE & PURPOSE

This Framework defines how **[COMPANY]**:

- Onboards and monitors customers and counterparties  
- Issues, redeems, and manages digital assets (including stablecoins / RWAs)  
- Uses third-party providers for KYC, AML, Travel Rule, analytics, and oracles  
- Applies security controls to infrastructure and keys  
- Classifies tokens under securities / e-money / payment / VASP regimes by jurisdiction

This applies to:

- All products and protocols under the **[PLATFORM NAME]**  
- All entities in the **[GROUP NAME]** involved in issuance, custody, or exchange  
- All employees, officers, contractors, and key third parties

---

## 2. THIRD-PARTY PROVIDERS & RESPONSIBILITIES

### 2.1 KYC / KYB / IDENTITY PROVIDERS

**Purpose:** Verify identity of individuals and entities; run sanctions, PEP, and document checks.

- Primary provider: `[NAME – e.g., Sumsub / Onfido / Veriff / Trulioo / Persona / Socure]`
- Backup / regional providers (if any): `[LIST]`
- Services used:
  - [ ] Individual KYC (ID + selfie + liveness)
  - [ ] Corporate KYB (registry checks, UBOs)
  - [ ] PEP / sanctions screening
  - [ ] Adverse media / fraud flags

**Integration pattern:**

- Frontend → KYC provider workflow → callback / webhook → compliance decision stored in:
  - `[INTERNAL DB / COMPLIANCE REGISTRY / ON-CHAIN FLAG]`

### 2.2 BLOCKCHAIN ANALYTICS / WALLET RISK SCORING

**Purpose:** Detect high-risk counterparties, tainted funds, sanctions evasion, darknet flows.

- Providers: `[Chainalysis / Elliptic / TRM Labs / Crystal / etc.]`
- Scope:
  - [ ] Screening of all deposit addresses  
  - [ ] Continuous monitoring of treasury and issuer wallets  
  - [ ] Risk scoring for large outbound transfers / OTC deals

### 2.3 TRAVEL RULE & VASP-TO-VASP MESSAGING

**Purpose:** Comply with FATF Recommendation 16 (Travel Rule) and equivalent regimes.

- Providers: `[Notabene / 21 Analytics / Shyft / VerifyVASP / TRISA / internal]`
- Trigger thresholds: `[AMOUNT + CONDITIONS]`
- Data exchanged:
  - Originator name, account, address (where required)
  - Beneficiary name, account, VASP IDs

### 2.4 ORACLES & PROOF OF RESERVES

**Purpose:** Provide independent, on-chain attestation of reserves and external data.

- Oracle network: `[Chainlink / RedStone / API3 / Pyth / other]`
- Feeds used:
  - [ ] Proof of Reserves (PoR) for stablecoins / RWAs  
  - [ ] FX / price data for collateral valuation  
  - [ ] Other: `[DESCRIPTION]`

**Control objective:**

> Enforce at protocol level: `TotalSupply(ASSET) <= ReportedReserves(ASSET)` from oracle feed, where legally and technically feasible.

### 2.5 LEGAL / AUDIT & COMPLIANCE ADVISORS

- Global / regional law firms: `[LIST]`
- Audit / assurance firms: `[LIST]`
- Role:
  - Licensing / registration strategy  
  - Opinions on token classification  
  - Independent reviews of reserves, controls, and disclosures

---

## 3. KYC / AML PROGRAM LINKAGE

[Short pointer into your separate KYC/AML document.]

- Master policy: `KYC-AML-PROGRAM-[VERSION].md`
- Alignment:
  - FATF Recommendations (esp. 10, 15, 16)  
  - Local AML/CTF and sanctions laws in **[LIST CORE JURISDICTIONS]**
- Key decisions:
  - Customer risk tiers: `[LOW / MEDIUM / HIGH]`  
  - EDD triggers: `[PEP, high-risk jurisdiction, complex structures, etc.]`  
  - Transaction monitoring thresholds and logic: `[SUMMARY]`  

---

## 4. ASSET-LEVEL REGULATORY PROFILES

Each issued or supported asset has its own profile using:

- Template: `ASSET-REGULATORY-PROFILE.template.md`
- Files:  
  - `ASSET-REGULATORY-PROFILE-[FTHUSD].md`  
  - `ASSET-REGULATORY-PROFILE-[USDF].md`  
  - `ASSET-REGULATORY-PROFILE-[GOLD].md`  
  - `ASSET-REGULATORY-PROFILE-[WATER].md`  
  - etc.

Each profile must cover at minimum:

- Legal nature & rights  
- Backing & reserve model  
- Issuance & redemption rules  
- KYC/AML requirements per asset  
- Jurisdiction-specific classification (security / e-money / payment / other)

### 4.1 FTHUSD – Treasury / Institutional Rail

- **Type:** USD-backed institutional stablecoin (XRPL IOU)
- **Jurisdiction:** US-only at launch
- **Backed by:** USD in US banks (segregated reserve/operating accounts)
- **Users:**
  - Internal entities
  - KYC-approved institutional/wholesale customers
- **Controls:**
  - Full KYC/KYB
  - AML + sanctions screening
  - FTHUSD supply linked to PoR reserves via MintGuard invariants
  - Mint/burn only via **Treasury Node**

### 4.2 USDF – Client-Facing Rail

- **Type:** USD-linked client rail / payment & utility token (XRPL IOU)
- **Backed by:** FTHUSD held in vault OR directly by USD
- **Users:**
  - KYC'd members with Membership NFTs
  - Used for balances, fees, rewards, platform payments
- **Controls:**
  - No USDF issuance to wallets without Membership NFT
  - Limits per tier: `basic` (low caps) | `pro` (higher caps) | `otc` (very high caps with manual review)
  - Redemptions always ultimately go back to USD in US banks

---

## 5. SECURITY & TECHNICAL CONTROLS

### 5.1 KEY MANAGEMENT

- Key storage:
  - [ ] HSM  
  - [ ] Hardware wallets  
  - [ ] MPC  
- Key types and policies:
  - Issuer keys: `[MULTISIG / MPC; MIN SIGNERS; ROTATION POLICY]`
  - Treasury keys: `[THRESHOLDS; DUAL CONTROL; WITHDRAW LIMITS]`
  - Admin / ops keys: `[SEGREGATED; LEAST PRIVILEGE]`

**Issuer Wallet Structure:**

| Key Type | Purpose | Custody | Multi-Sig Threshold |
|----------|---------|---------|---------------------|
| **FTHUSD_Issuer** | God key, defines IOU, sets flags | Cold storage (air-gapped HSM or hardware wallet) | [e.g., 3-of-5] |
| **USDF_Issuer** | Client rail issuer | Cold storage | [e.g., 3-of-5] |
| **FTHUSD_Treasury** | Day-to-day mint/burn/send | Warm storage (online HSM, Treasury Node only) | [e.g., 2-of-3] |
| **USDF_Treasury** | Client-facing operations | Warm storage (online HSM, Treasury Node only) | [e.g., 2-of-3] |
| **Redemption_Wallet** | Burns redeemed tokens | Warm storage | [e.g., 2-of-3] |
| **USDF_Back_Vault** | Holds FTHUSD backing USDF | Warm storage (monitored 24/7) | [e.g., 2-of-3] |

**Issuer Account Flags (XRPL):**

- `DefaultRipple`: OFF (unless pathfinding needed)
- `RequireAuth`: ON (must approve all trustlines)
- `RequireDest`: ON (require destination tag for safety)
- `Freeze/Clawback`: Only if documented policy exists

### 5.2 INFRASTRUCTURE SECURITY

**Node Topology (3-Node Fleet):**

1. **Core Node** – Analytics, bots, blockchain monitoring
   - Public-facing (rate-limited)
   - RPC `:5005`, WS `:6006`, Peer `:51235`
   - CloudFlare/AWS Shield for DDoS protection

2. **Treasury Node** – Issuer & treasury operations ONLY
   - **Private** (VPN + IP whitelist only)
   - Only accessed by:
     - Internal backend services
     - Authorized ops bots
     - Admin via VPN + MFA
   - Holds warm keys for FTHUSD_Treasury, USDF_Treasury

3. **Member API Node** – Client-facing reads, quotes, member wallets
   - Public-facing (rate-limited per IP/wallet)
   - Read-only operations for members
   - No issuer key access

**Network Segmentation:**

```
┌─────────────────────────────────────────────────────────────┐
│                     Public Internet                          │
└───────────────────────┬─────────────────────────────────────┘
                        │
                ┌───────▼───────┐
                │   CloudFlare  │ ← DDoS protection, rate limiting
                │   (or equiv)  │
                └───────┬───────┘
                        │
         ┌──────────────┴──────────────┐
         │                             │
    ┌────▼────┐                   ┌────▼────┐
    │  Core   │                   │ Member  │
    │  Node   │                   │   API   │
    └─────────┘                   │  Node   │
                                  └─────────┘
                                        │
                         ┌──────────────▼──────────────┐
                         │   Internal Network (VPN)    │
                         ├─────────────────────────────┤
                         │  - Treasury Node            │
                         │  - HSM (Warm Storage)       │
                         │  - Compliance Registry DB   │
                         │  - EVM Control Plane        │
                         │  - Bank Gateway Service     │
                         └─────────────────────────────┘
                                        │
                         ┌──────────────▼──────────────┐
                         │  Cold Storage Vault         │
                         │  (Offline, Air-Gapped)      │
                         │  - FTHUSD_Issuer Master Key │
                         │  - USDF_Issuer Master Key   │
                         └─────────────────────────────┘
```

**Controls:**

- Network segmentation (prod vs dev vs management)  
- VPN + MFA for all admin access  
- Regular OS and dependency patching  
- Secure secrets management: `[VAULT / KMS / OTHER]`

### 5.3 APPLICATION & SMART CONTRACT SECURITY

**EVM Control Plane (Smart Contracts):**

Contracts deployed on `[Ethereum / Polygon / Base]` as control layer for XRPL operations:

1. **ComplianceRegistry**
   - Purpose: On-chain whitelist of approved wallets
   - Key functions:
     - `isWhitelisted(address)` → bool
     - `riskTierOf(address)` → LOW | MEDIUM | HIGH | BLOCKED
     - `whitelistCustomer(...)` (admin only)
     - `blockCustomer(...)` (admin only)

2. **MintGuard (MintController)**
   - Purpose: Enforce mint/burn rules, rate limits, supply caps
   - Key functions:
     - `canMint(amount)` → bool (checks: globalCap, reserves, pause status)
     - `requestMint(amount, reasonCode)` → emits MintApproved event
     - `confirmMint(amount, xrplTxHash)` → logs executed mint
     - `recordBurn(amount, xrplTxHash)` → decreases totalNetMinted
   - Invariants enforced:
     - `totalNetMinted + amount <= globalCap`
     - `totalNetMinted + amount <= maxAllowedSupply(reserves)`
     - `!SystemGuard.isPaused()`

3. **ReserveRegistry / PoRGuard**
   - Purpose: Track USD reserves, enforce supply <= reserves
   - Key functions:
     - `getReserve(assetId)` → amount, lastUpdated
     - `totalReservesUsd()` → uint256
     - `updateReserve(assetId, amount)` (oracle or admin)
     - `maxAllowedSupply()` → totalReservesUsd * 1e6
   - Invariant: `FTHUSD_circulating <= USD_reserves_total`

4. **MembershipNFTRegistry** (optional)
   - Purpose: Mirror XRPL Membership NFTs into EVM for tier checks
   - Key functions:
     - `hasMembership(address)` → bool
     - `membershipTier(address)` → basic | pro | otc | internal

5. **SystemGuard / Guardian**
   - Purpose: Circuit breaker, emergency pause
   - Key functions:
     - `isPaused()` → bool
     - `pause()` (GUARDIAN_ROLE only)
     - `unpause()` (GUARDIAN_ROLE only)
   - All critical operations check: `require(!systemGuard.isPaused())`

**Integration Flow (XRPL ↔ EVM):**

```
USD in US Bank
    ↓
Bank Gateway logs fiat_transaction
    ↓
Treasury Service checks:
    - ComplianceRegistry.isWhitelisted(customer)
    - MintGuard.canMint(amount)
    ↓
If approved:
    - MintGuard.requestMint(amount, reason) → emits MintApproved
    ↓
XRPL Bot (on Treasury Node):
    - Reads MintApproved event
    - Submits XRPL Payment from FTHUSD_Issuer
    - Waits for validation
    - Calls MintGuard.confirmMint(amount, txHash)
    ↓
FTHUSD balance updated on XRPL
```

**Secure SDLC:**

- Code reviews  
- Static analysis and SAST  
- Dependency checking (SCA)

**Contract security:**

- [ ] Internal security review  
- [ ] External audit by `[AUDITOR NAME]`  
- [ ] Formal verification / property-based tests (where applicable)

**Critical invariants:**

- `totalSupply <= reserves`  
- No unauthorized mint/burn  
- No freezing / clawback outside defined policy (if implemented)

### 5.4 PENETRATION TESTING & VULNERABILITY MANAGEMENT

- External pen-test frequency: `[ANNUAL / BIANNUAL]`
- Scope: external APIs, admin interfaces, key management flows
- Vulnerability SLAs:
  - Critical: `[X] days`  
  - High: `[Y] days`  
  - Medium/Low: `[Z] days`  

### 5.5 INCIDENT RESPONSE

- Documented IR plan with:
  - Detection → triage → containment → eradication → recovery → lessons learned  
  - Roles and contact tree (SecOps, DevOps, Compliance, Legal)
  - Regulator and partner notification triggers per jurisdiction

---

## 6. PROOF OF RESERVES (PoR) POLICY

### 6.1 Reserve Sources

**For FTHUSD:**

- Reserves = sum of:
  - USD in US banks (operating + reserve accounts)
  - (Optional) Short-term U.S. Treasuries / MMFs

**For USDF:**

- Policy: USDF fully backed by FTHUSD held in `USDF_Back_Vault` wallet
- Invariant: `USDF_circulating <= FTHUSD_in_USDF_Back_Vault`

### 6.2 PoR Invariants

**Primary Rule:**

> At all times: `FTHUSD_circulating <= USD_reserves_total`

**Secondary Rule:**

> At all times: `USDF_circulating <= FTHUSD_in_USDF_Back_Vault`

Where:

- `FTHUSD_circulating` = total FTHUSD issued minus burns, net of USDF backing
- `USD_reserves_total` = sum of balances in designated US bank accounts

### 6.3 PoR Process (Operational)

**Daily (US business days):**

1. Pull bank balances from US banks (portal export, API, or manual)
2. Log to `fiat_accounts` + `fiat_transactions` tables
3. Update `ReserveRegistry` on EVM (if using smart contract pattern)
4. Pull FTHUSD + USDF supply from XRPL via Core Node
5. Run reconciliation script:
   - Check: `FTHUSD_supply <= USD_reserves`
   - Check: `USDF_supply <= FTHUSD_in_back_vault`
   - If invariant fails:
     - Automatically trigger `SystemGuard.pause()` (mint blocked)
     - Human review required

**Monthly:**

- Export bank statements and on-chain ledger snapshots
- Generate PoR report: "On date T, FTHUSD supply = X, reserves = X+ε"
- Store report in internal archive (IPFS later)

**Quarterly/Annual:**

- Independent auditor reviews:
  - Bank balances vs. XRPL supply
  - Reconciliation methodology
  - Reserve custody arrangements

---

## 7. MINT / BURN WORKFLOWS

### 7.1 Mint FTHUSD (USD → FTHUSD on XRPL)

**Workflow:**

1. **USD In:** Customer wires $X to US bank account
   - Bank Gateway logs: amount, sender, reference, value date

2. **KYC / Whitelist Check:**
   - Confirm customer:
     - Is KYC-approved (status in `customers` + `kyc_verifications` tables)
     - Is US-based (for now)
     - Has Membership NFT (KYC membership)
   - ComplianceRegistry check: `isWhitelisted(customerProxy) == true`
   - Risk tier not `BLOCKED`

3. **PoR & MintGuard Check:**
   - Update ReserveRegistry with new USD amount
   - Call MintGuard.canMint(amountFTHUSD):
     - Checks: `totalNetMinted + amount <= globalCap`
     - Checks: `totalNetMinted + amount <= maxAllowedSupply(reserves)`
     - Checks: `!SystemGuard.isPaused()`

4. **Record Intent (On-Chain):**
   - Call `MintGuard.requestMint(amount, reasonCode)`
   - Event emitted: `MintApproved`

5. **XRPL Mint (Treasury Node Only):**
   - Mint bot reads `MintApproved` events
   - On **Treasury Node**:
     - Submit XRPL Payment from `FTHUSD_Issuer` to `FTHUSD_Treasury` (or client wallet)
     - Wait for validated ledger
     - Call `MintGuard.confirmMint(amount, xrplTxHash)`

6. **Optional: Convert to USDF:**
   - Move FTHUSD into `USDF_Back_Vault`
   - Issue USDF from `USDF_Issuer` to client wallet via Treasury Node
   - Log USDF issuance in `token_issuances` table

### 7.2 Burn / Redeem FTHUSD (FTHUSD → USD back to bank)

**Workflow:**

1. **Client Redemption Request:**
   - Client submits request in portal: "Redeem X FTHUSD to USD"
   - System checks:
     - KYC still valid
     - No sanctions triggers
     - Within daily/monthly limits

2. **Client Sends FTHUSD to Redemption Wallet:**
   - App shows XRPL address for `FTHUSD_Redemption`
   - Client sends X FTHUSD to that address

3. **XRPL Confirmation:**
   - Bot watches for inbound Payment to `FTHUSD_Redemption`
   - When validated:
     - Burn FTHUSD (Payment back to Issuer or canonical burn)
     - Call `MintGuard.recordBurn(amount, xrplTxHash)`

4. **Bank Payout:**
   - Treasury Service instructs US bank to send USD to customer's verified account
   - Bank Gateway logs outgoing wire/ACH in `fiat_transactions`

5. **Reconciliation:**
   - `totalNetMinted` drops in MintGuard
   - XRPL FTHUSD supply drops
   - USD reserves drop by X

**Same Pattern for USDF:**

- USDF → FTHUSD internal swap (if needed)
- FTHUSD → USD bank payout

---

## 8. MEMBERSHIP NFTs & ACCESS CONTROL

### 8.1 NFT Types

**1. KYC Membership NFT** (v1 – required)

- Purpose: Proves wallet belongs to KYC'd participant
- Minted after:
  - KYC approved
  - US residency / entity confirmed
- Required for:
  - Having trustlines to FTHUSD/USDF
  - Receiving FTHUSD/USDF from treasury

**2. Node Access NFT** (v2 – optional)

- Purpose: Proves access to private XRPL endpoint
- Use case: Family offices / partners get premium infra access

**3. OTC Tier NFT** (v2+ – optional)

- Purpose: Mark wallets authorized for large block trades, special limits

### 8.2 NFT Metadata Template

```json
{
  "type": "membership",
  "tier": "basic",        // "basic" | "pro" | "otc" | "internal"
  "kyc_status": "approved",
  "jurisdiction": "US",
  "issued_by": "[COMPANY NAME]",
  "issued_at": "2025-11-17T00:00:00Z",
  "expires_at": "2026-11-17T00:00:00Z",
  "note": "US-only program. Not a security."
}
```

### 8.3 Access Control Rules

**Rule Engine:**

- No FTHUSD or USDF issuance unless:
  - `wallet` has `membership_nft.status = ACTIVE`
  - `ComplianceRegistry.isWhitelisted(wallet) == true`
  - `riskTier != BLOCKED`

**Tier-Based Limits:**

| Tier | Daily Mint Cap | Daily Redeem Cap | KYC Refresh |
|------|----------------|------------------|-------------|
| `basic` | $10,000 | $10,000 | Annual |
| `pro` | $100,000 | $100,000 | Quarterly |
| `otc` | $10,000,000+ | $10,000,000+ | Quarterly + manual review |
| `internal` | Unlimited | Unlimited | N/A |

---

## 9. SECURITIES / E-MONEY / PAYMENT CLASSIFICATION

For each major jurisdiction where **[COMPANY]** operates or has users, a separate annex defines how tokens are classified.

> Files:  
> - `JURISDICTION-ANNEX-US.md`  
> - `JURISDICTION-ANNEX-EU-MICA.md`  
> - `JURISDICTION-ANNEX-UK.md`  
> - `JURISDICTION-ANNEX-SG.md`  
> - `JURISDICTION-ANNEX-UAE.md`  
> - `JURISDICTION-ANNEX-HK.md`  
> - `JURISDICTION-ANNEX-CH.md`  

Each annex should include:

### 9.X.1 REGULATORY ROLES

- Which entity is the:
  - Issuer  
  - Custodian  
  - Exchange / broker / dealer  
  - Payment service provider  
  - VASP / CASP / DPT operator

### 9.X.2 TOKEN TESTS (SECURITIES VS PAYMENT)

- US:
  - Howey / Reeves analysis for [ASSET]  
  - Is [ASSET] a security? MSB? Payment stablecoin?

- EU (MiCA / MiFID II):
  - Is [ASSET] an **ART**, **EMT**, or other crypto-asset?  
  - Is it also a "financial instrument" under MiFID II?

- UK:
  - Security token / e-money token / unregulated token classification.

- SG:
  - DPT vs Single-Currency Stablecoin vs Capital Markets Product.

- UAE / HK / CH:
  - Local token categories and licensing hooks.

### 9.X.3 OFFERING & DISTRIBUTION RULES

- Who can hold and trade [ASSET] (retail, pro, institutions only)?  
- Filings, whitepapers, or prospectuses needed?  
- Marketing / promotion restrictions.

### 9.X.4 CONTROLS & LIMITATIONS

- Geofencing / IP blocking where required  
- Whitelists / allowlists by jurisdiction  
- Hard blocks for prohibited countries

---

## 10. TESTING & ASSURANCE SCHEDULE

### 10.1 ANNUAL CONTROL CALENDAR

- **Q1:**
  - KYC/AML program review & updates  
  - Global sanctions list sanity check and vendor alignment
- **Q2:**
  - Smart contract audit refresh where changes have occurred  
  - External pen-test
- **Q3:**
  - PoR / reserves methodology review  
  - Jurisdiction annex updates (MiCA, SEC/DOJ guidance, etc.)
- **Q4:**
  - Independent compliance review (internal audit / external)  
  - Board reporting and approval of updated Framework

### 10.2 METRICS & REPORTING

Track at least:

- **KYC:**
  - # onboarded, # rejected, # escalations
- **AML:**
  - # alerts, # SAR/STR filed
- **Security:**
  - # critical vulns, time-to-fix
- **Legal:**
  - # jurisdictions active  
  - Status of licenses/registrations
- **PoR:**
  - Daily: FTHUSD supply vs. USD reserves (% backed)
  - Daily: USDF supply vs. FTHUSD backing (% backed)
  - Monthly: Independent PoR report published

---

## 11. OPERATIONAL RUNBOOK

### 11.1 Day 0 – Go-Live Checklist

- [ ] XRPL nodes healthy & synced (all 3: Core, Treasury, Member API)
- [ ] XRPL Core API passing smoke tests
- [ ] US bank accounts active with test deposits cleared
- [ ] KYC provider sandbox → production cut-over done
- [ ] Issuer accounts (FTHUSD, USDF) funded with XRP for fees
- [ ] Issuer account flags set: RequireAuth, RequireDest, NoRipple
- [ ] EVM contracts deployed and verified: ComplianceRegistry, MintGuard, ReserveRegistry, SystemGuard
- [ ] Governance doc: who can trigger mints & redeems, and how

### 11.2 Daily Ops

**KYC Queue:**

- Review new applicants, approve/reject
- Mint Membership NFTs for approved customers

**Bank Reconciliation:**

- Load previous day's bank activity
- Match incoming credits to customers / issuance requests
- Trigger mints of FTHUSD → allocate to FTHUSD vault / USDF users

**PoR Check:**

- Update ReserveRegistry with current USD balances
- Verify: `FTHUSD_supply <= USD_reserves`
- Verify: `USDF_supply <= FTHUSD_in_vault`
- If fails → auto-trigger SystemGuard.pause()

**Monitoring:**

- Node health: disk, memory, ledger age
- XRPL metrics: load, failed transactions
- EVM contract events: MintApproved, MintExecuted, BurnRecorded, Paused
- Alert if:
  - Node falls behind
  - RPC errors spike
  - Invariant violation detected

### 11.3 Weekly

**Reconciliation:**

- Total FTHUSD supply on XRPL vs. DB vs. USD in reserve accounts
- Total USDF supply vs. FTHUSD backing

**Compliance:**

- Check for expiring KYC (if time limits set)
- Adverse media hits
- Suspend / review flagged wallets

**Security:**

- Patch OS / dependencies
- Check logs for weird access

### 11.4 Monthly / Quarterly

**Board/Owner Report:**

- FTHUSD supply
- USDF in circulation
- USD reserves
- KYC stats (onboarded, rejected)
- Incidents (if any)
- PoR status (green/yellow/red)

**Policy Review:**

- Limits (per customer, per day)
- Risk appetite
- Necessary tweaks before scaling

---

## 12. CHANGE MANAGEMENT

- Material changes (new asset, new jurisdiction, new product) trigger:
  - Update of relevant `ASSET-REGULATORY-PROFILE`  
  - Update of relevant `JURISDICTION-ANNEX`  
  - Legal review and sign-off  
  - Board / committee approval where required

- Versioning:
  - This Framework uses semantic versioning (e.g. `1.0.0 → 1.1.0`)  
  - Changelog maintained at end of file.

---

## 13. SAFETY PROTECTIONS SUMMARY

**Four Independent Brakes:**

1. **Bank & Fiat Reality**
   - Can't update ReserveRegistry without USD hitting US bank accounts

2. **EVM Guard Contracts**
   - MintGuard + ReserveRegistry + SystemGuard make minting mathematically impossible if:
     - Reserves too low
     - Caps exceeded
     - System paused

3. **Node Topology**
   - Only Treasury Node can touch issuer flows
   - Core/Member nodes can fail without compromising minting ability

4. **Human Processes**
   - Compliance must whitelist customers
   - Ops must trigger mints/burns via controlled bots
   - Emergency multi-sig can pause system

**Invariants Enforced:**

- `FTHUSD_circulating <= USD_reserves_total`
- `USDF_circulating <= FTHUSD_in_USDF_Back_Vault`
- `totalNetMinted + newMint <= globalCap`
- `totalNetMinted + newMint <= maxAllowedSupply(reserves)`
- No mints when `SystemGuard.isPaused() == true`

---

## 14. CONTACTS & ESCALATION

- **Head of Compliance / MLRO:** [NAME, EMAIL, PHONE]
- **Chief Information Security Officer (CISO):** [NAME, EMAIL, PHONE]
- **General Counsel:** [NAME, EMAIL, PHONE]
- **24/7 Incident / Emergency Contact:** [PHONE, PAGERDUTY]

---

## 15. RELATED DOCUMENTATION

**Compliance Templates:**

- [ASSET-ISSUANCE-INTAKE.template.md](ASSET-ISSUANCE-INTAKE.template.md)
- [KYC-AML-PROGRAM.template.md](KYC-AML-PROGRAM.template.md)
- [COMPLIANCE-VENDOR-GUIDE.md](COMPLIANCE-VENDOR-GUIDE.md)
- [JURISDICTION-COMPLIANCE-MAP.md](JURISDICTION-COMPLIANCE-MAP.md)
- [SECURITY-CONTROLS.template.md](SECURITY-CONTROLS.template.md)

**Regulatory Profiles:**

- [../regulatory/ASSET-REGULATORY-PROFILE.template.md](../regulatory/ASSET-REGULATORY-PROFILE.template.md)
- [../regulatory/FTHUSD-REGULATORY-PROFILE.md](../regulatory/FTHUSD-REGULATORY-PROFILE.md)

**Case Studies:**

- [../case_studies/vortex_spring_water_tokenization.md](../case_studies/vortex_spring_water_tokenization.md)
- [../xrpl_competition_analysis.md](../xrpl_competition_analysis.md)

---

## 16. CHANGELOG

- **v1.0 – [DATE]:** Initial global framework created.
  - Integrated FTHUSD/USDF architecture
  - Defined 3-node XRPL topology (Core, Treasury, Member API)
  - Established EVM control plane (ComplianceRegistry, MintGuard, ReserveRegistry, SystemGuard)
  - Documented PoR policy and mint/burn workflows
  - Defined Membership NFT structure and tier-based access control
  - Created operational runbook (daily, weekly, monthly tasks)
  - Established safety invariants and circuit breakers

---

**Document Version:** 1.0  
**Last Updated:** 2025-11-17  
**Owner:** Compliance + Legal + Engineering + Treasury Teams  
**Review Cycle:** Quarterly (or when regulations change)

---

## APPENDIX A: SYSTEM ARCHITECTURE DIAGRAM

```
┌───────────────────────────────────────────────────────────────┐
│                    [COMPANY] BANK RACK SYSTEM                  │
├───────────────────────────────────────────────────────────────┤
│                                                                 │
│  PUBLIC LAYER                                                  │
│  ├─ Core Node (XRPL) ─────→ Analytics, Bots, Monitoring       │
│  └─ Member API Node (XRPL) ─→ Client Reads, Quotes, Balances  │
│                                                                 │
│  PRIVATE LAYER (VPN + IP Whitelist)                           │
│  ├─ Treasury Node (XRPL) ──→ Issuer Operations (Mint/Burn)    │
│  ├─ XRPL Core API ─────────→ REST wrapper for internal services│
│  ├─ Compliance & KYC Service ─→ KYC/AML engine + whitelist    │
│  ├─ Membership / NFT Service ─→ Mint/burn NFTs + access logic │
│  ├─ Treasury & Token Service ─→ Bridge bank ↔ XRPL supply     │
│  └─ Bank Gateway Service ───→ Track USD in/out from US banks  │
│                                                                 │
│  EVM CONTROL PLANE (Ethereum / Polygon / Base)                │
│  ├─ ComplianceRegistry ────→ Whitelist + risk tiers           │
│  ├─ MintGuard ─────────────→ Mint/burn approval + rate limits │
│  ├─ ReserveRegistry ───────→ USD reserves + PoR attestations  │
│  ├─ MembershipNFTRegistry ─→ Mirror XRPL NFT tiers (optional) │
│  └─ SystemGuard ───────────→ Pause/unpause + emergency controls│
│                                                                 │
│  STORAGE LAYER                                                 │
│  ├─ Postgres DB ───────────→ customers, wallets, kyc, fiat_tx │
│  ├─ Redis ─────────────────→ Cache, session state             │
│  └─ S3 / IPFS ─────────────→ Documents, PoR reports, audit logs│
│                                                                 │
│  COLD STORAGE                                                  │
│  └─ Air-Gapped HSM/Hardware ─→ FTHUSD_Issuer, USDF_Issuer keys│
│                                                                 │
└───────────────────────────────────────────────────────────────┘
```

---

**END OF GLOBAL COMPLIANCE FRAMEWORK**

For questions or updates, contact:

- **Compliance Officer:** [compliance@domain.com]
- **Legal Counsel:** [legal@domain.com]
- **Security Team:** [security@domain.com]
- **Engineering Lead:** [engineering@domain.com]
