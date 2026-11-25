#!/bin/sh
# Parliament-editable seat reconciliation; invoked by the protected S6 boot.
# No separate scheduler or direct model calls.
set -eu

town=${VICHE_TOWN_ROOT:-/var/lib/lubko/wd/viche}
seats=${VICHE_SEATS_ROOT:-/var/lib/lubko/wd/viche-seats}
[ -s "$town/government/LAWS.md" ] || exit 1
[ -s "$town/government/seats.tsv" ] || exit 1
command -v antonina >/dev/null 2>&1
mkdir -p "$seats"
git -C "$town" rev-parse --is-inside-work-tree >/dev/null

ids=$(mktemp)
trap 'rm -f "$ids"' EXIT HUP INT TERM
tab=$(printf '\t')
while IFS="$tab" read -r seat_id title focus; do
    [ -n "$seat_id" ] || continue
    case "$seat_id" in
        *[!0123456789abcdef]*|'') echo "Invalid seat ID: $seat_id" >&2; exit 1 ;;
    esac
    [ -n "$title" ] && [ -n "$focus" ] || {
        echo "Incomplete seat: $seat_id" >&2; exit 1;
    }
    printf '%s\n' "$seat_id" >> "$ids"
done < "$town/government/seats.tsv"

[ -s "$ids" ] || { echo "No parliamentary seats" >&2; exit 1; }
unique=$(sort -u "$ids" | wc -l)
total=$(wc -l < "$ids")
[ "$unique" -eq "$total" ] || { echo "Duplicate seat IDs" >&2; exit 1; }

while IFS="$tab" read -r seat_id title focus; do
    [ -n "$seat_id" ] || continue
    seat_dir=$seats/$seat_id
    if [ ! -f "$seat_dir/.git" ] && [ ! -d "$seat_dir/.git" ]; then
        if [ -d "$seat_dir" ] && [ -n "$(ls -A "$seat_dir")" ]; then
            echo "Refusing to replace seat directory: $seat_dir" >&2
            exit 1
        fi
        git -C "$town" worktree add --detach "$seat_dir" HEAD
    fi
    # All seats have durable, independently recoverable sessions; don't let a
    # failed provider continuation permanently remove a future voter.
    if [ -f "$town/government/seat-liveness.sh" ]; then
        /bin/sh "$town/government/seat-liveness.sh" "$seat_id" ||
            echo "Viche: seat $seat_id recovery failed" >&2
    fi
done < "$town/government/seats.tsv"

# Three independent branches: readiness is checked separately and durably.
# The protected constitutional boot still owns parliamentary sittings.
# A branch failure never suppresses another branch's reconciliation.
if [ -f "$town/government/branch-liveness.sh" ]; then
    /bin/sh "$town/government/branch-liveness.sh" legislature ||
        echo "Viche: Legislature liveness investigation required" >&2
fi

# Janitor Office: observe disk health each cycle; safe reclamation is self-throttled and
# non-fatal so it can never block seat reconciliation. Authority and safeguards:
# records/bills/janitor-office-act.md (Act 12); observation is within Act 4.2.
if [ -f "$town/government/janitor.sh" ]; then
    # A whole-box inventory can take minutes. It has its own exclusive lock;
    # never block legislative, executive or judicial dispatch behind it.
    janitor_state=${VICHE_STATE_ROOT:-/var/lib/lubko/wd/viche-state}/janitor
    mkdir -p "$janitor_state"
    (
        /bin/sh "$town/government/janitor.sh" cycle ||
            echo "Viche: janitor cycle failed; see janitor action log" >&2
    ) >> "$janitor_state/boot-cycle.log" 2>&1 < /dev/null &
fi

# Independent Executive: no parliamentary summons required.
if [ -f "$town/government/branch-liveness.sh" ]; then
    /bin/sh "$town/government/branch-liveness.sh" executive ||
        echo "Viche: Executive liveness investigation required" >&2
fi

# The innovation office is an Executive unit ONLY after parliamentary enactment.
if grep -Eq '^## Act [0-9]+ — Executive Innovation Office Act \(enacted ' "$town/government/LAWS.md"; then
    /bin/sh "$town/government/executive-innovation-cycle.sh" ||
        echo "Viche: Executive Innovation Office needs recovery" >&2
fi

# Deterministic oversight continues even when every AI session is unavailable.
# Failure of telemetry/auditing must not prevent unrelated reconciliation.
if [ -f "$town/government/oversight-watch.sh" ]; then
    /bin/sh "$town/government/oversight-watch.sh" ||
        echo "Viche: watchdog cycle failed; investigate monitoring coverage" >&2
fi
# Independent feedback never holds up legislature, executive, or judiciary.
# Serialize collectors, bound their runtime, and timestamp their evidence.
if [ -f "$town/government/outcome-metrics.py" ]; then
    metrics_state=${VICHE_STATE_ROOT:-/var/lib/lubko/wd/viche-state}/institutional-outcomes
    mkdir -p "$metrics_state"
    (
        flock -n 9 || exit 0
        timeout 150 python3 "$town/government/outcome-metrics.py" ||
            echo "Viche: outcome feedback unavailable; do not infer success" >&2
    ) 9>"$metrics_state/collector.lock"       >>"$metrics_state/collector.log" 2>&1 < /dev/null &
fi

# Independent Judiciary: evidence and adjudication, not executive delivery,
# proposing bills, or modifying its own measurement rules.
if [ -f "$town/government/branch-liveness.sh" ]; then
    /bin/sh "$town/government/branch-liveness.sh" judiciary ||
        echo "Viche: Judiciary liveness investigation required" >&2
fi
# Run the historic legislative Centre ONLY until lawful transfer.
if ! grep -Eq '^## Act [0-9]+ — Executive Innovation Office Act \(enacted ' "$town/government/LAWS.md"; then
    if [ -f "$town/government/innovation-centre-cycle.sh" ]; then
        /bin/sh "$town/government/innovation-centre-cycle.sh" ||
            echo "Viche: legislative Innovation Centre failed; investigate" >&2
    fi
fi
if [ -f "$town/government/branch-health.sh" ]; then
    /bin/sh "$town/government/branch-health.sh" ||
        echo "Viche: independent branch readiness incident recorded" >&2
fi
# Durable independent case routing persists even if every branch model fails.
if [ -f "$town/government/institutional-cases.py" ]; then
    python3 "$town/government/institutional-cases.py" reconcile ||
        echo "Viche: corrective-case recording failed; investigate" >&2
fi
# Act 18 §7: the Executive maintains the generated board-trail index; refresh it
# each measurement window (throttled, non-fatal) so the Founder-visible status
# map cannot silently go stale. Runs before the §5 lens that consumes it.
if [ -f "$town/government/board-trail-refresh.sh" ]; then
    /bin/sh "$town/government/board-trail-refresh.sh" ||
        echo "Viche: board-trail refresh failed" >&2
fi
if [ -f "$town/government/judiciary-measurements.py" ]; then
    python3 "$town/government/judiciary-measurements.py" ||
        echo "Viche: Judiciary self-measurement unavailable" >&2
fi

# Government setup completed; not proof of delivery.
state=${VICHE_STATE_ROOT:-/var/lib/lubko/wd/viche-state}/health
mkdir -p "$state"
date +%s > "$state/government-setup.last"
