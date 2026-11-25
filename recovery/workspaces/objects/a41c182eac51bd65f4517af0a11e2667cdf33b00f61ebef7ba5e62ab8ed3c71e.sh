#!/bin/sh
# Act 31 integration queue, hermetic: a local bare origin, real
# propose-delivery.sh and suite-status.sh, and a fake antonina for reviewers.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT HUP INT TERM
town=$tmp/town
remote=$tmp/origin.git
state=$tmp/state
mkdir -p "$town" "$state" "$tmp/bin"
git init --bare -q -b main "$remote"
git -C "$town" init -q -b main
git -C "$town" config user.name Fixture
git -C "$town" config user.email fixture@example.invalid
git -C "$town" config commit.gpgsign false
git -C "$town" remote add origin "$remote"
mkdir -p "$town/government" "$town/tests" "$town/records" "$town/constitution"
for f in suite-status.sh integrator.py propose-delivery.sh review-delivery.sh dispatch-gate.sh; do
  cp "$repo/government/$f" "$town/government/$f"
done
# Suites: red when records/BREAK and records/ARM are both present (green on
# each side alone, red once merged); every run is counted.
cat > "$town/tests/records-smoke.sh" <<'EOF'
#!/bin/sh
echo run >> "${SUITE_COUNTER:-/dev/null}"
if [ -e records/BREAK ] && [ -e records/ARM ]; then echo 'records/BREAK with records/ARM'; exit 1; fi
EOF
cp "$town/tests/records-smoke.sh" "$town/tests/run-all.sh"
printf 'canonical policy\n' > "$town/AGENTS.md"
printf 'old line\n' > "$town/records/shared.md"
printf 'row1\n' > "$town/records/ledger.tsv"
printf '# Laws\n' > "$town/government/LAWS.md"
printf 'charter\n' > "$town/constitution/CONSTITUTION.md"
printf '#!/bin/sh\necho v1\n' > "$town/government/tool.sh"
git -C "$town" add -A
git -C "$town" commit -qm baseline
git -C "$town" push -q -u origin main

# Fake Antonina: records calls, hands out reviewer ids, reports them running.
cat > "$tmp/bin/antonina" <<EOF
#!/bin/sh
echo "\$*" >> "$tmp/antonina.log"
case "\$1 \$2" in
  'agent new') n=\$(grep -c '^agent new' "$tmp/antonina.log"); echo "rev\$n-fixture" ;;
  'agent run') exit 0 ;;
  'agent status') echo '{"state":"running"}' ;;
esac
EOF
chmod +x "$tmp/bin/antonina"
export PATH="$tmp/bin:$PATH" VICHE_TOWN_ROOT="$town" VICHE_STATE_ROOT="$state" SUITE_COUNTER="$tmp/suite-runs"

seat() { # seat NAME: a registered worktree on a fresh branch from main
  git -C "$town" worktree add -q -b "work-$1" "$tmp/$1" main >/dev/null 2>&1
  git -C "$tmp/$1" config user.name Fixture
}
propose() { # propose WORKTREE OFFICE SLUG
  (cd "$tmp/$1" && /bin/sh "$town/government/propose-delivery.sh" --office "$2" "$3") >/dev/null
}
integrate() { python3 "$town/government/integrator.py" run 2>>"$tmp/integrator.log"; }
st() { jq -r --arg b "delivery/$1" '[.entries[] | select(.branch == $b)] | last | .status' "$state/delivery/queue.json"; }
on_main() { git -C "$remote" cat-file -e "main:$1" 2>/dev/null; }

# 1. Additive records (a new file) land without review, as candidate + carrier.
seat a
printf 'plenary outcome\n' > "$tmp/a/records/outcome.md"
git -C "$tmp/a" add -A; git -C "$tmp/a" commit -qm 'c1a00002: plenary outcome'
base=$(git -C "$remote" rev-parse main)
propose a c1a00002 outcome
integrate
test "$(st outcome)" = landed
on_main records/outcome.md
carrier=$(git -C "$remote" rev-parse main)
candidate=$(git -C "$remote" rev-parse main^)
test "$(git -C "$remote" rev-parse main^^)" = "$base"                      # single candidate on main
test "$(git -C "$remote" diff --name-only "$candidate" "$carrier")" = records/suite-status.json
git -C "$remote" show -s --format=%B "$candidate" | grep -q '^Reviewed-By: none (additive records'
git -C "$remote" show -s --format=%B "$candidate" | grep -q '^Proposed-By: c1a00002$'
git -C "$remote" show "main:records/suite-status.json" | jq -e --arg c "$candidate" \
  '.commit == $c and .result == "green" and .verifier == "integrator"' >/dev/null
