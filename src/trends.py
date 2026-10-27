"""Simple sector / stage rollups over DealEvent lists."""

from __future__ import annotations

from collections import Counter
from typing import Any, Iterable, List

from src.schema import DealEvent


def rollup(events: Iterable[DealEvent]) -> dict[str, Any]:
    events_list: List[DealEvent] = list(events)
    by_sector = Counter(e.sector for e in events_list)
    by_stage = Counter(e.stage for e in events_list)
    demo_count = sum(1 for e in events_list if e.demo)
    return {
        "event_count": len(events_list),
        "demo_event_count": demo_count,
        "by_sector": dict(sorted(by_sector.items())),
        "by_stage": dict(sorted(by_stage.items())),
        "label": "DEMO/PLACEHOLDER rollup — not live market data",
    }
