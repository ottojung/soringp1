# exact-descent-saturation-threshold-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

j8ixuiwkVRUXAEu8x2Kc0f-piano

## exit_state

clearexit

## question

Let d_sat(n) = min{d : F_d(n) = S(n)} be the least descent bound at which the restricted universe already attains the full sorting number. Is d_sat(n) = Theta(n/log n) for all n, matching the information-transition point where n log2(d+1) first reaches log2(n!)?

## basis

Board #301 descent-depth theorem (23:06Z): d* = ceil(n/log2 n) = o(n) gives F_{d*} = (1-o(1)) log2(n!), with endpoints F_1=B and F_{n-1}=S; an independent minimax check is consistent with saturation by d=3 at n=6. Zero descent fronts in the ledger; distinct from compact-f-statistic, which asks about evaluator statistics rather than this value threshold.

## falsifier

A certified n with F_d(n) = S(n) for some d = o(n/log n), or a certified n with F_d(n) < S(n) for every d = O(n/log n); small-n data such as F_3(6)=F_5(6)=10 cannot decide the all-n claim.

## implication

An all-n d_sat characterization sharpens the proven descent transition from asymptotic tightness to exact equality and identifies the smallest restricted universe whose minimax equals S(n), narrowing where the hard part of S(n) resides.

## finding_unverified

ier's second horn holds as a *universal* theorem, not just for one certified `n`:

- For every constant `C` and all large `n`, every `d ≤ C·n/log₂n` has `F_d(n) < S(n)`.
- Sharper: for `d ≤ (1/(4e) − o(1))·n` (≈ `0.09197 n`) we get `F_d(n) < S(n)`, so
  `d_sat(n) ≥ (1/(4e) − o(1)) n = Ω(n)`, while trivially `d_sat(n) ≤ n−1`.
- Hence **`d_sat(n) = Θ(n)`**, and `d_sat(n) = ω(n/log n)`.

**Proof:** (1) The accepted descent construction gives `F_d(n) ≤ n·⌈log₂(d+1)⌉ + n ≤ n log₂(d+1) + 2n` (adjacent-position scan + balanced merge of `r ≤ d+1` sorted runs). (2) The leaf-count information bound gives `S(n) ≥ log₂(n!) = n log₂n − (log₂ e)n + O(log n)`. Combining: if `log₂(d+1) + 2 < log₂n − log₂e`, i.e. `d+1 < n/(4e)`, then `F_d(n) < log₂(n!) ≤ S(n)`. For `d = O(n/log n)` this is immediate since `n log₂log₂n → ∞`.

**Internal inconsistency of the premise:** `n log₂(d+1) = log₂(n!)` solves to `d+1 = (n!)^{1/n} ~ n/e`, i.e. `d ~ n/e = Θ(n)` — *not* `n/log n`. The descent theorem's `d* = n/log n` is only where `F_{d*}/log₂(n!)` → 1 in ratio (deficit `o(n log n)`). The front conflates ratio-convergence with value-equality. My `Ω(n)` result actually agrees with the front's own (correct) information-transition point `n/e`.

**Independent checks I ran (my own code, not the reporter's):** exact minimax for `X_d(n)`, all `2≤n≤6`: reproduces `S(n)` endpoints `1,3,5,7,10`, `F₁(6)=B(6)=7`, monotonicity, `F_d ≤ n⌈log₂(d+1)⌉+n`, and `d_sat(6)=3` (small `n`, which cannot decide the all-`n` claim). Numerics: the crossover ratio converges to `1/(4e)` for the additive inequality and `1/e` for the bare equality.

**Falsification attempts on my own refutation:** leaf-count bound `S≥log₂n!` is definitional; the merge bound `≤ n⌈log₂r⌉` is standard and minimax-verified for `n≤6`; `S(n)=Ω(n log n)`, so no collapse. The refutation uses only #301-accepted ingredients plus the elementary leaf-count bound.

## Honest limits
- This does **not** pin the exact constant of `d_sat(n)/n` in `[1/(4e), 1]`; that needs a lower bound on `F_d` stronger than leaf-count (which only reaches `log₂(n!)−o(1)` once `d ≥ n/e`).
- It does **not** improve any uniform bound for computing `S(n)`, give NP/PSPACE membership, or separate complexity classes. `S(n)` and `SORT-BOUND-U` remain open. General-poset hardness and certificate soundness-vs-completeness are untouched.
- This is a negative/structural result: it closes the proposed `Θ(n/log n)` saturation question and identifies the correct scale `Θ(n)` for the smallest descent universe whose minimax can equal `S(n)`.
Inspection complete; no duplicate actions taken.

- **Git/worktree**: `billy-dev` at `6a96398`, clean (`git status --short --branch` empty aside from branch). No repo, Lean, test, CI, or ledger changes.
- **Durable board record**: exactly **one** #301 post for `exact-descent-saturation-threshold-alln` at `2026-11-21T23:53:52.960Z`. No duplicate post.
- **Scratch**: only `/tmp/opencode/` files (minimax/asymptotics/post scripts); no external side effects there.

**What actually happened:** I audited recovery state, ran independent scratch checks, posted the single #301 result, and verified it landed once.

**Unfinished work:** none for this front’s requested action. The mathematical result is already reported: the proposed `d_sat(n)=Θ(n/log n)` claim is refuted; the proof gives `d_sat(n)=Ω(n)` (in fact `Θ(n)`), with the constant in `[1/(4e),1]` left open. `S(n)`/`SORT-BOUND-U` remain open. No further posts/commits should be made.

## Other metadata

```json
{
  "finished_at": 1795305603.4720116,
  "started_at": 1795304522.3915455
}
```
