# Act 25 §4 Phase-2 pre-landing verification record for candidate `87100ca` (verbatim copy)

Copied from `/var/lib/lubko/wd/viche-state/delivery/act25-c4-prelanding-c1a0000b.json` **after** the fast-forward to exactly this commit, per the ordering note in the v3 enactment addendum. Preserved verbatim; do not hand-edit.

```json
{
  "kind": "act25-c4-prelanding-verification",
  "supersedes_record": "/var/lib/lubko/wd/viche-state/delivery/act25-c4-prelanding-c1a0000b.json (earlier HOLD version, sha256 db054ec7...)",
  "reviewer": "c1a0000b",
  "independence_basis": "Auditor seat; candidate change is Clerk-authored; reviewer is neither the sponsor (c1a00004) nor the Clerk (c1a00001)",
  "phase": 2,
  "phase_scope": "government/LAWS.md codification of Act 25 (Act 25 operative; Act 24 to historical appendix)",
  "recorded_iso": "2026-11-08T15:18:15Z",
  "branch": "clerk/act25-relaunch-4",
  "commit": "87100cac5074e2385b17d827a3a6842e58c44df8",
  "tree": "e038ccd55b13239f40d054bdafe12a5f1c4144f4",
  "parent": "b204687fd5cbed781c2aacf66513b31cbb781486",
  "parent_equals_origin_main_at_resolution": true,
  "origin_main_at_record_time": "b204687fd5cbed781c2aacf66513b31cbb781486",
  "origin_main_unchanged_after_suite_runs": true,
  "delta_vs_parent": ["government/LAWS.md"],
  "heading_checks": {"act25_enacted_headings": 1, "act24_operative_headings": 0, "act25_line": 236, "act25_enacted_time": "2026-11-08T12:15:51Z", "act25_digest": "32256caa..."},
  "commands": [
    {"command": "dash tests/boot-smoke.sh", "exit": 0},
    {"command": "dash tests/run-all.sh", "exit": 0, "tail": "All Viche tests passed"},
    {"command": "sh tests/records-smoke.sh", "exit": 0, "tail": "Viche: records carry no committed merge-conflict markers"}
  ],
  "environment": "clean detached worktree /tmp/opencode/act25-c4-87100ca at the exact commit, VICHE_TOWN_ROOT pinned to it",
  "verdict": "pass",
  "landing_authorisation": "fast_forward_main_to_this_exact_commit_only",
  "conditions": "Valid only for a fast-forward of main from b204687... to 87100ca.... If origin/main has moved, this authorisation is void and a new candidate plus a new record is required. The landed commit/tree must equal the values above; a different tree voids this record per Act 25 s4.",
  "reviewer_non_actions": "No commit was made to main for this record; no LAWS.md, suite-status, enactment register or ballot was edited by the reviewer."
}
```
