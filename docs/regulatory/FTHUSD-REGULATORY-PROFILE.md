# FTHUSD – Regulatory Profile & Issuance Framework

**Version:** 1.0  
**Last Updated:** 2025-01-17  
**Issuer / Platform:** Unykorn Global Finance – FTH Platform  
**Primary Contact:** [CONTACT NAME, regulatory@fth.global]

---

## 1. Asset Overview

### 1.1 Asset Identity

- **Token Name:** FTH USD
- **Ticker / Code:** FTHUSD
- **Network:** XRP Ledger (XRPL)
- **Issuer XRPL Account:** `[ISSUER_ACCOUNT – TBD]`
- **Treasury / Ops Account(s):**
  - Primary Treasury: `[TREASURY_ACCOUNT – TBD]`
  - Reserve Vault (if distinct): `[RESERVE_VAULT_ACCOUNT – TBD]`

### 1.2 Asset Type & Economic Nature

- **Category:**
  - [x] Fiat-backed Stablecoin (e.g., USD, EUR)
  - [ ] Commodity-backed (e.g., gold, water rights)
  - [ ] Credit / Claim on Receivables
  - [ ] Revenue Share / Profit-Linked Instrument
  - [ ] Membership / Utility Token
  - [ ] Other: `N/A`

- **What FTHUSD Legally Represents:**

> In plain language:  
> "FTHUSD represents a 1:1 claim on USD held in custodial accounts. Each FTHUSD token is backed by $1.00 USD (or equivalent) in cash, cash equivalents, or high-quality stablecoins (RLUSD, USDC) held in segregated accounts."

- **Regulatory characterization (initial view):**
  - [x] E-money / Electronic Money Instrument
  - [ ] Security / Financial Instrument
  - [x] Payment / Settlement Token
  - [ ] Utility Token
  - [ ] Hybrid / To be determined by counsel

**Note:** This section must be confirmed by legal counsel in each jurisdiction before public offering. Initial characterization is "e-money / payment token" but may require registration as MSB, EMI, or VASP depending on jurisdiction.

---

## 2. Jurisdictional Scope & Regulatory Mapping

### 2.1 Primary Jurisdictions

- **Issuer Domicile:** [TBD – likely US (Delaware / Wyoming) or offshore (Cayman / BVI)]
- **Main Operating Jurisdictions:**
  - United States – issuance, treasury, institutional clients
  - United Kingdom – potential future expansion (EMI license path)
  - Singapore – VASP licensing path for APAC clients
  - EU (selected jurisdictions) – MiCA compliance path

### 2.2 Licensing / Registration Requirements (High-Level)

For each key jurisdiction, summarize the expected regime:

#### United States

- **Regime Type:**
  - [x] Money Services Business (MSB)
  - [ ] Electronic Money Institution (EMI / e-money license)
  - [ ] Virtual Asset Service Provider (VASP)
  - [ ] Securities / Investment Firm
  - [ ] Other: State-by-state money transmission licenses (likely required)

- **Likely Applicable Laws / Rules (non-exhaustive):**
  - Bank Secrecy Act (BSA) / FinCEN MSB registration
  - State money transmission laws (varies by state)
  - OFAC sanctions compliance
  - Proposed federal stablecoin legislation (monitoring)

- **Current Status for FTHUSD:**
  - [x] Not offered to residents / entities in this jurisdiction
  - [ ] Offered on a reverse-enquiry / OTC-only basis
  - [ ] Offered under exemption: `N/A`
  - [ ] Fully licensed / registered: `N/A`
  - Notes: `Currently in pre-launch / whitelist-only pilot phase. No public offering. FinCEN MSB registration planned before U.S. client onboarding. State MTL analysis in progress.`

#### United Kingdom

- **Regime Type:**
  - [ ] Money Services Business (MSB)
  - [x] Electronic Money Institution (EMI / e-money license)
  - [ ] Virtual Asset Service Provider (VASP)
  - [ ] Securities / Investment Firm
  - [ ] Other: N/A

