# Compliance Documentation Framework

**Version:** 1.0  
**Last Updated:** 2025-01-17  
**Purpose:** Navigation and usage guide for FTH/Unykorn compliance templates and tools

---

## Overview

This directory contains **reusable compliance templates** for tokenizing any asset on XRPL. Whether you're issuing a stablecoin, tokenizing water rights, gold, sukuk, or securities, these templates provide the regulatory and compliance skeleton you need to:

- Pass bank due diligence
- File regulatory applications (MSB, EMI, DPT licenses, etc.)
- Demonstrate AML/CTF compliance to auditors
- Onboard new assets and partners systematically
- Integrate third-party compliance vendors

**Key Principle:** *One protocol, many assets, all with the same regulatory skeleton.*

---

## Template Inventory

| Template | Purpose | When to Use | Output |
|----------|---------|-------------|--------|
| **[ASSET-ISSUANCE-INTAKE.template.md](ASSET-ISSUANCE-INTAKE.template.md)** | Onboard new asset issuers, custodians, or partners | When evaluating new asset for tokenization or new partner for co-issuance | Completed intake form → due diligence package |
| **[KYC-AML-PROGRAM.template.md](KYC-AML-PROGRAM.template.md)** | Master KYC/AML/sanctions program aligned with FATF/BSA/AMLD | When writing AML policy for regulator submission or internal compliance manual | Compliance program document → regulator filing or audit evidence |
| **[COMPLIANCE-VENDOR-GUIDE.md](COMPLIANCE-VENDOR-GUIDE.md)** | Select and integrate KYC, analytics, Travel Rule, and oracle vendors | When building or expanding compliance tech stack | Vendor selection matrix → RFP criteria + integration plan |
| **[JURISDICTION-COMPLIANCE-MAP.md](JURISDICTION-COMPLIANCE-MAP.md)** | Understand licensing, AML, and securities rules by jurisdiction | When planning multi-jurisdiction expansion or filling out regulatory profiles | Jurisdiction compliance checklist → licensing roadmap |
| **[SECURITY-CONTROLS.template.md](SECURITY-CONTROLS.template.md)** | Define key management, node security, incident response, and technical controls | When writing security section for regulatory profile or SOC 2 audit | Security controls document → Section 7/8 of regulatory profile |

---

## How to Use These Templates

### Step 1: Start with Regulatory Profile

Before using these compliance templates, create your **asset-specific regulatory profile** using the master template in `../regulatory/`:

1. Copy **[ASSET-REGULATORY-PROFILE.template.md](../regulatory/ASSET-REGULATORY-PROFILE.template.md)**
2. Rename to `[ASSET_SYMBOL]-REGULATORY-PROFILE.md` (e.g., `FTHUSD-REGULATORY-PROFILE.md`, `WTR.VRTX-REGULATORY-PROFILE.md`)
3. Fill in bracketed placeholders `[LIKE_THIS]` with asset-specific details
4. See **[FTHUSD-REGULATORY-PROFILE.md](../regulatory/FTHUSD-REGULATORY-PROFILE.md)** for a worked example

The regulatory profile is your **master document** that references all these compliance templates.

---

### Step 2: Adapt Templates to Your Asset

Each template is designed to be **generic and reusable**. Adapt as follows:

#### For Asset Onboarding

**Template:** [ASSET-ISSUANCE-INTAKE.template.md](ASSET-ISSUANCE-INTAKE.template.md)

**Use Case:** Partner bank wants to co-issue FTHUSD, or you're tokenizing a new asset (gold, real estate, etc.)

**Workflow:**
1. Send intake form to prospective partner/issuer (Google Form, Notion, PDF, email)
2. Review responses for red flags:
   - Jurisdiction on sanctions list?
   - Backing model unclear or unbacked?
   - No KYC/AML program?
3. Escalate to Compliance Officer for due diligence
4. If approved → proceed to onboarding (create regulatory profile, integrate systems)

**Customization:**
- Section 3 (Regulatory Profile): Point to your jurisdiction compliance requirements (see [JURISDICTION-COMPLIANCE-MAP.md](JURISDICTION-COMPLIANCE-MAP.md))
- Section 8 (Risk Assessment): Adjust risk factors based on your risk appetite
- Section 10 (Bank Participation): Describe your co-issuance or custodian paths

---

#### For KYC/AML Policy

**Template:** [KYC-AML-PROGRAM.template.md](KYC-AML-PROGRAM.template.md)

**Use Case:** Filing for MSB license, EMI license, or preparing for SOC 2 audit

