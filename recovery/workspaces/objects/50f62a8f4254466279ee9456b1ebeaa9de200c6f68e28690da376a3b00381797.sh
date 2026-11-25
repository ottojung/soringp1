#!/bin/sh
# Record an independent verdict on one exact delivery commit (Act 31).
#
#   review-delivery.sh delivery/SLUG HEAD approve|reject --office OFFICE --reason TEXT
#
# The integrator lands a delivery that needs review only after an approval of
# that exact HEAD by an office other than the one that proposed it; a later
# reject replaces an earlier approve. The office name is an assertion recorded
# for audit, as reviewer identities always were (government/DELIVERY.md).
set -eu
[ "$#" -ge 3 ] || { echo 'usage: review-delivery.sh delivery/SLUG HEAD approve|reject --office OFFICE --reason TEXT' >&2; exit 2; }
branch=$1 head=$2 verdict=$3
shift 3
office= reason=
while [ "$#" -gt 0 ]; do
    case "$1" in
        --office) [ "$#" -ge 2 ] || exit 2; office=$2; shift 2 ;;
        --reason) [ "$#" -ge 2 ] || exit 2; reason=$2; shift 2 ;;
        *) echo "unknown option: $1" >&2; exit 2 ;;
    esac
done
case "$branch" in
    delivery/*) : ;;
    *) echo 'only delivery/ branches are reviewed' >&2; exit 2 ;;
esac
case "${branch#delivery/}" in ''|*[!a-z0-9-]*) echo 'bad delivery branch' >&2; exit 2 ;; esac
printf '%s' "$head" | grep -Eqx '[0-9a-f]{40}' || { echo 'HEAD must be a full 40-hex commit id' >&2; exit 2; }
case "$verdict" in approve|reject) : ;; *) echo 'verdict is approve or reject' >&2; exit 2 ;; esac
printf '%s' "$office" | grep -Eqx '[a-z0-9][a-z0-9-]{0,63}' || { echo 'need --office NAME (lowercase, digits, hyphens)' >&2; exit 2; }
[ -n "$(printf '%s' "$reason" | tr -d '[:space:]')" ] || { echo 'need --reason' >&2; exit 2; }
state=${VICHE_STATE_ROOT:-/var/lib/lubko/wd/viche-state}
mkdir -p "$state/delivery"
jq -nc --arg at "$(date -u +%FT%TZ)" --arg branch "$branch" --arg head "$head" \
    --arg verdict "$verdict" --arg office "$office" --arg reason "$reason" \
    '{at:$at,branch:$branch,head:$head,verdict:$verdict,office:$office,reason:$reason}' \
    >> "$state/delivery/reviews.jsonl"
echo "Recorded: $office $verdict $branch@$head. The integrator acts on it within a cycle."
