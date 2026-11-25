# antonina-wRZThnzGHJrJG8tIN6hH7k-clenched

Session: ses_e00a171b6fferUOutxm2l9F7zN
Workspace: /home/lubko/soring-fronts/fj-threshold-sawtooth-limit-alln
Created: 1795285749419; updated: 1795287972931

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 13 (msg_1ff65fd88001yVOmACVaxZq6mY)

I'll start by carefully inspecting the current state — git branch, working directory, and durable task records — before doing anything, since the prompt warns about a possible interrupted turn with existing side effects.

## Output 28 (msg_1ff660c4e001JZLN7yZO4wVwq0)

Good — I'm on `billy-dev` with a clean working tree, so no interrupted repository changes. Let me read the key docs and find board #301.

## Output 47 (msg_1ff661fdc0014Jpa7mV7lGaqbQ)

Now let me check the board #301 (via the digest script), the durable frontier ledger, and the exact front description to understand what's been done.

## Output 62 (msg_1ff66309300122cj5xCdLvzYnL)

The front lives on the board, not in the repo. Let me query board #301 for the relevant posts (sourcing the profile first as operations requires).

## Output 73 (msg_1ff664350001y8yVW4fPAryrFV)

I need the full text of the two key posts (18:03Z result and 18:25Z referee corrections). Let me pull them into scratch files, not the repo.

## Output 100 (msg_1ff66880c0015Kb1AfWTReBYyb)

Let me check the ledger entry for this front and look for any scratch work from an interrupted prior turn on this specific question.

## Output 120 (msg_1ff66af50001DushB7j71NCUan)

I now have the full context. There's no prior scratch work or board post for this specific front — it's fresh. Let me verify the key computation with exact integer arithmetic in scratch space (`/tmp/opencode/fjlim`), never in the repo.

## Output 159 (msg_1ff7e5700001gelnI1Dxw0DKXd)

The scratch computation was killed — it tried to compute `n!` exactly for n up to 8M (impossible). No external side effects occurred; only a local scratch process. Let me redo it with a closed form for F(m) and `lgamma`-based C(n), avoiding huge factorials.

## Output 177 (msg_1ff7eb39f001oGZ79NYGRrH39h)

Excellent — the computation is clean and reproduces the referee's finite-n range exactly. Two rays give t(n)/n → ~0.01771 (dyadic) and ~0.00339 (4/3-ray). Now let me seriously try to break this: check predicate monotonicity (so binary search = true min), validate C(n) against exact factorials at larger n, and solve the analytic fixed-point equations that govern the limits.

## Output 195 (msg_1ff7f4189001N0x6o2F06KMgJM)

All falsification checks pass. Let me also compute the fully self-consistent limits (tracking the dyadic mantissa of the small part `a` too) to confirm the empirical convergence to single constants.

## Output 213 (msg_1ff7f83d60012HgsIfagNhKKTT)

The self-consistent fixed points match the empirical limits to 6 decimals. Let me do two final checks: confirm F closed form against literature values, and map the full continuum of limit points across dyadic mantissas.

## Output 240 (msg_1ff80479e001wYEMbWOFF75oQ2)

## Recovery / state audit

- `billy-dev`, clean worktree at `6a96398`; no commits, no Lean, no repo, ledger or board changes by me. The only local action was a scratch computation that was OOM-killed and then rewritten; no external side effect occurred. Board #301 has no post under this front's tag, and the ledger entry `fj-threshold-sawtooth-limit-alln` is still `running` with no finding — so nothing was duplicated. All scratch work is in `/tmp/opencode/fjlim/`.

## Verdict: the convergence claim is DISPROVED (paper-level theorem)

**t(n)/n does not converge.** It has a continuum of limit points; two explicit subsequences have limits that differ by ≥ 0.0144.

| subsequence | n | t(n)/n (j=22) | rigorous limit interval | self-consistent limit |
|---|---|---|---|---|
| dyadic `n=2^j` | 4,194,304 | 0.017706 | [0.017492, 0.017811] | **0.0177057** |
| `n=round((4/3)·2^j)` | 5,592,405 | 0.003393 | [0.003367, 0.003410] | **0.0033930** |

The analytic fixed points were predicted (before comparison) from the FJ sawtooth and match the exact-integer computation to 6 decimals. Sweeping the dyadic mantissa `n/t0 ≈ t0·2^20` gives limit points ranging continuously from ≈0.00339 (near `t0=4/3`) up to ≈0.01835 (near `t0≈1.85`): the "sawtooth-smoothed 0.0174" of the 18:03Z post is *one* limit point, not the limit.

**Proof skeleton (deduction, exact integers + standard asymptotics).** With `s=k/2^{⌊log₂k⌋}`, `ceil(log₂(3k/4)) − log₂k = [s>4/3] − log₂s =: f(s)`. Riemann sums give `Δ(⌊t·2^j⌋) = 2^j(c+Φ(t)) + O(j)`, `c=1/ln2−4/3`, `Φ(t)=∫₁^t f`, so `Δ(m)/m → R(t)=(c+Φ(t))/t` (continuous; `R(1)=R(2)=c≈0.109362`, `R(4/3)≈0.027658`, `max≈0.113729`). Dividing the predicate `P(a,b)` by `n` and using Stirling gives `H(ε)−ε = ε·r(a) + (1−ε)·r(b) + o(1)`, `ε=t(n)/n`. Since `b=n−t(n) ≥ 0.98n`, the dominant term `r(b)` is the sawtooth at *n's dyadic mantissa* — it does not average out. For `n=2^j`, `b`'s mantissa → 2, so `r(b)→c`; for `n≈(4/3)2^j`, `b`'s mantissa → 4/3, so `r(b)→R(4/3)`. The entropy root is strictly increasing there, forcing distinct limits. (The small-part term `ε·r(a) ≤ 0.02·0.114` shifts ε by <0.0004, far below the 0.0144 gap.)

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
