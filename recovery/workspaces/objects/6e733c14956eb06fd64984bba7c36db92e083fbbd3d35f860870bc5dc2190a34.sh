#!/bin/sh
set -eu
root=$(CDPATH= cd -- "$(dirname "$0")/.." && pwd -P)
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT HUP INT TERM
git -C "$tmp" init -q -b main
git -C "$tmp" config user.name test
git -C "$tmp" config user.email test@example.invalid
mkdir -p "$tmp/government" "$tmp/tests" "$tmp/records"
run_hash=$(printf 'fixture output\n' | sha256sum | cut -d ' ' -f1)
export VICHE_STATE_ROOT=$tmp/state
mkdir -p "$VICHE_STATE_ROOT/delivery"
write_publication() {
    commit=$1 published_at=$2 receipt=$3
    digest=$(sha256sum "$receipt" | cut -d ' ' -f1)
    published_at_ns=$((published_at * 1000000000))
    printf '{"generated_by":"government/reviewed-merge.sh","commit":"%s","published_at_ns":%s,"receipt_sha256":"%s"}\n' \
        "$commit" "$published_at_ns" "$digest" > "$VICHE_STATE_ROOT/delivery/published-$commit.json"
}
printf 'fixture\n' > "$tmp/government/base"
git -C "$tmp" add . && git -C "$tmp" commit -qm base
base=$(git -C "$tmp" rev-parse HEAD)
# Record a green verification of main, then introduce a change. The record
# precedes the change but its tree necessarily differs from the resulting tree.
main_base=$(git -C "$tmp" rev-parse HEAD)
base_tree=$(git -C "$tmp" rev-parse HEAD^{tree})
printf '{"generated_by":"government/suite-status.sh","suite":"tests/run-all.sh","result":"green","commit":"%s","tree":"%s","runs":[{"run":1,"result":"green","exit":0,"output_sha256":"%s"}]}\n' "$main_base" "$base_tree" "$run_hash" > "$tmp/records/suite-status.json"
git -C "$tmp" add . && git -C "$tmp" commit -qm green-record
# Construct a realistic merge commit: the receipt must name the final merged
# commit/tree, not merely its feature-branch parent.
git -C "$tmp" checkout -qb code-change HEAD
printf 'changed\n' > "$tmp/government/base"
git -C "$tmp" add . && git -C "$tmp" commit -qm candidate
git -C "$tmp" checkout -qb merge-candidate main
git -C "$tmp" merge --no-ff -q -m 'merge candidate' code-change
green_change=$(git -C "$tmp" rev-parse HEAD)
green_tree=$(git -C "$tmp" rev-parse HEAD^{tree})
printf '{"generated_by":"government/suite-status.sh","suite":"tests/records-smoke.sh","result":"green","commit":"%s","tree":"%s","recorded_at":1000,"runs":[{"run":1,"result":"green","exit":0,"output_sha256":"%s"}]}\n' \
    "$green_change" "$green_tree" "$run_hash" > "$VICHE_STATE_ROOT/delivery/verified-wrong-suite.json"
git -C "$tmp" checkout -q main
git -C "$tmp" merge --ff-only -q merge-candidate
# A green record for the wrong suite does not satisfy the code-change gate.
out=$(/bin/sh "$root/government/suite-compliance-check.sh" "$tmp")
printf '%s' "$out" | python3 -c 'import json,sys;x=json.load(sys.stdin); assert x["compliant"]==0; assert x["unreadable"]>0'
# Matching identity fields without a generated successful run are not evidence.
printf '{"generated_by":"government/suite-status.sh","suite":"tests/run-all.sh","result":"green","commit":"%s","tree":"%s","recorded_at":1000,"runs":[{"run":1,"result":"green","exit":0,"output_sha256":"%s"},{"run":2,"result":"red","exit":1,"output_sha256":"%s"}]}\n' \
    "$green_change" "$green_tree" "$run_hash" "$run_hash" > "$VICHE_STATE_ROOT/delivery/verified-malformed.json"
out=$(/bin/sh "$root/government/suite-compliance-check.sh" "$tmp")
printf '%s' "$out" | python3 -c 'import json,sys;x=json.load(sys.stdin); assert x["compliant"]==0; assert x["unreadable"]>0'
# JSON booleans are not valid integer run IDs/exits in suite-status evidence.
printf '{"generated_by":"government/suite-status.sh","suite":"tests/run-all.sh","result":"green","commit":"%s","tree":"%s","recorded_at":1000,"runs":[{"run":true,"result":"green","exit":false,"output_sha256":"%s"}]}\n' \
    "$green_change" "$green_tree" "$run_hash" > "$VICHE_STATE_ROOT/delivery/verified-bool.json"
out=$(/bin/sh "$root/government/suite-compliance-check.sh" "$tmp")
printf '%s' "$out" | python3 -c 'import json,sys;x=json.load(sys.stdin); assert x["compliant"]==0; assert x["unreadable"]>0'
printf '{"generated_by":"government/suite-status.sh","suite":"tests/run-all.sh","result":"green","commit":"%s","tree":"%s","recorded_at":1000,"runs":[{"run":1,"result":"green","exit":0,"output_sha256":"%s"}]}\n' \
    "$green_change" "$green_tree" "$run_hash" > "$VICHE_STATE_ROOT/delivery/verified-$green_change.json"
