# Getting Started

**Quick start guide for XRPL Sovereign Bank Rack System**

This guide will help you understand the system, set up your environment, and start using the compliance templates and liquidity scoring tools.

---

## Table of Contents

1. [Understanding the System (5-minute overview)](#1-understanding-the-system)
2. [Prerequisites](#2-prerequisites)
3. [Installation](#3-installation)
4. [Running Liquidity Scoring](#4-running-liquidity-scoring)
5. [Using Compliance Templates](#5-using-compliance-templates)
6. [Understanding XRPL Nodes (Conceptual)](#6-understanding-xrpl-nodes-conceptual)
7. [Next Steps](#7-next-steps)

---

## 1. Understanding the System

**What is this?**

A production-ready institutional playbook for operating a **US-regulated XRPL stablecoin issuer**. It includes:

- ✅ **Compliance framework** (880-line master template + 6 sub-templates)
- ✅ **Liquidity scoring engine** (Python-based asset prioritization)
- ✅ **3-node XRPL architecture** (Core, Treasury, Member API nodes)
- ✅ **EVM control plane** (Smart contracts for mint/burn authorization)
- ✅ **Policy-driven AI swarm** (Dry-run mode for analysis)

**Who is this for?**

- **Banks & financial partners** looking to issue stablecoins on XRPL
- **Compliance teams** building AML/KYC programs
- **Engineers** implementing XRPL payment infrastructure
- **Institutional clients** evaluating tokenization platforms

**Key Design Principle:**

```
XRPL = Payment Rail (fast, cheap money movement)
EVM = Control Plane (authorization logic, safety constraints)
PostgreSQL = Source of Truth (customer data, compliance records)
Smart Contracts = Enforcement (mathematical invariants: supply ≤ reserves)
```

---

## 2. Prerequisites

### Required Software

- **Python 3.9+** (for liquidity scoring and AI swarm)
- **Git** (for cloning the repository)
- **Text editor** (VS Code, Sublime, Vim, etc.)

### Optional (for full development)

- **Docker** (for containerized XRPL nodes)
- **PostgreSQL 14+** (for database operations)
- **Node.js 18+** (for some utilities)
- **Foundry** (for Solidity contract development)

### Required Knowledge

- Basic command line usage
- Understanding of stablecoins and tokenization
- Familiarity with XRPL concepts (trustlines, payments, NFTs)

---

## 3. Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/kevanbtc/XRPL-Template-system.git
cd XRPL-Template-system
```

### Step 2: Set Up Python Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1

# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Verify Installation

```bash
# Test Python imports
python -c "import pandas; import numpy; print('Python environment ready')"

# Check project structure
ls docs/compliance/  # Should show compliance templates
```

**Expected Output:**

```
Python environment ready

docs/compliance/:
- GLOBAL-COMPLIANCE-FRAMEWORK.template.md
- KYC-AML-PROGRAM.template.md
- ASSET-ISSUANCE-INTAKE.template.md
- COMPLIANCE-VENDOR-GUIDE.md
- JURISDICTION-COMPLIANCE-MAP.md
- SECURITY-CONTROLS.template.md
- README.md
```

---

## 4. Running Liquidity Scoring

The liquidity scoring engine helps prioritize which assets to onboard based on market data and risk metrics.

### Step 1: Prepare Sample Data

The system expects a CSV file with asset data. Example format:

```csv
asset_code,issuer,market_cap_usd,daily_volume_usd,trustlines,age_days,regulatory_clarity
FTHUSD,rFTH...,10000000,500000,1200,365,HIGH
USDF,rUSDF...,5000000,200000,800,180,MEDIUM
```

### Step 2: Run Scoring

```bash
python scripts/asset_scoring.py --input data/assets.csv --output results/scores.json
```

### Step 3: Review Results

```bash
cat results/scores.json
```

**Example Output:**

```json
{
  "ranked_assets": [
    {
      "asset_code": "FTHUSD",
      "score": 8.7,
      "rank": 1,
      "strengths": ["High market cap", "Strong regulatory clarity"],
      "risks": ["Limited trading history"]
    },
    {
      "asset_code": "USDF",
      "score": 7.2,
      "rank": 2,
      "strengths": ["Active community"],
      "risks": ["Lower daily volume", "Medium regulatory clarity"]
    }
  ]
}
```

### Step 4: Use Weekly Helper (Optional)

```powershell
# On Windows, run weekly analysis
.\tools\weekly.ps1
```

This runs scoring + generates a summary report.

---

## 5. Using Compliance Templates

### Step 1: Identify Your Use Case

| Use Case | Start Here |
|----------|------------|
| **New stablecoin launch** | [GLOBAL-COMPLIANCE-FRAMEWORK.template.md](docs/compliance/GLOBAL-COMPLIANCE-FRAMEWORK.template.md) |
| **Onboarding a new asset** | [ASSET-ISSUANCE-INTAKE.template.md](docs/compliance/ASSET-ISSUANCE-INTAKE.template.md) |
| **Building KYC/AML program** | [KYC-AML-PROGRAM.template.md](docs/compliance/KYC-AML-PROGRAM.template.md) |
| **Selecting compliance vendors** | [COMPLIANCE-VENDOR-GUIDE.md](docs/compliance/COMPLIANCE-VENDOR-GUIDE.md) |
| **Multi-jurisdiction expansion** | [JURISDICTION-COMPLIANCE-MAP.md](docs/compliance/JURISDICTION-COMPLIANCE-MAP.md) |
| **Security audit preparation** | [SECURITY-CONTROLS.template.md](docs/compliance/SECURITY-CONTROLS.template.md) |

### Step 2: Copy Template

```bash
# Example: Create compliance document for your project
cp docs/compliance/GLOBAL-COMPLIANCE-FRAMEWORK.template.md my-compliance-plan.md
```

### Step 3: Fill in Placeholders

Open `my-compliance-plan.md` and search for:

- `[YOUR_COMPANY]`
- `[YOUR_ASSET]`
- `[YOUR_ISSUER_ACCOUNT]`
- `TODO` or `PLACEHOLDER`

Replace with your actual values.

### Step 4: Review Checklist Sections

The template includes checklists like:

```markdown
## Day 0 Setup Checklist

- [ ] Deploy XRPL nodes (Core, Treasury, Member API)
- [ ] Configure HSM for issuer key storage
- [ ] Deploy EVM control plane contracts (ComplianceRegistry, MintGuard, ReserveRegistry, SystemGuard)
- [ ] Integrate KYC provider (Sumsub, Onfido, etc.)
- [ ] Connect to US bank accounts for reserves
- [ ] Run end-to-end mint/burn test (testnet)
```

Check off each item as you complete it.

### Step 5: Maintain Living Document

Compliance is not one-time. Update your document:

- **Daily**: After mint/burn operations (log in Section 6.3)
- **Weekly**: After reserve reconciliation (update Section 6.2)
- **Quarterly**: Review vendor performance, update risk scores
- **Annually**: Full compliance audit, update all policies

---

## 6. Understanding XRPL Nodes (Conceptual)

You don't need to run XRPL nodes to use the compliance templates, but if you're building the full system, here's what you need to know.

### 3-Node Architecture

```
┌──────────────┐       ┌──────────────┐       ┌──────────────┐
│  Core Node   │       │ Treasury Node│       │ Member API   │
│ (Analytics)  │       │ (Operations) │       │ (Clients)    │
│              │       │              │       │              │
│ Public       │       │ Private      │       │ Public       │
│ Rate-limited │       │ VPN + IP     │       │ Rate-limited │
│ No keys      │       │ whitelist    │       │ No keys      │
│              │       │ HSM keys     │       │              │
└──────────────┘       └──────────────┘       └──────────────┘
```

### What Each Node Does

**Core Node** (Public, for analytics):
- Heavy queries (transaction history, account data)
- Bot listeners (monitoring for events)
- No sensitive keys stored
- Can be DDoS'd without affecting issuer operations

**Treasury Node** (Private, for operations):
- **ONLY** for issuer operations (mint/burn)
- Warm keys stored in HSM (Hardware Security Module)
- Accessible only from backend services via VPN
- Multi-sig required (2-of-3 or 3-of-5)

**Member API Node** (Public, for clients):
- Client-facing WebSocket/RPC
- Wallet apps, member portals connect here
- Read-only operations (account_info, balances, quotes)
- Rate-limited per IP/wallet

### Running a Test Node (Testnet)

For testing purposes, you can run a single node in Docker:

```bash
# Pull XRPL Docker image
docker pull xrpllabsofficial/xrpld:latest

# Run testnet node
docker run -d \
  --name xrpl-testnet \
  -p 6006:6006 \
  -v $(pwd)/xrpl-data:/var/lib/rippled/db \
  xrpllabsofficial/xrpld:latest \
  --testnet

# Check node status
docker logs xrpl-testnet
```

**Production Warning**: Do NOT use Docker for mainnet production. Use dedicated servers with:
- Hardware security modules (HSM) for key storage
- Network segmentation (VPC, firewalls)
- DDoS protection (CloudFlare, AWS Shield)
- 24/7 monitoring and alerting

See [ARCHITECTURE.md](ARCHITECTURE.md) Section 3 for full node configuration details.

---

## 7. Next Steps

### For Compliance Teams

1. Read: [docs/compliance/GLOBAL-COMPLIANCE-FRAMEWORK.template.md](docs/compliance/GLOBAL-COMPLIANCE-FRAMEWORK.template.md) (880 lines, complete playbook)
2. Customize: Replace placeholders with your company details
3. Review: [docs/compliance/JURISDICTION-COMPLIANCE-MAP.md](docs/compliance/JURISDICTION-COMPLIANCE-MAP.md) for your target jurisdictions
4. Select vendors: Use [docs/compliance/COMPLIANCE-VENDOR-GUIDE.md](docs/compliance/COMPLIANCE-VENDOR-GUIDE.md)

### For Engineers

1. Read: [ARCHITECTURE.md](ARCHITECTURE.md) (1,062 lines, full technical design)
2. Study: Section 4 (EVM Control Plane) for smart contract specifications
3. Review: Section 6 (Data Models) for PostgreSQL schema
4. Build: Start with testnet XRPL node (see Section 6 above)

### For Financial Partners

1. Read: [docs/regulatory/FTHUSD-REGULATORY-PROFILE.md](docs/regulatory/FTHUSD-REGULATORY-PROFILE.md) (worked example for USD stablecoin)
2. Review: [docs/case_studies/vortex_spring_water_tokenization.md](docs/case_studies/vortex_spring_water_tokenization.md) (RWA tokenization example)
3. Evaluate: Liquidity scoring results (Section 4 above)
4. Connect: Discuss partnership via [GitHub Issues](https://github.com/kevanbtc/XRPL-Template-system/issues)

### For AI/Analysis Work

```bash
# Run policy-driven AI swarm (dry-run mode)
python ai/run.py --policy policies/default.yaml --dry-run

# Output: Analysis report without executing any operations
```

**Note**: AI swarm is in **dry-run mode** by default. It analyzes compliance gaps, suggests policies, but does NOT execute any on-chain transactions.

---

## 🆘 Troubleshooting

### Python Import Errors

```bash
# If you see "ModuleNotFoundError"
pip install -r requirements.txt --upgrade
```

### Git Clone Issues

```bash
# If GitHub authentication fails
git config --global credential.helper store
git clone https://github.com/kevanbtc/XRPL-Template-system.git
```

### XRPL Node Sync Issues

- **Testnet node not syncing**: Check firewall rules (port 51235 must be open for peers)
- **Docker container crashes**: Increase Docker memory limit to 4GB+

### Compliance Template Confusion

- **Too many templates?** Start with [GLOBAL-COMPLIANCE-FRAMEWORK.template.md](docs/compliance/GLOBAL-COMPLIANCE-FRAMEWORK.template.md) only. It consolidates all others.
- **Which jurisdiction?** See [JURISDICTION-COMPLIANCE-MAP.md](docs/compliance/JURISDICTION-COMPLIANCE-MAP.md) Table 1 for quick reference.

---

## 📚 Additional Resources

- **[README.md](README.md)** – Project overview and badges
- **[ARCHITECTURE.md](ARCHITECTURE.md)** – Full technical deep dive
- **[docs/README.md](docs/README.md)** – Documentation hub
- **[docs/compliance/README.md](docs/compliance/README.md)** – Compliance documentation guide
- **[Contributing Guidelines](CONTRIBUTING.md)** – How to contribute (coming soon)

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/kevanbtc/XRPL-Template-system/issues)
- **Discussions**: [GitHub Discussions](https://github.com/kevanbtc/XRPL-Template-system/discussions)
- **Security**: security@[domain].com (for vulnerabilities only)

---

**Welcome to the XRPL Sovereign Bank Rack System!** 🚀

You're now ready to start building your compliant XRPL stablecoin issuer platform.
