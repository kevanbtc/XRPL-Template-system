# COLLATERAL TRIAGE FRAMEWORK

**Purpose:** Institutional-grade decision system for evaluating exotic/complex assets
**Audience:** Credit committees, treasury operations, asset managers
**Philosophy:** Sort the real from the theater. Only monetize what can survive external scrutiny.

---

## EXECUTIVE SUMMARY

You will be handed messy, high-nominal-value assets with varying degrees of documentation and marketability.

**Your job is NOT to:**
- Believe the appraisal because it's on letterhead
- Build infrastructure around "maybe someday" assets
- Waste engineering time on beautiful distractions

**Your job IS to:**
- Run hard-nosed external verification on everything
- Assign realistic LTV only after third-party confirmation
- Build rails only for assets that pass the "would a bank touch this?" test
- Track everything else as optionality, not capital

This framework gives you:
1. **Asset ranking methodology** (Tier 1 → Tier 3)
2. **Go/No-Go decision checklists** for each asset class
3. **Time-boxing rules** (how much effort before you walk away)
4. **Integration templates** (how verified assets plug into your rails)

---

## PART 1: ASSET TAXONOMY & RANKING

### Tier 1 — Bank & Institutional Grade

**Definition:** Assets a mainstream lender, insurer, or institutional buyer would accept as collateral with minimal hesitation.

**Characteristics:**
- Independently verified value (recent appraisal, market pricing)
- Clear legal ownership and perfected security interest
- Established market for liquidation
- Regulated custodian or auditable physical control
- Insurance available and in place

**LTV Range:** 30–75% depending on liquidity

**Examples:**
- Investment-grade bonds (government, corporate)
- Exchange-traded securities
- Physical gold/silver held by LBMA vault
- Cash deposits in regulated banks
- High-value gems with recent independent appraisal + insurance + custody

**Default Assumption:** These justify full engineering integration (vaults, oracles, facilities, stablecoins).

---

### Tier 2 — Exotic but Monetizable (Deal-Specific)

**Definition:** Assets with provable value and *some* institutional interest, but requiring bespoke structuring or specialized counterparties.

**Characteristics:**
- Appraisals exist but may need updating
- Legal ownership clear but instruments non-standard
- No broad market, but known specialist buyers/lenders exist
- Higher due diligence cost
- Longer time-to-liquidity (months, not days)

**LTV Range:** 0–40% (case-by-case, post-verification)

**Examples:**
- Fine art, rare collectibles (authenticated, appraised, insured)
- Restricted securities with lock-up periods
- Foreign currency holdings with conversion restrictions
- Pre-revenue IP with defensible patents and buyer interest
- Equipment/machinery with specialist resale market

**Default Assumption:** Cap verification effort (40–80 hours). If no term sheet materializes, downgrade to Tier 3.

---

### Tier 3 — Speculative / Legacy / Hopium

**Definition:** Assets with high nominal value on paper but no current path to institutional acceptance.

**Characteristics:**
- Value claims unsupported by independent verification
- No clear buyer or lender interest despite outreach
- Legal enforceability unclear or historically rejected
- Market consists of retail dreamers, not institutions

**LTV Range:** 0% (excluded from capital calculations)

**Examples:**
- Historic bonds from defunct governments (Chinese Imperial, Confederate, Weimar)
- "Revaluation" currency plays (IQD, VND, ZWD) without central bank commitment
- Unverified mining claims, exploration rights
- Assets in active litigation with no clear timeline
- "Oil certificates" / "gold commitments" not traceable to counterparty balance sheets

**Default Assumption:** Document existence, archive securely, assign zero value until external reality changes. Do not build infrastructure around these.

---

## PART 2: ASSET-BY-ASSET TRIAGE PLAYBOOKS

### 🟢 ASSET 1: HDG RUBY COLLECTION

**Nominal Value:** $376.7M (HDG Appraisal Group, Oct 2021)
**Current Status:** Appraisal exists, ownership via I.B.E. → FollowMe monetization rights
**Initial Tier:** **Tier 1.5** (institutional-grade *if* verification passes)

#### Go/No-Go Checklist

**Phase 1: Appraisal Verification (Week 1–2, ~$5–10K cost)**

- [ ] **Contact HDG directly** — confirm appraisal is in their system, not forged
  - Get: Digital copy from HDG's records, confirmation of appraiser credentials
  - Red flag: HDG doesn't respond, denies issuing it, or appraiser no longer with firm

- [ ] **Age check** — appraisal dated Oct 2021 (now 3+ years old)
  - Action required: Commission **fresh appraisal** from independent source (Sotheby's, Christie's, GIA-certified appraiser)
  - Budget: $15–30K for comprehensive re-appraisal
  - Timeline: 4–8 weeks
  - Red flag: New appraisal comes in <50% of original (suggests inflated original valuation)

- [ ] **GIA Reports** — for individual high-value stones
  - Get: Individual gem reports for any stone >$1M in claimed value
  - Budget: $300–500 per stone
  - Red flag: Stones claimed as "pigeon blood ruby" grade without GIA Natural Ruby Report

