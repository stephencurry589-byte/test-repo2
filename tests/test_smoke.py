"""Smoke: schema + stub adapter + rollup run. Stdlib unittest; also pytest-compatible."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.adapters.stub_press import StubPressAdapter
from src.cli import load_seed, run
from src.equity_stub import theme_hypotheses
from src.schema import DealEvent, Firm
from src.trends import rollup


class SmokeTest(unittest.TestCase):
    def test_schema_firm_and_event(self):
        f = Firm(
            name="X (PLACEHOLDER)",
            aum_public="PLACEHOLDER",
            strategy="growth",
            source_url="https://example.com/x",
            placeholder=True,
        )
        e = DealEvent(
            event_id="demo-1",
            firm_name=f.name,
            company_name="DemoCo (DEMO)",
            sector="ai_infra",
            stage="series_a",
            announced_date="2026-10-01",
            source_url="https://example.com/demo",
            demo=True,
        )
        self.assertTrue(f.placeholder)
        self.assertTrue(e.demo)
        self.assertIn("name", f.to_dict())
        self.assertIn("event_id", e.to_dict())

    def test_stub_adapter_returns_demo_events(self):
        events = StubPressAdapter().fetch_events()
        self.assertGreaterEqual(len(events), 1)
        self.assertLessEqual(len(events), 2)
        for ev in events:
            self.assertTrue(ev.demo)
            self.assertIn("DEMO", ev.notes.upper() + ev.company_name.upper())

    def test_rollup(self):
        events = StubPressAdapter().fetch_events()
        r = rollup(events)
        self.assertEqual(r["event_count"], len(events))
        self.assertIn("by_sector", r)
        self.assertIn("by_stage", r)
        self.assertTrue(r["demo_event_count"] >= 1)

    def test_seed_placeholders(self):
        firms = load_seed()
        self.assertLessEqual(len(firms), 15)
        self.assertGreaterEqual(len(firms), 1)
        self.assertTrue(all(f.placeholder for f in firms))

    def test_equity_stub_demo(self):
        hyps = theme_hypotheses()
        self.assertTrue(all(h.demo for h in hyps))
        self.assertTrue(all(h.evidence_urls for h in hyps))

    def test_cli_run_json_serializable(self):
        payload = run()
        text = json.dumps(payload)
        self.assertIn("DEMO", text.upper() + payload["disclaimer"].upper())
        self.assertGreaterEqual(payload["trends"]["event_count"], 1)


if __name__ == "__main__":
    unittest.main()