- **Likely Applicable Laws / Rules (non-exhaustive):**
  - Electronic Money Regulations 2011 (EMRs)
  - Payment Services Regulations 2017 (PSRs)
  - FCA authorization requirements for e-money issuers

- **Current Status for FTHUSD:**
  - [x] Not offered to residents / entities in this jurisdiction
  - [ ] Offered on a reverse-enquiry / OTC-only basis
  - [ ] Offered under exemption: `N/A`
  - [ ] Fully licensed / registered: `N/A`
  - Notes: `Future expansion path. EMI license application anticipated 2026+.`

#### Singapore

- **Regime Type:**
  - [ ] Money Services Business (MSB)
  - [ ] Electronic Money Institution (EMI / e-money license)
  - [x] Virtual Asset Service Provider (VASP)
  - [ ] Securities / Investment Firm
  - [ ] Other: N/A

- **Likely Applicable Laws / Rules (non-exhaustive):**
  - Payment Services Act 2019 (PS Act)
  - MAS licensing for Digital Payment Token (DPT) services
  - AML/CFT requirements under MAS Notice PSN02

- **Current Status for FTHUSD:**
  - [x] Not offered to residents / entities in this jurisdiction
  - [ ] Offered on a reverse-enquiry / OTC-only basis
  - [ ] Offered under exemption: `N/A`
  - [ ] Fully licensed / registered: `N/A`
  - Notes: `Future expansion. MAS licensing path under evaluation.`

---

## 3. Issuance, Redemption & Backing

### 3.1 Backing & Reserve Structure

- **Backing Model:**
  - [x] 1:1 fully backed by cash / cash equivalents
  - [ ] Over-collateralized (e.g., 120%)
  - [ ] Basket of assets (specify weights)
  - [ ] Other: N/A

- **Reserve Components for FTHUSD:**
  - Cash in bank accounts: `YES, target 60-80%`
  - Third-party stablecoins (e.g., RLUSD, USDC): `YES, up to 40%`
  - Custodied commodities / RWAs: `NO`
  - Internal credits / structured notes: `NO`

- **Reserve Accounts & Custodians:**
  - Bank / Custodian 1: `[BANK_NAME – TBD], US` – Role: `Primary USD settlement & reserves (FDIC-insured or swept to money market)`
  - Bank / Custodian 2: `[BANK_NAME – TBD], US/EU` – Role: `Secondary reserves, diversification`
  - Digital Custody Provider(s): `[CUSTODY_PROVIDER – TBD for RLUSD/USDC holdings if used]`

- **Reserve Policies:**
  - Target collateralization ratio: `100% minimum, with buffer reserves for operational liquidity`
  - Rebalancing frequency: `Daily reconciliation; rebalancing as needed to maintain 100%+ backing`
  - Acceptable reserve asset types: `USD cash (bank deposits, FDIC-insured accounts), U.S. Treasury bills (short-dated), RLUSD, USDC (from approved issuers), money market funds (AAA-rated)`

### 3.2 Issuance Rules

- **Who can receive newly issued FTHUSD?**
  - [x] Only whitelisted institutional counterparties
  - [x] Internal affiliates / SPVs only
  - [ ] Retail users (subject to KYC)
  - Notes: `Phase 1: Whitelist-only (internal SPVs, vetted institutional partners). Phase 2+: Expand to accredited investors and institutional clients post-licensing.`

- **Minting Triggers:**
  - Receipt of fiat funds: `Bank wires (USD) to designated reserve accounts`
  - Receipt of on-chain stablecoins (e.g., RLUSD, USDC): `YES – 1:1 swap allowed for whitelisted counterparties`
  - Internal treasury operations: `Treasury rebalancing between FTH entities (logged and reconciled)`

- **Approval Workflow:**
  - Min # of signers required for mint: `2-of-3 multi-sig (HSM-backed)`
  - Systems involved (manual vs automated): `Hybrid: automated mint request via internal API, manual approval by treasury + compliance officers, HSM signature for on-chain mint`

