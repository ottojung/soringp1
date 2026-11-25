#!/bin/sh
# Hermetic check that BOTH existing offices receive the same durable dialogue.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
scratch=$(mktemp -d)
trap 'rm -rf "$scratch"' EXIT HUP INT TERM
mkdir -p "$scratch/bin" "$scratch/town/government" "$scratch/town/records" \
    "$scratch/state" "$scratch/seats/branches/innovation-office"
: > "$scratch/seats/branches/innovation-office/.git"
printf 'Founder charter fixture\n' > "$scratch/charter"
printf 'c1a00001\tClerk\tlegislature\nc1a00002\tExecutive\tlegislature\n' \
    > "$scratch/town/government/seats.tsv"
cat > "$scratch/town/government/LAWS.md" <<'LAWS'
## Act 25 — Executive Innovation Office Act (re-enacted in fixture)
LAWS
printf 'Founder reports policy fixture\n' \
    > "$scratch/town/government/AGENT-REPORTING-POLICY.md"
cp "$repo/government/INNOVATION-LEGISLATURE-DIALOGUE.md" "$scratch/town/government/"
cp "$repo/government/EXECUTIVE-INNOVATION.md" "$scratch/town/government/"
cat > "$scratch/town/government/branch-bootstrap.sh" <<'SH'
#!/bin/sh
exit 0
SH
cat > "$scratch/town/government/appointments.sh" <<'SH'
#!/bin/sh
printf 'test-agent-id\n'
SH
cat > "$scratch/town/government/terminal-continuity.sh" <<'SH'
#!/bin/sh
echo 'No recovery holds in fixture'
SH
cat > "$scratch/bin/antonina" <<'SH'
#!/bin/sh
set -eu
case "$1 $2" in
 "agent status") echo '{"state":"idle","alive":false}' ;;
 "agent run")
    printf '%s\n' "$@" > "$PROMPT_LOG"
    echo 'started' ;;
 *) echo "Unexpected command: $*" >&2; exit 1 ;;
esac
SH
chmod +x "$scratch/bin/antonina" "$scratch/town/government/"*.sh
PATH=$scratch/bin:$PATH
VICHE_TOWN_ROOT=$scratch/town
VICHE_STATE_ROOT=$scratch/state
VICHE_SEATS_ROOT=$scratch/seats
VICHE_CONSTITUTION=$scratch/charter
VICHE_TOWNHALL_ID=302
PROMPT_LOG=$scratch/invocation.txt
export PATH VICHE_TOWN_ROOT VICHE_STATE_ROOT VICHE_SEATS_ROOT VICHE_CONSTITUTION VICHE_TOWNHALL_ID PROMPT_LOG
/bin/sh "$repo/government/executive-innovation-cycle.sh"
grep -Fq 'GT2QzYsFG4t92DvJkE4Wuk-lodge' "$PROMPT_LOG"
grep -Fq 'parallel, orthogonal' "$PROMPT_LOG"
grep -Fq 'do NOT originate or sponsor' "$PROMPT_LOG"
grep -Fq 'current problems AND unrealized opportunities' "$PROMPT_LOG"
grep -Fq 'Judiciary independently investigates violations' "$PROMPT_LOG"
grep -Fq 'Executive implements only measures authorized' "$PROMPT_LOG"
jq -e '.controlled_by=="executive" and .quality_verified==false' \
    "$scratch/state/executive/innovation-office/health.json" >/dev/null
/bin/sh "$repo/government/sitting.sh" c1a00001 > "$scratch/clerk.txt"
grep -Fq 'GT2QzYsFG4t92DvJkE4Wuk-lodge' "$scratch/clerk.txt"
grep -Fq 'only voting members may' "$scratch/clerk.txt"
grep -Fq 'Neither a question nor a dialogue comment changes' "$scratch/clerk.txt"
/bin/sh "$repo/government/sitting.sh" c1a00002 > "$scratch/member.txt"
grep -Fq 'GT2QzYsFG4t92DvJkE4Wuk-lodge' "$scratch/member.txt"
# A law naming new Post offices is NOT evidence of independently accepted
# migration; the established two-way channel must still be visible.
printf '%s\n' '## Act 32 — Institutional Knowledge and Communications Act (enacted fixture)' \
    >> "$scratch/town/government/LAWS.md"
rm -f "$scratch/state/executive/innovation-office/last-dispatch"
 /bin/sh "$repo/government/executive-innovation-cycle.sh"
grep -Fq 'GT2QzYsFG4t92DvJkE4Wuk-lodge' "$PROMPT_LOG"
/bin/sh "$repo/government/sitting.sh" c1a00001 > "$scratch/enacted-clerk.txt"
grep -Fq 'GT2QzYsFG4t92DvJkE4Wuk-lodge' "$scratch/enacted-clerk.txt"
# Private/sensitive blockers must not be automatically rerouted to PUBLIC Post.
grep -Fq 'mailbox remains the operational path' \
    "$repo/government/AGENT-REPORTING-POLICY.md"
echo 'Innovation–Legislature dialogue survives knowledge-Act enactment; public Post cannot replace protected mailbox automatically'
