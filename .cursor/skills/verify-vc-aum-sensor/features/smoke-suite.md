# Smoke suite

The smoke suite proves schema, stub adapter, rollup, seed, equity stub, and CLI JSON serialization via six stdlib unittest cases.

## Sub-features

- `smoke-run` executes all six tests and exits 0.
- `smoke-count` reports exactly six tests ran.
- `smoke-ok` prints unittest `OK` with no failures/errors.

## How to get to it (user POV)

- From repo root run `python3 tests/test_smoke.py`.
- Optionally `python3 -m pytest` if pytest is installed (not required).

## Driving it with verify.sh / shell

Preconditions:

- Doctor passed.
- `tests/test_smoke.py` present.

- **Full suite.** Run `python3 tests/test_smoke.py`. Exit code `0`; stdout contains `Ran 6 tests` and `OK`.
- **Via helper.** Run `.cursor/skills/verify-vc-aum-sensor/scripts/verify.sh run`. Smoke section marked PASS.
- **Proof.** Keep the unittest transcript (command + exit + stdout) in the VERIFY-RUN artifact.

## Gotchas

- Running from a non-repo cwd breaks `sys.path` inserts; always start at repo root.
- `__pycache__` stale bytecode is rare; doctor re-imports fresh modules.
- Do not weaken assertions to force green — report product gaps separately.
