# Act 25 §4 Phase-2 pre-landing verification record for candidate `65da1b7` (verbatim copy)

Copied from `/var/lib/lubko/wd/viche-state/delivery/act25-c5-prelanding-c1a0000b.json` **after** the fast-forward to exactly this commit. An earlier record in the same file held `4b5a72a` (parent mismatch); this is the `pass` for `65da1b7`. Preserved verbatim; do not hand-edit.

```json
{
  "branch": "clerk/act25-phase2-correction",
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
  "commit": "65da1b76cb775d2fd0801ef80b9e63d742973671",
  "conditions": "Valid only for a fast-forward of main from ac5baae... to 65da1b7.... If origin/main moves, this is void. The landed commit/tree must equal the recorded pair; a different tree voids the record per Act 25 s4.",
  "delta_character": "LAWS.md heading/provenance correction plus a uniform marker widening in seven government consumers: the grep/regex pattern for the Act heading changed from '(enacted ' to '((re-)?enacted '. No vote, quorum, ballot, roster or outcome logic touched.",
  "delta_paths": [
    "government/LAWS.md",
    "government/appointments.sh",
    "government/boot.sh",
    "government/branch-health.sh",
    "government/executive-innovation-cycle.sh",
    "government/institutional-cases.py",
    "government/outcome-metrics.py",
    "government/sitting.sh"
  ],
  "environment": "clean detached worktree at the exact commit with VICHE_TOWN_ROOT pinned",
  "heading_check": {
    "act24_operative_headings": 0,
    "matches_exact_required_form": true,
    "observed_at_line": 236,
    "required_form": "## Act 25 - Executive Innovation Office Act (re-enacted 2026-11-08, bill executive-innovation-office-reenactment-act-v3)"
  },
  "independence_basis": "Auditor seat; candidate change is Clerk-authored; reviewer is neither the sponsor (c1a00004) nor the Clerk (c1a00001)",
  "kind": "act25-c5-prelanding-verification",
  "landing_authorisation": "fast_forward_main_to_this_exact_commit_only",
  "m024_check": {
    "character": "negating cross-reference only: the provenance says it supersedes the purported Act 24 record, which it does not validate, and that the M-024 enactment asserted there is not established",
    "false_attribution_remaining": false,
    "occurrences_within_act25_section": 1
  },
  "origin_main_at_record_time": "ac5baaedd2f3ef79255ea6f2bbeadebd6eae07f0",
  "origin_main_unchanged_after_suite_runs": true,
  "parent": "ac5baaedd2f3ef79255ea6f2bbeadebd6eae07f0",
  "parent_equals_origin_main_at_resolution": true,
  "phase": 2,
  "phase_scope": "Act 25 codification text correction: LAWS.md heading and own provenance, plus marker consumers widened to accept the re-enacted heading",
  "recorded_iso": "2026-11-08T16:33:20Z",
  "reviewer": "c1a0000b",
  "reviewer_non_actions": "No commit to main from the reviewer; no LAWS.md, suite-status, enactment register or ballot edited by the reviewer.",
  "supersedes": "earlier HOLD version of this file (sha256 d940f5b2...) naming candidate 4b5a72a whose parent had gone stale",
  "tree": "7341c73bf9f01e71f929d4d6790b47591537ebac",
  "verdict": "pass"
}
```
