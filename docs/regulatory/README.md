# Regulatory Documentation

**Reusable regulatory framework for all FTH/Unykorn tokenized assets**

---

## Overview

This directory contains **standardized regulatory profiles** for each tokenized asset issued on the FTH/Unykorn platform. The goal is simple:

> **"One protocol, many assets, all with the same regulatory skeleton."**

This makes banks, regulators, and partners comfortable because they see:
- **Consistent structure** across all assets
- **Clear responsibilities** (issuer, custodian, compliance)
- **Transparent backing** and redemption processes
- **Room to grow** (co-issuance, bank partnerships, multi-jurisdiction)

---

## Master Template

**[ASSET-REGULATORY-PROFILE.template.md](ASSET-REGULATORY-PROFILE.template.md)**

This is the **master template** you copy and fill in for each new asset.

### Template Structure

1. **Asset Overview** – What is this token? What does it represent?
2. **Jurisdictional Scope** – Where can it operate? What licenses are needed?
3. **Issuance, Redemption & Backing** – How are tokens minted/burned? What backs them?
4. **KYC/AML/Sanctions** – Who can hold this token? What checks are required?
5. **Risk Management & Controls** – What could go wrong? How do we prevent it?
6. **XRPL Integration** – Accounts, nodes, technical controls
7. **Transparency & Audit** – What do we publish? How do auditors verify?
8. **Bank Participation** – How do banks join as partners/custodians/co-issuers?
9. **Legal Disclaimers & Change Management** – Version control, update cycle
10. **Contact & Escalation** – Who to call when things go sideways

---

## Asset-Specific Profiles

### Live / In Development

| Asset | Profile Document | Status | Last Updated |
|-------|------------------|--------|--------------|
| **FTHUSD** | [FTHUSD-REGULATORY-PROFILE.md](FTHUSD-REGULATORY-PROFILE.md) | DRAFT (pre-launch) | 2025-01-17 |
| **USDF** | `USDF-REGULATORY-PROFILE.md` *(copy template)* | TBD | – |
| **FTH Gold** | `FTH-GOLD-REGULATORY-PROFILE.md` *(copy template)* | TBD | – |
| **FTH Water** | `FTH-WATER-REGULATORY-PROFILE.md` *(copy template)* | TBD | – |

### Planned / Future

- **FTH Sukuk** (Islamic finance instruments)
- **FTH Cheques** (tokenized receivables)
- **FTH Silver**
- **FTH [New Asset]** – Just copy the template and fill it in.

---

## How to Use

### For New Assets

1. **Copy the template:**
   ```powershell
   Copy-Item ASSET-REGULATORY-PROFILE.template.md NEW-ASSET-REGULATORY-PROFILE.md
   ```

2. **Replace all `[BRACKETED_PLACEHOLDERS]`** with real values:
   - `[ASSET_NAME]` → "FTH Gold"
   - `[ASSET_TICKER]` → "FTHGOLD"
   - `[ISSUER_ACCOUNT]` → `rXXXXXXXXXXXXXXXXXXXXXXXXXXXX`
   - etc.

3. **Check all `[ ]` checkboxes** that apply to your asset.

4. **Fill in jurisdiction-specific sections** (U.S., UK, Singapore, etc.) based on where you plan to operate.

5. **Add to the table above** and commit to the repo.

### For Bank/Partner Onboarding

When a bank or partner joins:

1. **Don't redesign the document.**
2. **Append them to:**
   - Section 3.1: Reserve Accounts & Custodians
   - Section 8: Participation by Banks & External Partners
3. **Update transparency commitments** (include their reserves in monthly snapshots).
4. **Version bump** and notify key counterparties.

### For Regulatory Inquiries

When regulators or partners ask "How do you handle [X]?":

1. **Point them to the relevant asset profile.**
2. **Section headers are your friend:**
   - "How do you ensure 1:1 backing?" → Section 3.1
   - "What's your KYC process?" → Section 4
   - "How do you handle sanctions?" → Section 4.3
   - "Who audits you?" → Section 7.3

3. **All profiles have the same structure**, so once they understand one asset, they understand your whole empire.

---

## Key Design Principles

### 1. Consistency Across Assets
Every asset has the same 10-section structure. Banks and regulators don't have to learn a new framework for each token.

### 2. Grow Into It
Start with "whitelist-only, small-scale" answers. As you get licenses and bank partners, **update the same document** instead of creating new ones.

### 3. On-Chain + Off-Chain Proof
- **Off-chain:** Bank statements, audit letters, legal docs
- **On-chain:** IPFS hashes in XRPL memo fields, Vault NFTs, reserve account balances

Auditors can verify everything by checking the blockchain + IPFS.

### 4. Future-Proof for Multi-Issuer
Section 8 explicitly covers "what if banks want to co-issue this token?" so you don't have to rewrite the whole framework when that happens.

---

## Compliance Workflow

### Phase 1: Whitelist-Only (Current)
- **Internal SPVs** and **vetted institutional partners** only
- **Reverse inquiry / OTC** basis
- **No public offering**
- **FinCEN MSB registration** (U.S.) in progress
- **State MTL analysis** underway

### Phase 2: Institutional Expansion
- **Accredited investors** and **institutional clients**
- **FinCEN MSB** registered
- **Selected state MTLs** obtained (or exemptions confirmed)
- **First bank partner** onboarded as reserve custodian

### Phase 3: Bank Co-Issuance
- **Multiple banks** issue the same token (e.g., `FTHUSD`)
- **Shared governance** (issuer consortium or FTH oversight)
- **Aggregated proof-of-reserves** dashboard
- **Cross-issuer audits** by Big 4 firm

### Phase 4: Retail / Global
- **EMI licenses** (UK, EU via MiCA)
- **VASP licenses** (Singapore, Hong Kong, etc.)
- **Public offering** (subject to regulatory approval)
- **Retail wallets** integrated (Ledger, MetaMask, etc.)

---

## Related Documentation

### In This Repo
- **[../case_studies/vortex_spring_water_tokenization.md](../case_studies/vortex_spring_water_tokenization.md)** – Example of tokenizing water rights (Vortex Spring)
- **[../xrpl_competition_analysis.md](../xrpl_competition_analysis.md)** – Who else is doing this on XRPL? What are your responsibilities as issuer/node operator?

### External (fth-xrpl-financial-os repo)
- **Security Plan:** `../fth-xrpl-financial-os/docs/security/README.md`
- **Technical Architecture:** `../fth-xrpl-financial-os/docs/architecture/`
- **Compliance Procedures:** `../fth-xrpl-financial-os/docs/compliance/`

---

## Contact

- **Regulatory / Compliance Questions:** regulatory@fth.global
- **Technical / Integration Questions:** integrations@fth.global
- **Security Incidents:** security@fth.global

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | 2025-01-17 | Initial framework: template + FTHUSD example | FTH Compliance Team |

---

**Remember:** This is a **living framework**. As you scale, add bank partners, and expand into new jurisdictions, you **update the same documents** instead of creating new ones.

That's what makes this "institutional-grade" instead of "startup chaos."

---

**End of Regulatory README**

Next: Fill out profiles for USDF, FTH Gold, FTH Water, etc. Same structure, different backing.
