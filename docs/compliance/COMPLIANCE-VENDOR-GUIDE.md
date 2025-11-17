# Compliance Vendor Integration Guide

**Version:** 1.0  
**Last Updated:** 2025-01-17  
**Purpose:** Guide for selecting and integrating third-party compliance vendors into XRPL/RWA platform operations

---

## Overview

You won't find *one* vendor that does KYC, Travel Rule, securities law, cybersecurity, and oracle PoR all in one box. But you *can* assemble a small, repeatable roster that covers all the bases.

This guide explains:
1. **What vendors do** (KYC, analytics, Travel Rule, oracles)
2. **Who the real players are**
3. **How they integrate** with your XRPL/FTH stack
4. **What you get from each**

---

## 1. KYC / KYB / AML Onboarding (Front Door)

### What They Do

These are the "show me your passport / selfie / company docs" people. They handle:
- Identity verification (document scanning, biometrics, liveness checks)
- KYB (Know Your Business) for corporate entities
- Sanctions/PEP screening (OFAC, UN, EU, UK HMT, etc.)
- Ongoing monitoring and document expiration alerts

### Recommended Vendors

| Vendor | Strengths | Coverage | Crypto-Friendly? |
|--------|-----------|----------|------------------|
| **Sumsub** | KYC, KYB, AML screening; 220+ countries, documents, PoA, sanctions | Global | ✅ Very |
| **Onfido** | AI identity verification, doc scans + biometrics, fraud detection | Global | ✅ Yes |
| **Veriff** | Strong doc coverage + fraud detection; fintech/crypto focus | Global | ✅ Yes |
| **Persona** | Modular identity flows, good UX, flexible risk rules | US/Global | ✅ Yes |
| **Trulioo** | Extensive global ID database, good for emerging markets | 195+ countries | ✅ Yes |
| **Jumio** | Strong liveness detection, government ID verification | Global | ✅ Yes |
| **Socure** | AI-powered identity verification, synthetic fraud detection | US-focused | ⚠️ Mixed |

### Integration Pattern

```
User Flow:
1. User visits FTH platform → clicks "Create Account"
2. Frontend: POST /kyc/start → redirect to vendor's flow
3. User completes KYC (uploads ID, takes selfie, etc.)
4. Webhook: Vendor posts back status → you map APPROVED | REVIEW | REJECTED
5. Your system:
   - APPROVED → enable XRPL trustline, allow minting/redemption
   - REVIEW → manual compliance review queue
   - REJECTED → deny access, log reason
```

**XRPL Integration:**
- Your issuer/gateway only opens trustlines or mints IOUs once KYC flag is green
- Store KYC status in off-chain compliance registry (database) mapped to XRPL addresses
- For high-security: require KYC re-verification before large redemptions

**APIs to Implement:**
- `POST /api/kyc/initiate` → create session with vendor
- `POST /api/kyc/webhook` → receive status updates
- `GET /api/kyc/status/:userId` → check current KYC status
- `POST /api/kyc/refresh` → trigger periodic re-verification

---

## 2. Blockchain Analytics / Wallet Risk Scoring

### What They Do

These are the **"watch every address that touches us"** providers:
- Wallet risk scoring (darknet, sanctioned, hacked funds, mixing)
- Transaction monitoring and behavioral analysis
- Investigations and case management
- Travel Rule compliance (some providers)
- Real-time alerts for high-risk counterparties

### Recommended Vendors

| Vendor | Strengths | XRPL Support | Notes |
|--------|-----------|--------------|-------|
| **Chainalysis** | 800-lb gorilla; wallet risk, transaction monitoring, investigations | ⚠️ Limited native | Primarily BTC/ETH/EVM; may need custom integration for XRPL |
| **Elliptic** | Strong risk-based monitoring, training for compliance teams | ⚠️ Limited native | Similar to Chainalysis; strong on typologies |
| **TRM Labs** | Real-time risk graph, government partnerships, Travel Rule | ⚠️ Limited native | Fast-growing; good API |
| **Crystal** | Blockchain intelligence + Travel Rule tooling | ⚠️ Check coverage | May have better XRPL support than others |
| **Beosin** | Security audits + blockchain analytics | ✅ Some | Asia-focused; good for XRPL bridges |
| **Global Ledger** | Smaller player, flexible integrations | ? | Worth evaluating for custom XRPL work |

