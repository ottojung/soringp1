# antonina-wNZBHz8c8yQB2OCm0nwfXU-king

Session: ses_e0bfdebafffen1zuxrGm1f8K18
Workspace: /home/lubko/soring-fronts/parallel-module-reversal-soundness-alln
Created: 1795095139565; updated: 1795098783358

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 542 (msg_1f438e239001TX1Z41RpfBPRHa)

## Outcome

The all‑`n` soundness claim is **false**. The smallest counterexample is at **n = 9**. This is a **falsification**, not a theorem completion; no new symmetry or compression result is claimed.

## Explicit counterexample

States are successor bitmasks (`succ[i]` has bit `j` iff `i < j`).

- Module `S = A` on keys `0,1,2`:
  `A = (0,1,1)` — relations `1 < 0`, `2 < 0`, with `1 ‖ 2` (the `Λ` poset).
  Its dual is `Aᵒᵖ = (6,0,0)` — relations `0 < 1`, `0 < 2`.

- Outside component `B` on keys `0..5`:
  `B = (0,1,1,3,7,11)`, Hasse relations `5 < 3 < 1 < 0`, `4 < 1`, `4 < 2`, `2 < 0`.

Disjoint union (shift `B`’s masks by `|A| = 3`):

```
P = A ⊔ B    = (0,1,1,0,8,8,24,56,88)
Q = Aᵒᵖ ⊔ B  = (6,0,0,0,8,8,24,56,88)
```

Exact minimax values, reproduced independently here with the repository isomorphism‑class DP (`quotient_classes(9)`, 183231 classes, `S(9)=19`) and the full `verify(9)` sweep:

```
F(P) = 12
F(Q) = 11
e(P) = e(Q) = 1512
```

So reversing the module `S = A` changes `F` by 1. In `P`, every outside key lies in `B`, and every key of `B` is incomparable with every key of `A`; hence `S` is a parallel module in the question’s sense (cross moves `x∈S, y∉S` with `x ‖ y`). The quotient `P/S` is nevertheless **prime**, because `B` is not an antichain — so this is outside the already‑proved interval‑module case (Theorem 3) and outside the restricted “self‑dual complement / antichain quotient” theorem of `docs/research-parallel-duality.md`.

## Minimality and scope

- Exhaustive isomorphism‑class checks: `n ≤ 7` gives 0 violations (existing note/probe); I re‑ran `n = 8`: 6248 pairs, 0 violations.
- At `n = 9`: 1840 pairs with both components non‑self‑dual, of which **96 violate** the equality — split `(3,6): 8`, `(4,5): 40`, `(5,4): 40`, `(6,3): 8`. So the failure is structural, not an isolated numerical accident.

**Consequence.** Exact state compression cannot quotient by arbitrary parallel‑module reversals. The sound cases remain interval modules and the stricter antichain‑complement (parallel‑quotient) case proved via self‑duality of an antichain; the general “outside arbitrary but incomparable with `S`” case is unsound from `n = 9`.

## Side‑effect / recovery audit

- Git worktree is clean (`git status --porcelain` empty); no repo, Lean, test, workflow, ledger or canonical‑main changes. Scratch only under `/tmp/opencode`; all background computations completed.
- **No new #301 post was made.** An identical prior result already exists on the board (`2026-11-08T23:43:00Z`, author `SoringP1 frontier: parallel-reversal-symmetry`, same `P/Q` and `F=12/11`, same `n=9` minimality). Per the recovery instruction I did not duplicate it.
- NO theorem completion claimed; no `S(n)` / `SORT-BOUND-U` complexity claim.
