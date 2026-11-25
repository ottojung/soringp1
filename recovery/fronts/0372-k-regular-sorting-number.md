# k-regular-sorting-number

## status

investigated

## origin

ai_proposal_unverified

## agent_id

k5nwVjfJrXKFT1eXmG4Tyk-glimpses

## exit_state

clearexit

## question

Is the exact sorting number sequence S(n) k-regular for some integer base k >= 2, i.e. does its k-kernel span a finite-dimensional Q-vector space, or is the k-kernel infinite-dimensional for every base k?

## basis

Board #301 s-residue-automaticity reduces S mod p automaticity to the increments and builds an automatic model; Allouche-Shallit k-regular sequences strictly generalize p-automatic sequences, and no ledger front tests finite-dimensional linear digit representations of S.

## falsifier

Exhibit an explicit finite k-kernel or linear representation that reproduces S(n) for all n, or prove infinite rank for an explicit base k from a structural argument plus a certified finite prefix.

## implication

A finite k-regular representation would evaluate S(n) on unary input in O(n) time by O(log n) fixed-size matrix products, placing S_unary in FP; failure would extend the board's automatic-sequence barrier to all finite-dimensional digit-DP evaluators.

## finding_unverified

 in `k`.

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

## Other metadata

```json
{
  "finished_at": 1794144891.302888,
  "started_at": 1794144373.4605136
}
```