**XRPL Challenge:** Most analytics tools focus on Bitcoin/Ethereum/EVM chains. XRPL support is limited. You may need:
- Custom integration via their APIs
- Or: focus on **bridge monitoring** (when assets move from XRPL → EVM or CEX)

### Integration Pattern

```
Transaction Flow:
1. User submits issuance/redemption request
2. Your system: extract source/destination XRPL address
3. API call to analytics vendor: POST /risk-score
   {
     "address": "rXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "blockchain": "xrpl"
   }
4. Vendor returns risk score (0-100) + risk factors
5. Your system:
   - Low risk (0-30): auto-approve
   - Medium risk (31-70): manual review
   - High risk (71-100): reject or freeze, file SAR

6. For ongoing monitoring:
   - Pipe all transactions to vendor via webhook or batch API
   - Vendor flags sanctioned addresses or suspicious patterns
   - Your ops team investigates alerts
```

**XRPL-Specific Considerations:**
- Monitor **issuer account** for unexpected trustlines (potential wash trading)
- Track **large transfers** between hot wallets and unknown addresses
- Flag **bridge transactions** (XRPL → Ethereum/Polygon) as higher risk
- Integrate with **DEX order book monitoring** (unusual FTHUSD/XRP trading patterns)

**APIs to Implement:**
- `POST /api/analytics/screen-address` → check wallet risk before allowing trustline
- `POST /api/analytics/monitor-transaction` → submit completed tx for retrospective analysis
- `GET /api/analytics/alerts` → fetch flagged transactions for review
- `POST /api/analytics/case-management` → create investigation case for SAR filing

---

## 3. Travel Rule (FATF R.16) / VASP-to-VASP Messaging

### What It Is

**Travel Rule** = FATF Recommendation 16:
- When you transfer >$1000 (or local equivalent) of crypto, you must exchange originator/beneficiary info with the counterparty VASP
- Applies to **VASP-to-VASP** transfers (not internal wallet-to-wallet within same platform)

### What They Do

- Pre-transaction screening (is counterparty a registered VASP?)
- VASP due diligence and reputation scores
- Secure messaging (encrypted originator/beneficiary data exchange)
- Self-hosted wallet handling (when user withdraws to personal wallet)
- Compliance reporting and audit trails

### Recommended Vendors

| Vendor | Strengths | Network Model | Notes |
|--------|-----------|---------------|-------|
| **Notabene** | Purpose-built for Travel Rule, VASP due diligence, sanctions | Network-based | Widely adopted; good APAC/EU coverage |
| **21 Analytics** | Data-protected VASP messaging, self-hosted wallet handling | Software-based | Privacy-focused; good for EU/Switzerland |
| **Shyft Network** | Blockchain-native Travel Rule protocol, VASP registry | Blockchain network | Token-based incentives; decentralized |
| **VerifyVASP** | VASP identity verification and messaging | Directory-based | Lightweight; good for smaller VASPs |
| **TRISA** | Open-source Travel Rule protocol, non-profit | Federated network | Free; requires technical setup |
| **Crystal Travel Rule** | Integrated with Crystal analytics platform | Software + network | Combined analytics + Travel Rule |

### Integration Pattern