### 3.3 Redemption Rules

- **Redemption Rights:**
  - Who can redeem: `WHITELIST ONLY (Phase 1); institutional counterparties + accredited investors (Phase 2+)`
  - Minimum / maximum redemption amounts: `Min: $1,000 USD equivalent; Max: per agreement (daily limits may apply for large redemptions)`
  - Fees: `Standard: 0–0.1%; wire fees may apply; no fee for internal SPV transfers`
  - Settlement channels: `Bank wires (USD), RLUSD (1:1 swap), USDC (subject to availability)`

- **Redemption Process (Step-by-Step):**
  1. Holder submits redemption request via `FTH portal or email (redemptions@fth.global)`.
  2. KYC/AML and sanctions checks conducted or refreshed (if >90 days since last check).
  3. Tokens sent to designated redemption address `[REDEMPTION_ACCOUNT – TBD]`.
  4. Tokens burned on XRPL (multi-sig approval required).
  5. Fiat / assets sent to holder's verified bank account or XRPL wallet (RLUSD/USDC).
  6. Logs and ledger entries archived (transaction ID, amounts, timestamps, approvers).

---

## 4. KYC / AML / Sanctions & User Controls

### 4.1 User Categories

- **User Types:**
  - [x] Internal entities (SPVs, vaults, DAOs)
  - [x] Institutional clients (funds, banks, brokers)
  - [ ] High-net-worth individuals (Phase 2+)
  - [ ] Retail / general public (not planned for Phase 1)

### 4.2 Onboarding Checks

For each user type, define:

- Required KYC documents (ID, corporate docs, beneficial owners)
- AML risk assessment (PEP/sanctions checks, source of funds)
- Ongoing monitoring (screening frequency, thresholds)

| User Type           | KYC Level     | AML Checks                                    | Ongoing Review  |
|---------------------|---------------|-----------------------------------------------|-----------------|
| Internal SPV        | Simplified    | Screening of controllers, UBOs                | Annual          |
| Institutional Bank  | Full CDD      | Sanctions, adverse media, UBOs, licenses     | Quarterly       |
| Institutional Fund  | Full CDD      | Fund docs, AML policy, sanctions, UBOs       | Semi-annual     |
| HNW Individual      | Full CDD      | ID, source of wealth, PEP/sanctions, SOF     | Annual (Phase 2+)|

### 4.3 Sanctions & Restricted Jurisdictions

- **Prohibited jurisdictions:** `OFAC-sanctioned countries (Iran, North Korea, Syria, Cuba, Crimea region, etc.); jurisdictions with high AML/CFT risk per FATF`
- **Restricted (extra controls):** `China, Russia (case-by-case with enhanced due diligence); high-risk jurisdictions per internal risk model`
- **Sanctions lists monitored:**
  - [x] UN
  - [x] OFAC
  - [x] EU
  - [x] UK HMT
  - [x] Others: `FATF, national lists (Canada, Australia, etc.)`

- **Controls:**
  - Onboarding rejections criteria: `Matches on sanctions lists, prohibited jurisdictions, adverse media (terrorism, money laundering), insufficient documentation`
  - Freezing or blocking of addresses: `Immediate freeze upon sanctions match; XRPL account blacklist or trustline freeze (if supported by token design)`
  - Reporting to relevant FIUs (Financial Intelligence Units): `Suspicious Activity Reports (SARs) filed per FinCEN (U.S.) or equivalent; 24-48 hour turnaround`

---

## 5. Risk Management & Controls

### 5.1 Key Risks Identified

- **Operational Risk:** Key compromise, node failures, system outages, human error in minting/redemption
- **Liquidity Risk:** Inability to meet redemptions in stressed markets (bank runs, reserve asset illiquidity)
- **Market Risk:** Reserve asset price moves (mitigated by holding cash + T-bills, minimal exposure to volatile assets)
- **Legal / Regulatory Risk:** Misclassification as security, unlicensed MSB activity, jurisdiction-specific enforcement
- **Reputational Risk:** De-peg event, dispute over redemption, fraud allegation, loss of bank partner

