# Asset Liquidity Scoring

Compute composite scores to prioritize assets that convert to cash the fastest with strong LTV and real market depth.
 
## Overview

This doc explains how to run the RWA Liquidity Scoring Engine, interpret outputs, and turn them into a concrete 7–14 day cash plan.

---

## 1. Components

- Engine
  - `scripts/asset_scoring.py`
  - `docs/templates/scoring/AssetIntake.template.md`
  - `docs/templates/scoring/AssetLiquidityFocus.template.md`
  - `docs/templates/scoring/LiquiditySprintBoard.template.md`
  - `docs/templates/scoring/RejectLog.template.md`

- Data & Config
  - `data/assets.json` – raw asset definitions
  - `docs/templates/scoring/AssetIntake.template.md` – intake structure
  - `docs/templates/scoring/RejectLog.template.md` – rejection structure
  - `docs/templates/scoring/AssetLiquidityFocus.template.md` – sprint plan scaffold

- Outputs
  - `output/asset_scores.csv` – machine-readable, for BI
  - `output/asset_scores.md` – human-readable explanations
  - `output/Assets.current.md` – ranked asset index (can be copied into `docs/scoring/Assets.current.md`)

---

## 2. Scoring Criteria

Each asset has 5 core criteria, each scored 0–5:

- TTC – Time-to-Cash
  - 0 – No credible path-to-cash
  - 5 – Cash in days/weeks with clear, live counterparties
- LTV – Loan-to-Value potential
  - 0 – No lender would reasonably lend
  - 5 – Conventional / institutional LTV possible
- LD – Liquidity Depth
  - 0 – Extremely niche or fantasy buyers
  - 5 – Deep market with many buyers, real size
- CC – Compliance / Cleanliness
  - 0 – Serious regulatory or KYC/AML problems
  - 5 – Clean KYC/docs/jurisdiction, no sanctions issues
- VF – Verification / Proof quality
  - 0 – Hearsay only, no documents
  - 5 – Notarized docs, on-chain or bank-verified, strong paper trail

Weights, gates, and thresholds live in your weights/config file (JSON/JSONC). Tune them to your strategy.

---

## 3. Hard Gates & Reject Rules

An asset is Reject / Dogshit if any:

- TTC == 0
- VF <= 1
- CC <= 1
- LD <= 1 AND LTV <= 1

Rejected assets are pinned to the bottom, labeled Reject, and appear in the MD report with reasons. Log them in `RejectLog.template.md`.

---

## 4. Buckets & Bandwidth

- Immediate – 1–3 assets, execute now, ~40% of bandwidth
- Near-Term – unlock 1–3 things then promote to Immediate
- Background – cheap doc/proof work while Immediate runs
- Archive – real but not worth cycles right now
- Reject / Dogshit – stop unless facts change

---

## 5. Weekly Ops Cadence

1) Monday – Intake & Update

- Intake new assets using `AssetIntake.template.md`.
- Update `data/assets.json` with scores and counterparties.

1) Run scoring

```bash
python scripts/asset_scoring.py
```

This regenerates:

- `output/asset_scores.csv`
- `output/asset_scores.md`
- `output/Assets.current.md`

Copy or symlink `output/Assets.current.md` → `docs/scoring/Assets.current.md` if you want it versioned with docs.

---

1) Midweek – Focus & Execution

- Identify top Immediate and Near-Term from `asset_scores.md`.
- Fill `AssetLiquidityFocus.template.md` for 1–3 Immediate items (each with owner, deadline, path to wired cash).
- Translate into `LiquiditySprintBoard.template.md` for tracking.

---

1) Friday – Review & Reject Discipline

- Review Rejects and log them in `RejectLog.template.md` with reasons.
- Adjust scores next week only if evidence changes.

---

## 6. How to Tune Weights

- Speed/certainty: raise TTC and LD.
- Collateral focus: raise LTV.
- Compliance/partner trust gating: raise VF and CC.

After changes:

1) Commit updated weights
1) Re-run scoring
1) Compare rankings to prior run

---

## 7. Humans vs. Machines

