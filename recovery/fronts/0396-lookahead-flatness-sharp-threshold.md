# lookahead-flatness-sharp-threshold

## status

investigated

## origin

ai_proposal_unverified

## agent_id

mGt6VDsjKQC07CYxMxhhz3-prepared

## exit_state

clearexit

## question

Is the first lookahead depth at which the extension-count hierarchy L_t(A_n) exceeds the information bound C(n) exactly floor(n/2)+1 for every n with E(n)>0, and does L_t then stay at C(n) for all smaller t?

## basis

Newest antichain-lookahead-depth post proves L_t(A_n)=C(n) for 0<=t<=floor(n/2) and states convergence needs depth > n/2; the exact-reset divisibility note and the E(n) table n<=22 supply the excess side.

## falsifier

An explicit n with E(n)>0 and L_{floor(n/2)+1}(A_n)=C(n), or a proof that some n with E(n)>0 keeps L_t(A_n)=C(n) for every t below S(n).

## implication

A positive answer would make the linear-depth extension-count hierarchy complete at the first depth not covered by the flatness theorem; a counterexample would show that the soundness-completeness gap of that hierarchy is strictly larger than the proved n/2 flatness bound.

## finding_unverified

## Recovery / side-effect check

- Host: **billy-dev**. Worktree clean at `6a96398`.
- No prior post for `lookahead-flatness-sharp-threshold` existed, so I posted the finding exactly once to Antonina #301.
- No duplicate post, commit, branch, Lean file, or repository edit. Scratch scripts remain under `/tmp/opencode`.

## Mathematical finding

The front’s sharp-threshold claim is **false**, and not just at one exceptional `n`.

**Theorem (paper proof).** For every `n >= 0` and every
\[
0 \le t \le \left\lfloor \frac n2 \right\rfloor + 1,
\]
we have
\[
L_t(A_n)=C(n)=\lceil \log_2 n! \rceil .
\]

**Proof sketch.** The lower bound is the known dominance chain `L_t >= L_0`, with `L_0(A_n)=C(n)`.

Let `m=floor(n/2)`. For `t <= m`, repeatedly compare disjoint pairs of isolated keys. Each comparison has isomorphic children and halves the extension count. After `t` steps the state is
\[
P_t=A_{n-2t}\sqcup (C_2)^t,
\]
so `L_0(P_t)=C(n)-t` and hence `L_t(A_n) <= t+L_0(P_t)=C(n)`.

For `t=m+1`, use `m` such disjoint comparisons. The remaining state is
\[
P_m=A_{n-2m}\sqcup (C_2)^m,
\]
with `n-2m in {0,1}` and one lookahead level left. The key lemma is `L_1(P_m)=L_0(P_m)`: for `m>=2`, compare minimal elements of two distinct `C_2` components; swapping the two chains is an automorphism exchanging the two outcomes, so each child has exactly half the extensions. The cases `m=0,1` are direct. Therefore
\[
L_{m+1}(A_n)\le m+L_0(P_m)=m+(C(n)-m)=C(n),
\]
and equality follows from the lower bound.

## Explicit counterexample

Take `n=12`. Literature gives `S(12)=30`, while `C(12)=29`, so `E(12)=1>0`. But
\[
\left\lfloor \frac{12}{2}\right\rfloor+1=7,
\]
and the theorem gives
\[
L_7(A_{12})=29=C(12),
\]
not `> C(12)`. Thus the first exceeding depth is at least **8**, not 7.

A finite exact check of the next layer (`L_2(R_6)=23=L_0(R_6)` for `R_6=(C_2)^{⊔6}`) also gives `L_8(A_{12})=29`, so the first exceeding depth is at least **9**. I did not determine the exact first depth.

## Consequence and limits

- The proposed first-exceeding depth `floor(n/2)+1` is refuted for **every** `n` with `E(n)>0`, not merely for `n=12`.
- The flatness/completeness gap of the extension-count hierarchy is at least one full layer larger than the front claimed.
- This is **not** a new lower bound on `S(n)`, not a faster exact evaluator, and not a `SORT-BOUND-U` class result. It only shows the hierarchy cannot detect positive excess at the first depth beyond the proved `n/2` flatness bound.
- Exact first-depth behaviour remains open; no all-`n` jump formula is established.
- No repository or Lean changes were justified.

## Other metadata

```json
{
  "finished_at": 1794169999.9737241,
  "started_at": 1794169099.3769593
}
```
