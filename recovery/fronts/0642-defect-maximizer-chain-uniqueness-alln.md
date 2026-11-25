# defect-maximizer-chain-uniqueness-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

woqZenqy18eAdNIXAeXM4K-losing

## exit_state

clearexit

## question

The 10:20Z board result shows the b-chain C_b attains the maximum of delta(A_a,B) over all b-element hosts B; for every a >= 1 and b large, is C_b the unique isomorphism-type maximizer, or are there infinitely many non-chain information-tight hosts B attaining the same maximal defect delta(A_a,C_b)? (An independent two-implementation computation already shows a V-plus-isolated 4-poset ties the chain at (a=1,b=4).)

## basis

Board #301 10:20Z T1/T2 plus an independently checked counterexample (two different minimax algorithms) where a non-chain information-tight host ties the chain maximum at b=4,a=1 while its single-comparability refinement drops strictly below; no ledger front addresses maximizer uniqueness.

## falsifier

Exhibit by exact minimax an infinite family of non-chain b-element posets B with delta(A_a,B) = delta(A_a,C_b) at fixed a, or a single pair (a,b) where a non-chain host has delta strictly above the chain, which would also refute the chain-extremality claim.

## implication

Characterizing the defect maximizers sharpens the extremal law for the superadditivity recursion F(A_a disjoint-union B) >= F(B)+S(a)+min(a,b)+1 and determines whether defect upper envelopes need only chain-host strategies; this is structural and separates no complexity class.

## finding_unverified

idate infinite family with a fresh, independent exact-minimax computation (scratch only, no repo changes).
The independent exact minimax confirms the family ties the chain for every tested b (3–8) and reproduces the cited (1,4) example. Now let me determine the board-posting mechanism so I can report the falsification once (no prior post exists).
I have a rigorous result: a general sufficient condition for equality in the chain-extremality law at `a=1`, plus an explicit infinite family. It also explains the previously observed `(1,4)` tie. Let me write the board report (one post only) and verify no duplicate exists immediately before posting.
Post succeeded. Let me verify it appears exactly once.
## Result: uniqueness is refuted — an infinite family of non-chain maximizers at `a = 1`

**Recovery audit.** No side effects from the interrupted turn: worktree clean at `6a96398` on `billy-dev`, no scratch files for this front, and board #301 pages 1–5 had **0** posts with my author tag. I made exactly **one** board comment (verified: 1 hit, `2026-11-21T10:39:18Z`). No repo, Lean, test, CI, ledger, or main changes.

### The theorem (paper proof)

Let `F(P)` be the exact adaptive minimax cost of identifying the unknown linear extension, `delta(A_a,B) = F(B ⊔ A_a) − F(B) − S(a)`, and "information-tight" mean `F(P) = ⌈log₂ e(P)⌉`.

**T0 (sufficient condition, `a = 1`).** If a `b`-element host `B` is information-tight with `e(B) = 2^k`, then `delta(A_1,B) = delta(A_1,C_b) = ⌈log₂(b+1)⌉`.

*Proof:* `F(B) = k`. From the 10:20Z composition bound, `F(B ⊔ A_1) ≤ F(B) + F(C_b ⊔ A_1) = k + ⌈log₂(b+1)⌉` (binary insertion is optimal for `C_b ⊔ A_1`). The information bound gives `F(B ⊔ A_1) ≥ ⌈log₂(2^k(b+1))⌉ = k + ⌈log₂(b+1)⌉`. Both bounds coincide, so `delta = ⌈log₂(b+1)⌉`. ∎

**Corollary (infinite family).** For every `b ≥ 3`, let `Vcap_b = {x<y, x<z, y,z < t₁ < … < t_{b−3}}` (the 3-element `V` when `b=3`). It is non-chain, `e = 2`, `F = 1`, so T0 applies. These are pairwise non-isomorphic, information-tight, non-chain maximizers for **all** `b ≥ 3`: `C_b` is not the unique isomorphism-type maximizer, and there are infinitely many `b` with non-chain maximizers.

T0 also *explains* the previously observed `(1,4)` tie: `V`-plus-isolated has `e = 8 = 2³`, `F = 3`, hence `delta = 3 + ⌈log₂5⌉ − 3 = 3 = delta(A_1,C_4)`.

**Independent check (experiment).** A fresh from-scratch minimax over sets of surviving linear extensions (no project code) reproduced `S(1..5) = 0,1,3,5,7` and `delta(Vcap_b,A_1) = 2,3,3,3,3,3,4` for `b = 3..8`, each equal to `⌈log₂(b+1)⌉`; it also reproduced `F(V+isolated)=3, F(+A₁)=6, delta=3`.

### Honest limits

- **What fails is uniqueness only.** Chain *extremality* (T1, 10:20Z) is untouched: the family attains the maximum and never exceeds it; the "strictly above" falsifier remains impossible by T1's proof.
- **T0 is sufficient, not necessary** — I do not claim a full equality classification.
- **No extension to `a > 1`**: power-of-two `e(B)` makes ceilings additive only for `a=1`; for `a>1`, `F(C_b ⊔ A_a)` can exceed `⌈log₂ C(a+b,a)⌉`, which is the exact obstruction to the same argument.
- **No complexity consequence.** This is structural (sharpening the equality cases of the disjoint-union defect envelope). It separates no class; `S(n)` and `SORT-BOUND-U` remain open. No Lean or repository changes were made.

Board report: Antonina #301, `10:39:18Z`, author `SoringP1 researcher: defect-maximizer-chain-uniqueness-alln` (posted once).

## Other metadata

```json
{
  "finished_at": 1795257624.2329884,
  "started_at": 1795256852.4812376
}
```
