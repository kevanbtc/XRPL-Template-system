#!/usr/bin/env python3
"""Asset Liquidity Scoring Script
Reads asset data and scoring weights, computes composite liquidity priority scores.
Outputs:
  - Markdown table: output/asset_scores.md
  - CSV: output/asset_scores.csv
  - Optional Focus summary: output/Focus.current.md
  - Stdout summary table (optional)

Scoring Formula (per asset):
  composite = sum( (criterion_score/5)*weight ) * (100 / sum(weights))
Then gating & penalties adjust composite.
Buckets determined by threshold values in weights file.
"""
import argparse
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "assets.json"
WEIGHTS_FILE = ROOT / "docs" / "templates" / "scoring" / "AssetScoringWeights.jsonc"
OUTPUT_DIR = ROOT / "output"
OUTPUT_DIR.mkdir(exist_ok=True)
CSV_FILE = OUTPUT_DIR / "asset_scores.csv"
MD_FILE = OUTPUT_DIR / "asset_scores.md"

LANGUAGE_FIELDS = ["VF", "LD", "TTC", "LTV", "CR", "CC", "EC", "NL"]


def strip_jsonc(path: Path):
    text = path.read_text(encoding="utf-8")
    cleaned = re.sub(r"//.*", "", text)
    return json.loads(cleaned)


