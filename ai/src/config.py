from dataclasses import dataclass
from pathlib import Path
import os
from typing import Any, Dict

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover
    yaml = None  # graceful fallback


@dataclass
class Config:
    # Paths (ai/src -> parent is ai, parent of that is repo root if mirrored)
    root: Path = Path(__file__).resolve().parents[1]
    output_dir: Path = root.parent / "output"
    output_scores_csv: Path = output_dir / "asset_scores.csv"

    # Defaults (overridden by policy if present)
    # Scoring / selection thresholds
    min_bucket: str = "Near-Term"  # Immediate, Near-Term, Medium, Long-Term, Reject
    top_n: int = 5

    # Market simulation defaults (fees used by MarketAgent)
    venue_a_fee_bps: float = 0.5
    venue_b_fee_bps: float = 0.5
    max_slippage_bps: float = 1.0

    # Risk defaults
    min_score: float = 60.0
    max_position_usd: float = 10_000.0
    max_portfolio_usd: float = 50_000.0
    max_trades: int = 5
    allowed_buckets: tuple = ("Immediate", "Near-Term")
    min_net_bps: float = 5.0

    # Trader
    dry_run: bool = True

    # Policy dicts (loaded from YAML)
    risk: Dict[str, Any] = None  # type: ignore
    liquidity: Dict[str, Any] = None  # type: ignore
    swarm: Dict[str, Any] = None  # type: ignore

    @staticmethod
    def from_env() -> "Config":
        cfg = Config(dry_run=os.getenv("AI_DRY_RUN", "true").lower() != "false")
        cfg.load_policy()
        return cfg

    def load_policy(self) -> None:
        policy_path = self.root.parent / "config" / "ai_policy.yaml"
        if not policy_path.exists():
            return
        if yaml is None:  # pragma: no cover
            print("[ai][policy] Warning: PyYAML not installed; using defaults")
            return
        with policy_path.open("r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        self.risk = data.get("risk", {})
        self.liquidity = data.get("liquidity", {})
        self.swarm = data.get("swarm", {})

        # Map policy into config fields for convenience
        self.min_score = float(self.risk.get("min_score", self.min_score))
        self.min_net_bps = float(self.risk.get("min_net_bps", self.min_net_bps))
        self.max_position_usd = float(self.risk.get("max_position_usd", self.max_position_usd))
        self.max_portfolio_usd = float(self.risk.get("max_portfolio_usd", self.max_portfolio_usd))
        self.max_trades = int(self.risk.get("max_trades", self.max_trades))
        self.allowed_buckets = tuple(self.risk.get("allowed_buckets", list(self.allowed_buckets)))

        # Swarm behavior
        self.dry_run = bool(self.swarm.get("dry_run", self.dry_run))
