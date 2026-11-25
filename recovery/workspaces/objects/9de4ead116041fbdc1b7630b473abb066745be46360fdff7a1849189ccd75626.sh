#!/bin/sh
# Clerk integration coverage is part of the real appointment/office fixture,
# not repeated sightings of a single failed invocation.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
/bin/sh "$repo/tests/appointment-recovery-integration-smoke.sh"
echo 'Viche Clerk liveness smoke passed (real appointment and safety gates)'
