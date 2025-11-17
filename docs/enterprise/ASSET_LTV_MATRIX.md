# ASSET CLASSIFICATION & LTV MATRIX

**The Complete RWA Lending Reference**

**Version:** 1.0  
**Date:** November 2025  
**Classification:** Internal Reference — Operations & Credit Teams

---

## Overview

This document catalogs the **25 most common real-world assets (RWAs)** accepted by private credit funds, OTC lenders, and asset-backed lending platforms.

For each asset class, we provide:

- **Typical LTV ranges** (Loan-to-Value)
- **Funding speed** (how fast capital can be deployed)
- **Tokenization approach** (how to IOU/tokenize on XRPL)
- **Documentation requirements**
- **Risk considerations**

This is the **institutional playbook** for asset-backed lending.

---

## Table of Contents

1. [Precious Metals](#1-precious-metals)
2. [Water Rights & Infrastructure](#2-water-rights--infrastructure)
3. [Energy & Mining](#3-energy--mining)
4. [Hospitality & Development](#4-hospitality--development)
5. [Government Securities](#5-government-securities)
6. [Land & Real Estate](#6-land--real-estate)
7. [Receivables & Trade Finance](#7-receivables--trade-finance)
8. [Digital Assets](#8-digital-assets)
9. [Other Asset Classes](#9-other-asset-classes)

---

## 1. Precious Metals

### 1.1 Gold (Mined, Unmined, Doré, Claims)

**LTV:** 40-75%  
**Funding Speed:** Fast (24-72 hours)

**Tokenization Approach:**
- Tokenize ounces into VaultProof records
- Issue "GOLD-OZ.IOU" or revenue-share tokens
- Create gold-backed stablecoin if verified and vaulted

**Required Documentation:**
- Geological survey and reserve reports
- Assay certificates (purity, quantity)
- Ownership documentation (mining claims, concessions)
- Offtake contracts (if any)
- Insurance certificates
- Environmental compliance

**Risk Considerations:**
- Price volatility (hedge with futures or collar strategies)
- Production risk (unmined reserves)
- Jurisdiction risk (political stability, mining regulations)
- Refining and transport logistics

**Typical Deal Structure:**
- Senior secured note backed by offtake receivables
- Equipment lien (mining machinery as additional collateral)
- Quarterly interest, bullet principal
- Personal guarantee from operator (if small-scale)

---

### 1.2 Silver, Platinum, Palladium

**LTV:** 30-60%  
**Funding Speed:** Fast (24-72 hours)

**Tokenization Approach:**
- Similar to gold: ounce-based IOUs
- Revenue-share tokens for producing mines

**Required Documentation:**
- Same as gold plus market hedging strategy (more volatile metals)

**Risk Considerations:**
- Higher price volatility than gold
- Industrial demand factors (auto, electronics)

---

## 2. Water Rights & Infrastructure

### 2.1 Water Rights (Municipal, Agricultural, Industrial)

**LTV:** 30-65%  
**Funding Speed:** Moderate (1-2 weeks)

**Tokenization Approach:**
- Tokenize water-credit units (e.g., acre-feet)
- Mint infrastructure-backed notes
- Use rights as collateral for construction finance

**Required Documentation:**
- State or municipal water rights certificate
- Historical usage data (5-10 years)
- Third-party appraisal of rights value
- Offtake agreements (if selling to municipality/utility)
- Hydrological reports

**Risk Considerations:**
- Regulatory risk (water law changes)
- Drought risk (climate variability)
- Priority issues (senior vs. junior rights)
- Environmental restrictions

**Typical Deal Structure:**
- Revenue-share note tied to water sales
- Construction loan for well/infrastructure development
- Quarterly distributions based on actual usage/sales

---

### 2.2 Wells & Water Infrastructure

**LTV:** 35-70%  
**Funding Speed:** Moderate

**Tokenization Approach:**
- Infrastructure-backed tokens
- Revenue-sharing agreements

**Required Documentation:**
- Engineering reports
- Permits and licenses
- Operating history

---

## 3. Energy & Mining

### 3.1 Lithium, Rare Earth & Battery Metals

**LTV:** 25-50%  
**Funding Speed:** Moderate (2-4 weeks)

**Tokenization Approach:**
- Tokenized forward offtake (pre-sale of future production)
- Miner revenue credits
- IOU-based pre-sale financing

**Required Documentation:**
- Geological survey and resource estimates (NI 43-101 or JORC standard)
- Government mining license
- Offtake agreements with battery manufacturers or traders
- Feasibility study (FS or PFS)
- Environmental impact assessment

**Risk Considerations:**
- Long development timelines (3-7 years typical)
- Capex intensity (requires significant infrastructure)
- Market risk (lithium prices highly cyclical)
- Permitting risk (environmental, indigenous rights)

**Typical Deal Structure:**
- Convertible note (debt converts to equity if mine succeeds)
- Revenue-based financing (% of future sales)
- Offtake prepayment (buyer advances funds against future delivery)

---

### 3.2 Oil & Gas Wells

**LTV:** 25-60%  
**Funding Speed:** Moderate

**Tokenization Approach:**
- Offtake tokens (barrels or MCF)
- Production-backed notes

**Required Documentation:**
- Lease agreements
- Operating agreements (if joint venture)
- Production history (decline curve analysis)
- Reserve reports (3P: proven, probable, possible)
- Revenue history

**Risk Considerations:**
- Commodity price risk
- Depletion (declining production over time)
- Regulatory and environmental liability

---

### 3.3 Solar Farms, PPAs, Utility Contracts

**LTV:** 40-65%  
**Funding Speed:** Moderate

**Tokenization Approach:**
- Tokenize kilowatt output
- PPA-backed yield tokens
- Construction financing notes

**Required Documentation:**
- Power Purchase Agreement (PPA) with utility or corporate offtaker
- Output certifications (capacity, expected generation)
- Equipment ownership and specifications
- Interconnection agreement
- Insurance (performance, equipment)

**Risk Considerations:**
- Technology risk (panel degradation)
- Offtaker credit risk
- Weather variability (less sun = less revenue)

---

### 3.4 Carbon Credits

**LTV:** 40-70%  
**Funding Speed:** Fast (once verified)

**Tokenization Approach:**
- Tokenized carbon offset credits
- Compliance-backed stable tokens

**Required Documentation:**
- Registry certificate (Verra, Gold Standard, etc.)
- Verification report (third-party)
- Project documentation (forestry, renewable energy, methane capture, etc.)

**Risk Considerations:**
- Market price volatility
- Regulatory changes (carbon markets)
- Verification standards (additionality, permanence)

---

## 4. Hospitality & Development

### 4.1 Hotel & Resort Development Contracts (Hilton, Marriott, IHG)

**LTV:** 20-60%  
**Funding Speed:** Fast (1-2 weeks for smaller deals)

**Tokenization Approach:**
- Fractional "Build Tokens" (represent equity in development)
- Construction drawdown notes (release funds as milestones hit)
- Revenue-share tokens (once operational)

**Required Documentation:**
- Developer agreement (legal contract with developer)
- Brand agreement (Hilton franchise agreement, management contract)
- Pro forma financials (revenue and cost projections)
- Feasibility study (market analysis, competitive set)
- Construction timeline and budget
- Permits and zoning approvals

**Risk Considerations:**
- Construction risk (delays, cost overruns)
- Market risk (occupancy, ADR may not meet projections)
- Brand performance (franchisee quality)
- Exit risk (liquidity for investors)

**Typical Deal Structure:**
- Senior construction loan (60-70% LTV on completed value)
- Mezzanine or preferred equity (higher risk, higher return)
- Milestone-based funding (draw against completed work)

---

## 5. Government Securities

### 5.1 T-Bills, Treasury Notes, Government Bonds

**LTV:** 80-95%  
**Funding Speed:** Instant (same-day)

**Tokenization Approach:**
- Tokenize into "UST.IOU" or "TBILL.IOU"
- Back stablecoins (e.g., FTHUSD 1:1 with T-bills)
- Use for liquidity lines or credit facilities

**Required Documentation:**
- Custodial statement (from broker or bank)
- CUSIP verification
- Broker/dealer confirmation
- Control agreement (if using as collateral)

**Risk Considerations:**
- Minimal credit risk (US government backing)
- Interest rate risk (price declines if rates rise)
- Liquidity (generally high, but can be impaired in crisis)

**Typical Deal Structure:**
- Repo-style financing (lender provides cash, takes T-bill as collateral)
- Stablecoin issuance (T-bills held in reserve, mint stablecoins against them)
- Credit line (draw against T-bill portfolio)

---

## 6. Land & Real Estate

### 6.1 Raw Land

**LTV:** 20-40%  
**Funding Speed:** Moderate (2-4 weeks)

**Tokenization Approach:**
- Land-tied stable yields (income from lease or future development)
- Fractionalized ownership tokens
- Collateralized credit lines

**Required Documentation:**
- Title (free and clear, or with acceptable liens)
- Survey and legal description
- Appraisal (third-party, recent)
- Zoning documentation
- Environmental Phase I (and Phase II if concerns)

**Risk Considerations:**
- Illiquid (hard to sell quickly)
- No income (typically)
- Zoning risk (may not get development approvals)
- Market risk (value depends on future use)

---

### 6.2 Agricultural Land

**LTV:** 35-60%  
**Funding Speed:** Moderate

**Tokenization Approach:**
- Revenue-share tokens (crop income)
- Land appreciation tokens

**Required Documentation:**
- Same as raw land plus:
- Crop history (yields, revenues)
- Soil quality reports
- Water rights (if applicable)

---

### 6.3 Commercial Real Estate (Income-Producing)

**LTV:** 50-70%  
**Funding Speed:** Moderate (2-3 weeks)

**Tokenization Approach:**
- Senior credit notes (debt)
- Preferred equity tokens (profit-sharing)
- Rental income-backed bonds

**Required Documentation:**
- Title and deed
- Appraisal (MAI-certified)
- Rent roll (tenant list, lease terms, occupancy)
- Operating statements (3 years historical)
- Environmental Phase I
- Property condition assessment

**Risk Considerations:**
- Tenant credit risk
- Lease rollover risk
- Property condition (capex needs)
- Market risk (cap rates, demand)

---

## 7. Receivables & Trade Finance

### 7.1 Invoice Receivables / Trade Finance

**LTV:** 60-90%  
**Funding Speed:** Rapid (24-48 hours)

**Tokenization Approach:**
- Tokenized invoice (each invoice = unique asset)
- Settlement-backed stablecoin
- Short-term credit notes (30-90 day terms)

**Required Documentation:**
- Invoice copy
- Purchase order (PO)
- Payor verification (confirm debtor will pay)
- Delivery confirmation (goods shipped/received)

**Risk Considerations:**
- Payor credit risk (will they pay?)
- Fraud risk (fake invoices)
- Recourse vs. non-recourse (who bears default risk?)

**Typical Deal Structure:**
- Invoice factoring (buy invoice at discount, collect full amount)
- Invoice financing (loan against invoice, seller retains ownership)
- Typical advance: 80-90% of invoice value
- Fees: 1-3% per month

---

### 7.2 Government Receivables (Contracts with Agencies)

**LTV:** 70-85%  
**Funding Speed:** Fast

**Tokenization Approach:**
- Receivable-backed tokens
- Revenue assignment notes

**Required Documentation:**
- Government contract
- Payment history
- Assignment of proceeds (legal right to collect)

**Risk Considerations:**
- Government budget risk (payment delays)
- Contract performance (must deliver to get paid)

---

## 8. Digital Assets

### 8.1 Bitcoin (BTC)

**LTV:** 50-70%  
**Funding Speed:** Instant (minutes)

**Tokenization Approach:**
- Wrapped reserve tokens (e.g., WBTC-style)
- Stablecoin collateral (lend stables against BTC)
- Credit line (draw cash against BTC holdings)

**Required Documentation:**
- On-chain proof of ownership (wallet address, signature)
- Custody arrangement (if held by third party)

**Risk Considerations:**
- Price volatility (requires margin calls or liquidation mechanisms)
- Custody risk (hacking, loss of keys)
- Regulatory uncertainty

**Typical Deal Structure:**
- Overcollateralized loan (150-200% LTV on volatile assets)
- Daily mark-to-market (adjust collateral requirements)
- Liquidation if collateral falls below threshold

---

### 8.2 Ethereum (ETH)

**LTV:** 40-60%  
**Funding Speed:** Instant

**Tokenization Approach:**
- Same as BTC (wrapped or collateralized)

**Risk Considerations:**
- Higher volatility than BTC
- Smart contract risk (if using DeFi protocols)

---

### 8.3 Stablecoins (USDC, USDT, DAI)

**LTV:** 90-100%  
**Funding Speed:** Instant

**Tokenization Approach:**
- Use as collateral directly (minimal haircut)

**Risk Considerations:**
- Counterparty risk (issuer solvency)
- Regulatory risk (stablecoin rules evolving)

---

## 9. Other Asset Classes

### 9.1 Private Company Shares / Equity

**LTV:** 10-35%  
**Funding Speed:** Moderate (2-4 weeks)

**Tokenization Approach:**
- Tokenized equity (security token)
- Convertible note tokens
- Locked collateral IOUs (shares held in escrow)

**Required Documentation:**
- Cap table (ownership structure)
- Shareholder agreement
- Valuation report (409A, third-party)
- Financials (audited if available)

**Risk Considerations:**
- Illiquid (no public market)
- Valuation uncertainty
- Dilution risk (future fundraises)

---

### 9.2 Sports & Entertainment Contracts

**LTV:** 10-40%  
**Funding Speed:** Fast

**Tokenization Approach:**
- Tokenize future earnings (athlete contracts, royalties)
- Revenue-share tokens
- Insurance-backed credit lines

**Required Documentation:**
- Proof of contract (player agreement, recording contract, etc.)
- Payment history (past earnings)
- Agent or manager attestation

**Risk Considerations:**
- Performance risk (injury, career decline)
- Contractual disputes
- Reputation risk

---

### 9.3 High-End Vehicles, Yachts, Aircraft

**LTV:**
- Exotic cars: 30-60%
- Yachts: 25-50%
- Private jets: 30-55%

**Funding Speed:** Fast (1 week)

**Tokenization Approach:**
- Tokenized title (digital lien)
- Collateralized loan tokens

**Required Documentation:**
- Title and registration
- Appraisal (NADA, Aircraft Bluebook, or marine surveyor)
- Insurance (comprehensive, agreed value)
- Maintenance records

**Risk Considerations:**
- Depreciation (rapid for some assets)
- Condition risk (maintenance, damage)
- Market risk (luxury market volatility)

---

### 9.4 Art & Collectibles

**LTV:** 30-50%  
**Funding Speed:** Slow (verification-heavy, 2-4 weeks)

**Tokenization Approach:**
- Fractional art tokens
- Custody-backed IOUs

**Required Documentation:**
- Appraisal (certified art appraiser)
- Provenance (chain of ownership, authenticity)
- Insurance (fine art policy)
- Custody arrangement (secure storage)

**Risk Considerations:**
- Valuation subjectivity
- Illiquid market
- Authentication risk (forgeries)

---

### 9.5 Intellectual Property (Patents, Trademarks, Copyrights)

**LTV:** 20-40%  
**Funding Speed:** Slow (complex, 4-8 weeks)

**Tokenization Approach:**
- Royalty-backed tokens
- License revenue-sharing agreements

**Required Documentation:**
- IP registration (patent, trademark, copyright)
- Valuation report (IP valuation specialist)
- License agreements (if generating revenue)
- Legal opinion (enforceability, validity)

**Risk Considerations:**
- Valuation difficulty
- Enforcement risk (infringement, litigation costs)
- Obsolescence (technology changes)

---

## How to Use This Matrix

### Step 1: Asset Classification

Determine which category the client's asset falls into.

### Step 2: LTV Determination

Apply the **typical LTV range** based on:
- Asset quality (location, condition, production history)
- Borrower creditworthiness
- Market conditions
- Your risk appetite

### Step 3: Documentation Checklist

Collect all **required documents** for that asset class.

### Step 4: Risk Assessment

Evaluate the **risk considerations** specific to that asset.

### Step 5: Tokenization Design

Choose the appropriate **tokenization approach**:
- Debt token (fixed coupon, senior claim)
- Equity token (profit-sharing, subordinated)
- Revenue token (tied to asset income)
- Stablecoin backing (if highly liquid collateral)

### Step 6: Deal Structuring

Design the loan/note structure:
- Term (short/medium/long)
- Payment schedule (monthly, quarterly, bullet)
- Covenants (financial ratios, reporting requirements)
- Security (first lien, second lien, unsecured)

### Step 7: Legal Documentation

Prepare:
- Subscription agreement
- Promissory note or loan agreement
- Security agreement
- UCC-1 filing (if personal property)
- Deed of trust or mortgage (if real estate)

### Step 8: Custody & VaultProof

- Engage custodian (if applicable)
- Create VaultProof record (hash all docs)
- Link to XRPL position

### Step 9: Funding & Servicing

- Investor subscribes
- Funds wired to SPV/custodian
- Issue XRPL token/position
- Service loan (collect payments, monitor collateral, report)

---

## LTV Quick Reference Table

| Asset Class | LTV Range | Speed | Liquidity |
|-------------|-----------|-------|-----------|
| **T-Bills / Gov't Securities** | 80-95% | Instant | Very High |
| **Gold (Vaulted)** | 60-75% | Fast | High |
| **Stablecoins (USDC)** | 90-100% | Instant | Very High |
| **Bitcoin** | 50-70% | Instant | High |
| **Ethereum** | 40-60% | Instant | High |
| **Invoice Receivables** | 60-90% | Rapid | Medium |
| **Commercial Real Estate** | 50-70% | Moderate | Medium |
| **Gold (Unmined)** | 40-50% | Fast | Low |
| **Solar/Energy PPAs** | 40-65% | Moderate | Medium |
| **Water Rights** | 30-65% | Moderate | Low |
| **Agricultural Land** | 35-60% | Moderate | Low |
| **Hospitality Development** | 20-60% | Fast | Low |
| **Lithium/Rare Earth** | 25-50% | Moderate | Low |
| **Oil & Gas Wells** | 25-60% | Moderate | Medium |
| **Raw Land** | 20-40% | Moderate | Low |
| **Carbon Credits** | 40-70% | Fast | Medium |
| **Private Equity** | 10-35% | Moderate | Very Low |
| **Exotic Cars** | 30-60% | Fast | Medium |
| **Yachts** | 25-50% | Fast | Low |
| **Aircraft** | 30-55% | Fast | Medium |
| **Art & Collectibles** | 30-50% | Slow | Low |
| **IP/Royalties** | 20-40% | Slow | Very Low |
| **Sports Contracts** | 10-40% | Fast | Low |

---

## Risk Management Guidelines

### Conservative Portfolio (Low Risk, Lower Yield)

**Target LTV:** 50-60%  
**Asset Mix:**
- 50% T-bills / government securities
- 30% Vaulted gold / precious metals
- 20% Investment-grade commercial real estate

**Expected Yield:** 8-10%  
**Default Risk:** <1%

---

### Balanced Portfolio (Moderate Risk, Moderate Yield)

**Target LTV:** 60-70%  
**Asset Mix:**
- 30% Government securities / stablecoins
- 30% Gold / precious metals
- 25% Commercial real estate
- 15% Invoice receivables / trade finance

**Expected Yield:** 10-12%  
**Default Risk:** 1-3%

---

### Aggressive Portfolio (Higher Risk, Higher Yield)

**Target LTV:** 70-80%  
**Asset Mix:**
- 20% Government securities (liquidity buffer)
- 25% Mining projects (lithium, gold)
- 25% Real estate development (Hilton, multifamily)
- 15% Energy projects (solar, oil & gas)
- 15% Opportunistic (water, IP, sports contracts)

**Expected Yield:** 12-16%  
**Default Risk:** 3-7%

---

## Underwriting Checklist

For every deal, verify:

- [ ] **Asset exists and is legally owned by borrower**
- [ ] **Title is clear** (or liens are disclosed and acceptable)
- [ ] **Third-party valuation** (appraisal, assay, financial analysis)
- [ ] **LTV is within policy limits** for asset class
- [ ] **Borrower creditworthiness** (background check, financials, references)
- [ ] **Security perfected** (UCC-1 filed, deed recorded, control agreement)
- [ ] **Insurance in place** (property, liability, key person if applicable)
- [ ] **Exit strategy clear** (how will loan be repaid? asset sale, refinance, cashflow?)
- [ ] **Legal review complete** (counsel opines on enforceability)
- [ ] **Compliance clear** (no OFAC, PEP, sanctions issues)
- [ ] **VaultProof created** (all docs hashed and linked to XRPL)
- [ ] **Custodian engaged** (if required for asset type)

---

## End of Asset Classification & LTV Matrix

**This document is confidential and intended for internal use by Unykorn credit and operations teams.**

For questions or updates, contact:  
**Unykorn Capital Management, LLC — Credit Policy Committee**

**Last updated:** November 2025  
**Version:** 1.0
