# descent-family-evaluator-complexity-transition-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

ZG20LXterdxufLjuXGu3e6-induced

## exit_state

clearexit

## question

For the d-descent permutation universe X_d(n), whose exact minimax F_d(n) runs from F_1(n)=B(n)=n+O(log n) up to F_{n-1}(n)=S(n), is exact evaluation of F_d(n) polynomial-time for every fixed constant d, and does the jump to 2^{Omega(n log^2 n)} evaluation complexity occur only once d grows like n/log n?

## basis

Board #301 descent-depth theorem (23:06Z: F_d = n log2(d+1) + O(n), d* = ceil(n/log2 n)) and binary-rate result (~23:3xZ: B(n) <= n-1+ceil log2(n-1)); winning-frontier barrier (23:32Z); an independent small-n minimax check is consistent with F_1=B and F_{n-1}=S for n<=6. No descent front appears in the 660-front ledger; distinct from the just-dispatched compact-f-statistic statistic question.

## falsifier

A polynomial-time exact evaluator of F_d(n) at d = Theta(n/log n), giving polynomial-time S(n), or a rigorous 2^{Omega(n)} lower bound for exact evaluation already at some fixed constant d >= 2.

## implication

A uniform polynomial evaluator for all d would put S_unary in FP; a sharp transition would locate exactly where restricted-family hardness begins and tighten the n log^2 n exponent barrier for exact evaluation.

## finding_unverified

uniform `2^{Ω(n)}` lower bound at fixed d≥2 would require lower‑bound methods that do not exist for any natural PSPACE problem; AGENTS.md forbids pursuing this. Both falsifiers thus fail, for independent reasons.
- **F3 — rigorous state‑count barrier (all n≥2, all d≥1), method not function.** The standard partial‑order minimax recurrence visits at least `2^{n−1}` distinct states: for each `T ⊆ {1,…,n−1}`, `S_T = X_d ∩ {π_i < π_{i+1} ∀ i∈T}` is reachable (identity permutation keeps every branch nonempty), and the single‑descent permutation at `i ∈ T\T'` separates `S_T` from `S_{T'}`. Verified exactly for n≤7 (2,4,8,16,32,64); full reachable‑state counts are larger (4168 at n=6,d=1; 59718 at n=6,d=2). So evaluating F_d via the only known exact method costs `2^{Ω(n)}` **even at d=1** — the structural theorem does not give poly‑time by this route, and any d‑dependent transition cannot be located at the recurrence's state count.

## Concrete failed approaches
- **Width DP:** states have width ≤ d+1, but width‑(d+1) posets number `2^{Θ(n log n)}` and positions carry descent labels — no compression.
- **Known‑boundary merge DP:** polynomial if boundaries are known, but the optimal tree need not scan adjacent positions, so general partial orders (not just boundary info) are reachable; I could not close it.
- **Closed form via Hwang–Lin:** only covers two‑list merging; exact optimal merging of ≥3 lists with unknown boundaries is not in the repo baseline and web search is cancelled here.

## Distinguishing soundness/completeness and general posets
The constructive upper bound is a *sound* certificate (`F_d ≤ n⌈log2(d+1)⌉+n`), not a completeness result; for `d=3` the known bounds are `2n−O(log n)` vs `3n`, a Θ(n) gap, so exact `F_d` — and hence NP‑membership — is not established. General‑poset sorting hardness does not transfer to the special union‑of‑chains family `X_d(n)`, and our constructions do not apply to general posets.

## Honest limits
**[E] remains open.** I have not built a poly‑time evaluator for fixed d≥2 and cannot prove an evaluation lower bound for a tally function. The genuinely new content is F1–F3 and the documented failed approaches. No consequence for S(n), SORT‑BOUND‑U, or any P/NP/PSPACE claim. The decisive obstacle is a computational principle other than the minimax recurrence that computes F_d(n) exactly (a closed form or a compressed state invariant), or a proof none exists — both beyond current techniques.
Recovery check: the previous turn already completed and its external side effect is confirmed.

- **Git/worktree**: clean on `billy-dev` at `6a96398` (`git status --short --branch` empty).
- **Board #301**: the single intended post is present — `[2026-11-21T23:56:54.605Z] SoringP1 researcher: descent-family-evaluator-complexity-transition-alln` (verified via `board_digest.py --contains "descent-family-evaluator-complexity-transition-alln"`).
- **No duplicates made**: I did not repost, commit, or change repo/ledger state.

No unfinished work remains for this front. The reported finding stands as posted: falsifier (a) is mis-specified (poly eval at `d=Θ(n/log n)` does not give S(n)); falsifier (b) is unachievable by known techniques for a tally language; and the standard minimax recurrence has a rigorous `2^{Ω(n)}` reachable-state barrier for every fixed `d>=1` (method barrier, not a function lower bound). **[E] poly-time exact evaluation for fixed constant d remains open**; no S(n)/SORT-BOUND-U/P/NP/PSPACE consequence.

## Other metadata

```json
{
  "finished_at": 1795305603.3675458,
  "started_at": 1795304521.477316
}
```
