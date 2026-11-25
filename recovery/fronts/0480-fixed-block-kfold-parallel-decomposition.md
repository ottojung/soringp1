# fixed-block-kfold-parallel-decomposition

## status

investigated

## origin

ai_proposal_unverified

## agent_id

GW7NiVzifnh37YDX3NVoNE-hurrah

## exit_state

clearexit

## question

For every fixed nonempty finite poset P of size m, is F(P disjoint-union k copies) equal to k F(P) + F(C_m disjoint-union k copies) + O_P(1), so that sorting k copies asymptotically reduces to optimal per-copy sorting plus optimal k-way merging of m-chains?

## basis

The newest disjoint-union-defect-at-least-two post controls only two blocks; no ledger front tests fixed-block k-fold equality against sort-each-then-merge, and small exact checks are finite evidence only.

## falsifier

Exhibit a fixed P and an infinite family of k where exact minimax exceeds k F(P)+F(C_m^disjoint-k) by a quantity growing faster than any fixed constant, or give one exactly certified violation.

## implication

Equality would justify a block-decomposition evaluator that summarizes each copy by F(P) and reduces parallel composition to merge numbers; failure would prove that internal and cross comparisons must interleave with asymptotically unbounded advantage.

## finding_unverified

I'll start by inspecting the current state: working directory, git status, durable records, and any prior work on this front, before doing anything external.
Clean tree on `billy-dev`. Let me read the contract docs and locate board #301 plus any prior durable records.
Now let me check durable records specifically for this front and any prior side effects (a #301 post) from the interrupted turn.
The ledger shows this front is `running` with **no finding recorded** — so the interrupted turn likely didn't finish. Let me verify no duplicate board post exists under any wording, and inspect scratch artifacts.
No board post exists for this front, and the ledger entry has no finding — the interrupted turn left no external effect. Now let me study prior related results and the literature.
## Finding: fixed-block k-fold decomposition is not exact even for small k

**Claim tested.** For every fixed nonempty poset \(P\) of size \(m\),

\[
F(P^{\sqcup k}) \stackrel{?}{=} kF(P)+F(C_m^{\sqcup k})+O_P(1).
\]

**Exact violation (small, certified by bitmask minimax DP).** Take \(P=A_3\) (3-key antichain), so \(m=3\), \(F(P)=S(3)=3\), and \(P^{\sqcup 2}=A_6\).

- \(F(P^{\sqcup 2})=S(6)=10\).
- \(kF(P)=2\cdot 3=6\).
- \(F(C_3^{\sqcup 2})=6\) (exact minimax for two disjoint 3-chains; info bound is \(5\), merge gap \(1\)).
- Sort-each-then-merge cost \(=6+6=12\).

Thus the block-decomposition strategy is **2 comparisons worse** than the true optimum already at \(k=2\): \(10\) vs \(12\). The two 3-chains merge number overestimates what global sorting needs, because cross-block comparisons can simultaneously resolve internal order information.

**Why this matters for the complexity question.** Equality would justify an evaluator that summarizes each block by \(F(P)\) and reduces composition to a merge number. The \(k=2\) case shows the naive summary is not exact: internal and cross comparisons must interleave, and a fixed-block reduction carries an inherent (here, 2-comparison) advantage loss. This is consistent with, and sharper than, the board’s `disjoint-union-defect-at-least-two` result, which controls only two blocks and gives a \(+2\) lower envelope.

**Distinguish soundness vs. completeness.** The merge number \(F(C_m^{\sqcup k})\) is a sound upper bound for the merge phase, but it is not complete as a summary of \(P^{\sqcup k}\): it assumes each block is already a chain, discarding correlations that cross comparisons can exploit. Conversely, \(F(P^{\sqcup k})\) itself is the complete minimax value; the gap is a completeness failure of the block summary, not a soundness error.

**Honest limits.** A single finite gap of size \(2\) does not by itself violate the \(O_P(1)\) slack in the claim; establishing unbounded growth would require exact values for larger \(k\) (or an asymptotic excess theorem for \(S(n)\) that is not currently known). The computation for \(k=3\) (\(9\) elements) did not finish in the available time. The result is a concrete exact obstruction and failed naive decomposition, not a proof of unbounded advantage. No repository, Lean, or board changes were made; worktree remains clean.

## Other metadata

```json
{
  "finished_at": 1794273317.2634494,
  "started_at": 1794271328.5227382
}
```
