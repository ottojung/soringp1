#!/bin/sh
# Hermetic Act 26 source tests for government/suite-compliance-check.sh.
# Builds a synthetic Git history and state directory; no network, no live town.
set -eu
root=$(CDPATH= cd -- "$(dirname "$0")/.." && pwd -P)
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT HUP INT TERM
git -C "$tmp" init -q -b main
git -C "$tmp" config user.name test
git -C "$tmp" config user.email test@example.invalid
mkdir -p "$tmp/government" "$tmp/tests" "$tmp/records"
export VICHE_STATE_ROOT=$tmp/state
mkdir -p "$VICHE_STATE_ROOT/delivery"
run_hash=$(printf 'fixture output\n' | sha256sum | cut -d ' ' -f1)

commit_at() {
    when=$1
    message=$2
    GIT_AUTHOR_DATE="@$when +0000" GIT_COMMITTER_DATE="@$when +0000" \
        git -C "$tmp" commit -qm "$message"
}

# write_act26 <path> <commit> <tree> <created-epoch> <parent> <mode>
# mode: valid | noassert | noverdict | nodigest
write_act26() {
    python3 - "$@" <<'PY'
import datetime, hashlib, json, sys
path, commit, tree, created, parent, mode = sys.argv[1:7]
stamp = datetime.datetime.fromtimestamp(int(created), datetime.timezone.utc)
record = {
    'schema': 'act26-prelanding-record/v1',
    'reviewer': 'c1-test-reviewer',
    'independence_basis': 'synthetic non-sponsor, non-Clerk reviewer',
    'phase': 'synthetic phase',
    'bill_id': 'synthetic-bill',
    'commit': commit,
    'tree': tree,
    'parent': parent,
    'main_at_verification': parent,
    'commands': [{'command': 'sh tests/run-all.sh (synthetic)', 'exit': 0}],
    'content_assertions': [{
        'claim': 'synthetic claim',
        'expected': 'the candidate contains the expected content',
        'actual': 'the candidate contains the expected content',
        'basis': 'synthetic diff',
        'method': 'inspection',
    }],
    'verdict': 'pass',
    'status': 'verified',
    'landing_authorisation': 'fast_forward_main_to_this_exact_commit_only',
    'created_at': stamp.strftime('%Y-%m-%dT%H:%M:%SZ'),
    'board_pin': {'author': 'c1-test-reviewer',
                  'message_id': 'sha256:synthetic-pin',
                  'server_timestamp': stamp.strftime('%Y-%m-%dT%H:%M:%SZ')},
}
if mode == 'noassert':
    del record['content_assertions']
if mode == 'noverdict':
    del record['verdict']
if mode == 'noreviewer':
    del record['reviewer']
if mode == 'nopin':
    del record['board_pin']
if mode == 'nocmd':
    del record['commands']
if mode == 'nobasis':
    del record['content_assertions'][0]['basis']
    del record['content_assertions'][0]['method']
if mode == 'backdated':
    record['created_at'] = stamp.strftime('%Y-%m-%dT%H:%M:%SZ')
    record['board_pin']['server_timestamp'] = '2020-01-01T00:00:00Z' 
if mode != 'nodigest':
    body = {k: v for k, v in record.items() if k not in ('sha256','board_pin')}
    canonical = json.dumps(body, sort_keys=True, separators=(',', ':'),
                           ensure_ascii=True).encode('utf-8')
    digest = hashlib.sha256(canonical).hexdigest()
with open(path, 'w', encoding='utf-8') as f:
    f.write(json.dumps(record, indent=1) + '\n')
if mode != 'nodigest':
    with open(path + '.sha256', 'w', encoding='utf-8') as f:
        f.write(digest + '\n')
PY
}

# T0 base.
printf 'base\n' > "$tmp/government/base"
git -C "$tmp" add .
commit_at 1700000000 base

# C1: a valid Act 26 record must make this change compliant.
printf 'valid act26\n' > "$tmp/tests/act26-valid"
git -C "$tmp" add .
commit_at 1700000100 'change with valid act26 record'
c1=$(git -C "$tmp" rev-parse HEAD)
c1_tree=$(git -C "$tmp" rev-parse HEAD^{tree})
printf 'boundary one\n' > "$tmp/README.md"
git -C "$tmp" add .
commit_at 1700000200 'boundary after valid change'
write_act26 "$VICHE_STATE_ROOT/delivery/act26-valid.json" \
    "$c1" "$c1_tree" 1700000150 "$(git -C "$tmp" rev-parse "$c1^")" valid

