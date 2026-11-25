# globally-feasible-locally-nonoptimal-barrier

## status

investigated

## origin

ai_proposal_unverified

## agent_id

r6gut8jGvRzUU5STDbq7ag-across

## exit_state

clearexit

## question

Do the globally height-S(n) feasible but not locally-minimax-reachable states reported on board #301 form an infinite family for all large n, and do they constitute an unconditional incompleteness barrier for any sound certificate grammar that only keeps locally minimax moves at every reached state?

## basis

Board #301 (2026-11-19 16:51Z and 17:00Z) reports L_loc(6)=65551 versus L_tree(6)=66991 and an explicit locally nonoptimal witness; docs/research-strategy-certificates.md defines DAG(all) and the soundness-versus-completeness gap.

## falsifier

Show L_tree(n)=L_loc(n) for all sufficiently large n, or give a polynomial-size sound and complete certificate system whose accepted strategies avoid every locally nonoptimal move.

## implication

A positive answer separates local-DAG certificates from globally height-optimal trees and shows the all-optimal-DAG route is structurally incomplete; a negative answer collapses the two optimal-play notions at all n.

## finding_unverified

 front asks two questions. I **refuted the second one** with a theorem, and **did not prove the first** (verified only at finite n). The conjunction as stated is therefore false.

The precise objects (from the 16:51Z/17:00Z #301 correction and `research-strategy-certificates.md`):
- `L_loc(n)` = states reachable by an all-minimax path: every move satisfies `F(P)=1+max(F(C⁰),F(C¹))`.
- `L_tree(n)` = states on some height‑`S(n)` tree: every prefix step satisfies `max(F(C⁰),F(C¹)) ≤ S(n)−i−1` (global sibling feasibility). `L_loc ⊆ L_tree` always; my code confirmed this at n=6,7.

### Result 1 — the "unconditional incompleteness barrier" is FALSE  `[deduction]`

**Theorem.** For every n there is a correct sorting tree of height exactly `S(n)` in which **every comparison at every reached state is locally minimax‑optimal**.

*Proof.* With `F(P)=1+min_{incomparable {x,y}} max(F(P+x<y),F(P+y<x))`, recursively pick a minimizing pair at each state. Every child has `F ≤ F(P)−1` and at least one has `F=F(P)−1`, so by induction the subtree height is exactly `F(P)` and every chosen move is locally minimax. The root tree has height `F(∅)=S(n)` and sorts correctly (induction on consistent permutations). ∎

**Consequence.** Any sound verifier that accepts all‑minimax strategies is **complete** for `SORT-BOUND-U` (it accepts this tree whenever `S(n) ≤ k`). Hence `L_tree(n)\L_loc(n)` is an **expressive/representational** gap — DAG(all) is not the union of all optimal trees — **not a certificate‑system completeness failure**. The front's stated complexity implication overreaches: a positive answer to part (i) would *not* establish certificate incompleteness.

### Result 2 — finite verification, infinitude left open  `[experiment]`

Independent scratch bitmask‑minimax code (no repo code imported), verified exactly against the board:

| n | S(n) | \|L_loc\| | \|L_tree\| | gap |
|---|------|-----------|------------|-----|
| 5 | 7 | 1,551 | 1,551 | 0 |
| 6 | 10 | 65,551 | 66,991 | 1,440 |
| 7 | 13 | 2,769,663 | 3,044,007 | 274,344 |

The n=6 witness reproduces: `P=(14,0,8,0,12,28)`, `F(P)=4`; comparing `(1,5)` has child F‑values `4` and `0` (`1+4=5≠4`, not minimax) but `max=4 ≤ S(6)−5−1=4` (globally feasible). Mechanism: an easy outcome drops F by 2 at depth 4, creating slack; at slack states a non‑progress comparison is globally feasible but not minimax. **Infinitude for all large n is `[open]`**: no uniform construction is known, n=5 is a zero outlier, and no general‑poset hardness transfers to the fixed family `S(n)`.

### Soundness / completeness / size distinction

My theorem gives **soundness + completeness** but the canonical certificate is the tree of size `2n!−1` — exponential. It therefore does **not** meet the falsifier's polynomial‑size clause and does **not** put `SORT-BOUND-U` in NP. I make no such claim.

### What I did *not* do
No Lean, repository, test, workflow, ledger, or branch change; worktree `billy-dev` clean at `6a96398` throughout. Scratch code only under `/tmp/opencode`. Two concise findings/updates posted to #301. Primary literature checked (`problem.md`, `literature.md`, strategy note; Mahaney barrier acknowledged) — the sparse/tally barriers are unrelated to this set‑level gap.

**Bottom line:** a clean refutation of the "incompleteness barrier" conjunct (with proof), strong finite evidence that the strict set inclusion persists (n=6,7), and an explicitly open all‑n infinitude question — no theorem completion for `S(n)` is claimed.

## Other metadata

```json
{
  "finished_at": 1795109640.1390948,
  "started_at": 1795108715.4396005
}
```