### 5.2 Mitigation Measures

- **Multi-sig / HSM-backed control** of issuer and treasury keys (2-of-3 or 3-of-5 schemes)
- **Segregation of duties** between issuance (treasury), compliance (KYC/AML), and operations (node management)
- **Regular reconciliation** of circulating supply vs reserves (daily automated + weekly manual audit)
- **Stress tests** on redemption scenarios (10%, 25%, 50% redemption within 24 hours)
- **Business continuity and disaster recovery plans** (backup nodes, failover banking relationships, incident playbooks)
- **Reserve diversification** (multiple banks, mix of cash + T-bills + RLUSD/USDC)
- **Legal counsel** on retainer for regulatory guidance across jurisdictions

### 5.3 Incident Response

- **Trigger Events:**
  - Suspected key compromise (unauthorized transactions, wallet intrusion)
  - Large unexpected outflows (>$X in Y minutes without pre-announced redemption)
  - Regulatory inquiry / enforcement action (subpoena, cease-and-desist, inquiry letter)
  - Material de-peg of FTHUSD (>2% deviation from $1.00 for >24 hours)

- **Response Steps:**
  1. **Immediate freeze / pause** (if supported by token design and legal basis; multi-sig approval required)
  2. **Convene risk & compliance committee** (within 2 hours of detection)
  3. **Notify regulators / key partners** where required (FinCEN SAR, bank partners, major clients)
  4. **Publish communication** to affected counterparties (via portal, email, status page)
  5. **Root cause analysis and corrective actions** (within 48 hours: preliminary report; within 7 days: full RCA + remediation plan)

---

## 6. XRPL Integration & Technical Controls

### 6.1 XRPL Accounts & Roles

- **Issuer Account:** `[ISSUER_ACCOUNT – TBD, e.g. rFTHUSD...]`
  - Explorer link: `https://livenet.xrpl.org/accounts/[ISSUER_ACCOUNT]`
  - Role: Issues FTHUSD tokens; holds no balance (all issued tokens distributed to treasury/clients)

- **Treasury / Ops:** `[TREASURY_ACCOUNT – TBD]`
  - Explorer link: `https://livenet.xrpl.org/accounts/[TREASURY_ACCOUNT]`
  - Role: Operational wallet for minting, distribution, fee management

- **Reserve Vault:** `[RESERVE_VAULT_ACCOUNT – TBD]`
  - Explorer link: `https://livenet.xrpl.org/accounts/[RESERVE_VAULT_ACCOUNT]`
  - Role: Holds on-chain reserve assets (RLUSD, USDC) backing FTHUSD; includes memo fields with reserve report hashes

- **Redemption Sink:** `[REDEMPTION_ACCOUNT – TBD]`
  - Explorer link: `https://livenet.xrpl.org/accounts/[REDEMPTION_ACCOUNT]`
  - Role: Receives FTHUSD for burning; tokens immediately burned upon receipt

### 6.2 Node Infrastructure

- Number of nodes under our control: `3 (initially)`
- Roles: `2x Full history / stock servers (public-facing APIs); 1x internal-only (compliance / treasury queries)`
- Hosting: `Hybrid: 2x cloud (AWS / GCP, different regions), 1x bare metal (co-location facility for redundancy)`
- Security hardening: `SSH key-only access, firewall rules (whitelist IPs), fail2ban, automated patching, 24/7 monitoring (Prometheus + Grafana), daily backups, HSM integration for key signing`

### 6.3 Token Configuration

- **Transfer flags, freeze settings, clawback (if any):**
  - `DefaultRipple` enabled (allows FTHUSD to ripple through trust lines)
  - `RequireAuth` flag: TBD (may enable for whitelist enforcement)
  - `Global Freeze` available for emergency use (requires multi-sig + legal approval)
  - `Individual Freeze` available for sanctions compliance
  - `Clawback`: under evaluation (may enable in future for regulatory compliance)

