# QUICK REFERENCE: MONEY FLOW & KEY PLAYERS

**The One-Page Answer to "How Does This Actually Work?"**

---

## The Simple Truth

**Unykorn doesn't replace banks. It adds proof.**

Traditional side:
- SPVs hold assets
- Custodians hold collateral
- Banks hold cash
- Lawyers draft agreements

Modern side:
- XRPL ledger provides immutable proof
- Your 3-node fleet = your truth oracle
- Dashboards show real-time status
- Automated compliance and reporting

---

## Who Gives You Money?

### 1. Private Credit Funds
**They lend:** $1M-$50M per deal  
**They want:** 10-14% yield, senior secured position, verified collateral  
**They plug in:** Wire fiat → SPV bank account

### 2. Family Offices & HNW
**They invest:** $100K-$5M per position  
**They want:** Safe yield (8-12%), transparency, real assets  
**They plug in:** Subscription agreement + wire

### 3. OTC Desks & Brokers
**They bring:** Other people's money (placement agents)  
**They want:** Clean products they can sell fast  
**They earn:** 0.5-2% placement fees

---

## Where Do Custodians Fit?

**Custodians = The Adult in the Room**

They hold (so you can't touch):
- Cash reserves
- T-bills and securities
- Gold (via depository)
- Title documents

**Real custodian types:**
- **Traditional:** US Bank, Wilmington Trust, BNY Mellon (for SPV accounts, T-bills, securities)
- **Digital:** Anchorage, BitGo, Coinbase Custody (for BTC/ETH/stablecoins)

Custodian statements → VaultProof → Dashboard

---

## Where Do Gateways Fit?

**Gateways = Money Movement Layer**

**On-ramps (fiat → crypto):**
- Circle (USDC business accounts)
- MoonPay, Transak (retail/institutional)
- Stripe Treasury (bank accounts, wires)

**Off-ramps (crypto → fiat):**
- Same providers, reverse flow

**Use case:**  
Investor wires USD → gateway → SPV account → your system records subscription

---

## Exact Money Flow

### When You Onboard an Asset:

```
Client brings asset (gold mine, hotel, water rights, T-bills)
         ↓
Form SPV (Unykorn Real Assets SPV I, LLC)
         ↓
Custodian holds collateral (bank, depository, title company)
         ↓
Your system creates VaultProof + tokenizes economics
         ↓
Investor onboards (KYC, subscription agreement)
         ↓
Investor wires funds → SPV/custodian
         ↓
Your XRPL system issues position (immutable record)
         ↓
Asset generates revenue → SPV → waterfall → investors
         ↓
All payments logged on XRPL (live proof)
```

---

## Why Your XRPL Nodes Matter

**Most platforms:** Trust third-party RPC (can be manipulated)  
**You:** Run your own 3-node mainnet fleet

**What this gives investors:**

1. **No RPC failures** — You control uptime
2. **No fake mint/burn events** — Ledger is immutable
3. **No hidden transactions** — Everything logged
4. **Instant verification** — Anyone can audit
5. **Real-time proof** — Live dashboards powered by your nodes

**This is the same credibility Circle uses for USDC attestation.**

Private credit funds value this at **100-200 bps of credibility premium**.

---

## Asset → Money Conversion (IOU Lending)

### Step 1: Intake Asset
Collect: title, appraisal, revenue data, compliance docs

### Step 2: Tokenize Asset
Create: VaultProof record, RWA token, IOU placeholder

### Step 3: Assign Loan Structure
Choose: credit line, term loan, bridge, revenue-share, pre-sale

### Step 4: Apply LTV
- Gold: 50-75%
- Real estate: 50-70%
- T-bills: 80-95%
- Water: 30-65%
- Lithium: 25-50%

### Step 5: Issue IOU on XRPL
Mint: "UNYK-LEND.IOU" or "ASSET-CREDIT.IOU"  
Backed 1:1 by collateral in SPV

### Step 6: Fund the Loan
Sources: your treasury, stablecoin liquidity, investors, OTC partners

### Step 7: Collect Revenue
- Origination fee: 1-5%
- Interest: 8-18% (typical RWA rates)
- Tokenization fee: 0.5-1%
- AUM fee: 1-4%

---

## Three Fastest Paths to Credibility + Cash

### 1. Real Estate Credit Notes
**Why:** Everyone understands buildings  
**LTV:** 50-70%  
**Yield:** 10-12%  
**Speed:** 2-3 weeks from handshake to funded

### 2. T-Bill Backed Stablecoin
**Why:** Safe, liquid, institutional-grade  
**LTV:** 80-95%  
**Spread:** 1.5-2% (you keep the spread)  
**Speed:** Same-day funding

### 3. Gold Yield Notes
**Why:** Sexy + solid collateral  
**LTV:** 60-75%  
**Yield:** 12-14%  
**Speed:** 24-72 hours

---

## What Makes This Institutional?

**Traditional funds give:**
- Quarterly PDF reports
- Excel spreadsheets
- "Trust us" emails
- 6-12 month deal timelines

**You give:**
- Live XRPL ledger proof
- Real-time dashboards
- Immutable transaction history
- 4-8 week execution

**Legal side:**
- Real SPVs (Delaware, Cayman)
- Real custodians (US Bank, Anchorage)
- Real bank accounts (not "trust the blockchain")
- Real legal agreements (Reg D, subscription docs)

**Technical side:**
- Your own XRPL nodes (no third-party dependencies)
- VaultProof records (all docs hashed and linked)
- Automated compliance (KYC/AML, sanctions screening)
- API access (for institutional integrations)

---

## Red Flags You Avoid

❌ **"Trust our dashboard"** — Anyone can fake a website  
✅ **"Verify on-chain"** — XRPL ledger is immutable

❌ **"We hold the collateral"** — Operator can abscond  
✅ **"Custodian holds collateral"** — Third-party verification

❌ **"Quarterly reports"** — Stale data, easy to manipulate  
✅ **"Live ledger"** — Real-time, tamper-proof

❌ **"DeFi yields"** — Anonymous, regulatory risk  
✅ **"Asset-backed notes"** — Real collateral, legal agreements

---

## Bottom Line

**External capital providers (private credit, HNW, OTC) plug into your Unykorn SPVs because you bring:**

1. **High-yield, asset-backed deals** (10-14%+)
2. **Better proof** (XRPL ledger + owned nodes)
3. **Faster execution** (4-8 weeks vs 6-12 months)
4. **Cleaner visibility** (dashboards + API access)

**You're not asking them to trust crypto.**  
**You're offering normal deals with better rails.**

---

## Next Steps

**For clients:** See `ASSET_LTV_MATRIX.md` (25 asset types you can accept)  
**For operations:** See `RWA_OPERATIONS_MANUAL.md` (full workflows)  
**For investors:** See `LENDER_ONE_PAGER.md` (what they get, how they invest)

**For legal setup:** See `SPV_TEMPLATES/` (formation docs, operating agreements)  
**For compliance:** See `COMPLIANCE_PLAYBOOK.md` (KYC/AML, Reg D, reporting)

---

**Last updated:** November 2025  
**Version:** 1.0
