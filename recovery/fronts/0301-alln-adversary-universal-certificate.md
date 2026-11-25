# alln-adversary-universal-certificate

## status

investigated

## origin

ai_proposal_unverified

## agent_id

vpBATj5JQDrx81BOmQ3N2O-voters

## exit_state

clearexit

## question

For all sufficiently large n, if S(n) >= k+1 (a NO instance of SORT-BOUND-U), does there exist a uniform polynomial-size adversary strategy (as a function from history to comparison outcome) that forces >= k+1 comparisons for every sorter, and is this universally checkable by the same meet-backwards criterion as sorter strategies?

## basis

AGENTS.md states verification of adaptive strategy is in P (ledger: adaptive-tree-verification-hardness); board shows adversary encoding fronts running; Mahaney/sparsity constrain many-one NP-hardness but not witness duality.

## falsifier

Exhibit an infinite family of (n,k) with k>=S(n)-? NO-instances where every adversary strategy that is sound against all sorters requires superpolynomial description length or is not polynomially checkable under the same P-time validity test.

## implication

Would separate sorter-certificate (NP side) from adversary-certificate (coNP side) for SORT-BOUND-U without conflating fixed networks with adaptive trees, clarifying the NP/coNP boundary relative to unary sparsity.

## finding_unverified

l sorter strategies is: no sorter strategy can force a win against it within k. That’s exactly the complement game — equivalent to evaluating the AND-OR tree from adversary’s perspective. With an explicit adversary strategy object, you might need to explore all possible sorter branches it can face; if the adversary strategy doesn’t create merges, this could blow up. The "same meet-backwards criterion" would require the adversary object to have the same DAG/join structure to make the universal check local — if not polynomial-size in that form, check becomes hard.

Also note: "verification of adaptive strategy is in P" is mentioned in ledger context (per user quote) but not obviously supported by strong evidence in repo; combined with Parberry’s coNP-complete network verification and the ATM universality, it’s not obvious it’s in P for arbitrary representations.

**Concrete obstruction found (falsifying the "same criterion + poly-size" for all large n):**
Consider representing adversary strategy as a function `f(P, history)` giving an outcome for some pair. To be checkable by "meet-backwards criterion" like sorter (local intersection), the adversary must also be expressible as a DAG where we can do backwards meets from "dead-ends" (non-total states at depth k). But the adversary wins by *preventing* total orders — the "bad" set is large. There’s no reason the minimal such adversary DAG is polynomial-size for all NO instances; more directly, the dual of a polynomial sorter certificate is not obviously a polynomial adversary certificate in the same grammar. Also, if you don’t require the DAG form, an arbitrary adversary function might be hard to verify universally.

A concrete failed route: assume adversary strategy is given as a table over reachable posets — but number of reachable posets is `2^{Θ(n²)}` in general (Kleitman–Rothschild), so table would be superpolynomial. If restricted to "uniform polynomial-size" programs/circuits, checking "∀ sorter moves, follow adversary => no total order within k" is a universal property over an exponentially large tree of sorter choices; without the same merge structure, this is not obviously in P by local joins — could be equivalent to coNP-hardness depending on representation. The sparsity of SORT-BOUND-U blocks many-one NP-hardness but doesn’t force coNP-membership or polynomial adversary witnesses.

**Conclusion on the front:** The minimax duality gives existence of adversary strategies, but the claim “uniform polynomial-size adversary strategy… universally checkable by the same meet-backwards criterion as sorter strategies” is not established. A plausible obstruction is: (a) polynomial representation fails without merge structure (state explosion), or (b) universal checkability fails for non-merge representations (becomes coNP-like). The falsifier is reasonable — exhibit infinite family where every sound adversary strategy is either superpolynomial or not polynomially checkable by the same P-time meet-backwards test. I see no proof of the equivalence; the duality of games does not imply duality of succinct certificate complexity under the *same* local-join criterion.

**Limits:** No new theorem/counterexample constructed here (only analysis). Did not create Lean/repo changes. Did not conflate general-poset hardness with S(n). Distinction between fixed networks (Parberry/coNP) vs adaptive trees (game) is critical. No claim about P vs NP/coNP separation — only about witness duality/representation.


## Other metadata

```json
{
  "finished_at": 1793849500.6459475,
  "started_at": 1793848575.4118612
}
```
