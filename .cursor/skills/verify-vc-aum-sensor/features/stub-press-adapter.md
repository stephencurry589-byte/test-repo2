# Stub press adapter

`StubPressAdapter` returns 1–2 DEMO deal events for rollups — not live press scrape.

## Sub-features

- `adapter-fetch` returns ≥1 and ≤2 events.
- `adapter-demo` every event marked `demo=True` with DEMO in name/notes.
- `adapter-rollup` trends count matches event list.

## How to get to it (user POV)

- Indirect via CLI ingest; adapter lives under `src/adapters/stub_press.py`.

## Driving it with verify.sh / shell

Preconditions:

- Doctor passed.

- **Via smoke.** `test_stub_adapter_returns_demo_events` and `test_rollup` pass.
- **Via CLI.** JSON `events` length 1–2; each `"demo": true`; `trends.event_count` equals that length.
- **Proof.** Include event_ids from CLI stdout in the artifact.

## Gotchas

- Replacing the stub with a live adapter is a product change — update this map and re-prove; do not fake DEMO flags.
