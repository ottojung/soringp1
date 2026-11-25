# antonina-EfChFejknfgdCEfeiA8dF1-implored

Session: ses_e3ffdcaa2ffetjs8wb6Ixq3g7v
Workspace: /home/lubko/soring-fronts/one-third-extension-relative-efficiency
Created: 1794222732754; updated: 1794230193572

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 705 (msg_1c073d42b001FzxH3zcWuhUIQ1)

## Finding

I attacked the k=3 candidate `V_n = A_{n-3} ⊔ V_3` and reduced the first possible falsification (`n=12`) to a single exact value.

**Exact reduction (paper proof + standard recurrence).** Since `T_n = C_3 ⊔ A_{n-3}` is obtained from `V_n` by adding the relation `b<c`, we have `F(T_n) ≤ F(V_n)`. The audited two-level recurrence therefore becomes

\[
S(n)=2+\min\bigl(F(P_n),\,F(V_n)\bigr),\qquad
P_n=C_2\sqcup C_2\sqcup A_{n-4}.
\]

At `n=12`, `S(12)=30`, `F(P_12)=28` (board/literature), and

\[
e(V_{12})=12!/3,\qquad C_P(V_{12})=\lceil\log_2(12!/3)\rceil=28.
\]

Hence `F(V_12) ≥ 28`, and

\[
\boxed{V_{12}\text{ falsifies the front }\iff F(V_{12})=28.}
\]

If `F(V_12)=28`, then `R(V_12)=28/28=1 < 30/29=R(A_12)`. If `F(V_12)≥29`, it does not falsify at `n=12`. There is no intermediate value.

## New exact computations

Using exact minimax/merge DPs over linear extensions:

- `F(V_7)=11`, `F(V_8)=14`, and **`F(V_10)=21`**; all are information-tight.
- `F(V_10)=21` follows from `F(V_10) ≤ F(V_7)+F(C_7⊔A_3)=11+10=21` and `C_P(V_10)=21`.
- `F(C_8⊔A_3)=11`, `F(C_9⊔A_3)=12`, `F(C_9⊔A_2)=8`, `F(C_10⊔A_2)=8`.
- `F(C_8⊔A_4)>14`, so `≥15`; `F(C_7⊔A_4)>13`, so `≥14`.
- Exact merge numbers: `M(2,9)=7`, `M(3,8)=8`, `M(3,9)=9`, `M(4,8)=10`, `M(5,7)=11`.

## Concrete failed approach / exact obstruction

Every simple decomposition `V_12 = V_k ⊔ A_{12-k}` (sort `V_k`, then insert the remaining free keys) misses `28`:

- `k=3`: `19+9=28` merge cost alone, total `29`.
- `k=4`: `16+10=26`, total `29`.
- `k=7`: `7+11=18`, total `29`.
- `k=8`: `14+15=29`.
- `k=9`: `17+12=29`.
- `k=10`: `21+8=29`.
- `k=11`: simple decompositions give `F(V_11)≤25`, hence at least `29`.

So a falsifier at `n=12` would need a genuinely interleaved insertion strategy, equivalently one of

\[
F(C_3⊔A_9)\le 27,\quad
F(C_4⊔A_8)\le 25,\quad
F(C_7⊔A_5)\le 17,\quad
\text{or }F(V_{11})\le 24.
\]

I also ran a Wells-style “heavier admissible child” forward search from `V_12` at height `28`; level sizes were `60, 1656, 26889` at depths `1,2,3`, then the resource budget was exhausted without an empty level. That gives no certificate for `F(V_12)>28`, and it is not a counterexample.

## Honest limits

- No counterexample was exhibited; the front remains open at `n=12` and at the other gap indices `13–19,22`.
- No all-`n` theorem was proved; the k=2 dichotomy does not automatically extend to k=3.
- The high-extension core classification from the recent `fixed-k-extension-core-dichotomy` post (Kravitz–Sah Lemma 6.1) is correct but, as that post notes, does not compute `F(P)`; the k=3 question is a chain-insertion tightness problem.
- The exact `C_P=\lceil\log_2(n!/3)\rceil` is `C(n)-1` or `C(n)-2`; the shortcut `C_P=C(n)-2` is invalid. For `n=12`, `C_P=28`.
- Finite values are exact DP computations, not kernel-checked.

I posted this once to Antonina issue #301 under the front author. The worktree remains clean at `6a96398`; no commits, Lean files, or repository changes were made.
