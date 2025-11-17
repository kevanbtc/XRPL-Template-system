# Weekly liquidity workflow runner (Windows PowerShell)
# Runs scoring, generates grouped index, snapshots history, and executes AI dry-run.

param(
  [string]$Date = (Get-Date -Format 'yyyy-MM-dd')
)

$ErrorActionPreference = 'Stop'

Write-Host "==> Ensuring output and history directories exist"
New-Item -ItemType Directory -Force -Path output, history\asset_scores, history\assets_index, output\ai_runs | Out-Null

Write-Host "==> Running asset scoring"
python scripts/asset_scoring.py

Write-Host "==> Generating grouped assets index"
python scripts/generate_assets_index.py --input output/asset_scores.csv --output output/Assets.current.md

Write-Host "==> Snapshotting history to date $Date"
Copy-Item output\asset_scores.csv  "history\asset_scores\asset_scores-$Date.csv"
Copy-Item output\Assets.current.md "history\assets_index\Assets-$Date.md"

Write-Host "==> Running AI swarm (dry-run)"
if (Test-Path ai\run.py) {
  python ai\run.py
} else {
  Write-Warning "ai\run.py not found; skipping AI dry-run"
}

Write-Host "==> Done. Outputs in output\\ and history\\ folders. Forensic logs in output\\ai_runs\\."
