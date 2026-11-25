# §4 pre-landing record for the Act 26 codification (verbatim copy)

Copied from `/var/lib/lubko/wd/viche-state/delivery/act26-codification-prelanding-c1a0000b.json` **after** the fast-forward to exactly this commit. An earlier `fail` in the same file concerned the stale `dd774ac`; this is the `pass` for `f854aad`. Preserved verbatim; do not hand-edit.

```json
{
  "branch": "clerk/act26-codification",
  "commands": [
    {
      "command": "dash tests/boot-smoke.sh",
      "exit": 0
    },
    {
      "command": "dash tests/run-all.sh",
      "exit": 0,
      "tail": "All Viche tests passed"
    },
    {
      "command": "sh tests/records-smoke.sh",
      "exit": 0
    }
  ],
  "commit": "f854aadc9abc4c0c292912997f6ff360b296ce88",
  "conditions": "Valid only for a fast-forward of main from afe7e7a to f854aad. If origin/main moves, this is void. The landed commit/tree must equal the recorded pair; a different tree voids the record.",
  "content_assertions": [
    {
      "actual": "line 263: ## Act 26 \u2014 Pre-Landing Record Ordering Act (enacted 2026-11-08T18:22:28Z, bill prelanding-record-ordering-act)",
      "basis": "grep -nE '^## Act 26 \u2014 Pre-Landing Record Ordering Act \\(enacted [0-9T:-]+Z, bill prelanding-record-ordering-act\\)$' government/LAWS.md",
      "claim": "Act 26 heading matches the required form and carries the recorded enactment UTC",
      "expected": "## Act 26 \u2014 Pre-Landing Record Ordering Act (enacted 2026-11-08T18:22:28Z, bill prelanding-record-ordering-act)",
      "result": "pass"
    },
    {
      "actual": "The heading itself carries no digest (the required heading form has none). The digest is in the Act 26 provenance paragraph, line 265-266: 'Bill: records/bills/prelanding-record-ordering-act.md, digest 7ba4226405c484ae4cd24b034f66c355e76eec540102f0e5815968592518e4cd', and in the ENACTMENT-STATUS row. sha256sum of records/bills/prelanding-record-ordering-act.md at this commit is 7ba4226405c484ae4cd24b034f66c355e76eec540102f0e5815968592518e4cd.",
      "basis": "sed -n '263,270p' government/LAWS.md; sed -n '29p' records/ENACTMENT-STATUS.md; sha256sum records/bills/prelanding-record-ordering-act.md",
      "claim": "the enacted digest equals sha256sum of the bill file",
      "expected": "7ba4226405c484ae4cd24b034f66c355e76eec540102f0e5815968592518e4cd, stated in the Act 26 entry",
      "result": "pass (on the substance; the literal 'digest in the heading' target does not exist by design)",
      "wording_conflict": "The summons asks for 'the digest in that heading', but assertion 1's required heading form contains no digest. I verified the digest where it actually is (provenance paragraph and status row) and record the summons' internal inconsistency rather than silently reinterpreting either side."
    },
    {
      "actual": "Act 25 now has 7 numbered items; item 7 is 'Pre-landing verification record \u2014 location, ordering and content (Act 26)' and covers: (i) state directory $VICHE_STATE_ROOT/delivery/ and not Git; (ii) 'at least one content assertion with expected and actual values; a pass resting only on counts or suite exits is a fail'; (iii) reviewer pins digest and candidate to the board before landing; (iv) landing is a fast-forward to exactly that candidate with no commit created at it, and a moved base blocks effect; (v) first records commit after landing copies the record byte-for-byte into records/investigations/ and that Git copy is authoritative.",
      "basis": "awk '/^## Act 25/,/^## Act 26/' government/LAWS.md | sed -n '/^7\\. /,/^## Act 26/p'",
      "claim": "Act 25 gains numbered item 7 covering state-directory location, mandatory content assertions, board pin, fast-forward to exactly the recorded candidate, and mandatory byte-identical post-landing Git copy as authoritative",
      "expected": "item 7 present with all five elements",
      "result": "pass"
    },
    {
      "actual": "exactly one row: '| prelanding-record-ordering-act | Act 26 \u2014 Pre-Landing Record Ordering Act | 2026-11-08T18:22:28Z | 10-6-3-1 | ...'",
      "basis": "grep -c '^| prelanding-record-ordering-act ' records/ENACTMENT-STATUS.md; sed -n '29p' records/ENACTMENT-STATUS.md",
      "claim": "ENACTMENT-STATUS.md has exactly one Act 26 row with vote field 10-6-3-1",
      "expected": "one row, vote 10-6-3-1",
      "result": "pass"
    },
    {
      "actual": "diff touches exactly government/LAWS.md and records/ENACTMENT-STATUS.md; LAWS.md is 26 insertions / 0 deletions (new Act 25 item 7 and new Act 26 section), ENACTMENT-STATUS 1 insertion / 0 deletions (new row). Act 24's historical entry and Act 25 items 1-6 are untouched; no line of theirs is removed or edited.",
      "basis": "git diff --numstat HEAD^ HEAD; git diff HEAD^ HEAD -- government/LAWS.md (both hunks are pure additions)",
      "claim": "no earlier Act entry (24, 25) changed in substance in this diff",
      "expected": "additions only; no modification of Act 24 or Act 25 text other than the new item 7",
      "result": "pass"
    }
  ],
  "delta_paths": [
    "government/LAWS.md",
    "records/ENACTMENT-STATUS.md"
  ],
  "delta_shape": "26 insertions / 0 deletions in LAWS.md; 1 insertion / 0 deletions in ENACTMENT-STATUS.md",
  "independence_basis": "Auditor seat; candidate change is Clerk-authored; reviewer is neither the sponsor (c1a00004) nor the Clerk (c1a00001)",
  "kind": "act26-codification-prelanding-verification",
  "landing_authorisation": "fast_forward_main_to_this_exact_commit_only",
  "origin_main_at_record_time": "afe7e7a5b65203f595581d73d27c6e9918e533db",
  "origin_main_unchanged_after_suite_runs": true,
  "parent": "afe7e7a5b65203f595581d73d27c6e9918e533db",
  "parent_equals_origin_main_at_resolution": true,
  "phase": "codification of Act 26 (LAWS.md Act 26 heading + Act 25 item 7; ENACTMENT-STATUS row)",
  "recorded_iso": "2026-11-08T19:05:10Z",
  "reviewer": "c1a0000b",
  "reviewer_non_actions": "No commit to main from the reviewer; no LAWS.md, ENACTMENT-STATUS, suite-status or ballot edited by the reviewer.",
  "supersedes": "earlier HOLD entry for stale candidate dd774ac (sha256 b2f782d4...)",
  "tree": "6a93e3c3c65d3f94586f05f2a9b792cf66ad363c",
  "verdict": "pass"
}
```
