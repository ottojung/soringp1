# upper-inequality-all-posets

## status

investigated

## origin

ai_proposal_unverified

## agent_id

YFeOaACE3HM82uHbmgBt7R-promote

## exit_state

clearexit

## question

Does the (U) inequality alpha(P) <= C(covers(P) + psi(m_P, M_P)) with C=(5-log2 15)/8 hold for every finite poset P, where alpha=F(P)-log2 e(P) and psi(m,M)=0 if (m,M)=(1,1), else min(mM,m+M)?

## basis

Newest board #301 merge-block-dominance-amplification (01:32Z) identifies (U) with psi as the precise remaining gap; independent exhaustive computation here over all 2,567,284 unlabelled n=10 posets finds no counterexample (max ratio 0.136377646629 < C).

## falsifier

Exhibit a finite poset P with exact alpha(P) > C(covers(P)+psi(m_P,M_P)), computed by exact minimax and exact linear-extension counting, or prove the inequality for every finite poset.

## implication

An all-n proof would give a universal local excess bound stronger than the mM-normalized inequality and a potential pruning bound for exact evaluation; a counterexample would show (U) fails outside height two, with no direct S(n) or SORT-BOUND-U consequence either way.

## finding_unverified

There's a discrepancy: `fonly` says F=9, the repo minimax says F=11. Let me investigate carefully.
The independent C minimax confirms F=11; `fonly` has a bug for this poset. Let me pin down the bug.
The `fonly` bug is a 128-bit key overflow at n=12 (12×12=144 bits). The true F is 11. Let me verify the counterexample thoroughly and check n=13.
We have a verified counterexample at n=12. Let me check the family's trend and verify with a third independent method.
The counterexample is confirmed by three independent methods. Let me check the family's growth and compute further members.
Recovering safely — inspecting prior work and durable records before continuing.
No external effects happened — worktree clean, no commits, no board post from this front. Re-verifying the candidate before reporting.
Recovery inspection first: worktree clean at `6a96398`, no commits, no Lean/repo changes. Ledger front `upper-inequality-all-posets` still `running`, no finding recorded. Board #301 has no post matching this falsifier (no `upper-inequality-all-posets` post, no `0.13713`/`13713060` string on downloaded pages 1–30 or live digest). No external side effect happened. All work below is local scratch only (`/tmp/opencode/upineq/`); nothing posted, committed, or published.

**Finding: (U) is FALSE [experiment, exact, independently checkable].**

- [definition] `(U)`: `alpha(P) <= C(covers(P)+psi(m_P,M_P))`, `C=(5-log2 15)/8=0.136638675548935...`, `alpha=F-log2 e`, `psi=0` iff `(m,M)=(1,1)` else `min(mM,m+M)`.
- [experiment] Counterexample, n=12, successor masks:
  `P=(1020,1000,976,992,960,384,768,256,0,0,1022,1023)`.
  Exact values: `F=11`, `e=306`, `covers=16`, `m=M=2`, `psi=4`, `D=20`, `alpha=11-log2 306=2.742612157307`, `C*D=2.732773510979`, excess `+0.009839`, ratio `0.137130607865367 > C`. Exact integer form holds: `15^20·2^88 > 306^8·2^100`.
- Verification is three-way independent: (1) repo labelled minimax `scripts/structural_lower_bounds.py:minimax` gives `F=11`; (2) standalone C memoized minimax (`/tmp/opencode/upineq/fmin.c`, hash-table, no nauty/canonicalization) gives `F=11`; (3) minimax over subsets of the 306 linear extensions (`/tmp/opencode/upineq/verify_subset.py`) gives `F=11`. `e=306`, closure, covers, `m/M` recomputed by direct definition. Antisymmetry/transitivity checked.
- Trend (same extension chain, `F` by method (2), `e`/covers by definition): n=13 `F=12,e=496,D=22`, ratio `0.138445622255142`; n=14 `F=13,e=802,D=24`, ratio `0.139689232231045`; n=15 `F=14,e=1298,D=26`, ratio `0.140689435846187`. All violate `(U)` by the exact integer test. n=13 `F` also confirmed by method (1); n=14/15 `F` is single-method.
- Origin: greedy one-point extension from the n=10 `m=M=2` ratio leader `(1020,1000,976,992,960,384,768,256,0,0)` (ratio `0.133876`), which rises through n=11 (`0.135008`) to breach `C` at n=12.

Failed approach caught: `fonly` (unsigned `__int128` canonical key = 12×12=144 bits) overflows at n=12 and returned spurious `F=9` for this poset; cross-check against (1)–(3) exposed it. The n=10 exhaustive census (`2,567,284` classes, max ratio `0.136377646629`, `badU=0`) is unaffected — keys fit at n=10 — and I reproduced it independently here.

Honest limits: this refutes the all-poset (U) only; per the front statement there is no direct `S(n)` or `SORT-BOUND-U` consequence. No all-n replacement constant is claimed; n=14/15 `F` values rest on one implementation. No repo, Lean, PR, or board changes made.

## Other metadata

```json
{
  "finished_at": 1794335806.8741064,
  "started_at": 1794317993.4124444
}
```
