# antonina-09egTtHT6suGqwu0k3l89c-land

Session: ses_e49a3ec1cffedbb7kiCPccK86C
Workspace: /home/lubko/soring-fronts/exec-t5-threshold-20261107
Created: 1794060850242; updated: 1794063695677

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 395 (msg_1b684235a001ZvP8uZdtuAsN2U)

## Result

The exact value is

\[
\boxed{T(5)=20.}
\]

The bound `T(5) <= 27` from `Merge(2,6)` is valid but far from sharp. The actual smallest counterexample has only 7 elements: a fence poset with `e=21` and `m=6`. Thus the `n<=6` table value `T(5)=29` is an artefact of the size cutoff, and the first failing level in general is `e=21`, not `28` or `30`.

---

## 1. Sharp counterexample: `n=7`, `e=21`, `m=6`

Let `W` be the poset on `{0,...,6}` with predecessor masks

\[
\operatorname{pred}(0)=\varnothing,\quad
\operatorname{pred}(1)=\varnothing,\quad
\operatorname{pred}(2)=\{0\},\quad
\operatorname{pred}(3)=\{0,1\},
\]
\[
\operatorname{pred}(4)=\{0,1,2\},\quad
\operatorname{pred}(5)=\{0,1,2,3\},\quad
\operatorname{pred}(6)=\{0,1,2,3,4\}.
\]

Equivalently, the only incomparable pairs are the consecutive pairs
`(0,1),(1,2),...,(5,6)`; its incomparability graph is the path `P_7`. This is a fence/zigzag poset.

Exact computation on its full extension set gives

\[
e(W)=21,\qquad m(W)=6.
\]

The value `e=21` is the Fibonacci number `F_8`, and `W` is the fence family member that generalises the familiar `e=8` and `e=13` witnesses.

Therefore `W` is not sortable in 5 comparisons, so

\[
T(5)\le 20.
\]

Other counterexamples worth recording, but not sharp:

- `Merge(2,6)`: `n=8`, `e=binom(8,2)=28`, exact `m=6`. This only gives `T(5)<=27`.
- Ordinal sum of the `e=8,m=4` witness and an `e=3,m=2` poset: `n=8`, `e=24`, `m=6`. This gives `T(5)<=23`.

The `Merge(2,6)` value is not obtained from the balanced tape-merge theorem: Stockmeyer–Yao’s exact range is `m <= n <= floor(3m/2)+1`, and `(2,6)` lies outside it. The value `M(2,6)=6` here is exact minimax, not a formula from that range. The same caution applies to Murphy–Paull, Christen, and Li–Sun–Zhang: their exact identifications are range-restricted; the safe universal special case remains `M(m,m)=2m-1`.

---

## 2. Lower bound: every poset with `e<=20` has `m<=5`

We use two established inputs.

1. **`T(4)=12`** from the certified package at commit `41f1b50`, `docs/research-t4-threshold.md`: every finite poset with `e(P)<=12` has `m(P)<=4`.
2. **Kahn–Saks (1984)**: every non-total finite poset with `e` extensions has an incomparable pair whose two orientation classes both have between `3e/11` and `8e/11` extensions.

Also use the standard ordinal-sum facts

\[
e(P_1\oplus\cdots\oplus P_t)=\prod_i e(P_i),\qquad
m(P_1\oplus\cdots\oplus P_t)=\sum_i m(P_i).
\]

If some poset `P` with `e(P)<=20` had `m(P)>=6`, then in its ordinal-sum decomposition some indecomposable factor `Q` would satisfy `m(Q)>=6` and `e(Q)<=20`. So it suffices to rule out indecomposable `Q` with `e(Q)<=20`.

For indecomposable `Q`, its incomparability graph is connected. Let `q` be the number of incomparable pairs and `n` the number of elements. Then

\[
n-1 \le q \le e(Q)-1,
\]

where the second inequality is the spanning-tree/adjacent-swap argument used in the T(4) package. Hence

\[
n\le e(Q)\le 20.
\]

Now proceed by extension count.

### Case `e<=12`

Immediate from `T(4)=12`: `m<=4<=5`.

### Case `13<=e<=17`

Kahn–Saks gives a comparison whose larger child has at most

\[
\left\lfloor \frac{8e}{11}\right\rfloor
\]

extensions. For `e=13,...,17` these bounds are respectively

\[
9,\ 10,\ 10,\ 11,\ 12.
\]

So both children have at most `12` extensions. By `T(4)=12`, each child has `m<=4`. Therefore

\[
m(Q)\le 1+4=5.
\]

This part is a paper proof; no enumeration is used.

### Case `18<=e<=20`

Here `n<=e<=20`. The remaining finite class is every connected poset with `n<=e` and `e in {18,19,20}`. A natural-extension enumeration (each new label is maximal, with predecessor set an ideal) covers all such posets, with pruning at `e>20` safe because `e` is nondecreasing when a maximal element is added.

For every connected core found, the probe checks all incomparable pairs and verifies that at least one comparison has both child extension counts `<=12`. The counts of natural-extension representations checked are:

