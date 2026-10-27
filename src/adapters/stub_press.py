"""Stub public-source press adapter — returns DEMO-tagged fake events only."""

from __future__ import annotations

from typing import List

from src.adapters.base import BaseAdapter
from src.schema import DealEvent


class StubPressAdapter(BaseAdapter):
    name = "stub_press"

    def fetch_events(self) -> List[DealEvent]:
        # Clearly fake / demo — do not invent real deals as fact.
        return [
            DealEvent(
                event_id="demo-stub-001",
                firm_name="Example Capital Alpha (PLACEHOLDER)",
                company_name="DemoCo AI Infra (DEMO)",
                sector="ai_infra",
                stage="series_b",
                announced_date="2026-10-01",
                source_url="https://example.com/demo/press/stub-001",
                amount_usd_public="DEMO_USD_50M",
                geo="US",
                is_follow_on=False,
                demo=True,
                notes="DEMO stub event from StubPressAdapter — not a real deal",
            ),
            DealEvent(
                event_id="demo-stub-002",
                firm_name="Example Growth Delta (PLACEHOLDER)",
                company_name="DemoClimate Grid (DEMO)",
                sector="climate",
                stage="growth",
                announced_date="2026-10-15",
                source_url="https://example.com/demo/press/stub-002",
                amount_usd_public="DEMO_USD_120M",
                geo="EU",
                is_follow_on=True,
                demo=True,
                notes="DEMO stub event from StubPressAdapter — not a real deal",
            ),
        ]