- [ ] **Custody Confirmation**
  - Require: Vault receipt from licensed custodian (Brinks, Loomis, Malca-Amit, or equivalent)
  - Must show: Specific inventory matching appraisal, insured storage, your entity (or SPV) as authorized party
  - Red flag: "In a safe somewhere" / "with a trusted friend" / unclear location

- [ ] **Insurance**
  - Require: All-risk insurance policy from major carrier (Lloyds, Chubb, AIG)
  - Coverage amount: At minimum 60% of appraised value
  - Budget: ~0.5–2% annual premium (~$1.1–4.5M/year for $376M coverage)
  - Red flag: No insurer will quote, or premiums >5% (suggests high loss risk)

**Decision Point 1:** If Phase 1 fails any critical checkpoint → **STOP**. Downgrade to Tier 3. Do not proceed.

---

**Phase 2: Lender/Buyer Outreach (Week 3–6, ~20–40 hours + legal fees)**

Assuming Phase 1 passed:

- [ ] **Sounding with 3–5 real lenders:**
  - Art/jewelry secured lenders: Borro, Luxury Asset Capital, Sutton Capital
  - Private bank art finance desks: Citi Private Bank, JPM Private Bank, UBS
  - Family offices known for hard-asset lending

- [ ] **Present full package:**
  - Updated appraisal
  - GIA reports
  - Custody agreement
  - Insurance policy
  - Legal opinion on ownership/title

- [ ] **Ask one question:**
  > "Would you lend against this? If yes, at what LTV, rate, and minimum/maximum ticket size?"

- [ ] **Record responses:**
  - Best offer LTV: ____%
  - Rate: ____%
  - Ticket size: $___M – $___M
  - Conditions: ________________

**Decision Point 2:**

- If **zero** lenders respond positively → **STOP**. Downgrade to Tier 2 or 3. Treat as long-term optionality, not active collateral.
- If **1+ lenders** provide term sheets → **PROCEED** to Phase 3.

---

**Phase 3: Facility Structuring (Week 7–10)**

You now have:
- Verified appraisal (conservative number)
- Real lender interest
- Term sheet with LTV and rate

**Actions:**

1. **Form SPV:** `Ruby Vault I, LLC` (Delaware or Wyoming)
2. **Perfect security interest:** Pledge rubies to SPV, file UCC-1
3. **Execute facility:** Sign credit agreement, draw initial tranche
4. **On-chain integration:** Create Vault NFT on private ledger (VLT-RUBY-HDGR-2021-001)
5. **Oracle setup:** Chainlink adapter to verify:
   - Quarterly appraisal updates
   - Insurance policy active
   - Custody confirmations
   - Lender facility availability

**Vault Metadata:**

```yaml
vault_id: VLT-RUBY-HDGR-2021-001
asset_type: Natural Corundum Ruby Collection
appraised_value_usd: 376_700_000
discount_applied: 80%  # institutional haircut
discounted_collateral_value: 75_340_000
facility_ltv: 40%
facility_size_usd: 30_000_000
lender: [Confidential - see docs]
facility_maturity: 2027-12-31
ipfs_docs_cid: Qm...
oracle_adapter: ruby-vault-proof-v1
verification_frequency: quarterly
insurance_carrier: Lloyds
insurance_policy_number: [redacted]
custody_provider: Malca-Amit
custody_location: Geneva Freeport
```

**Integration into Unykorn Rails:**

- **Stablecoin Backing:** Ruby facility ($30M) can back TGUSD issuance
  - Mint cap: 90% of facility ($27M TGUSD)
  - Over-collateralization: 111% (conservative)

- **Private Placement:** Issue "Ruby Vault I Notes" — $20M, 3yr, 10% coupon
  - Secured by facility cash flows
  - NFT-based note ownership
  - AFO automated payments

- **Bank Filings Page:** Publish daily PoR showing:
  - Facility balance verified
  - Insurance active
  - Appraisal date and value
  - Link to IPFS doc bundle (investors only)

---

**Time Budget:** 10–12 weeks, $50–100K all-in (appraisals, legal, insurance deposits)

**Expected Outcome:** $20–30M usable facility backing real stablecoin issuance or private notes.

**Success Metric:** You can show investors/partners a credit agreement from a real lender with your entity as borrower and rubies as named collateral.

---

### 🟡 ASSET 2: IQD BOXES + OIL CERTIFICATES

**Nominal Value:** Unclear (boxes of Iraqi Dinar + oil-related paper)
**Current Status:** Swiss registration letter confirms boxes exist; contents/value unverified
**Initial Tier:** **Tier 2 (speculative, time-boxed verification only)**

#### Go/No-Go Checklist

**Phase 1: Reality Check (Week 1–2, max 20 hours)**

- [ ] **Inventory confirmation**
  - Require: Photos of opened boxes showing actual currency denominations/quantities
  - Require: Itemized list with serial number ranges (if IQD notes)
  - Red flag: Only "trust me" descriptions, no physical evidence