# C2: a record whose tree does not match the change is not evidence.
printf 'tree mismatch\n' > "$tmp/tests/tree-mismatch"
git -C "$tmp" add .
commit_at 1700000300 'change with mismatched act26 tree'
c2=$(git -C "$tmp" rev-parse HEAD)
c2_parent=$(git -C "$tmp" rev-parse HEAD~1)
c2_wrong_tree=$(git -C "$tmp" rev-parse HEAD~1^{tree})
printf 'boundary two\n' > "$tmp/README.md"
git -C "$tmp" add .
commit_at 1700000400 'boundary after mismatched change'
write_act26 "$VICHE_STATE_ROOT/delivery/act26-tree-mismatch.json" \
    "$c2" "$c2_wrong_tree" 1700000350 "$c2_parent" valid

# A suite-status record committed after the change still cannot satisfy the
# existing Git-record ordering rule (the change is already in first-parent
# history, so the record does not precede it).
c2_tree=$(git -C "$tmp" rev-parse "$c2^{tree}")
printf '{"generated_by":"government/suite-status.sh","suite":"tests/run-all.sh","result":"green","commit":"%s","tree":"%s","runs":[{"run":1,"result":"green","exit":0,"output_sha256":"%s"}]}\n' \
    "$c2" "$c2_tree" "$run_hash" > "$tmp/records/suite-status.json"
git -C "$tmp" add .
commit_at 1700000450 'post-change git suite record'

# C3: a record created after the landing is not evidence. The landing is
# bounded above by the first-parent commit after the change.
printf 'late record\n' > "$tmp/tests/late-record"
git -C "$tmp" add .
commit_at 1700000500 'change with late act26 record'
c3=$(git -C "$tmp" rev-parse HEAD)
c3_tree=$(git -C "$tmp" rev-parse HEAD^{tree})
c3_parent=$(git -C "$tmp" rev-parse HEAD~1)
printf 'boundary three\n' > "$tmp/README.md"
git -C "$tmp" add .
commit_at 1700000600 'boundary after late change'
write_act26 "$VICHE_STATE_ROOT/delivery/act26-late.json" \
    "$c3" "$c3_tree" 1700000700 "$c3_parent" valid

# C4: records missing content_assertions, verdict or the canonical sha256 are
# not records, even when every other field matches.
printf 'missing fields\n' > "$tmp/tests/missing-fields"
git -C "$tmp" add .
commit_at 1700000700 'change with incomplete act26 records'
c4=$(git -C "$tmp" rev-parse HEAD)
c4_tree=$(git -C "$tmp" rev-parse HEAD^{tree})
c4_parent=$(git -C "$tmp" rev-parse HEAD~1)
printf 'boundary four\n' > "$tmp/README.md"
git -C "$tmp" add .
commit_at 1700000800 'boundary after incomplete change'
write_act26 "$VICHE_STATE_ROOT/delivery/act26-no-assertions.json" \
    "$c4" "$c4_tree" 1700000750 "$c4_parent" noassert
write_act26 "$VICHE_STATE_ROOT/delivery/act26-no-verdict.json" \
    "$c4" "$c4_tree" 1700000750 "$c4_parent" noverdict
write_act26 "$VICHE_STATE_ROOT/delivery/act26-no-digest.json" \
    "$c4" "$c4_tree" 1700000750 "$c4_parent" nodigest
write_act26 "$VICHE_STATE_ROOT/delivery/act26-no-reviewer.json" \
    "$c4" "$c4_tree" 1700000750 "$c4_parent" noreviewer
write_act26 "$VICHE_STATE_ROOT/delivery/act26-no-pin.json" \
    "$c4" "$c4_tree" 1700000750 "$c4_parent" nopin
write_act26 "$VICHE_STATE_ROOT/delivery/act26-no-commands.json" \
    "$c4" "$c4_tree" 1700000750 "$c4_parent" nocmd
write_act26 "$VICHE_STATE_ROOT/delivery/act26-no-basis.json" \
    "$c4" "$c4_tree" 1700000750 "$c4_parent" nobasis
write_act26 "$VICHE_STATE_ROOT/delivery/act26-backdated.json" \
    "$c4" "$c4_tree" 1700000750 "$c4_parent" backdated
