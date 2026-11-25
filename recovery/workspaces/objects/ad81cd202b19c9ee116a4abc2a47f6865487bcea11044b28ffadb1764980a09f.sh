#!/bin/sh
# Independent high-priority Founder intake loop; normal parliamentary sitting cadence is unchanged.
set -eu
interval=${VICHE_FOUNDER_POLL_SECONDS:-60}
case "$interval" in ''|*[!0-9]*|0) exit 2;; esac
: "${VICHE_TOWNHALL_ID:?Set Town Hall ID}"
town=${VICHE_TOWN_ROOT:-/var/lib/lubko/wd/viche}
trap 'exit 0' TERM INT
while :; do
  /bin/sh "$town/government/founder-intake.sh" || echo 'Viche: Founder intake failed; will retry without dropping events' >&2
  sleep "$interval" & wait "$!" || exit 0
done
