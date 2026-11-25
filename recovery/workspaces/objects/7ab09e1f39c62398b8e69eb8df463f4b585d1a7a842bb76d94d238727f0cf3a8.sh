#!/bin/sh
# The end-to-end test supersedes the old synthetic observation-count fixture;
# it uses distinct invocation IDs and exercises supervisor, appointment,
# Clerk, seat and handoff recovery together.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
/bin/sh "$repo/tests/appointment-recovery-integration-smoke.sh"
echo 'Executive recovery timing checks passed (distinct invocation evidence)'
