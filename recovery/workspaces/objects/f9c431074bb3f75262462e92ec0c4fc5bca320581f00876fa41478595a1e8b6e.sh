#!/bin/sh
# Act 19 §3.1: worktree progress permanently breaks the earlier failure streak,
# even if the office later checks out a previously used commit.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
d=$(mktemp -d)
trap 'rm -rf "$d"' EXIT HUP INT TERM
mkdir -p "$d/work" "$d/state"
git -C "$d/work" init -q
git -C "$d/work" -c user.name=test -c user.email=test@example.test commit --allow-empty -qm head-A
head_a=$(git -C "$d/work" rev-parse HEAD)
. "$repo/government/office-continuity.sh"
oc_worktree=$d/work
base=$(date +%s)
now=$((base+10))

# Two failures at A are below threshold.
oc_record_failure "$d/state" executive agent-A run-A1 upstream_endpoint_unavailable "$((base+1))" yes "$now" "$d/work"
oc_record_failure "$d/state" executive agent-A run-A2 upstream_endpoint_unavailable "$((base+2))" yes "$now" "$d/work"
if oc_reset_due "$d/state" executive "$now"; then
  echo 'two failures must not reset' >&2; exit 1
fi

# A durable commit starts a new streak. One failure on B is only one failure.
git -C "$d/work" -c user.name=test -c user.email=test@example.test commit --allow-empty -qm head-B
head_b=$(git -C "$d/work" rev-parse HEAD)
oc_record_failure "$d/state" executive agent-B run-B1 upstream_endpoint_unavailable "$((base+3))" yes "$now" "$d/work"
if oc_reset_due "$d/state" executive "$now"; then
  echo 'progress must break the A-head streak' >&2; exit 1
fi

# Returning to A must not resurrect run-A1/run-A2. The first new A-head failure
# begins a fresh streak; two more distinct invocations then reach the threshold.
git -C "$d/work" checkout -q --detach "$head_a"
oc_record_failure "$d/state" executive agent-A2 run-A3 upstream_endpoint_unavailable "$((base+4))" yes "$now" "$d/work"
if oc_reset_due "$d/state" executive "$now"; then
  echo 'returning to an old HEAD resurrected its earlier failure streak' >&2; exit 1
fi
oc_record_failure "$d/state" executive agent-A2 run-A4 upstream_endpoint_unavailable "$((base+5))" yes "$now" "$d/work"
oc_record_failure "$d/state" executive agent-A2 run-A5 upstream_endpoint_unavailable "$((base+6))" yes "$now" "$d/work"
oc_reset_due "$d/state" executive "$now"

# The successful reset records an append-only sequence boundary.
oc_clear_failures "$d/state" executive
test "$(cat "$d/state/reset-sequence-executive")" -eq "$(wc -l < "$d/state/failures/events.tsv")"
if oc_reset_due "$d/state" executive "$now"; then
  echo 'a completed reset left its old events eligible' >&2; exit 1
fi
test "$head_b" != "$head_a"
echo 'Act 19 progress epoch survives return to an earlier Git HEAD'
