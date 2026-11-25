#!/bin/sh
# Independent of Viche's parliamentary/executive/judicial cycle.
# This service only keeps a general-purpose AI recovery investigator available.
. /home/lubko/.profile
set -eu
export VICHE_TOWNHALL_ID=302
export VICHE_TOWN_ROOT=/var/lib/lubko/wd/viche
export VICHE_SEATS_ROOT=/var/lib/lubko/wd/viche-seats
export VICHE_STATE_ROOT=/var/lib/lubko/wd/viche-state
export VICHE_CONSTITUTION=/var/lib/lubko/from-host/viche-constitution/CONSTITUTION.md
trap 'exit 0' TERM INT
while :; do
  /bin/sh "$VICHE_TOWN_ROOT/government/recovery-steward-cycle.sh" ||
    echo 'Viche recovery steward launcher failed; independent supervisor will retry' >&2
  sleep 180 & wait "$!" || exit 0
done
