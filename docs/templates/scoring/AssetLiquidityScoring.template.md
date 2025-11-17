# Asset Liquidity & Quick-Money Scoring Framework (Template)

> Purpose: Rank assets by their probability of producing near-term deployable liquidity (0–180 day window) with minimal friction.

## Scoring Overview
Each asset receives 0–5 raw scores across criteria. Weighted sum → 0–100 composite. Categories:
- **Immediate (≥80):** Prioritize full monetization sprint now
- **Near-Term (60–79):** Prep verification; queue for next sprint
- **Background (40–59):** Light monitoring; no major spend
- **Archive (<40):** Document only; zero active budget

## Criteria & Weights (Adjustable)
| Code | Criterion | Description | Raw (0–5) Guidance | Weight (%) |
|------|-----------|-------------|--------------------|------------|
| VF   | Verification Friction (inverse) | Ease of proving ownership/condition | 5 = turnkey docs; 0 = missing chain-of-title | 12 |
| LD   | Liquidity Depth | Size & reliability of buyer/lender market | 5 = multiple institutional channels; 0 = fantasy market | 15 |
| TTC  | Time-to-Cash | Expected days to first cash draw | 5 ≤ 30d; 4 ≤ 60d; 3 ≤ 90d; 2 ≤ 120d; 1 ≤ 180d; 0 > 180d | 20 |
| LTV  | Realizable LTV Yield | Conservative LTV * nominal size potential | 5 ≥ 100M usable; 4 ≥ 50M; 3 ≥ 10M; 2 ≥ 1M; 1 ≥ 250K; 0 < 250K | 18 |
| CR   | Counterparty Readiness | Warm path to credible lenders/buyers | 5 = active dialogues; 0 = unknown path | 10 |
| CC   | Compliance Cleanliness | KYC/AML/reg risk level | 5 = low risk, standard asset; 0 = sanctions/illicit red flags | 8 |
| EC   | Execution Complexity (inverse) | Operational steps count/coordination | 5 = few steps, internal; 0 = many external dependencies | 10 |
| NL   | Narrative Leverage | Boost to broader fundraising/reputation | 5 = high signaling power; 0 = confusing or negative | 7 |

Total weights default: 100%. Adjust in `AssetScoringWeights.jsonc`.

## Raw Scoring Guidance
- Assign 0–5 per criterion using defined thresholds.
- Use the lowest plausible number in uncertainty (conservative bias).
- Gate: If VF ≤1 or CC ≤1 → auto cap composite ≤59 (cannot enter Near-Term/Immediate) unless board override.

## Composite Score Formula
```
composite = Σ( raw_i / 5 * weight_i ) * (100 / Σweights)
```
Apply gating reductions:
- High compliance risk: composite = min(composite, 50)
- Verification unresolved >60d: composite -= 10

## Priority Buckets Actions
| Bucket | Action | Spend Cap | Review Cadence |
|--------|--------|-----------|----------------|
| Immediate | Full facility/appraisal/oracle sprint | As budgeted | Weekly deep dive |
| Near-Term | Prep docs, line up counterparties | 25K | Bi-weekly |
| Background | Passive monitoring, minimal reach-outs | 5K | Monthly |
| Archive | No spend; maintain dossier/IPFS | 0 | Quarterly |

## Example Scoring (Illustrative)
| Asset | VF | LD | TTC | LTV | CR | CC | EC | NL | Composite | Bucket |
|-------|----|----|-----|-----|----|----|----|----|----------|--------|
| Rubies (post re-appraisal) | 4 | 4 | 3 | 4 | 3 | 5 | 3 | 4 | 74 | Near-Term → Immediate after appraisal |
| Santander notes (pre bank letter) | 2 | 3 | 2 | 4 | 2 | 4 | 3 | 5 | 63 | Near-Term |
| Unykorn IP licensing (pilot clients) | 5 | 4 | 4 | 3 | 4 | 5 | 4 | 4 | 82 | Immediate |
| IP-backed note (after 3 licenses) | 5 | 3 | 4 | 3 | 4 | 5 | 4 | 4 | 80 | Immediate |
| IQD boxes | 1 | 0 | 0 | 1 | 0 | 2 | 2 | 2 | 23 | Archive |
| Historic bonds | 1 | 0 | 0 | 0 | 0 | 3 | 2 | 1 | 19 | Archive |

## Data Structure (assets.json Entry Template)
```json
{
  "name": "Rubies Collection",
  "codes": {
    "VF": 4,
    "LD": 4,
    "TTC": 3,
    "LTV": 4,
    "CR": 3,
    "CC": 5,
    "EC": 3,
    "NL": 4
  },
  "tags": ["RWA", "gem"],
  "notes": "Awaiting updated appraisal & insurance placement",
  "gates": {"verification_days": 20, "compliance_risk": false}
}
```

## Implementation Steps
1. Populate `data/assets.json` with current assets
2. Tune weights in `AssetScoringWeights.jsonc` if strategy changes (e.g. favor TTC more → raise weight)
3. Run `asset_scoring.py` → outputs ranked table + CSV
4. Review gating flags; adjust raw scores after new verification events
5. Commit updated scores monthly (versioned, CID if desired)

## Override Policy
- Board override can promote a Near-Term asset to Immediate if: signed term sheet OR lender LOI
- Archive assets require formal justification to move above Background (e.g., new legal opinion creating credible market)

## Change Log
- v1.0: Initial weighting focused on fastest liquidity (higher TTC and LTV emphasis)