- [ ] **IQD Market Reality**
  - Research: What is the **actual** market rate for IQD today?
  - Check: eBay, currency dealer sites, forex platforms
  - Question: Can you sell IQD at any reasonable rate (even 50% discount to official rate)?
  - Red flag: Only buyers are "RV" groups promising future 1:1 ratios with USD

- [ ] **Oil Certificate Legal Read**
  - Hire: One experienced oil & gas lawyer (not a generalist)
  - Task: Review sample oil certificate, determine:
    - Is this a contractual right to physical oil delivery?
    - Is there a named counterparty (oil company, state entity)?
    - Can the right be enforced in any jurisdiction?
    - Has any similar instrument ever been successfully monetized?
  - Budget: $5–10K for opinion letter
  - Red flag: Lawyer says "this is not a legally enforceable instrument"

**Decision Point 1:** If lawyer opinion is negative AND IQD has no real market → **STOP IMMEDIATELY**.

- Downgrade to Tier 3
- Archive documents
- Assign zero value
- **Do not spend further time/money**

---

**Phase 2: Market Sounding (Week 3–4, only if Phase 1 shows glimmer of hope)**

If lawyer found *some* contractual value in oil certs OR IQD can be sold at any reasonable rate:

- [ ] **Contact 2–3 specialist buyers:**
  - For IQD: Currency dealers specializing in exotic/restricted currencies
  - For oil certs: Commodity trade finance firms, oil traders, structured trade desks

- [ ] **Get binding quotes:**
  - IQD: Offer to sell X million IQD at market rate minus Y% discount
  - Oil certs: Present legal opinion + docs, ask for bid

- [ ] **Record best offer:**
  - IQD: $_____ total (basis: ___ million IQD at rate ___)
  - Oil certs: $_____ (basis: ____% of face value)

**Decision Point 2:**

- If best offer is <10% of "claimed value" → **STOP**. Downgrade to Tier 3.
- If best offer is meaningful (e.g., $500K+) → **PROCEED** to close deal.

---

**Phase 3: Monetization (if applicable)**

- [ ] **Execute sale:** Convert IQD or oil certs to USD/EUR
- [ ] **Bank proceeds:** Deposit in Unykorn/Forum Europe operating account
- [ ] **Record source:** "Legacy Asset Realization — IQD/Oil Holdings"
- [ ] **Use proceeds:** Treat as ordinary capital (seed liquidity, fund operations, etc.)

**DO NOT:**
- Build vaults or oracles around IQD boxes
- Treat unmonetized IQD as collateral for anything
- Include IQD boxes in "reserves" or "backing" calculations

**Integration into Unykorn Rails:**

Only after cash hits the bank:

```yaml
# Not a vault — just a capital inflow record
source: Legacy_Asset_Realization
asset_type: IQD_Holdings
proceeds_usd: [actual sale amount]
realization_date: 2025-XX-XX
status: monetized_closed
```

These proceeds flow through normal treasury operations. The rails only see clean cash.

---

**Time Budget:** 4 weeks max, $10–20K max spend (legal opinion + travel/meeting costs)

**Expected Outcome:** Either small cash realization ($100K–$1M) OR confirmation of zero value.

**Success Metric:** Avoid wasting 6 months chasing "the RV is coming" fantasies.

---

### 🔴 ASSET 3: HISTORIC CHINESE BONDS ("Super Petchili")

**Nominal Value:** Varies (often claimed in billions)
**Current Status:** Genuine historic instruments, but China does not honor, courts have rejected claims
**Initial Tier:** **Tier 3 (zero value for capital purposes, optionality only)**

#### Go/No-Go Checklist

**Phase 1: Authentication Only (Week 1, ~$2–5K)**

- [ ] **Verify bonds are genuine historic pieces:**
  - Contact scripophily experts (e.g., R.M. Smythe, Spink)
  - Send high-res scans
  - Get opinion: "These are authentic 191X era bonds" vs. "These are reproductions"

- [ ] **Get collector value quote:**
  - Ask: What would a numismatic collector pay per bond?
  - Typical range: $50–500 per bond (depending on condition, rarity)

**Decision Point 1:**

- If bonds are **authentic** → document, archive, consider selling a few to collectors for small cash
- If bonds are **reproductions** → discard, assign zero value

---

**Phase 2: Limited Optionality Preservation**

- [ ] **Perfect documentation:**
  - Photograph every bond (front/back, high-res)
  - Catalog: Issue dates, serial numbers, denominations
  - Store in climate-controlled secure location
  - Create IPFS bundle with full documentation

- [ ] **Legal package (minimal):**
  - One-time legal opinion on ownership/chain of custody
  - UCC filing if you want to perfect security interest (optional)
  - Budget: $3–5K

- [ ] **Monitor for "black swan" events:**
  - Chinese government announces buyback program (extremely unlikely)
  - International arbitration tribunal orders payment (never succeeded to date)
  - Litigation consortium secures settlement (track high-profile cases)

