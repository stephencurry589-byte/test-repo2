# CLI rollup

The CLI runs the ingest stub and prints a JSON rollup (firms, demo events, trends, equity hypotheses, disclaimer) to stdout.

## Sub-features

- `cli-json` emits parseable JSON on stdout.
- `cli-disclaimer` includes DEMO/PLACEHOLDER / not-trade-advice text.
- `cli-trends` includes `trends.event_count >= 1` and sector/stage keys.

## How to get to it (user POV)

- Run `python3 -m src.cli` from repo root.

## Driving it with verify.sh / shell

Preconditions:

- Doctor passed.
- Seed file readable.

- **Run CLI.** `python3 -m src.cli`. Exit `0`; stdout is JSON.
- **Assert shape.** Parsed object has `disclaimer`, `trends`, `events`, `equity_hypotheses`, `seed_firm_count`.
- **DEMO guard.** `disclaimer` (case-insensitive) mentions DEMO or PLACEHOLDER; every event has `"demo": true`.
- **Proof.** Save full stdout under the VERIFY-RUN artifact with exit code.

## Gotchas

- CLI writes only to stdout — do not expect a results file on disk.
- Amounts like `DEMO_USD_50M` are placeholders, not numeric facts.