**Workflow:**
1. Copy template to new document: `[ENTITY_NAME]-KYC-AML-PROGRAM.md`
2. Replace bracketed placeholders:
   - `[ISSUER_NAME]` → your legal entity name
   - `[JURISDICTION]` → countries where you operate (reference [JURISDICTION-COMPLIANCE-MAP.md](JURISDICTION-COMPLIANCE-MAP.md))
   - `[X%]`, `[X years]`, `[X days]` → specific thresholds per jurisdiction
3. Integrate XRPL-specific controls (Section 12):
   - KYC gates on trustline establishment
   - Transaction monitoring for large transfers
   - Sanctions screening before minting/redemption
4. Plug in vendor details (Section 13):
   - KYC provider: [Sumsub/Onfido/etc.]
   - Blockchain analytics: [Chainalysis/TRM/etc.]
   - Travel Rule: [Notabene/21 Analytics/etc.]
5. Submit to regulator or auditor

**Customization:**
- **Appendix A:** List specific laws (US: BSA, FinCEN MSB rules; EU: AMLD5, MiCA; etc.)
- **Appendix B:** Prohibited countries (OFAC-sanctioned jurisdictions + high-risk per FATF)
- **Appendix C:** CDD/EDD checklists (add fields for crypto-specific risks)

---

#### For Vendor Selection

**Template:** [COMPLIANCE-VENDOR-GUIDE.md](COMPLIANCE-VENDOR-GUIDE.md)

**Use Case:** Choosing KYC provider, blockchain analytics, Travel Rule solution, or oracle (Chainlink PoR)

**Workflow:**
1. Identify compliance gap (e.g., "We need KYC for institutional customers" or "We need Travel Rule for VASP-to-VASP transfers")
2. Review vendor comparison tables in guide:
   - KYC: Sumsub vs. Onfido vs. Veriff vs. Trulioo
   - Analytics: Chainalysis vs. Elliptic vs. TRM Labs
   - Travel Rule: Notabene vs. 21 Analytics vs. Shyft Network
   - Oracles: Chainlink PoR vs. Pyth vs. RedStone
3. Evaluate vendors against selection criteria (Section 5):
   - Regulatory coverage (your target jurisdictions)
   - Blockchain support (native XRPL or custom integration needed?)
   - Cost structure (per-check vs. monthly minimum)
   - Integration effort (SDK quality, API docs, time to production)
4. Run pilot integration with top 2 vendors
5. Select winner and proceed with full integration

**Customization:**
- **Section 6:** Adjust recommended vendor stack by phase (Phase 1 = pilot with 1 vendor; Phase 4 = multi-vendor redundancy)
- **Section 7:** Tailor onboarding checklist to your procurement process (NDA, vendor security questionnaire, contract negotiation)

---

#### For Multi-Jurisdiction Expansion

**Template:** [JURISDICTION-COMPLIANCE-MAP.md](JURISDICTION-COMPLIANCE-MAP.md)

**Use Case:** Deciding where to launch FTHUSD (US vs. EU vs. Singapore), or expanding existing operations

**Workflow:**
1. Identify target jurisdictions (e.g., US, UK, Singapore, UAE)
2. For each jurisdiction, review:
   - Regulatory regime (which authority licenses crypto businesses?)
   - Licensing requirements (MSB, EMI, DPT, VARA, etc.)
   - Securities classification test (is FTHUSD a security here?)
   - AML/CTF requirements (Travel Rule threshold, SAR filing deadline, recordkeeping)
3. Create licensing roadmap:
   - **Phase 1:** US (FinCEN MSB registration, state-by-state MTLs via agent banks)
   - **Phase 2:** UK (FCA AML registration, EMI license application)
   - **Phase 3:** Singapore (MAS DPT license)
   - **Phase 4:** EU (EMI license under MiCA), UAE (VARA license)
4. Populate your regulatory profile (Section 1.3: Jurisdictions in Scope, Section 1.4: Licensing Status)

**Customization:**
- Add new jurisdictions as needed (follow same structure: Regulatory Regime → Licensing → Securities Test → AML/CTF → Key Guidance)
- Update Travel Rule thresholds and SAR deadlines as regulations change (quarterly review recommended)

---

#### For Security & Technical Controls

**Template:** [SECURITY-CONTROLS.template.md](SECURITY-CONTROLS.template.md)

**Use Case:** Writing Section 7 (XRPL Accounts & Node Infrastructure) of your regulatory profile, or preparing for SOC 2 / ISO 27001 audit

