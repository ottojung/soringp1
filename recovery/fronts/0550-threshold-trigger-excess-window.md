# threshold-trigger-excess-window

## status

investigated

## origin

ai_proposal_unverified

## agent_id

DMfIzzj5PpsgrCiKdDJXYq-marrying

## exit_state

clearexit

## question

For which n does the exact threshold table T(r)=F_{r+3}-1 (reported for r<=8) ever trigger on states reachable from the n-antichain at residual budget r, given that every such state obeys e >= 2^(r-E(n)) with real excess E(n)=S(n)-log2(n!), making a trigger possible only when E(n) >= r-log2 T(r)?

## basis

The e>=2^(r-E) information bound follows from the comparison model in docs/problem.md; a short check gives r-log2 T(r) about 1.54 at r=8, while all exactly known n<=22 have excess below 1, so the reported T(8)=88 table never triggers on reachable states there.

## falsifier

Exhibit an n and a genuinely reachable state P at residual budget r>=7 with e(P) <= T(r), which requires an unusually large real excess E(n) near or above r-log2 T(r); or argue no reachable state ever meets this for any n and r>=7.

## implication

If the table is inert for all n it is a barrier showing the finite threshold and census results cannot improve the asymptotic unary evaluator bound; if it triggers, it pinpoints the narrow excess window where threshold-based base cases can actually help.

## finding_unverified

). **No witness found, no exhaustion.** [experiment, failed/incomplete approach]

I did **not** obtain an `n` and genuinely reachable `P` at residual budget `r>=7` with `e(P)<=T(r)`, nor a proof that none exists.

## 4. Obstruction / limits (honest)
- **Open for the window cases.** For `n∈{14,15,16,17}, r=8` (and analogous `r=7` cases) the global/adversary information condition is satisfiable and even `e_min ∈ [76,81] ⊂ [1,88]`, so nothing in the comparison/information counting above rules out a trigger state. Deciding existence seems to require either (a) an explicit reachable poset `P` at depth `t` with `e(P)<=T(r)` and a certificate that `P` lies on some `S(n)`-feasible strategy (or at least is reachable with `m(P)<=r`), or (b) a structural argument that no poset in the threshold family/low-`e` regime is reachable from `A_n` within `t` comparisons under any optimal/budget-feasible play. I have neither. [open]
- **Why nontrivial.** `T(r)` is tiny (`54,88`) while reachable states at those depths are highly constrained by ~27–34 prior comparisons; the realizable set of `(P,e(P),m(P))` from the antichain root is not characterized. General-poset threshold facts (core-threshold) give the `e=>m` implication but not root-reachability/completeness for triggering. [distinction: soundness of threshold vs reachability/completeness of trigger]
- **Asymptotic note (caution).** `g(r) ~ (1-log2 φ)r ≈ 0.306 r`. Sergeev’s bound gives `E(n)=O(n/(log n)^{1/5})` **[literature]**, so for sufficiently large `n` the condition `E(n)>=g(r)` is compatible with larger `r` (within that asymptotic allowance), but actual growth/values of `E(n)$ for `n>=23` are open and `T(r)` is verified here only for `r<=8`; no asymptotic trigger can be concluded.

## 5. Complexity implication (conditional) [deduction]
- **If inert (no reachable/encountered state has `e(P)<=T(r)` in the relevant evaluation regime):** the finite `T(r<=8)` table cannot act as a base-case/pruning shortcut for exact evaluation of `S(n)` in that regime — a **barrier to this specific threshold/base-case method**, not to all methods and not a separation result.
- **If it triggers:** it identifies a narrow window where such base cases can help, but (per the sound adversary form) compatibility at fixed `r` is tied to `E(n)>=g(r)`; for known `n<=22` this window is nonempty at `r=7,8` despite the front’s stated evidence, so triggering is not excluded by the global-excess argument (though no instance was found).
- This does **not** by itself yield a new uniform bound for `SORT-BOUND-U` / `S_unary`, nor any `P/NP/PSPACE` separation; `SORT-BOUND-U ∈ PSPACE` remains the baseline constraint (`AGENTS.md`/`docs/problem.md`).

## Bottom line
**Mathematical finding:** the front’s key inequality `e(P) >= 2^(r-E(n))` for every reachable state at residual budget `r` is **false** (counterexample `n=3,r=1,e=1`); the correct adversary statement gives only existence of some balanced-path state with that bound. With the correct `E(n)$, the `r=8` (and `r=7`) information window is **nonempty for several exactly known `n`** (`n=14..17` for `r=8`), contradicting the provided evidence. A **concrete reachable trigger state was not found** (greedy/partial beam search inconclusive) and **nonexistence was not proved**; the exact answer “for which `n` does `T(7),T(8)` trigger on genuinely reachable states?” remains **open** from this analysis. No substantive new theorem/counterexample warranting a repo or Lean change was established.

## Other metadata

```json
{
  "finished_at": 1795076336.5137017,
  "started_at": 1795074873.3670905
}
```
