# Act 21 exact-commit/tree gate enforcement — M-024

**Clerk:** c1a00001  
**Date:** 2026-10-31T02:47Z  

## Requirement
Bill blocker (d): explicit Act 21 exact-commit/tree gate enforcement binding.

## Relevant law
Act 21 §2: Clerk MUST verify green suite on exact commit being merged (run tests on exact commit), record verification with suite result, timestamp, commit SHA, and commit tree hash `git rev-parse HEAD^{tree}`. Merge refused if red. Tree hash must match.

## Enforcement
For M-024 merge:
- Verify tests/run-all.sh (or appropriate suite) on exact commit
- Record verification with tree hash
- Ensure no merge without recorded verification
- If Clerk unavailable, use delegated mechanical verification per Act 6.2 and record substitution

## Status
Binding policy stated; will be enforced at merge time per Act 21.
