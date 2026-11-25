# chain-installation-k-safe-lemma-m-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

Up77QQCHQ4zFKg4GtkqiHB-impose

## exit_state

clearexit

## question

For n = s^2 with s = 2^r (r large), let k = S(n) and follow the top-extension chain-installation path from the antichain A_n until the s sorted chains are installed; for every intermediate state Q at depth d write tau(Q) = k - d - log2(e(Q)). Is information viability tau(Q) >= 0 COMPLETE for genuine k-safety there, i.e. does F(Q) <= k - d hold for EVERY such intermediate Q for all sufficiently large r (equivalently F(Q) - log2(e(Q)) <= tau(Q) along the whole path), or does F-nontightness of some partial union of chains violate this infinitely often?

## basis

Newest board #301 result ksafe-winning-frontier-transfer-obstruction-alln (2026-11-23T14:54Z): sharp threshold log2(4/3) confined to the 2-to-3-element chain step, monotone tau accumulation thereafter, and tau >= 0 proved only NECESSARY for k-safety while Lemma M (F(Q) <= k-d) is explicitly left open as 'the next decisive obstacle'. docs/problem.md realistic outcomes and docs/research-winning-frontier-barrier.md Sec. 3.1 (Sergeev sublinear surplus). This is a soundness-versus-completeness question on the fixed antichain family, not a general-poset hardness transfer.

## falsifier

Exhibit, for infinitely many r, an intermediate union-of-chains state Q on the top-extension installation path at budget k = S(s^2) with tau(Q) >= 0 but F(Q) > k - d(Q); a constructive family or a rigorous existence argument both count. A single finite counterexample is not enough.

## implication

A positive all-large-r answer supplies the missing Lemma M and makes the k-safe transfer from the winning-frontier construction go through at the exact optimal budget, showing that enumeration barrier cannot be converted into a certificate-size lower bound by that route; an infinite-family negative answer blocks the transfer for infinitely many n and identifies a concrete sufficiency gap between information slack and minimax safety. Neither horn alone places SORT-BOUND-U in any class.

## finding_unverified

chain-installation obstruction shape (a 2-chain state before/at the binding step family), but note n=9 is not of the form `s^2, s=2^r`.

I also saw `n=10, (2,2,2,2,2), d=5, S(10)=22, tau=0.794, CanSort(17)=FALSE` but the subsequent exact-F search hit the F=50 sentinel/oom path in that run; I do **not** report n=10 as a confirmed value.

### Strict-rare split lemma (exhaustive small-n evidence)

I exhaustively checked all posets on n<=6 (134,737 labeled poset closures, 482,115 rare-outcome incomparable-pair splits): **0 violations** of `p=e_child/e < 1/2 => F(child) <= F(P)-1`; violations occur only at exactly balanced `p=1/2` (the known prime-defect phenomenon). This is **[experiment]**, not a proof. If a general `p<1/2 => F(child)<=F(P)-1` lemma were true, it would give a strong sufficient condition along top-extension steps with `p<=1/3`, but I do not have a proof and the p=1/2 boundary is real.

## Assessment against the front

- **The asked-for all-large-r positive answer is not established.** I found no proof of Lemma M / tau-completeness on the whole top-extension path.
- **The asked-for infinite-family falsifier is not established either.** The n=9 candidate is a single finite case, `n!=s^2, s=2^r`; the front explicitly says "A single finite counterexample is not enough." Also the n=9 value needs independent solver confirmation because of the packing bugs encountered.
- **Most plausible status: likely false / fragile, but open as stated.** The n<=8 exact data show no violation, while the n=9 candidate suggests the first genuine k-safety gap may appear exactly where information slack is small (`delta ~0.53`, tau at the 2-chain endpoint). The 14:54Z threshold `delta<log2(4/3)` was only a necessary information obstruction; the real obstruction for completeness is `Delta(Q)=F(Q)-log2 e(Q) <= tau(Q)`, i.e. non-tightness of intermediate union-of-chains states. That is exactly Lemma M.
- **Complexity implication (as requested, neither horn alone places SORT-BOUND-U):** A confirmed infinite-family negative answer would block this k-safe transfer route for those n, identifying a concrete sufficiency gap between information slack and minimax safety. A positive all-large-r answer would supply Lemma M and make that transfer go through, ruling out this enumeration/certificate-size barrier route — but it would not by itself place SORT-BOUND-U in P/NP/coNP/PSPACE or prove any separation.

## Concrete next decisive step

1. **Independently recheck n=9 (2,2,2,2,1)** with a separate exact solver / different representation (or a hand-checkable lower-bound certificate) to confirm `F=16`. If confirmed, test n=16? No, n=16 is large; but test other n with small delta and the same shape, and try to lift to an infinite family of `s^2` by a structural argument.
2. **Prove or refute the strict-rare lemma**: `p<1/2 => F(child)<=F(P)-1`. It holds for all 482k rare splits at n<=6; a proof would settle the top-extension step except p=1/2, and a counterexample would be very informative.
3. **Target Lemma M directly as a merge-nontightness bound**: bound `F(Q)-log2 e(Q)` for unions of <=s chains along the path by a chain-merging/insertion argument (Ford-Johnson/merge-insertion style gives upper bounds on F but needs to be compared to tau). This is the actual mathematical gap, not more state enumeration.

**No repository changes, no Lean, no board post made.** All claims above are labeled; n>=9 computation is explicitly tentative pending independent confirmation.

## Other metadata

```json
{
  "finished_at": 1795451557.6219068,
  "started_at": 1795447566.2682538
}
```
