import sys
from pathlib import Path
from pprint import pprint
import csv


def _ensure_path_on_sys_path() -> None:
    here = Path(__file__).resolve()
    src = here.parent / "src"
    if str(src) not in sys.path:
        sys.path.insert(0, str(src))


_ensure_path_on_sys_path()

from config import Config  # noqa: E402
from swarm import Orchestrator  # noqa: E402
from agents.scoring_agent import ScoringAgent  # noqa: E402
from agents.market_agent import MarketAgent  # noqa: E402
from agents.risk_agent import RiskAgent  # noqa: E402
from agents.trader_agent import TraderAgent  # noqa: E402


def _maybe_seed_csv(cfg: Config) -> None:
    cfg.output_dir.mkdir(parents=True, exist_ok=True)
    if cfg.output_scores_csv.exists():
        return
    rows = [
        {"Asset": "ASSET_A", "Score": 82, "Bucket": "Immediate", "Notes": "High demand"},
        {"Asset": "ASSET_B", "Score": 74, "Bucket": "Near-Term", "Notes": "Growing volume"},
        {"Asset": "ASSET_C", "Score": 58, "Bucket": "Medium", "Notes": "Moderate"},
        {"Asset": "DOGSHIT", "Score": 12, "Bucket": "Reject", "Notes": "Hard reject"},
        {"Asset": "ASSET_D", "Score": 91, "Bucket": "Immediate", "Notes": "Low TTC"},
    ]
    with cfg.output_scores_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Asset", "Score", "Bucket", "Notes"])
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    cfg = Config.from_env()
    _maybe_seed_csv(cfg)

    # Swarm rounds from policy if provided
    max_rounds = int(getattr(cfg, "swarm", {}).get("max_rounds", 8)) if getattr(cfg, "swarm", None) else 8
    ork = Orchestrator(
        agents=[
            ScoringAgent(cfg),
            MarketAgent(cfg),
            RiskAgent(cfg),
            TraderAgent(cfg),
        ]
    )

    state = ork.run(state={}, max_rounds=max_rounds)

    # Human-friendly summary
    print("\nSwarm run complete")
    print("Rounds:", state.get("rounds"))
    print("Messages:")
    for m in state.get("log", []):
        print(f" - {m.sender}: {m.payload}")

    focus = state.get("focus_assets", [])
    print(f"\nFocus assets ({len(focus)}):")
    for r in focus:
        if hasattr(r, "asset"):
            asset, score, bucket = r.asset, r.score, r.bucket
        else:
            asset = r.get("asset") or r.get("Asset")
            score = r.get("score") or r.get("Score")
            bucket = r.get("bucket") or r.get("Bucket")
        print(f"  - {asset} | score={score} | bucket={bucket}")

    opps = state.get("market_opps", [])
    print(f"\nMarket opportunities ({len(opps)}):")
    for o in opps:
        print(
            f"  - {o['asset']} {o['direction']} | net_bps={o['net_bps']} | est_profit($1k)={o['est_profit_1000']}"
        )

    approved = state.get("approved_opps", [])
    print(f"\nApproved opportunities ({len(approved)}):")
    for o in approved:
        print(f"  - {o['asset']} {o['direction']} | net_bps={o['net_bps']}")

    plan = state.get("trade_plan", [])
    print(f"\nDry-run trade plan ({len(plan)}):")
    for t in plan:
        print(
            f"  - {t['asset']} {t['direction']} | size=${t['size_usd']} | exp_profit=${t['expected_profit_usd']}"
        )

    # Persist forensic run log
    try:
        from datetime import datetime
        import json

        base_dir = Path(__file__).resolve().parent
        runs_dir = base_dir.parent / "output" / "ai_runs"
        runs_dir.mkdir(parents=True, exist_ok=True)

        def _to_plain(obj):
            # Convert dataclasses or Messages to dicts
            if hasattr(obj, "__dict__"):
                return {k: _to_plain(v) for k, v in obj.__dict__.items()}
            if isinstance(obj, (list, tuple)):
                return [_to_plain(x) for x in obj]
            if isinstance(obj, dict):
                return {k: _to_plain(v) for k, v in obj.items()}
            return obj

        messages = []
        for m in state.get("log", []):
            # m is our Message dataclass
            messages.append({"sender": getattr(m, "sender", "unknown"), "payload": getattr(m, "payload", {})})

        focus_serialized = []
        for r in focus:
            if hasattr(r, "asset"):
                focus_serialized.append({"asset": r.asset, "score": r.score, "bucket": r.bucket, "notes": getattr(r, "notes", "")})
            else:
                focus_serialized.append({
                    "asset": r.get("asset") or r.get("Asset"),
                    "score": r.get("score") or r.get("Score"),
                    "bucket": r.get("bucket") or r.get("Bucket"),
                    "notes": r.get("notes") or r.get("Notes", ""),
                })

        run_record = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "policy": {
                "risk": getattr(cfg, "risk", {}),
                "liquidity": getattr(cfg, "liquidity", {}),
                "swarm": getattr(cfg, "swarm", {}),
            },
            "inputs": {
                "scores_csv": str(cfg.output_scores_csv),
                "focus_assets": focus_serialized,
            },
            "messages": messages,
            "approved": state.get("approved_opps", []),
            "trades": plan,
        }
        out_name = f"ai_run_{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}.json"
        with (runs_dir / out_name).open("w", encoding="utf-8") as f:
            json.dump(run_record, f, indent=2)
        print(f"\nWrote run log: {runs_dir / out_name}")
    except Exception as e:  # pragma: no cover
        print(f"[ai][runlog] Warning: could not write run log: {e}")


if __name__ == "__main__":
    main()
