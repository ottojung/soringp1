#!/bin/sh
# Exact-commit reviewed Git delivery. No GitHub API or PR permission needed.
# A successful test or this script does not grant legislative authority.
set -eu
[ "$#" -ge 1 ] || { echo 'Usage: reviewed-merge.sh delivery/BRANCH [--publish --verified-by OFFICE --reviewed-by OFFICE --evidence REF]' >&2; exit 2; }
branch=$1; shift
case "$branch" in
    delivery/*) : ;;
    *) echo 'Only the review-delivery namespace may be integrated' >&2; exit 2 ;;
esac
case "$branch" in
    *[!a-zA-Z0-9_/-]*|*../*|*//*|'delivery/') exit 2 ;;
esac
publish=false
verified_by=
reviewed_by=
evidence=
while [ "$#" -gt 0 ]; do
    case "$1" in
        --publish) publish=true; shift ;;
        --verified-by) verified_by=$2; shift 2 ;;
        --reviewed-by) reviewed_by=$2; shift 2 ;;
        --evidence) evidence=$2; shift 2 ;;
        *) echo "Unknown option: $1" >&2; exit 2 ;;
    esac
done
if [ "$publish" = true ]; then
    [ -n "$verified_by" ] && [ -n "$reviewed_by" ] && [ -n "$evidence" ] ||
        { echo 'Publishing requires verification and independent review evidence' >&2; exit 2; }
    [ "$verified_by" != "$reviewed_by" ] ||
        { echo 'Reviewing office must be distinct from verifying office' >&2; exit 2; }
fi
repo=${VICHE_TOWN_ROOT:-/var/lib/lubko/wd/viche}
state=${VICHE_STATE_ROOT:-/var/lib/lubko/wd/viche-state}
mkdir -p "$state/delivery"
# Pin the intended pair of refs. A later main update makes the push fail
# naturally; a normal force-free Git push never replaces another office's work.
git -C "$repo" fetch -q origin \
    "+refs/heads/main:refs/remotes/origin/main" \
    "+refs/heads/$branch:refs/remotes/origin/$branch" ||
    { echo 'Cannot fetch canonical main and delivery ref' >&2; exit 1; }
base=$(git -C "$repo" rev-parse refs/remotes/origin/main)
target=$(git -C "$repo" rev-parse "refs/remotes/origin/$branch")
[ "$base" != "$target" ] || exit 1
files=$(git -C "$repo" diff --name-only "refs/remotes/origin/main...refs/remotes/origin/$branch")
[ -n "$files" ] || { echo 'No delivery delta' >&2; exit 1; }
substantive=$(printf '%s\n' "$files" | grep -vx AGENTS.md | grep -v '^$' || :)
[ -n "$substantive" ] || { echo 'Only policy synchronization; nothing to integrate' >&2; exit 1; }
suite=tests/records-smoke.sh
while IFS= read -r file; do
    case "$file" in
        constitution/*|records/ballots/*|records/bills/*|government/LAWS.md|government/seats.tsv)
            echo "Legislative/protected path requires separate enactment: $file" >&2
            exit 1 ;;
        AGENTS.md|records/*) : ;;
        *) suite=tests/run-all.sh ;;
    esac
done <<EOF
$files
EOF
scratch=$(mktemp -d "$state/delivery/merge.XXXXXXXX") || exit 1
cwd=$scratch/checkout
cleanup() {
    if [ -d "$cwd" ]; then
        git -C "$repo" worktree remove --force "$cwd" >/dev/null 2>&1 || :
    fi
    rm -rf "$scratch"
}
trap cleanup 0
trap 'exit 130' 1 2 3 15
git -C "$repo" worktree add --quiet --detach "$cwd" "$base"
if ! git -C "$cwd" merge --no-commit --no-ff "$target" > "$scratch/merge.log" 2>&1; then
    unmerged=$(git -C "$cwd" diff --name-only --diff-filter=U)
    [ "$unmerged" = AGENTS.md ] ||
        { echo 'Merge conflicts require independent substantive review:' >&2; cat "$scratch/merge.log" >&2; exit 1; }
    # Old worktree policy cannot supersede canonical Founder instructions.
    git -C "$cwd" checkout --ours -- AGENTS.md
    git -C "$cwd" add -- AGENTS.md
fi
# Even a clean automatic merge must not restore an obsolete policy.
git -C "$cwd" show refs/remotes/origin/main:AGENTS.md > "$cwd/AGENTS.md"
git -C "$cwd" add -- AGENTS.md
git -C "$cwd" diff --cached --check ||
    { echo 'Merge candidate has whitespace/conflict defects' >&2; exit 1; }
git -C "$cwd" commit -m "Integrate reviewed delivery $branch" > "$scratch/commit.log"
candidate=$(git -C "$cwd" rev-parse HEAD)
tree=$(git -C "$cwd" rev-parse HEAD^{tree})
VICHE_TOWN_ROOT="$cwd" /bin/sh "$cwd/government/suite-status.sh" \
    --commit "$candidate" --suite "$suite" > "$scratch/suite.log" 2>&1 ||
    { echo "Exact merge candidate $candidate failed $suite" >&2; tail -n 15 "$scratch/suite.log" >&2; exit 1; }
jq -e --arg sha "$candidate" --arg tree "$tree" \
    '.result=="green" and .commit==$sha and .tree==$tree and .incident==false' \
    "$cwd/records/suite-status.json" >/dev/null ||
    { echo 'Verifier did not attest the exact candidate/tree' >&2; exit 1; }
receipt="$state/delivery/verified-$candidate.json"
cp "$cwd/records/suite-status.json" "$receipt"
if [ "$publish" != true ]; then
    echo "CHECKED exact merge $candidate tree=$tree suite=$suite receipt=$receipt"
    echo 'Not pushed; verification alone is not review or enactment.'
    exit 0
fi
# Preflight the actual canonical checkout BEFORE pushing. Source-of-truth
# state can contain locally generated reports and untracked audit records even
# though the Git target branch is clean. A fast-forward would refuse these
# overlapping files AFTER our push, leaving main published but undeployed.
# Never delete, overwrite, or stash unreviewed canonical evidence to force it.
canonical_head=$(git -C "$repo" rev-parse HEAD)
[ "$canonical_head" = "$base" ] ||
    { echo 'Canonical checkout is not at fetched main; reconcile before publish' >&2; exit 1; }
changed=$(git -C "$repo" diff --name-only "$base" "$candidate")
while IFS= read -r path; do
    [ -n "$path" ] || continue
    if { [ -e "$repo/$path" ] || [ -L "$repo/$path" ]; } &&
       ! git -C "$repo" ls-files --error-unmatch -- "$path" >/dev/null 2>&1; then
        echo "Canonical untracked evidence overlaps the approved merge: $path" >&2
        echo 'Preserve and reconcile this evidence independently before publishing.' >&2
        exit 1
    fi
    if ! git -C "$repo" diff --quiet -- "$path" ||
       ! git -C "$repo" diff --cached --quiet -- "$path"; then
        echo "Canonical tracked local edits overlap the approved merge: $path" >&2
        exit 1
    fi
done <<EOF
$changed
EOF

# Caller must separately establish reviewer identity and legal scope; capture
# the attestation in durable host state without altering the verified tree.
printf '%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$(date -u +%FT%TZ)" "$branch" "$candidate" "$verified_by" "$reviewed_by" "$evidence" \
    >> "$state/delivery/review-authorizations.tsv"
git -C "$cwd" push origin "HEAD:refs/heads/main" ||
    { echo 'Non-fast-forward main; re-review a newly constructed merge' >&2; exit 1; }
# Append a separate post-publication chronology event for Judiciary review.
# This durable host record binds the observed publication time to the exact
# pre-push receipt; a receipt without this event cannot prove it preceded main.
published_at_ns=$(python3 -c 'import time; print(time.time_ns())')
receipt_sha=$(sha256sum "$receipt" | cut -d ' ' -f1)
publication="$state/delivery/published-$candidate.json"
publication_tmp=$(mktemp "$state/delivery/.published.XXXXXXXX")
printf '{"generated_by":"government/reviewed-merge.sh","commit":"%s","published_at_ns":%s,"receipt_sha256":"%s"}\n' \
    "$candidate" "$published_at_ns" "$receipt_sha" > "$publication_tmp"
mv -f "$publication_tmp" "$publication"
# Preserve pre-existing generated status; its newest exact receipt is produced
# by this verifier. No broad git reset or destructive worktree cleanup.
if [ -f "$repo/records/suite-status.json" ]; then
    cp "$repo/records/suite-status.json" "$state/delivery/suite-pre-$candidate.json"
fi
git -C "$repo" fetch -q origin main
git -C "$repo" merge --ff-only FETCH_HEAD ||
    { echo 'Published Git revision but canonical checkout needs reconciliation' >&2; exit 1; }
cp "$receipt" "$repo/records/suite-status.json"
echo "PUBLISHED signed candidate $candidate to main; exact gate $suite green; evidence=$receipt"