def load_assets(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def score_asset(asset, weights, gates, thresholds):
    codes = asset.get("codes", {})
    weight_sum = sum(weights.values())
    raw_total = 0.0
    contributions = {}
    for k, w in weights.items():
        v = codes.get(k, 0)
        part = (v / 5.0) * w
        contributions[k] = part * (100.0 / weight_sum)
        raw_total += (v / 5.0) * w
    composite = raw_total * (100.0 / weight_sum)

    vf = codes.get("VF", 0)
    cc = codes.get("CC", 0)
    gating_notes = []
    if vf < gates["min_vf_for_near_term"] or cc < gates["min_cc_for_near_term"]:
        composite_before = composite
        composite = min(composite, thresholds["background"] - 1)
        gating_notes.append(
            f"Gated below Near-Term (VF={vf}, CC={cc}, " f"was {composite_before:.2f})"
        )

    if asset.get("gates", {}).get("compliance_risk"):
        if composite > gates["compliance_cap"]:
            composite_before = composite
            composite = gates["compliance_cap"]
            gating_notes.append(f"Compliance cap applied (was {composite_before:.2f})")

    verification_days = asset.get("gates", {}).get("verification_days", 0)
    if verification_days > gates["verification_penalty_days"]:
        composite_before = composite
        composite -= gates["verification_penalty_points"]
        gating_notes.append(
            f"Verification delay penalty "
            f"-{gates['verification_penalty_points']} "
            f"(days={verification_days}, was {composite_before:.2f})"
        )

    composite = max(composite, 0)

    # Reject rules
    ttc = codes.get("TTC", 0)
    ld = codes.get("LD", 0)
    ltv = codes.get("LTV", 0)
    if (ttc == 0) or (vf <= 1) or (cc <= 1) or (ld <= 1 and ltv <= 1):
        bucket = "Reject"
        composite_before = composite
        composite = min(composite, 5.0)
        gating_notes.append(
            f"REJECT: Unviable for near-term liquidity "
            f"(TTC={ttc}, VF={vf}, CC={cc}, LD={ld}, LTV={ltv}; "
            f"was {composite_before:.2f})"
        )
    else:
        if composite >= thresholds["immediate"]:
            bucket = "Immediate"
        elif composite >= thresholds["near_term"]:
            bucket = "Near-Term"
        elif composite >= thresholds["background"]:
            bucket = "Background"
        else:
            bucket = "Archive"

    return round(composite, 2), bucket, contributions, gating_notes


def compute_scores(assets, weights_doc):
    weights = weights_doc["weights"]
    gates = weights_doc["gates"]
    thresholds = weights_doc["thresholds"]
    scored = []
    for a in assets:
        composite, bucket, contributions, gating_notes = score_asset(
            a, weights, gates, thresholds
        )
        row = {
            "name": a.get("name", "UNKNOWN"),
            "composite": composite,
            "bucket": bucket,
            "contributions": contributions,
            "gating_notes": gating_notes,
        }
        row.update(a.get("codes", {}))
        scored.append(row)
    scored.sort(key=lambda x: x["composite"], reverse=True)
    return scored


def write_outputs(scored, csv_path: Path, md_path: Path, print_stdout: bool = True):
    header = ["Asset", "Score", "Bucket"] + LANGUAGE_FIELDS

    def fmt(row):
        return [row["name"], f"{row['composite']:.2f}", row["bucket"]] + [
            str(row.get(c, 0)) for c in LANGUAGE_FIELDS
        ]

    if print_stdout:
        print("\nLiquidity Priority Ranking:\n")
        print("| " + " | ".join(header) + " |")
        print("|" + "|".join(["-" * (len(h) + 2) for h in header]) + "|")
        for r in scored:
            print("| " + " | ".join(fmt(r)) + " |")

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        for r in scored:
            w.writerow(fmt(r))

    bucket_actions = {
        "Immediate": (
            "Commit execution resources now (legal finalize, "
            "commercialization, compliance monitoring). Allocate ~40% bandwidth."
        ),
        "Near-Term": (
            "Advance verification & packaging (data room, appraisals, "
            "counterparties). Target readiness within next sprint."
        ),
        "Background": (
            "Maintain light progress & monitoring. "
            "Improve documentation opportunistically."
        ),
        "Archive": (
            "Park with no active spend. "
            "Revisit only if new verifiable evidence appears."
        ),
        "Reject": (
            "Hard pass. Do not spend time or money until evidence "
            "dramatically improves (verification, compliance, liquidity, "
            "or time-to-cash)."
        ),
    }

    with md_path.open("w", encoding="utf-8") as md:
        md.write("# Asset Liquidity Scores\n\n")
        md.write(
            "Composite scores after gating & penalties. "
            "Higher = faster + more efficient path to near-term cash.\n\n"
        )
        md.write("| " + " | ".join(header) + " |\n")
        md.write("| " + " | ".join(["---"] * len(header)) + " |\n")
        for r in scored:
            md.write("| " + " | ".join(fmt(r)) + " |\n")
        md.write("\n## Detail Breakdown\n")
        for r in scored:
            md.write(f"\n### {r['name']} ({r['bucket']}, {r['composite']:.2f})\n")
            md.write(f"Action: {bucket_actions[r['bucket']]}\n\n")
            md.write("Contributions (% of composite):\n")
            for k, v in r["contributions"].items():
                md.write(f"- {k}: {v:.2f}\n")
            if r["gating_notes"]:
                md.write("Gating / Penalties:\n")
                for note in r["gating_notes"]:
                    md.write(f"  - {note}\n")
        md.write("\n---\nGenerated by asset_scoring.py\n")


def generate_focus_md(
    scored, path: Path, top_immediate: int = 3, top_nearterm: int = 3
):
    immediate = [r for r in scored if r["bucket"] == "Immediate"][:top_immediate]
    nearterm = [r for r in scored if r["bucket"] == "Near-Term"][:top_nearterm]

    def why_lines(r):
        return [
            f"- TTC: {r.get('TTC', 0)}",
            f"- LTV: {r.get('LTV', 0)}",
            f"- LD: {r.get('LD', 0)}",
            f"- CC: {r.get('CC', 0)}",
        ]

    with path.open("w", encoding="utf-8") as md:
        md.write("# Liquidity Focus (Current)\n\n")
        md.write("Auto-generated from the latest scoring run.\n\n")
        md.write("## Immediate (Top)\n\n")
        if not immediate:
            md.write("- None\n")
        for idx, r in enumerate(immediate, 1):
            md.write(f"{idx}) {r['name']} — {r['composite']:.2f}\n")
            for line in why_lines(r):
                md.write(line + "\n")
            md.write("Next 7 days: _________________________________\n\n")

        md.write("## Near-Term (Next Sprint)\n\n")
        if not nearterm:
            md.write("- None\n")
        for r in nearterm:
            md.write(
                f"- {r['name']} — {r['composite']:.2f} | "
                "Unlocks: appraisal/counterparties/docs\n"
            )

        md.write("\n## Reject Log (Dogshit)\n\n")
        rejects = [r for r in scored if r["bucket"] == "Reject"]
        if not rejects:
            md.write("- None\n")
        for r in rejects:
            reasons = "; ".join(r.get("gating_notes", [])) or "No reasons recorded"
            md.write(f"- {r['name']} — {r['composite']:.2f} | {reasons}\n")


def parse_args():
    p = argparse.ArgumentParser(description="Asset Liquidity Scoring")
    p.add_argument(
        "--weights", type=str, default=str(WEIGHTS_FILE), help="Path to weights JSONC"
    )
    p.add_argument(
        "--assets", type=str, default=str(DATA_FILE), help="Path to assets JSON"
    )
    p.add_argument("--csv", type=str, default=str(CSV_FILE), help="Path to CSV output")
    p.add_argument(
        "--md", type=str, default=str(MD_FILE), help="Path to Markdown output"
    )
    p.add_argument(
        "--focus-md",
        type=str,
        default=str(OUTPUT_DIR / "Focus.current.md"),
        help="Path to Focus summary Markdown output",
    )
    p.add_argument(
        "--no-stdout", action="store_true", help="Do not print table to stdout"
    )
    p.add_argument("--no-md", action="store_true", help="Skip Markdown report output")
    p.add_argument("--no-csv", action="store_true", help="Skip CSV output")
    p.add_argument(
        "--print-focus",
        action="store_true",
        help="Print Immediate/Near-Term summary to stdout",
    )
    return p.parse_args()


def main():
    args = parse_args()
    weights_doc = strip_jsonc(Path(args.weights))
    assets = load_assets(Path(args.assets))
    scored = compute_scores(assets, weights_doc)

    write_outputs(
        scored, Path(args.csv), Path(args.md), print_stdout=(not args.no_stdout)
    )

    if args.no_md:
        try:
            Path(args.md).unlink(missing_ok=True)
        except Exception:
            pass
    if args.no_csv:
        try:
            Path(args.csv).unlink(missing_ok=True)
        except Exception:
            pass

    focus_path = Path(args.focus_md)
    generate_focus_md(scored, focus_path)
    if args.print_focus:
        print(f"\nFocus summary written to {focus_path}")
        print(focus_path.read_text(encoding="utf-8"))

    print(f"\nWrote scores to {Path(args.csv)} and {Path(args.md)}")


if __name__ == "__main__":
    main()
