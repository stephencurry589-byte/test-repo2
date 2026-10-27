# VC AUM sensor verification map

Maintained source for verifying user-facing behavior of the VC AUM sensor CLI scaffold. Read this index before driving, then use the matching feature file.

## Baseline preconditions

- Work from the git repo root (contains `src/cli.py`, `tests/test_smoke.py`, `data/top50_seed.json`).
- Python 3.10+ with stdlib only (no third-party install required).
- Run `.cursor/skills/verify-vc-aum-sensor/scripts/verify.sh doctor` and require exit 0.
- Seed and adapters are DEMO/PLACEHOLDER; never assert live AUM or real deals.
- Never treat a skipped entry point as verified via a different path.

## Driving conventions

- Start every recipe from a clean doctor pass.
- Commands are literal; keep flags and module paths unchanged.
- Prefer exit code + structured stdout (JSON / unittest summary) over screenshots.
- Capture command, exit code, and stdout for every drive; keep proof files out of cleanup.

## Proof and skip reporting

- CLI proof: command, stdout, stderr, exit code.
- Smoke proof: unittest summary with `Ran N tests` and `OK`.
- Record feature ID with every artifact.
- Unreachable path → report attempted command and unmet precondition.

## Features

- [Smoke suite](./smoke-suite.md) — six stdlib unittest checks.
- [CLI rollup](./cli-rollup.md) — ingest stub → JSON stdout.
- [Seed placeholders](./seed-placeholders.md) — DEMO firm seed load.
- [Stub press adapter](./stub-press-adapter.md) — demo deal events.
- [Equity theme stub](./equity-theme-stub.md) — theme → ticker hypotheses.
