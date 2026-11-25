# join-reduced-canonical-strategy-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

8JgLl8sY4XxqJY7xbQFDIS-protest

## exit_state

clearexit

## question

For every n, does there exist an optimal height-S(n) adaptive comparison strategy whose set of antichain-reachable states is join-reduced under relation meet (no two distinct reachable states P,Q with F(P)=F(Q)=F(P&Q)) AND has polynomially many states in n? Independent scratch computation found such strategies at n=5 (S=7, 239 states) and n=6 (S=10, 1439 states), so the reported greedy-merge non-confluence at n=5,6,7 does not by itself preclude a compact canonical optimum.

## basis

Freshest #301 result lossless-merge-confluence-canonical-form (19:07Z) refuted greedy confluence at n=5,6,7; two follow-ups already dispatched cover budget-tight witnesses and corrected-criterion confluence. Independent scratch checks (curator_verify.py) found join-reduced optimal strategies at n=5,6 with height S(n); these are finite experiments, not an all-n claim.

## falsifier

Exhibit infinitely many n where every height-S(n) strategy either necessarily contains a mergeable state pair in any canonical form or needs superpolynomially many join-reduced states, backed by exact minimax enumeration and a size argument.

## implication

A yes answer would revive the polynomial-size canonical-DAG / succinct NP-certificate route for SORT-BOUND-U despite non-confluence; a no answer would upgrade the confluence failure from 'greedy merging fails' to 'no compact canonical optimum exists', bearing directly on certificate completeness.

## finding_unverified

 and confirm no prior post exists from my front, then check git state for side effects.
All checks confirm the theorem. Let me write the board report and post it to #301.
Let me verify the post landed and confirm the worktree is still clean.
Done. I worked entirely on `billy-dev` in the assigned worktree, studied the contract/problem/board #301 and the relevant primary literature, and attacked the FRONT claim. Here is the honest outcome.

## Mathematical finding (deduction, all n): the FRONT is false

**Theorem.** For *any* deterministic comparison‑sorting strategy Σ on n distinct labelled keys, the map (root‑to‑node outcome path) → (poset at that node) is injective, so Σ has **exactly 2n!−1 distinct reachable posets** (n! chains + n!−1 internal states).

*Proof.* A correct sorter has one leaf per input permutation = n! distinct total orders, hence n!−1 internal nodes. Two distinct paths share a maximal prefix ending at state S, then diverge at a comparison (i,j): one branch adds i<j, the other j<i (i,j incomparable in S). All later states are transitive closures of consistent supersets, so they permanently contain i<j vs j<i — a poset cannot contain both. So distinct paths never yield the same poset. ∎

**Corollary.** 2n!−1 is superpolynomial for n≥4, so *no* strategy — canonical or otherwise, join‑reduced or not — has polynomially many reachable states. The FRONT's existence claim fails for every n≥4. Verified computationally: 47/239/1439 = 2n!−1 for n=4/5/6, path‑injective for optimal and hundreds of random non‑optimal strategies.

## Correction of the premise (experiment + deduction)

The cited "join‑reduced optimal strategies at n=5 (239 states) and n=6 (1439 states)" are precisely **2·5!−1 and 2·6!−1 — the full reduced trees**, the maximum possible count. They are not "compact canonical optima"; the ratio 1439/239≈6 exposes factorial growth. So the basis does not support the FRONT — it refutes it.

## Structural clarification (exact obstruction)

Two objects were conflated: (a) reachable labelled posets of one strategy (universally 2n!−1, never polynomial; this is where join‑reducedness lives), and (b) framed‑DAG annotation states (compressible to polynomial via join+frame identifications, e.g. the known 19‑node n=7 certificate). Compression happens on (b), so join‑reducedness of (a) is irrelevant to certificate size. Moreover, a lossless join `F(P)=F(Q)=F(P&Q)` is exactly the merge join‑reducedness forbids — so requiring it removes the only surplus‑free state identification, and cannot produce compactness. The genuinely open question (framed‑DAG completeness / no‑cheap‑coarsening) is a different front.

## Honest limits

- Refutation holds under the stated "reachable labelled posets" reading; if "states" meant framed‑DAG annotations or isomorphism classes, that is a separate, already‑tracked question.
- This does **not** show SORT‑BOUND‑U ∉ NP, does not prove superpolynomial certificates, and leaves SORT‑BOUND‑U ∈ PSPACE unchanged — no complexity‑class result.
- "Every optimal strategy is join‑reduced" is only experimental (n≤6, thousands of sampled strategies; confluence‑witness states never co‑occur in one strategy), **not proved**.
- No genuine new theorem about certificate completeness was found; I did not manufacture one.

**Deliverables:** one concise finding posted to Antonina #301 (timestamp 19:44:50Z); worktree clean at `6a96398`, no stash, no repo/Lean/test/workflow/ledger changes (scratch code only in `/tmp/opencode`).

## Other metadata

```json
{
  "finished_at": 1795031115.2857504,
  "started_at": 1795030230.9961834
}
```
