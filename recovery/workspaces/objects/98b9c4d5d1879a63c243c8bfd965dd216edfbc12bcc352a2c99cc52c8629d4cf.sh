#!/bin/sh
# A stale seat receives current instructions without losing unrelated work.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
scratch=$(mktemp -d)
trap 'rm -rf "$scratch"' EXIT HUP INT TERM
town=$scratch/town
seat=$scratch/seat
mkdir -p "$town" "$scratch/state"
git init -q -b main "$town"
git -C "$town" config user.name Fixture
git -C "$town" config user.email fixture@example.invalid
git -C "$town" config commit.gpgsign false
printf 'Old instructions\n' > "$town/AGENTS.md"
git -C "$town" add AGENTS.md
git -C "$town" commit -qm initial
git -C "$town" worktree add -qb stale "$seat"
printf 'Current founder instructions\n' > "$town/AGENTS.md"
git -C "$town" commit --only -qm current -- AGENTS.md

# Other staged and untracked work must survive signed/local policy commits.
printf 'independent staged work\n' > "$seat/notes"
git -C "$seat" add notes
printf 'independent untracked work\n' > "$seat/free-note"
VICHE_TOWN_ROOT=$town VICHE_STATE_ROOT=$scratch/state \
  /bin/sh "$repo/government/policy-sync.sh" "$seat"
cmp "$town/AGENTS.md" "$seat/AGENTS.md"
test "$(git -C "$seat" show HEAD:AGENTS.md)" = 'Current founder instructions'
test "$(git -C "$seat" diff --cached --name-only)" = notes
test "$(cat "$seat/free-note")" = 'independent untracked work'
old=$(git -C "$seat" rev-parse HEAD)
VICHE_TOWN_ROOT=$town VICHE_STATE_ROOT=$scratch/state \
  /bin/sh "$repo/government/policy-sync.sh" "$seat"
test "$(git -C "$seat" rev-parse HEAD)" = "$old"

# Refuse to clobber genuine edits to the agent's policy draft.
printf 'Newer founder instructions\n' > "$town/AGENTS.md"
git -C "$town" commit --only -qm newest -- AGENTS.md
printf 'Agent local edit\n' > "$seat/AGENTS.md"
if VICHE_TOWN_ROOT=$town VICHE_STATE_ROOT=$scratch/state \
  /bin/sh "$repo/government/policy-sync.sh" "$seat" >/dev/null 2>&1; then
  echo 'Overwrote dirty instructions' >&2
  exit 1
fi
test "$(cat "$seat/AGENTS.md")" = 'Agent local edit'
test "$(git -C "$seat" rev-parse HEAD)" = "$old"

# Reject unregistered/cloned directories even if they contain AGENTS.md.
mkdir -p "$scratch/unregistered"
printf 'Legacy\n' > "$scratch/unregistered/AGENTS.md"
if VICHE_TOWN_ROOT=$town VICHE_STATE_ROOT=$scratch/state \
  /bin/sh "$repo/government/policy-sync.sh" "$scratch/unregistered" >/dev/null 2>&1; then
  echo 'Accepted an unmanaged worktree' >&2
  exit 1
fi
echo 'Canonical policy freshness and non-destructive synchronization smoke passed'
