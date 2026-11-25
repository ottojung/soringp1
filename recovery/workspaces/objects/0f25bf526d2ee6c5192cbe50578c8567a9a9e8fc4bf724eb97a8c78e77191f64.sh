#!/bin/sh
# Act 18 §7 — schedule regeneration of the generated board-trail index.
#
# The Executive SHALL maintain records/board-trail/index.json. Nothing else
# invoked the generator, so the index could silently go stale (observed
# 2026-10-21: index ~2 days old, missing #313/#314). This wrapper is invoked
# from government/boot.sh each cycle and throttles regeneration to a measurement
# window (default 3600 s) so the Founder-visible status map stays fresh without
# needless board load.
#
# Non-fatal: a board outage must never block boot. The generator retries each
# board call internally and records board_readable=false rather than fabricating
# a Git-only gap. POSIX /bin/sh only.
set -eu
town=${VICHE_TOWN_ROOT:-/var/lib/lubko/wd/viche}
state=${VICHE_STATE_ROOT:-/var/lib/lubko/wd/viche-state}
interval=${VICHE_BOARD_TRAIL_REFRESH_SECONDS:-3600}
case "$interval" in ''|*[!0-9]*) interval=3600;; esac
# Allow tests and hermetic callers to suppress the live board scan.
[ "${VICHE_BOARD_TRAIL_REFRESH:-1}" = 0 ] && exit 0
gen=$town/government/board-trail-index.py
[ -f "$gen" ] || exit 0
now=$(date +%s)
stampdir=$state/board-trail
stamp=$stampdir/last-refresh
mkdir -p "$stampdir"
if [ -s "$stamp" ]; then
    last=$(cat "$stamp")
    case "$last" in ''|*[!0-9]*) last=0;; esac
    [ $((now - last)) -ge "$interval" ] || exit 0
fi
if python3 "$gen"; then
    printf '%s\n' "$now" > "$stamp"
else
    echo "Viche: board-trail index regeneration failed; index may be stale" >&2
fi
exit 0
