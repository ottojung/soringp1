# endpoint-feasibility-gap-n7

## status

investigated

## origin

executive_derived_open_lemma

## agent_id

TcxpwbSEf3ToWdWPgsaPXm-hither

## exit_state

clearexit

## question

Compute the exact finite quantity |C(7)| where C(n) is the set of poset states P reachable from the n-antichain with cover count c(P) plus minimax cost F(P) at most S(n), and compare with verified |L_tree(7)|=3044007 and |L_loc(7)|=2769663; settle whether the endpoint-feasibility gap |C(n)|-|L_tree(n)| (700 at n=5, 6060 at n=6) vanishes at n=7 (the identity claim) or persists/grows.

## basis

The reroute-endpoint-global-feasibility-alln front produced no final finding and is absent from the Antonina registry; its basis records the n=5/n=6 gaps and the unsettled n=7 identity claim. This bounded n=7 computation resolves that unfinished obligation.

## falsifier

Exact enumeration with |C(7)|>|L_tree(7)| refutes the n=7 identity claim; |C(7)|=|L_tree(7)| confirms it. Report independently checkable counts and the decomposition C(7)\L_tree(7) and L_tree(7)\L_loc(7).

## implication

A vanishing endpoint gap at n=7 supports endpoint cheap-statistic pruning as complete at that scale and weakens the case for an infinite endpoint-infeasibility obstruction; a persisting gap gives concrete witness families and a new obstruction to endpoint-based evaluators of S(n).

## finding_unverified

The decisive n=7 result is in and all cross-checks match the board. Let me add an independent cross-check computing the endpoint cost via BFS shortest-path length (d_min) instead of cover count, verifying D2 (d_min = cover count) at n=7.
Two independent methods agree on |C(7)|. Let me compute the structural witness family values F(A_7), F(V_7) from the board's D4 criterion to explain *why* the gap vanishes at n=7.
All cross-checks are consistent. Let me measure peak memory precisely to document that the predecessor's O obstruction is resolved.
Peak RSS ~351 MB in ~28s — the predecessor's ~2.3 GB Python OOM is resolved. Now the side-effect audit and duplicate-author scan before posting.
New posts appeared since my initial fetch. Let me re-scan all pages fresh for the exact author before posting.
No duplicate author. Worktree clean at base commit. Let me write and post the single #301 comment.
Post returned exit 0. Let me verify exactly one comment by my author now exists on #301.
Done. Here is the outcome.

## Finding (posted as exactly one #301 comment, 19:34:11Z)

**|C(7)| = 3,044,007 = |L_tree(7)|** — the endpoint-feasibility gap **vanishes at n=7**, confirming the previously unverified n=7 identity claim and refuting the stated falsifier (|C(7)| > |L_tree(7)|).

Decomposition: `C(7)\L_tree(7) = 0`, `L_tree(7)\L_loc(7) = 274,344`, with `L_loc ⊂ L_tree ⊂ C` (0 violations). So C = L_tree as **sets**, not just cardinalities.

## How it was established
- **Paper reasoning first**: C is a purely terminal statistic (d_min + F(P)) that ignores intermediate sibling-budget constraints; the gap `C\L_tree` is exactly endpoint-only over-acceptance, and by board D4 reduces structurally to whether `F(A_n)=S(n)−2 ∧ F(V_n)≥S(n)−1`.
- **One decisive experiment**: a from-scratch C++ engine (own bitmask transitive closure, open-addressing memoized exact minimax F, own cover count, L_loc/L_tree BFS). Validated **before** n=7 against every known board value — poset counts A001035 for n=5,6, S(5)=7, S(6)=10, |L_loc|=1551/65551, |L_tree|=1551/66991, |C(5)|=2251 (gap 700), |C(6)|=73051 (gap 6060) — then n=7: S(7)=13 ✓, all 6,129,859 posets enumerated = A001035(7) ✓, |L_loc(7)|=2,769,663 ✓, |L_tree(7)|=3,044,007 ✓, gap components ✓.
- **Second independent method**: recomputed endpoint cost via BFS shortest-path length d_min instead of cover count → same 3,044,007; D2 had 0 violations over all 6.1M posets.
- **Structural reason** [deduction]: F(A₆)=8=S−2, F(V₆)=9=S−1 (witness); F(A₇)=10=S−3, F(V₇)=11<S−1 (no witness).
- **Resource obstruction resolved**: peak RSS 351 MB in 28 s, versus the predecessor's ~2.3 GB Python OOM.

## Honest limits
Finite n=7 only — not an all-n theorem. The trend (700 → 6060 → 0) is non-monotone, so one vanishing data point does not prove eventual identity nor refute an infinite obstruction; that remains [open]. No theorem completion for S(n)/SORT-BOUND-U, no class separation, no repo/Lean/test/workflow/ledger/main changes. Worktree clean at base `6a96398`.

## Other metadata

```json
{
  "finished_at": 1795116870.9571366,
  "started_at": 1795116293.131652
}
```
