# antonina-lBDyfn5nBb1ZWzlXpKEsXK-forecast

Session: ses_e3e5756b8ffeCHGJQ8GuRwqXus
Workspace: /home/lubko/soring-fronts/merge-block-dominance-amplification
Created: 1794250418724; updated: 1794274357184

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 1018 (msg_1c1cb1655001rhBCGS3xZ4DwuY)

I have the structural reduction and the exact equality family; the exhaustive `n=10` type-slack scan is still running on `billy-dev`. I will report the final mathematical finding, including whether any dominating pair crosses the constant, when it finishes.

## Output 1271 (msg_1c315c86a001nn7UF7Wkfjm3tA)

## Finding

No strict counterexample was found; **negative `Delta` can attain `C` exactly**, but I did not prove it can never exceed `C`. The main new result is a reduction of the whole dominance question to a specific strengthened all-`n` inequality `U`.

### 1. Negative `Delta` can be tight

Let

- `Q = Merge(2,4)`, with `F=5`, `e=15`, `covers=4`, `m=M=2`, so `R(Q)=C`.
- `W = C1 ⊕ Q ⊕ C1`, with `F=5`, `e=15`, `covers=8`, `m=M=1`, so `R(W)=α/9`.

Then

\[
\Delta=(M_W-M_Q)(m_Q-m_W)=(1-2)(2-1)=-1,
\]

both ratios are at most `C`, and

\[
R(W\oplus Q)=\frac{2\alpha}{9+8-1}=\frac{\alpha}{8}=C,
\qquad \alpha=5-\log_2 15.
\]

So the dominance hypothesis is attained with equality. The open question is strictly whether it can be beaten.

### 2. Dominance reduces to a strengthened inequality

Define

\[
\psi(m,M)=
\begin{cases}
0,&(m,M)=(1,1),\\
\min(mM,m+M),&\text{otherwise},
\end{cases}
\]

and consider

\[
(U)\qquad \alpha(B)\le C\bigl(\mathrm{covers}(B)+\psi(m_B,M_B)\bigr)
\]

for every finite poset `B`, where `α(B)=F(B)-log2 e(B)`.

If `(U)` holds, then every negative-`Delta` pair satisfies `R(A⊕D)≤C`. For `Delta<0`, the denominator is

\[
T=\mathrm{covers}(A)+\mathrm{covers}(D)+M_A m_D+M_D m_A,
\]

and `(U)` reduces the claim to the purely numerical type inequality

\[
\psi(m_A,M_A)+\psi(m_D,M_D)\le M_A m_D+M_D m_A,
\]

which I checked for all types `m,M≤14` with no exception. The same inequality is exactly what makes `(U)` closed under ordinal sums.

For `m=1` or `M=1`, `(U)` is identical to the board’s original inequality `α≤C(covers+Mm)`. For `m,M≥2` it is strictly stronger because `m+M≤mM`. Therefore the dominance front is **not** implied by the already-open all-`B` inequality alone; the precise remaining gap is `(U)`.

### 3. Finite verification

Over all unlabelled blocks of size `3..9` (`202,677` blocks total), the minimum of

\[
s_A+s_D+C\Delta,\qquad s_B=C(\mathrm{covers}(B)+M_Bm_B)-\alpha(B),
\]

over negative-`Delta` type pairs is exactly `0`. It is attained by the `(1,1)/(2,2)` pair `W,Q`; every other negative-`Delta` type pair is strictly positive. The `(U)` excess is `≤0` on the same census, with equality at `Merge(2,4)` and its one-point ordinal extensions.

This subsumes the earlier pair search over total size `≤14`.

### 4. Honest limits

- I did **not** prove `(U)` for all `n`.
- I did **not** find a strict counterexample.
- An exhaustive `n=10` type scan was started but killed by the infrastructure restart at about 500k memo states; I make no `n=10` claim.
- The leaf bound `ceil(log2 e(P))` is sound but incomplete; general-poset SUPI approximations do not give exact `F(P)` and do not transfer to `S(n)`.
- No `S(n)` or `SORT-BOUND-U` complexity consequence follows.

I posted this as a concise update to board #301 under `merge-block-dominance-amplification`. The repository worktree remains clean; no Lean or repository changes were made.
