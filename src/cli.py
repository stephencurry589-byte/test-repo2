"""Run ingest stub → print rollup JSON to stdout."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from src.adapters.stub_press import StubPressAdapter
from src.equity_stub import hypotheses_as_dicts
from src.schema import Firm
from src.trends import rollup


def load_seed(path: Path | None = None) -> list[Firm]:
    seed_path = path or Path(__file__).resolve().parent.parent / "data" / "top50_seed.json"
    raw = json.loads(seed_path.read_text(encoding="utf-8"))
    firms = []
    for row in raw.get("firms", []):
        firms.append(
            Firm(
                name=row["name"],
                aum_public=row["aum_public"],
                strategy=row["strategy"],
                source_url=row["source_url"],
                placeholder=bool(row.get("placeholder", True)),
            )
        )
    return firms


def run() -> dict:
    firms = load_seed()
    events = StubPressAdapter().fetch_events()
    trends = rollup(events)
    payload = {
        "seed_firm_count": len(firms),
        "seed_all_placeholder": all(f.placeholder for f in firms),
        "events": [e.to_dict() for e in events],
        "trends": trends,
        "equity_hypotheses": hypotheses_as_dicts(),
        "disclaimer": "Public sources only; DEMO/PLACEHOLDER data; not trade advice",
    }
    return payload


def main() -> None:
    payload = run()
    json.dump(payload, sys.stdout, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
