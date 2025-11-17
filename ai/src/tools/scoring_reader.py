from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List

BUCKET_ORDER = ["Immediate", "Near-Term", "Medium", "Long-Term", "Reject"]


@dataclass
class ScoreRow:
    asset: str
    score: float
    bucket: str
    notes: str = ""


def _bucket_rank(bucket: str) -> int:
    try:
        return BUCKET_ORDER.index(bucket)
    except ValueError:
        return len(BUCKET_ORDER)


def read_scores(csv_path: Path) -> List[ScoreRow]:
    """Read scores from a CSV at csv_path and return a list of ScoreRow.

    Expected columns (case-insensitive): Asset, Score, Bucket, Notes
    """
    rows: List[ScoreRow] = []
    if not csv_path.exists():
        return rows

    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            asset = r.get("Asset") or r.get("asset") or r.get("name") or "Unknown"
            score_str = r.get("Score") or r.get("score") or "0"
            bucket = r.get("Bucket") or r.get("bucket") or "Reject"
            notes = r.get("Notes") or r.get("notes") or ""
            try:
                score = float(score_str)
            except Exception:
                score = 0.0
            rows.append(ScoreRow(asset=asset, score=score, bucket=bucket, notes=notes))

    return rows


def filter_by_bucket(rows: Iterable[ScoreRow], min_bucket: str) -> List[ScoreRow]:
    """Return rows whose bucket rank is <= min_bucket rank (better or equal).

    Example: min_bucket='Near-Term' will include 'Immediate' and 'Near-Term'.
    """
    min_rank = _bucket_rank(min_bucket)
    return [r for r in rows if _bucket_rank(r.bucket) <= min_rank]


def top_assets(
    rows: Iterable[ScoreRow], min_bucket: str = "Near-Term", limit: int = 5
) -> List[ScoreRow]:
    """Return the top assets filtered by bucket and sorted by bucket rank,
    score desc, asset name.
    """
    filtered = filter_by_bucket(list(rows), min_bucket)
    sorted_rows = sorted(
        filtered,
        key=lambda r: (_bucket_rank(r.bucket), -r.score, r.asset.lower()),
    )
    return sorted_rows[:limit]