**DO NOT:**
- Hire lawyers to "enforce payment" (courts have consistently rejected)
- Join "bondholder associations" promising imminent redemption
- Build any infrastructure assuming payment
- Include in capital/reserve calculations

**Integration into Unykorn Rails:**

```yaml
# Archive record only — not a vault
asset_type: Historic_Chinese_Bonds
classification: Tier_3_Optionality
quantity: [X bonds]
authentication_status: verified_genuine
collector_value_usd: [small amount]
face_value_usd: [large amount - for reference only]
enforceability: none_established
current_ltv: 0.00%
notes: "Documented and archived. Monitored for geopolitical changes. Not included in any capital calculations."
```

**Optional Cash Realization:**

If you want small immediate cash:
- Sell 10–20 bonds to collectors via auction house
- Expect: $50–500 per bond
- Keep remainder as "free lottery ticket"

---

**Time Budget:** 1 week, $5–10K max

**Expected Outcome:** Clean documentation, maybe $5–20K from collector sales, zero expectations of sovereign payment.

**Success Metric:** You didn't waste engineering/legal resources building redemption infrastructure for assets with no path to payment.

---

### 🟢 ASSET 4: SANTANDER BANKING PACKAGE (EUR CHEQUES + IBAN)

**Nominal Value:** €200M (10× €20M cheques)
**Current Status:** Account ownership confirmed, cheque nature unverified
**Initial Tier:** **Tier 1 (if verified) or Tier 3 (if not)**

This is your **highest-priority verification target** because:
- It's current banking paper (not historic)
- You have direct bank contact
- If real, it's $200M+ institutional collateral
- Verification cost is low (mostly time + relationship management)

#### Go/No-Go Checklist

**Phase 1: Bank Verification (Week 1–2, zero cost except time)**

- [ ] **Call/email Santander RM directly:**
  - Reference: IBAN ES21 0049 5656 5323 1000 2112
  - Reference: Cheque serial numbers (from photos)
  - Reference: Forum Europe S.L. as account holder

- [ ] **Questions to ask (in writing, via secure email):**

  1. **Cheque Nature:**
     - Are these cashier's/certified cheques or ordinary corporate cheques?
     - Are funds currently reserved/blocked for these cheques?
     - Expiry date, revocation conditions?

  2. **Account Status:**
     - Is account active and in good standing?
     - Any encumbrances, liens, legal holds?

  3. **Monetization Options:**
     - Can Santander issue a **blocked funds letter** for PoF purposes?
     - Can Santander convert to SBLC / Bank Guarantee?
     - Can Santander extend a credit line secured by these instruments?
     - Would Santander be willing to confirm status to third-party lenders/auditors?

- [ ] **Get written responses:**
  - Email confirmations (acceptable)
  - Official bank letters on letterhead (better)
  - Meeting minutes signed by RM (best)

**Decision Point 1:**

**IF BANK CONFIRMS:**
- Cheques are certified/cashier's cheques WITH funds blocked
- OR bank offers to issue SBLC/credit facility

→ **PROCEED TO PHASE 2** (full integration)

**IF BANK SAYS:**
- These are ordinary cheques, funds not blocked
- No guarantee, no facility, no blocked funds letter available

→ **STOP**. Downgrade to Tier 3. These are only "account ownership proofs", not collateral.

---

**Phase 2: Facility Structuring (Week 3–6, assuming positive bank response)**

- [ ] **Negotiate facility terms:**
  - Type: Credit line, term loan, SBLC, or blocked deposit facility
  - Size: Likely 40–60% of cheque face value (€80–120M facility on €200M nominal)
  - Rate: Euribor + 200–500 bps
  - Maturity: 1–3 years
  - Covenants: Standard corporate facility terms

- [ ] **Legal structure:**
  - Borrower: Forum Europe S.L. or new SPV "Santander Facility I, S.L."
  - Collateral: Pledge of cheques or assignment of account balances
  - Jurisdiction: Spanish law, likely Madrid courts
  - Budget: €20–40K legal fees

- [ ] **Execute facility:**
  - Sign credit agreement
  - File security registrations
  - Draw initial tranche (test functionality)

---

**Phase 3: On-Chain Integration (Week 7–10)**

- [ ] **Create Vault NFT (Private Ledger):**

```yaml
vault_id: VLT-SANTANDER-CHK-BATCH-001
asset_type: Santander_EUR_Cheque_Batch
iban: ES2100495656532310002112
account_holder: FORUM_EUROPE_SL
bank: Banco_Santander_SA
cheque_count: 10
cheque_face_value_eur: 20_000_000
batch_nominal_eur: 200_000_000
facility_id: FAC-SANTANDER-001
facility_type: Blocked_Funds_Credit_Line
facility_size_eur: 100_000_000
facility_maturity: 2027-12-31
oracle_adapter: santander-iban-proof-v1
verification_method: Daily_Bank_Statement
ipfs_docs_cid: QmSantanderChequeVault2025-001
risk_tier: Tier_1_Bank_Grade
current_ltv: 50%
max_ltv: 60%
```

