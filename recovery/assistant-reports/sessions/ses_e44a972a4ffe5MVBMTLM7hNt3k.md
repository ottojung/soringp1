# antonina-k5nwVjfJrXKFT1eXmG4Tyk-glimpses

Session: ses_e44a972a4ffe5MVBMTLM7hNt3k
Workspace: /home/lubko/soring-fronts/k-regular-sorting-number
Created: 1794144374274; updated: 1794144884252

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 279 (msg_1bb5deaa1001HawFBYXquQcN8d)

## Mathematical finding

The front is **negative for every base**: `S(n)` is **not `k`-regular for any integer `k ≥ 2`**. Equivalently, every `k`-kernel of `S` spans an infinite-dimensional `Q`-vector space.

### Proof idea

Sergeev’s bound plus the information lower bound give

\[
S(n)=\log_2(n!)+o(n)=n\log_2 n-\frac{n}{\ln 2}+o(n).
\]

Assume `S` is `k`-regular. Along `n = k^m`,

\[
v_m=\frac{S(k^m)}{k^m}
\]

is a linear recurrence sequence over `Q`, because the base-`k` digits of `k^m` are `1` followed by `m` zeros, so `S(k^m)` is an entry of `A_0^m` applied to fixed vectors.

A standard LRS fact says: if an LRS satisfies `v_m = Cm + D + o(1)`, then `C` and `D` are algebraic. The rational generating function has only unit-circle poles, convergence kills every nonconstant root, and the polynomial part at `z=1` has algebraic coefficients.

But the sorting asymptotic gives

\[
v_m=m\log_2 k-\frac{1}{\ln 2}+o(1).
\]

Hence `−1/ln2` would be algebraic. This contradicts Lindemann’s theorem: `ln2` is transcendental, so `1/ln2` is too. Therefore no finite `k`-regular representation exists, uniformly in `k`.

## What this closes and what it does not

- **Closes:** the proposed finite-dimensional linear digit evaluator for `S_unary(1^n)`; the `O(n)` matrix-product route cannot exist.
- **Extends:** the board’s automatic-sequence barrier from `p`-automatic residues to all `k`-regular representations.
- **Does not prove:** any separation of `SORT-BOUND-U` from P, NP, or PSPACE.
- **Does not cover:** nonlinear digit recursions, unbounded-order recurrences, or unbounded-state digit DP.
- **Not a certificate result:** this concerns the exact sequence `S`, not certificate soundness or completeness. General-poset regularity or hardness results do not transfer.

## Why growth and finite prefixes are insufficient

I checked the obvious falsification routes. `k`-regular sequences with `n log_2 n + O(n)` growth, monotonicity, and increments `O(log n)` do exist—for example `Σ_{j≤n} floor(log_k j)`. What cannot exist is a `k`-regular sequence matching the exact second-order coefficient `−n/ln2`. Sanity checks:

- `Σ_{j≤n} floor(log_2 j) = n log_2 n − 2n + O(log n)`, constant `−2` (algebraic).
- `Σ_{j<n} s_2(j) = (1/2)n log_2 n + O(log n)`, linear constant `0` (algebraic).

This also clarifies the companion `k-regular-asymptotic-barrier` front: a `k`-regular model with `n log_2 n + O(n)` may exist, but it cannot match the proven `−n/ln2` term.

## Artifacts and effects

- Note: `docs/research-k-regular-nonregularity.md`
- Updated `docs/README.md` and `docs/research-plan.md`
- Signed commit `4d801a1` on branch `billy-dev`
- Pushed as `research/k-regular-sorting-number-20261108` (`4d801a11acde8513e909d89f50fa8681d53277ef`)
- One board #301 post at `2026-11-08T13:33:50Z`
- No Lean changes, no PR, no duplicate posts or commits

Recovery inspection found no earlier `k-regular` board post, commit, or repository change, so this was the first completion of the front. The ledger entry remains `running` for the keeper to record; I did not edit it manually.

**Honest limit:** the proof depends on Sergeev’s primary asymptotic theorem and Lindemann’s theorem; neither is kernel-checked here. The LRS and algebraic-coefficient steps are standard, but this is a paper proof, not a Lean verification.

## Output 307 (msg_1bb5e43a3001AZxE8ygRLZnPLj)

Recovery inspection complete. I made no new posts, commits, pushes, or repository changes.

**Confirmed state**

- **Working directory:** `/home/lubko/soring-fronts/k-regular-sorting-number`
- **Git:** clean worktree, `HEAD = 4d801a1` (`Prove exact sorting number is not k-regular in any base`), branch `billy-dev`, ahead of `origin/billy-dev` by one commit.
- **Remote durable artifact:** `origin/research/k-regular-sorting-number-20261108` points to `4d801a11acde8513e909d89f50fa8681d53277ef`.
- **Board #301:** exactly one matching post by `SoringP1 frontier: k-regular-sorting-number` at `2026-11-08T13:33:50Z`. No duplicate.
- **PR:** none created.
- **Lean:** no changes.
- **Durable ledger:** the `k-regular-sorting-number` entry is still `running` with no finding recorded; that transition belongs to the keeper, so I did not edit it.

**Mathematical result remains as reported**

`S(n)` is not `k`-regular for any integer base `k ≥ 2`; every `k`-kernel is infinite-dimensional. The proof uses Sergeev’s `log₂(n!)+o(n)` bound, the LRS structure of `S(k^m)`, and the transcendence of `1/ln2`. It rules out finite-dimensional linear digit representations but does not separate complexity classes or address certificate completeness.

No unfinished external action remains on my side.
