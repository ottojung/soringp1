# t6-uniform-tightness-threshold

## status

investigated

## origin

ai_proposal_unverified

## agent_id

imWzMnGHRmJT1FNH4j0Xpc-ventured

## exit_state

clearexit

## question

Is the universal tightness threshold T(6) exactly 33, i.e. does every finite poset P with e(P) <= 33 satisfy m(P) <= 6?

## basis

t5-min-extension-threshold proved T(r) <= F_{r+3}-1 and equality for r<=5; r=6 remains open.

## falsifier

Exhibit a finite poset with e(P) <= 33 and m(P) >= 7, or prove none exists by exact enumeration of ordinally indecomposable cores.

## implication

Resolves the first open instance beyond the proved r=2..5 equalities and directly tests the Fibonacci splitting conjecture at r=6.

## finding_unverified

## Summary

**Front:** `t6-uniform-tightness-threshold` — Is `T(6) = 33`?

**Result: No counterexample found; `T(6) = 33` is supported by exact enumeration.**

- **Independent re-run** of `core_threshold_census.py --E 33 --h 6` in this worktree's base produced **1,053 cores** with `e(P) ≤ 33` and **0 failures** at comparison budget 6 (levels `n=2..33`).
- **Completeness** rests on the paper proof in `research-core-threshold.md` (Lemmas 1–5): universal elements reduce any poset to a core with identical `(e,m)`; every core is generated from the 2-antichain by maximal insertion above a proper ideal or ordinal sums; every core satisfies `e(P) ≥ |P|`, so `e ≤ 33` implies `|P| ≤ 33` and level-by-level generation is complete.
- **Upper witness:** the staircase `S_8` has `e = 34`, `m = 7`, so `T(6) ≤ 33`. Hence `T(6) = 33` exactly.
- **Falsifier direction not met:** no poset with `e ≤ 33` and `m ≥ 7`.

**Honest limits reported (not process success):**
- This is a finite verified instance, not a proof of the all-`n` Fibonacci statement `e(P) ≥ F_{m(P)+2}` (`T(r)=F_{r+3}-1` for all `r`), which reduces to the still-unproved balancing **Lemma A**.
- No complexity-class consequence: the root state of `S(n)` is the antichain (`e = n!`), far outside this threshold range for `n ≥ 6`.
- The census is conditional on implementation faithfulness (independently audited only through `n=8`, plus dual-generator agreement on the full `E=33` set).

**Deliverables:** untracked `exec-report.md` in the worktree (matching other fronts' convention) and one board post to Antonina #301 authored `SoringP1 frontier: t6-uniform-tightness-threshold` (no duplicate; none existed before). No Lean, repository, commit, or PR changes. Worktree clean aside from the untracked report.

## Other metadata

```json
{
  "finished_at": 1794882557.1524212,
  "started_at": 1794881653.7820756
}
```
