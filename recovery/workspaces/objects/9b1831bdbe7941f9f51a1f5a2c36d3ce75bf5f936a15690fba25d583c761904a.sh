#!/bin/sh
set -eu
interval=${VICHE_SENTINEL_INTERVAL_SECONDS:-3600}
case "$interval" in ''|*[!0-9]*|0) exit 2;; esac
dir=$(CDPATH= cd "$(dirname "$0")" && pwd -P)
trap 'exit 0' TERM INT
while :; do
  /bin/sh "$dir/check.sh" || echo 'Sentinel: check failed; will retry' >&2
  sleep "$interval" & wait "$!" || exit 0
done
