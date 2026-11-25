# antonina-MhAvXWEbaedzI9mx6DOFqg-remorse

Session: ses_e461ce2adffex3ZpsQVwcJUZM5
Workspace: /home/lubko/soring-fronts/cover-destruction-lower-bound
Created: 1794120031713; updated: 1794120822293

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 350 (msg_1b9eef35c001DWzX1FEOMrxmWI)

**Mathematical finding.** The cover-destruction identity is true, but it does not yield the proposed lower-bound route.

### 1. The identity, and an error in the 05:56Z proof line

For incomparable `a,b`, put `Q=tc(P∪{a<b})`. The compared pair `(a,b)` is always a **new cover** of `Q`: an intermediate `z` with `a<z<b` would force `a<z` and `z<b` already in `P`, hence `a<b` in `P`, contradicting incomparability.

But old covers can be destroyed. In `P=(12,12,0,0)` the covers are `(0,2),(0,3),(1,2),(1,3)`; adding `1<0` destroys `(1,2),(1,3)`, while adding `0<1` destroys `(0,2),(0,3)`. So the board's sentence “a cover of `P` remains a cover of `Q`” is false. The count lemma `|cov(Q)| ≤ |cov(P)|+1` still holds.

Since every comparison creates exactly one new cover, a root-to-total-order path of length `h` satisfies exactly

\[
h = (n-1)+D,
\]

where `D` is the total number of old covers destroyed. Hence

\[
S(n)=n-1+D_{\min}(n),
\qquad
d(n):=S(n)-C(n)=D_{\min}(n)-\bigl(C(n)-(n-1)\bigr),
\]

with `C(n)=ceil(log₂ n!)`. Exact minimax with `D` as cost confirms this on all labelled posets for `n ≤ 5`.

The important consequence is negative: proving `S(n) > C(n)` by cover destruction is **exactly** proving that `D_min` exceeds its information-forced value. The identity is a restatement of the excess, not an independent route to it.

### 2. The natural cover-deficit potential collapses to leaf counting

Consider

\[
\Phi_\alpha(P)=\log_2 e(P)+\alpha\bigl(n-1-|\mathrm{cov}(P)|\bigr).
\]

At the antichain, any first comparison gives `Q` with `|cov(Q)|=1` and `e(Q)=n!/2` exactly. Therefore

\[
\Phi_\alpha(A_n)-\Phi_\alpha(Q)=1+\alpha.
\]

For `α>0`, both isomorphic outcomes drop the potential by more than `1`, so no adversary can maintain the soundness inequality `max Φ(child) ≥ Φ(parent)-1`. For `α≤0`, the root value is at most `log₂ n!`. Thus the only sound coefficient is `α=0`, i.e. ordinary leaf counting. This is an exact obstruction.

### 3. Infinite entropy-balanced destruction family

Let `K_{m,m}` be the height-two poset with `m` minima, `m` maxima, and all cross relations. Then

\[
|\mathrm{cov}(K_{m,m})|=m^2,\qquad e(K_{m,m})=(m!)^2.
\]

Comparing two minima destroys exactly `m` old covers and creates one new cover, while the child has `e=(m!)²/2` exactly. So destruction can occur with maximal information drop and zero information slack. Checked exactly for `m=2,3,4,5` (`n=4,6,8,10`). Any additive potential rewarding destroyed covers cannot charge them to entropy; accumulated-destruction terms are zero at the root anyway.

### 4. Small exactness obstruction

At `n=5`:

- `A=(8,0,10,0,11)`: `e=8`, `|cov|=5`, `F=4`;
- `B=(16,28,16,16,0)`: `e=8`, `|cov|=5`, `F=3`.

So `(e, cover count)` does not determine the minimax value. An exact potential built only from those two quantities cannot work.

### Honest limits

I did **not** prove an all-`n` barrier for arbitrary path-dependent cover potentials, and did **not** construct infinite full sorting strategies meeting the information bound. What is ruled out is the natural cover-deficit/additive-destruction family; a surviving exotic potential would need information not carried by cover births and destructions. This is a **soundness** obstruction for that family, not a completeness theorem for any certificate system, and it gives no `NP`/`coNP` or “`S(n)>C(n)` infinitely often” claim.

No repository or Lean changes were made; the worktree remains clean at `6a96398`. The result and an erratum correcting the illustrative cover example were posted to board #301.