```
Withdrawal Flow (User sends FTHUSD to external XRPL address):
1. User submits withdrawal request:
   {
     "amount": 5000,
     "destination": "rExternalAddress...",
     "asset": "FTHUSD"
   }

2. Your system checks if Travel Rule threshold exceeded (>$1000 or equivalent)

3. If YES:
   a. Call Travel Rule vendor API:
      POST /vasp/lookup
      {
        "address": "rExternalAddress...",
        "blockchain": "xrpl"
      }
   
   b. Vendor responds:
      - Custodial (VASP): "Binance XRPL hot wallet"
      - Self-hosted: "Non-custodial wallet"
   
   c. If VASP:
      - Exchange originator/beneficiary info via vendor's messaging protocol
      - Confirm counterparty VASP accepts transfer
      - Proceed with transaction
   
   d. If self-hosted:
      - Require user to prove control (sign message with private key)
      - Record attestation that user owns destination wallet
      - Proceed with transaction

4. Log all Travel Rule data for 5+ years (recordkeeping requirement)
```

**XRPL-Specific Considerations:**
- XRPL DEX trades (FTHUSD/XRP) *within* your platform = **no Travel Rule** (same VASP)
- XRPL → CEX deposit = **Travel Rule applies** (different VASPs)
- XRPL → personal wallet = **depends on jurisdiction** (some require self-hosted attestation)

**APIs to Implement:**
- `POST /api/travel-rule/check-threshold` → determine if Travel Rule applies
- `POST /api/travel-rule/vasp-lookup` → identify counterparty VASP
- `POST /api/travel-rule/exchange-data` → send originator info, receive beneficiary info
- `GET /api/travel-rule/audit-trail` → export Travel Rule records for regulators

---

## 4. Oracles & Proof of Reserve (PoR)

### What They Do

These are your **"machine of truth"** for reserves and external data:
- Publish reserve balances on-chain (cryptographic proof)
- Enable smart contracts to gate issuance based on reserves
- Provide price feeds (for collateralized or basket-backed tokens)
- Attest to off-chain data (bank balances, custodian holdings)

**Chainlink is not your KYC vendor.** It's your **reserve integrity** layer.

### Recommended Vendors

| Vendor | Strengths | XRPL Support | Use Case |
|--------|-----------|--------------|----------|
| **Chainlink** | Proof of Reserve (PoR), price feeds, cross-chain interop | ⚠️ Limited native | Industry standard; used by TUSD, PAXG; may need bridge for XRPL |
| **Pyth Network** | High-frequency price oracles, low-latency | ⚠️ Limited native | Good for trading apps; less PoR-focused |
| **RedStone** | Modular oracles, gas-efficient, supports multiple chains | ⚠️ Check coverage | Emerging player; flexible data sources |
| **API3** | First-party oracles (data providers run nodes directly) | ⚠️ Limited native | Good for custom data feeds |
| **Supra** | Fast finality, cross-chain oracle, VRF | ⚠️ Check coverage | Newer; worth evaluating |

### Integration Pattern

```
Reserve Attestation Flow:
1. Off-chain reserves (bank, custodian, T-bills)
   ↓
2. Periodic attestation by bank/custodian
   → Signed statement: "Account X holds $Y as of date Z"
   ↓
3. Attestation pushed to oracle network (Chainlink PoR)
   → Oracle nodes verify + sign
   → Aggregated proof published on-chain
   ↓
4. Your issuance contract/engine reads oracle feed
   → IF (circulating_supply + mint_request) > PoR_balance:
      REJECT mint
   → ELSE:
      APPROVE mint

5. Dashboard displays PoR feed + circulating supply in real-time
```

**XRPL Integration:**
- **Problem:** Chainlink doesn't natively support XRPL (no smart contracts on XRPL)
- **Solution 1:** Use Chainlink on EVM sidechain (e.g., Ethereum, Polygon) and bridge data to XRPL via **off-chain oracle service** that posts memo fields to XRPL Reserve Vault account
- **Solution 2:** Build custom oracle that:
  - Reads Chainlink PoR feeds
  - Publishes reserve hashes to XRPL memo fields
  - Your backend enforces mint limits based on those hashes

