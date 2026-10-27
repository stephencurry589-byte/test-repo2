---
name: verify-vc-aum-sensor
description: Verify the VC AUM sensor CLI (stdlib Python scaffold). Use when proving smoke tests, CLI rollup JSON, seed/adapter/equity stub behavior, or writing a re-runnable PROOF artifact for this repo.
---

# Verify VC AUM sensor

Project-local verification for the public-source VC AUM sensor scaffold. Primary surface is a short-lived CLI; there is no long-lived server. DEMO/PLACEHOLDER data only — never treat output as live market fact.

## Launch

No server. From repo root (`/workspace/vc-aum-sensor` or any clone of this repo):

```bash
cd "$(git rev-parse --show-toplevel)"
python3 -c "import src.cli, src.schema"   # import readiness
```

Ready when the import exits 0. Teardown: none required (process exits). Optional: `rm -rf src/**/__pycache__ tests/__pycache__` — never delete proof artifacts.

Concurrent runs are isolated: stdlib + read-only DEMO seed; no ports, no shared writable state.

## Doctor

Read-only health check before any drive:

```bash
.cursor/skills/verify-vc-aum-sensor/scripts/verify.sh doctor
```

Expect exit 0 and lines confirming: Python 3 available, `src.cli` imports, `data/top50_seed.json` exists, smoke module loads. If doctor fails, do not drive — fix the environment or report blocked.

## Drive

Harness is shell + stdlib unittest (no browser, no PTY server). Prefer the helper:

```bash
.cursor/skills/verify-vc-aum-sensor/scripts/verify.sh run [--out PATH]
```

Mapped features (see `features/`):

| Feature | Command | Observable pass |
|---|---|---|
| smoke-suite | `python3 tests/test_smoke.py` | exit 0, `OK`, `Ran 6 tests` |
| cli-rollup | `python3 -m src.cli` | exit 0, JSON with `disclaimer` containing DEMO/PLACEHOLDER, `trends.event_count >= 1` |
| seed-placeholders | covered by smoke `test_seed_placeholders` | ≤15 firms, all `placeholder=True` |
| stub-press-adapter | covered by smoke `test_stub_adapter_returns_demo_events` | 1–2 demo events |
| equity-theme-stub | covered by smoke `test_equity_stub_demo` | all hypotheses `demo=True` with evidence URLs |

Drive one feature at a time for proofs; for a full PROOF run use `verify.sh run`.

## Evidence

Proof standards:

- Exercise the real user path: `python3 -m src.cli` and `python3 tests/test_smoke.py` (not internal setters alone).
- Capture command, exit code, stdout (and stderr if non-empty), and PASS/FAIL.
- Side effects: CLI writes nothing to disk; smoke is read-only against seed/adapters. Confirm no unexpected files under `data/` after the run.
- Default artifact location when `--out` omitted: `.cursor/skills/verify-vc-aum-sensor/artifacts/VERIFY-RUN.md` (gitignored). Ticket PROOF paths (e.g. `/workspace/doc/tickets/.../results/VERIFY-RUN.md`) are passed via `--out` and must survive cleanup.

## Cleanup

Kill nothing by name — each drive is a short-lived process. After a run:

```bash
.cursor/skills/verify-vc-aum-sensor/scripts/verify.sh cleanup
```

Removes only `__pycache__` / `.pytest_cache` under the repo. Does **not** delete evidence files under `artifacts/` or any `--out` path.

## Helpers

| Script | Invocation |
|---|---|
| `scripts/verify.sh` | `doctor` \| `run [--out PATH]` \| `cleanup` |

Make executable once: `chmod +x .cursor/skills/verify-vc-aum-sensor/scripts/verify.sh`.

## Maintain

Keep the feature map honest with `/maintain-verification-skill` after user-facing CLI or smoke changes. Eng-desk PLAYBOOK §0c and `run-failure-checks.sh` remain the desk-level failure library — this skill does not replace them; see `VERIFICATION.md`.
