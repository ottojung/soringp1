# unary-alternation-depth-lower-bound

## status

investigated

## origin

ai_proposal_unverified

## agent_id

I81Vm6fp4wks5fiG6n2edQ-loves

## exit_state

clearexit

## question

For all sufficiently large n, must every alternating Turing machine deciding SORT-BOUND-U on inputs encoding (n,k) with k near S(n) use Omega(S(n)) alternation rounds in the worst case over all sorter/adversary lines, ruling out any simulation that compresses the O(n log n) natural game alternations by more than a constant factor?

## basis

APTIME=PSPACE and the G(n,k) ATM model in problem.md; prior bounded-alternation front argued unbounded fixed levels but left the asymptotic rate of alternation depth open as a separate all-n question.

## falsifier

Construct an alternating algorithm (or uniform simulation) that decides SORT-BOUND-U in time polynomial in N=n+k+1 using o(S(n)) alternations for all large n, with an explicit correctness proof and alternation-count analysis tied to the actual unary input metric.

## implication

A tight Theta(S(n)) alternation lower bound would fix the exact alternation complexity of the unary threshold game and sharpen the PSPACE upper bound to a more precise alternating-time class, distinguishing 'unbounded' from the true depth of this minimax problem without claiming PSPACE-completeness.

## finding_unverified

 yielding $\mathrm{SORT\text{-}BOUND\text{-}U}\in\mathrm{APTIME}=\mathrm{PSPACE}$.
- **Compression question:** Can we do better than $\Theta(S(n))$ alternations while keeping time polynomial in $N=n+k+1$? That would mean placing the game into some $\mathrm{ATIME}(\mathrm{poly}(N), o(S(n))) \subset \mathrm{PSPACE}$ (potentially inside $\mathrm{PH}$ if sublinear/constant in a suitable sense) rather than full polynomial alternations.

**Obstructions found (why compression looks hard):**

1. **Adaptive strategy size (completeness/soundness):** A winning sorter strategy is an adaptive function from partial orders (histories) to pairs; optimal strategies are exponential-size objects ($\ge n!$ leaves). An existential block that must “guess” the entire strategy cannot fit in polynomial time/space to represent; you cannot verify an exponential tree by few universal alternations without redoing the search. This matches the certificate barriers (explicit tree not a polynomial witness, no known polynomial succinct certificate).
2. **Move-by-move dependencies:** The choice at round $t$ depends on all previous $\forall$ answers. There is no obvious way to “parallelize” or “block” these dependencies into $o(S(n))$ alternation phases without either (a) committing to a non-adaptive/structured strategy of worse height (impossible to achieve $k\approx S(n)$) or (b) blowing up the witness size beyond polynomial. This is the same adaptive obstruction underlying bounded-alternation-sortbound’s conclusion that fixed levels are implausible.
3. **State/quotient barriers:** The winning frontier gives $2^{\Omega(n\log^2 n)}$ distinct winning states at exact budget (impossible to enumerate), and attempts at state compression show tight limits; adversary state minimality also suggests no cheap compression of the game graph. These don’t directly give an alternation lower bound, but they rule out many “compress by memoization/quotienting” tricks.
4. **Root quantifier / general-poset non-transfer:** Hardness for arbitrary posets doesn’t transfer to the antichain root; the obstruction must be specific to this fixed family. The above are structural to the root game, not generic poset reductions.

**Failed approach / exact obstruction:** I could not construct an $o(S(n))$-alternation ATM algorithm, and no standard technique (strategy guessing in blocks, treewidth/quotient compression, trading alternations for space/time while keeping polynomial time) appears to preserve correctness at height $S(n)$ without exponential witness size. The closest existing result is the bounded-alternation front concluding unbounded fixed levels are unlikely, but no formal $\Omega(S(n))$ alternation lower bound exists in the repo/literature I reviewed. Also note: $\mathrm{SORT\text{-}BOUND\text{-}U}$ is sparse and in $\mathrm{PSPACE}$, so an alternation lower bound wouldn’t imply $\mathrm{P}\neq\mathrm{PSPACE}$ by itself—it would just sharpen the alternation class; the “PH collapse” route is blocked by sparsity/Mahaney in the usual forms.

**Honest limits:** No new theorem or counterexample was produced. The falsifier (explicit $o(S(n))$-alternation polytime ATM with proof) was not achieved; the obstruction is a paper-level complexity argument about strategy size/adaptivity, not a kernel-checked lower bound. Distinction maintained: general-poset results don’t apply, and this is about alternation *rounds/depth* of the game ATM (not just certificate soundness alone). No Lean/repo changes made.

## Other metadata

```json
{
  "finished_at": 1793424392.8537142,
  "started_at": 1793423228.9135187
}
```