- [ ] **Build Proof Server:**
  - Backend service (FastAPI/Express)
  - Endpoints: `/uploadStatement`, `/latestProof`
  - Accepts: Daily PDF statements from banker (encrypted)
  - Extracts: Account balance, blocked funds amount
  - Outputs: JSON for Chainlink adapter

- [ ] **Deploy Chainlink External Adapter:**
  - Name: `santander-iban-proof-v1`
  - Reads: Your Proof Server `/latestProof`
  - Validates: Proof freshness (<36hrs), balance non-negative
  - Returns: `facility_available_eur` (scaled to 1e18)

- [ ] **Deploy Oracle Feed Contract:**
  - Contract: `SantanderFacilityFeed`
  - Storage: `facilityAvailable` (wei-scaled EUR)
  - Update: Daily via Chainlink job
  - Access: Public read for facility registry

- [ ] **Create Facility Registry:**
  - Contract: `FacilityRegistry`
  - Tracks: FAC-SANTANDER-001 parameters
  - Function: `getUsableCapacity(facilityId)` → returns oracle-verified EUR amount

- [ ] **Deploy Stablecoin Pool:**
  - Pool: `TGUSD-SANTANDER-POOL-001`
  - Backing: Santander facility (oracle-verified)
  - Mint cap: 90% of facility balance (EUR → USD via FX oracle)
  - Collateralization: 120% minimum
  - Redemption: Enabled if PoR valid

---

**Phase 4: Private Placement Documentation (Week 11–12)**

- [ ] **Draft PPM (Private Placement Memorandum):**

**Key sections:**

1. **Issuer:** Unykorn Global Finance / Forum Europe S.L.
2. **Program:** Santander Facility I — EUR-backed digital securities
3. **Underlying:** Santander IBAN + blocked funds/credit facility
4. **Digital Infrastructure:** Vault NFT + Chainlink PoR + stablecoin contracts
5. **Instruments Offered:**
   - TGUSD (stablecoin backed by facility)
   - EUR-denominated notes (e.g., 3yr, 8% coupon)
6. **Use of Proceeds:** RWA onboarding, liquidity provision, treasury operations
7. **Risk Factors:** Bank risk, FX risk, oracle risk, regulatory changes
8. **Reporting:** Daily PoR dashboard, IPFS-hosted docs, on-chain transparency

- [ ] **Bank Filings Page Section:**

```markdown
### Santander Facility I

**Backing:** Credit facility with Banco Santander S.A.
**Facility Size:** €100,000,000
**Underlying:** 10× €20M negotiable cheques, IBAN ES21…2112
**Account Holder:** FORUM EUROPE S.L. (verified)
**Last Verification:** 2025-01-15 14:32 UTC
**Facility Available:** €98,450,000 (Chainlink oracle)
**Stablecoins Issued:** $105,000,000 TGUSD
**Collateralization:** 123% (target: 120%)
**Status:** ✅ Fully backed

**Documentation:**
- [Account Ownership Certificates](ipfs://Qm...)
- [Credit Agreement Summary](ipfs://Qm...) [Investors Only]
- [Daily PoR Feed](https://explorer.unykorn.finance/facility/FAC-SANTANDER-001)
```

---

**Time Budget:** 12 weeks, €50–100K all-in (legal, Chainlink nodes, engineering)

**Expected Outcome:**
- €80–120M verified facility
- $80–120M stablecoin backing capacity
- Institutional-grade PoR system
- Template reusable for future bank facilities

**Success Metric:**
You can show an external auditor:
1. Bank-issued confirmation of facility
2. Daily oracle proofs of balance
3. On-chain mint/burn rules tied to oracle
4. Full IPFS document trail

---

## PART 3: DECISION RULES & TIME-BOXING

### Rule 1: The 40-Hour Rule

For **any Tier 2 asset**, set a hard time limit:

> "We will invest maximum 40 focused hours (1 work week) attempting to verify/monetize this asset. If no concrete progress (term sheet, binding offer, facility commitment) emerges, we STOP and downgrade to Tier 3."

This prevents "sunk cost fallacy" spirals.

---

### Rule 2: The "Would a Bank Touch This?" Test

Before building **any** infrastructure (oracles, vaults, contracts):

> "If I walked into Chase Private Bank / Citi / UBS with this asset, would they:
> A) Offer me a loan against it?
> B) Laugh me out of the room?"

If B, don't build. Document and archive only.

---

### Rule 3: The Paper vs. Reality Gap

Appraisals, certificates, and official-looking documents **do not equal value**.

Value = **"Will a third party give me cash/credit secured by this asset?"**

Until you have a binding term sheet from a real counterparty, assume value = 0 for capital purposes.

---

### Rule 4: Separation of Concerns

Keep the rails clean:

- **Tier 3 assets:** Archive, document, monitor for changes. **Never** appear in capital calculations.
- **Tier 2 assets:** Time-boxed verification. Only upgrade to Tier 1 if third-party validation occurs.
- **Tier 1 assets:** Full integration (vaults, oracles, facilities, stablecoins).

Your stablecoin holders should **never** be exposed to "hopium collateral."

---

## PART 4: INTEGRATION TEMPLATES

Once an asset passes verification and achieves Tier 1 status, use this template:

### Standard Vault Creation Process

**Step 1: Evidence Bundle**
- Collect all docs (appraisals, legal opinions, custody agreements, insurance policies, bank confirmations)
- Organize in folder: `VAULT-[ASSET-ID]-[YEAR]/`
- PGP sign entire bundle
- Upload to IPFS → get CID
- Store CID + hash on-chain

**Step 2: Mint Vault NFT (Private Ledger)**

```yaml
vault_id: VLT-[ASSET-CLASS]-[ID]-[YEAR]
asset_type: [Rubies | Santander_Cheques | Gold | etc.]
appraised_value_usd: [amount]
discount_applied_pct: [haircut, e.g., 80%]
discounted_collateral_value: [amount]
facility_id: FAC-[ID]
facility_type: [Credit_Line | SBLC | Blocked_Deposit]
facility_size_usd: [amount]
facility_provider: [Bank name or lender]
facility_maturity: [YYYY-MM-DD]
oracle_adapter: [adapter name]
verification_frequency: [daily | weekly | quarterly]
ipfs_docs_cid: [CID]
insurance_carrier: [if applicable]
custody_provider: [if applicable]
risk_tier: Tier_1
current_ltv_pct: [%]
max_ltv_pct: [%]
created_date: [YYYY-MM-DD]
last_updated: [YYYY-MM-DD]
```

**Step 3: Oracle Setup**

Build Chainlink External Adapter:

1. **Data Source:** How do you verify this asset still exists/has value?
   - Bank statements (Santander)
   - Quarterly appraisals (rubies)
   - Vault receipts (gold)
   - Insurance policy active confirmations

2. **Proof Server:** Your backend service that:
   - Ingests verification docs (PDFs, APIs, emails)
   - Validates authenticity (signatures, seals, hashes)
   - Extracts key data (balance, value, status)
   - Exposes `/latestProof` endpoint for Chainlink

3. **External Adapter:** Node.js service that:
   - Accepts Chainlink job run with `vault_id` or `facility_id`
   - Calls Proof Server
   - Validates freshness
   - Returns normalized numeric output (scaled to 1e18)

4. **On-Chain Feed:** Contract storing latest oracle value:
   ```solidity
   uint256 public facilityAvailable; // or assetValue
   uint256 public lastUpdated;
   function updateValue(uint256 _newValue) external onlyOracle;
   ```

**Step 4: Facility Registry**

Contract tracking facility parameters:

```solidity
struct Facility {
    bytes32 id;
    uint256 cap;
    uint256 minCollateralRatio; // e.g., 12000 = 120%
    address oracleFeed;
    bool active;
}

function getUsableCapacity(bytes32 id) public view returns (uint256) {
    Facility storage f = facilities[id];
    if (!f.active) return 0;
    uint256 available = OracleFeed(f.oracleFeed).facilityAvailable();
    return available > f.cap ? f.cap : available;
}
```

**Step 5: Stablecoin Pool**

```solidity
// TGUSD-[FACILITY-ID]-POOL
uint256 public totalMinted;
bytes32 public facilityId;

function mint(address to, uint256 amount) external {
    uint256 capacity = facilityRegistry.getUsableCapacity(facilityId);
    uint256 capacityUSD = capacity * eurUsdPrice / 1e18; // if EUR facility
    uint256 maxMint = capacityUSD * 90 / 100; // 90% of capacity

    require(totalMinted + amount <= maxMint, "Exceeds capacity");

    totalMinted += amount;
    _mint(to, amount);
}
```

**Step 6: Reporting & Transparency**

Bank Filings page section:

```markdown
### [Facility Name]

**Backing:** [Asset type / Bank facility]
**Facility Size:** [Amount in base currency]
**Underlying:** [Brief description]
**Last Verification:** [Timestamp] UTC
**Facility Available:** [Oracle-verified amount]
**Stablecoins Issued:** [Amount] [TICKER]
**Collateralization:** [%] (target: [%])
**Status:** ✅ Fully backed | ⚠️ Below target | 🔴 Failed PoR

**Documentation:**
- [Evidence Bundle](ipfs://...)
- [Facility Agreement Summary](ipfs://...) [Accredited Investors Only]
- [Live PoR Feed](https://explorer...)
```

---

## PART 5: EXAMPLE DECISION FLOW

**Scenario:** Someone hands you a "€500M gold certificate from Dubai"

### Week 1: Initial Assessment

**Questions:**
1. Who issued this certificate? (Named entity with contact info?)
2. Where is the physical gold? (Named vault, verifiable address?)
3. Can we visit the vault? (Access allowed?)
4. Is gold insured? (Policy number, carrier?)
5. Do you have legal title? (Ownership docs, not just "certificate"?)