**Workflow:**
1. Copy template sections into your regulatory profile or standalone security policy document
2. Fill in:
   - **Section 1:** Key hierarchy (Master Key, Regular Key, Treasury, Redemption Sink)
   - **Section 1.2:** HSM vendor and configuration (Thales Luna, AWS CloudHSM, Fireblocks, etc.)
   - **Section 1.3:** Multi-sig thresholds and signer roles
   - **Section 2:** Node infrastructure (validator vs. API node, hosting, firewall rules)
   - **Section 5:** Incident response plan (freeze/blacklist decision tree)
3. Integrate XRPL-specific controls:
   - Set `NoRipple`, `RequireAuth`, `RequireDest` flags on issuer account
   - Monitor trustlines, memos, and large transfers
   - Document freeze policy (law enforcement only, not arbitrary)
4. Schedule penetration test and publish results

**Customization:**
- **Section 1.1:** Adjust key hierarchy based on your architecture (e.g., add "Oracle Signing Key" if using Chainlink)
- **Section 2.2:** Modify network segmentation diagram for your cloud provider (AWS, GCP, Azure)
- **Section 5.2:** Customize freeze/blacklist decision tree based on your legal counsel's guidance

---

## Compliance Workflow: New Asset Onboarding

Use this workflow to systematically onboard a new asset (stablecoin, gold, water, etc.):

```
Step 1: Asset Intake
  ↓
[ASSET-ISSUANCE-INTAKE.template.md]
  ↓ (Prospective issuer fills out form)
  ↓
Step 2: Due Diligence
  ↓
Compliance Officer reviews:
  - Legal structure (SPV? HoldCo/OpCo?)
  - Backing model (1:1 reserves? Collateralized? Algorithmic?)
  - Regulatory status (licensed? registered? exempt?)
  - Jurisdiction (sanctioned? high-risk?)
  ↓
Decision: APPROVE | REJECT | REQUEST MORE INFO
  ↓ (If APPROVED)
  ↓
Step 3: Create Regulatory Profile
  ↓
Copy [ASSET-REGULATORY-PROFILE.template.md]
  → Fill in asset details
  → Use [JURISDICTION-COMPLIANCE-MAP.md] for licensing requirements
  → Use [SECURITY-CONTROLS.template.md] for Section 7/8
  ↓
Step 4: Technical Integration
  ↓
- Create XRPL issuer account
- Set account flags (NoRipple, RequireAuth, etc.)
- Configure multi-sig (from SECURITY-CONTROLS template)
- Integrate KYC/AML vendors (from COMPLIANCE-VENDOR-GUIDE)
  ↓
Step 5: Compliance Testing
  ↓
- Test KYC flow (user onboarding → KYC approval → trustline enabled)
- Test sanctions screening (reject address on OFAC list)
- Test transaction monitoring (alert on large transfer)
- Test Travel Rule (VASP-to-VASP info exchange)
  ↓
Step 6: Regulatory Filing (if required)
  ↓
- Submit MSB/EMI/DPT license application
- Include: Regulatory Profile, KYC/AML Program, Security Controls
- Attach: Audited financials, background checks, insurance certificates
  ↓
Step 7: Go Live
  ↓
- Whitelist-only launch (Phase 1)
- Monitor for 30-90 days
- Expand to institutional (Phase 2) after stable operations
```

---

## Template Update & Version Control

**Who Updates Templates:**
- **Legal/Compliance:** Regulatory content (laws, jurisdictions, securities tests)
- **Security/Engineering:** Technical controls (HSMs, nodes, multi-sig)
- **Operations:** Vendor guides (new vendors, pricing updates)

**Review Cycle:**
- **Quarterly:** Review all templates for regulatory changes (new FATF guidance, MiCA implementation, etc.)
- **Ad Hoc:** Update templates when major event occurs (new vendor added, security incident, regulatory enforcement action)

**Version Control:**
- Use semantic versioning: `1.0` → `1.1` (minor update) → `2.0` (major overhaul)
- Document version changes in each template's header:
  ```markdown
  **Version:** 2.0  
  **Last Updated:** 2025-04-15  
  **Change Summary:** Added Japan FSA guidance, updated Chainlink PoR integration, refreshed vendor pricing
  ```

---

## Asset Tracking Table

Use this table to track which assets have completed compliance documentation:

| Asset Symbol | Asset Name | Regulatory Profile Status | KYC/AML Program Status | Security Controls Status | Go-Live Date |
|--------------|------------|---------------------------|------------------------|--------------------------|--------------|
| **FTHUSD** | FTH USD Stablecoin | DRAFT (v1.0) | DRAFT (adapted) | DRAFT (adapted) | TBD (Phase 1: Q1 2025) |
| **USDF** | Bank Consortium Stablecoin | TBD | TBD | TBD | TBD |
| **WTR.VRTX** | Vortex Spring Water Rights | TBD | TBD | TBD | TBD |
| **GOLD** | Tokenized Gold | TBD | TBD | TBD | TBD |
| **SUKUK001** | Islamic Bond Token | TBD | TBD | TBD | TBD |

