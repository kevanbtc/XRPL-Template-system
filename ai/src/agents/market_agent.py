from typing import Any, Dict, List, Optional

from swarm import Agent, Message

from config import Config


class MarketAgent(Agent):
    name = "market"

    def __init__(self, cfg: Config) -> None:
        self.cfg = cfg

    @staticmethod
    def _pseudo_price(asset: str, venue: str) -> float:
        # Simple deterministic pseudo-price based on asset+venue
        h = sum(ord(c) for c in (asset + "@" + venue)) % 1000
        base = 1.0 + (h / 1000.0)  # 1.000 .. 1.999
        return round(base, 4)

    def step(self, state: Dict[str, Any]) -> Optional[Message]:
        if state.get("market_loaded"):
            return None
        focus = state.get("focus_assets", [])
        opps: List[Dict[str, Any]] = []
        for r in focus:
            # Support both dataclass ScoreRow and plain dict
            if hasattr(r, "asset"):
                asset = r.asset
                score = getattr(r, "score", 0.0)
                bucket = getattr(r, "bucket", "")
            else:
                asset = r.get("asset") or r.get("Asset") or "UNKNOWN"
                score = r.get("score") or float(r.get("Score", 0.0))
                bucket = r.get("bucket") or r.get("Bucket") or ""

            pa = self._pseudo_price(asset, "VenueA")
            pb = self._pseudo_price(asset, "VenueB")
            cheaper, expensive = (pa, pb) if pa < pb else (pb, pa)
            direction = "buy@A->sell@B" if pa < pb else "buy@B->sell@A"
            spread_bps = (expensive - cheaper) / cheaper * 10_000
            fees_bps = self.cfg.venue_a_fee_bps + self.cfg.venue_b_fee_bps
            net_bps = spread_bps - fees_bps
            if net_bps > 0:
                est_profit_1000 = net_bps / 10_000 * 1_000.0
                opps.append(
                    {
                        "asset": asset,
                        "score": score,
                        "bucket": bucket,
                        "price_a": pa,
                        "price_b": pb,
                        "direction": direction,
                        "spread_bps": round(spread_bps, 2),
                        "net_bps": round(net_bps, 2),
                        "est_profit_1000": round(est_profit_1000, 2),
                    }
                )
        state["market_loaded"] = True
        state["market_opps"] = opps
        return Message(self.name, {"opportunities": len(opps)})