- **Trustline requirements and recommended limit settings:**
  - Users must set trustline to issuer account `[ISSUER_ACCOUNT]`
  - Recommended limit: `Unlimited` (for institutional users) or `[specific USD amount]` based on relationship

- **Integration guidelines for third parties (wallets, custodians, banks):**
  - API docs: `[LINK – TBD, will include REST + WebSocket endpoints for balance queries, transaction submission]`
  - Custody integration: Support for Ledger, Fireblocks, BitGo, Copper (XRPL integrations)
  - Bank integration: ISO 20022 messaging for fiat on/off-ramp (via SWIFT / wire instructions linked to XRPL addresses)

---

## 7. Transparency, Reporting & Audit

### 7.1 Public Disclosures

- **What we publish, and how often:**
  - Reserve snapshots: `Monthly (Phase 1); weekly (Phase 2+ / at scale)`
  - Circulating supply of FTHUSD: `Real-time via XRPL explorer; dashboard at fth.global/reserves`
  - Attestations from custodians / trustees (if any): `Quarterly letters from banks confirming reserve balances`
  - Methodology for reserve valuation: `Published in this document + updated on website; cash at face value, T-bills at market value (daily), RLUSD/USDC at 1:1 USD`

### 7.2 On-Chain "Ledger Strength" Features

- **Reserve Vault transactions with memos including:**
  - Hashes of reserve reports (SHA-256 hash of monthly reserve PDF)
  - IPFS CIDs to documentation bundles (full reserve reports, audit letters, KYC policies)

- **Verification guide for auditors:**
  1. Locate Reserve Vault account on XRPL: `[RESERVE_VAULT_ACCOUNT]`
  2. Confirm balances and trustlines: Check RLUSD, USDC balances; compare to circulating FTHUSD
  3. Verify memo hashes / CIDs match supplied documents: Download PDF from IPFS, compute SHA-256, compare to on-chain memo field

### 7.3 Third-Party Audits

- **Audit firm:** `[NAME – TBD, targeting Big 4 or specialized crypto auditor (e.g., Armanino, Mazars)]`
- **Frequency:** `Semi-annual (Phase 1); quarterly (Phase 2+ / at scale)`
- **Scope:**
  - Reserves vs circulating supply (1:1 attestation)
  - Control environment (key management, multi-sig, access controls)
  - Compliance with stated policies (this document + internal AML/KYC procedures)
  - Technology review (node security, smart contract / token config audit)

---

## 8. Participation by Banks & External Partners

**This is where you future-proof for "as we grow and banks want in."**

### 8.1 Bank Roles

- Possible roles for banks and financial institutions:
  - **Reserve custodians** (hold USD reserves in segregated accounts)
  - **Distribution partners / primary dealers** (issue FTHUSD to their clients on demand, backed by reserves they hold)
  - **White-label issuers** (co-branded tokens, e.g., `FTHUSD.BANK_X`)
  - **Liquidity providers / market makers** (maintain FTHUSD <> XRP, FTHUSD <> RLUSD order books on XRPL DEX)

### 8.2 Onboarding a New Bank Partner

For each bank:

1. **Legal & compliance due diligence**
   - Review bank's AML/KYC policies, regulatory licenses, risk appetite
   - Confirm bank's XRPL technical readiness or willingness to integrate

2. **Bilateral or tripartite agreements** (issuer – bank – custodian)
   - Define roles: Who holds reserves? Who issues IOUs? Who owns customer relationship?
   - Liability allocation, indemnification, dispute resolution

3. **Definition of:**
   - **Who holds reserves**: Bank holds USD reserves in segregated account(s) in its own name
   - **Who issues IOUs**: Bank may issue FTHUSD from its own XRPL account (with FTH platform oversight) or FTH issues on bank's behalf
   - **Who owns customer relationship**: Bank owns client KYC/AML; FTH provides platform + compliance framework

