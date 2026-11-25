#!/bin/sh
# Hermetic delivery inventory/proposal tests; only a local bare Git remote.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
scratch=$(mktemp -d)
trap 'rm -rf "$scratch"' EXIT HUP INT TERM
town=$scratch/town
seats=$scratch/seats
state=$scratch/state
remote=$scratch/origin.git
mkdir -p "$town" "$seats" "$state"
git init --bare -q "$remote"
git -C "$town" init -q -b main
git -C "$town" config user.name Fixture
git -C "$town" config user.email fixture@example.invalid
git -C "$town" config commit.gpgsign false
git -C "$town" remote add origin "$remote"
mkdir -p "$town/tests" "$town/records"
printf 'Canonical policy\n' > "$town/AGENTS.md"
printf '#!/bin/sh\nexit 0\n' > "$town/tests/records-smoke.sh"
printf '#!/bin/sh\nexit 0\n' > "$town/tests/run-all.sh"
git -C "$town" add -A
git -C "$town" commit -qm 'baseline'
git -C "$town" push -q -u origin main
git -C "$town" fetch -q origin main

records=$seats/c1a00001
git -C "$town" worktree add -qb records-review "$records" main
mkdir -p "$records/records"
printf 'Independently reviewed audit evidence\n' > "$records/records/report.md"
git -C "$records" add -A
git -C "$records" commit -qm 'audit record'
python3 "$repo/government/delivery-candidates.py" --repo "$town" --seats "$seats" > "$scratch/candidates.json"
jq -e '.candidate_count==1 and .candidates[0].category=="records-review" and
  .candidates[0].ahead_main==1 and .candidates[0].unpublished_commits==1 and
  (.candidates[0].dirty | length)==0' "$scratch/candidates.json" >/dev/null

(cd "$records" && VICHE_TOWN_ROOT=$town VICHE_STATE_ROOT=$state \
  /bin/sh "$repo/government/propose-delivery.sh" audited-record) >/dev/null
test "$(git -C "$remote" rev-parse refs/heads/delivery/audited-record)" = "$(git -C "$records" rev-parse HEAD)"
test "$(wc -l < "$state/delivery/proposals.tsv")" -eq 1

# Local dirty edits cannot be hidden by an existing signed HEAD.
printf 'not-committed\n' > "$records/records/draft.md"
if (cd "$records" && VICHE_TOWN_ROOT=$town VICHE_STATE_ROOT=$state \
    /bin/sh "$repo/government/propose-delivery.sh" unsaved-record) >/dev/null 2>&1; then
  echo 'Dirty branch was proposed' >&2; exit 1
fi
if git -C "$remote" show-ref --verify --quiet refs/heads/delivery/unsaved-record; then
  echo 'Unexpected dirty delivery ref' >&2; exit 1
fi

legislative=$seats/c1a00002
git -C "$town" worktree add -qb bill-draft "$legislative" main
mkdir -p "$legislative/records/bills"
printf 'Draft only; NOT LAW\n' > "$legislative/records/bills/draft.md"
git -C "$legislative" add -A
git -C "$legislative" commit -qm draft
python3 "$repo/government/delivery-candidates.py" --repo "$town" --seats "$seats" > "$scratch/candidates.json"
jq -e '.candidates | any(.category=="legislative-review" and
  (.needs|contains("parliamentary authority")))' "$scratch/candidates.json" >/dev/null

policy=$seats/c1a00003
git -C "$town" worktree add -qb policy-only "$policy" main
printf 'policy synchronization only\n' > "$policy/AGENTS.md"
git -C "$policy" add -A
git -C "$policy" commit -qm policy
if (cd "$policy" && VICHE_TOWN_ROOT=$town VICHE_STATE_ROOT=$state \
    /bin/sh "$repo/government/propose-delivery.sh" useless-policy) >/dev/null 2>&1; then
  echo 'Policy-only changes were proposed' >&2; exit 1
fi

test -s "$repo/government/reviewed-merge.sh"
test ! -e "$repo/.github/workflows/delivery-pr.yml"
echo 'Delivery candidate inventory and guarded Git publication smoke passed'
