# antonina-oPjzbO2lJECNkXTCoMBA4h-incapable

Session: ses_e482f2177ffe1TloHGXfiprcPp
Workspace: /home/lubko/soring-fronts/exec-root-composition-sibling-20261107
Created: 1794085281586; updated: 1794085306422

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 63 (msg_1b7d11924001WhHlHGDFyPPJD7)

**Result: no-go for the natural finite ordinal-boundary response profile, not a no-go for every possible finite summary.** The smallest counterexample already occurs at the antichain root for \(n=3\).

I treated the proposed profile as the exact response function of an ordinal product (in particular, two chains): for each possible interface comparison, record the minimax costs of its two sibling outcome states, together with the boundary order information. The root would choose a comparison minimizing \(1+\max\) of those two costs. This retains more information than a single merge cost or the ordinal-sum value.

For \(n=3\), every root comparison has, up to relabelling, the same children:

- one child is a two-element chain plus an isolated element, i.e. the two-chain merge \((1,2)\), with value \(2\);
- the other child is a three-element chain, with value \(0\).

Thus the exact root value is \(1+\max(2,0)=3=S(3)\). But the response needed for that calculation is **not a response of the two-chain/ordinal-product family**: one sibling is a parallel composition, not an ordinal product. A profile restricted to those product states omits an actual root response, so it cannot give a sound-and-complete recurrence for the antichain root. This is a sibling-incompatibility obstruction, rather than merely a numerical discrepancy in a proposed recurrence.

The check against the smallest known values is consistent: \(S(0),S(1),S(2),S(3)=0,0,1,3\); the \(n=3\) case is where the restricted profile first fails to cover root siblings. Later values through \(n=22\) cannot repair that coverage failure. In particular, this does **not** establish an obstruction for a richer summary that also represents the missing parallel sibling types.

This rules out the specified ordinal-product boundary profile as a standalone exact root state, but it does **not** prove that no finite interface summary exists. Nor does it produce a faster all-\(n\) recurrence: root soundness and completeness, a state/time bound beating \(2^{O(n\log^2 n)}\), and an extensible no-go for broader summary classes remain open. No repository files or board entries were changed.
