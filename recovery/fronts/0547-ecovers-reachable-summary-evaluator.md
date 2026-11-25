# ecovers-reachable-summary-evaluator

## status

investigated

## origin

ai_proposal_unverified

## agent_id

cdlQj2MJNVG37G7sR8lMTD-slightly

## exit_state

clearexit

## question

All-n question: for every poset state P reachable on some height-S(n) optimal comparison strategy from the n-element antichain, is the exact continuation cost F(P) always a function of the two cheap statistics (e(P), covers(P)) -- the number of linear extensions and the number of cover relations -- such that a uniform exact evaluator for unary S(n) could memoize F by that O(n log n)-bit key instead of the full Theta(n log^2 n)-bit isomorphism type?

## basis

Newest main note notes/research-realizability-window.md states Conjecture K (F as a function of (e,covers) on reachable classes) and leaves it OPEN, with an n<=6 census showing no split; a fresh independent experiment here (own closure/extension/minimax code) finds the pair already FAILS on general posets at n=5 (e=8, covers=5, F in {3,4}), so the reachability restriction is essential. Related fronts cover e-only keys and general coarse summaries, not this specific pair.

## falsifier

Exhibit an n and two states P,Q reachable on height-S(n) optimal plays with e(P)=e(Q) and covers(P)=covers(Q) but F(P) not equal to F(Q); or show covers(P) is unbounded on reachable states so no fixed-size (e,covers) key can exist. Either witness would refute the all-n claim.

## implication

If the pair is determining and efficiently computable, an (e,covers)-keyed memoized exact evaluator would use O(n log n)-bit state keys and could evade the isomorphism-identity space lower bound, giving a smaller-space uniform evaluator; if refuted, no such two-statistic summary can be complete for exact evaluation.

## finding_unverified

ect but depth exceeds 13 — let me trace the worst permutation to find the inconsistency.
The forced path appears to violate the budget under my fast-canon F — let me check whether canon_fast is a valid canonical form on all posets and whether the new F computation is correct.
The state is not transitively closed — canon_fast is producing invalid canonical forms. Let me verify.
The core result is solid (validated brute-canon engine); the tree builder had a side issue but is redundant. Let me confirm no prior report exists on the board for this front, then prepare the finding.
I have a rigorous, independently verified counterexample. Let me draft and post the finding to board #301.
## Finding: Conjecture K is FALSE (refuted at n=7)

I attacked the all‑n claim that for every poset state `P` on some height‑`S(n)` optimal play from the antichain (`P ∈ R_n`), the exact continuation cost `F(P)` is determined by `(e(P), covers(P))`.

**Explicit falsifying witness** (canonical successor‑bitmask form, 7 labelled keys):

| state | e | covers | F | in R₇? |
|---|---|---|---|---|
| `P = (0,0,3,3,7,23,63)` | 8 | 8 | **3** | yes — depths 8, 9, 10 |
| `Q = (0,1,3,3,7,15,31)` | 8 | 8 | **4** | yes — depths 8, 9 |

Both have the same two‑statistic key `(8,8)` but different exact costs (`ceil(log₂ 8)=3`, so P is information‑bound tight, Q is strictly non‑tight). My independent n=7 census found **16 distinct `(e,covers)` keys with F‑splits** on reachable states.

### Verification (all from scratch, no repository code)
- Wrote an independent engine (own transitive closure, subset‑DP extension count, cover count, memoized minimax, brute‑force canon). It reproduced the note's n≤6 census **exactly** (`S(n)=0,1,3,5,7,10`; `|Rₙ|=19,136`; keys `11,52`; zero splits) — so the engine is validated.
- `e=8` for both states confirmed two ways: subset DP **and** brute enumeration of all 7! permutations. Covers counted by the literal “no element strictly between” definition (8 each, explicit lists). F recomputed with a fresh minimax solver (3 and 4).
- Reachability is genuine: the joint‑child DP places both at depth 8, and I reconstructed and replayed **explicit budget‑checked comparison paths** from the antichain (8 comparisons each), verifying `max(F(child₀),F(child₁)) ≤ 13−(depth+1)` at every step and `F ≤ 13−8=5` at the endpoint. Hence each lies on a height‑`S(7)=13` strategy.

### The distinctions the task asked for
- **General‑poset vs reachable:** the previously known n=5 `e=8` split has its F=4 member *outside* `R₅`, so it never refuted Conjecture K. My witness is *inside* `R₇` — the reachability restriction does **not** rescue the claim.
- **Soundness vs completeness:** this refutes **soundness** of the `(e,covers)` memo key on reachable states. Even soundness wouldn't give the claimed smaller‑space evaluator (e is #P‑hard in general; on `Rₙ` its cost is open; transitions aren't a function of the key). The proximate space‑barrier‑evasion route is closed as a no‑go for this key.

### Honest limits
Finite n=7 counterexample only — no all‑n family, no improved bound or algorithm for `S(n)`, no membership result for `SORT‑BOUND‑U`, no Lean. An extra explicit decision‑tree replay was attempted but abandoned after a bug in a secondary canonicalizer experiment; it is unnecessary — the reachability argument is constructive and the brute‑force e/F values stand alone.

Reported to Antonina issue #301. **Worktree left clean** (no Lean, note, test, ledger, or repo changes).

## Other metadata

```json
{
  "finished_at": 1795076072.957664,
  "started_at": 1795072808.1704886
}
```
