# Dev Environment Guide – XRPL Liquidity Engine + AI Swarm

This doc explains how to set up a local dev env on Windows (PowerShell) and run:

- The asset scoring engine
- The grouped assets index generator
- The AI swarm dry-run

---

## 1. Prerequisites

- Python 3.11+
- Git
- Optional: Docker and Git Bash

Check Python:

```powershell
python --version
```

If you have both `python` and `py`, be consistent (this doc assumes `python`).

---

## 2. Install dependencies

From the repo root:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

This installs:

- PyYAML – for policy loading
- pytest – for tests
- Any other libs listed in `requirements.txt`

---

## 3. Core workflow (weekly cadence)

### 3.1 Run scoring

```powershell
python scripts/asset_scoring.py
```

Outputs:

- `output\asset_scores.csv` – machine-readable scores
- `output\asset_scores.md` – human-readable breakdown

### 3.2 Generate grouped assets index

```powershell
python scripts/generate_assets_index.py --input output/asset_scores.csv --output output/Assets.current.md
```

Now `output\Assets.current.md` is your grouped index by bucket:

- Immediate
- Near-Term
- Background
- Archive
- Reject

### 3.3 Snapshot history

```powershell
$date = Get-Date -Format 'yyyy-MM-dd'

New-Item -ItemType Directory -Force -Path history\asset_scores, history\assets_index | Out-Null

Copy-Item output\asset_scores.csv  "history\asset_scores\asset_scores-$date.csv"
Copy-Item output\Assets.current.md "history\assets_index\Assets-$date.md"
```

This gives you a dated trail of how rankings evolved.

### 3.4 Run the AI swarm dry-run

```powershell
python ai\run.py
```

You’ll see:

- Focus assets (by score & bucket)
- Market opportunities (net bps, after fees)
- Approved opportunities (after risk gates)
- Dry-run trade plan (sizes + expected profit)

Swarm also writes forensic logs to:

- `output\ai_runs\ai_run_*.json`

(These are `.gitignore`’d; treat them as local evidence or ship them to a secure store.)

---

## 4. Running tests

From repo root:

```powershell
pytest -q
```

This validates:

- Policy/config loading is sane
- Risk agent gates behave correctly (score, bucket, net bps)

CI runs the same command on every push/PR.

---

## 5. Docker usage (optional)

Build:

```powershell
docker build -t xrpl-liquidity-swarm .
```

Run:

```powershell
docker run --rm xrpl-liquidity-swarm
```

Mount local `output` for persistence:

```powershell
docker run --rm -v ${PWD}\output:/app/output xrpl-liquidity-swarm
```

---

## 6. Files to know

- `scripts/asset_scoring.py` – scoring engine
- `scripts/generate_assets_index.py` – Assets.current.md generator
- `docs/scoring/README.md` – ops manual for scoring + buckets + cadence
- `docs/scoring/Assets.current.md` – grouped index output
- `docs/templates/scoring/*` – intake, focus, reject log, sprint board
- `ai/run.py` – AI swarm entry point
- `ai/config/ai_policy.yaml` (and/or `config/ai_policy.yaml`) – policy source of truth
- `output/ai_runs/` – forensic AI run logs
- `../fth-xrpl-financial-os/docs/security/README.md` – companion security doctrine (external repo)

---

## 7. Safety and governance

- AI swarm is dry-run only – no live orders.
- All thresholds live in YAML policy, not in code.
- Runs produce forensic JSON for Legal/Compliance review.
- CI enforces tests and an AI swarm sanity check.

Treat this repo as the liquidity machine front-end under the broader FTH XRPL Financial OS security umbrella.
