# antonina-4hN9U1hI3GCQhkr53fID4i-campfires

Session: ses_e3d1846fbffe84C0pMnP1jXCuj
Workspace: /home/lubko/soring-fronts/disjoint-union-defect-min-size
Created: 1794271328613; updated: 1794274655612

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 625 (msg_1c31a5ae9001NNBUmL5r1wZVGa)

## Outcome

I did not find a counterexample, and I did not prove the all-`n` strengthening. The precise finding is a reduction of a would-be counterexample to an **excess-density threshold**, plus a concrete obstruction showing why the existing `+2` proof does not extend.

### Mathematical finding

For a poset \(P\), write
\[
r(P)=F(P)-\log_2 e(P)
\]
for its information excess. Since \(e(A\sqcup B)=\binom{a+b}{a}e(A)e(B)\),
\[
F(A\sqcup B)-F(A)-F(B)
\;\ge\; \log_2\binom{a+b}{a}-r(A)-r(B).
\]
So a counterexample to
\[
F(A\sqcup B)\ge F(A)+F(B)+\min(|A|,|B|)+1
\]
would force
\[
r(A)+r(B)\ge \log_2\binom{a+b}{a}-\min(a,b).
\]

Using the exact recorded excess maxima \(r(1..9)=0,0,0.415,0.678,1.0,1.300,1.608,1.913,2.219\), this excludes every split with \(|A|+|B|\le 11\). I also independently rechecked all splits with total size \(\le7\) exactly; the minimum defect is never below \(\min+1\). The only tight cases found are \((2,2),(2,3),(3,3)\).

### Exact obstruction to the `+2` argument

The extreme-extension adversary used for the `+2` theorem forces only **two** cross comparisons. Counting maximal/minimal cross-pairs cannot force \(\min+1\): for chains both extrema are singletons.

A naive additive merge bound also fails. For \(A=A_2\), \(B=A_3\),
\[
F(A)=1,\quad F(B)=3,\quad M(2,3)=4,
\]
but
\[
A\sqcup B=A_5,\qquad F(A\sqcup B)=7<1+3+4.
\]
Cross comparisons can replace internal comparisons via transitivity, so the first-cross-comparison induction has a genuine gap.

### Remaining obstruction

- **Balanced case** \(a=b=m\): any universal bound \(r(P)\le c|P|\) with \(c<1/2\) would prove the claim; all known constructions are far below \(1/2\), but no such all-`n` bound is proved.
- **Asymmetric case** \(a\) fixed, \(b\to\infty\): \(\log_2\binom{a+b}{a}\sim a\log_2 b\), while \(r(B)\) can grow linearly (ordinal sums of \(A_3\) blocks give \(r\approx0.138n\)). The excess threshold eventually becomes vacuous, so this regime needs a separate insertion/merge argument.

### State

- No repository, Lean, test, or branch changes.
- Worktree clean at `6a96398`.
- The only external effect is the single board post to Antonina #301 at `2026-11-10T01:37:16Z`, authored as `SoringP1 frontier: disjoint-union-defect-min-size`.
- No prior post for this front existed, so nothing was duplicated after the backend restart.
