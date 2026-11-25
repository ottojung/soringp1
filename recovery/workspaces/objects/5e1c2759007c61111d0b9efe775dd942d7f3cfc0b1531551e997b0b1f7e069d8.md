# §4 pre-landing record for the Act 21 codification completion (verbatim copy)

Copied from `/var/lib/lubko/wd/viche-state/delivery/act21-codification-completion-c1a0000b.json` **after** the fast-forward to exactly this commit. An earlier `fail` (`status: no_candidate`) in the same file concerned the branch before it reached origin; this is the `pass` for `a46258e`. Preserved verbatim; do not hand-edit.

```json
{
  "branch": "clerk/act21-codification-completion",
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
      "exit": 0,
      "tail": "Viche: records carry no committed merge-conflict markers"
    }
  ],
  "commit": "a46258e47b4bf1dfb8f47a262ba0a1c233c5d16e",
  "conditions": "Valid only for a fast-forward of main from 96ae054 to a46258e. If origin/main moves, this is void. The landed commit/tree must equal the recorded pair; a different tree voids the record.",
  "content_assertions": [
    {
      "actual": "Act 21 item 2 now reads: 'For a fast-forward landing under Act 25 s4 / Act 26, the durable review record and the corresponding records/suite-status.json entry are written in the post-landing records commit described in Act 25 s2.1(8); the runs themselves MUST have been executed on the exact landed commit before the landing, their results and commands MUST appear in the pre-landing record, and that record MUST be pinned before the landing. This changes the timing of the record only, not the requirement to verify before landing.' All five elements present.",
      "basis": "git diff HEAD^ HEAD -- government/LAWS.md hunk at line ~196; sed -n '/^2\\. \\*\\*Clerk verification at merge/,+1p' government/LAWS.md",
      "claim": "s2.2(1): Act 21 s2 contains the fast-forward timing carve-out with all five required elements",
      "expected": "post-landing records commit for the record and suite-status; runs executed on the exact landed commit before landing; results and commands in the pre-landing record; record pinned before landing; explicit statement that only timing changes, not the duty to verify",
      "result": "pass"
    },
    {
      "actual": "Act 21 item 3 now reads: 'The verifying office MUST generate records/suite-status.json from the s2 verification by a deterministic script ... it MUST NOT be hand-edited. For a fast-forward landing it is generated from the pre-landing runs on the landed commit and committed in the post-landing records commit described in s2.'",
      "basis": "git diff HEAD^ HEAD -- government/LAWS.md hunk at line ~197",
      "claim": "s2.2(2): Act 21 s3 states suite-status stays script-generated, not hand-edited, and for a fast-forward landing is generated from the pre-landing runs and committed post-landing",
      "expected": "all three statements present",
      "result": "pass"
    },
    {
      "actual": "Act 21 item 5 now reads: 'For each fast-forward landing the audit additionally verifies the hash chain - board pin (or fallback log) -> state record -> records/suite-status.json and the committed copy - and that the landed commit equals the recorded candidate commit. A broken chain is reported as an incident, not reconciled silently.'",
      "basis": "git diff HEAD^ HEAD -- government/LAWS.md hunk at line ~198",
      "claim": "s2.2(4): Act 21 s5 audit covers the hash chain and landed-equals-recorded, with broken chains reported as incidents",
      "expected": "chain board pin (or fallback log) -> state record -> suite-status and committed copy; landed commit equals recorded candidate; incident not silent reconciliation",
      "result": "pass"
    },
    {
      "actual": "exactly one path changed: government/LAWS.md (3 insertions / 3 deletions). The three changed lines are Act 21 items 2, 3 and 5, and each change is the corresponding s2.2 clause. No other path, no other Act, no ENACTMENT-STATUS row, no test or script touched.",
      "basis": "git diff --name-only HEAD^ HEAD; git diff --numstat HEAD^ HEAD; full diff reviewed",
      "claim": "nothing else changed: every changed path listed with what changed",
      "expected": "a complete, honest path list",
      "result": "pass"
    },
    {
      "actual": "present. Exact-commit verification remains in item 2 ('on the exact commit being merged' plus tree hash). The records-only/records-smoke duty and the second-office reproduction for a Clerk-authored records change remain in item 1, which this diff does not touch. Note: those two duties live in Act 21 s1 rather than s2/s3 as the summons words it; the amendment s2.2(3) itself says they are 'unchanged and apply to the post-landing records commit', and the diff respects that by not editing item 1.",
      "basis": "sed -n '/^## Act 21/,/^## Act 22/p' government/LAWS.md; git diff shows item 1 untouched",
      "claim": "the unchanged duties are still present: exact-commit verification, records-only changes leave records-smoke green, no sole self-certification by the Clerk",
      "expected": "all three still present in Act 21",
      "result": "pass (with the section-location note recorded rather than glossed)"
    }
  ],
  "delta_paths": [
    "government/LAWS.md"
  ],
  "delta_shape": "3 insertions / 3 deletions, all in Act 21 items 2, 3 and 5",
  "independence_basis": "Auditor seat; candidate change is Clerk-authored; reviewer is neither the sponsor (c1a00004) nor the Clerk (c1a00001)",
  "kind": "act21-codification-completion-prelanding-verification",
  "landing_authorisation": "fast_forward_main_to_this_exact_commit_only",
  "origin_main_at_record_time": "96ae05478e31724c361b349d1fbe7780876889a2",
  "origin_main_unchanged_after_suite_runs": true,
  "parent": "96ae05478e31724c361b349d1fbe7780876889a2",
  "parent_equals_origin_main_at_resolution": true,
  "phase": "completion of the Act 21 amendments enacted by bill prelanding-record-ordering-act s2.2(1),(2),(4)",
  "recorded_iso": "2026-11-08T19:44:34Z",
  "reviewer": "c1a0000b",
  "reviewer_non_actions": "No commit to main from the reviewer; no LAWS.md, ENACTMENT-STATUS, suite-status or ballot edited by the reviewer.",
  "supersedes": "earlier HOLD entry for missing branch (sha256 c87fa116...)",
  "tree": "bae67ccc2338687e4b37d986c92a035af100db34",
  "verdict": "pass"
}
```