**Red Flags:**
- "Certificate" is just a PDF, no named issuer
- Gold location is "somewhere in Dubai"
- No vault visit allowed ("trust the certificate")
- No insurance
- "Title transfers upon payment of storage fees" (not actual ownership)

**Decision:** **STOP**. This is Tier 3. Do not proceed. Archive docs, assign zero value.

---

**Alternative Scenario:** Someone hands you a "€500M gold certificate" AND:
- Issuer is **Brinks Dubai Freeport** (real company, contact info verifiable)
- Certificate shows specific vault location, bar serial numbers, weights
- You can schedule a vault visit with Brinks (they confirm)
- Gold is insured by Lloyds (policy provided)
- Legal opinion confirms you have bailment rights / ownership

**Decision:** **PROCEED** to verification.

### Week 2–4: Verification

- [ ] Visit vault with independent assayer
- [ ] Verify serial numbers match certificate
- [ ] Re-weigh bars, re-assay purity
- [ ] Confirm insurance active
- [ ] Get updated legal opinion on title

**Cost:** $20–40K (travel, assayer fees, legal)

**Outcome:**
- Verified: 10,000 oz gold, 99.99% purity, secure vault, insured
- Market value: ~$20M (at $2000/oz)
- Discounted value (Tier 1 gold): $18M (10% haircut)

### Week 5–6: Monetization

**Option A: Direct loan**
- Approach 3–5 gold lenders (Sprott, Monetary Metals, etc.)
- Get offers: e.g., $13.5M loan at 75% LTV, 8% rate

**Option B: Integrate into your rails**
- Create VLT-GOLD-BRINKS-DUBAI-001
- Build oracle (quarterly vault receipts + insurance confirmations)
- Back $12M TGUSD issuance (150% collateralization)

**Decision:** Proceed with Option A or B (or both).

---

## PART 6: SUMMARY DECISION MATRIX

| Asset Class | Nominal Value | Verification Cost | Time Budget | Expected Outcome | Go/No-Go Trigger |
|------------|---------------|-------------------|-------------|------------------|------------------|
| **Santander Cheques** | €200M | €50–100K | 12 weeks | €80–120M facility | Bank written confirmation of blocked funds/facility |
| **HDG Rubies** | $376.7M | $50–100K | 10–12 weeks | $20–30M facility | Lender term sheet post-appraisal |
| **IQD Boxes** | Claimed: high<br>Realistic: ? | $10–20K | 4 weeks MAX | $0–1M cash realization | Legal opinion confirms contractual value OR market buyer found |
| **Chinese Bonds** | Face: billions<br>Realistic: collector value | $5–10K | 1 week | $5–20K (collector sales) | Authentication only; assume zero sovereign payment |
| **Generic "Gold Certificate"** | Varies | $0 (initial triage)<br>$20–40K (if proceeds) | 1 week initial<br>4 weeks verify | $0 OR $10–20M facility | Can schedule vault visit with named, reputable custodian |

---

## PART 7: OPERATIONAL CHECKLISTS

### Pre-Integration Checklist (All Tier 1 Assets)

Before building vaults/oracles/facilities:

- [ ] **Third-party verification complete**
  - Independent appraisal/assay/audit (if applicable)
  - Bank confirmation (if banking asset)
  - Legal opinion on ownership/title

- [ ] **Lender/buyer interest confirmed**
  - At least 1 binding term sheet OR purchase offer
  - Terms documented (LTV, rate, maturity, ticket size)

- [ ] **Insurance in place**
  - All-risk policy from major carrier
  - Coverage ≥ 60% of verified value
  - Your entity (or SPV) named as loss payee

- [ ] **Custody/control established**
  - Physical asset: Licensed vault/custodian
  - Financial asset: Segregated account, no encumbrances
  - Vault receipts / account statements available

- [ ] **Legal structure finalized**
  - SPV formed (if needed)
  - Security interests perfected (UCC filings, pledges)
  - Facility/loan agreement executed

- [ ] **Cost-benefit validated**
  - Expected facility size ≥ 5× verification cost
  - Example: $30M ruby facility justifies $50K appraisal cost
  - Example: $200K IQD realization does NOT justify $100K legal fight

---

### Post-Integration Checklist (Ongoing Operations)

Once asset is live in your rails:

**Daily:**
- [ ] Oracle updates successfully (check Chainlink job runs)
- [ ] PoR feed shows "healthy" status
- [ ] No failed verifications in logs

**Weekly:**
- [ ] Review facility utilization (how much capacity used?)
- [ ] Check for any custodian/bank notices (emails, letters)
- [ ] Verify insurance premiums current

**Monthly:**
- [ ] Review oracle data quality (any anomalies?)
- [ ] Update Bank Filings page if material changes
- [ ] Reconcile on-chain minting vs. off-chain facility availability

