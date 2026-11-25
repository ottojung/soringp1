# defect-pruning-certificate-completeness-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

BeBURtrUDM1R3VGiSONLcM-mcculloch

## exit_state

clearexit

## question

Does the positive defect D(P)=F(P)-ceil(log2 e(P)) on reachable optimal-play states yield a polynomial-size certificate that a proposed comparison is non-optimal for all n, or does identifying the harder child require solving minimax?

## basis

Board defect-prune-reachable-optplay-alln (first defect at n=6) and soundness-versus-completeness distinction.

## falsifier

Show an infinite family of reachable states with D(P)>0 where no polynomial-size witness identifies a non-optimal comparison without computing F of both children, or prove such a defect certificate exists.

## implication

If defect certificates exist, defect pruning becomes a sound and complete pruning rule for exact evaluation; otherwise the n=6 defect witness remains only a local heuristic.

## finding_unverified

Posted the finding to Antonina #301. No repository, Lean, test, CI, or ledger changes were made; scratch computations only.

## Mathematical finding

For the defect-pruning question, the answer is the second horn: **identifying the harder child still requires solving minimax (equivalently the #P linear-extension threshold), not merely exhibiting defect.**

Exact computation for `n ≤ 6` (130,023 labelled posets at `n=6`) shows:

- `D(P)=F(P)-⌈log₂ e(P)⌉` is 0 or 1; the first positive-defect state is the known witness `(30,16,8,0,0,18)`, with `F=5`, `e=16`, `L=4`, `D=1`.
- For `D=1` parents, non-optimal comparisons are exactly those whose harder child has **no drop** in `L=⌈log₂ e⌉`: `L(child)=L(parent)`. Optimal harder children instead have `L(child)=L(parent)-1` (or lower).
- Thus non-optimality in this regime is the threshold statement `e(child) > 2^{L(parent)-1}`.

Counting linear extensions is #P-complete (Brightwell–Winkler), and they observe that an easy count would immediately yield the optimal next comparison. So no polynomial-time test or polynomial-size witness for this threshold is known; certifying it would require solving #P or supplying an exponentially large extension set. Knowing `D(P)>0` is itself as hard as computing `F(P)`.

## Honest limits

- Verified only through `n=6`; no `D>1` observed yet.
- No all-`n` construction of positive-defect states with non-optimal comparisons, and no `#P ≠ P` claim.
- The `n=6` witness therefore remains a local heuristic: defect pruning is strictly stronger than information pruning at `d=L(P)`, but only once `F(P)` is already known.

## Other metadata

```json
{
  "finished_at": 1795410625.0193825,
  "started_at": 1795409776.6645586
}
```
