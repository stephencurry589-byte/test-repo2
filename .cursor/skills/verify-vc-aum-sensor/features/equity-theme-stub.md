# Equity theme stub

Theme → ticker hypotheses are DEMO stubs with evidence URLs and disclaimers — not trade advice.

## Sub-features

- `equity-demo` all hypotheses have `demo=True`.
- `equity-evidence` each hypothesis has non-empty `evidence_urls`.
- `equity-in-cli` CLI payload includes `equity_hypotheses`.

## How to get to it (user POV)

- Appears in `python3 -m src.cli` JSON under `equity_hypotheses`.

## Driving it with verify.sh / shell

Preconditions:

- Doctor passed.

- **Via smoke.** `test_equity_stub_demo` passes.
- **Via CLI.** Every hypothesis object has `"demo": true` and a non-empty `evidence_urls` list.
- **Proof.** Record theme names and demo flags from CLI stdout.

## Gotchas

- Tickers like `DEMO_TICKER_AI1` are stubs; proofs must not claim investability.