4. **Technical integration:**
   - XRPL addresses: Bank sets up issuer/treasury accounts; FTH provides guidance
   - APIs / messaging: ISO 20022 for fiat settlement; REST/WebSocket for XRPL transaction submission
   - Node access: Bank may run own node or use FTH's infrastructure

5. **Disclosure update:**
   - Add bank to this document under Section 3.1 (Reserve Accounts & Custodians)
   - Add bank to Section 8 (Bank Participation) with role description
   - Update transparency / reporting commitments (include bank's reserves in monthly snapshots)

### 8.3 Co-Issuance / Multi-Issuer Scenarios

If FTHUSD ever becomes a **multi-issuer** product (e.g., `FTHUSD` issued by multiple banks):

- **Governance model:**
  - How new issuers join: Application + due diligence + vote by existing issuers (or FTH approval)
  - Voting: Weighted by reserves held or equal vote per issuer
  - Risk rules: All issuers must maintain 100%+ reserves, pass audits, comply with shared AML/KYC standards

- **Minimum standards for co-issuers:**
  - Licensing: Must hold MSB (U.S.), EMI (EU/UK), or equivalent in operating jurisdictions
  - Reserves: 1:1 backing minimum; daily reconciliation; quarterly audits
  - Tech stack: Must integrate with XRPL (own node or FTH-provided); multi-sig key management

- **Shared reporting framework and proof-of-reserves scheme:**
  - Aggregated reserve dashboard: Real-time view of all issuers' reserves + circulating supply
  - Cross-issuer audits: Independent auditor verifies reserves across all issuers quarterly
  - IPFS-backed transparency: Each issuer publishes reserve reports to IPFS; CIDs aggregated in shared registry

---

## 9. Legal Disclaimers & Change Management

### 9.1 Disclaimers

- This document is for informational purposes and does not constitute legal, tax, or investment advice.
- The regulatory characterization of FTHUSD may evolve as laws change or as we obtain further legal opinions.
- Availability of FTHUSD is subject to jurisdictional restrictions and internal risk policies.
- FTHUSD is not FDIC-insured and is not a deposit or obligation of any bank (unless explicitly stated by a bank partner).
- Redemption rights may be suspended in extraordinary circumstances (e.g., force majeure, court order, regulatory action).

### 9.2 Version Control & Amendments

- **Owner of this document:** `FTH Compliance & Legal Team`
- **Update Cycle:** `Quarterly review; updates upon material change (new bank partner, licensing milestone, policy change)`
- Changes must be:
  - Logged in Git (commit messages referencing "Regulatory Profile – FTHUSD Update")
  - Reviewed by legal / compliance
  - If material, communicated to key counterparties (banks, institutional clients) and, where required, regulators (via filing or notification)

---

## 10. Contact & Escalation Paths

- **Primary Regulatory / Compliance Contact:**
  - Name: `[NAME – TBD]`
  - Email: `regulatory@fth.global`
  - Phone: `[PHONE – TBD]`

- **Technical / Integration Contact:**
  - Name: `[NAME – TBD]`
  - Email: `integrations@fth.global`
  - Phone: `[PHONE – TBD]`

- **Reporting Issues or Concerns:**
  - Email: `compliance@fth.global` (for AML/KYC issues, suspicious activity)
  - Email: `security@fth.global` (for technical incidents, key compromise)
  - Portal: `https://fth.global/support` (general inquiries)
  - Expected response time: `Critical incidents: 2 hours; general inquiries: 24 hours (business days)`

---

## Document Status

- **Version:** 1.0
- **Status:** DRAFT – Pre-launch / whitelist pilot phase
- **Next Review:** Q2 2025 (prior to Phase 2 expansion)
- **Approvals Required:** Legal counsel sign-off, compliance officer approval, executive review

---

**End of FTHUSD Regulatory Profile**

This document is a living framework and will evolve as FTH scales, adds bank partners, and expands into new jurisdictions.

**Key Principle:** "One protocol, many assets, all with the same regulatory skeleton."

This makes real-world institutions relax instead of reaching for the fire extinguisher. 🧯 ✅
