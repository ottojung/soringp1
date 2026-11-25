#!/bin/sh
# Real Act19 seat test, including three distinct managed invocation IDs,
# immutable worktree/appointment continuity and one supervisor reset.
# Old fixture wrongly counted repeated polling of one failed invocation.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
/bin/sh "$repo/tests/appointment-recovery-integration-smoke.sh"
echo 'Viche parliamentary seat liveness smoke passed'
