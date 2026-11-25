#!/bin/sh
# Act 30 §3: an unanswered reversible request lets the requester proceed after
# its deadline; the addressee audits afterwards; irreversible acts never proceed.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
d=$(mktemp -d)
trap 'rm -rf "$d"' EXIT HUP INT TERM
mkdir -p "$d/town"
pbd="/bin/sh $repo/government/proceed-by-default.sh"
t=$d/town
fails() { if "$@" >/dev/null 2>&1; then echo "expected failure: $*" >&2; exit 1; fi; }
age() { # ID HOURS_AGO: move the deadline into the past
  past=$(date -u -d "@$(( $(date +%s) - $2 * 3600 ))" +%FT%TZ)
  sed "s/^deadline: .*/deadline: $past/" "$t/records/proceed/$1.txt" > "$d/x" && mv "$d/x" "$t/records/proceed/$1.txt"
}

# Validation.
fails $pbd request "$t" executive judiciary 0 reversible 'x'
fails $pbd request "$t" executive judiciary 73 reversible 'x'
fails $pbd request "$t" executive judiciary 24 maybe 'x'
fails $pbd request "$t" 'bad office' judiciary 24 reversible 'x'
fails $pbd request "$t" executive judiciary 24 reversible ''

# A fresh request: addressee sees it as waiting; requester may not proceed yet.
r1=$($pbd request "$t" executive judiciary 24 reversible 'close case C-12 as duplicate')
case "$r1" in P-[0-9]*-*) : ;; *) echo "bad id $r1" >&2; exit 1 ;; esac
$pbd brief "$t" judiciary | grep -q "WAITING ON YOU"
$pbd brief "$t" judiciary | grep -q 'close case C-12 as duplicate'
test -z "$($pbd brief "$t" executive)"
fails $pbd proceed "$t" "$r1" 'going ahead early'
$pbd sweep "$t"
test "$($pbd list "$t" pending | wc -l)" -eq 1

# Deadline passes with no answer: sweep marks it due; requester may proceed.
age "$r1" 1
$pbd sweep "$t"
test "$($pbd list "$t" due | cut -f1)" = "$r1"
$pbd brief "$t" executive | grep -q 'DEADLINE PASSED, NO ANSWER'
$pbd brief "$t" executive | grep -q "proceed-by-default.sh proceed $t"
$pbd proceed "$t" "$r1" 'closed C-12 with evidence E'
grep -q '^status: proceeded$' "$t/records/proceed/$r1.txt"
fails $pbd proceed "$t" "$r1" 'twice'

# After the fact: addressee and the Judiciary get an audit prompt; upheld closes it.
$pbd brief "$t" judiciary | grep -q 'AWAITING YOUR AFTER-THE-FACT AUDIT'
$pbd brief "$t" judiciary | grep -q 'closed C-12 with evidence E'
test -z "$($pbd brief "$t" clerk)"
fails $pbd audit "$t" "$r1" bogus 'x'
$pbd audit "$t" "$r1" upheld 'evidence checked, fine'
grep -q '^status: audited-upheld$' "$t/records/proceed/$r1.txt"
test -z "$($pbd brief "$t" judiciary)"
fails $pbd audit "$t" "$r1" reversed 'second audit'

# Irreversible acts never proceed by default, even long after the deadline.
r2=$($pbd request "$t" executive judiciary 24 irreversible 'delete the old worktree archive')
age "$r2" 48
$pbd sweep "$t"
code=0; $pbd proceed "$t" "$r2" 'going' >/dev/null 2>&1 || code=$?
test "$code" -eq 3
test -z "$($pbd brief "$t" executive)"          # not offered as "you may proceed"
$pbd brief "$t" judiciary | grep -q 'class irreversible'

# An answer before the deadline settles it; proceeding afterwards is a no-op, not a bypass.
r3=$($pbd request "$t" recovery-steward executive 12 reversible 'rotate the stale session')
$pbd answer "$t" "$r3" declined 'keep it until the audit finishes'
grep -q '^status: declined$' "$t/records/proceed/$r3.txt"
age "$r3" 1
fails $pbd proceed "$t" "$r3" 'ignoring the refusal'
fails $pbd answer "$t" "$r3" approved 'late change of mind'

r4=$($pbd request "$t" auditor executive 6 reversible 'refresh the metrics page')
$pbd answer "$t" "$r4" approved 'yes'
age "$r4" 1
$pbd proceed "$t" "$r4" 'already approved'
grep -q '^status: approved$' "$t/records/proceed/$r4.txt"

# Reversed audits stay visible in the list.
r5=$($pbd request "$t" executive judiciary 1 reversible 'merge the docs fix')
age "$r5" 2
$pbd proceed "$t" "$r5" 'merged'
$pbd audit "$t" "$r5" reversed 'quality gate was red'
$pbd list "$t" all | awk -F '\t' -v id="$r5" '$1==id && $2=="audited-reversed" {ok=1} END {exit !ok}'

# No ledger directory: everything is quiet and succeeds.
mkdir -p "$d/empty"
test -z "$($pbd brief "$d/empty" executive)"
$pbd sweep "$d/empty"
test -z "$($pbd list "$d/empty")"

echo 'proceed-by-default smoke passed'
