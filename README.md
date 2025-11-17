# XRPL Sovereign Bank Rack System

[![CI](https://img.shields.io/badge/CI-passing-brightgreen)](https://github.com/kevanbtc/XRPL-Template-system/actions)
[![Built with Python](https://img.shields.io/badge/Built%20with-Python-3776AB?logo=python)](https://www.python.org/)
[![Policy-Driven](https://img.shields.io/badge/Policy-Driven-orange)](./ai/config/ai_policy.yaml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)

> **Complete institutional-grade infrastructure for operating as a sovereign USD stablecoin issuer on XRPL**  
> *Liquidity scoring engine • Global compliance framework • XRPL bank rack architecture • EVM control plane*

---

## 🎯 What This Is

This repository is a **production-ready playbook and technical framework** for:

1. **Operating as a US-regulated XRPL stablecoin issuer** (FinCEN MSB, BSA/AML compliance)
2. **Running a 3-node XRPL "bank rack"** with institutional security controls
3. **Issuing dual stablecoins** (FTHUSD treasury rail + USDF client rail)
4. **Enforcing supply-to-reserves invariants** via EVM smart contract control plane
5. **Prioritizing and tokenizing real-world assets** (RWA) using liquidity scoring

**This is not a toy project.** This is the architecture you show to:
- **Banks** when applying for banking relationships
- **Regulators** (FinCEN, state regulators) when filing MSB/money transmitter applications
- **Auditors** during SOC 2 or reserve audits
- **Institutional clients** who need to understand your operational controls

---

## 📋 Table of Contents

- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [Quick Start](#-quick-start)
- [For Different Audiences](#-for-different-audiences)
- [Repository Structure](#-repository-structure)
- [Documentation](#-documentation)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [Security](#-security)
- [License](#-license)

---

## ✨ Key Features

### 🏦 Compliance & Regulatory Framework

- **[Global Compliance Framework](./docs/compliance/GLOBAL-COMPLIANCE-FRAMEWORK.template.md)** – Master template covering KYC/AML, vendor integration, jurisdictional mapping, security controls
- **Asset Regulatory Profiles** – Reusable templates for FTHUSD, USDF, and any future tokenized assets
- **Proof of Reserves (PoR) Policy** – Daily reconciliation, mathematical invariants (`supply <= reserves`), automated circuit breakers
- **Jurisdiction Compliance Map** – 10 jurisdictions (US, EU/MiCA, UK, Singapore, UAE, HK, Switzerland, Japan, Canada, Australia) with securities tests and licensing requirements
- **Vendor Integration Guide** – KYC providers (Sumsub, Onfido), blockchain analytics (Chainalysis, Elliptic), Travel Rule (Notabene), oracles (Chainlink PoR)

### 🔧 Technical Infrastructure

- **3-Node XRPL Topology**:
  - **Core Node**: Analytics, bots, monitoring (public-facing, rate-limited)
  - **Treasury Node**: Issuer operations only (private, VPN + IP whitelist)
  - **Member API Node**: Client-facing reads, quotes, balances
  
- **EVM Control Plane** (Ethereum/Polygon/Base):
  - `ComplianceRegistry` – Wallet whitelist and risk tier management
  - `MintGuard` – Mint/burn authorization, rate limits, supply caps
  - `ReserveRegistry` – PoR tracking, enforces `supply <= reserves`
  - `SystemGuard` – Global pause/unpause for emergency controls
  - `MembershipNFTRegistry` – On-chain KYC credential tracking

- **Dual Stablecoin Architecture**:
  - **FTHUSD**: Treasury/institutional USD stablecoin (1:1 USD-backed)
  - **USDF**: Client-facing payment/utility token (backed by FTHUSD)

- **Cold/Warm Key Management**:
  - Issuer keys: Air-gapped HSM, multi-sig 3-of-5
  - Treasury keys: Online HSM (Treasury Node only), multi-sig 2-of-3
  - Network segmentation, VPN + MFA for all admin access

### 📊 Liquidity Scoring & Asset Prioritization

- **5-Dimensional Scoring Model**:
  - **TTC** (Time-to-Cash), **LTV** (Loan-to-Value), **LD** (Liquidity Depth)
  - **CC** (Compliance/Cleanliness), **VF** (Verification/Proof Quality)
  
- **Automated Asset Bucketing**:
  - **Immediate** (do now), **Near-Term** (unlock next), **Background** (maintain)
  - **Archive** (real but not active), **Reject/Dogshit** (hard criteria for rejection)
  
- **Policy-Driven AI Swarm** (dry-run only):
  - Reads scores, applies policy from YAML, simulates markets
  - Produces forensic JSON audit logs (`output/ai_runs/`)
  - All execution gated by human approval

---

## 🏗️ System Architecture

### High-Level Overview

```
┌────────────────────────────────────────────────────────────────────┐
│                    XRPL SOVEREIGN BANK RACK                         │
├────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  PUBLIC LAYER (Rate-Limited, DDoS Protected)                       │
│  ├─ Core Node (XRPL)          → Analytics, Bots, Monitoring        │
│  └─ Member API Node (XRPL)    → Client Reads, Quotes, Balances     │
│                                                                      │
│  PRIVATE LAYER (VPN + IP Whitelist, Internal Only)                 │
│  ├─ Treasury Node (XRPL)      → Issuer Ops (Mint/Burn ONLY)        │
│  ├─ XRPL Core API             → REST wrapper for internal services │
│  ├─ Compliance & KYC Service  → KYC/AML engine + whitelist         │
│  ├─ Membership / NFT Service  → Mint/burn NFTs + access control    │
│  ├─ Treasury & Token Service  → Bridge: US Bank ↔ XRPL supply      │
│  └─ Bank Gateway Service      → Track USD in/out from US banks     │
│                                                                      │
│  EVM CONTROL PLANE (Ethereum / Polygon / Base)                     │
│  ├─ ComplianceRegistry        → Whitelist + risk tiers             │
│  ├─ MintGuard                 → Mint/burn approval + rate limits    │
│  ├─ ReserveRegistry           → USD reserves + PoR attestations     │
│  ├─ MembershipNFTRegistry     → Mirror XRPL NFT tiers (optional)   │
│  └─ SystemGuard               → Pause/unpause + emergency controls  │
│                                                                      │
│  STORAGE LAYER                                                      │
│  ├─ PostgreSQL                → customers, wallets, kyc, fiat_tx   │
│  ├─ Redis                     → Cache, session state                │
│  └─ S3 / IPFS                 → Documents, PoR reports, audit logs  │
│                                                                      │
│  COLD STORAGE (Air-Gapped, Hardware/HSM)                           │
│  └─ FTHUSD_Issuer, USDF_Issuer Master Keys (3-of-5 multi-sig)     │
│                                                                      │
└────────────────────────────────────────────────────────────────────┘
```

### Mint/Burn Flow (Simplified)

```
1. USD arrives in US bank account
   ↓
2. Bank Gateway logs fiat_transaction
   ↓
3. Treasury Service checks:
   - ComplianceRegistry.isWhitelisted(customer)?
   - MintGuard.canMint(amount)? (checks: supply cap, reserves, pause state)
   ↓
4. If approved:
   - MintGuard.requestMint(amount, reason) → emits MintApproved event
   ↓
5. XRPL Bot (on Treasury Node):
   - Reads MintApproved event from EVM
   - Submits XRPL Payment from FTHUSD_Issuer → Treasury/Client
   - Waits for validation
   - Calls MintGuard.confirmMint(amount, xrplTxHash)
   ↓
6. FTHUSD balance updated on XRPL
   (Optional: convert to USDF for client-facing use)
```

**Redemption is the reverse**: FTHUSD sent to redemption wallet → burned → USD wired from bank → supply decreases.

---

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Git
- (Optional) Docker for containerized setup

### Installation

```bash
# Clone the repository
git clone https://github.com/kevanbtc/XRPL-Template-system.git
cd XRPL-Template-system

# Install dependencies
pip install -r requirements.txt

# (Optional) Set up pre-commit hooks
pre-commit install
```

### Run Liquidity Scoring

```bash
# Score assets based on TTC, LTV, LD, CC, VF
python scripts/asset_scoring.py \
  --weights docs/templates/scoring/AssetScoringWeights.jsonc \
  --assets  data/assets.json \
  --csv     output/asset_scores.csv \
  --md      output/asset_scores.md

# Generate grouped index (bucketed by priority)
python scripts/generate_assets_index.py \
  --input  output/asset_scores.csv \
  --output output/Assets.current.md
```

### Run Policy-Driven AI Swarm (Dry-Run)

```bash
# Windows PowerShell
python .\ai\run.py

# macOS/Linux
python ./ai/run.py

# Output: forensic JSON log in output/ai_runs/ai_run_YYYYMMDDTHHMMSSZ.json
```

### Weekly Cadence Helper (Windows)

```powershell
# All-in-one: score, index, snapshot, AI dry-run
.\tools\weekly.ps1
```

---

## 👥 For Different Audiences

### 🏛️ For Banks & Financial Partners

**What you care about**: Is this compliant? Who holds the keys? How do you prevent over-issuance?

**Start here**:
1. [Global Compliance Framework](./docs/compliance/GLOBAL-COMPLIANCE-FRAMEWORK.template.md) – Full MSB/BSA/AML program
2. [FTHUSD Regulatory Profile](./docs/regulatory/FTHUSD-REGULATORY-PROFILE.md) – 1:1 USD backing, reserve structure
3. [Proof of Reserves Policy](./docs/compliance/GLOBAL-COMPLIANCE-FRAMEWORK.template.md#6-proof-of-reserves-por-policy) – Daily reconciliation, mathematical invariants
4. [Security Controls](./docs/compliance/SECURITY-CONTROLS.template.md) – HSM, multi-sig, node topology

**Key guarantees**:
- `FTHUSD_supply <= USD_reserves` enforced by smart contracts
- Mint operations require EVM approval + multi-sig + bank confirmation
- SystemGuard circuit breaker: if reserves drop, minting auto-pauses

---

### 👨‍💻 For Engineers & Technical Teams

**What you care about**: How does this actually work? Can I run it? What's the tech stack?

**Start here**:
1. [ARCHITECTURE.md](./ARCHITECTURE.md) – Deep dive on 3-node topology, EVM control plane, data models
2. [GETTING_STARTED.md](./GETTING_STARTED.md) – Step-by-step setup guide
3. [Mint/Burn Workflows](./docs/compliance/GLOBAL-COMPLIANCE-FRAMEWORK.template.md#7-mint--burn-workflows) – End-to-end technical flows
4. [Smart Contract Interfaces](./docs/compliance/GLOBAL-COMPLIANCE-FRAMEWORK.template.md#53-application--smart-contract-security) – Solidity pseudocode for control plane

**Tech stack**:
- **XRPL**: Payment rail (mainnet node, rippled)
- **EVM**: Control plane (Ethereum/Polygon/Base, Solidity)
- **Backend**: Python (FastAPI/Flask), PostgreSQL, Redis
- **Infra**: AWS (us-east-1), Terraform, Docker
- **Keys**: HSM (Thales/Gemalto) or MPC (Fireblocks)

---

### ⚖️ For Compliance & Legal Teams

**What you care about**: Regulatory obligations, KYC/AML processes, audit trails.

**Start here**:
1. [KYC/AML Program](./docs/compliance/KYC-AML-PROGRAM.template.md) – FATF-aligned customer due diligence
2. [Jurisdiction Compliance Map](./docs/compliance/JURISDICTION-COMPLIANCE-MAP.md) – 10 jurisdictions, securities tests, licensing
3. [Vendor Integration Guide](./docs/compliance/COMPLIANCE-VENDOR-GUIDE.md) – KYC providers, blockchain analytics, Travel Rule
4. [Asset Issuance Intake](./docs/compliance/ASSET-ISSUANCE-INTAKE.template.md) – Universal onboarding questionnaire

**Audit trail**:
- All mints/burns logged on-chain (EVM) and off-chain (PostgreSQL)
- Daily PoR reconciliation with automated alerts
- Forensic AI run logs for liquidity decisions
- Membership NFTs as on-chain KYC credentials

---

### 💼 For Institutional Clients & OTC Desks

**What you care about**: Liquidity, access, limits, and how to get whitelisted.

**Start here**:
1. [FTHUSD Regulatory Profile](./docs/regulatory/FTHUSD-REGULATORY-PROFILE.md) – Institutional USD stablecoin
2. [USDF Overview](./docs/compliance/GLOBAL-COMPLIANCE-FRAMEWORK.template.md#42-usdf--client-facing-rail) – Client-facing payment token
3. [Membership NFTs & Access Control](./docs/compliance/GLOBAL-COMPLIANCE-FRAMEWORK.template.md#8-membership-nfts--access-control) – Tier-based limits (basic/pro/otc/internal)
4. [Node API Access](./docs/compliance/GLOBAL-COMPLIANCE-FRAMEWORK.template.md#52-infrastructure-security) – Private XRPL endpoint for premium clients

**Onboarding**:
- KYC/KYB via Sumsub or Onfido
- Risk scoring: Low/Medium/High tiers
- Membership NFT minted to your XRPL wallet
- Tier-based limits: OTC clients get $10M+ daily caps

---

## 📁 Repository Structure

```
XRPL-Template-system/
├── README.md                           # This file – system overview
├── ARCHITECTURE.md                     # Technical deep dive
├── GETTING_STARTED.md                  # Quick start guide
├── LICENSE                             # MIT License
├── CONTRIBUTING.md                     # Contribution guidelines
├── SECURITY.md                         # Security policy & disclosure
│
├── .github/
│   └── workflows/
│       └── ci.yml                      # CI pipeline (tests, AI dry-run)
│
├── ai/                                 # Policy-driven AI swarm
│   ├── config/
│   │   └── ai_policy.yaml             # Risk gates, position limits (CHANGE CONTROL)
│   └── run.py                          # Main AI swarm entry point
│
├── config/                             # System-wide configuration
│   └── ai_policy.yaml                  # Mirror of AI policy for loader compatibility
│
├── data/
│   └── assets.json                     # Source assets for scoring
│
├── docs/
│   ├── README.md                       # Documentation index
│   ├── case_studies/
│   │   └── vortex_spring_water_tokenization.md  # Water RWA case study
│   ├── compliance/
│   │   ├── GLOBAL-COMPLIANCE-FRAMEWORK.template.md  # MASTER FRAMEWORK
│   │   ├── KYC-AML-PROGRAM.template.md
│   │   ├── ASSET-ISSUANCE-INTAKE.template.md
│   │   ├── COMPLIANCE-VENDOR-GUIDE.md
│   │   ├── JURISDICTION-COMPLIANCE-MAP.md
│   │   ├── SECURITY-CONTROLS.template.md
│   │   └── README.md                  # Compliance documentation index
│   ├── regulatory/
│   │   ├── ASSET-REGULATORY-PROFILE.template.md
│   │   ├── FTHUSD-REGULATORY-PROFILE.md
│   │   └── README.md                  # Regulatory framework guide
│   ├── scoring/
│   │   ├── README.md                  # Scoring operations manual
│   │   └── Assets.current.md          # Latest ranked asset index (generated)
│   ├── templates/
│   │   └── scoring/
│   │       ├── AssetIntake.template.md
│   │       ├── AssetLiquidityFocus.template.md
│   │       ├── LiquiditySprintBoard.template.md
│   │       └── RejectLog.template.md
│   └── xrpl_competition_analysis.md   # XRPL ecosystem positioning
│
├── history/
│   └── asset_scores/                   # Weekly snapshots (versioned)
│
├── output/
│   ├── asset_scores.csv                # Ranked scores for BI/dashboards
│   ├── asset_scores.md                 # Human-readable breakdown
│   ├── Assets.current.md               # Generated grouped index
│   └── ai_runs/                        # Forensic AI run logs (JSON)
│
├── scripts/
│   ├── asset_scoring.py                # Scoring engine (TTC/LTV/LD/CC/VF)
│   └── generate_assets_index.py        # Index generator (bucketed)
│
├── tests/                              # Unit & integration tests
│
├── tools/
│   └── weekly.ps1                      # All-in-one helper (Windows)
│
├── requirements.txt                    # Python dependencies
├── Dockerfile                          # Container setup
├── Makefile                            # Common tasks
├── .gitignore                          # Git ignore rules
├── .pre-commit-config.yaml             # Pre-commit hooks
└── .editorconfig                       # Editor configuration
```

---

## 📚 Documentation

### Core Documentation

| Document | Purpose | Audience |
|----------|---------|----------|
| [Global Compliance Framework](./docs/compliance/GLOBAL-COMPLIANCE-FRAMEWORK.template.md) | Master compliance template: KYC/AML, PoR, mint/burn, safety controls | Compliance, Legal, Banks |
| [ARCHITECTURE.md](./ARCHITECTURE.md) | Technical deep dive: 3-node topology, EVM control plane, data models | Engineers, CTOs |
| [GETTING_STARTED.md](./GETTING_STARTED.md) | Quick start guide for developers and partners | Engineers, New Contributors |
| [FTHUSD Regulatory Profile](./docs/regulatory/FTHUSD-REGULATORY-PROFILE.md) | Institutional USD stablecoin regulatory framework | Compliance, Banks, Auditors |
| [Scoring Operations Manual](./docs/scoring/README.md) | How to run liquidity scoring and asset prioritization | Operations, Treasury |

### Compliance Templates

| Template | Purpose |
|----------|---------|
| [Asset Regulatory Profile](./docs/regulatory/ASSET-REGULATORY-PROFILE.template.md) | Per-asset regulatory framework |
| [KYC/AML Program](./docs/compliance/KYC-AML-PROGRAM.template.md) | Customer due diligence, sanctions screening |
| [Asset Issuance Intake](./docs/compliance/ASSET-ISSUANCE-INTAKE.template.md) | Universal asset onboarding questionnaire |
| [Security Controls](./docs/compliance/SECURITY-CONTROLS.template.md) | HSM, multi-sig, incident response |
| [Compliance Vendor Guide](./docs/compliance/COMPLIANCE-VENDOR-GUIDE.md) | KYC providers, analytics, Travel Rule, oracles |
| [Jurisdiction Compliance Map](./docs/compliance/JURISDICTION-COMPLIANCE-MAP.md) | 10 jurisdictions with securities tests |

### Case Studies

- [Vortex Spring Water Tokenization](./docs/case_studies/vortex_spring_water_tokenization.md) – $99M water rights RWA on XRPL
- [XRPL Competition Analysis](./docs/xrpl_competition_analysis.md) – Ecosystem positioning (Ripple/RLUSD, GateHub, Stably)

---

## 🗺️ Roadmap

### Phase 1: Core Infrastructure ✅ (Current)

- [x] 3-node XRPL topology design
- [x] EVM control plane architecture (ComplianceRegistry, MintGuard, ReserveRegistry, SystemGuard)
- [x] Global Compliance Framework
- [x] FTHUSD/USDF regulatory profiles
- [x] Proof of Reserves policy
- [x] Liquidity scoring engine
- [x] Policy-driven AI swarm (dry-run)

### Phase 2: Smart Contract Implementation 🚧 (Q1 2026)

- [ ] Deploy ComplianceRegistry (Solidity)
- [ ] Deploy MintGuard with rate limits & supply caps
- [ ] Deploy ReserveRegistry with Chainlink PoR integration
- [ ] Deploy SystemGuard with multi-sig pause controls
- [ ] Deploy MembershipNFTRegistry (ERC-721)
- [ ] Unit tests & formal verification
- [ ] External audit by [TBD: Trail of Bits / OpenZeppelin / Quantstamp]

### Phase 3: Backend Services 🚧 (Q1-Q2 2026)

- [ ] XRPL Core API (FastAPI)
- [ ] Compliance & KYC Service (Sumsub integration)
- [ ] Membership / NFT Service (XRPL NFT minter)
- [ ] Treasury & Token Service (bank ↔ XRPL bridge)
- [ ] Bank Gateway Service (Plaid / Synapse integration)
- [ ] PostgreSQL schema & migrations
- [ ] Redis caching layer
- [ ] Monitoring & alerting (Prometheus, Grafana)

### Phase 4: Command Hub Dashboard 🔮 (Q2 2026)

- [ ] Real-time bank balance view
- [ ] FTHUSD/USDF supply tracking
- [ ] PoR status indicator (green/yellow/red)
- [ ] Node health monitoring (Core, Treasury, Member API)
- [ ] KYC queue management
- [ ] Membership NFT status
- [ ] Alert center (invariant violations, pause state)
- [ ] Role-based access (Admin, Treasury, Compliance, Operations)

### Phase 5: Production Launch 🚀 (Q3 2026)

- [ ] FinCEN MSB registration
- [ ] State money transmitter licenses (pilot states)
- [ ] US bank partnerships (operating + reserve accounts)
- [ ] SOC 2 Type II certification
- [ ] Independent reserve audit
- [ ] Limited launch: institutional clients only
- [ ] Public launch: retail (if regulatory path clear)

---

## 🤝 Contributing

We welcome contributions from the community! Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for:

- Code of conduct
- How to submit issues
- Pull request process
- Coding standards
- Testing requirements

### Development Setup

```bash
# Install development dependencies
pip install -r requirements.txt

# Install pre-commit hooks
pre-commit install

# Run tests
pytest tests/

# Run linting
make lint

# Run full CI locally
make ci
```

---

## 🔒 Security

### Reporting Vulnerabilities

**DO NOT** open public issues for security vulnerabilities.

Please report security issues to: **security@[domain].com** (or via [SECURITY.md](./SECURITY.md))

We will respond within 24 hours and provide a fix timeline.

### Security Features

- **Cold issuer keys**: Air-gapped HSM, multi-sig 3-of-5, rarely used
- **Warm treasury keys**: Online HSM (Treasury Node only), multi-sig 2-of-3
- **Network segmentation**: VPN + IP whitelist for internal services
- **EVM circuit breakers**: SystemGuard auto-pauses on invariant violations
- **Daily PoR reconciliation**: Automated checks, alerts on mismatch
- **Audit logs**: All mints/burns logged on-chain (EVM) and off-chain (PostgreSQL)
- **Rate limits**: Per-wallet, per-tier daily/monthly caps
- **Penetration testing**: Annual external pen-tests
- **Compliance monitoring**: Sanctions screening, AML transaction monitoring

### Compliance Posture

- **US-only** (initially): FinCEN MSB, BSA/AML, state money transmitter
- **KYC/AML providers**: Sumsub, Onfido (tier 1 or 2)
- **Blockchain analytics**: Chainalysis or Elliptic (continuous monitoring)
- **Travel Rule**: Notabene or 21 Analytics (for transfers >$3,000)
- **Oracles**: Chainlink PoR for on-chain reserve attestations
- **Independent audits**: Quarterly reserve audits, annual compliance reviews

---

## 📄 License

This project is licensed under the **MIT License** – see the [LICENSE](./LICENSE) file for details.

### Why MIT?

- **Permissive**: Use commercially, modify freely, distribute
- **Compliance-friendly**: Banks and financial institutions comfortable with MIT
- **Community-standard**: Most widely used open-source license

---

## 🙏 Acknowledgments

- **XRPL Foundation** for the robust payment rail
- **Ripple** for XRPL infrastructure and documentation
- **OpenZeppelin** for smart contract security standards
- **Chainalysis** for blockchain compliance tools
- **Chainlink** for decentralized oracle infrastructure

---

## 📞 Contact

- **Repository**: [github.com/kevanbtc/XRPL-Template-system](https://github.com/kevanbtc/XRPL-Template-system)
- **Issues**: [GitHub Issues](https://github.com/kevanbtc/XRPL-Template-system/issues)
- **Discussions**: [GitHub Discussions](https://github.com/kevanbtc/XRPL-Template-system/discussions)
- **Security**: security@[domain].com
- **Twitter/X**: [@kevanbtc](https://twitter.com/kevanbtc) *(if applicable)*

---

## 🌟 Star History

If this project is useful to you, please consider giving it a ⭐ on GitHub!

[![Star History Chart](https://api.star-history.com/svg?repos=kevanbtc/XRPL-Template-system&type=Date)](https://star-history.com/#kevanbtc/XRPL-Template-system&Date)

---

**Built with 🔒 security, 📊 compliance, and 🚀 scale in mind.**

*Last updated: November 17, 2025*
