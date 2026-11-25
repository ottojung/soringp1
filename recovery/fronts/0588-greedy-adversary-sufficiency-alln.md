# greedy-adversary-sufficiency-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

mPBe8eFJsiMnRkAo0Rsyp5-lannes

## exit_state

clearexit

## question

Define G(n) as the value of the exact sorting game when the adversary is restricted to always answer into the outcome whose child has more linear extensions (with ties chosen adversarially). Determine whether G(n) equals S(n) for every n, or whether the greedy adversary is strictly weaker than the unrestricted adversary at some n.

## basis

Board #301 (2026-11-17) proves L_k(A_n)=ceil(log2 n!) for the entire greedy leaf-count hierarchy; docs/research-one-ply-obstruction.md defines L1 and an e=8 state with no balanced split; S(12)=30>C(12)=29 is literature. Small independent n<=9 experiments here are consistent with G(n)=S(n); n=12 remains unresolved.

## falsifier

Exhibit an n, with the first candidate n=12 where C(12)=29 but S(12)=30, and a sorter strategy reaching a total order within 29 comparisons against every greedy-adversary answer sequence, yielding G(n)<S(n); alternatively prove G(n)<S(n) on an infinite family.

## implication

A counterexample rules out every lower-bound or certificate method whose adversary model inspects only the larger-entropy child (the one-ply, L_k and entropy-balance family), since such a method cannot certify S(n)>ceil(log2 n!) at n=12; an equality proof would make greedy-adversary analysis sufficient for exact S(n).

## finding_unverified

le G(A_{12})$ can remain 29 even if $L_k(A_{12})$ becomes 30. Thus the $L_k(A_n)=C(n)$ claim, if read as blocking all finite-ply lift, is misleading for $L_k$ vs $F$, while the genuine open point is whether the **heavy-child** restriction $G$ already captures $S$.

I also note a model distinction from Stober–Weiß/Wells [literature]: “check only the larger-extension child” is used as a *forward-search pruning/lower-bound* device for proving $S(n)>C$ in explored cases; it is sound as a refutation search heuristic in that context but, as a general poset claim, the heavy branch is not always the $F$-hardest branch (board `ROOT-ANTICHAIN CAPACITY`: $g(P)<F(P)$ for 1620/130023 labelled $n=6$ posets, min witness $e=30,g=5,F=6$). $G\le F$ holds by definition, but $G=S$ at the antichain root for all $n$ is exactly the unresolved question.

## Concrete failed/inconclusive approaches and exact obstruction

- **Exact/DFS decision of $G(A_{12})\le 29$:** naive memoized search (Python, then C without symmetry reduction) too slow (~$2.4\times 10^4$ nodes/45s C, enormous branching/state count) to reach a conclusion.
- **Heuristic 29-step heavy-child path (beam):** widths 1 and 1500 failed to maintain a feasible frontier to depth 29 (1500 died at depth 19); wider search not completed. Not a refutation of $G(12)=29$.
- **Iterative heavy lookahead $h_k$:** computed $k\le 2$ only ($=29$); $k=3$ infeasible here.

**Exact obstruction:** A resolution needs either (i) an explicit, independently checkable height-29 strategy whose every heavy/tie-consistent play solves $A_{12}$ (a *completeness* certificate for $G(12)=29<S(12)$ — and note: verifying such a strategy against the restricted adversary is easier than unrestricted, but producing it requires search/argument I did not complete), or (ii) a proof that every sorter strategy has some heavy/tie-consistent answer path of length $\ge 30$ (showing $G(12)=30=S(12)$ at this $n$). The antichain-root state space and comparison branching make exhaustive certification nontrivial; no known compact invariant was obtained.

## Complexity implication (careful, as requested)

- A verified $G(n)<S(n)$ (e.g. at $n=12$) would rule out **soundness-as-completeness** for any exact lower-bound/certificate method whose adversarial justification inspects only the larger-extension (entropy/heavy) child — including one-ply/heavy-leaf-lookahead families in the greedy-adversary sense and entropy-balance arguments that take the heavier side — for certifying $S(n)>C(n)$ at that $n$. It would be a barrier to that *method family*, not a separation of P/NP/PSPACE and not a complexity lower bound for computing $S(n)$.
- A proof of $G(n)=S(n)$ for all $n$ would show greedy-adversary analysis is sufficient (complete) for exact $S(n)$, reducing the exact game to that restricted adversary model; computational tractability would remain a separate issue.

## Honest limits

No new theorem or counterexample was established. $G(12)$ and the all-$n$ question remain open from this pass. Small-$n$ evidence ($\le 6$ here) supports but cannot prove equality; beam/ply experiments were negative-or-inconclusive only. Primary-source details of Wells’ original $n=12$ argument were not fully re-derived from the PDF here (fetch unavailable), so I rely on the standard literature attribution recorded in-repo for $S(12)=30$ and on the structural distinction above rather than claiming a reproduced $g(A_{12})$ certificate. No Lean/repository/board changes were made.

## Other metadata

```json
{
  "finished_at": 1795152378.1342032,
  "started_at": 1795148414.8790498
}
```
