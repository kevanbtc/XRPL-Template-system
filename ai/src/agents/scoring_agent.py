from typing import Optional, Dict, Any
from tools.scoring_reader import read_scores, top_assets, BUCKET_ORDER
from config import Config
from swarm import Agent, Message


class ScoringAgent(Agent):
    name = "scoring"

    def __init__(self, cfg: Config) -> None:
        self.cfg = cfg

    def step(self, state: Dict[str, Any]) -> Optional[Message]:
        if state.get("scoring_loaded"):
            return None
        rows = read_scores(self.cfg.output_scores_csv)
        # Determine min_bucket that includes all allowed buckets (e.g., Immediate + Near-Term -> min_bucket Near-Term)
        allowed = set(self.cfg.allowed_buckets)
        order = [b for b in BUCKET_ORDER if b in allowed]
        min_bucket = order[-1] if order else self.cfg.min_bucket
        focus = top_assets(rows, min_bucket=min_bucket, limit=self.cfg.top_n)
        state["scoring_loaded"] = True
        state["focus_assets"] = focus
        return Message(self.name, {"focus_assets_count": len(focus)})
