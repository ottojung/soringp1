#!/bin/sh
# Ensure host assignment cannot silently be reinterpreted as a ban on CI.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
grep -Fq 'GitHub Actions may run CI' "$repo/government/executive-agenda.md"
grep -Fq 'Never delete or disable working workflows' "$repo/government/executive-cycle.sh"
grep -Fq 'GitHub-hosted CI builds, tests and Lean verification' "$repo/government/sitting.sh"
grep -Fq 'GitHub-hosted CI' "$repo/government/audit-cycle.sh"
grep -Fq 'CI on GitHub-hosted runners' "$repo/government/OVERSIGHT.md"
grep -Fq 'not restrict GitHub' "$repo/records/FOUNDER-CI-HOST-CLARIFICATION-2026-10-16.md"
echo 'Host assignment and GitHub Actions CI policy smoke checks passed'
