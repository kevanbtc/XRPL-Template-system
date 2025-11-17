from typing import Optional, Dict, Any, List

from config import Config
from swarm import Agent, Message


class RiskAgent(Agent):
    name = "risk"

    def __init__(self, cfg: Config) -> None:
        self.cfg = cfg

    def step(self, state: Dict[str, Any]) -> Optional[Message]:
        if state.get("risk_screened"):
            return None
        opps: List[Dict[str, Any]] = state.get("market_opps", [])
        approved: List[Dict[str, Any]] = []
        allowed_buckets = set(
            getattr(self.cfg, "allowed_buckets", ("Immediate", "Near-Term"))
        )
        for o in opps:
            bucket = o.get("bucket", "")
            score = float(o.get("score", 0.0))
            net_bps = float(o.get("net_bps", 0.0))
            if bucket == "Reject" or bucket not in allowed_buckets:
                continue
            if score < self.cfg.min_score:
                continue
            if net_bps < getattr(self.cfg, "min_net_bps", 0.0):
                continue
            approved.append(o)
        state["risk_screened"] = True
        state["approved_opps"] = approved
        return Message(
            self.name, {"approved": len(approved), "approved_opps": approved}
        )
