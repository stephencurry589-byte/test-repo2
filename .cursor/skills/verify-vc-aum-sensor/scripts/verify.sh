#!/usr/bin/env bash
# VC AUM sensor verification helper — doctor | run [--out PATH] | cleanup
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
cd "$ROOT"
SKILL_DIR="$ROOT/.cursor/skills/verify-vc-aum-sensor"
DEFAULT_OUT="$SKILL_DIR/artifacts/VERIFY-RUN.md"
TS_ZONE="America/Chicago"

usage() {
  echo "Usage: $0 doctor | run [--out PATH] | cleanup" >&2
  exit 2
}

doctor() {
  local ok=0
  echo "doctor: repo=$ROOT"
  if ! command -v python3 >/dev/null 2>&1; then
    echo "doctor: FAIL — python3 not on PATH"
    return 1
  fi
  echo "doctor: python3=$(python3 --version 2>&1)"
  if [[ ! -f "$ROOT/data/top50_seed.json" ]]; then
    echo "doctor: FAIL — missing data/top50_seed.json"
    return 1
  fi
  echo "doctor: seed=present"
  if ! python3 -c "import src.cli, src.schema, src.trends, src.equity_stub; from src.adapters.stub_press import StubPressAdapter" 2>&1; then
    echo "doctor: FAIL — import error"
    return 1
  fi
  echo "doctor: imports=ok"
  if [[ ! -f "$ROOT/tests/test_smoke.py" ]]; then
    echo "doctor: FAIL — missing tests/test_smoke.py"
    return 1
  fi
  echo "doctor: smoke_module=present"
  echo "doctor: PASS"
  return 0
}

cleanup() {
  find "$ROOT" -type d -name '__pycache__' -not -path '*/.git/*' -exec rm -rf {} + 2>/dev/null || true
  find "$ROOT" -type d -name '.pytest_cache' -not -path '*/.git/*' -exec rm -rf {} + 2>/dev/null || true
  echo "cleanup: removed __pycache__/.pytest_cache only (evidence retained)"
}

sha_line() {
  local f="$1"
  if [[ -f "$f" ]]; then
    sha256sum "$f"
  else
    echo "MISSING  $f"
  fi
}

run_verify() {
  local out="${1:-$DEFAULT_OUT}"
  mkdir -p "$(dirname "$out")"
  local start_epoch end_epoch
  start_epoch=$(date +%s)
  local when
  when=$(TZ="$TS_ZONE" date '+%Y-%m-%d %H:%M:%S %Z')
  local git_sha
  git_sha=$(git -C "$ROOT" rev-parse HEAD 2>/dev/null || echo "NO_GIT")

  local doctor_rc=0 doctor_out
  doctor_out=$(doctor 2>&1) || doctor_rc=$?

  local smoke_rc=0 smoke_out
  if [[ $doctor_rc -eq 0 ]]; then
    smoke_out=$(python3 tests/test_smoke.py 2>&1) || smoke_rc=$?
  else
    smoke_out="SKIPPED — doctor failed"
    smoke_rc=99
  fi

  local cli_rc=0 cli_out
  if [[ $doctor_rc -eq 0 ]]; then
    cli_out=$(python3 -m src.cli 2>&1) || cli_rc=$?
  else
    cli_out="SKIPPED — doctor failed"
    cli_rc=99
  fi

  local verdict="PASS"
  if [[ $doctor_rc -ne 0 || $smoke_rc -ne 0 || $cli_rc -ne 0 ]]; then
    verdict="FAIL"
  fi

  # Side-effect check: data/ should still only contain seed (no new files from CLI)
  local data_files
  data_files=$(find "$ROOT/data" -type f | sort | tr '\n' ' ')

  end_epoch=$(date +%s)
  local elapsed=$((end_epoch - start_epoch))

  {
    echo "# VERIFY-RUN — vc-aum-sensor"
    echo
    echo "- When: $when (America/Chicago)"
    echo "- Repo: $ROOT"
    echo "- Git HEAD: \`$git_sha\`"
    echo "- Verdict: **$verdict**"
    echo "- Elapsed_s: $elapsed"
    echo
    echo "## Exit codes"
    echo
    echo "| Step | Exit |"
    echo "|---|---|"
    echo "| doctor | $doctor_rc |"
    echo "| python3 tests/test_smoke.py | $smoke_rc |"
    echo "| python3 -m src.cli | $cli_rc |"
    echo
    echo "## sha256 of key files"
    echo
    echo '```'
    sha_line "$ROOT/README.md"
    sha_line "$ROOT/tests/test_smoke.py"
    sha_line "$ROOT/src/cli.py"
    sha_line "$ROOT/data/top50_seed.json"
    sha_line "$ROOT/.cursor/skills/verify-vc-aum-sensor/scripts/verify.sh"
    sha_line "$ROOT/.cursor/skills/verify-vc-aum-sensor/SKILL.md"
    echo '```'
    echo
    echo "## Doctor"
    echo
    echo '```'
    echo "$doctor_out"
    echo '```'
    echo
    echo "## Smoke (python3 tests/test_smoke.py)"
    echo
    echo '```'
    echo "$smoke_out"
    echo '```'
    echo
    echo "## CLI (python3 -m src.cli)"
    echo
    echo '```'
    echo "$cli_out"
    echo '```'
    echo
    echo "## Side effects"
    echo
    echo "- data/ files after run: \`$data_files\`"
    echo "- Expected: only seed JSON under data/; CLI is stdout-only."
    echo
    echo "## Feature coverage this run"
    echo
    echo "- smoke-suite: $([[ $smoke_rc -eq 0 ]] && echo PASS || echo FAIL)"
    echo "- cli-rollup: $([[ $cli_rc -eq 0 ]] && echo PASS || echo FAIL)"
    echo "- seed-placeholders / stub-press-adapter / equity-theme-stub: exercised via smoke suite"
    echo
    echo "## Re-run"
    echo
    echo '```bash'
    echo "cd $ROOT"
    echo ".cursor/skills/verify-vc-aum-sensor/scripts/verify.sh run --out $out"
    echo '```'
  } > "$out"

  cleanup >/dev/null
  echo "verify: wrote $out"
  echo "verify: verdict=$verdict doctor=$doctor_rc smoke=$smoke_rc cli=$cli_rc"
  [[ "$verdict" == "PASS" ]]
}

cmd="${1:-}"
case "$cmd" in
  doctor) doctor ;;
  cleanup) cleanup ;;
  run)
    shift || true
    out_path="$DEFAULT_OUT"
    if [[ "${1:-}" == "--out" ]]; then
      out_path="${2:?--out requires PATH}"
    elif [[ -n "${1:-}" ]]; then
      usage
    fi
    run_verify "$out_path"
    ;;
  *) usage ;;
esac
