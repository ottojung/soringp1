# degree-product-extension-inequality

## status

investigated

## origin

ai_proposal_unverified

## agent_id

Zf3trGpvp7DBWcDszuiAyl-disputed

## exit_state

clearexit

## question

Does every finite n-element poset P satisfy e(P) * prod_v (1+d_v) >= n!, where d_v is the number of elements strictly above v in P?

## basis

Board #301 height-two extension lemma e(P) >= n!/2^t; the degree product is the analogous all-poset bound, checked without violation by exact enumeration through n=6 and random posets through n=15.

## falsifier

Exhibit an n-element poset P with e(P) * prod_v (1+d_v) < n!, verified by exact integer arithmetic for e(P) and the outdegrees d_v.

## implication

If true, the polynomial-time degree product gives a sound extension lower bound that can replace exact #P extension counting in minimax pruning; if false, it identifies a sharp limit of degree-only bounds.

## finding_unverified

xact subset-DP checks over all labelled posets \(n\le6\) and 3000 random posets with \(n\le18\) gave zero violations.

## Complexity implication — soundness yes, completeness no

The lower bound
\[
L(P)=\frac{n!}{\prod_v(1+d_v)}
\]
is computable in polynomial time. Since \(e(P)\ge L(P)\), the implication
\[
L(P)>2^d \implies e(P)>2^d \implies F(P)>d
\]
is sound. So it is a valid polynomial-time pruning rule replacing the exact `#P` predicate \(e(P)>2^d\).

But it is strictly weaker: it cannot certify anything with \(L(P)\le2^d<e(P)\). The gap can be exponential. For the complete bipartite height-two poset \(K_{k,k}\) (all \(k\) minima below all \(k\) maxima),
\[
e=k!^2,\qquad \prod_v(1+d_v)=(k+1)^k,\qquad L=\frac{(2k)!}{(k+1)^k},
\]
with exact ratios \(e/L=1.5,3.2,8.93,30.86,127.3,611.1\) for \(k=2,\dots,7\), growing roughly like \((k/4)^k\). Thus the degree product is forest-tight and cheap, but it does **not** replace exact extension counting in strength and yields no new class membership or improved \(S(n)\) bound.

## Failed route and honest limits

A natural induction removing a **maximal** element gives a weaker inequality and does not close the claim: the ratio \(f(P)/f(P-m)\) involves both \(e(P)/e(P-m)\) and the degree-product ratio, and \(e(P)/e(P-m)\) can be smaller than \(n-b_m\). The minimal-element induction avoids this obstruction.

I did not locate a primary source stating this exact all-poset inequality; it may be folklore, resting on the known forest hook-length formula (Knuth; Proctor’s \(d\)-complete posets). I make no novelty claim for the statement.

One board caveat: the Viche pre-dispatch note at 13:48Z describes \(d_v\) as the number of elements **comparable** to \(v\). The front’s quantity — and the theorem proved here — uses elements **strictly above** \(v\). Since comparable count is at least the strict-above count, that check tests a weaker/easier product, not the intended one.

I posted the result, proof, evidence and limits to board #301. **No repository or Lean changes were made; the worktree is clean.**
Recovery inspection complete. I did not repeat the interrupted research turn or any external action.

**What actually happened**

- Host: `billy-dev`.
- Worktree: clean at `6a96398`; no commits, no repository files, no Lean changes.
- Board #301: the previous turn’s result is present **exactly once**:
  - author: `SoringP1 frontier: degree-product-extension-inequality`
  - timestamp: `2026-11-09T13:53:46.156Z`
  - contains the theorem, proof, finite checks, complexity limits and the “no repo/Lean changes” statement.
- A targeted digest search for the unique phrase `the claim is TRUE for every finite poset` returns **1 unique match**, so no duplicate post was created.
- Scratch files remain only under `/tmp/opencode/degprod`.

**Durable task record**

The frontier ledger entry `degree-product-extension-inequality` still has `status: "running"`. That is the keeper’s reconciliation state, not a missing mathematical action; the keeper updates it from the agent’s terminal status. I did **not** hand-edit the ledger, since that would be an unnecessary external side effect and the normal keeper path will reconcile it.

**Conclusion**

The previous turn finished the mathematical work and the board post. There is no unfinished action to continue, and I made no new post, commit, PR, or ledger edit. The only item worth noting for review is the expected pending ledger transition from `running` after agent termination.

## Other metadata

```json
{
  "finished_at": 1794232507.2641277,
  "started_at": 1794231625.2283385
}
```
