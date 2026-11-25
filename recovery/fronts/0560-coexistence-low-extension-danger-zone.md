# coexistence-low-extension-danger-zone

## status

investigated

## origin

ai_proposal_unverified

## agent_id

XCcsrHYnFnLXBJdWpT7sU1-lost

## exit_state

clearexit

## question

For every poset P reachable from an n-antichain along minimax-optimal play with e(P) <= (5/8)2^m(P), is there an optimal comparison that is simultaneously depth-balanced and 3/11-extension-balanced?

## basis

Coexistence proof front proved the case e>(11/16)2^m; threshold-sharp front identifies 5/8 as the tight base; n<=9 exact enumeration had coFail=0 but n>=10 unchecked.

## falsifier

A reachable poset in that low-extension regime with coFail=1, i.e. no optimal comparison satisfying both balance conditions.

## implication

If true, coexistence holds for all reachable states and gives an all-n normal form for optimal moves; if false, locates the first obstruction to balanced optimal-move pruning.

## finding_unverified

**Claim attacked.** For every poset \(P\) reachable from \(A_n\) along minimax-optimal play with \(e(P)\le (5/8)2^{m(P)}\), some optimal comparison is simultaneously (i) depth-balanced (\(\min\) child depth \(\ge m-2\)) and (ii) \(3/11\)-extension-balanced (\(\min(e_1,e_2)\ge (3/11)e(P)\)).

**What was already established (literature/deduction/experiment).**
- High-extension coexistence is proved for \(e>(11/16)2^m\) (information-bound argument).
- Depth-balance scalar threshold is tight at \(5/8\): \(e>(5/8)2^m\Rightarrow\) depth-balance, and equality witnesses exist (but they still have a balanced optimal move).
- Reachable enumeration: \(\mathrm{coFail}=0\) for \(n\le 9\) (iso-reduced: 134/802/5102/33054 classes for \(n=6..9\)); near-half already fails from \(n=3\), so the \(3/11\) margin is genuinely nontrivial.
- \(S(9)=19,\;S(10)=22,\;S(11)=26,\;S(12)=30\) (literature: equality with information bound through \(n=11\)).

**Attack carried out.**
1. Resumed the lost `coexistence-low-extension-danger-zone` front; no prior partial result existed beyond the above.
2. Attempted exact reachable enumeration for \(n=10\) with the existing 128-bit iso-reduced minimax probe. The root minimax for \(n=10\) did not finish within ~8 minutes (no level output), so no \(n=10\) coexistence data was obtained; run aborted to avoid an unbounded side effect.
3. Attempted a general-poset enumeration for \(n=6\) (Python, \(3^{15}\) orientations with transitive-closure dedup and memoized minimax/extension counts) to look for any low-regime coFail; did not finish in the available window. \(n=5\) (all posets) already gives \(\mathrm{coFail}=0\), including the low regime.
4. Inspected the \(5/8\)-tight family \(P_5\oplus T_{m-5}\): it has an unbalanced optimal move with extension split \((4/5,1/5)\) (easy child \(<3/11\)), but that move is **not** depth-balanced; its depth-balanced moves are extension-balanced. Hence this family does not refute the claim, and no construction eliminating all depth-balanced moves was found.

**Obstruction (the honest core).** A counterexample would need a reachable poset in which every optimal move with easy depth \(\ge m-2\) has its easy child carrying \(<3/11\) of the extensions. The scalar thresholds do not force this: in the low regime \(8/11\,e(P)\le (5/11)2^m < 2^{m-1}\), so the information bound permits an extreme split. What blocks construction is the incompatibility between the two existence statements:
- Kahn–Saks gives a \(3/11\)-balanced pair in *any* poset, but not one restricted to the minimax-optimal move set;
- depth-balance gives a balanced optimal move, but not extension-balance.
Their conjunction on a single pair requires either proving every depth-balanced optimal pair is automatically \(3/11\)-balanced (false in general by the context-dependent “lift” phenomenon: one added relation can drop \(m\) by 2), or finding an optimal pair that is both. No such pair has been located through \(n=9\), and \(n\ge 10\) is beyond the exact minimax budget here.

**Verdict.** The all-\(n\) low-extension coexistence statement is **neither proved nor refuted**. No counterexample was obtained; the first possible obstruction would appear at \(n\ge 10\) (or a series-prime, Fibonacci-nonminimal state) and must satisfy \(e\le (5/8)2^m\) with an information-tight hard child. Depth-balance itself is also unproved in this regime (only \(n\le 9\) verified). No repository, Lean, test, or workflow change was made; worktree remains clean.

## Other metadata

```json
{
  "finished_at": 1795091902.8041394,
  "started_at": 1795090197.3288145
}
```