wrong_parent=$(git -C "$tmp" rev-parse "$c4_parent^")
write_act26 "$VICHE_STATE_ROOT/delivery/act26-wrong-parent.json" \
    "$c4" "$c4_tree" 1700000750 "$wrong_parent" valid

# C5: the existing reviewed-merge receipt route must remain a positive control.
printf 'receipt change\n' > "$tmp/tests/receipt-change"
git -C "$tmp" add .
commit_at 1700000900 'change with pre-push receipt'
c5=$(git -C "$tmp" rev-parse HEAD)
c5_tree=$(git -C "$tmp" rev-parse HEAD^{tree})
printf '{"generated_by":"government/suite-status.sh","suite":"tests/run-all.sh","result":"green","commit":"%s","tree":"%s","recorded_at":1000,"runs":[{"run":1,"result":"green","exit":0,"output_sha256":"%s"}]}\n' \
    "$c5" "$c5_tree" "$run_hash" > "$VICHE_STATE_ROOT/delivery/verified-$c5.json"
receipt_digest=$(sha256sum "$VICHE_STATE_ROOT/delivery/verified-$c5.json" | cut -d ' ' -f1)
printf '{"generated_by":"government/reviewed-merge.sh","commit":"%s","published_at_ns":1001000000000,"receipt_sha256":"%s"}\n' \
    "$c5" "$receipt_digest" > "$VICHE_STATE_ROOT/delivery/published-$c5.json"

# The authoritative post-landing Git copy must bind to the independently
# authored state receipt; test invalid receipts with matching copies too.
mkdir -p "$tmp/records/investigations"
cp "$VICHE_STATE_ROOT"/delivery/*.json "$tmp/records/investigations/"
for f in "$VICHE_STATE_ROOT"/delivery/*.json.sha256; do
    [ -e "$f" ] || continue
    cp "$f" "$tmp/records/investigations/"
done
git -C "$tmp" add records/investigations
commit_at 1700000950 'postlanding evidence archive'

out=$(/bin/sh "$root/government/suite-compliance-check.sh" "$tmp")

# (i) valid canonical Act 26 record: compliant, with the record file as source.
printf '%s' "$out" | python3 -c '
import json, sys
x = json.load(sys.stdin)
row = next(r for r in x["per_change"] if r["commit"] == sys.argv[1])
assert row["status"] == "compliant", row
assert row["source"] == "act26-valid.json", row
assert "act26-prelanding-record" in row["source_labels"], row
assert "act26-prelanding-record" in row["reason"], row
' "$c1"

# (ii) tree mismatch: unreadable, even though commit/parent/digest are valid.
printf '%s' "$out" | python3 -c '
import json, sys
x = json.load(sys.stdin)
row = next(r for r in x["per_change"] if r["commit"] == sys.argv[1])
assert row["status"] == "unreadable", row
' "$c2"

# (iii) record created after the landing: unreadable.
printf '%s' "$out" | python3 -c '
import json, sys
x = json.load(sys.stdin)
row = next(r for r in x["per_change"] if r["commit"] == sys.argv[1])
assert row["status"] == "unreadable", row
' "$c3"

# (iv) missing content_assertions / verdict / sha256: unreadable.
printf '%s' "$out" | python3 -c '
import json, sys
x = json.load(sys.stdin)
row = next(r for r in x["per_change"] if r["commit"] == sys.argv[1])
assert row["status"] == "unreadable", row
' "$c4"

# (v) existing receipt path still yields a positive result.
printf '%s' "$out" | python3 -c '
import json, sys
x = json.load(sys.stdin)
row = next(r for r in x["per_change"] if r["commit"] == sys.argv[1])
assert row["status"] == "compliant", row
assert row["status"] == "compliant", row
assert "pre-push-receipt" in row["reason"], row
' "$c5"

# No synthetic violation or red episode exists in this fixture.
printf '%s' "$out" | python3 -c '
import json, sys
x = json.load(sys.stdin)
assert x["violations"] == 0, x
assert x["main_red_episodes"] == 0, x
assert x["compliant"] == 2, x
'

echo 'suite-compliance-act26-record-smoke: passed (valid Act 26 record compliant with source; tree mismatch, late/backdated record, missing required fields, missing pin/commands/basis and wrong parent unreadable; receipt control green)'
