#!/bin/sh
# Repeated observing of one failure is not N failures or N unsafe holds.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT HUP INT TERM
. "$repo/government/office-continuity.sh"
mkdir -p "$tmp/liveness"
oc_mark_unsafe_hold "$tmp/liveness" executive agent-1 run-1
oc_mark_unsafe_hold "$tmp/liveness" executive agent-1 run-1
[ "$(wc -l < "$tmp/liveness/unsafe-holds/executive")" -eq 1 ]
oc_mark_unsafe_hold "$tmp/liveness" executive agent-1 run-2
[ "$(wc -l < "$tmp/liveness/unsafe-holds/executive")" -eq 2 ]
oc_surface_permanent "$tmp/liveness" agent-1 ""
oc_surface_permanent "$tmp/liveness" agent-1 ""
grep -Fq 'unclassified_failure classification=missing_backend_classification' \
 "$tmp/liveness/permanent-incidents.log"
if grep -Fq 'permanent_failure classification=missing_backend_classification' "$tmp/liveness/permanent-incidents.log"; then
 echo 'Missing classification was fabricated as permanent' >&2; exit 1
fi
[ "$(wc -l < "$tmp/liveness/permanent-incidents.log")" -eq 1 ]
oc_surface_permanent "$tmp/liveness" agent-2 invalid_api_key
oc_surface_permanent "$tmp/liveness" agent-2 invalid_api_key
[ "$(wc -l < "$tmp/liveness/permanent-incidents.log")" -eq 2 ]
grep -Fq 'permanent_failure classification=invalid_api_key' \
 "$tmp/liveness/permanent-incidents.log"
# If the append-only incident log is lost before durable publication, no
# stale auxiliary marker may prevent a later observation from reporting it.
cp "$tmp/liveness/permanent-incidents.log" "$tmp/previous-log"
: > "$tmp/liveness/permanent-incidents.log"
oc_surface_permanent "$tmp/liveness" agent-2 invalid_api_key
[ "$(wc -l < "$tmp/liveness/permanent-incidents.log")" -eq 1 ]
echo 'Idempotent holds and honest incident classifications smoke passed'