**Instructions:**
- Copy this table into your internal compliance tracker (Notion, Confluence, Excel)
- Update "Status" column: DRAFT → REVIEW → APPROVED → LIVE
- Link to actual documents in your repository

---

## Integration with Case Studies & Regulatory Profiles

### How Compliance Templates Connect to Other Docs

```
docs/
├── case_studies/
│   └── vortex_spring_water_tokenization.md
│         ↑ (References compliance requirements)
│         |
├── regulatory/
│   ├── ASSET-REGULATORY-PROFILE.template.md  ← Master template
│   ├── FTHUSD-REGULATORY-PROFILE.md          ← Example instantiation
│   └── README.md                              ← Regulatory framework guide
│         ↑ (Links to compliance templates)
│         |
└── compliance/  ← YOU ARE HERE
    ├── ASSET-ISSUANCE-INTAKE.template.md
    ├── KYC-AML-PROGRAM.template.md
    ├── COMPLIANCE-VENDOR-GUIDE.md
    ├── JURISDICTION-COMPLIANCE-MAP.md
    ├── SECURITY-CONTROLS.template.md
    └── README.md (this file)
```

**Cross-References:**
- **Case Studies → Compliance Templates:** Case studies (like Vortex water) describe *what* you're tokenizing; compliance templates describe *how* you do it compliantly
- **Regulatory Profiles → Compliance Templates:** Regulatory profiles are *asset-specific outputs*; compliance templates are *reusable inputs*
- **Vendor Guide → KYC/AML Program:** Vendor guide tells you *who* to hire; KYC/AML program tells you *what* those vendors must do

---

## Best Practices

### 1. Don't Lock Yourself Into Brand-Specific Templates

These templates are deliberately **generic**:
- Use `[ISSUER_NAME]` instead of "FTH" or "Unykorn"
- Use `[ASSET_SYMBOL]` instead of "FTHUSD" or "WTR.VRTX"
- Why? So you can white-label for partners, co-issuers, or bank consortiums

**Example:** If Chase Bank wants to co-issue FTHUSD, you copy the regulatory profile and replace `[ISSUER_NAME]` with "JPMorgan Chase Bank, N.A."

---

### 2. Keep One Master Template, Many Instantiations

**Anti-Pattern:** Creating 10 different versions of the KYC/AML program with copy-paste variations

**Better Pattern:**
- **Master Template:** `KYC-AML-PROGRAM.template.md` (stays generic, versioned, reviewed quarterly)
- **Instantiations:** `FTHUSD-KYC-AML-PROGRAM.md`, `USDF-KYC-AML-PROGRAM.md` (specific to each asset/entity)

This way, when regulations change (e.g., FATF updates Travel Rule guidance), you:
1. Update master template
2. Review all instantiations
3. Update instantiations only if asset-specific changes needed

---

### 3. Align with "Grow Into It" Model

These templates are designed for **phased compliance growth**:

| Phase | Compliance Posture | Templates Needed |
|-------|-------------------|------------------|
| **Phase 1: Whitelist-Only** | Simplified KYC (known counterparties only), manual compliance checks | Intake form, basic KYC/AML program, minimal vendor stack |
| **Phase 2: Institutional** | Full CDD, EDD for HNW, blockchain analytics, quarterly audits | Full KYC/AML program, vendor guide (1-2 vendors), security controls |
| **Phase 3: Bank Co-Issuance** | Bank-grade compliance, co-issuer due diligence, shared governance | Multi-entity regulatory profile, jurisdiction map (multi-country), vendor redundancy |
| **Phase 4: Retail / Global** | Public offering, Travel Rule enforcement, real-time monitoring, SOC 2 Type II | All templates fully implemented, multi-vendor integration, continuous audit |

**Key Insight:** You don't need *all* templates *fully completed* in Phase 1. Start with intake + basic KYC/AML, then expand as you grow.

---

## External Resources

- **FATF Recommendations:** https://www.fatf-gafi.org/publications/fatfrecommendations/
- **EU MiCA Regulation:** https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R1114
- **FinCEN Virtual Currency Guidance:** https://www.fincen.gov/resources/statutes-and-regulations/guidance/application-fincens-regulations-certain-business-models
- **Chainalysis Compliance Resources:** https://www.chainalysis.com/compliance/
- **Chainlink Proof of Reserve:** https://chain.link/proof-of-reserve
- **XRPL Developer Docs (Account Flags, Multi-Sig):** https://xrpl.org/accounts.html