**Example XRPL Memo Structure:**
```json
{
  "type": "PoR",
  "date": "2025-01-17",
  "reserves_usd": 50000000,
  "circulating_fthusd": 49500000,
  "chainlink_feed": "0x...",
  "ipfs_report": "Qm..."
}
```

**APIs to Implement:**
- `GET /api/reserves/current` → fetch latest PoR data
- `POST /api/reserves/attest` → trigger new attestation (manual or scheduled)
- `GET /api/reserves/history` → export historical PoR records
- `GET /api/reserves/verify/:txid` → verify specific XRPL memo against Chainlink feed

---

## 5. Vendor Integration Architecture

### Overall System Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                     FTH / Unykorn Platform                   │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  User Onboarding                                             │
│  ├─ KYC/KYB Provider (Sumsub/Onfido) ─→ Compliance Registry│
│  └─ Sanctions Screening (OFAC/UN/EU)                        │
│                                                               │
│  Transaction Monitoring                                      │
│  ├─ Blockchain Analytics (Chainalysis/TRM) ─→ Alert Queue  │
│  ├─ Travel Rule (Notabene/21Analytics) ─→ VASP Messaging   │
│  └─ Behavioral Monitoring (Internal + Vendor)               │
│                                                               │
│  Reserve Integrity                                           │
│  ├─ Bank/Custodian Attestations ─→ Chainlink PoR           │
│  ├─ Oracle Feed ─→ XRPL Memo Fields (Reserve Vault)        │
│  └─ Issuance Engine (checks PoR before minting)             │
│                                                               │
│  XRPL Operations                                             │
│  ├─ Issuer Account (FTHUSD, WTR.VRTX, etc.)                │
│  ├─ Treasury Account (minting, distribution, fees)          │
│  ├─ Reserve Vault (holds RLUSD/USDC backing + PoR memos)   │
│  └─ Redemption Sink (burns redeemed tokens)                 │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### Vendor Selection Criteria

When evaluating vendors, consider:

1. **Regulatory Coverage**
   - Do they support your target jurisdictions (US, EU, UK, SG, UAE, HK)?
   - Are they certified/approved by regulators in those jurisdictions?

2. **Blockchain Support**
   - Native XRPL support (rare) vs. need for custom integration
   - API quality and documentation
   - Rate limits and SLAs

3. **Cost Structure**
   - Per-verification pricing (KYC)
   - Monthly minimums (analytics, Travel Rule)
   - Enterprise vs. startup tiers

4. **Integration Effort**
   - SDK availability (JS, Python, Go)
   - Webhook support
   - Time to production (weeks vs. months)

5. **Data Privacy & Security**
   - SOC 2 Type II certified?
   - GDPR compliance?
   - Data residency options?

6. **Vendor Lock-In**
   - Can you switch vendors without major re-architecture?
   - Do they use proprietary formats or open standards?

---

## 6. Recommended Vendor Stack by Phase

### Phase 1: Whitelist-Only / Pilot (Current)

**Minimal viable stack:**
- **KYC/KYB:** Sumsub or Onfido (1 vendor, manual review for edge cases)
- **Analytics:** TRM Labs or Elliptic (bridge monitoring focus)
- **Travel Rule:** None yet (internal-only transfers)
- **Oracles:** Manual reserve attestations via IPFS + XRPL memos

**Cost:** $5K–$15K/month

---

### Phase 2: Institutional Expansion

**Add:**
- **Analytics:** Upgrade to Chainalysis (full suite with investigations)
- **Travel Rule:** Notabene or 21 Analytics (prepare for VASP-to-VASP flows)
- **Oracles:** Chainlink PoR pilot (EVM sidechain + bridge to XRPL)

**Cost:** $25K–$50K/month

---

### Phase 3: Bank Co-Issuance / Multi-Jurisdiction

