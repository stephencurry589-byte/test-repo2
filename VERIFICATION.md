# Verification

Project-local pstack verification for this repo. Produces a re-runnable PROOF file artifact.

## Skill

- Skill: `.cursor/skills/verify-vc-aum-sensor/` (`name: verify-vc-aum-sensor`)
- Feature map: `.cursor/skills/verify-vc-aum-sensor/features/`
- Helper: `.cursor/skills/verify-vc-aum-sensor/scripts/verify.sh`

## Re-run (local)

```bash
cd /workspace/vc-aum-sensor   # or your clone root
.cursor/skills/verify-vc-aum-sensor/scripts/verify.sh doctor
.cursor/skills/verify-vc-aum-sensor/scripts/verify.sh run
# default artifact: .cursor/skills/verify-vc-aum-sensor/artifacts/VERIFY-RUN.md
```

Ticket / external PROOF path:

```bash
.cursor/skills/verify-vc-aum-sensor/scripts/verify.sh run \
  --out /path/to/results/VERIFY-RUN.md
```

Manual equivalent (same gates the helper runs):

```bash
python3 tests/test_smoke.py   # expect: Ran 6 tests … OK, exit 0
python3 -m src.cli            # expect: JSON stdout with DEMO disclaimer, exit 0
```

## Maintain

After CLI or smoke surface changes, run `/maintain-verification-skill` against `.cursor/skills/verify-vc-aum-sensor/`.

## Eng-desk pointer

Desk-level failure library and gates stay in eng PLAYBOOK §0c and `run-failure-checks.sh` at eng-desk. This repo skill does not rewrite that playbook; use it for product PROOF artifacts that tickets can re-run.
