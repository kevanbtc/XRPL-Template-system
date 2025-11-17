# [ASSET_NAME] – Regulatory Profile & Issuance Framework

**Version:** 1.0  
**Last Updated:** [DATE]  
**Issuer / Platform:** Unykorn Global Finance – FTH Platform  
**Primary Contact:** [CONTACT NAME, EMAIL]

---

## 1. Asset Overview

### 1.1 Asset Identity

- **Token Name:** [ASSET_NAME]
- **Ticker / Code:** [ASSET_TICKER]
- **Network:** XRP Ledger (XRPL)
- **Issuer XRPL Account:** `[ISSUER_ACCOUNT]`
- **Treasury / Ops Account(s):**
  - Primary Treasury: `[TREASURY_ACCOUNT]`
  - Reserve Vault (if distinct): `[RESERVE_VAULT_ACCOUNT]`

### 1.2 Asset Type & Economic Nature

- **Category:**
  - [ ] Fiat-backed Stablecoin (e.g., USD, EUR)
  - [ ] Commodity-backed (e.g., gold, water rights)
  - [ ] Credit / Claim on Receivables
  - [ ] Revenue Share / Profit-Linked Instrument
  - [ ] Membership / Utility Token
  - [ ] Other: `[DESCRIPTION]`

- **What [ASSET_NAME] Legally Represents:**

> In plain language:  
> "[ASSET_NAME] represents a [DESCRIPTION: e.g. 1:1 claim on USD held in custodial accounts / 1 oz of allocated gold / share in revenue stream X]."

- **Regulatory characterization (initial view):**
  - [ ] E-money / Electronic Money Instrument
  - [ ] Security / Financial Instrument
  - [ ] Payment / Settlement Token
  - [ ] Utility Token
  - [ ] Hybrid / To be determined by counsel

*(This section must be confirmed by legal counsel in each jurisdiction before public offering.)*

---

## 2. Jurisdictional Scope & Regulatory Mapping

### 2.1 Primary Jurisdictions

- **Issuer Domicile:** [COUNTRY / STATE]
- **Main Operating Jurisdictions:**
  - [JURISDICTION_1] – [ROLE, e.g. issuance, treasury, clients]
  - [JURISDICTION_2] – [ROLE]
  - [JURISDICTION_3] – [ROLE]

### 2.2 Licensing / Registration Requirements (High-Level)

For each key jurisdiction, summarize the expected regime:

#### [JURISDICTION_1]

- **Regime Type:**
  - [ ] Money Services Business (MSB)
  - [ ] Electronic Money Institution (EMI / e-money license)
  - [ ] Virtual Asset Service Provider (VASP)
  - [ ] Securities / Investment Firm
  - [ ] Other: `[DESCRIPTION]`

- **Likely Applicable Laws / Rules (non-exhaustive):**
  - [LAW 1: e.g., "Money Transmission Act – [CITATION]"]
  - [LAW 2: e.g., "Virtual Asset / Stablecoin Regulation – [CITATION]"]

- **Current Status for [ASSET_NAME]:**
  - [ ] Not offered to residents / entities in this jurisdiction
  - [ ] Offered on a reverse-enquiry / OTC-only basis
  - [ ] Offered under exemption: `[EXEMPTION BASIS]`
  - [ ] Fully licensed / registered: `[LICENSE TYPE, REG NO.]`
  - Notes: `[DETAIL]`

*(Repeat this block per jurisdiction you care about.)*

---

## 3. Issuance, Redemption & Backing

### 3.1 Backing & Reserve Structure

- **Backing Model:**
  - [ ] 1:1 fully backed by cash / cash equivalents
  - [ ] Over-collateralized (e.g., 120%)
  - [ ] Basket of assets (specify weights)
  - [ ] Other: `[DESCRIPTION]`

- **Reserve Components for [ASSET_NAME]:**
  - Cash in bank accounts: `[YES/NO, % OF BACKING]`
  - Third-party stablecoins (e.g., RLUSD, USDC): `[YES/NO, %]`
  - Custodied commodities / RWAs: `[YES/NO, %]`
  - Internal credits / structured notes: `[YES/NO, %]`

- **Reserve Accounts & Custodians:**
  - Bank / Custodian 1: `[NAME, COUNTRY]` – Role: `[e.g. primary USD settlement & reserves]`
  - Bank / Custodian 2: `[NAME, COUNTRY]` – Role: `[e.g. gold custodian, segregated accounts]`
  - Digital Custody Provider(s): `[NAMES]`

- **Reserve Policies:**
  - Target collateralization ratio: `[E.G. 100%, 120%]`
  - Rebalancing frequency: `[E.G. daily / weekly / event-driven]`
  - Acceptable reserve asset types: `[LIST]`

