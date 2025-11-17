# UNYKORN RWA OPERATIONS MANUAL

**Real-World Asset Lending & Tokenization**  
*Institutional Operations Guide*

**Version:** 1.0  
**Date:** November 2025  
**Classification:** Confidential — For Internal & Partner Use

---

## Executive Summary

This manual documents the **actual operational mechanics** of the Unykorn Real Assets platform:

- How external capital providers plug in
- Where custodians and gateways fit
- How money flows from investor to asset and back
- Why XRPL + owned node infrastructure creates institutional credibility
- Concrete workflows for asset intake, investor onboarding, and lifecycle management

This is not aspirational — this is the **blueprint for operations**.

---

## Table of Contents

1. [External Capital Providers](#1-external-capital-providers)
2. [Custodians & Gateways](#2-custodians--gateways)
3. [Money Flow Architecture](#3-money-flow-architecture)
4. [SPV Structure Template](#4-spv-structure-template)
5. [Credibility Framework](#5-credibility-framework)
6. [Asset Onboarding Workflow](#6-asset-onboarding-workflow)
7. [Investor Intake Playbook](#7-investor-intake-playbook)
8. [Real Estate Fractionalization](#8-real-estate-fractionalization)
9. [Lender Materials](#9-lender-materials)

---

## 1. External Capital Providers

### Who Actually Funds Your Deals?

Three categories of external capital will fund asset-backed deals structured through Unykorn SPVs:

---

### A) Private Credit Funds

**What they are:**  
Institutional funds specializing in asset-backed lending outside traditional bank channels.

**What they lend on:**
- Real estate (income-producing, development, hospitality)
- Mining operations (gold, lithium, rare earth)
- Water rights and infrastructure
- Government receivables and T-bills
- Equipment financing
- Construction projects (Hilton, Marriott, IHG contracts)

**Why they lend to Unykorn SPVs:**
- **Senior secured position** in clearly documented collateral
- **LTV ratios** appropriate to asset class (50-80%)
- **Verified collateral** with custodian statements + VaultProof records
- **Strong yields** (10-14%+ depending on asset)
- **Transparent reporting** via XRPL-backed dashboards

**How they plug in:**
- Wire fiat (USD, EUR) to SPV bank account or custodian
- Receive senior secured note or loan participation
- Get digital position record on XRPL for transparent tracking

**Credibility boost from XRPL:**
- Cannot fake mint/burn events
- Cannot manipulate reporting
- Cannot hide transactions
- Live proof of collateral coverage
- Immutable payment history

Private credit funds value your **owned XRPL node fleet** because it eliminates:
- RPC failures and third-party dependencies
- Data manipulation risks
- Dashboard fabrication
- Reporting opacity

**Your node = your truth oracle.**

---

### B) High-Net-Worth Individuals & Family Offices

**What they want:**
- Safe yield (8-15%) backed by real assets
- Proof of collateral
- Clear LTV and waterfall structure
- Fast subscription process
- Ongoing transparency

**What they fund:**
- Real estate credit notes
- Gold-backed yield notes
- Mining production notes
- Trade finance participations
- T-bill backed programs
- Construction lending

**What they care about (in order):**
1. **Collateral** — What backs this?
2. **LTV** — How much cushion do I have?
3. **Transparency** — Can I see real-time status?
4. **Custody** — Who holds the assets?
5. **Ledger** — Who runs the books? (You, via XRPL nodes)

**How they plug in:**
- Sign subscription agreement
- Wire fiat → SPV bank/custodian account
- Receive token or digital note representing position
- Get interest paid monthly or quarterly

**Your system advantage:**
- Eliminates PDF chaos
- Shows real-time collateral status
- Displays SPV cash balances
- Tracks distributions automatically
- Provides immutable audit trail

**Family offices love accounting clarity** — your XRPL infrastructure delivers it.

---

### C) OTC Desks, Brokers & Syndicators

**What they are:**  
Intermediaries who **bring investors**, not their own capital.

**What they route to you:**
- HNW clients seeking yield
- Accredited investors
- Other funds
- Private credit desks
- Corporate treasury managers

**Why they like you:**
- You provide **real products** (not vaporware)
- With **real proof** (custody + ledger)
- That they can sell fast
- Without legal minefields

**Your system speeds up:**
- Paperwork (digital agreements, e-signature)
- Identity verification (automated KYC/KYB)
- Onboarding (investor portal)
- Reporting (real-time dashboards)

**They become your sales force.**

Typical broker/syndicator compensation:
- 0.5-2% placement fee
- Or ongoing trailer (0.25-0.5% annual on AUM placed)

---

## 2. Custodians & Gateways

### The Adult in the Room

Institutional credibility requires **third-party verification and custody**. Here's where custodians and gateways fit:

---

### A) Custodians (Hold Assets & Provide Proof)

**Role:**  
Hold collateral assets so **you cannot unilaterally access them**.

**What they hold:**
- T-bills and government securities
- Cash reserves
- Physical gold (via depository sub-custodian)
- Securities and bonds
- Client subscription funds
- SPV operating accounts

**What they do:**
- Verify asset exists
- Issue proof statements (monthly/quarterly)
- Hold collateral in segregated accounts
- Support audits
- Enable institutional onboarding

**What they DON'T do:**
- Take investment risk
- Make credit decisions
- Guarantee performance

**They hold and record. Period.**

---

### Traditional & RWA Custodians

**For fiat, T-bills, securities, real estate SPV accounts:**

| Custodian | Use Case |
|-----------|----------|
| **US Bank Global Corporate Trust & Custody** | Trustee/custodian for structured products, real estate securitizations, ABS/MBS, CLOs |
| **Wilmington Trust** | SPVs, securitizations, structured trusts |
| **BNY Mellon** | Global custody, fund admin, collateral management |
| **Apex Group / IQ-EQ / JTC** | Fund/SPV administration + custody support for PE/real estate funds |

**How they fit Unykorn:**
- Hold SPV cash, T-bills, securities
- Act as trustee on certain note issuances
- Issue monthly statements → feed into VaultProof records

---

### Digital Asset Custodians

**For BTC, ETH, stablecoins backing:**

| Custodian | Use Case |
|-----------|----------|
| **Anchorage Digital** | OCC-chartered digital bank + institutional custody |
| **BitGo** | Institutional digital asset custody, WBTC co-issuer |
| **Coinbase Custody** | Segregated institutional custody |

**How they fit Unykorn:**
- Hold BTC/ETH/stablecoins backing certain notes or stablecoin reserves
- Provide API or statements linking to proof layer
- Enable institutional-grade security for digital collateral

---

### B) Gateways & On/Off-Ramps (Move Money)

**Role:**  
Enable fiat ↔ crypto conversions and ACH/wire access.

**Key Providers (by category):**

| Provider | Function |
|----------|----------|
| **Stripe Treasury / Issuing** | Bank accounts, cards, payouts via partner banks |
| **Circle** | USDC business accounts, on/off-ramp infrastructure |
| **MoonPay / Transak / Wert** | Fiat → crypto on/off ramps for investors |
| **Plaid (with BaaS partner)** | ACH/wire access & account verification |

**How they fit:**
- Investor sends USD → gateway → SPV/custodian account
- Your system records subscription + mints digital position
- Distributions flow back: SPV → gateway → investor bank account

**Note:** Gateways don't hold long-term — they facilitate movement.

---

## 3. Money Flow Architecture

### Exact Path: Asset Owner → SPV → Investor → Returns

Here's the **precise flow** when you onboard a client asset and raise external capital:

---

### Step 1: Asset Owner Comes In

**Example assets:**
- Income-producing real estate
- Gold mine with offtake agreements
- Hilton development contract
- Water rights with municipal offtake
- Corporate receivables
- T-bills

**Asset owner brings:**
- Title, deed, or contract
- Appraisal or feasibility study
- Revenue/production history
- Entity documentation

---

### Step 2: Unykorn SPV Created

**Structure:**
- "Unykorn Real Assets SPV I, LLC" holds the asset
- Or sub-SPV created for specific asset class:
  - Unykorn Gold SPV
  - Unykorn Water SPV
  - Unykorn Hilton Projects SPV

**Legal setup:**
- SPV formation (Delaware, Wyoming, or offshore)
- Operating agreement
- Security agreements
- UCC-1 filings (if applicable)

---

### Step 3: Custodian/Trustee Engaged

**Bank or corporate trustee holds:**
- T-bills backing certain tranches
- Cash reserves
- Security interests (via assignments, control agreements)

**Specialized custodians hold:**
- Gold → metals depository
- Real estate → title company + escrow
- Contracts → legal escrow agent

**Critical point:**  
**You (Unykorn) don't hold the collateral.**  
Custodian = institutional trust.

---

### Step 4: Unykorn Infrastructure Models the Deal

**System creates:**
- LTV analysis
- Coupon structure
- Tenor (loan term)
- Collateral waterfall
- Payment schedule

**VaultProof record generated with:**
- Title/contract copies (hashed)
- Appraisals (hashed)
- Financial projections
- Custodian statements
- On-chain identity references

**Legal + technical pairing:**
- Legal: Subscription agreement, note, security agreement
- Technical: XRPL position, VaultProof record, dashboard access

---

### Step 5: Token/Note Created (But Not Yet Distributed)

**Example instruments:**
- "Unykorn Real Estate Credit Note 2026-A"
- "Unykorn Gold Yield Note Series 1"
- "Unykorn Water Project Bond 01"

**Structure:**
- Face value (e.g., $1M)
- Coupon (e.g., 12% annual)
- Term (e.g., 24 months)
- Collateral (specific asset in SPV)
- Waterfall (senior/subordinated)

**Not yet issued** — awaiting investor subscriptions.

---

### Step 6: Investor/Lender Onboarding

**Process:**
1. **KYC/KYB collection:**
   - Individual: Passport, proof of address, accreditation
   - Entity: Articles, operating agreement, beneficial ownership, officer IDs
2. **Investor classification:**
   - Accredited investor (US)
   - Qualified purchaser
   - Professional investor (international)
3. **Subscription agreement signed:**
   - Amount
   - Series/tranche
   - Risk disclosures
   - Rights and obligations

---

### Step 7: Funds Move Through Gateway to SPV/Custodian

**Fiat path:**
- Investor wires USD/EUR → SPV bank account at custodian
- Custodian confirms receipt
- Treasury team marks subscription as funded

**Stablecoin path (optional):**
- Investor sends USDC/FTHUSD → designated SPV wallet
- Your treasury node validates receipt
- Converted to fiat or held as stablecoin collateral

**Key point:**  
Investors do **not** send money to a blockchain address directly.  
Blockchain handles **reporting, not custody**.

---

### Step 8: XRPL System Finalizes Allocation

**Your system issues:**
- Ledger record (XRPL position entry)
- Token representing economic position (if tokenized)
- Dashboard access credentials

**Records:**
- Amount invested
- Series/tranche
- Collateral reference (VaultProof link)
- Payment schedule
- Rights (senior, subordinated, equity)

**Investor now sees:**
- Position in personal dashboard
- Collateral backing their note
- Payment schedule
- Real-time ledger proof

---

### Step 9: Ongoing Lifecycle

**Asset generates revenue:**
- Real estate: Rental income
- Mine: Gold sales / offtake payments
- Contract: Milestone payments
- T-bills: Interest income

**SPV receives cash:**
- Flows to custodian account
- Treasury team applies waterfall:
  1. Operating expenses
  2. Senior creditors (your investors)
  3. Subordinated creditors
  4. Equity holders

**Distributions recorded:**
- **Legal:** Wire from custodian to investor accounts
- **Technical:** XRPL ledger entries logged via your nodes
- **Reporting:** Dashboard updates automatically

**Transparency:**
- Outstanding principal
- Interest paid to date
- Next payment due
- Collateral coverage ratio

**Everything a serious lender cares about is visible and provable.**

---

## 4. SPV Structure Template

### Clean Legal Spine

This is the **minimal viable SPV framework** you'd use (expand with counsel):

---

**UNYKORN REAL ASSETS SPV I, LLC**  
Jurisdiction: Delaware / Wyoming / Cayman Islands

---

### Purpose

To acquire, hold, and finance real-world assets including:
- Real estate
- Mineral rights
- Water rights
- Contractual receivables
- Government securities
- Infrastructure contracts

And to issue secured notes and participations in connection therewith.

---

### Manager

**Unykorn Capital Management, LLC**  
(or equivalent management entity)

Responsible for:
- Deal sourcing
- Due diligence
- Investor relations
- Compliance
- Reporting

---

### Custodian/Trustee

**[Name of bank or corporate trustee]**

To hold in segregated accounts on behalf of the SPV and its investors:
- Cash reserves
- Securities (T-bills, bonds)
- Security interests (via control agreements)

Supports:
- Institutional onboarding
- Audit procedures
- Third-party verification

---

### Security & Collateral

All investor/lender claims are secured by:
- **Perfected security interest** in underlying SPV assets
- **Documented via:**
  - Security agreements
  - UCC-1 filings
  - Assignments
  - Custodial control agreements

**Collateral waterfall:**
1. Senior secured creditors
2. Subordinated creditors
3. Equity holders

---

### Record-Keeping & Ledger

**Legal records:**  
Maintained in corporate books and records (traditional).

**Technical records:**  
All economic positions, cashflows, and collateral references are **mirrored** to the XRPL-based Unykorn ledger.

**XRPL infrastructure:**
- 3-node mainnet fleet (core / treasury / member API)
- Controlled by Manager
- Provides tamper-resistant, time-stamped proof of:
  - Issuance
  - Transfers
  - Payments
  - Redemptions

**Important note:**  
On-chain entries **do not replace** legal contracts.  
They serve as **immutable audit trail** and **transparency layer**.

---

### Use of Proceeds

SPV funds are used to:
- Acquire or finance eligible assets
- Fund loans and structured products
- Pay operating expenses
- Pay fees to Manager, Custodian, and service providers
- Distribute returns to investors per waterfall

---

### Regulatory Compliance

**Securities offerings:**
- Reg D 506(b) or 506(c) (US accredited investors)
- Reg S (international)
- Private placement exemptions

**Reporting:**
- Quarterly unaudited financials to investors
- Annual audited financials (if required by offering docs)
- Monthly VaultProof updates + XRPL dashboard access

---

### Dissolution & Wind-Down

Upon maturity or early termination:
- Assets liquidated or returned
- Waterfall applied
- Investors receive final distributions
- SPV dissolved per operating agreement

---

**This structure makes lawyers and funds nod instead of back away.**

---

## 5. Credibility Framework

### Why Institutions Trust Unykorn's RWA Platform

This section explains **how your XRPL infrastructure creates institutional credibility**.

---

### A) Real Assets, Real SPVs

**Not DeFi theater:**
- Each deal sits in a **dedicated SPV**
- Clear title, collateral documentation
- Custodian/trustee relationships
- Traditional legal agreements

**Investors see:**
- Legal entity structure
- Officers and directors
- Registered agent
- Bank accounts at real banks

**Plus:**
- XRPL-backed transparency layer
- Live proof of reserves
- Immutable transaction history

---

### B) Custodied Collateral

**Cash, T-bills, securities:**
- Held at qualified custodians / corporate trustees
- Segregated accounts
- Monthly statements

**Physical assets:**
- Gold → metals depository (e.g., Brink's, Loomis)
- Property → title company + escrow
- Contracts → legal escrow agents

**Investors know:**
- You cannot unilaterally access collateral
- Third-party verification exists
- Audit trail is clean

---

### C) XRPL-Backed Truth Layer

**This is your differentiator.**

Traditional funds give:
- Quarterly PDF reports
- Excel spreadsheets
- "Trust us" emails

**You give:**
- **Live ledger proof** via owned XRPL nodes
- **Immutable transaction history**
- **Real-time dashboards** showing:
  - Positions
  - Collateral coverage
  - Payment history
  - Outstanding balances

**What investors see:**
- How many notes/tokens minted
- When distributions occurred
- Current collateral ratios
- Transaction confirmations

**What they can trust:**
- You run your own 3-node fleet
- No reliance on third-party RPC (no data manipulation risk)
- Mint/burn events cannot be faked
- Payment records cannot be altered

**This is the same credibility mechanism Circle uses for USDC attestation.**

---

### D) Bank-Compatible, Not "DeFi Anarchy"

**Traditional side:**
- Bank accounts
- Custodians
- Legal agreements
- Subscription documents
- Wire transfers

**Modern side:**
- Programmatic ledger (XRPL)
- Automation (payments, reporting)
- Dashboards (investor portals)
- Instant settlement (optional for secondary)

**Result:**
- Regulatory clarity
- Institutional comfort
- Operational efficiency

---

### E) Ready for Funds & Family Offices

**Deal structures they already know:**
- Senior secured notes
- Loan participations
- Preferred equity
- Revenue-sharing agreements

**Reporting they don't get elsewhere:**
- Real-time positions
- Live collateral tracking
- Immutable payment history
- API access for their systems

**Speed they crave:**
- 4-8 weeks from handshake to funded deal
- vs. 6-12 months in traditional markets

---

### Summary: Why Your Node Fleet Matters

Private credit funds and family offices **love** that you run your own XRPL infrastructure because:

1. **No RPC failures** — You control uptime
2. **No data manipulation** — Ledger is immutable
3. **No fake dashboards** — Your nodes = source of truth
4. **No hidden transactions** — Everything logged
5. **Instant verification** — Anyone can audit the chain

**Your node = your truth oracle.**

That's worth 100-200 basis points of credibility premium in pricing.

---

## 6. Asset Onboarding Workflow

### From Raw Asset to Investable Product

This is the **exact process** for taking a client's asset and structuring it into a fundable deal:

---

### Step 0: Define the Product

**Asset identification:**
- Real estate / Gold / Water rights / T-bills / Contract / Other

**SPV selection:**
- Existing SPV or new sub-SPV?

**Instrument type:**
- Senior secured note
- Loan participation
- Preferred equity
- Revenue-sharing agreement

**Target parameters:**
- Yield: 10-14%
- Term: 12-36 months
- LTV: 50-75% (depending on asset)

---

### Step 1: Asset Due Diligence

**Documentation collected:**
- Title, deed, or contract (original or certified copy)
- Appraisal (within 6-12 months)
- Revenue history (if applicable)
- Operating statements
- Environmental reports (real estate)
- Geological reports (mining)
- Water rights certificates (water)
- Brand agreements (Hilton, Marriott contracts)

**Verification:**
- Title search
- Lien search
- UCC search
- Background checks on asset owner

**Risk assessment:**
- LTV calculation
- Market analysis
- Stress testing
- Legal review

---

### Step 2: SPV Formation & Asset Transfer

**If new SPV required:**
- Form LLC/trust
- Draft operating agreement
- Appoint manager/trustee
- Open bank account with custodian

**Asset transfer:**
- Purchase agreement or assignment
- Record deed (real estate)
- File UCC-1 (personal property)
- Assign contracts (revenue rights)

**Custodian engagement:**
- Custody agreement signed
- Collateral delivered
- Control agreement executed (for securities)

---

### Step 3: VaultProof Registration

**Create permanent record:**
- Asset ID (unique identifier)
- Asset class (real estate, mining, water, T-bills, etc.)
- Legal description
- Appraisal value
- LTV calculation
- Collateral position (senior/subordinated)

**Documentation hashing:**
- Title/deed → SHA-256 hash
- Appraisal → hash
- Operating agreement → hash
- Custodian statements → hash

**On-chain reference:**
- XRPL memo field or domain record
- Links legal docs to ledger position

---

### Step 4: Product Structuring

**Design the note/loan:**
- Face value: $500K - $10M (typical)
- Coupon: 10-14% annual
- Term: 12-36 months
- Payment frequency: Monthly/quarterly
- Collateral: Specific asset(s) in SPV
- Waterfall: Define senior/subordinated tranches

**Legal documents prepared:**
- Term sheet
- Subscription agreement
- Promissory note (if debt)
- Security agreement
- Disclosure documents

---

### Step 5: Regulatory Compliance

**Securities classification:**
- Reg D 506(c) (US accredited only)
- Reg D 506(b) (US accredited + up to 35 sophisticated)
- Reg S (international)

**Filings:**
- Form D (within 15 days of first sale)
- Blue sky notice filings (if required)

**Disclosures:**
- Risk factors
- Use of proceeds
- Manager compensation
- Conflicts of interest

---

### Step 6: Investor Marketing

**Target investors:**
- Private credit funds
- Family offices
- HNW individuals
- Broker-dealer networks

**Materials provided:**
- Investor presentation (10-15 slides)
- Term sheet (2-3 pages)
- VaultProof summary (asset verification)
- Financial projections

**Marketing channels:**
- Direct outreach
- Broker-dealer networks
- Fund platforms (e.g., iCapital, CAIS)
- Family office networks

---

### Step 7: Subscription & Funding

**See Section 7 (Investor Intake Playbook) for detailed process.**

Summary:
- Investor completes KYC/KYB
- Signs subscription agreement
- Wires funds to SPV/custodian
- Receives position on XRPL + dashboard access

---

### Step 8: Ongoing Asset Management

**Performance monitoring:**
- Revenue tracking (monthly)
- Collateral revaluation (annual or as needed)
- Covenant compliance
- Lien monitoring

**Reporting to investors:**
- Monthly: Cash flow, payment confirmations
- Quarterly: Financials, collateral status, VaultProof updates
- Annual: Audited financials (if required), tax documents (K-1s)

**Ledger updates:**
- All payments logged on XRPL
- Dashboard reflects real-time status
- Immutable audit trail maintained

---

### Step 9: Exit / Maturity

**At maturity:**
- Asset liquidated or refinanced
- Waterfall applied:
  1. Expenses
  2. Senior creditors (principal + interest)
  3. Subordinated creditors
  4. Equity holders
- Final distributions

**Ledger finalization:**
- Positions marked redeemed
- Final payment confirmations
- Archive VaultProof records

**Investor closeout:**
- Final statement
- Tax documents
- Return of original subscription docs (if requested)

---

## 7. Investor Intake Playbook

### Checklist for Every Lender/Investor

This is the **operational checklist** you (and staff) follow every time you onboard a lender or investor:

---

### Step 0: Define the Product

**Confirm:**
- Asset: [Real estate / Gold / Water / T-bills / Other]
- SPV: [Name, jurisdiction]
- Instrument: [Senior note / Loan participation / Preferred equity / Revenue share]
- Target yield: [10-14%]
- Term: [12-36 months]
- Minimum investment: [$25K - $100K typical]

---

### Step 1: KYC/KYB & Eligibility

**Individual investors — collect:**
- Government-issued photo ID (passport or driver's license)
- Proof of address (utility bill, bank statement)
- Accreditation verification:
  - Income ($200K individual / $300K joint for past 2 years)
  - Net worth ($1M+ excluding primary residence)
  - Professional certifications (Series 7, 65, 82)

**Entity investors — collect:**
- Articles of incorporation/formation
- Operating agreement or bylaws
- Certificate of good standing
- Beneficial ownership (FinCEN form)
- Officer/director IDs (same as individual)

**Screening:**
- OFAC sanctions lists
- PEP (politically exposed persons) databases
- Adverse media search
- AML red flag review

**Eligibility confirmation:**
- Accredited investor? (US)
- Qualified purchaser? (US, $5M+ investments)
- Professional investor? (International)
- Jurisdiction restrictions?

---

### Step 2: Legal Documents

**Prepare and send:**
- **Investor presentation** (10-15 slides)
  - Deal overview
  - Asset description
  - Collateral details
  - Terms & pricing
  - Risk factors
- **Term sheet** (2-3 pages)
  - Face value, coupon, term
  - Collateral and LTV
  - Payment schedule
  - Waterfall/priority
- **Subscription agreement** (10-20 pages)
  - Investment amount
  - Representations & warranties
  - Investor suitability
  - Signatures
- **Promissory note** or **loan agreement** (if debt)
- **Risk disclosures** (5-10 pages)
  - Market risks
  - Collateral risks
  - Liquidity risks
  - Regulatory risks

**Execution:**
- E-signature acceptable (DocuSign, HelloSign) if jurisdiction permits
- Wet signatures for certain jurisdictions (offshore, high-value)

**Receive:**
- Fully executed copies
- Store in secure document management system
- Link to investor record in CRM/database

---

### Step 3: Funding

**Provide wiring instructions:**
- Bank name, address, SWIFT/ABA
- Account name: [SPV name]
- Account number
- Reference: [Investor name + Series/Tranche]

**OR stablecoin instructions (if applicable):**
- Wallet address (SPV-controlled)
- Acceptable stablecoins (USDC, FTHUSD)
- Minimum confirmation blocks

**Confirmation process:**
- Custodian/bank confirms receipt
- Treasury team verifies amount and reference
- Mark subscription as "funded" in system
- Send confirmation email to investor

**Typical funding time:**
- Domestic wire: Same day or next day
- International wire: 1-3 days
- Stablecoin: 5-15 minutes

---

### Step 4: Record the Position

**Allocate investor amount:**
- Series/Tranche: [e.g., "2026-A Senior"]
- Position size: [$100,000]
- Effective date: [Funding date]

**Legal registry:**
- Add to SPV's investor ledger (cap table for equity, note register for debt)
- Record in corporate books

**XRPL-based digital record:**
- Mint token or issue position entry using treasury node
- Link to VaultProof asset record
- Assign to investor's wallet or ledger account

**Investor receives:**
- Confirmation statement (PDF + email)
- Dashboard login credentials
- Payment schedule
- Contact information for support

---

### Step 5: Ongoing Reporting

**Investor portal access:**
- Login: Secure, 2FA-enabled
- Positions tab: Shows all holdings
- Collateral tab: VaultProof summaries, asset performance
- Transactions tab: All payments, distributions, adjustments
- Documents tab: Agreements, statements, tax docs

**Automated reporting:**
- **Monthly:**
  - Payment confirmations (interest/coupon)
  - XRPL ledger entries (immutable proof)
  - Cash flow updates
- **Quarterly:**
  - Unaudited financials (SPV level)
  - Collateral revaluation (if applicable)
  - VaultProof updates
  - Performance metrics
- **Annually:**
  - Audited financials (if required by offering docs)
  - Tax documents (1099-INT, K-1, etc.)
  - Collateral appraisals (real estate, equipment)

**Alert triggers:**
- Payment delays
- Covenant breaches
- Collateral impairment
- Significant events (refinancing, early redemption offers)

---

### Step 6: Exit / Redemption

**At maturity:**
- Calculate final payment (principal + accrued interest)
- Process via custodian (wire to investor's bank)
- Log redemption on XRPL (position marked "redeemed")

**Early redemption (if permitted):**
- Investor requests redemption per terms
- Manager evaluates (may require liquidity event or secondary sale)
- If approved: Process same as maturity

**Investor closeout:**
- Final account statement
- Tax documents (1099, K-1)
- Confirmation of zero balance
- Archive all records per retention policy (typically 7 years)

**Ledger finalization:**
- XRPL position burned or marked inactive
- VaultProof updated to reflect redemption
- Dashboard shows "Closed" status

---

**This is the full loop:**  
Who → What → Where → When → How XRPL + your infrastructure support credibility and speed.

---

## 8. Real Estate Fractionalization

### How Your System Handles Property Deals

Real estate is the **fastest path to credibility** and capital. Here's the exact structure:

---

### Property Flow Diagram

```
┌─────────────────┐
│  Real Property  │ (Apartment, hotel, commercial site)
└────────┬────────┘
         │
         │ Legal transfer
         ▼
┌─────────────────────────────┐
│ Unykorn Real Estate SPV LLC │ (Owns property or long-term economic rights)
└────────┬────────────────────┘
         │
         │ Structured as:
         ├─── Senior Credit Notes (debt, secured by property)
         └─── Preferred Equity Tokens (profit-sharing, subordinated)
         │
         ▼
┌──────────────────┐          ┌─────────────────┐
│   Custodian Bank │          │ Unykorn Ledger  │
│                  │          │  (XRPL Nodes)   │
│ Holds:           │◄────────►│                 │
│ - SPV bank acct  │          │ Records:        │
│ - Rent escrow    │          │ - Note issuance │
│ - Reserves       │          │ - Distributions │
│ - Title docs     │          │ - Balances      │
└──────────────────┘          └─────────────────┘
         │                              │
         │                              │
         ▼                              ▼
┌─────────────────────────────────────────────┐
│              INVESTORS                      │
│                                             │
│ Senior Creditors:  10-12% fixed, secured   │
│ Equity Investors:  15-20%+ profit share    │
│                                             │
│ Each receives:                              │
│ - Legal agreement (note/equity docs)        │
│ - XRPL position (immutable ledger record)   │
│ - Dashboard access (real-time reporting)    │
└─────────────────────────────────────────────┘
```

---

### Step 1: Property Ownership

**Options:**

A) **SPV owns the property directly:**
   - Deed transferred to "Unykorn Real Estate SPV 1, LLC"
   - SPV is on title
   - Clear ownership

B) **SPV owns economic rights (alternative for complex deals):**
   - Original owner retains title
   - SPV receives long-term lease or profit-sharing agreement
   - Easier for international or legacy-encumbered properties

---

### Step 2: Custodian Engagement

**Bank/trustee holds:**
- SPV operating account
- Rent collection account (if income-producing)
- Reserve accounts (repairs, taxes, insurance)
- Escrow for sale proceeds (if eventual sale)

**Title company holds:**
- Original deed
- Title insurance policy
- Lien documentation

---

### Step 3: Capital Structure Design

**Two-tier structure (typical):**

#### Tier 1: Senior Credit Notes (Debt)

**Terms:**
- Face value: 60-75% of appraised value (conservative LTV)
- Coupon: 10-12% annual
- Term: 24-36 months
- Payment: Monthly interest, bullet principal at maturity
- Security: First lien on property

**Investor profile:**
- Conservative lenders
- Family offices seeking safe yield
- Private credit funds

**Priority:**
- First claim on cashflows (after operating expenses)
- First claim on sale proceeds

---

#### Tier 2: Preferred Equity (Subordinated)

**Terms:**
- Investment: 15-25% of appraised value
- Return: Profit share (e.g., 70/30 split after debt service)
- Term: Typically tied to asset hold period (3-7 years)
- Payment: Quarterly distributions from excess cashflow
- Exit: Sale proceeds after debt repayment

**Investor profile:**
- Sophisticated investors seeking higher returns
- Real estate syndicators
- HNW individuals with RE experience

**Priority:**
- Second claim (after senior debt service)
- Participation in upside (property appreciation)

---

### Step 4: Tokenization (Economics, Not Deed)

**What you DON'T do:**  
Tokenize the deed itself (too messy, regulatory minefield).

**What you DO:**  
Tokenize economic interests:

- **Senior Note Token:** 1 token = $1,000 face value of senior debt
- **Equity Share Token:** 1 token = 0.01% of net distributable cashflow

**Legal structure:**
- Tokens represent **contractual rights** per subscription agreement
- Not direct property ownership (avoids securities/property law conflicts)
- Clear in offering documents

---

### Step 5: Cashflow Waterfall

**Monthly operating flow:**

```
Rental Income (or other property revenue)
         ↓
    - Operating Expenses (management, maintenance, utilities, taxes, insurance)
         ↓
    - Debt Service (senior note interest + principal, if amortizing)
         ↓
    - Reserves (set aside for capex, vacancies)
         ↓
    - Preferred Equity Distributions (if excess cashflow available)
         ↓
    - Residual to Sponsor/Manager (if any remains)
```

**Sale proceeds flow:**

```
Gross Sale Price
         ↓
    - Transaction Costs (broker, legal, closing)
         ↓
    - Senior Debt Repayment (principal + accrued interest)
         ↓
    - Preferred Equity Return of Capital
         ↓
    - Preferred Equity Profit Share (per agreement, e.g., 70% to investors)
         ↓
    - Residual to Sponsor/Manager (remaining 30% or per agreement)
```

---

### Step 6: Reporting & Transparency

**Traditional side:**
- Monthly rent roll
- Quarterly financials (income statement, balance sheet)
- Annual appraisal updates
- Tax documents (K-1s for equity, 1099-INT for debt)

**Unykorn system adds:**
- **Real-time XRPL ledger** showing:
  - Note/token balances
  - Payment confirmations (immutable timestamps)
  - Distributions per investor
- **VaultProof dashboard:**
  - Property details (address, photos, description)
  - Appraisal summary
  - Occupancy/revenue metrics
  - Collateral coverage ratio (asset value / debt outstanding)
- **API access** for institutional investors who want to integrate into their systems

---

### Step 7: Investor Experience

**What senior note holders see:**
- Position: "$100,000 Senior Note 2026-A"
- Coupon: "12% annual, paid monthly"
- Next payment: "January 15, 2026 — $1,000"
- Collateral: "123 Main St, Anytown — Appraised $2.5M, LTV 60%"
- Payment history: List of all distributions with XRPL confirmation hashes

**What equity holders see:**
- Position: "1,000 Preferred Equity Tokens (1% of distributions)"
- Current yield: "18% annualized (trailing 12 months)"
- Property performance: Occupancy 95%, NOI $250K/year
- Exit projection: "Year 5 sale, estimated 2.1x return"

---

### Step 8: Why This Works

**Legal clarity:**
- SPV owns property → clear title chain
- Investors own contractual rights → securities law compliance
- Custodian holds cash → institutional credibility

**Operational efficiency:**
- Traditional property management (unchanged)
- Modern reporting (XRPL + dashboards)
- Automated distributions (smart contract triggers optional)

**Investor confidence:**
- Real asset backing (not speculative)
- Third-party custody (not operator-controlled)
- Immutable payment history (XRPL ledger)
- Live performance data (no waiting for quarterly PDFs)

---

### Why This Is Miles Ahead of "Fractional Real Estate" Gimmicks

**Typical fractional platforms:**
- Opaque SPV structures
- No real custody
- PDF-based reporting
- "Trust us" on valuations

**Unykorn real estate:**
- Institutional-grade SPV + custodian
- Live ledger proof via owned XRPL nodes
- Real-time dashboards
- Third-party appraisals linked to VaultProof

**Result:**  
Credible enough for family offices and private credit funds, not just retail speculators.

---

## 9. Lender Materials

### One-Pager for External Capital Providers

This is **copyable text** you can send to funds, family offices, and brokers:

---

# UNYKORN RWA CREDIT PLATFORM

**Information for Lenders & Investors**

---

## What We Do

Unykorn originates and structures **asset-backed credit opportunities** on top of real-world assets:

- **Real estate** (income-producing, development, hospitality)
- **Gold and precious metals** (mines, offtake agreements, vaulted assets)
- **Water rights** (municipal, agricultural, infrastructure)
- **Hospitality contracts** (Hilton, Marriott, IHG developments)
- **Treasury securities** (T-bills, government bonds)
- **Corporate receivables** (trade finance, invoices)

Each deal is housed in a **dedicated SPV** with clearly documented collateral, custodian relationships, and legal agreements.

---

## How You Lend

1. **Subscribe** to a specific note, loan participation, or credit product
2. **Fund** in fiat (USD, EUR) or stablecoins to a designated SPV/custodian account
3. **Receive:**
   - Legal claim (promissory note or loan agreement)
   - Digital position record on our XRPL ledger
   - Dashboard access for ongoing transparency

---

## Collateral & Protection

**All deals are secured by specific assets** documented in:
- Security agreements
- Title records or custody statements
- UCC-1 filings (perfected security interests)

**Cash, T-bills, and securities** are held at established banks or custodians with **segregated accounts**.

**Physical assets** (gold, property) are held via:
- Metals depositories (e.g., Brink's, Loomis)
- Title companies and escrow agents
- Third-party trustees

---

## Transparency & Reporting

We operate our own **3-node XRPL mainnet infrastructure**, which serves as a **tamper-resistant ledger** for:

- Issuance of positions
- Transfers and redemptions
- Interest and principal payments

**You can log into a secure portal to view:**
- Your positions (real-time balances)
- Deal-level collateral and performance
- Transaction history (immutable, time-stamped)
- Distribution confirmations (on-chain proof)

---

## Who This Is For

- **Private credit funds** seeking asset-backed yield (10-14%+)
- **Family offices & UHNW individuals** seeking safe, transparent investments
- **Broker-dealers & OTC desks** sourcing structured yield products for clients
- **Asset owners** looking to raise secured capital quickly

---

## Why It's Different

| Traditional Lenders | Unykorn RWA Platform |
|---------------------|----------------------|
| Quarterly PDF reports | Real-time ledger proof |
| Opaque SPV structures | Transparent, custodied collateral |
| 6-12 month deal timelines | 4-8 week execution |
| "Trust us" spreadsheets | Immutable XRPL audit trail |
| Limited visibility | Live dashboards + API access |

---

## Typical Terms

**Senior secured notes:**
- LTV: 50-75% (depending on asset)
- Yield: 10-14% annual
- Term: 12-36 months
- Payment: Monthly or quarterly
- Minimum: $25K-$100K (varies by deal)

**Preferred equity / profit-sharing:**
- Target returns: 15-20%+
- Term: 3-7 years (tied to asset hold period)
- Payment: Quarterly distributions + exit proceeds

---

## Deal Flow

**Current pipeline (example categories):**
- Real estate credit: $25M
- Gold-backed notes: $15M
- Water infrastructure bonds: $10M
- Hospitality project finance: $20M
- Treasury-backed programs: $50M

**Target annual origination:** $100M-$250M Year 1

---

## Contact

**Unykorn Capital Management, LLC**  
[Your contact info]

**Interested in learning more?**  
Request our full investor presentation, sample term sheet, or VaultProof demo.

---

**This document is for discussion purposes only and does not constitute an offer to sell or a solicitation of an offer to buy any securities. Any such offer or solicitation will be made only by means of a confidential private placement memorandum and related subscription documents.**

---

## Appendix: Infrastructure & Security

### XRPL Node Architecture

**We operate our own 3-node mainnet fleet:**

| Node | Role | Purpose |
|------|------|---------|
| **Core** | Routing, DEX, analytics | General ledger queries, market data |
| **Treasury** | Mint/burn, PoR-critical ops | Token issuance, reserve proofs, high-security operations |
| **Member API** | Balance queries, dashboards | Investor portal backend, read-only access |

**Why this matters to lenders:**
- No reliance on third-party RPC providers (no data manipulation risk)
- Full control over ledger views and logging
- Institutional-grade uptime and redundancy
- Audit trail integrity guaranteed

---

### VaultProof System

**Every asset in the SPV is mapped to a VaultProof record:**

- **Legal documents** (hashed for immutability)
- **Appraisals and valuations**
- **Custodian statements**
- **Revenue/production data**
- **On-chain references** (XRPL identifiers)

**Investors can verify:**
- What collateral backs their note
- Current valuations and LTV
- Custody arrangements
- Payment history

**This is end-to-end auditability** — not "trust us."

---

### Compliance & Regulatory

**Securities offerings:**
- Reg D 506(c) (US accredited investors)
- Reg S (international)
- Private placement exemptions

**Investor onboarding:**
- KYC/KYB (identity verification, source of funds)
- Accreditation checks (income, net worth, professional status)
- Sanctions screening (OFAC, PEP lists)

**Ongoing compliance:**
- Form D filings (SEC)
- Blue sky notices (state securities)
- AML monitoring
- Annual audits (where required)

---

## Sample Use Cases

### Use Case 1: Gold Mine Offtake Financing

**Asset:**  
Gold mine with verified reserves, existing offtake agreement with major refiner.

**Structure:**
- $5M senior secured note at 12% annual, 24-month term
- Collateral: First lien on offtake receivables + equipment
- LTV: 60% of projected offtake value

**Investor return:**
- $600K annual interest ($50K/month)
- Principal at maturity from offtake proceeds

**Unykorn revenue:**
- 2% origination ($100K)
- 1% annual servicing ($50K/year)
- Treasury spread on stablecoin liquidity (if applicable)

---

### Use Case 2: Apartment Building Acquisition

**Asset:**  
50-unit apartment building, 92% occupied, $750K annual NOI.

**Structure:**
- $4M senior note (70% LTV) at 10% annual, 36-month term
- $1M preferred equity (15% target return, profit-sharing)

**Investor returns:**
- **Senior:** $400K annual interest ($33K/month)
- **Equity:** Quarterly distributions from excess cashflow + exit proceeds

**Unykorn revenue:**
- 1.5% origination on debt ($60K)
- 3% origination on equity ($30K)
- 0.5% annual servicing ($25K/year)

---

### Use Case 3: T-Bill Backed Stablecoin Program

**Asset:**  
$20M in short-term T-bills held at qualified custodian.

**Structure:**
- Issue FTHUSD stablecoin backed 1:1 by T-bills
- Offer 4-5% yield to stablecoin holders (below T-bill yield)
- Retain 1.5-2% spread

**Investor returns:**
- 4-5% safe yield with T-bill backing
- Instant redemption (vs. holding T-bills directly)
- On-chain proof of reserves

**Unykorn revenue:**
- 1.5-2% treasury spread on $20M = $300K-$400K annual
- Minimal risk (fully collateralized)

---

## Summary

**Unykorn RWA Platform** = **Traditional finance meets modern infrastructure**

- Real assets, real SPVs, real custody
- XRPL-backed transparency and proof
- 4-8 week execution (vs. 6-12 months traditional)
- Institutional-grade reporting and compliance

**For lenders and investors who want:**
- Asset-backed yield (10-14%+)
- Transparent collateral
- Real-time reporting
- Operational efficiency

**Contact us to discuss specific opportunities or request deal flow.**

---

## End of RWA Operations Manual

**This document is confidential and intended for internal use and distribution to qualified institutional partners only.**

For questions or clarifications, contact:  
**Unykorn Capital Management, LLC**  
[Contact information]

**Last updated:** November 2025  
**Version:** 1.0
