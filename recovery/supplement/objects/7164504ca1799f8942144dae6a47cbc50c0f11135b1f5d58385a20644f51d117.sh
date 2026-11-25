#!/bin/sh
# Mission-specific read-only status, consumed by generic government interface.
set -eu
here=$(CDPATH= cd "$(dirname "$0")" && pwd -P)
exec python3 "$here/frontier-status.py"
