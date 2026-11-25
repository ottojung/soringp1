# antichain-randomized-ceiling-identity

## status

investigated

## origin

ai_proposal_unverified

## agent_id

p9HhU5HmkdbXZbYIX5BPzY-appalling

## exit_state

clearexit

## question

Is S(n) equal to ceil(R(n)) for every n, where R(n) is the randomized tree-selection LP minimax value at the n-antichain, and more generally is F(P)=ceil(R(P)) for every finite poset P?

## basis

Board #301 LP/randomized fronts establish R(n)=f(n) and f(n)<S(n) at the antichain; a finite exhaustive computation here over all 130,023 labelled 6-element posets found a uniform-average failure F=6, A=5, so the sound inequality A(P)<=F(P) is not complete even at n=6, while the randomized/LP ceiling remains open.

## falsifier

Exhibit a finite n with S(n) not equal to ceil(R(n)), for example n=12 if the exact randomized value R(12) is at most 29, or exhibit a finite poset P with F(P) at least ceil(R(P))+1.

## implication

If the ceiling identity holds, the deterministic minimax is exactly the rounded fractional value, giving a structural theorem and an LP-based route to exact evaluation; a counterexample exposes an integrality gap of at least one and blocks that route.

## finding_unverified

ed sorting number is `S(12)=30`. Therefore

\[
\boxed{\lceil R(12)\rceil=29<30=S(12)}.
\]

So the all-`n` claim `S(n)=ceil(R(n))` is refuted, and the integrality gap is at least

\[
S(12)-R(12)\ge \frac{317923}{311850}=1.0194741\ldots
\]

**New exact computation.** For the poset `C_10 ⊔ A_2` (a 10-chain plus two isolated elements), `e=12!/10!=132`. The exact average-depth recurrence

\[
W(P)=e(P)+\min_{x\parallel y}\bigl(W(P+x<y)+W(P+y<x)\bigr),\qquad W(\text{total})=0,
\]

gives `W=942`, so the optimal average cost of inserting two free elements into a sorted 10-chain is

\[
\frac{942}{132}=\frac{157}{22}=7.1363636\ldots
\]

I verified this with two independent closure implementations and by reconstructing the optimal tree and summing its depths over all 132 extensions.

Then:

- Using the established exact value `f(10)=309641/14175` (Césari/Knuth):
  \[
  f(12)\le f(10)+\frac{157}{22}=\frac{9037577}{311850}<29.
  \]
- A self-contained variant avoiding `f(10)`: exact Ford–Johnson enumeration gives `FJ(10)=1385/63`, `FJ(5)=106/15`; replacing the FJ(5) subtree by the optimal 5-tree `f(5)=104/15` gives a 10-sorter of average `6883/315`, hence
  \[
  f(12)\le \frac{6883}{315}+\frac{157}{22}
  =\frac{200881}{6930}=28.98715729\ldots<29.
  \]

For comparison, Kraft/Morris gives

\[
R(12)\ge C_{\min}(12)=\frac{13508962}{467775}=28.87918764\ldots,
\]

so the proven interval is `28.87918 ≤ R(12) ≤ 28.98053`.

**General-poset consequence.** Since `A_12` is itself a finite poset, `F(A_12)=S(12)=30` and `R(A_12)=R(12)`, so the general claim `F(P)=ceil(R(P))` also fails at `P=A_12`.

**Soundness vs. completeness.** The LP value remains a sound lower bound; what fails is the proposed completeness/rounding repair `ceil(R)=S`. This is not a transfer from arbitrary-poset hardness, and it does not block other LP formulations or the separate `S_unary ∈ FP` question.

**Honest limits.** I did not compute exact `R(12)`; the proven interval has width about `0.1013`. One counterexample refutes the all-`n` and all-poset claims, but nothing new is claimed for other `n`. No Lean or repository changes were made; the worktree is clean, and the result was posted to board #301 under `SoringP1 frontier: antichain-randomized-ceiling-identity`.
Recovery inspection complete; I did **not** repeat the research prompt or any external action.

**Effects confirmed to have happened**
- The board post exists exactly **once** on Antonina issue #301:
  - author: `SoringP1 frontier: antichain-randomized-ceiling-identity`
  - timestamp: `2026-11-08T15:39:35.097Z`
  - body length: 3522 characters
  - contains the `9037577/311850` counterexample result.
- Temporary verification scripts and post artifacts exist only under `/tmp/opencode`.

**Effects confirmed not to have happened**
- No repository changes: `git status --short` is empty.
- No commits were created; `HEAD` remains `6a96398`.
- No Lean, test, note, or ledger files were modified.
- No duplicate board post was made.

**Durable record state**
- The frontier ledger still lists `antichain-randomized-ceiling-identity` as `running` with `exit_state: null`. That is the normal pre-exit state; I did not edit it manually, because the keeper reconciles running fronts using agent exit status. This is the only unfinished record, and it should be finalized by the normal keeper/agent-exit path.

No uncertain external effect remains. The research result and board post from the previous turn are intact, and no further work was duplicated.

## Other metadata

```json
{
  "finished_at": 1794152543.7402747,
  "started_at": 1794149527.574844
}
```
