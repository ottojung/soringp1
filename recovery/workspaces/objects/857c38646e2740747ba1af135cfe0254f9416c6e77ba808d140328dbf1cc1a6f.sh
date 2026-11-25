#!/bin/sh
# Act 21 §3 — durable suite-status record generator (POSIX /bin/sh; no Bash).
#
# The verifying office (the Clerk, Act 21 §2) runs the applicable test suite on
# the exact commit being merged and records the result, timestamp, commit SHA and
# tree hash. This script is the deterministic generator: it applies the §1
# flaky-red policy (a red blocks only after two CONSECUTIVE reds on the same
# commit), writes records/suite-status.json, and MUST NOT be hand-edited.
#
# Usage:
#   suite-status.sh [--suite PATH] [--commit REF] [--ci green|red|unavailable]
#
#   --suite   test suite to run (default tests/run-all.sh; use
#             tests/records-smoke.sh for a records/-only change, Act 21 §1)
#   --commit  commit ref to verify (default HEAD); its SHA and tree are recorded
#   --ci      the CI suite result on main, if known (default unavailable);
#             §3 reconciliation: a disagreement is recorded as an incident
#
# Exit status: 0 if the recorded result is green, 1 if red (a standing incident).
set -eu

town=${VICHE_TOWN_ROOT:-/var/lib/lubko/wd/viche}
suite=${SUITE_STATUS_SUITE:-tests/run-all.sh}
commit=${SUITE_STATUS_COMMIT:-HEAD}
ci=${SUITE_STATUS_CI:-unavailable}

usage() {
    echo "usage: suite-status.sh [--suite PATH] [--commit REF] [--ci green|red|unavailable]" >&2
}

while [ "$#" -gt 0 ]; do
    case "$1" in
        --suite) [ "$#" -ge 2 ] || { usage; exit 2; }; suite=$2; shift 2 ;;
        --commit) [ "$#" -ge 2 ] || { usage; exit 2; }; commit=$2; shift 2 ;;
        --ci) [ "$#" -ge 2 ] || { usage; exit 2; }; ci=$2; shift 2 ;;
        -h|--help) usage; exit 0 ;;
        *) usage; exit 2 ;;
    esac
done

case "$ci" in
    green|red|unavailable) : ;;
    *) echo "suite-status: invalid --ci value: $ci" >&2; exit 2 ;;
esac
case "$suite" in
    tests/*) : ;;
    *) echo "suite-status: suite must be a relative tests/ script" >&2; exit 2 ;;
esac
case "$suite" in
    *../*|*/../*|*//*) echo "suite-status: unsafe suite path" >&2; exit 2 ;;
esac

sha=$(git -C "$town" rev-parse --verify "$commit^{commit}" 2>/dev/null) || {
    echo "suite-status: cannot resolve commit: $commit" >&2; exit 2
}
tree=$(git -C "$town" rev-parse --verify "$commit^{tree}")

# Act 21 verifies the EXACT commit. A dirty or newer canonical checkout must
# never masquerade as the selected revision. Isolate both source and Git index
# in a temporary detached worktree. This checkout is never pushed or retained.
scratch=$(mktemp -d "${TMPDIR:-/tmp}/viche-suite.XXXXXXXX") || exit 2
checkout=$scratch/revision
cleanup() {
    if [ -d "$checkout" ]; then
        git -C "$town" worktree remove --force "$checkout" >/dev/null 2>&1 || :
    fi
    rm -rf "$scratch"
}
trap 'cleanup' 0
trap 'exit 130' 1 2 3 15
git -C "$town" worktree add --quiet --detach "$checkout" "$sha" ||
    { echo "suite-status: cannot create checkout for $sha" >&2; exit 2; }
[ -f "$checkout/$suite" ] ||
    { echo "suite-status: suite missing from verified commit: $sha" >&2; exit 2; }
[ "$(git -C "$checkout" rev-parse HEAD)" = "$sha" ] ||
    { echo "suite-status: checkout SHA mismatch" >&2; exit 2; }
[ "$(git -C "$checkout" rev-parse HEAD^{tree})" = "$tree" ] ||
    { echo "suite-status: checkout tree mismatch" >&2; exit 2; }

# Run each replay in that immutable source checkout; emit an exit code and an
# output digest. Flaky-red reruns use the SAME original source revision.
run_once() {
    out=$(cd "$checkout" && VICHE_TOWN_ROOT="$checkout" /bin/sh "$suite" 2>&1) && rc=0 || rc=$?
    hash=$(printf '%s' "$out" | sha256sum | cut -d ' ' -f1)
    printf '%s\t%s\n' "$rc" "$hash"
}

first=$(run_once)
rc1=$(printf '%s' "$first" | cut -f1)
h1=$(printf '%s' "$first" | cut -f2)
r1=red; [ "$rc1" -eq 0 ] && r1=green

if [ "$rc1" -eq 0 ]; then
    result=green
    runs="[{\"run\":1,\"result\":\"$r1\",\"exit\":$rc1,\"output_sha256\":\"$h1\"}]"
else
    second=$(run_once)
    rc2=$(printf '%s' "$second" | cut -f1)
    h2=$(printf '%s' "$second" | cut -f2)
    r2=red; [ "$rc2" -eq 0 ] && r2=green
    result=red
    [ "$rc2" -eq 0 ] && result=green
    runs="[{\"run\":1,\"result\":\"$r1\",\"exit\":$rc1,\"output_sha256\":\"$h1\"},{\"run\":2,\"result\":\"$r2\",\"exit\":$rc2,\"output_sha256\":\"$h2\"}]"
fi

main_sha=$(git -C "$town" rev-parse --verify refs/remotes/origin/main 2>/dev/null || echo "")

recon=unavailable
if [ "$ci" != unavailable ]; then
    recon=disagree
    [ "$ci" = "$result" ] && recon=agree
fi
incident=false
[ "$result" = red ] && incident=true
[ "$recon" = disagree ] && incident=true

now=$(date +%s)
iso=$(date -u +%FT%TZ)
out=$town/records/suite-status.json
mkdir -p "$town/records"
tmp=$(mktemp "$town/records/.suite-status.XXXXXX")
{
    printf '{\n'
    printf '  "generated_by": "government/suite-status.sh",\n'
    printf '  "act": 21,\n'
    printf '  "recorded_at": %s,\n' "$now"
    printf '  "recorded_iso": "%s",\n' "$iso"
    printf '  "suite": "%s",\n' "$suite"
    printf '  "commit": "%s",\n' "$sha"
    printf '  "tree": "%s",\n' "$tree"
    printf '  "main": "%s",\n' "$main_sha"
    printf '  "result": "%s",\n' "$result"
    printf '  "runs": %s,\n' "$runs"
    printf '  "ci_result": "%s",\n' "$ci"
    printf '  "ci_reconciliation": "%s",\n' "$recon"
    printf '  "incident": %s\n' "$incident"
    printf '}\n'
} > "$tmp"
mv -f "$tmp" "$out"
printf 'suite-status: %s on %s (tree %s) -> %s\n' "$result" "$sha" "$tree" "$out"
[ "$result" = green ] || exit 1
