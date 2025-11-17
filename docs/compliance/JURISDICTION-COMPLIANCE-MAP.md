# Global Jurisdiction Compliance Map

**Version:** 1.0  
**Last Updated:** 2025-01-17  
**Purpose:** High-level regulatory requirements and securities classification tests by jurisdiction for token issuance

---

## Overview

This document maps compliance requirements across key jurisdictions for **stablecoins**, **tokenized securities**, and **other digital assets**. Use it to:
- Determine licensing needs per jurisdiction
- Understand securities classification tests
- Identify AML/CTF baseline requirements
- Plan multi-jurisdiction expansion

**Not legal advice.** Always consult local counsel before operating in any jurisdiction.

---

## Global Baseline: FATF Recommendations

The **Financial Action Task Force (FATF)** sets the global AML/CTF standard. All member jurisdictions are expected to implement these recommendations:

### Key FATF Requirements for VASPs (Virtual Asset Service Providers)

| Requirement | Description | Reference |
|-------------|-------------|-----------|
| **VASP Definition** | Entities that exchange, transfer, safeguard, or administer virtual assets as a business | R.15 |
| **Licensing/Registration** | VASPs must be licensed or registered in each jurisdiction where they operate | R.15 |
| **AML/CTF Program** | VASPs must implement risk-based AML/CTF controls (CDD, EDD, transaction monitoring, SAR/STR) | R.10, R.20, R.21 |
| **Travel Rule** | VASPs must exchange originator/beneficiary information for transfers ≥$1,000 USD (or local equivalent) | R.16 |
| **Sanctions Screening** | Screen customers and transactions against UN, OFAC, EU, and local sanctions lists | R.6 |
| **Recordkeeping** | Retain transaction and customer records for at least 5 years | R.11 |
| **Supervision** | VASPs must be supervised by a competent authority (FIU, central bank, etc.) | R.27 |

**Action Item:** Every jurisdiction below implements FATF to varying degrees. Always assume FATF baseline applies.

---

## 1. United States

### Regulatory Regime

| Authority | Role | Key Laws |
|-----------|------|----------|
| **FinCEN** (Treasury) | AML/CTF supervision of MSBs (Money Services Businesses) | BSA (Bank Secrecy Act), PATRIOT Act |
| **SEC** | Securities regulation (if token is a security) | Securities Act 1933, Exchange Act 1934 |
| **CFTC** | Commodities regulation (if token is a commodity derivative) | Commodity Exchange Act |
| **OCC / Federal Reserve / FDIC** | Banking supervision (if issuer is a bank or trust company) | National Bank Act, various state banking codes |
| **State Regulators** | Money transmitter licenses (varies by state) | State MSB laws |

### Licensing Requirements

**For Stablecoins / Payment Tokens:**
- **Federal:** Register with FinCEN as MSB (Money Services Business)
- **State:** Obtain money transmitter licenses in **every state** where you have customers (or use agent banks)
- **Alternative:** Operate as licensed trust company (OCC, NY DFS, WY SPDI) or bank

**For Securities Tokens:**
- Register offering with SEC (Reg D, Reg A+, Reg S) or rely on exemption
- Register as broker-dealer or work with registered B-D
- Custodian must be qualified (registered B-D or trust company)

### Securities Classification Test: **Howey Test**

