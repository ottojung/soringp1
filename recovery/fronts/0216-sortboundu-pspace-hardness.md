# sortboundu-pspace-hardness

## status

investigated

## origin

ai_proposal_unverified

## agent_id

nfefboOPmr92TeE5x4GaXB-dotted

## exit_state

clearexit

## question

Is SORT-BOUND-U = {1^n # 1^k : S(n) <= k} many-one polynomial-time hard for PSPACE (or complete), and if so can a direct reduction from a standard PSPACE-complete game be constructed without passing through general poset sorting?

## basis

SORT-BOUND-U is in PSPACE via alternating TM of the sorter-vs-adversary game (research-certificates-barriers Claim A), but PSPACE-hardness/ completeness is open per research-hardness-boundaries; unary encoding is sparse so NP-hardness blocked but PSPACE not obviously blocked.

## falsifier

Prove SORT-BOUND-U is in PH (or strictly below PSPACE) under some plausible assumption, or show that every reduction from a PSPACE-complete language produces an instance not realizable by any comparison-based sorting game on an antichain with the exact move rules.

## implication

PSPACE-completeness would make P != PSPACE equivalent to SORT-BOUND-U not in P and would rule out uniform subexponential exact algorithms for all practical purposes in a strong class sense.

## finding_unverified

rder is reached within k comparisons. S(n) ≤ k iff the sorter wins G(n,k). [deduction]"

So it's a two-player game: sorter wants to sort (force a total order) quickly, adversary wants to force many comparisons. The players alternate moves? Sorter moves by picking a pair to compare; adversary moves by giving the answer (direction). Yes, alternating moves, adversarial to the sorter. The depth/budget is k comparisons total. This is an alternating game (sorter-existential, adversary-universal in the sense of trying to prevent). So it's like a game tree where existential and universal nodes alternate? Or simply alternating players. This is similar to "path-finding" games or more directly to "evaluation games". Chandra-Kozen-Stockmeyer showed that alternating Turing machines characterize PSPACE/EXPTIME etc. So you can simulate this game by an ATM: existential states where sorter moves (guess the pair), universal states where adversary moves (branch on both answers). The state is just the current poset. Since posets on n elements can be represented in O(n^2) bits, and k is polynomial in n in the unary case (or bounded), the game is in PSPACE. That matches Claim A.
Let us look up the exact sparsity barrier again. For NP: sparse NP-complete (many-one) => P=NP. For EXPTIME: sparse EXPTIME-complete (many-one) => EXPTIME=P? Or different collapse. Also from some sources, Berman showed that if there is a sparse set in EXPTIME that is hard for EXPTIME under polynomial-time reductions, then EXPTIME ⊆ P/poly in some forms? Or more directly, the isomorphism conjecture / Berman's theorem gives that no sparse set is EXPTIME-complete. Let us look up carefully.

Let us start by exploring more. I need to understand the full picture - especially around sparsity barriers for PSPACE.

Let us look up the full context again.

Let us look up more about PSPACE hardness barriers and also think about the structure of this problem.

**Mathematical finding (disproof attempt):** Under the standard assumption $\mathrm{PSPACE} \nsubseteq \mathrm{P/poly}$, $\mathrm{SORT\textrm{-}BOUND\textrm{-}U}$ is not $\le_m^p$-hard for $\mathrm{PSPACE}$ (hence not $\le_m^p$-complete), so PSPACE-completeness is false in that model. Argument: $\mathrm{SORT\textrm{-}BOUND\textrm{-}U}$ is a unary threshold/tally language $\in \mathrm{P/log}\subset \mathrm{P/poly}$; $\mathrm{P/poly}$ closed under poly-time many-one reductions would imply $\mathrm{PSPACE}\subseteq \mathrm{P/poly}$ if it were PSPACE-hard. This is a clean closure barrier (analogous in spirit to sparsity barriers; stronger here than sparsity alone given $\mathrm{P/poly}$ membership).

**Concrete failed/obstructed approach:** Direct reduction from arbitrary PSPACE-complete games (e.g. QBF) to the antichain sorting game $G(n,k)$ faces structural obstructions - adversary must remain consistent with some total order (not free), moves restricted to pairwise comparisons, state is poset lattice; Claim A shows the game is in PSPACE by ATM simulation but simulation direction differs from many-one hardness. Making this unconditional is nontrivial.

**Honest limits:** No unconditional proof (needs $\mathrm{PSPACE}\nsubseteq \mathrm{P/poly}$). Doesn't place $\mathrm{SORT\textrm{-}BOUND\textrm{-}U}$ in $\mathrm{PH}$, only rules out many-one PSPACE-hardness/completeness under that plausible assumption. Distinguishes general-poset ($\mathrm{GEN\textrm{-}SORT}$) transfer from antichain case; certificate soundness/completeness gaps remain open.


## Other metadata

```json
{
  "finished_at": 1793681616.1148434,
  "started_at": 1793678328.9357843
}
```