**Quarterly:**
- [ ] Fresh appraisal/valuation (if required by lender or your policy)
- [ ] Audit vault/custody (physical check or statement review)
- [ ] Renew insurance policies (if annual)
- [ ] Review facility terms (approaching maturity? refinance needed?)

**Annually:**
- [ ] Full external audit of vault system (optional but recommended for large programs)
- [ ] Legal opinion refresh (confirm title still clear)
- [ ] Lender relationship review (refinance, expand facility?)

---

## PART 8: COMMUNICATION TEMPLATES

### Template 1: Explaining to Asset Owners

> "We've built a system that can turn real, verified assets into programmable capital. Here's how we evaluate what you've brought us:
>
> **Phase 1:** We verify everything independently. Not because we don't trust you, but because our investors will ask, and we need answers.
>
> **Phase 2:** We approach 3–5 real lenders/buyers. If they'll give us a term sheet, we know it's real.
>
> **Phase 3:** If it passes those tests, we build digital infrastructure (vaults, oracles, stablecoins) and your asset backs real financial products.
>
> **What we DON'T do:** Build infrastructure around 'maybes' or 'somedays.' If it doesn't pass external verification, we document it and wait for reality to change.
>
> You want us to be hard on this. Because the assets that DO pass become the foundation of a system that actually works."

---

### Template 2: Explaining to Investors

> "Our collateral system has three tiers:
>
> **Tier 1:** Assets we can borrow against TODAY from real banks/lenders. These back stablecoins, notes, and programs. Full oracle transparency.
>
> **Tier 2:** Assets undergoing time-boxed verification. Not yet in capital calculations. If they pass, they graduate to Tier 1.
>
> **Tier 3:** Documented but unmonetizable. We track them for optionality, but they have zero weight in our reserves.
>
> You can see the breakdown on our Bank Filings page. We only count Tier 1 in collateralization ratios. Tier 2/3 are disclosed for completeness, not backing."

---

### Template 3: Explaining to Regulators/Auditors

> "Our asset intake process follows a credit committee framework:
>
> 1. **Initial Triage:** Every asset is initially assigned Tier 3 (zero value) until proven otherwise.
>
> 2. **External Verification:** We require third-party confirmation (appraisals, bank letters, legal opinions) before upgrading to Tier 2.
>
> 3. **Lender Validation:** We require at least one binding term sheet from a reputable lender/buyer before upgrading to Tier 1.
>
> 4. **Ongoing Monitoring:** Tier 1 assets have automated oracle verification (daily, weekly, or quarterly depending on asset type). PoR data is published on-chain.
>
> 5. **Conservative Haircuts:** We apply institutional-grade haircuts (e.g., 80% for rubies, 50% for bank facilities) before calculating LTV.
>
> This ensures our stablecoin holders are never exposed to 'hopium' collateral. Only verified, lender-accepted assets back our issuance."

---

## CONCLUSION: THE ADULT IN THE ROOM

The system you're building has one unfair advantage over the "real" system:

> **You can be honest about what's real and what's theater.**

Traditional finance is full of:
- Mark-to-model assets (synthetic CDOs, anyone?)
- Circular collateral loops (rehypothecation chains)
- "Trust us" reserves (stablecoins with no audits)

Your system can be different:

- **Transparent:** Every vault has IPFS docs, oracle feeds, on-chain proofs
- **Conservative:** Tier 3 until proven otherwise
- **Mechanical:** Oracles enforce rules, not human discretion
- **Honest:** Bank Filings page shows Tier 1/2/3 breakdown

When you sit across from a bank, a regulator, or a sophisticated investor, you can say:

> "Here's what we have that's real. Here's how we verify it. Here's how it backs our issuance. And here's what we DON'T count (the Tier 3 stuff) even though it's technically 'ours.'"

That makes you the adult in a room full of carnival barkers.

---

## NEXT STEPS

You now have:

1. ✅ **Infrastructure** (Terraform, XRPL nodes, deployment automation)
2. ✅ **Business case** (SPV, revenue models, pitch decks)
3. ✅ **Operational mechanics** (custodians, money flows, asset types)
4. ✅ **Dual-ledger architecture** (public/private XRPL, hide-yet-prove)
5. ✅ **Collateral triage system** (this document)

**Recommended immediate action:**

Pick ONE asset (probably **Santander** because it's current banking paper with direct contact) and run the full playbook:

- Week 1–2: Bank verification call
- Week 3–6: Facility negotiation (if bank confirms)
- Week 7–10: On-chain integration (vault, oracle, pool)
- Week 11–12: First stablecoin issuance backed by verified Santander facility

That proves the entire pattern. Then you can run the same playbook on:
- Rubies (if appraisal + lender interest materializes)
- Any future bank facilities (other IBANs, other banks)
- Gold, T-bills, real estate, or any Tier 1 RWA

Everything else (IQD boxes, Chinese bonds) stays documented but dormant until external reality changes.

**You're no longer building castles in the sky. You're building a bank that admits what's real.**