**Add:**
- **KYC/KYB:** Multi-vendor redundancy (Sumsub + Trulioo for emerging markets)
- **Analytics:** Add secondary vendor (Elliptic or TRM) for cross-validation
- **Travel Rule:** Full integration with multiple Travel Rule networks
- **Oracles:** Production Chainlink PoR with real-time feeds

**Cost:** $100K–$250K/month

---

### Phase 4: Retail / Global

**Add:**
- **KYC/KYB:** Regional specialists (e.g., Jumio for APAC, Persona for US)
- **Analytics:** Full Chainalysis suite + TRM for redundancy
- **Travel Rule:** Multi-network coverage (Notabene + TRISA)
- **Oracles:** Decentralized oracle network (Chainlink + RedStone)

**Cost:** $500K+/month

---

## 7. Vendor Onboarding Checklist

For each vendor:

- [ ] Sign NDA and review contract terms
- [ ] Complete vendor security questionnaire (SOC 2, pen test results, etc.)
- [ ] Set up sandbox/test environment
- [ ] Implement API integration (POC)
- [ ] Test happy path + edge cases
- [ ] Load test (check rate limits)
- [ ] Document integration in internal wiki
- [ ] Train compliance team on vendor tools
- [ ] Set up monitoring/alerting for vendor API downtime
- [ ] Establish escalation path for vendor support
- [ ] Review and approve invoice/billing structure
- [ ] Go live in production
- [ ] Schedule quarterly vendor review

---

## 8. Vendor Risk Management

### Vendor Concentration Risk

**Problem:** Over-reliance on single vendor for critical function (e.g., only Chainalysis for analytics)

**Mitigation:**
- Maintain relationships with 2+ vendors per category
- Implement "hot swap" capability (can switch vendors in <1 week)
- Export data regularly to avoid vendor lock-in

### Vendor Downtime Risk

**Problem:** Vendor API outage blocks critical operations (e.g., KYC checks)

**Mitigation:**
- Cache vendor responses (KYC status, risk scores) for graceful degradation
- Implement fallback to manual review during outages
- Set up status page monitoring (vendor's uptime metrics)
- Include SLA credits in contracts

### Data Privacy & Cross-Border Risk

**Problem:** Vendor stores data in jurisdiction with unfavorable laws (e.g., China, Russia)

**Mitigation:**
- Specify data residency in contracts (e.g., "EU-only" or "US-only")
- Use vendors with regional data centers
- Implement data minimization (don't send unnecessary PII to vendors)
- Regular audits of vendor's data handling practices

---

## 9. Next Steps

1. **Immediate (Phase 1):**
   - [ ] Sign contracts with 1 KYC vendor (Sumsub or Onfido)
   - [ ] Set up sandbox integrations
   - [ ] Document API flows for XRPL onboarding

2. **Short-Term (Phase 2):**
   - [ ] Evaluate blockchain analytics vendors (TRM, Chainalysis, Elliptic)
   - [ ] Pilot Travel Rule integration (Notabene or 21 Analytics)
   - [ ] Design Chainlink PoR architecture for XRPL

3. **Medium-Term (Phase 3+):**
   - [ ] Add vendor redundancy (2nd KYC provider, 2nd analytics provider)
   - [ ] Build internal compliance dashboard aggregating all vendor data
   - [ ] Automate quarterly vendor reviews

---

## Related Documentation

- **[KYC-AML-PROGRAM.template.md](KYC-AML-PROGRAM.template.md)** – KYC/AML policy framework that these vendors implement
- **[JURISDICTION-COMPLIANCE-MAP.md](JURISDICTION-COMPLIANCE-MAP.md)** – Regulatory requirements by jurisdiction
- **[SECURITY-CONTROLS.template.md](SECURITY-CONTROLS.template.md)** – Technical controls for vendor integration

---

**Document Version:** 1.0  
**Last Updated:** 2025-01-17  
**Owner:** Compliance + Engineering Teams  
**Review Cycle:** Quarterly or when adding new vendors
