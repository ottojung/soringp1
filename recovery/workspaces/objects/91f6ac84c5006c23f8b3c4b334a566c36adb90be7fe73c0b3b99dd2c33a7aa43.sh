#!/bin/sh
# Act 21 exact-revision verifier: hermetic POSIX smoke test.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
scratch=$(mktemp -d)
trap 'rm -rf "$scratch"' EXIT HUP INT TERM
town=$scratch/town
mkdir -p "$town/government" "$town/records" "$town/tests"
cp "$repo/government/suite-status.sh" "$town/government/"
git -C "$town" init -q -b main
git -C "$town" config user.email fixture@example.invalid
git -C "$town" config user.name Fixture
git -C "$town" config commit.gpgsign false

cat > "$town/tests/green.sh" <<'EOF'
#!/bin/sh
exit 0
EOF
cat > "$town/tests/red.sh" <<'EOF'
#!/bin/sh
echo boom
exit 1
EOF
cat > "$town/tests/flaky.sh" <<'EOF'
#!/bin/sh
n=$(cat "$SUITE_STATUS_SMOKE_COUNTER" 2>/dev/null || echo 0)
n=$((n + 1))
printf '%s\n' "$n" > "$SUITE_STATUS_SMOKE_COUNTER"
[ "$n" -ge 2 ]
EOF
SUITE_STATUS_SMOKE_COUNTER=$scratch/flaky.count
export SUITE_STATUS_SMOKE_COUNTER
git -C "$town" add -A
git -C "$town" commit -qm 'committed gate and fixtures'

run() {
  VICHE_TOWN_ROOT=$town /bin/sh "$town/government/suite-status.sh" "$@"
}
check_result() {
  jq -e --arg expected "$1" '.result == $expected' "$town/records/suite-status.json" >/dev/null
}

run --suite tests/green.sh >/dev/null
check_result green
jq -e --arg commit "$(git -C "$town" rev-parse HEAD)" \
  --arg tree "$(git -C "$town" rev-parse HEAD^{tree})" \
  '.commit==$commit and .tree==$tree' "$town/records/suite-status.json" >/dev/null

if run --suite tests/red.sh >/dev/null 2>&1; then
  echo "FAIL: committed red suite must block" >&2; exit 1
fi
check_result red
jq -e '.incident == true and (.runs|length)==2' "$town/records/suite-status.json" >/dev/null

run --suite tests/flaky.sh >/dev/null
check_result green
jq -e '.runs|map(.result)==["red","green"]' "$town/records/suite-status.json" >/dev/null

run --suite tests/green.sh --ci red >/dev/null
jq -e '.ci_reconciliation=="disagree" and .incident==true' "$town/records/suite-status.json" >/dev/null

# Important regression: HEAD vs --commit vs dirty worktree must never mix.
printf '#!/bin/sh\nexit 0\n' > "$town/tests/probe.sh"
git -C "$town" add tests/probe.sh
git -C "$town" commit -qm 'green revision'
good=$(git -C "$town" rev-parse HEAD)
printf '#!/bin/sh\necho intentional-failure; exit 1\n' > "$town/tests/probe.sh"
git -C "$town" add tests/probe.sh
git -C "$town" commit -qm 'red revision'
bad=$(git -C "$town" rev-parse HEAD)

# Deliberately fool the old implementation: current working file green,
# specified revision red. The updated verifier must report the red commit.
printf '#!/bin/sh\nexit 0\n' > "$town/tests/probe.sh"
if run --suite tests/probe.sh --commit "$bad" >/dev/null 2>&1; then
  echo "FAIL: dirty current checkout masqueraded as red commit" >&2; exit 1
fi
check_result red
jq -e --arg sha "$bad" --arg tree "$(git -C "$town" rev-parse "$bad^{tree}")" \
  '.commit==$sha and .tree==$tree' "$town/records/suite-status.json" >/dev/null

# Conversely, verifying an older green commit remains green despite HEAD red.
run --suite tests/probe.sh --commit "$good" >/dev/null
check_result green
jq -e --arg sha "$good" '.commit==$sha' "$town/records/suite-status.json" >/dev/null

# Invalid suites and suites absent at the target revision must fail closed.
if run --suite tests/../government/suite-status.sh >/dev/null 2>&1; then
  echo "FAIL: accepted traversal" >&2; exit 1
fi
if run --suite tests/probe.sh --commit HEAD~2 >/dev/null 2>&1; then
  echo "FAIL: accepted test absent from verified commit" >&2; exit 1
fi

test "$(git -C "$town" worktree list --porcelain | grep -c '^worktree ')" -eq 1
test "$(git -C "$town" status --porcelain -- tests/probe.sh)" = ' M tests/probe.sh'
echo 'Exact-commit quality-gate, flaky-red and isolation smoke passed'
