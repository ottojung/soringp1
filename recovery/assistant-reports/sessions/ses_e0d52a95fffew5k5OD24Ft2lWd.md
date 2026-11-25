# antonina-cdlQj2MJNVG37G7sR8lMTD-slightly

Session: ses_e0d52a95fffew5k5OD24Ft2lWd
Workspace: /home/lubko/soring-fronts/ecovers-reachable-summary-evaluator
Created: 1795072808732; updated: 1795076049683

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f2ad5943001uqAeFSzfoZl354)

I'll start by understanding the repository state and the required reading materials.

## Output 153 (msg_1f2ae6939001K79Y3bFgYmOeMF)

Let me look at the board's most relevant recent work on summaries and the general-poset failures, then set up my own independent experiment.

## Output 168 (msg_1f2af0a85001PrlVO0e2scJJOf)

Now I'll build my own independent experiment from scratch. Let me set up a scratch directory and write fresh code.

## Output 204 (msg_1f2b00bf2001NRoI7GKCjHqNSR)

My engine reproduces the n≤6 census exactly. Now let me optimize canonization and push to n=7.

## Output 238 (msg_1f2b4cfa1001KeW9SC8a353k5U)

I found **16 distinct `(e,covers)` keys with F-splits among reachable states at n=7** — a decisive refutation. Let me now rigorously verify a clean witness with independent recomputation and explicit reachability paths.

## Output 256 (msg_1f2b8f0ec001YyAvT9XYQ4DxrK)

The witness is verified (e=8, covers=8, F=3 vs F=4, both in R₇), but my path replay tracked canonical rather than concrete labels. Let me fix that and add disk caching of F to avoid recomputation.

## Output 274 (msg_1f2bfc50b0016BLY85zYp50WF7)

Both witnesses have explicit budget-checked paths. Let me now build a complete height-13 decision tree containing one witness as a node and verify it sorts all 5040 permutations — a fully independent end-to-end check.

## Output 315 (msg_1f2c4f1d2001d8Jd5eTiO8RvdQ)

The full tree build is slow due to brute-force canonization. Let me implement a faster canonicalizer and validate it against the brute-force one before retrying.

## Output 365 (msg_1f2cc3ca1001hd2FEQInlItqQP)

The color IDs depend on vertex iteration order — that breaks invariance. Let me fix it by assigning IDs from sorted signatures.

## Output 428 (msg_1f2cff5c800193d0c7UHWzOjka)

Found the bug: I was assigning vertex labels as positions instead of permuting the position blocks. Let me fix canon_fast properly.

## Output 446 (msg_1f2d07355001tNn3htfPeolxD8)

canon_fast is now invariant. Let me re-key the cached F values through canon_fast and rebuild the explicit tree quickly.

## Output 549 (msg_1f2d660150015keDOAyZFUwW5h)

The memoization keyed by canonical form reused subtrees with wrong labels. Let me key by the exact concrete state.

## Output 567 (msg_1f2d6ffe70017dRGquzdSYXfji)

Sorting is now correct but depth exceeds 13 — let me trace the worst permutation to find the inconsistency.

## Output 585 (msg_1f2dc7661001S4LqdU6VW1zDCo)

The forced path appears to violate the budget under my fast-canon F — let me check whether canon_fast is a valid canonical form on all posets and whether the new F computation is correct.

## Output 605 (msg_1f2dccac0001PY84Ow7J2BDpuf)

The state is not transitively closed — canon_fast is producing invalid canonical forms. Let me verify.

## Output 616 (msg_1f2dcf1e60015BfuowlikavKRm)

The core result is solid (validated brute-canon engine); the tree builder had a side issue but is redundant. Let me confirm no prior report exists on the board for this front, then prepare the finding.

## Output 675 (msg_1f2de0fd6001cyBVY1Lmh0W0y2)

I have a rigorous, independently verified counterexample. Let me draft and post the finding to board #301.

## Output 720 (msg_1f2dea7e1001EeVoFc5uJKlSJt)

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