jq -e '[.assertions[] | select(.expected != .actual)] | length == 0' "$state/delivery/integration-$candidate.json" >/dev/null
test -s "$state/delivery/published-$candidate.json"
test "$(git -C "$town" rev-parse HEAD)" = "$carrier"                     # canonical fast-forwarded
python3 "$town/government/integrator.py" office c1a00002 | grep -q 'landed on main'
test ! -s "$tmp/antonina.log"                                             # no reviewer needed

# 2. A pure append to an existing record is additive too.
seat b
printf 'row2\n' >> "$tmp/b/records/ledger.tsv"
git -C "$tmp/b" add -A; git -C "$tmp/b" commit -qm 'append a ledger row'
propose b judiciary ledger
integrate
test "$(st ledger)" = landed
test "$(git -C "$remote" show main:records/ledger.tsv | wc -l)" -eq 2

# 3. Code needs an independent review; the integrator commissions it, ignores
#    the proposer's own approval and lands after another office approves.
seat c
printf '#!/bin/sh\necho v2\n' > "$tmp/c/government/tool.sh"
git -C "$tmp/c" add -A; git -C "$tmp/c" commit -qm 'tool v2'
propose c executive tool
head=$(git -C "$tmp/c" rev-parse HEAD)
integrate
test "$(st tool)" = reviewing
grep -q '^agent new --title Viche reviewer: delivery/tool' "$tmp/antonina.log"
grep -q '^agent run --id rev1-fixture ' "$tmp/antonina.log"
grep -q "review-delivery.sh delivery/tool $head approve --office reviewer-rev1-fixture" "$tmp/antonina.log"
python3 "$town/government/integrator.py" office executive | grep -q 'under independent review'
/bin/sh "$town/government/review-delivery.sh" delivery/tool "$head" approve --office executive --reason 'mine' >/dev/null
integrate
test "$(st tool)" = reviewing                                              # self-approval ignored
test "$(grep -c '^agent new' "$tmp/antonina.log")" -eq 1                   # no second reviewer yet
/bin/sh "$town/government/review-delivery.sh" delivery/tool "$head" approve --office reviewer-rev1-fixture --reason 'correct' >/dev/null
integrate
test "$(st tool)" = landed
git -C "$remote" show main:government/tool.sh | grep -q v2
git -C "$remote" show -s --format=%B main^ | grep -q '^Reviewed-By: reviewer-rev1-fixture$'
git -C "$remote" show main:records/suite-status.json | jq -e '.suite == "tests/run-all.sh"' >/dev/null

# 4. A rejection stops the delivery and tells the proposer why.
seat d
printf '#!/bin/sh\necho v3\n' > "$tmp/d/government/tool.sh"
git -C "$tmp/d" add -A; git -C "$tmp/d" commit -qm 'tool v3'
propose d executive tool-v3
integrate
/bin/sh "$town/government/review-delivery.sh" delivery/tool-v3 "$(git -C "$tmp/d" rev-parse HEAD)" reject \
  --office c1a00005 --reason 'breaks the v2 contract' >/dev/null
integrate
test "$(st tool-v3)" = rejected
python3 "$town/government/integrator.py" office executive | grep -q 'REJECTED by c1a00005: breaks the v2 contract'
git -C "$remote" show main:government/tool.sh | grep -q v2

# 5. A red candidate is not landed, keeps its log, and is not re-run every cycle.
seat e
printf 'x\n' > "$tmp/e/records/BREAK"
git -C "$tmp/e" add -A; git -C "$tmp/e" commit -qm 'green alone, red once merged'
SUITE_COUNTER=/dev/null propose e c1a00004 breaker
seat arm
printf 'x\n' > "$tmp/arm/records/ARM"
git -C "$tmp/arm" add -A; git -C "$tmp/arm" commit -qm 'main moves on'
git -C "$tmp/arm" push -q origin HEAD:main
: > "$tmp/suite-runs"
integrate
test "$(st breaker)" = red
if on_main records/BREAK; then echo 'a red candidate reached main' >&2; exit 1; fi
runs=$(wc -l < "$tmp/suite-runs")
test "$runs" -eq 2                                                         # flaky-red rule: two runs
integrate
test "$(wc -l < "$tmp/suite-runs")" -eq "$runs"
log=$(jq -r '[.entries[] | select(.branch == "delivery/breaker")] | last | .log' "$state/delivery/queue.json")
grep -q 'records/BREAK with records/ARM' "$log"
python3 "$town/government/integrator.py" office c1a00004 | grep -q 'RED: tests/records-smoke.sh failed twice'

