# balanced-fj-sufficiency-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

2YnFP2SECfYxPn7J3N5RsB-gallows

## exit_state

clearexit

## question

Does the information-plus-Ford-Johnson sufficient condition hold for every balanced split? Precisely, for all n>=3 with a=floor(n/2) and b=ceil(n/2), is ceil(log2 n!) >= F(a)+F(b)+min(a,b)+1, where F is the Ford-Johnson upper bound, so that the antichain defect inequality S(n)>=S(a)+S(b)+min(a,b)+1 is certified on all balanced splits for every n?

## basis

Fresh #301 finite-range theorem (16:42Z/16:45Z) proves the antichain defect inequality for a+b<=50, and the referee integer check reports balanced splits satisfy the condition for a<=5000; the asymptotic FJ slack suggests it may persist, but this is a conjecture, not an established all-n claim.

## falsifier

Find any n with ceil(log2 n!) < F(floor(n/2))+F(ceil(n/2))+floor(n/2)+1 by exact integer computation, refuting balanced-split sufficiency and bounding how far the information-plus-FJ method can certify the defect inequality.

## implication

Would extend the board's n<=50 certified antichain defect theorem to all balanced splits, yielding a substantive lower-bound recurrence for exact unary S(n); a refutation would delimit the information-plus-FJ method to finitely many n.

## finding_unverified

The corrected exact check finds **zero violations** for all n in [3, 50000] (min margin 0 at n=3,4,5 — tight), and float screening to 10⁶ finds none, with slack growing ≈0.414n. Now let me rigorously verify my analytic all-n proof bound (so the result isn't just finite computation) and measure the asymptotics precisely.
The mathematics is now solid. Let me verify the exact-check independence once more with a fresh implementation (to avoid any coding artifact), then prepare a single board post.
The fresh script was too slow (recomputing factorial each n). Let me optimize it while keeping it independent of the closed-form grouping.
Independent re-derivation confirms the result. Let me check the board post command syntax, then post exactly once.
Everything checks out. Now let me write the report and post it exactly once to #301.
The JSON output shows the issue body rather than the confirmation. Let me verify the comment was actually posted exactly once.
The post is confirmed: exactly one comment at 17:30:30Z, no duplicate. Let me do a final state audit.
Done. Here is my report.

## Mathematical finding

**The front's claim is TRUE for all n — the requested falsification failed because no counterexample exists.**

For every `n ≥ 3`, with `a = ⌊n/2⌋`, `b = ⌈n/2⌉`:

```
C(n) = ⌈log₂ n!⌉  ≥  F(a) + F(b) + a + 1
```

where `F(m) = Σ_{k≤m} ⌈log₂(3k/4)⌉` is the Ford–Johnson upper bound. Minimum margin is exactly **0** (tight at n=3,4,5,6) and grows to ≈0.414n (slack 20720 at n=50000).

### Proof (paper-level, two components)

Writing `Δ(m) = F(m) − log₂(m!)`, the condition is equivalent to `log₂ C(n,a) > a + Δ(a) + Δ(b)`. Two explicit bounds close it:

- **(B1)** `Δ(m) < 0.114m + 0.5 log₂ m + 0.63` for all `m ≥ 2`, derived from the exact grouping identity `F(m) = J(m+1) − (2^{J+2}+J−4+⌈J/2⌉)/3`, `J = ⌊log₂(3m−1)⌋−1`, plus the fact that `log₂ s − 2s ≤ −1.9138` on `(½,1]`, minus Stirling's lower bound on `log₂(m!)`.
- **(B2)** `log₂ C(n,a) > n − 1 − log₂ n` (central binomial coefficient bound).

Combining gives sufficiency for all `n ≥ 36` (conservatively; `n ≥ 29` with tighter constants). The range `3 ≤ n ≤ 50000` is covered by an **exact-integer check with zero violations**, done twice independently (closed-form F + exact factorial; and F from the definition by bit tests). The overlap makes it an all-n theorem.

### Consequence
Since `S(n) ≥ C(n)` and `S(a) ≤ F(a), S(b) ≤ F(b)`, this certifies the antichain defect recurrence

```
S(n) ≥ S(⌊n/2⌋) + S(⌈n/2⌉) + ⌊n/2⌋ + 1   for all n ≥ 3,
```

extending the board's 16:42Z finite theorem (a+b ≤ 50) to all balanced splits.

## Honest limits

- This is a **sufficient condition (soundness)**, not a complete method: the same info+FJ method provably *fails* for unbalanced splits — `(1,50)` is the first failure (`C(51)=220 < 221`) and `(1,b)` fails for all `b ≥ 50`. So the defect inequality outside the balanced band remains uncertified by this method.
- A lower-bound **recurrence for the numbers S(n)** is not a lower bound on the *complexity of computing* `S(n)`. No P/NP/PSPACE placement, no faster evaluator; `SORT-BOUND-U` status is unchanged. General-poset hardness results were neither used nor extended.
- No repository, Lean, test, CI, or ledger changes. Scratch scripts only in `/tmp/opencode/balfj/`.

## State audit
Worktree clean on `billy-dev` at `6a96398`. Recovery check found no prior post under my tag; I posted the result to #301 **exactly once** (17:30:30Z, 1 matching message, no duplicate).

## Other metadata

```json
{
  "finished_at": 1795282308.109479,
  "started_at": 1795280739.2001965
}
```
