#!/bin/sh
# Consolidation-audit check (Act 6.2; Constitution VI): every `origin` ballot
# branch `ballot/<seat>-<bill>` for a bill must be either counted in the durable
# ballot record `records/ballots/<bill>.tsv` or explicitly reported missing.
#
# Fixes the 2026-10-21 defect (Act 22): a valid ballot committed to origin at
# 04:34:56Z, before the 04:36:42Z consolidation, was missed because the
# remote-tracking ref was stale (no fetch immediately before consolidating).
# The Clerk MUST re-fetch and run this before declaring a tally final.
#
# Usage: ballot-completeness.sh BILL_ID
# Exit 0 if every origin ballot branch is counted; 1 if any is missing.
set -eu
[ "$#" -eq 1 ] || { echo "usage: ballot-completeness.sh BILL_ID" >&2; exit 2; }
bill=$1
case "$bill" in ''|*[!a-zA-Z0-9_-]*) echo "Invalid bill ID" >&2; exit 2;; esac
town=${VICHE_TOWN_ROOT:-/var/lib/lubko/wd/viche}
rec=$town/records/ballots/$bill.tsv
# Re-fetch so the audit sees every pushed ballot branch (the root cause).
git -C "$town" fetch -q origin 2>/dev/null || true
tab=$(printf '\t')
total=0
counted=0
missing=0
for ref in $(git -C "$town" for-each-ref --format='%(refname)' "refs/remotes/origin/ballot/*-$bill"); do
    name=${ref#refs/remotes/origin/ballot/}
    seat=${name%-$bill}
    case "$seat" in ''|*[!0-9a-f]*) echo "ballot-completeness: unparsable branch $name" >&2; continue;; esac
    total=$((total + 1))
    if [ -f "$rec" ] && awk -F "$tab" -v s="$seat" '$1==s { f=1 } END { exit f ? 0 : 1 }' "$rec"; then
        counted=$((counted + 1))
    else
        missing=$((missing + 1))
        printf 'MISSING: %s (branch %s)\n' "$seat" "$ref"
    fi
done
printf 'ballot-completeness %s: origin_branches=%d counted=%d missing=%d\n' \
    "$bill" "$total" "$counted" "$missing"
[ "$missing" -eq 0 ]