# 6. A conflict with main is reported, not landed.
seat f
printf 'their line\n' > "$tmp/f/records/shared.md"
git -C "$tmp/f" add -A; git -C "$tmp/f" commit -qm 'edit shared'
seat g
printf 'main line\n' > "$tmp/g/records/shared.md"
git -C "$tmp/g" add -A; git -C "$tmp/g" commit -qm 'edit shared on main'
git -C "$tmp/g" push -q origin HEAD:main
propose f c1a00006 shared
integrate
/bin/sh "$town/government/review-delivery.sh" delivery/shared "$(git -C "$tmp/f" rev-parse HEAD)" approve \
  --office c1a00007 --reason ok >/dev/null
integrate
test "$(st shared)" = conflict
python3 "$town/government/integrator.py" office c1a00006 | grep -q 'CONFLICT: conflicts with main in records/shared.md'

# 7. The Constitution is refused; law without an enactment trailer is refused.
seat h
printf 'amended\n' > "$tmp/h/constitution/CONSTITUTION.md"
git -C "$tmp/h" add -A; git -C "$tmp/h" commit -qm 'amend charter'
propose h c1a00008 charter
seat i
printf '## Act 99\n' >> "$tmp/i/government/LAWS.md"
git -C "$tmp/i" add -A; git -C "$tmp/i" commit -qm 'new act'
propose i c1a00009 law
integrate
/bin/sh "$town/government/review-delivery.sh" delivery/law "$(git -C "$tmp/i" rev-parse HEAD)" approve \
  --office c1a0000a --reason ok >/dev/null
integrate
test "$(st charter)" = refused
test "$(st law)" = refused
jq -r '.entries[] | select(.branch == "delivery/law") | .reason' "$state/delivery/queue.json" | grep -q 'Enacts: BILL'

# 8. Canonical evidence is never overwritten: an untracked canonical file at
#    the same path waits; the stale generated suite record is backed up.
seat j
printf 'new report\n' > "$tmp/j/records/report.md"
git -C "$tmp/j" add -A; git -C "$tmp/j" commit -qm 'report'
printf 'unreviewed local evidence\n' > "$town/records/report.md"
printf '{"stale":true}\n' > "$town/records/suite-status.json"
propose j judiciary report
integrate
test "$(st report)" = approved
jq -r '.entries[] | select(.branch == "delivery/report") | .reason' "$state/delivery/queue.json" | grep -q 'untracked canonical file'
grep -q 'unreviewed local evidence' "$town/records/report.md"
mv "$town/records/report.md" "$tmp/kept-report.md"
integrate
test "$(st report)" = landed
ls "$state/delivery/"suite-canonical-*.json >/dev/null

# 9. An office's dispatch gate wakes when its delivery changes state.
cp "$repo/government/dispatch-gate.sh" "$town/government/dispatch-gate.sh"
echo same | /bin/sh "$town/government/dispatch-gate.sh" check c1a00004 >/dev/null
/bin/sh "$town/government/dispatch-gate.sh" commit c1a00004
if echo same | /bin/sh "$town/government/dispatch-gate.sh" check c1a00004 >/dev/null; then
  echo 'gate did not skip unchanged inputs' >&2; exit 1
fi
printf '[{"status":"landed"}]\n' > "$state/delivery/office/c1a00004.json"
echo same | /bin/sh "$town/government/dispatch-gate.sh" check c1a00004 | grep -q inputs_changed

# 10. Proposals from before Act 31 (no office column) are never picked up.
printf '2026-11-10T00:00:00Z\twork-x\trefs/heads/delivery/legacy\t%s\ttree\ttests/run-all.sh\n' "$head" \
  >> "$state/delivery/proposals.tsv"
integrate
test "$(jq '[.entries[] | select(.branch == "delivery/legacy")] | length' "$state/delivery/queue.json")" -eq 0

VICHE_INTEGRATOR=off python3 "$town/government/integrator.py" run
echo 'integrator smoke passed'
