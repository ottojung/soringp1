#!/bin/sh
# Agents publish signed, locally-tested branches for independent review
# without GitHub API tokens or PR creation permissions.
# This script NEVER merges, enacts laws, edits ballots or changes the charter.
#
#   propose-delivery.sh --office OFFICE SHORT-SLUG
#
# OFFICE is who proposes (your seat id, or clerk, executive, judiciary, economy,
# innovation-office, recovery-steward). The integration queue (Act 31,
# government/integrator.py) lands it: additive records at once, anything else
# after an independent review it arranges itself. Watch the outcome with
# `python3 government/integrator.py office OFFICE`.
set -eu
office=
slug=
while [ "$#" -gt 0 ]; do
    case "$1" in
        --office) [ "$#" -ge 2 ] || exit 2; office=$2; shift 2 ;;
        -*) echo "unknown option: $1" >&2; exit 2 ;;
        *) [ -z "$slug" ] || { echo 'one slug only' >&2; exit 2; }; slug=$1; shift ;;
    esac
done
[ -n "$slug" ] && [ -n "$office" ] ||
    { echo 'Usage: propose-delivery.sh --office OFFICE SHORT-SLUG' >&2; exit 2; }
printf '%s' "$office" | grep -Eqx '[a-z0-9][a-z0-9-]{0,63}' ||
    { echo 'OFFICE is lowercase letters, digits and hyphens' >&2; exit 2; }
case "$slug" in
    ''|*[!a-z0-9-]*) echo 'Expected a lowercase alphanumeric/hyphen slug' >&2; exit 2 ;;
esac
repo=${VICHE_TOWN_ROOT:-/var/lib/lubko/wd/viche}
state=${VICHE_STATE_ROOT:-/var/lib/lubko/wd/viche-state}
cwd=$(pwd -P)
[ "$cwd" != "$repo" ] || { echo 'Do not propose main itself' >&2; exit 2; }
git -C "$repo" worktree list --porcelain | grep -Fxq "worktree $cwd" ||
    { echo 'Only a registered Viche worktree can publish a delivery' >&2; exit 2; }
[ -z "$(git -C "$cwd" status --porcelain)" ] ||
    { echo 'Commit or intentionally discard local changes before proposing' >&2; exit 1; }
branch=$(git -C "$cwd" symbolic-ref --short HEAD) ||
    { echo 'Detached HEAD cannot propose delivery' >&2; exit 1; }
[ "$branch" != main ] || exit 1
head=$(git -C "$cwd" rev-parse HEAD)
tree=$(git -C "$cwd" rev-parse HEAD^{tree})
# Reconcile remote main without changing any worktree or merging changes.
git -C "$repo" fetch -q origin main ||
    { echo 'Cannot verify current upstream main' >&2; exit 1; }
if git -C "$cwd" merge-base --is-ancestor "$head" refs/remotes/origin/main; then
    echo 'Nothing unpublished: this commit is already on main' >&2
    exit 1
fi
files=$(git -C "$cwd" diff --name-only refs/remotes/origin/main...HEAD)
substantive=$(printf '%s\n' "$files" | grep -v -x 'AGENTS.md' | grep -v '^$' || :)
[ -n "$substantive" ] ||
    { echo 'Refusing a proposal containing only synchronized instructions' >&2; exit 1; }
suite=tests/records-smoke.sh
if printf '%s\n' "$substantive" | grep -Eq '^(government/|tests/|constitution/|deploy/|\.github/)'; then
    suite=tests/run-all.sh
fi
[ -s "$cwd/$suite" ] || { echo "Missing applicable suite: $suite" >&2; exit 1; }
# Source is clean at the exact HEAD verified above. CI on the proposed
# ref is a second check, not an Act 21 substitute.
if ! (cd "$cwd" && /bin/sh "$suite" > /dev/null); then
    echo "Verification failed on $head: $suite" >&2; exit 1
fi
[ "$(git -C "$cwd" rev-parse HEAD)" = "$head" ] &&
[ -z "$(git -C "$cwd" status --porcelain)" ] ||
    { echo 'Worktree changed during verification; refusing to publish' >&2; exit 1; }

target=refs/heads/delivery/$slug
git -C "$cwd" push origin "HEAD:$target" ||
    { echo "Push to $target failed; no force push was attempted" >&2; exit 1; }
mkdir -p "$state/delivery"
printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$(date -u +%FT%TZ)" "$branch" "$target" "$head" "$tree" "$suite" "$office" \
    >> "$state/delivery/proposals.tsv"
printf 'Proposed %s at %s for %s with green %s.\n' "$target" "$head" "$office" "$suite"
printf 'Comparison: https://github.com/ottojung/viche/compare/main...delivery/%s\n' "$slug"
printf 'The integration queue lands it (Act 31); nothing else is needed from you.\n'
printf 'Outcome: python3 %s/government/integrator.py office %s\n' "$repo" "$office"
