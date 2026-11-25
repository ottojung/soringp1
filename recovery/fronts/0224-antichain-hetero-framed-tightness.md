# antichain-hetero-framed-tightness

## status

investigated

## origin

ai_proposal_unverified

## agent_id

00Y9urAC8nVV08TFkeq31w-thieves

## exit_state

clearexit

## question

For odd n >= 3, does there exist any framed comparison DAG (with possibly heterogeneous leaf certificate classes) of height exactly ceil(log2 n!) that is sound for sorting the n-element antichain, or does some all-n recursive divisibility obstruction block all information-theoretically tight general framed certificates?

## basis

Exact-reset obstruction for A_n->V_n (docs/research-exact-reset-realizability.md) plus root-dag-completeness-prefix gap on heterogeneous frames and soundness-vs-completeness distinction in AGENTS.md/docs/problem.md.

## falsifier

Construct an explicit heterogeneous framed-DAG of height ceil(log2 n!) for some odd n>=5, accepted by the existing soundness checker and correctly sorting A_n; or prove that for all odd n>=3 every height ceil(log2 n!) framed tree forces some node mass not partitionable by any set of allowed framed leaf classes.

## implication

A general obstruction would show information-theoretic tightness is incompatible with framed-certificate completeness for infinitely many n, sharply constraining any NP-certificate route for SORT-BOUND-U beyond the exact-reset case already ruled out.

## finding_unverified

 Kasai et al. 1994), 15 (42 > 41), 17 (50 > 49, Stober–Weiß), 19 (58 > 57). Now the key structural question: does the framed-DAG model (with joins, heterogeneous leaf classes) have any power *beyond* an ordinary decision tree for this task? Let me verify the checker semantics support an unfolding argument.
The checker semantics confirm the unfolding route: a node's annotation is the **intersection** of incoming feasible arcs, and a leaf is accepted iff that intersection is total. Now the paper proof. Let me construct the explicit falsifying certificate for n=5 (S(5)=7=C(5)) with the existing memoized minimax, converting the optimal tree into a framed DAG with identity frames.
The falsifier's constructive arm succeeds. Now the paper-side half of the front: I've verified the equivalence theorem against the checker's exact semantics. Let me check the board-posting mechanism before reporting.
Board confirms no prior report of this specific finding (the adjacent front's finding is different — shelling/insertion strategies, not framed DAG height-equivalence). Everything is verified. Now I'll compose and post exactly one board comment, with `--json` redirected to a file per operations.md.
Posted once and confirmed by digest. Final housekeeping check:
**Recovery audit:** No side effects from the interrupted turn (clean worktree, no posts/commits); the interrupted run was a read-only exhaustive computation I did not re-run — it was superseded by a cheaper decisive route.

**Mathematical finding (front: antichain-hetero-framed-tightness), reported once to board #301:**

1. **Equivalence theorem (paper proof, checker-semantics-grounded).** For every n, k: a framed DAG is *accepted* by `scripts/check_framed_strategy.py` at budget k sorting the antichain **iff** an ordinary adaptive comparison decision tree of height ≤ k sorts n keys. Tree→DAG: insert with identity frames (each node then has exactly one feasible incoming arc, so the checker's intersection collapses to the propagated closure). DAG→tree: unfold joins into per-path copies; each copy-leaf inherits one incoming path's propagated rows, a superset of the verified-total intersection, hence also total; impossible branches contribute no copy. So heterogeneous leaf classes and joins add **no height power** — they compress size only.

2. **Falsifier verified (constructive arm).** Accepted framed DAG of height exactly **7 = ⌈log₂ 5!⌉** sorting A₅ (239 nodes, identity frames), plus n=3 at height 3; `ACCEPT` from the existing soundness checker, budget−1 correctly rejected. The proposed **all-odd-n divisibility obstruction is false** — consistent with tightness at odd n=3,5,7,9,11.

3. **Honest boundary.** The exact-reset divisibility mechanism does *not* transfer to sorting: sorting leaves are singletons (granularity 1, not `(n−1)!`), so no first-split cardinality mismatch can arise. The genuine odd-n non-tightness starts at n=13 (S(13)=34 > C(13)=33; also 15,17,19 per literature) — there the equivalence theorem shows **no** framed DAG of height C(n) can sort A_n, independent of heterogeneity.

4. **Complexity implication.** Framed-certificate completeness at the information bound collapses exactly to the S(n)=C(n) question (settled for n ≤ 22); NP-certificate routes must remain at height S(n) — frontier unchanged but the C(n)-framing is provably vacuous.

No repository or Lean changes (worktree clean); certificates and generator under `/tmp/opencode/`, regenerable via the repo's memoized minimax.

## Other metadata

```json
{
  "finished_at": 1793697655.3279266,
  "started_at": 1793693039.1556933
}
```
