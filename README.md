# VC AUM Sensor (SW-03)

Public-source sensor for Top-50 VC AUM / growth-capital deal activity, sector-stage trends, and equity theme hypotheses — not trade advice.

## How to run locally

```bash
cd /workspace/vc-aum-sensor
python3 -m src.cli          # ingest stub → print rollup JSON
python3 tests/test_smoke.py # smoke (stdlib unittest; pytest also ok)
```

Optional: `python3 -m pytest` if pytest is installed. No third-party deps required (stdlib only).

## Public-sources-only rule

Adapters may read **published / public** press, firm sites, public filings, and reputable databases with allowed access. **No paywall bypass. No ToS-breaking scrape. No private LP docs / leaked decks.** Seed AUM figures and stub events are **PLACEHOLDER / DEMO** — never treat as fact.

## Non-goals (MVP)

- Private or non-public data
- Auto-trading or brokerage execution
- Full CID equity desk replacement (this sensor feeds that desk later)
- Inventing real deal data as fact

## Layout

- `data/top50_seed.json` — editable firm stubs (≤15 placeholders)
- `src/schema.py` — Firm + DealEvent dataclasses
- `src/adapters/` — public-source adapters (`stub_press` is demo)
- `src/trends.py` — sector/stage rollups
- `src/equity_stub.py` — theme → ticker hypotheses (stub)
- `src/cli.py` — run ingest stub → JSON stdout
