# constant-truthtable-queries-for-unary-s-value

## status

investigated

## origin

ai_proposal_unverified

## agent_id

NBFYvvyrdbPgIEmFo3UV2k-prize

## exit_state

clearexit

## question

Is there a fixed constant c such that for all n >= 1 the value S(n) is computable on input 1^n by a uniform polynomial-time nonadaptive (truth-table) reduction making at most c queries to SORT-BOUND-U?

## basis

docs/problem.md gives equivalence of S_unary and SORT-BOUND-U via O(log U(n)) adaptive queries; Sergeev 2020 places S(n) in an o(n)-width window above ceil(log2(n!)), but no constant-query truth-table reduction is known.

## falsifier

Prove that for every constant c there exists some n for which no c-query nonadaptive uniform reduction from 1^n to SORT-BOUND-U determines S(n), by an information-theoretic or structural argument.

## implication

A positive answer would give constant parallel decision-oracle access to S_unary despite unknown exact values; a negative all-c result would show the standard adaptive binary-search dependence is unavoidable.

## finding_unverified

width may still be `ω(1)`).

## Concrete failed / insufficient approaches (and why)

1. **Naive counting on the fixed function [failed as stated].** One cannot argue “`c` bits < `log |window|` so impossible” directly for the actual `S`, because `b(n)` is a deterministic function of the fixed `S` and `Q(n)`; correctness requires only `E(1^n,b(n))=S(n)` on the true `b(n)`, not separation of hypothetical `S`-values. The correct invariant is Theorem 1: regardless of correlation, the reduction induces the poly-time list `E(1^n,·)`, so the unavoidable necessity is *constant listability*, not raw bit-counting against the true singleton.
2. **Same-input “threshold interval must be singleton” as an absolute impossibility [insufficient].** For queries `(1^n # 1^{k_i})`, `b(n)` identifies which of `c+1` threshold intervals contains `S(n)`. This does force `S(n)` into a `c+1`-list (Theorem 1 refinement), but it does **not** by itself force `S_unary ∈ FP` or force incorrectness: a fixed `E` could in principle satisfy `E(1^n,b(n))=S(n)` without naming the interval boundary as a query. It becomes a hardness only insofar as constant listability is hard/open.
3. **Cross-input monotonicity propagation as extra power [does not beat characterization].** A query `(1^m # 1^k)` yields a numeric consequence on `S(n)` only in cases `m>=n, b=1 => S(n)<=k` or `m<=n, b=0 => S(n)>=k+1` [deduction from `S` monotone]; these can tighten a computable interval but still feed only `c` answer bits total. Theorem 1 shows they cannot produce more than a `2^c`-list, and any `2^c`-list is already selectable via same-input queries — so cross-input queries give no asymptotic advantage for this front.
4. **Sergeev/window argument [inconclusive].** Known/claimed uncertainty is `⌈log₂ n!⌉ + o(n)` [literature, asymptotic, non-effective in-repo]: too wide to certify a constant list, not provably `ω(1)` in an effective form that would exclude one. I found no finite effective narrowing to `O(1)` and no proof of unbounded effective width.

## Exact obstruction
The front reduces cleanly to a sharp open condition but is not closed by available methods:
- **Solved here:** structural equivalence `FP^{||SORT-BOUND-U}_tt[O(1)] ⇔ O(1)`-listable in poly-time; same-input thresholds suffice; cross-input queries add no list power. (Independently checkable by the short proof above.)
- **Open:** decide that listability condition for the specific function `S`. A proof of the falsifier needs (at least) a theorem that `S(n)` cannot lie in any fixed-size poly-time enumerable set for infinitely/all sufficiently large `n`; a proof of the positive answer needs an explicit constant-size poly-time candidate generator. Neither follows from current repo results, Sergeev’s asymptotic bound, or standard sparse-set btt theorems, and an unconditional negative would subsume a separation far beyond the known `PSPACE ∩ P/poly` landscape for this tally language.

**Bottom line:** I did not disprove or prove the existence claim; I proved the precise all-`n` characterization that any constant-`c` nonadaptive truth-table reduction to `SORT-BOUND-U` exists iff `S(n)` is uniformly `2^c`-list-computable in polynomial time (a barrier/normal form), and identified the unconditional falsifier as open for the same reason strong uniform lower bounds for `S_unary` are open. No Lean/repository changes were warranted (no independently checkable new theorem/counterexample beyond this reported deduction, and no closure of the front).

## Other metadata

```json
{
  "finished_at": 1795003955.7759764,
  "started_at": 1795003286.4741209
}
```
