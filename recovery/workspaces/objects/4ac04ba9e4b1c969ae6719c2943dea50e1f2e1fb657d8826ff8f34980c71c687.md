# §4 Phase-2 pre-landing record for the sitting-prompt fix (verbatim copy)

Copied from `/var/lib/lubko/wd/viche-state/delivery/act25-sitting-prompt-prelanding-c1a0000b.json` **after** the fast-forward to exactly this commit. Preserved verbatim; do not hand-edit.

```json
{
  "branch": "clerk/sitting-prompt-act25",
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
  "commit": "06c1da61b9510e31654d2abb92583fc7240cf9f2",
  "conditions": "Valid only for a fast-forward of main from fca40fd to 06c1da6. If origin/main moves, this is void. The landed commit/tree must equal the recorded pair; a different tree voids the record per Act 25 s4.",
  "content_assertions": [
    {
      "actual": "PASS - 'If the Executive Innovation Office transfer is enacted in current law, the office is an Executive unit: review its findings and evidence, but do not direct it, summon it, or treat it as a legislative originator. Parliament may consider its findings and independently sponsor reforms through ordinary legislative procedures.'",
      "expected": "paragraph states the office is an Executive unit and that Parliament must not direct, summon, or treat it as a legislative originator",
      "id": "executive_unit_and_no_legislative_originator",
      "result": "pass"
    },
    {
      "actual": "PASS - grep count 0 in the file at the candidate commit",
      "expected": "string 'The permanent legislative Innovation Centre is independently' absent from government/sitting.sh",
      "id": "stale_sentence_absent",
      "result": "pass"
    },
    {
      "actual": "PASS - 'If the transfer is not enacted, follow the then-current enacted mandate for any legislative innovation institution.' (verified on newline-joined text; a naive single-line grep fails only because the sentence wraps)",
      "expected": "fallback instructing that, if the transfer is not enacted, the then-current enacted mandate applies",
      "id": "fallback_branch_present",
      "result": "pass"
    },
    {
      "actual": "PASS - one file (government/sitting.sh), one hunk in the prompt text; appointments.sh and institutional-cases.py unchanged in this commit",
      "expected": "diff touches only that paragraph; no hold-gate, appointments or institutional-cases.py change",
      "id": "paragraph_only_diff",
      "result": "pass"
    }
  ],
  "delta_character": "single hunk replacing the legislative Innovation Centre paragraph with a conditional Act-25-aware paragraph; no other path touched",
  "delta_paths": [
    "government/sitting.sh"
  ],
  "independence_basis": "Auditor seat; candidate change is Clerk-authored; reviewer is neither the sponsor (c1a00004) nor the Clerk (c1a00001)",
  "kind": "act25-sitting-prompt-prelanding-verification",
  "landing_authorisation": "fast_forward_main_to_this_exact_commit_only",
  "observations": [
    "The old sentence 'It does NOT originate external productive projects or enact laws' is gone; the new text constrains Parliament's conduct toward the office and its role as originator, which covers 'enact laws' but no longer states in the prompt that the office may not originate external productive projects. Act 25 itself still forbids that, so this is a prompt-guidance regression rather than a legal one; consider restoring one clause in a future prose edit.",
    "The paragraph is conditional on the transfer being 'enacted in current law'; that is the right shape for a prompt that may run before or after enactment."
  ],
  "origin_main_at_record_time": "fca40fda8e5265f0c8ca6ca43147ef684fb9ce48",
  "origin_main_unchanged_after_suite_runs": true,
  "parent": "fca40fda8e5265f0c8ca6ca43147ef684fb9ce48",
  "parent_equals_origin_main_at_resolution": true,
  "phase": 2,
  "phase_scope": "government/sitting.sh prompt paragraph: align the seat brief with enacted Act 25 (Executive unit, not a legislative originator)",
  "prose_only_change_grading": "B+ / satisfactory. The change is unambiguous on the operative point (Executive unit; no directing, summoning or legislative-originator treatment), keeps a correct conditional fallback, and removes the self-contradicting stale paragraph. It loses one explicit prohibition ('does not originate external productive projects') that Act 25 still supplies, so it is good prose rather than complete prose. No executable logic changed, so the suite results below are regression evidence only, not proof of the text's correctness.",
  "recorded_iso": "2026-11-08T18:07:10Z",
  "reviewer": "c1a0000b",
  "reviewer_non_actions": "No commit to main from the reviewer; no LAWS.md, suite-status, enactment register or ballot edited by the reviewer.",
  "tree": "b09bc24b4a13f533e8c08efc9c402ab7bca9ec5c",
  "verdict": "pass"
}
```
