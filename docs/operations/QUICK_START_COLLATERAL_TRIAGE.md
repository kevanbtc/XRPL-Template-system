# UNYKORN COLLATERAL SYSTEM — QUICK START GUIDE

**For:** Operators who need to onboard new collateral assets
**Time to read:** 10 minutes
**Output:** Clear go/no-go decision on any asset

---

## THE ONE-PAGE DECISION TREE

```
NEW ASSET ARRIVES
       │
       ▼
   ┌───────────────────────────────────┐
   │ Is it CURRENT banking paper       │
   │ with DIRECT bank contact?         │────YES───┐
   │ (e.g., Santander cheques)         │          │
   └───────────────────────────────────┘          │
       │ NO                                        ▼
       ▼                                    PRIORITY: RUN SANTANDER
   ┌───────────────────────────────────┐   PLAYBOOK IMMEDIATELY
   │ Is it PHYSICAL HIGH-VALUE asset   │   (See Section 2)
   │ with APPRAISAL + INSURANCE?       │
   │ (e.g., rubies, gold)              │────YES───┐
   └───────────────────────────────────┘          │
       │ NO                                        ▼
       ▼                                    TIER 1 IF VERIFIED
   ┌───────────────────────────────────┐   Run full verification
   │ Is it EXOTIC with SOME             │   (appraisal, lender interest,
   │ documentation but unclear value?   │    custody, insurance)
   │ (e.g., IQD boxes, oil certs)      │────YES───┐
   └───────────────────────────────────┘          │
       │ NO                                        ▼
       ▼                                    TIER 2: TIME-BOXED
   ┌───────────────────────────────────┐   Max 40 hours + $20K
   │ Is it HISTORIC/LEGACY with         │   If no term sheet → STOP
   │ no current claim mechanism?        │
   │ (e.g., Chinese bonds, Confederate) │────YES───┐
   └───────────────────────────────────┘          │
       │ NO                                        ▼
       ▼                                    TIER 3: ARCHIVE ONLY
   ┌───────────────────────────────────┐   Document, assign zero value
   │ UNKNOWN / UNCLEAR                  │   Monitor for changes
   │                                    │
   └───────────────────────────────────┘
       │
       ▼
   DEFAULT: TIER 3
   (Zero value until proven otherwise)
```

---

## SECTION 1: THE THREE TIERS (30-SECOND VERSION)

### Tier 1: BANK GRADE (Build Infrastructure)

**Rule:** A real bank/lender will give you cash secured by this asset TODAY.

**What you do:**
- Full vault creation (NFT on private ledger)
- Chainlink oracle integration
- Facility contract deployment
- Stablecoin backing or private placement notes

**Examples:**
- Santander IBAN + verified blocked funds
- Appraised rubies + lender term sheet at 40% LTV
- Physical gold in Brinks vault + insurance + loan agreement

---

### Tier 2: SPECULATIVE (Time-Boxed Verification)

**Rule:** Might have value, but needs work to prove it. Cap your effort.

**What you do:**
- 40 hours max + $20K max spend
- Document → Verify → Market test
- If no binding term sheet emerges → STOP, downgrade to Tier 3

**Examples:**
- IQD boxes (if legal opinion shows contractual value)
- Unverified gem collection (needs appraisal + lender interest)
- Foreign bank statements (need correspondent bank confirmation)

---

### Tier 3: ARCHIVE ONLY (Zero Capital Value)

**Rule:** No current path to institutional acceptance. Don't waste time.

**What you do:**
- Document existence (photos, PDFs, IPFS)
- Assign zero value in all capital calculations
- Monitor for black swan events (government buyback, litigation win)
- Do NOT build infrastructure