### 3.2 Issuance Rules

- **Who can receive newly issued [ASSET_NAME]?**
  - [ ] Only whitelisted institutional counterparties
  - [ ] Internal affiliates / SPVs only
  - [ ] Retail users (subject to KYC)
  - Notes: `[CONSTRAINTS]`

- **Minting Triggers:**
  - Receipt of fiat funds: `[WIRES, ACH, etc.]`
  - Receipt of on-chain stablecoins (e.g., RLUSD, USDC): `[YES/NO, TERMS]`
  - Internal treasury operations: `[DESCRIPTION]`

- **Approval Workflow:**
  - Min # of signers required for mint: `[N]`
  - Systems involved (manual vs automated): `[E.G. dual-approval via HSM + back-office system]`

### 3.3 Redemption Rules

- **Redemption Rights:**
  - Who can redeem: `[WHITELIST ONLY / ALL HOLDERS / INSTITUTIONAL ONLY]`
  - Minimum / maximum redemption amounts: `[VALUES]`
  - Fees: `[SCHEDULE]`
  - Settlement channels: `[BANK WIRES, RLUSD, OTHER]`

- **Redemption Process (Step-by-Step):**
  1. Holder submits redemption request via `[PORTAL / EMAIL / API]`.
  2. KYC/AML and sanctions checks conducted or refreshed.
  3. Tokens sent to designated redemption address `[REDEMPTION_ACCOUNT]`.
  4. Tokens burned on XRPL.
  5. Fiat / assets sent to holder's verified bank / wallet.
  6. Logs and ledger entries archived.

---

## 4. KYC / AML / Sanctions & User Controls

### 4.1 User Categories

- **User Types:**
  - [ ] Internal entities (SPVs, vaults, DAOs)
  - [ ] Institutional clients (funds, banks, brokers)
  - [ ] High-net-worth individuals
  - [ ] Retail / general public (only if allowed)

### 4.2 Onboarding Checks

For each user type, define:

- Required KYC documents (ID, corporate docs, beneficial owners)
- AML risk assessment (PEP/sanctions checks, source of funds)
- Ongoing monitoring (screening frequency, thresholds)

Example table:

| User Type           | KYC Level     | AML Checks                         | Ongoing Review  |
|---------------------|---------------|------------------------------------|-----------------|
| Internal SPV        | Simplified    | Screening of controllers           | Annual          |
| Institutional Bank  | Full CDD      | Sanctions, adverse media, UBOs     | Quarterly       |
| HNW Individual      | Full CDD      | Source of wealth, PEP/ sanctions   | Annual          |

### 4.3 Sanctions & Restricted Jurisdictions

- **Prohibited jurisdictions:** `[LIST]`
- **Restricted (extra controls):** `[LIST]`
- **Sanctions lists monitored:**
  - [ ] UN
  - [ ] OFAC
  - [ ] EU
  - [ ] UK HMT
  - [ ] Others: `[LIST]`

- **Controls:**
  - Onboarding rejections criteria
  - Freezing or blocking of addresses
  - Reporting to relevant FIUs (Financial Intelligence Units)

---

## 5. Risk Management & Controls

### 5.1 Key Risks Identified

- **Operational Risk:** key compromise, node failures, system outages
- **Liquidity Risk:** inability to meet redemptions in stressed markets
- **Market Risk:** reserve asset price moves (if non-cash backing)
- **Legal / Regulatory Risk:** misclassification, unlicensed activity
- **Reputational Risk:** de-peg, dispute over redemption, fraud, etc.

### 5.2 Mitigation Measures

- Multi-sig / HSM-backed control of issuer and treasury keys
- Segregation of duties between issuance, treasury, compliance
- Regular reconciliation of circulating supply vs reserves
- Stress tests on redemption scenarios
- Business continuity and disaster recovery plans

### 5.3 Incident Response

- **Trigger Events:**
  - Suspected key compromise
  - Large unexpected outflows
  - Regulatory inquiry / enforcement action
  - Material de-peg of [ASSET_NAME]

- **Response Steps:**
  1. Immediate freeze / pause (if supported by token design and legal basis)
  2. Convene risk & compliance committee
  3. Notify regulators / key partners where required
  4. Publish communication to affected counterparties
  5. Root cause analysis and corrective actions

---

## 6. XRPL Integration & Technical Controls

### 6.1 XRPL Accounts & Roles

- **Issuer Account:** `[ISSUER_ACCOUNT]`
- **Treasury / Ops:** `[TREASURY_ACCOUNT]`
- **Reserve Vault:** `[RESERVE_VAULT_ACCOUNT]`
- **Redemption Sink:** `[REDEMPTION_ACCOUNT]`

Provide XRPL explorer links for each and a short description.