write_publication "$green_change" 1001 "$VICHE_STATE_ROOT/delivery/verified-$green_change.json"
out=$(/bin/sh "$root/government/suite-compliance-check.sh" "$tmp")
printf '%s' "$out" | python3 -c 'import json,sys;x=json.load(sys.stdin); assert x["compliant"]==1'
# A main change with no matching prior verification is unreadable.
printf 'unverified\n' > "$tmp/tests/unverified"
git -C "$tmp" add . && git -C "$tmp" commit -qm unverified-change
unverified_commit=$(git -C "$tmp" rev-parse HEAD)
unverified_tree=$(git -C "$tmp" rev-parse HEAD^{tree})
# A receipt timestamp after its publication event is not pre-change evidence.
printf '{"generated_by":"government/suite-status.sh","suite":"tests/run-all.sh","result":"green","commit":"%s","tree":"%s","recorded_at":true,"runs":[{"run":1,"result":"green","exit":0,"output_sha256":"%s"}]}\n' \
    "$unverified_commit" "$unverified_tree" "$run_hash" > "$VICHE_STATE_ROOT/delivery/verified-$unverified_commit.json"
write_publication "$unverified_commit" 1001 "$VICHE_STATE_ROOT/delivery/verified-$unverified_commit.json"
out=$(/bin/sh "$root/government/suite-compliance-check.sh" "$tmp")
printf '%s' "$out" | python3 -c 'import json,sys;x=json.load(sys.stdin); row=next(r for r in x["per_change"] if r["commit"]==sys.argv[1]); assert row["status"]=="unreadable",row' "$unverified_commit"
# Even an integer timestamp fails if it is later than the publication event.
printf '{"generated_by":"government/suite-status.sh","suite":"tests/run-all.sh","result":"green","commit":"%s","tree":"%s","recorded_at":2000,"runs":[{"run":1,"result":"green","exit":0,"output_sha256":"%s"}]}\n' \
    "$unverified_commit" "$unverified_tree" "$run_hash" > "$VICHE_STATE_ROOT/delivery/verified-$unverified_commit.json"
write_publication "$unverified_commit" 1001 "$VICHE_STATE_ROOT/delivery/verified-$unverified_commit.json"
out=$(/bin/sh "$root/government/suite-compliance-check.sh" "$tmp")
printf '%s' "$out" | python3 -c 'import json,sys;x=json.load(sys.stdin); row=next(r for r in x["per_change"] if r["commit"]==sys.argv[1]); assert row["status"]=="unreadable",row' "$unverified_commit"
# A red pre-push verification on the exact merge commit is a genuine violation.
git -C "$tmp" checkout -qb red-code HEAD
printf 'red\n' > "$tmp/tests/red"
git -C "$tmp" add . && git -C "$tmp" commit -qm red-change
git -C "$tmp" checkout -qb red-merge main
git -C "$tmp" merge --no-ff -q -m 'merge red candidate' red-code
red_commit=$(git -C "$tmp" rev-parse HEAD)
red_tree=$(git -C "$tmp" rev-parse HEAD^{tree})
printf '{"generated_by":"government/suite-status.sh","suite":"tests/run-all.sh","result":"red","commit":"%s","tree":"%s","recorded_at":1001,"runs":[{"run":1,"result":"red","exit":1,"output_sha256":"%s"},{"run":2,"result":"red","exit":1,"output_sha256":"%s"},{"run":3,"result":"green","exit":0,"output_sha256":"%s"}]}\n' \
    "$red_commit" "$red_tree" "$run_hash" "$run_hash" "$run_hash" > "$VICHE_STATE_ROOT/delivery/verified-malformed-red.json"
git -C "$tmp" checkout -q main
git -C "$tmp" merge --ff-only -q red-merge
# A red/red/green sequence is neither a valid flaky-red resolution nor a
# red-main receipt, and cannot create a violation.
out=$(/bin/sh "$root/government/suite-compliance-check.sh" "$tmp")
printf '%s' "$out" | python3 -c 'import json,sys;x=json.load(sys.stdin); assert x["violations"]==0; assert x["main_red_episodes"]==0'
printf '{"generated_by":"government/suite-status.sh","suite":"tests/run-all.sh","result":"red","commit":"%s","tree":"%s","recorded_at":1002,"runs":[{"run":1,"result":"red","exit":1,"output_sha256":"%s"},{"run":2,"result":"red","exit":1,"output_sha256":"%s"}]}\n' \
    "$red_commit" "$red_tree" "$run_hash" "$run_hash" > "$VICHE_STATE_ROOT/delivery/verified-red-$red_commit.json"
write_publication "$red_commit" 1003 "$VICHE_STATE_ROOT/delivery/verified-red-$red_commit.json"
printf '{"generated_by":"government/suite-status.sh","suite":"tests/run-all.sh","result":"red","commit":"%s","tree":"%s","runs":[{"run":1,"result":"red","exit":1,"output_sha256":"%s"},{"run":2,"result":"red","exit":1,"output_sha256":"%s"}]}\n' \
    "$red_commit" "$red_tree" "$run_hash" "$run_hash" > "$tmp/records/suite-status.json"
git -C "$tmp" add . && git -C "$tmp" commit -qm red-record
out=$(/bin/sh "$root/government/suite-compliance-check.sh" "$tmp")
printf '%s' "$out" | python3 -c 'import json,sys;x=json.load(sys.stdin); assert x["status"]=="measured"; assert x["compliant"]==1; assert x["unreadable"]>0; assert x["main_red_episodes"]==1; assert x["violations"]==1'
echo 'suite-compliance-smoke: passed (pre-push chronology required; boolean/late/missing unreadable; red violation)'