Token is a **security** if it meets all four prongs:
1. **Investment of money** → user pays money for token
2. **Common enterprise** → pooled funds or shared outcome
3. **Expectation of profit** → buyer expects token to appreciate or generate returns
4. **Efforts of others** → profits derive primarily from promoter/issuer efforts (not buyer's own work)

**Examples:**
- **FTHUSD stablecoin** (1:1 USD peg, no profit expectation) → **NOT a security**
- **Yield-bearing token** (earns interest) → **Likely a security** (profit from issuer's lending activities)
- **Governance token** (pure voting rights, no dividends) → **Gray area** (depends on facts)
- **Equity token** (share of company revenue) → **Definitely a security**

**Reves Test (for debt securities):** Also consider whether token is a "note" under Reves v. Ernst & Young (family resemblance test).

### AML/CTF Requirements

- **KYC:** CIP (Customer Identification Program) for all customers
- **Sanctions:** Screen against OFAC SDN, Consolidated, and Sectoral Sanctions lists
- **Travel Rule:** Threshold: **$3,000** for wire transfers; FinCEN proposes same for crypto
- **SAR Filing:** File Suspicious Activity Reports (SARs) within **30 days** of detection
- **Recordkeeping:** 5 years minimum

### Key Regulatory Guidance

- **FinCEN FIN-2013-G001:** Virtual currency exchangers/administrators are MSBs
- **FinCEN Notice (2019):** Clarifies VASP obligations
- **SEC Framework (2019):** Guidance on applying Howey test to digital assets
- **President's Working Group on Stablecoins (2021):** Calls for legislation treating stablecoin issuers like banks

---

## 2. European Union (EU)

### Regulatory Regime

| Authority | Role | Key Laws |
|-----------|------|----------|
| **EBA** (European Banking Authority) | AML/CTF guidance for crypto-asset service providers | AMLD5, AMLD6 |
| **ESMA** (European Securities Markets Authority) | Securities token regulation | MiFID II, Prospectus Regulation |
| **National Regulators** | Country-level licensing (e.g., BaFin in Germany, AMF in France) | National transposition of EU Directives |
| **MiCA Framework (2024)** | Crypto-asset regulation (stablecoins, asset-referenced tokens, e-money tokens) | Markets in Crypto-Assets Regulation |

### Licensing Requirements

**Under MiCA (effective 2024-2025):**
- **E-Money Tokens (EMTs):** Requires **e-money institution (EMI)** license
- **Asset-Referenced Tokens (ARTs):** Requires **ART issuer authorization** (stricter than EMI)
- **Crypto-Asset Service Providers (CASPs):** Licensing for exchanges, custodians, wallets

**For Securities Tokens:**
- Prospectus required for public offerings >€1M (Prospectus Regulation)
- Issuer or intermediary must have MiFID II license

### Securities Classification Test: **MiCA Categories**

| Token Type | Definition | Regulatory Treatment |
|------------|------------|----------------------|
| **E-Money Token (EMT)** | Pegged to single fiat currency (e.g., FTHUSD = 1 USD) | E-money institution license; reserve requirements; redemption at par |
| **Asset-Referenced Token (ART)** | Pegged to basket of assets (e.g., fiat + commodities) or algorithmic | ART issuer authorization; higher capital requirements; stress testing |
| **Utility Token** | Grants access to goods/services on platform | Lighter regulation unless it also qualifies as financial instrument |
| **Security Token** | Transferable securities under MiFID II (shares, bonds, derivatives) | Full MiFID II + Prospectus requirements |

**FTHUSD Classification:** **E-Money Token** (EMT) → requires EMI license

### AML/CTF Requirements

- **Directive:** AMLD5 (5th Anti-Money Laundering Directive) + AMLD6 (criminal liability)
- **KYC:** CDD for all customers; EDD for high-risk
- **Sanctions:** Screen against EU Consolidated List
- **Travel Rule:** Threshold: **€1,000** (per TFR – Transfer of Funds Regulation)
- **SAR Filing:** File STRs (Suspicious Transaction Reports) per national FIU rules
- **Recordkeeping:** 5 years minimum

### Key Regulatory Guidance

- **MiCA Regulation (2023):** Full crypto-asset framework effective 2024-2025
- **EBA Opinion on Crypto-Assets (2019):** Risk assessment methodology
- **ESMA Advice on ICOs (2019):** When tokens are securities under MiFID II

---

## 3. United Kingdom

### Regulatory Regime

| Authority | Role | Key Laws |
|-----------|------|----------|
| **FCA** (Financial Conduct Authority) | Crypto-asset regulation, AML/CTF supervision | MLR 2017 (Money Laundering Regulations), FSMA (Financial Services and Markets Act) |
| **HM Treasury** | Policy on stablecoins and e-money | Forthcoming stablecoin legislation |
| **Bank of England** | Systemic stablecoin oversight (proposed) | Future regulatory framework |

### Licensing Requirements

**Current (2025):**
- **Crypto-asset businesses:** Must register with FCA under MLR 2017 (AML/CTF registration)
- **E-Money Tokens:** Require **e-money institution (EMI)** license (existing UK regime)
- **Securities Tokens:** Prospectus + regulated activity authorization under FSMA

**Proposed (Future):**
- HM Treasury plans to bring **systemic stablecoins** under BoE/FCA supervision
- Likely to require authorization similar to payment institutions or banks

### Securities Classification Test: **UK Investment Tokens**

FCA uses **"specified investment"** test under FSMA:
- **Security Token:** Shares, debt securities, units in collective investment scheme → FCA authorization required
- **E-Money Token:** Regulated as e-money (not a security) if 1:1 fiat-backed
- **Unregulated Token:** Utility tokens with no investment characteristics → AML registration only

**FTHUSD Classification:** **E-Money** → requires EMI license

### AML/CTF Requirements

- **Law:** MLR 2017 (as amended)
- **KYC:** CDD for all customers; EDD for high-risk
- **Sanctions:** Screen against UK HM Treasury Consolidated List + OFAC
- **Travel Rule:** Threshold: **£1,000** (aligned with EU)
- **SAR Filing:** File SARs to National Crime Agency (NCA) ASAP (no hard deadline, but typically within days)
- **Recordkeeping:** 5 years minimum

### Key Regulatory Guidance

- **FCA PS19/22 (2020):** Crypto-asset AML/CTF guidance
- **HM Treasury Consultation (2023):** Future stablecoin regulation

---

## 4. Singapore

### Regulatory Regime

| Authority | Role | Key Laws |
|-----------|------|----------|
| **MAS** (Monetary Authority of Singapore) | Licensing and supervision of digital payment token services | PSA (Payment Services Act) |
| **MAS** | Securities regulation | SFA (Securities and Futures Act) |

### Licensing Requirements

**For Stablecoins / Payment Tokens:**
- Requires **Digital Payment Token (DPT) Service License** under PSA
- **Major Payment Institution (MPI)** license if transaction volume >S$3M/month

**For Securities Tokens:**
- Prospectus or exemption under SFA
- Capital Markets Services (CMS) license for dealing or custodian services

### Securities Classification Test: **SFA Capital Markets Products**

Token is a **capital markets product** (security) if it is:
- **Shares** or **debentures** (debt)
- **Units in a collective investment scheme (CIS)** → pooled investment with expectation of profit from promoter's efforts

**Digital Payment Token (DPT):** Any digital representation of value that:
- Is not issued by MAS or foreign central bank
- Is used as medium of exchange or payment
- **Excludes** securities and e-money

**FTHUSD Classification:** If 1:1 USD-backed and not marketed for investment → **DPT** (not a security) → PSA license required

### AML/CTF Requirements

- **Law:** PSA + MAS Notices (e.g., MAS Notice PSN02 on AML/CTF)
- **KYC:** CDD for all customers; EDD for high-risk
- **Sanctions:** Screen against UN, OFAC, and Singapore's national lists
- **Travel Rule:** Threshold: **S$1,500** (approx. USD $1,100)
- **STR Filing:** File Suspicious Transaction Reports (STRs) to STRO (Suspicious Transaction Reporting Office) immediately (no delay)
- **Recordkeeping:** 5 years minimum

### Key Regulatory Guidance

- **MAS Notice PSN02:** AML/CTF requirements for DPT service providers
- **MAS Digital Token Offering Guide (2020):** When DPTs are securities

---

## 5. United Arab Emirates (UAE)

### Regulatory Regime

| Authority | Role | Jurisdiction | Key Laws |
|-----------|------|--------------|----------|
| **VARA** (Virtual Assets Regulatory Authority) | Crypto-asset regulation | Dubai | VARA Law |
| **ADGM FSRA** | Financial services regulation (including crypto) | Abu Dhabi Global Market | FSMR (Financial Services and Markets Regulations) |
| **SCA** (Securities and Commodities Authority) | Federal securities regulator | Federal UAE | Federal Law No. 4 of 2000 |

### Licensing Requirements

**Dubai (VARA):**
- **Virtual Asset Service Providers (VASPs):** Must obtain VARA license for issuance, exchange, custody, etc.
- **Categories:** Broker-dealer, exchange, custodian, advisory, etc.

**Abu Dhabi (ADGM):**
- **Crypto-asset businesses:** Must obtain FSRA authorization
- **Fiat-Referenced Tokens:** May be treated as e-money or payment services

### Securities Classification Test

**VARA Framework:**
- **Virtual Asset:** Digital representation of value that can be traded/transferred digitally
- **Security Token:** Virtual asset that represents ownership or debt → additional securities rules apply

**Federal UAE (SCA):** Uses traditional securities tests (shares, bonds, derivatives)

**FTHUSD Classification:** Likely **virtual asset** (not security if no profit expectation) → VARA license required in Dubai

### AML/CTF Requirements

- **Law:** Federal Decree-Law No. 20 of 2018 (AML/CTF Law) + Cabinet Resolution No. 10 of 2019
- **KYC:** CDD for all customers; EDD for high-risk
- **Sanctions:** Screen against UN, OFAC, and UAE national lists
- **Travel Rule:** Threshold: **AED 3,500** (approx. USD $950)
- **SAR Filing:** File STRs to UAE FIU within **5 business days**
- **Recordkeeping:** 5 years minimum

### Key Regulatory Guidance

- **VARA Rulebook (2023):** Comprehensive virtual asset regulation for Dubai
- **ADGM Guidance on Crypto-Assets (2022):** FSRA requirements

---

## 6. Hong Kong

### Regulatory Regime

| Authority | Role | Key Laws |
|-----------|------|----------|
| **SFC** (Securities and Futures Commission) | Licensing for virtual asset trading platforms | SFO (Securities and Futures Ordinance), AMLO (Anti-Money Laundering Ordinance) |
| **HKMA** (Hong Kong Monetary Authority) | Regulation of stablecoins (proposed) | Future stablecoin regime |

### Licensing Requirements

**For Virtual Asset Trading Platforms (VATPs):**
- Requires **Type 1 (dealing in securities)** and **Type 7 (automated trading services)** licenses if trading security tokens
- New **VATP licensing regime** (effective 2023) covers all centralized exchanges

**For Stablecoins (Proposed):**
- HKMA plans to regulate **fiat-referenced stablecoins** similar to stored-value facilities (SVF) or deposit-taking institutions

### Securities Classification Test

**SFC Test:**
- **Security:** Shares, debentures, collective investment schemes under SFO
- **Virtual Asset:** Any digital representation of value (not legal tender) used as medium of exchange or investment

**If token offers profit or is sold as investment → likely a security**

**FTHUSD Classification:** If 1:1 USD and no profit expectation → **not a security**, but may fall under future stablecoin regime

### AML/CTF Requirements

- **Law:** AMLO + SFC Guidelines
- **KYC:** CDD for all customers; EDD for high-risk
- **Sanctions:** Screen against UN, OFAC, and Hong Kong lists
- **Travel Rule:** Threshold: **HK$8,000** (approx. USD $1,000)
- **STR Filing:** File STRs to JFIU (Joint Financial Intelligence Unit) immediately
- **Recordkeeping:** 5 years minimum

### Key Regulatory Guidance

- **SFC Position Paper on Virtual Asset Trading Platforms (2023):** Licensing regime details
- **HKMA Discussion Paper on Stablecoins (2024):** Proposed regulatory framework

---

## 7. Switzerland

### Regulatory Regime

| Authority | Role | Key Laws |
|-----------|------|----------|
| **FINMA** (Swiss Financial Market Supervisory Authority) | Licensing and supervision of financial services | FinSA (Financial Services Act), AMLA (Anti-Money Laundering Act) |
| **SRO** (Self-Regulatory Organizations) | Frontline AML/CTF supervision | AMLA |

### Licensing Requirements

**For Stablecoins / Payment Tokens:**
- **Payment Token:** No securities regulation, but AML/CTF compliance required
- **Large-scale issuance (>CHF 5M outstanding):** May require **banking license** or **securities dealer license**

**For Securities Tokens:**
- Prospectus or exemption under FinSA
- Securities dealer license if trading as intermediary

**For Custodians:**
- **Custodian license** under CISA (Collective Investment Schemes Act) if safeguarding client crypto

### Securities Classification Test: **FINMA Token Categories**

| Token Type | Definition | Regulatory Treatment |
|------------|------------|----------------------|
| **Payment Token** | Used as means of payment; no other function (e.g., Bitcoin, FTHUSD) | AML/CTF only (no securities regulation) |
| **Utility Token** | Grants access to digital service or application | No regulation if purely functional; AML if exchangeable |
| **Asset Token** | Represents ownership of assets, profit rights, or interest/dividend claims | Securities regulation (prospectus, licensing) |

**FTHUSD Classification:** **Payment Token** → AML/CTF compliance only (no securities prospectus needed)

### AML/CTF Requirements

- **Law:** AMLA + FINMA AML Ordinance
- **KYC:** CDD for all customers; EDD for high-risk
- **Sanctions:** Screen against SECO (Swiss State Secretariat for Economic Affairs) lists + UN + OFAC
- **Travel Rule:** Threshold: **CHF 1,000** (approx. USD $1,150)
- **SAR Filing:** File SARs to MROS (Money Laundering Reporting Office Switzerland) immediately
- **Recordkeeping:** 10 years (longer than most jurisdictions)
- **SRO Membership:** Crypto businesses must join an SRO (e.g., VQF, PolyReg) for AML/CTF audits

### Key Regulatory Guidance

- **FINMA ICO Guidelines (2018):** Token classification framework
- **FINMA Guidance on Stablecoins (2019):** Payment token treatment

---

## 8. Japan

### Regulatory Regime

| Authority | Role | Key Laws |
|-----------|------|----------|
| **FSA** (Financial Services Agency) | Licensing for crypto-asset exchanges and custodians | PSA (Payment Services Act), FIEA (Financial Instruments and Exchange Act) |
| **JFSA** | AML/CTF supervision | AML/CFT Act |

### Licensing Requirements

**For Crypto-Asset Service Providers:**
- **Crypto-Asset Exchange Service Provider (CAESP)** registration required for exchanges
- **Crypto-Asset Custody Service Provider (CACSP)** registration for custodians

**For Stablecoins:**
- **Electronic Payment Instruments (EPI):** Stablecoins pegged to fiat may be treated as EPI → requires trust company or bank license
- **Highly restrictive:** Japan has not fully opened stablecoin market to non-banks (as of 2025)

**For Securities Tokens:**
- Regulated under FIEA (securities dealer license, prospectus, etc.)

### Securities Classification Test

**FSA Test:**
- **Crypto-Asset:** Property value that can be transferred digitally (excludes fiat and securities)
- **Security:** Shares, bonds, derivatives under FIEA

**If token offers profit-sharing or resembles investment → security under FIEA**

**FTHUSD Classification:** Likely **Electronic Payment Instrument** → requires trust/bank license (difficult for non-banks)

### AML/CTF Requirements

- **Law:** AML/CFT Act (Act on Prevention of Transfer of Criminal Proceeds)
- **KYC:** CDD for all customers; EDD for high-risk
- **Sanctions:** Screen against METI (Ministry of Economy, Trade and Industry) lists + UN
- **Travel Rule:** Threshold: **¥100,000** (approx. USD $900)
- **SAR Filing:** File STRs to JAFIC (Japan Financial Intelligence Center) immediately
- **Recordkeeping:** 7 years

### Key Regulatory Guidance

- **FSA Revised PSA (2020):** Crypto-asset custody and custody regulations
- **FSA Stablecoin Guidance (2023):** EPI framework for fiat-backed stablecoins

---

## 9. Canada

### Regulatory Regime

| Authority | Role | Key Laws |
|-----------|------|----------|
| **FINTRAC** (Financial Transactions and Reports Analysis Centre) | AML/CTF supervision of MSBs | PCMLTFA (Proceeds of Crime (Money Laundering) and Terrorist Financing Act) |
| **CSA** (Canadian Securities Administrators) | Provincial securities regulation | Provincial Securities Acts |

### Licensing Requirements

**For Crypto-Asset Trading Platforms:**
- Register with FINTRAC as **Money Services Business (MSB)**
- Register with provincial securities regulator (e.g., OSC in Ontario) if trading securities or providing dealer/advisory services

**For Stablecoins:**
- If 1:1 fiat-backed and no profit expectation → **not a security** → FINTRAC registration only
- If yield-bearing or algorithmically-backed → may be a security → CSA registration required

### Securities Classification Test

**CSA Test:**
- **Investment Contract:** Howey-like test (investment of money, common enterprise, expectation of profit from efforts of others)
- **Security:** Includes shares, bonds, investment contracts

**FTHUSD Classification:** If 1:1 USD and no yield → **not a security** → FINTRAC MSB registration only

### AML/CTF Requirements

- **Law:** PCMLTFA
- **KYC:** CDD for all customers; EDD for high-risk
- **Sanctions:** Screen against OSFI (Office of the Superintendent of Financial Institutions) lists + UN + OFAC
- **Travel Rule:** Threshold: **CAD $1,000** (approx. USD $750)
- **STR Filing:** File STRs to FINTRAC within **30 days** of detection
- **Recordkeeping:** 5 years minimum

### Key Regulatory Guidance

- **FINTRAC Guidance on Virtual Currency (2020):** MSB obligations for crypto businesses
- **CSA Staff Notice 21-327 (2021):** Crypto-asset trading platform regulation

---

## 10. Australia

### Regulatory Regime

| Authority | Role | Key Laws |
|-----------|------|----------|
| **AUSTRAC** (Australian Transaction Reports and Analysis Centre) | AML/CTF supervision of digital currency exchanges | AML/CTF Act |
| **ASIC** (Australian Securities and Investments Commission) | Securities and financial services regulation | Corporations Act 2001 |

### Licensing Requirements

**For Digital Currency Exchanges (DCEs):**
- Register with AUSTRAC as **DCE** (digital currency exchange)
- If providing financial services (e.g., custody, dealing in securities) → ASIC **AFSL (Australian Financial Services License)** required

**For Stablecoins:**
- If 1:1 fiat-backed → **not a security** → AUSTRAC registration only
- If yield-bearing or investment product → may require AFSL

### Securities Classification Test

**ASIC Test:**
- **Managed Investment Scheme (MIS):** Pooled investment with profit from promoter's efforts → requires registration and prospectus
- **Financial Product:** Broad definition includes securities, derivatives, non-cash payment facilities

**FTHUSD Classification:** If 1:1 USD and no profit → **not a financial product** → AUSTRAC DCE registration only

### AML/CTF Requirements

- **Law:** AML/CTF Act 2006
- **KYC:** CDD for all customers; EDD for high-risk
- **Sanctions:** Screen against DFAT (Department of Foreign Affairs and Trade) lists + UN + OFAC
- **Travel Rule:** Threshold: **AUD $1,000** (approx. USD $750)
- **SMR Filing:** File Suspicious Matter Reports (SMRs) to AUSTRAC within **3 business days**
- **Recordkeeping:** 7 years

### Key Regulatory Guidance

- **AUSTRAC Guidance on Digital Currency (2020):** DCE registration and AML/CTF obligations
- **ASIC Information Sheet 225 (2022):** When crypto-assets are financial products

---

## Summary Table: Key Thresholds & Requirements

| Jurisdiction | Travel Rule Threshold | SAR/STR Filing Deadline | Recordkeeping | Stablecoin License |
|--------------|----------------------|-------------------------|---------------|--------------------|
| **US** | $3,000 (proposed) | 30 days | 5 years | MSB + State MTLs or Trust |
| **EU (MiCA)** | €1,000 | Per national FIU | 5 years | E-Money Institution (EMI) |
| **UK** | £1,000 | ASAP (days) | 5 years | EMI (proposed BoE/FCA) |
| **Singapore** | S$1,500 | Immediate | 5 years | DPT Service License (PSA) |
| **UAE (Dubai)** | AED 3,500 | 5 business days | 5 years | VARA License |
| **Hong Kong** | HK$8,000 | Immediate | 5 years | Proposed HKMA regime |
| **Switzerland** | CHF 1,000 | Immediate | 10 years | SRO membership (AML only) |
| **Japan** | ¥100,000 | Immediate | 7 years | Trust/Bank (EPI) |
| **Canada** | CAD $1,000 | 30 days | 5 years | FINTRAC MSB |
| **Australia** | AUD $1,000 | 3 business days | 7 years | AUSTRAC DCE |

---

## Securities Classification Decision Tree

Use this flowchart to determine if your token is a security:

```
START
  ↓
Does token grant profit rights, interest, dividends, or revenue share?
  ├─ YES → Likely a SECURITY → prospectus + licensing required
  └─ NO → Continue
       ↓
Is token 1:1 backed by fiat currency with redemption at par (no profit)?
  ├─ YES → Likely E-MONEY or PAYMENT TOKEN → e-money/payment license required (not securities regulation)
  └─ NO → Continue
       ↓
Does token value derive primarily from efforts of issuer/promoter (not buyer's own use)?
  ├─ YES → Likely a SECURITY (Howey/investment contract test)
  └─ NO → Continue
       ↓
Is token purely functional (access to service/product) with no investment marketing?
  ├─ YES → Likely UTILITY TOKEN → AML/CTF only (no securities regulation)
  └─ NO → GRAY AREA → consult local counsel
```

---

## Integration with Regulatory Profile Template

When filling out **[ASSET-REGULATORY-PROFILE.template.md](../regulatory/ASSET-REGULATORY-PROFILE.template.md)**, use this map to populate:

- **Section 1.3: Jurisdictions in Scope**
  - List target jurisdictions (e.g., US, UK, Singapore)
  - Reference sections above for licensing requirements

- **Section 1.4: Licensing & Regulatory Status**
  - Map to specific licenses needed per jurisdiction (e.g., "US: FinCEN MSB, NY NYDFS BitLicense; EU: EMI license")

- **Section 2.1: Asset Classification**
  - Use securities classification tests above to determine if asset is security, e-money, payment token, utility token
  - **Example:** "FTHUSD is classified as E-Money Token (EMT) under EU MiCA; Payment Token under Swiss FINMA; not a security in any jurisdiction"

- **Section 4: KYC/AML/Sanctions**
  - Apply FATF baseline + jurisdiction-specific thresholds (Travel Rule, SAR filing, recordkeeping)

- **Appendix A (Template):** Plug in jurisdiction-specific laws
  - **Example:** "US: BSA, FinCEN MSB rules, OFAC sanctions; EU: AMLD5, MiCA; UK: MLR 2017"

---

## Next Steps

1. **Identify Target Jurisdictions:**
   - [ ] List where you plan to operate or have customers
   - [ ] Prioritize by strategic importance (e.g., US, EU, Singapore)

2. **Run Securities Classification Tests:**
   - [ ] Apply Howey (US), MiCA (EU), FINMA (CH), etc.
   - [ ] Document classification in regulatory profile

3. **Map Licensing Path:**
   - [ ] Determine if you need MSB, EMI, DPT, VARA, etc.
   - [ ] Create licensing roadmap with timelines (Phase 1 = US MSB, Phase 2 = UK EMI, etc.)

4. **Implement Jurisdiction-Specific AML/CTF Controls:**
   - [ ] Configure KYC provider for geo-specific requirements (e.g., stricter CDD in EU vs. US)
   - [ ] Set Travel Rule thresholds per jurisdiction
   - [ ] Train compliance team on SAR/STR filing deadlines

5. **Monitor Regulatory Changes:**
   - [ ] Subscribe to FATF, MiCA, HKMA, FSA, etc. updates
   - [ ] Review this map quarterly for new developments

---

## Related Documentation

- **[ASSET-REGULATORY-PROFILE.template.md](../regulatory/ASSET-REGULATORY-PROFILE.template.md)** – Use this map to fill out jurisdiction sections
- **[KYC-AML-PROGRAM.template.md](KYC-AML-PROGRAM.template.md)** – Implement AML/CTF requirements per jurisdiction
- **[COMPLIANCE-VENDOR-GUIDE.md](COMPLIANCE-VENDOR-GUIDE.md)** – Select vendors with coverage in target jurisdictions

---

**Document Version:** 1.0  
**Last Updated:** 2025-01-17  
**Owner:** Legal + Compliance Teams  
**Review Cycle:** Quarterly (regulatory changes are frequent)