- Humans
  - `output/asset_scores.md`
  - `docs/scoring/Assets.current.md`
  - `AssetLiquidityFocus.template.md`
  - `LiquiditySprintBoard.template.md`
  - `RejectLog.template.md`

- Machines
  - `output/asset_scores.csv`
  - `data/assets.json`

This setup lets analysts, lenders, and automation look at the same reality from different angles.

---

## 8. Buckets & Thresholds (Canonical)

These thresholds are mirrored in `scripts/asset_scoring.py` and must be updated in lockstep.

- Immediate
  - Score ≥ 75
  - TTC ≥ 4
  - VF ≥ 4 and CC ≥ 4
- Near-Term
  - Score ≥ 55 and < 75
  - TTC ≥ 3
  - VF ≥ 3 and CC ≥ 3
- Background
  - Score ≥ 35 and < 55
- Archive
  - Score < 35 but not hard-reject
- Reject / "Dogshit"
  - Any of:
    - TTC == 0
    - VF ≤ 1
    - CC ≤ 1
    - (LD ≤ 1 AND LTV ≤ 1)

---

## 9. Liquidity vs. Risk

- Liquidity: TTC, LD, LTV
- Risk / Legitimacy: VF, CC, counterparties

Two assets with similar scores may have very different profiles:

- Fast but hairier (high liquidity, lower verification)
- Slower but pristine (lower liquidity, high verification)

Use the score to prioritize time, not to blindfold risk judgment.

---

## 10. History & Snapshots

After each weekly run:

- Keep `output/asset_scores.csv` and `output/Assets.current.md` as the current view.
- Copy them into a dated snapshot:
  - `history/asset_scores/asset_scores-YYYY-MM-DD.csv`
  - `history/assets_index/Assets-YYYY-MM-DD.md`

These snapshots form the audit trail that shows:

- How rankings changed over time
- When assets moved buckets
- When Reject/"Dogshit" assets were reconsidered

---

## 11. See also

- Security & Sovereign Infra: `../security/README.md`
- Compliance Evidence Index: `../security/compliance/evidence-index.md`

## AI Swarm Integration (Policy-Driven)


> This repo includes a policy-driven AI swarm that consumes your scoring CSV and proposes dry-run trades for review.

- Policy file: i/config/ai_policy.yaml (risk, liquidity, swarm)
- Runtime loader: i/src/config.py (graceful defaults if YAML missing)
- Runner: i/run.py (dry-run only; no live orders)
- Forensic logs: output/ai_runs/ai_run_*.json (audit-ready per-run trail)

### Contract
- Input: docs/scoring/Assets.current.md and the underlying CSV produced by scripts/asset_scoring.py.
- Output: Markdown console summary + JSON forensic log with all decisions.
- Gates: Allowed buckets, min score, min net bps, max trades, position/portfolio caps.

### How to run (local)
- Python 3.11+; optional PyYAML for policy loading (falls back to defaults if not installed).
- Execute python ai/run.py to simulate a policy-aligned dry-run and write a forensic log.

### Safety & Legal
- Dry-run only; no exchange/CEX/XRPL adapters are wired.
- All thresholds are policy-governed and versioned. Logs are immutable artifacts for audits.

## Weekly Cadence (Extended)

Use this to institutionalize the flow from intake  scoring  focus  sprint  AI dry-run planning  review:

1) Intake: Capture assets using docs/templates/scoring/AssetIntake.template.md.
2) Score: Run scripts/asset_scoring.py and regenerate the grouped index via scripts/generate_assets_index.py.
3) Focus: Curate AssetLiquidityFocus.template.md using the latest buckets (Immediate/Near-Term/Mid-Term).
4) Sprint: Plan execution in LiquiditySprintBoard.template.md (48h window).
5) AI Dry-Run: python ai/run.py to produce a plan and an audit log.
6) Review Board: Approve or reject dry-run proposals; update RejectLog.template.md with reasons.
7) Snapshot: Commit docs/scoring/Assets.current.md and store a dated copy under history/ for traceability.
8) Iterate: Tune i/config/ai_policy.yaml only via PR and review.

Tip: The AI runner will ignore 'Reject' bucket assets and enforce min net bps and score gates to filter noise.
