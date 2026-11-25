#!/bin/sh
# Act 18 §7 — the generated index must be refreshed each measurement window.
# This tests the scheduler wrapper (government/board-trail-refresh.sh): it
# invokes the generator, throttles repeat runs, records a durable stamp, and is
# non-fatal on generator failure. Hermetic: stub generator, scratch town/state.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
scratch=$(mktemp -d)
trap 'rm -rf "$scratch"' EXIT HUP INT TERM
export SCRATCH=$scratch
town=$scratch/town
mkdir -p "$town/government" "$scratch/state"
cp "$repo/government/board-trail-refresh.sh" "$town/government/"
mark=$scratch/runs

# Stub generator: append a line, or fail when the failure flag is present.
cat > "$town/government/board-trail-index.py" <<'STUB'
import os
if os.path.exists(os.environ["SCRATCH"] + "/fail"):
    raise SystemExit(1)
with open(os.environ["SCRATCH"] + "/runs", "a") as fh:
    fh.write("run\n")
STUB

VICHE_TOWN_ROOT=$town
VICHE_STATE_ROOT=$scratch/state
export VICHE_TOWN_ROOT VICHE_STATE_ROOT

# 1. First run invokes the generator and writes a durable stamp.
/bin/sh "$town/government/board-trail-refresh.sh"
[ "$(wc -l < "$mark")" -eq 1 ]
[ -s "$scratch/state/board-trail/last-refresh" ]

# 2. A second run inside the window is throttled (generator not invoked).
/bin/sh "$town/government/board-trail-refresh.sh"
[ "$(wc -l < "$mark")" -eq 1 ]

# 3. A zero interval forces regeneration.
VICHE_BOARD_TRAIL_REFRESH_SECONDS=0
export VICHE_BOARD_TRAIL_REFRESH_SECONDS
/bin/sh "$town/government/board-trail-refresh.sh"
[ "$(wc -l < "$mark")" -eq 2 ]
unset VICHE_BOARD_TRAIL_REFRESH_SECONDS

# 4. A generator failure is non-fatal and does not advance the stamp.
stamp_before=$(cat "$scratch/state/board-trail/last-refresh")
: > "$scratch/fail"
VICHE_BOARD_TRAIL_REFRESH_SECONDS=0
export VICHE_BOARD_TRAIL_REFRESH_SECONDS
/bin/sh "$town/government/board-trail-refresh.sh"
[ "$(wc -l < "$mark")" -eq 2 ] # no new run
[ "$(cat "$scratch/state/board-trail/last-refresh")" = "$stamp_before" ]
rm -f "$scratch/fail"

# 5. An explicit disable suppresses the board scan entirely.
VICHE_BOARD_TRAIL_REFRESH=0
export VICHE_BOARD_TRAIL_REFRESH
/bin/sh "$town/government/board-trail-refresh.sh"
[ "$(wc -l < "$mark")" -eq 2 ]

echo 'Act 18 board-trail refresh smoke passed'
