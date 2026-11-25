# clean-reachable-state-count-alln

## status

investigated

## origin

executive_commission

## agent_id

ESd3KCHwsin2aVsQD0bC9L-phases

## exit_state

clearexit

## question

For every large n, let N_clean(n) be the number of pairwise nonisomorphic posets reachable from the n-antichain A_n by a chain of minimax-optimal comparisons in which every step is Kraft-clean (both children have at most 2^{b-1} linear extensions, b=ceil(log2 e(P))). Is N_clean(n) bounded by 2^{O(n log n)}, asymptotically smaller than the 2^{Theta(n log^2 n)} full reachable/winning frontier, or is it already 2^{Omega(n log^2 n)}?

## basis

Verified n=9 #301 finding of researcher dmitri (G(A_n)=D(n); optimal trees have only D(n)=o(n) non-clean steps), winning-frontier barrier, Sergeev S(n)=log2(n!)+o(n), research-plan 'shrinking the exponent'. Ledger check: no existing front counts CLEAN-reachable states.

## falsifier

Exhibit n where exact enumeration gives N_clean(n) >= 2^{c n (log2 n)^2} with c near the full-frontier constant, OR show restricting to clean optimal steps loses root optimality (contradicting verified G(A_n)=D(n)).

## implication

If N_clean(n)=2^{O(n log n)}, an evaluator searching clean-reachable states plus the o(n) forced non-clean decision points (D(n)=o(n) by Sergeev) could in principle give a 2^{O(n log n)} exact algorithm for S(n), improving 2^{O(n log^2 n)}; a matching lower bound locates the exponent barrier inside clean steps.

## finding_unverified

Found the bug: color-class numbering depends on vertex order, so it isn't isomorphism-invariant across labelings. Fix: sort the signatures before assigning color indices.
Now let me re-validate against known unlabeled-poset counts.
The validation harness was generating cyclic (invalid) posets. Let me filter to valid posets (no self-loop after closure).
Canonicalization now validated (labeled 3/19/219/4231, unlabeled 2/5/16/63 for n=2..5). The earlier run used the buggy canonical form, so I must redo the computation.
F(A_n) now matches S(n) through n=7, and reachable counts follow dmitri's trend (n=8≈5102, n=9≈33054 expected). Let me run n=8 and n=9.
n=8 full reachable = 5102 exactly matches dmitri's board count — strong validation. Let me run n=9 with a longer timeout.
I’m treating the interruption as a recovery checkpoint, not a fresh run. So far, no board write or repository edit was made; I’m checking that and the scratch results before deciding what remains useful to do.
**Result: inconclusive on the all-\(n\) growth dichotomy.** I computed the exact clean-reachable frontier through \(n=8\), but those finite counts neither establish a \(2^{O(n\log n)}\) bound nor support a \(2^{\Omega(n\log^2 n)}\) lower bound.

From-scratch enumeration, counting the root separately:

| \(n\) | \(N_{\rm clean}(n)\), excluding root | Including root | \(F(A_n)\) |
|---:|---:|---:|---:|
| 2 | 1 | 2 | 1 |
| 3 | 4 | 5 | 3 |
| 4 | 11 | 12 | 5 |
| 5 | 18 | 19 | 7 |
| 6 | 131 | 132 | 10 |
| 7 | 758 | 759 | 13 |
| 8 | 4,589 | 4,590 | 16 |

**Experiment and cross-checks:** the implementation used its own transitive-closure posets, downset-DP extension counts, canonicalization, and exact minimax recurrence. It reproduced the known \(S(n)\) values through \(n=8\). At \(n=8\), it found 5,102 optimal-play-reachable states overall, matching the existing census; its clean subset has 4,589 states excluding the root. Extension counting also matched brute-force permutation counting at the \(n=8\) witness with successor masks `(62,48,8,0,32,0,140,12)`: both gave \(e=65\). The \(n=9\) run was killed before producing a result.

**What this does not show:** the soundness bound \(G(P)\ge\varepsilon(P)\) and the reported identity \(G(A_n)=D(n)\) do not make clean reachability a complete shortcut for evaluating \(S(n)\). In particular, \(G\) requires knowing which comparisons are minimax-optimal, which itself requires minimax values. Nor do general-poset obstructions establish a lower bound for states reachable from the antichain. Sergeev’s asymptotic sorting bound and the winning-frontier theorem motivate the proposed exponent comparison, but neither resolves the clean-frontier count.

The main failed approach was extending the census to \(n=9\); it exhausted the run without an exact count. So there is no falsification of either asymptotic alternative here—only a finite exact result and a concrete computational limit.

**Recovery audit:** still on `billy-dev` at `6a96398`, with a clean Git worktree. Scratch work is under `/tmp/opencode/cleanfront`; no repository or Lean changes, commits, ledger changes, or board posts were made.

## Other metadata

```json
{
  "finished_at": 1795210136.1286287,
  "started_at": 1795209211.9292054
}
```