\[
\begin{array}{c|c|c}
e & \text{connected cores } n\le e & \text{without a }(\le 12,\le 12)\text{ split}\\
\hline
18 & 324 & 0\\
19 & 304 & 0\\
20 & 305 & 0
\end{array}
\]

Thus in every case, by `T(4)=12`, both children have `m<=4`, so again

\[
m(Q)\le 1+4=5.
\]

The same script also directly recomputes exact minimax for every connected core with `e<=20`, and finds maximum exact `m` equal to `5` for every `e=13,...,20` — an independent corroboration.

Combining the cases: every indecomposable poset with `e<=20` has `m<=5`. By ordinal decomposition, every finite poset with `e<=20` has `m<=5`. Hence

\[
T(5)\ge 20.
\]

Together with the fence witness `e=21,m=6`,

\[
\boxed{T(5)=20.}
\]

The finite enumeration covers exactly the residual range `18<=e<=20`, `n<=e<=20`; the rest of the lower proof is paper deduction from Kahn–Saks and `T(4)=12`.

---

## 3. Reproduction

The self-contained probe is kept untracked in the worktree:

```sh
go run ./t5_threshold_probe.go
```

Output:

```text
Witness W pred=[0 0 1 3 7 15 31]: e=21 m=6
Merge(2,6): e=28 m=6
e=18: connected cores n<=e checked=324, lacking a <=12+<=12 split=0
e=19: connected cores n<=e checked=304, lacking a <=12+<=12 split=0
e=20: connected cores n<=e checked=305, lacking a <=12+<=12 split=0
max exact m over connected cores by e (13..20): 13:5 14:5 15:5 16:5 17:5 18:5 19:5 20:5
```

No tracked files were modified; the only worktree change is the untracked probe `t5_threshold_probe.go`.

---

## 4. What this does and does not buy

### For exact backward-search base cases

The certified base cases become:

\[
\begin{array}{c|c}
r & \text{all }P\text{ with }e(P)\le \cdot\text{ are }r\text{-sortable}\\
\hline
1 & 2\\
2 & 4\\
3 & 7 \quad\text{(Hanamura–Iwata 2011)}\\
4 & 12\\
5 & \mathbf{20}
\end{array}
\]

So in a Stober–Weiss/Peczarski-style backward layer deciding `m(P)<=5`, any state with `e(P)<=20` can be accepted immediately without expansion. Previously the certified constant-radius base at budget 5 was only `e<=12`.

This is a genuine enlargement of the base, but it is still a fixed constant threshold. It may reduce exact search work at small remaining budgets by a modest constant factor. It does **not** give a new asymptotic algorithm or complexity bound for `S(n)` or `SORT-BOUND-U`, does not settle any `S(n)` value, and does not lead to a complexity-class separation. It is a local lemma about the minimax function, useful as a pruning/base-case rule.

### Correcting the finite table

The `n<=6` value `T(5)=29` is not the unbounded threshold. The smallest counterexample is already at `n=7`; `Merge(2,6)` at `n=8` also breaks `29`, but even `28` is not minimal. The exact unbounded value is `20`.

The pattern suggested by the sharp witnesses is

\[
T(r)=F_{r+3}-1
\]

for the known range `r=1,...,5`:

\[
1,2,4,7,12,20.
\]

The `r=5` case is proved here; the general Fibonacci pattern remains a conjecture and is not needed for the result.

---

## Primary sources used

- J. Kahn, M. Saks, *Balancing poset extensions*, Order **1**(2) (1984), 113–126, DOI `10.1007/BF00565647`.
- S. Hanamura, S. Iwata, *Posets with seven linear extensions sortable by three comparisons*, Information Processing Letters **111**(8) (2011), 365–369, DOI `10.1016/j.ipl.2011.01.004`.
- P. K. Stockmeyer, F. F. Yao, *On the Optimality of Linear Merge*, SIAM J. Comput. **9**(1) (1980), 85–90, DOI `10.1137/0209006`.
- The T(4) package in this repository: commit `41f1b50`, `docs/research-t4-threshold.md`, `scripts/t4_threshold/`, `data/t4-threshold-candidates.json`.
- For the merge-family context: Murphy–Paull (1979), Christen (1978), and Li–Sun–Zhang (ISAAC 2016) give range-restricted exact merge results; none supplies a universal formula covering `Merge(2,6)`.

## Output 421 (msg_1b6876634001zbBc8Je155j2mu)

The prior turn caused **no external side effects**: there is no commit or board post, and Git history is unchanged. The only durable change is the untracked `t5_threshold_probe.go` in this isolated worktree. It reproduces the witness and finite enumeration output.

One important issue surfaced while checking that artifact: the probe’s `extensions` representation has capacity for only 30 extensions, but its search processes states with up to 20. It also records the empty poset’s base extension incorrectly for the `n=0` DFS. Consequently, the reported enumeration counts and `maxm` values are **not reliable evidence** for the claimed lower bound. The previous conclusion `T(5)=20` is therefore unverified; its proof’s decisive finite step needs a corrected, rerun certificate before it can be reported as established.

No action has been taken to post, commit, or remove the probe.
