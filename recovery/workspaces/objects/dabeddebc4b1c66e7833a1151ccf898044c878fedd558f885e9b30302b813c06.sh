#!/bin/sh
# Run every Viche test from one local or CI command.
set -eu
cd "$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)"

echo 'Checking shell syntax and constitutional roster'
/bin/sh -n constitution/*.sh government/*.sh tests/*.sh deploy/s6/viche/run deploy/s6/viche-intake/run
dash -n constitution/*.sh government/*.sh tests/*.sh deploy/s6/viche/run
! grep -Fiq 'sole permitted AI model' constitution/CONSTITUTION.md
# The founder removed Viche's model pin. Guard against accidental reintroduction
# anywhere in current law, source, scripts or operational documentation.
retired_model=$(printf '%s%s' long cat)
if grep -RiF "$retired_model" AGENTS.md README.md constitution government deploy; then
  echo 'Viche model pin regression in active policy/code' >&2; exit 1
fi
test -s government/seats.tsv
awk -F '\t' 'NF != 3 || $1 !~ /^[0-9a-f]+$/ { exit 1 }' government/seats.tsv
test "$(cut -f1 government/seats.tsv | sort -u | wc -l)" -eq "$(wc -l < government/seats.tsv)"

for script in tests/*-smoke.sh tests/ballot-integrity.sh; do
    printf '\nRunning %s\n' "$script"
    dash "$script"
done
echo 'All Viche tests passed'
