from typing import Any, Dict, List, Optional

from swarm import Agent, Message

from config import Config


class TraderAgent(Agent):
    name = "trader"

    def __init__(self, cfg: Config) -> None:
        self.cfg = cfg

    def step(self, state: Dict[str, Any]) -> Optional[Message]:
        if state.get("trade_planned"):
            return None
        approved: List[Dict[str, Any]] = state.get("approved_opps", [])
        remaining = float(self.cfg.max_portfolio_usd)
        max_trades = int(getattr(self.cfg, "max_trades", 5))
        plan: List[Dict[str, Any]] = []
        seen_assets = set()
        for o in approved:
            if remaining <= 0 or len(plan) >= max_trades:
                break
            asset = o.get("asset")
            if not asset or asset in seen_assets:
                continue
            size = min(float(self.cfg.max_position_usd), remaining)
            remaining -= size
            seen_assets.add(asset)
            plan.append(
                {
                    "asset": asset,
                    "direction": o["direction"],
                    "size_usd": round(size, 2),
                    "expected_net_bps": o["net_bps"],
                    "expected_profit_usd": round(size * o["net_bps"] / 10_000.0, 2),
                    "notes": f"Dry-run: {o['direction']} exploiting ~{o['net_bps']}bps after fees",
                }
            )
        state["trade_planned"] = True
        state["trade_plan"] = plan
        return Message(
            self.name,
            {
                "trades": len(plan),
                "allocated_usd": self.cfg.max_portfolio_usd - remaining,
            },
        )
