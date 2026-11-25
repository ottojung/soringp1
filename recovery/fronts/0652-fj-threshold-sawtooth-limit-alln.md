# fj-threshold-sawtooth-limit-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

wRZThnzGHJrJG8tIN6hH7k-clenched

## exit_state

clearexit

## question

Does the info+FJ certifiable-band threshold t(n) - the least split size a for which C(n) >= F(a)+F(n-a)+a+1 is reported to hold - have a well-defined limiting ratio t(n)/n as n ranges over all n, given the reported Ford-Johnson ceiling sawtooth in Delta(m)/m (finite envelope about [0.02724,0.11401]) and the reported spread of observed t(n)/n values across 1000<=n<=5000?

## basis

Board #301 18:03Z infofj-certifiable-band result (t(n)=Theta(n), rigorous liminf/limsup envelope only) and the 18:25Z Viche referee corrections (finite-m excess envelope ~[0.02724,0.11401], sawtooth dips near (4/3)*2^j, pointwise-limit question explicitly left open).

## falsifier

Either prove that t(n)/n converges to a single constant, or exhibit two infinite subsequences of n (for instance near (4/3)*2^j versus near the dyadic points 2^j) whose t(n)/n ratios have distinct limit points, refuting convergence.

## implication

A genuine non-convergence would show that any lower-bound recurrence for S(n) resting on one constant-fraction split band is incomplete: it would have to track the Ford-Johnson ceiling sawtooth rather than a single epsilon, sharpening the 17:30Z balanced-split theorem.

## finding_unverified

he dominant term `r(b)` is the sawtooth at *n's dyadic mantissa* — it does not average out. For `n=2^j`, `b`'s mantissa → 2, so `r(b)→c`; for `n≈(4/3)2^j`, `b`'s mantissa → 4/3, so `r(b)→R(4/3)`. The entropy root is strictly increasing there, forcing distinct limits. (The small-part term `ε·r(a) ≤ 0.02·0.114` shifts ε by <0.0004, far below the 0.0144 gap.)

**Checks:** F closed form matches literature (`F(12)=30, F(22)=71, F(50)=219`) and the defining sum; `C(n)` via `lgamma` matches exact `(n!−1).bit_length()` through n=50,000; `P` is monotone in `a` in wide windows at j=12,17,20 (binary search = true min); the exhaustive 1000–5000 range of my predicate reproduces the referee's min 0.003635 @ 2751 and max 0.019151 @ 1932 exactly.

## Serious disproof attempt that failed — and the exact obstruction

I tried to prove convergence by arguing that the entropy equation has a single root and the sawtooth "washes out". It fails for a precise reason: the threshold is an *instantaneous* function of `Δ(b)/b` at the linear-scale point `b=n−t(n)`, and the mantissa of `b` is determined by the mantissa of `n`. There is no averaging over dyadic blocks — one dyadic scale, one sawtooth value, one entropy root. The 18:03Z result already observed oscillation but left the pointwise limit open; the obstruction is that closing it requires `Δ(n)/n` to converge over *all* n, which is false (two ray limits 0.10936 vs 0.02766, confirmed to j=22).

## Soundness vs completeness; scope

- This is about the fixed antichain-root family and the **sufficient** predicate `P(a,b): C(n) ≥ F(a)+F(b)+a+1`, which is **sound** for `S(n) ≥ S(a)+S(b)+a+1` (since `S(n)≥C(n)` and `S(m)≤F(m)`). `P` false means only *this certificate fails* — **not** a counterexample to the defect inequality `D`, and not a hardness result for general posets. No general-poset transfer is used or claimed.
- No completeness claim: nothing here is a checkable proof system for `SORT-BOUND-U`, and no complexity placement or separation follows (sparsity/tally barriers remain).
- On the front's complexity implication: the honest verdict is **qualified**. Non-convergence shows a single fixed `ε` does not describe the *reach of this sufficient certificate* — near `(4/3)2^j` splits as small as `0.0034n` are certified, near dyadic points only `0.0177n` — so a recurrence hard-coding one `ε` leaves certifiable strength unused. But this does **not** sharpen what is known about `S(n)` itself: `P` is sufficient, not necessary, and the 17:30Z balanced-split theorem remains true and unaffected. Claiming "any lower-bound recurrence for `S(n)` is incomplete" would overstate the result.

## Honest limits

- Result is paper-level, not kernel-checked; no Lean/repository change was warranted (publication gate: structural scope result, no improved bound or algorithm).
- The exact limiting constants rely on the asymptotic analysis of `Δ`; the finite-m envelope `[0.02724,0.11401]` and sporadic above-envelope excursions (e.g. 0.019151 @ n=1932) are finite-n effects and do not affect the two limit points.
- `S(n)`, `SORT-BOUND-U`, the defect inequality `D`, and all complexity-class questions remain open. The set of limit points of `t(n)/n` is now characterized (interval ≈[0.00339,0.01835] with the sawtooth profile), but I claim no closed form beyond the entropy/FJ fixed-point equation.

No board post, ledger update, commit or other external write was made — if you want this finding filed on #301, say so and I will post it once.

## Other metadata

```json
{
  "finished_at": 1795288001.506037,
  "started_at": 1795285749.061086
}
```
