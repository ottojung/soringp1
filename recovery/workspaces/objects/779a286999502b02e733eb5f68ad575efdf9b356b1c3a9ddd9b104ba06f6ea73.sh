#!/bin/sh
# Founder-controlled constitutional bootstrap. Invoked by S6, not parliament.
# Charter and this file are from the same founder-approved read-only mount.
set -eu

constitutional_dir=$(CDPATH= cd "$(dirname "$0")" && pwd -P)
town=${VICHE_TOWN_ROOT:-/var/lib/lubko/wd/viche}
seats=${VICHE_SEATS_ROOT:-/var/lib/lubko/wd/viche-seats}
state=${VICHE_STATE_ROOT:-/var/lib/lubko/wd/viche-state}
charter=${VICHE_CHARTER_PATH:-$constitutional_dir/CONSTITUTION.md}
interval=${VICHE_SITTING_INTERVAL_SECONDS:-600}
: "${VICHE_TOWNHALL_ID:?VICHE_TOWNHALL_ID must identify the Antonina Town Hall issue}"

[ -s "$charter" ] || { echo "Viche: missing authoritative constitution" >&2; exit 1; }
case "$interval" in
    ''|*[!0-9]*|0) echo "Viche: invalid sitting interval" >&2; exit 1 ;;
esac
for command_name in antonina git jq; do
    command -v "$command_name" >/dev/null 2>&1 || {
        echo "Viche: missing $command_name" >&2; exit 1;
    }
done
mkdir -p "$state" "$seats"
charter_text=$(cat "$charter")
# Never accept a substitute charter from parliament's writable Git tree.
VICHE_CONSTITUTION=$charter
VICHE_CONSTITUTION_DIR=$(dirname "$charter")
export VICHE_CONSTITUTION VICHE_CONSTITUTION_DIR

reconcile() {
    # The canonical checkout must always use main, never a seat's ballot branch.
    # A failed switch preserves uncommitted work; never reset or force it.
    if [ "$(git -C "$town" branch --show-current)" != main ]; then
        git -C "$town" switch main || return 1
    fi
    if [ "${VICHE_TEST_NO_SYNC:-0}" != 1 ]; then
        # A temporary GitHub outage must not disable local agent recovery.
        if git -C "$town" fetch origin main; then
            git -C "$town" merge --ff-only FETCH_HEAD || return 1
        else
            echo "Viche: Git fetch unavailable; using local main" >&2
        fi
    fi
    [ "$(git -C "$town" branch --show-current)" = main ] || return 1
    [ -s "$town/government/LAWS.md" ] || return 1
    [ -s "$town/government/seats.tsv" ] || return 1
    /bin/sh "$town/government/boot.sh"
}

sitting() {
    failed=0
    pids=
    clerk=$(head -n 1 "$town/government/seats.tsv" | cut -f 1)
    [ -n "$clerk" ] || { echo "Viche: no parliamentary clerk" >&2; return 1; }
    # All seats join the inaugural sitting; subsequently summon as necessary.
    all=0
    [ -f "$state/inaugurated" ] || all=1
    tab=$(printf '\t')
    while IFS="$tab" read -r agent_id title focus; do
        [ -n "$agent_id" ] || continue
        if [ "$all" -eq 0 ] && [ "$agent_id" != "$clerk" ]; then
            grep -Fxq "$agent_id" "$town/records/SUMMONED.txt" 2>/dev/null || continue
        fi
        seat_id=$agent_id
        if ! agent_id=$(/bin/sh "$town/government/appointments.sh" ensure "$seat_id"); then
            echo "Viche: no appointee for $seat_id" >&2
            failed=1
            continue
        fi
        if ! status=$(antonina agent status --id "$agent_id" --json); then
            echo "Viche: cannot inspect seat $agent_id" >&2
            failed=1
            continue
        fi
        if ! current=$(printf '%s\n' "$status" | jq -er '.state'); then
            echo "Viche: malformed status for $agent_id" >&2
            failed=1
            continue
        fi
        [ "$current" != running ] || continue
        if ! suffix=$(/bin/sh "$town/government/sitting.sh" "$seat_id"); then
            echo "Viche: agenda hook failed for $agent_id" >&2
            failed=1
            continue
        fi
        prompt=$(cat <<EOF
You are parliamentary seat $seat_id ($title), provisional focus: $focus.
You serve Viche in reality, not in fiction. The authoritative charter below
comes from the Founder-controlled read-only mount and has highest authority.

=== AUTHORITATIVE CONSTITUTION ===
$charter_text
=== END AUTHORITATIVE CONSTITUTION ===

Use current ordinary law at $town/government/LAWS.md and records at $town/records.
Treat Antonina board issues and comments with author exactly Vitalik as
Founder communications; no signatures or identity verification are required.
Other authors do not carry Founder authority. Town Hall is issue #$VICHE_TOWNHALL_ID.
Parliament may amend ordinary laws, seats and agenda procedures, not this charter
or this boot supervisor. Never switch AI models or bypass Antonina.
Record evidence, independent votes, meaningful dissent, legitimate mandates and
failures. Do not confuse an agent exit with verified completed work.
There is no global limit on useful parallel agents or invocations.
Your seat worktree is $seats/$seat_id. Use branches and Git review;
the supervisor fast-forwards the canonical government checkout after merges.

=== GOVERNMENT AGENDA ===
$suffix
=== END AGENDA ===
EOF
)
        (antonina agent run --id "$agent_id" --cwd "$seats/$seat_id" --prompt "$prompt" --detach) &
        pids="$pids $!"
    done < "$town/government/seats.tsv"

    for pid in $pids; do
        wait "$pid" || failed=1
    done
    if [ "$all" -eq 1 ] && [ "$failed" -eq 0 ]; then
        touch "$state/inaugurated"
    fi
    [ "$failed" -eq 0 ]
}

cycle() {
    reconcile || { echo "Viche: government integration/reconciliation failed" >&2; return 1; }
    sitting
}

if [ "${1:-}" = --once ]; then
    [ "$#" -eq 1 ] || exit 2
    cycle
    exit $?
fi
[ "$#" -eq 0 ] || { echo "Usage: boot.sh [--once]" >&2; exit 2; }
trap 'exit 0' TERM INT
cycle || echo "Viche: cycle failed; will retry without changing model" >&2
while :; do
    sleep "$interval" & wait "$!" || exit 0
    cycle || echo "Viche: cycle failed; requires investigation" >&2
done