---

## FAQ

### Q1: Do I need all these templates for a simple stablecoin?

**A:** It depends on your scale and ambition:
- **Small pilot (friends & family):** Start with intake form + basic KYC/AML program + security controls (minimal)
- **Institutional launch:** Add vendor guide + jurisdiction map + full security controls
- **Bank partnership or public offering:** Implement all templates fully

### Q2: Can I use these templates for non-XRPL assets?

**A:** Yes, with modifications:
- Replace "XRPL" references with your blockchain (Ethereum, Polygon, Solana, etc.)
- Adjust "smart contract" sections (XRPL has no general-purpose smart contracts; other chains do)
- Update vendor XRPL integration patterns (e.g., Chainalysis has native Ethereum support but limited XRPL)

### Q3: What if my jurisdiction isn't in JURISDICTION-COMPLIANCE-MAP.md?

**A:** Add it using the same structure:
1. Regulatory Regime (authorities, key laws)
2. Licensing Requirements (for stablecoins, securities, exchanges)
3. Securities Classification Test (local equivalent of Howey, MiCA, etc.)
4. AML/CTF Requirements (Travel Rule threshold, SAR filing, recordkeeping)
5. Key Regulatory Guidance (links to official sources)

Then submit a pull request or update the template for your team.

### Q4: How do I handle conflicting regulations (e.g., US vs. EU)?

**A:** Adopt **highest common denominator** approach:
- If US requires 5-year recordkeeping and EU requires 7 years → keep 7 years globally
- If US Travel Rule is $3,000 and EU is €1,000 (~$1,100) → apply €1,000 threshold globally
- Document jurisdiction-specific carve-outs in Appendix A of KYC/AML program

### Q5: Who should review/approve these templates?

**A:** Recommended approvers:
- **Legal Counsel:** Regulatory profile, KYC/AML program, jurisdiction map
- **Compliance Officer:** All templates (primary owner)
- **CTO/CISO:** Security controls, vendor guide (technical sections)
- **CFO:** Vendor guide (cost estimates), asset intake (financial risk assessment)
- **Board (if applicable):** Final sign-off on master templates before regulatory filing

---

## Next Steps

1. **Copy Master Templates:**
   - [ ] Create `[YOUR_ASSET]-REGULATORY-PROFILE.md` from `../regulatory/ASSET-REGULATORY-PROFILE.template.md`
   - [ ] Create `[YOUR_ENTITY]-KYC-AML-PROGRAM.md` from `KYC-AML-PROGRAM.template.md`
   - [ ] Adapt `SECURITY-CONTROLS.template.md` for your XRPL architecture

2. **Fill In Asset-Specific Details:**
   - [ ] Replace all `[BRACKETED_PLACEHOLDERS]`
   - [ ] Add jurisdiction-specific thresholds from `JURISDICTION-COMPLIANCE-MAP.md`
   - [ ] Document your chosen vendors from `COMPLIANCE-VENDOR-GUIDE.md`

3. **Review & Approve:**
   - [ ] Legal counsel review
   - [ ] Compliance officer sign-off
   - [ ] Board approval (if required)

4. **Implement & Test:**
   - [ ] Integrate KYC/AML vendors
   - [ ] Configure XRPL issuer account (flags, multi-sig)
   - [ ] Test compliance flows (KYC → trustline → minting → redemption)

5. **File with Regulators (if required):**
   - [ ] Attach regulatory profile, KYC/AML program, security controls to MSB/EMI/DPT application
   - [ ] Include audited financials, insurance certificates, background checks

6. **Go Live:**
   - [ ] Launch Phase 1 (whitelist-only)
   - [ ] Monitor for 30-90 days
   - [ ] Expand to Phase 2 (institutional) after stable operations

---

**Document Version:** 1.0  
**Last Updated:** 2025-01-17  
**Owner:** Compliance + Legal + Engineering Teams  
**Review Cycle:** Quarterly (or when regulations change)

---

## Related Documentation

- **[../regulatory/README.md](../regulatory/README.md)** – Regulatory profile framework and usage guide
- **[../case_studies/vortex_spring_water_tokenization.md](../case_studies/vortex_spring_water_tokenization.md)** – Example of compliance applied to water rights tokenization
- **[../xrpl_competition_analysis.md](../xrpl_competition_analysis.md)** – XRPL ecosystem positioning and issuer responsibilities

---

**For questions or updates, contact:**
- **Compliance Officer:** [compliance@domain.com]
- **Legal Counsel:** [legal@domain.com]
- **Security Team:** [security@domain.com]