**Examples:**
- Historic Chinese bonds (courts reject claims)
- IQD "revaluation" hopes (no central bank commitment)
- Unverified "gold certificates" (can't visit vault)

---

## SECTION 2: SANTANDER PLAYBOOK (YOUR HIGHEST PRIORITY)

**Why prioritize:** Current banking paper + direct RM contact + €200M nominal = highest probability of real facility.

### Week 1: Bank Verification Call

**Action:** Email/call Santander RM

**Questions:**

1. Cheque status:
   - Certified/cashier's vs. ordinary corporate cheques?
   - Funds blocked/reserved?
   - Expiry/revocation terms?

2. Facility options:
   - Blocked funds letter available?
   - Convert to SBLC/Bank Guarantee?
   - Credit line against these instruments?

**Required output:** Written confirmation (email or letter)

---

### Week 2-4: Facility Negotiation (If Bank Confirms)

**IF BANK SAYS:**
- "These are certified, funds blocked, we can issue facility"

**THEN DO:**
- Negotiate terms (size, rate, maturity, covenants)
- Form SPV: "Santander Facility I, S.L."
- Execute credit agreement
- Draw initial tranche (test)

**Expected result:** €80-120M facility at 40-60% LTV

---

### Week 5-8: On-Chain Integration

**Deploy infrastructure:**

1. **Proof Server** (FastAPI + PostgreSQL)
   - Banker uploads daily statements
   - Extracts balance, blocked funds
   - Exposes API for Chainlink

2. **Chainlink Adapter** (Node.js)
   - Calls Proof Server daily
   - Returns facility available (1e18 scaled EUR)

3. **Smart Contracts** (Solidity)
   - `SantanderFacilityFeed` (oracle storage)
   - `FacilityRegistry` (capacity calculator)
   - `TGUSDSantanderPool` (stablecoin)

**Expected result:** $80-120M TGUSD minting capacity, backed by oracle-verified facility

---

### Week 9-10: First Issuance

**Launch:**
- Mint $10M TGUSD (test amount)
- Publish Bank Filings page section
- Issue private placement memo (if doing notes)
- First investor/partner onboarding

**Success metric:**
- External auditor can verify:
  - Bank facility exists (credit agreement)
  - Oracle updates daily (Chainlink logs)
  - Stablecoin minting never exceeds oracle-verified capacity
  - Full IPFS document trail

---

## SECTION 3: RUBY PLAYBOOK (SECOND PRIORITY)

### Week 1-2: Appraisal Verification ($5-10K)

- [ ] Contact HDG Appraisal Group (confirm cert authentic)
- [ ] Commission fresh appraisal (3+ years old = stale)
  - Budget: $15-30K
  - Source: Sotheby's, Christie's, or GIA-certified appraiser
- [ ] Get GIA reports for individual high-value stones
  - Budget: $300-500 per stone
- [ ] Confirm custody (licensed vault, not "safe somewhere")
- [ ] Get insurance quotes (Lloyds, Chubb)
  - Budget: 0.5-2% annual premium ($1.1-4.5M/year for $376M)

**STOP CONDITIONS:**
- HDG doesn't confirm appraisal
- Fresh appraisal <50% of original
- No insurer will quote or premiums >5%
- Custody unclear or insecure

**If any STOP condition → Downgrade to Tier 3, do not proceed.**

---

### Week 3-6: Lender Outreach

**Contact 3-5 real lenders:**
- Art/jewelry lenders: Borro, Luxury Asset Capital
- Private bank art finance: Citi, JPM, UBS
- Family offices (specialist lenders)

**Present package:**
- Fresh appraisal
- GIA reports
- Custody agreement
- Insurance policy
- Legal opinion on title

**Ask:** "What LTV, rate, and ticket size will you offer?"

**STOP CONDITION:** Zero lenders provide term sheets → Downgrade to Tier 2 or 3.

**IF SUCCESS:** Proceed to facility structuring (same as Santander, weeks 7-10).

---

## SECTION 4: IQD BOXES / OIL CERTS (LOW PRIORITY, TIME-BOXED)

### Week 1-2: Reality Check (20 hours max)

- [ ] Inventory: Photos of opened boxes, denominations, counts
- [ ] IQD market check: Can you sell at any real rate?
  - eBay, currency dealers, forex platforms
  - If only "RV groups" buying → it's a scam, STOP
- [ ] Oil cert legal opinion ($5-10K)
  - Hire oil & gas lawyer (not generalist)
  - Question: Is this enforceable contractual right?

**STOP CONDITION:** Lawyer says "not enforceable" AND IQD has no real market → Downgrade to Tier 3 immediately.

---

### Week 3-4: Market Sounding (Only if Phase 1 Shows Hope)

- [ ] Contact currency dealers (for IQD)
- [ ] Contact commodity traders (for oil certs)
- [ ] Get binding quotes

**DECISION:**
- Best offer >10% of claimed value → Execute sale, bank proceeds
- Best offer <10% → Downgrade to Tier 3

**DO NOT:**
- Build vaults/oracles for IQD boxes
- Include in capital calculations before monetization
- Spend >40 hours total on this

---

## SECTION 5: CHINESE BONDS (MINIMAL EFFORT)

### Week 1: Authentication Only

- [ ] Contact scripophily expert (R.M. Smythe, Spink)
- [ ] Send high-res scans
- [ ] Get: "Authentic" vs. "Reproduction"
- [ ] If authentic, get collector value quote ($50-500 per bond)

**DO:**
- Document (photos, IPFS)
- Archive securely
- Maybe sell a few to collectors for small cash

**DO NOT:**
- Hire lawyers to enforce payment (courts always reject)
- Join "bondholder associations" (all scams)
- Build infrastructure
- Include in capital calculations

**Assign:** Tier 3, zero value, optionality only.

---

## SECTION 6: INTEGRATION CHECKLIST (FOR TIER 1 ASSETS ONLY)

Once asset passes verification and you have lender term sheet:

### Pre-Integration (Week 1)

- [ ] Form SPV for this asset (`[Asset] Vault I, LLC`)
- [ ] Execute facility/loan agreement with lender
- [ ] Perfect security interest (UCC-1 filing, pledge)
- [ ] Bundle all docs → PGP sign → IPFS upload → get CID

### Vault Creation (Week 1)

- [ ] Mint Vault NFT on private ledger:
  ```yaml
  vault_id: VLT-[ASSET-CLASS]-[ID]-[YEAR]
  asset_type: [Type]
  appraised_value_usd: [Amount]
  facility_id: FAC-[ID]
  facility_size_usd: [Amount]
  ipfs_docs_cid: [CID]
  risk_tier: Tier_1
  current_ltv_pct: [%]
  ```

### Oracle Setup (Week 2-3)

- [ ] Build Proof Server (if new asset class)
  - Ingests verification docs (statements, appraisals, vault receipts)
  - Exposes `/latestProof` API

- [ ] Build Chainlink External Adapter
  - Calls Proof Server
  - Returns normalized value (1e18 scaled)

- [ ] Deploy Oracle Feed Contract
  - Stores latest value from Chainlink
  - Emits events on update

### Facility & Stablecoin (Week 3-4)

- [ ] Deploy FacilityRegistry (if first facility)
- [ ] Add facility to registry (ID, cap, LTV, oracle feed)
- [ ] Deploy stablecoin pool (or add facility to existing)
  - Mint cap = oracle-verified capacity × collateralization factor

- [ ] Test mint/burn flows

### Reporting (Week 4)

- [ ] Add section to Bank Filings page:
  ```markdown
  ### [Facility Name]
  **Backing:** [Asset type]
  **Facility Size:** [Amount]
  **Last Verification:** [Timestamp]
  **Facility Available:** [Oracle value]
  **Stablecoins Issued:** [Amount]
  **Collateralization:** [%]
  **Status:** ✅ / ⚠️ / 🔴
  **Documentation:** [IPFS links]
  ```

- [ ] Update investor reports
- [ ] Optional: Issue private placement memo

---

## SECTION 7: DAILY OPERATIONS (ONCE LIVE)

### Every Morning (10 minutes)

- [ ] Check CloudWatch: Did oracle update successfully?
- [ ] Review facility dashboard: Any anomalies?
- [ ] Check collateralization ratios: All >120%?

**If any alert:**
- Review logs
- Check Proof Server
- Contact banker/custodian if needed
- Manual oracle trigger if transient error

---

### Every Week (30 minutes)

- [ ] Review mint/burn activity (utilization %)
- [ ] Check facility draws vs. on-chain minting (should match)
- [ ] Rotate API keys if security log shows issues
- [ ] Update investor reports

---

### Every Month (2 hours)

- [ ] Reconcile on-chain state vs. off-chain facilities
- [ ] Update IPFS bundles (new statements/appraisals)
- [ ] Review insurance renewals (if applicable)
- [ ] External security scan on Proof Server

---

### Every Quarter (1 day)

- [ ] Fresh appraisals (if required by lender or policy)
- [ ] Audit vaults/custody (physical check or statement review)
- [ ] Facility renewal negotiations (if approaching maturity)
- [ ] Optional: External audit of entire vault system

---

## SECTION 8: EMERGENCY PROCEDURES

### Scenario 1: Oracle Feed Fails

**Symptoms:** Chainlink job fails 3+ times, no on-chain update

**Response:**
1. Check adapter logs (is Proof Server responding?)
2. Check Proof Server (is it healthy? Recent statement uploaded?)
3. If transient: Manually trigger Chainlink job
4. If persistent (>24hrs): Freeze affected stablecoin pool (emergency multisig)
5. Notify investors via governance forum
6. Fix root cause before unfreezing

---

### Scenario 2: Collateralization Drops Below 110%

**Symptoms:** Dashboard alert, ratio <110% (target: 120%)

**Response:**
1. Verify oracle data (is facility actually lower, or oracle issue?)
2. If real facility drop: Contact banker/lender immediately
3. Options:
   - Freeze new minting (preserve ratio)
   - Encourage redemptions (reduce outstanding)
   - Draw more facility (if available)
   - Add additional collateral (another vault)
4. Communicate to holders: "Temporary ratio squeeze, being addressed"

**Critical threshold:** <100% = full freeze + redemption priority mode

---

### Scenario 3: Lender Terminates Facility

**Symptoms:** Bank notice of non-renewal or early termination

**Response:**
1. Immediate freeze on new minting
2. Refinance urgently:
   - Approach 3-5 alternative lenders
   - Present existing structure (vault, oracle, track record)
   - Goal: Seamless facility transfer
3. If refinance fails:
   - Orderly wind-down (redeem all outstanding)
   - Sell underlying asset to cover redemptions
   - Communicate timeline to holders

**Timeline:** Aim to refinance within 30 days of notice.

---

### Scenario 4: Proof Server Compromised

**Symptoms:** Suspicious access logs, unexpected proof uploads

**Response:**
1. **IMMEDIATE:** Freeze oracle feed (prevent compromised data on-chain)
2. Rotate all API keys
3. Audit recent proofs (are they legitimate?)
4. Contact banker directly (verify recent statements out-of-band)
5. If fake proof made it on-chain:
   - Emergency multisig overrides oracle value
   - Freeze affected pools
   - Investigate + fix before resuming

**Prevention:** IP whitelist, 2FA for uploads, immutable audit logs.

---

## SECTION 9: CAPITAL ALLOCATION DECISION MATRIX

**Use this to decide how much effort/money to invest in each asset:**

| Asset | Est. Facility Size | Verification Cost | Time to Facility | Effort Justified? |
|-------|-------------------|-------------------|------------------|-------------------|
| **Santander cheques** | €80-120M | €50-100K | 8-10 weeks | ✅ YES (Priority 1) |
| **HDG Rubies** | $20-30M | $50-100K | 10-12 weeks | ✅ YES (Priority 2) |
| **IQD Boxes** | $0-1M (realistic) | $10-20K | 4 weeks max | ⚠️ MAYBE (time-boxed) |
| **Chinese Bonds** | $5-20K (collector) | $5-10K | 1 week | ⚠️ MINIMAL (auth only) |
| **Generic "Gold Cert"** | ??? | $0 (triage) | 1 week | 🔴 STOP unless vault visit possible |

**Decision Rule:**

> **Expected Facility Size ≥ 5× Verification Cost**

- Santander: €100M facility ≥ 5× €50K cost ✅
- Rubies: $25M facility ≥ 5× $50K cost ✅
- IQD: $500K proceeds < 5× $20K cost (but could still be worth it as quick win)
- Chinese Bonds: $10K collector sales < 5× $10K legal fight ❌

---

## SECTION 10: THE UNYKORN ADVANTAGE

**What makes your system different from traditional finance:**

### Traditional Bank:
- "Trust us" reserves (no proof)
- Opaque collateral (no public verification)
- Synthetic derivatives (circular collateral loops)
- Quarterly audits (stale data)

### Unykorn System:
- **Daily PoR:** Chainlink oracle updates every 24 hours
- **Public transparency:** Explorer shows facility value, mint caps, collateralization
- **Mechanical enforcement:** Smart contracts prevent over-minting
- **IPFS documentation:** Every vault has full evidence bundle
- **Tier separation:** Tier 3 assets never appear in capital calculations

**When you sit with a regulator/investor, you can say:**

> "Here's our live facility (€100M, verified by Chainlink 18 hours ago). Here's our stablecoin issuance ($85M, capped at 90% of facility). Here's the collateralization ratio (124%). Here's the evidence (IPFS bundle with bank statements). And here's what we DON'T count (Tier 3 archive — documented but zero value)."

**That's institutional credibility no "trust me bro" stablecoin can match.**

---

## CONCLUSION: YOUR NEXT 48 HOURS

**If you do nothing else, do this:**

### Hour 1-2: Santander Verification Email

Draft email to Santander RM:

> Subject: Facility inquiry — IBAN ES21…2112, Forum Europe S.L.
>
> Dear [RM Name],
>
> We are exploring the possibility of establishing a credit facility or blocked funds arrangement secured by the 10× €20M negotiable cheques (series [numbers]) tied to IBAN ES21 0049 5656 5323 1000 2112 (holder: FORUM EUROPE S.L.).
>
> Could you please confirm:
> 1. Are these instruments certified/cashier's cheques with funds currently blocked?
> 2. Would Santander be willing to issue a blocked funds letter for proof-of-funds purposes?
> 3. Alternatively, could we discuss converting these into a formal credit facility or SBLC?
>
> We can schedule a call this week to discuss terms.
>
> Best regards,
> [Your Name]

**Send this today.** This is your highest-leverage action.

---

### Hour 3-4: Ruby Verification Call

Contact HDG Appraisal Group:

> "We have a copy of appraisal certificate [number] dated October 2021 for a ruby collection valued at $376.7M. Can you confirm:
> 1. This appraisal is in your system (not forged)?
> 2. The appraiser is/was on your staff?
> 3. Process for obtaining an updated appraisal?"

**If they confirm: Schedule fresh appraisal.**
**If they deny: Stop immediately, downgrade to Tier 3.**

---

### Hour 5-8: Build Decision Framework

Take the four assets you have (Santander, Rubies, IQD, Chinese Bonds) and fill out this table:

| Asset | Current Tier | Verification Action | Budget | Timeline | Stop Condition | Expected Outcome |
|-------|--------------|---------------------|--------|----------|----------------|------------------|
| Santander | 1 (pending) | Bank call + facility negotiation | €50K | 8 weeks | Bank denies facility | €100M credit line |
| Rubies | 1.5 (pending) | Fresh appraisal + lender outreach | $50K | 10 weeks | No lender bites | $25M loan |
| IQD | 2 (speculative) | Legal opinion + market test | $20K | 4 weeks | No buyer found | $0 or $500K sale |
| Chinese | 3 (archive) | Authentication only | $5K | 1 week | N/A | $10K collector sales |

**This is your roadmap for the next 90 days.**

---

### After 48 Hours:

**You'll have:**
- Santander RM response (go/no-go on facility)
- HDG appraisal confirmation (go/no-go on fresh valuation)
- Clear decision matrix (where to invest time/money)

**You'll know:**
- Which assets are Tier 1 (build infrastructure)
- Which are Tier 2 (time-boxed verification)
- Which are Tier 3 (archive and forget)

**You'll avoid:**
- Wasting months chasing "maybes"
- Building infrastructure for zero-value assets
- Pretending hopium is collateral

**You'll become:**
- The adult in the room
- The system that admits what's real
- The platform that banks can actually work with

**Now go send that Santander email. Everything else flows from that one action.**
