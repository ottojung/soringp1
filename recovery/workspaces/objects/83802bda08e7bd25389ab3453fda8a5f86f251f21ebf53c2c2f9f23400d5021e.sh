#!/bin/sh
# Hermetic reviewed-merge mechanics: exact commit, conservative policy,
# reviewer gate and signed/fast-forward Git delivery over local bare origin.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT HUP INT TERM
town=$tmp/town
remote=$tmp/origin.git
state=$tmp/state
mkdir -p "$town" "$state"
git init --bare -q "$remote"
git -C "$town" init -q -b main
git -C "$town" config user.name Fixture
git -C "$town" config user.email fixture@example.invalid
git -C "$town" config commit.gpgsign false
git -C "$town" remote add origin "$remote"
mkdir -p "$town/government" "$town/tests" "$town/records"
cp "$repo/government/suite-status.sh" "$town/government/suite-status.sh"
printf '#!/bin/sh\nexit 0\n' > "$town/tests/records-smoke.sh"
printf '#!/bin/sh\nexit 0\n' > "$town/tests/run-all.sh"
printf 'canonical v1\n' > "$town/AGENTS.md"
git -C "$town" add -A
git -C "$town" commit -qm 'main baseline'
git -C "$town" push -q -u origin main

jud=$tmp/judiciary
git -C "$town" worktree add -qb judiciary "$jud" main
mkdir -p "$jud/records"
printf 'withdrawn stale model policy\n' > "$jud/AGENTS.md"
printf 'Independent audit finding\n' > "$jud/records/judiciary.md"
git -C "$jud" add -A
git -C "$jud" commit -qm 'signed-looking independent report'
git -C "$jud" push -q origin HEAD:refs/heads/delivery/audit-fixture

# Concurrent canonical policy changes must win over the old branch snapshot.
printf 'canonical v2\n' > "$town/AGENTS.md"
git -C "$town" commit --only -qm 'latest founder policy' -- AGENTS.md
git -C "$town" push -q origin main
base=$(git -C "$town" rev-parse HEAD)
run() {
  VICHE_TOWN_ROOT=$town VICHE_STATE_ROOT=$state \
    /bin/sh "$repo/government/reviewed-merge.sh" "$@"
}

if run delivery/audit-fixture --publish >/dev/null 2>&1; then
  echo 'Published without explicit review evidence' >&2; exit 1
fi
run delivery/audit-fixture > "$tmp/review.txt"
grep -q 'CHECKED exact merge' "$tmp/review.txt"
test "$(git -C "$town" rev-parse HEAD)" = "$base"
test ! -f "$town/records/judiciary.md"

# A canonical untracked report colliding with the approved commit must be
# protected BEFORE publishing main; preserving it is more important than speed.
printf 'unreviewed canonical evidence\n' > "$town/records/judiciary.md"
if run delivery/audit-fixture --publish --verified-by clerk --reviewed-by judiciary \
    --evidence 'fixture:collision' > "$tmp/collision.log" 2>&1; then
  echo 'Published over untracked canonical evidence' >&2; exit 1
fi
test "$(cat "$town/records/judiciary.md")" = 'unreviewed canonical evidence'
test "$(git -C "$remote" rev-parse refs/heads/main)" = "$base"
test ! -s "$state/delivery/review-authorizations.tsv"
rm "$town/records/judiciary.md"

run delivery/audit-fixture --publish --verified-by clerk --reviewed-by judiciary \
  --evidence 'fixture:independent-check' > "$tmp/review.txt"
grep -q 'PUBLISHED signed candidate' "$tmp/review.txt"
test -f "$town/records/judiciary.md"
test "$(cat "$town/AGENTS.md")" = 'canonical v2'
test "$(git -C "$town" rev-parse HEAD)" = "$(git -C "$remote" rev-parse refs/heads/main)"
jq -e '.result=="green" and .incident==false' "$town/records/suite-status.json" >/dev/null
test -s "$state/delivery/review-authorizations.tsv"
published=$(git -C "$town" rev-parse HEAD)
test -s "$state/delivery/published-$published.json"
jq -e --arg sha "$published" \
  '.generated_by=="government/reviewed-merge.sh" and .commit==$sha and (.published_at_ns|type)=="number" and (.receipt_sha256|test("^[0-9a-f]{64}$"))' \
  "$state/delivery/published-$published.json" >/dev/null

# An authorized research branch cannot bypass the legislative law/ballot gate.
law=$tmp/law
git -C "$town" worktree add -qb draft "$law" main
mkdir -p "$law/records/bills"
printf 'This is a draft, not law\n' > "$law/records/bills/new-draft.md"
git -C "$law" add -A
git -C "$law" commit -qm 'unvoted draft'
git -C "$law" push -q origin HEAD:refs/heads/delivery/unvoted-draft
if run delivery/unvoted-draft >/dev/null 2>&1; then
  echo 'Accepted a bill through technical merge gate' >&2; exit 1
fi
echo 'Exact-merge preview, explicit approval and git publication smoke passed'