### 6.2 Node Infrastructure

- Number of nodes under our control: `[NODES]`
- Roles: `[VALIDATOR / FULL HISTORY / STOCK SERVER / INTERNAL ONLY]`
- Hosting: `[CLOUD / BARE METAL / HYBRID]`
- Security hardening: `[SSH, firewall, monitoring, backup strategy]`

### 6.3 Token Configuration

- Transfer flags, freeze settings, clawback (if any)
- Trustline requirements and recommended limit settings
- Integration guidelines for third parties (wallets, custodians, banks)

---

## 7. Transparency, Reporting & Audit

### 7.1 Public Disclosures

- **What we publish, and how often:**
  - Reserve snapshots (`[MONTHLY / QUARTERLY]`)
  - Circulating supply of [ASSET_NAME]
  - Attestations from custodians / trustees (if any)
  - Methodology for reserve valuation

### 7.2 On-Chain "Ledger Strength" Features

- Reserve Vault transactions with memos including:
  - Hashes of reserve reports
  - IPFS CIDs to documentation bundles

- Verification guide for auditors:
  1. Locate Reserve Vault account on XRPL
  2. Confirm balances and trustlines
  3. Verify memo hashes / CIDs match supplied documents

### 7.3 Third-Party Audits

- Audit firm: `[NAME / TBD]`
- Frequency: `[ANNUAL / SEMI-ANNUAL]`
- Scope:
  - Reserves vs circulating supply
  - Control environment (keys, processes)
  - Compliance with stated policies

---

## 8. Participation by Banks & External Partners

*(This is where you future-proof for "as we grow and banks want in.")*

### 8.1 Bank Roles

- Possible roles for banks and financial institutions:
  - Reserve custodians
  - Distribution partners / primary dealers
  - White-label issuers (co-branded tokens)
  - Liquidity providers / market makers

### 8.2 Onboarding a New Bank Partner

For each bank:

1. Legal & compliance due diligence
2. Bilateral or tripartite agreements (issuer – bank – custodian)
3. Definition of:
   - Who holds reserves
   - Who issues IOUs
   - Who owns customer relationship
4. Technical integration:
   - XRPL addresses
   - APIs / messaging (ISO 20022, SWIFT, etc.)
5. Disclosure update:
   - Add bank to this document under Reserve/Custodian / Partner sections
   - Update transparency / reporting commitments

### 8.3 Co-Issuance / Multi-Issuer Scenarios

If [ASSET_NAME] ever becomes a **multi-issuer** product:

- Specify governance model (how new issuers join, voting, risk rules)
- Minimum standards for co-issuers (licensing, reserves, tech stack)
- Shared reporting framework and proof-of-reserves scheme

---

## 9. Legal Disclaimers & Change Management

### 9.1 Disclaimers

- This document is for informational purposes and does not constitute legal, tax, or investment advice.
- The regulatory characterization of [ASSET_NAME] may evolve as laws change or as we obtain further legal opinions.
- Availability of [ASSET_NAME] is subject to jurisdictional restrictions and internal risk policies.

### 9.2 Version Control & Amendments

- **Owner of this document:** `[ROLE / TEAM]`
- **Update Cycle:** `[E.G. QUARTERLY OR UPON MATERIAL CHANGE]`
- Changes must be:
  - Logged in Git (commit messages referencing "Regulatory Profile – [ASSET_NAME] Update")
  - Reviewed by legal / compliance
  - If material, communicated to key counterparties and, where required, regulators.

---

## 10. Contact & Escalation Paths

- **Primary Regulatory / Compliance Contact:**
  - Name: `[NAME]`
  - Email: `[EMAIL]`
  - Phone: `[PHONE]`

- **Technical / Integration Contact:**
  - Name: `[NAME]`
  - Email: `[EMAIL]`

- **Reporting Issues or Concerns:**
  - [EMAIL / PORTAL]
  - Expected response time: `[X HOURS / DAYS]`

---

## Usage Instructions

This template should be copied and instantiated for each asset:

- **FTHUSD-REGULATORY-PROFILE.md**
- **USDF-REGULATORY-PROFILE.md**
- **FTH-GOLD-REGULATORY-PROFILE.md**
- **FTH-WATER-REGULATORY-PROFILE.md**
- etc.

Replace all `[BRACKETED_PLACEHOLDERS]` with actual values.

Check all `[ ]` checkboxes that apply to your specific asset.

As you grow and add bank partners, simply **append them** to Section 3.1 (Reserve Accounts & Custodians) and Section 8 (Bank Participation) — don't redesign the document.

This way your entire empire looks like: **"One protocol, many assets, all with the same regulatory skeleton."**

Exactly what makes real-world institutions relax instead of reaching for the fire extinguisher.
