#!/bin/sh
# Act 30 §5: skip a model dispatch when every input is identical to the last
# dispatched pass; a heartbeat, a change, a failed launch or a broken probe
# always lets work through.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
d=$(mktemp -d)
trap 'rm -rf "$d"' EXIT HUP INT TERM
mkdir -p "$d/state" "$d/bin"
export VICHE_STATE_ROOT="$d/state" PATH="$d/bin:$PATH"
gate="/bin/sh $repo/government/dispatch-gate.sh"

check() { # key max_age input -> sets rc, prints reason
  rc=0
  out=$(printf '%s' "$3" | $gate check "$1" "$2") || rc=$?
}

# First pass dispatches. Not committed yet, so the next pass dispatches again:
# a failed or ambiguous launch never silences an office.
check exec 7200 'inputs A'; test "$rc" -eq 0; test "$out" = first_pass
check exec 7200 'inputs A'; test "$rc" -eq 0; test "$out" = first_pass
$gate commit exec
jq -e '.total_dispatches == 1 and .skips_since_dispatch == 0' "$d/state/dispatch-gate/exec.json" >/dev/null

# Identical inputs now skip (exit 10) and are counted.
check exec 7200 'inputs A'; test "$rc" -eq 10
check exec 7200 'inputs A'; test "$rc" -eq 10
jq -e '.skips_since_dispatch == 2 and .total_skips == 2 and .total_dispatches == 1' "$d/state/dispatch-gate/exec.json" >/dev/null

# A skip does not move the fingerprint; a change dispatches and is reported as such.
check exec 7200 'inputs B'; test "$rc" -eq 0; test "$out" = inputs_changed
$gate commit exec
jq -e '.total_dispatches == 2 and .skips_since_dispatch == 0 and .total_skips == 2' "$d/state/dispatch-gate/exec.json" >/dev/null
check exec 7200 'inputs B'; test "$rc" -eq 10
check exec 7200 'inputs A'; test "$rc" -eq 0; test "$out" = inputs_changed   # going back is a change too
$gate commit exec

# Heartbeat: unchanged inputs still dispatch once the last dispatch is older than MAX_AGE.
old=$(( $(date +%s) - 8000 ))
jq --argjson t "$old" '.last_dispatch_at = $t' "$d/state/dispatch-gate/exec.json" > "$d/tmp.json"
mv "$d/tmp.json" "$d/state/dispatch-gate/exec.json"
check exec 7200 'inputs A'; test "$rc" -eq 0; test "$out" = heartbeat
check exec 86400 'inputs A'; test "$rc" -eq 10                                # a longer window still skips

# Keys are independent.
check clerk 7200 'inputs A'; test "$rc" -eq 0; test "$out" = first_pass

# The switch turns skipping off but still records.
$gate commit clerk
check clerk 7200 'inputs A'; test "$rc" -eq 10
rc=0; out=$(printf 'inputs A' | VICHE_DISPATCH_GATE=off $gate check clerk 7200) || rc=$?
test "$rc" -eq 0; test "$out" = gate_off

# Bad arguments are refused, not guessed.
rc=0; printf x | $gate check 'bad key!' 2>/dev/null || rc=$?; test "$rc" -eq 2
rc=0; $gate bogus 2>/dev/null || rc=$?; test "$rc" -eq 2

# Event log and stats feed the digest.
$gate stats 0 | awk -F '\t' '$1=="exec" && $2==3 && $3==4 {ok=1} END {exit !ok}'
since=$(( $(date +%s) + 3600 ))
test -z "$($gate stats "$since")"

# board-signature: one stable line per issue; any lookup failure exits 1 so callers fail open.
cat > "$d/bin/antonina" <<'MOCK'
#!/bin/sh
[ "$1 $2" = 'board show' ] || exit 9
case "$4" in
  302) printf '{"updatedAt":"2026-11-16T10:00:00Z","messages":[{"id":"sha256:m302"},{"id":"older"}]}\n' ;;
  301) printf '{"updatedAt":"2026-11-15T10:00:00Z","messages":[]}\n' ;;
  *) exit 3 ;;
esac
MOCK
chmod +x "$d/bin/antonina"
sig=$($gate board-signature 302 301)
test "$sig" = '302 2026-11-16T10:00:00Z sha256:m302
301 2026-11-15T10:00:00Z -'
rc=0; $gate board-signature 302 999 >/dev/null 2>&1 || rc=$?; test "$rc" -eq 1
rc=0; $gate board-signature 'a b' >/dev/null 2>&1 || rc=$?; test "$rc" -eq 2

echo 'dispatch gate smoke passed'
