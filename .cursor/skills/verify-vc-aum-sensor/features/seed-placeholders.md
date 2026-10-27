# Seed placeholders

Editable firm stubs in `data/top50_seed.json` load as placeholder Firms (≤15).

## Sub-features

- `seed-load` reads JSON and builds Firm objects.
- `seed-cap` enforces ≤15 firms.
- `seed-flag` every firm has `placeholder=True`.

## How to get to it (user POV)

- Indirect: CLI and smoke load the seed; edit `data/top50_seed.json` to change stubs.

## Driving it with verify.sh / shell

Preconditions:

- Doctor passed; seed file exists.

- **Via smoke.** `python3 tests/test_smoke.py` — `test_seed_placeholders` passes.
- **Via CLI field.** `python3 -m src.cli` JSON has `seed_all_placeholder: true` and `seed_firm_count` in 1..15.
- **Proof.** Record `seed_firm_count` and `seed_all_placeholder` from CLI stdout.

## Gotchas

- Seed AUM strings are PLACEHOLDER — never promote to fact in proofs.
- Adding a firm with `placeholder: false` should fail smoke until intentional product change + map update.
