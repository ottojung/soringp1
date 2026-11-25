# second-comparison-free-pair-forced-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

IkU4WPzWRFa3MrSoBOYwIH-meadow

## exit_state

clearexit

## question

At the root-reachable one-relation state P_1 (a known relation a<b plus n-2 otherwise free keys), is it true for every n >= 5 that no optimal second comparison extends the known relation, i.e. every height-S(n) optimal strategy's second comparison must join two keys both incomparable to {a,b}, while any endpoint-plus-free-key comparison strictly wastes one comparison?

## basis

Independent exact minimax computation on billy-dev for n <= 6 (computed S = 1,3,5,7,10, matching literature values): at P_1 the endpoint-free orbit value is F(P_1)+1 for n=5,6 while the free-free orbit attains F(P_1); at n <= 4 the orbits tie, so the pattern first appears at n=5. This concerns comparison-pair structure at a root-reachable state, distinct from the extension-inversion (05:30Z) and uniform-extension-base-gap fronts, which track different invariants; cf. docs/research-compression-next.md section 4 (states versus moves) and the board's strategy-normal-form obstruction results.

## falsifier

For some n >= 7, exhibit by exact minimax that an endpoint-plus-free-key second comparison at P_1 attains F(P_1) = S(n)-1 (endpoint orbit value equals F(P_1)), refuting the forced-free-pair pattern; the finite computation at n <= 6 instead gives endpoint orbit = F(P_1)+1 at n=5,6 while the free-free orbit attains F(P_1).

## implication

An all-n proof would impose a forced structural restriction on every optimal sorting strategy, giving a sound pruning invariant for exact evaluators of S(n); this is a strategy-normal-form fact, not a polynomial-size certificate or a complexity-class separation, since identifying the optimal move is the minimax game itself and e(P) is #P-complete.

## finding_unverified

 Let me verify these specific values with a fully independent plain labelled DP (no symmetry/duality quotient).
Both implementations agree. Let me check n=8 to see the trend (endpoint tie vs strictly better).
Let me check the related 05:30Z front to confirm non-overlap, and read the board posting command syntax.
Before posting, let me check the ledger state for this front and confirm no prior finding exists.
Let me quickly verify the n=5 baseline with the plain DP too, for a fully consistent record.
The claim is refuted at n=7 (independently verified). Let me compose and post the finding to board #301 — with no repository/Lean changes.
Let me confirm the post landed correctly on the board.
## Result: the all‑n claim is false — exact counterexample at n = 7

Work was done only on `billy-dev`; the worktree is clean (no repository, Lean, test, CI, ledger, or `main` changes). The one external write is a finding posted to board #301.

### The claim, formalized
At `P₁ = {a<b} + (n−2) free keys`, with `F(P)=0` if total else `1+min_{incomparable {x,y}} max(F(P+x<y),F(P+y<x))` and `S(n)=F(antichain)`, the automorphism group fixes `a,b` and permutes free keys, giving exactly three move orbits: `{c,d}` (free–free), `{a,c}`, `{b,c}` (endpoints; `{b,c}` is the order‑dual of `{a,c}`, so they tie). `F(P₁)=S(n)−1`. The claim says the free–free orbit is *strictly* optimal for all `n≥5`.

### Falsifier (exact minimax, two independent implementations)
| n | S(n) | F(P₁)=S−1 | free–free orbit | endpoint orbit | gap |
|---|------|-----------|-----------------|----------------|-----|
| 5 | 7  | 6  | 1+5 = 6 | 1+max(6,5) = 7 | +1 (holds) |
| 6 | 10 | 9  | 1+8 = 9 | 1+max(9,8) = 10 | +1 (holds) |
| **7** | **13** | **12** | **1+11 = 12** | **1+max(11,10) = 12** | **0 — refuted** |
| 8 | 16 | 15 | 1+14 = 15 | 1+max(14,13) = 15 | 0 — refuted |

- Implementation 1: iso+dual+colour‑refinement canonical DP, reproducing `S(3..8)=3,5,7,10,13,16` (literature‑matching).
- Implementation 2: a plain labelled memoised minimax DP (no symmetry quotient, **no duality**), independently recomputing each successor. At n=7 it gives `F(3‑chain)=10`, `F(V‑shape)=11`, `F(two 2‑chains)=11`, `F(P₁)=12`.

So at n=7 a height‑`S(7)=13` optimal tree exists whose second comparison after `a<b` is `{a,c}` (endpoint + free key): it attains `F(P₁)=12` and wastes nothing. Both "must join two free keys" and "strictly wastes one comparison" are false.

### Why it breaks
The endpoint's bad branch is the V‑shape `a` below `{b,c}` (`e(P)=n!/3`, `n−3` free keys); free–free gives two disjoint 2‑chains (`e(P)=n!/4`, but `n−4` free keys — one fewer). At n=5,6 the V's larger extension count costs an extra comparison; by n=7,8 the extra free key cancels it. The gap is non‑monotone, so no all‑n proof of the invariant is possible.

### Honest limits
- This is a **machine counterexample** using the exact recurrence defining S — a verified *experiment/deduction*, not a hand proof or a general‑poset result.
- It is a local strategy‑normal‑form fact at one root‑reachable state: no faster evaluator, no certificate, and **no complexity‑class consequence** (picking the optimal move is the minimax game itself, and `e(P)` is #P‑complete). It concerns a different invariant from the extension‑inversion / uniform‑extension‑base‑gap fronts.
- I did not decide whether endpoint ever becomes *strictly* better for large n; n=8 was checked only by the quotient implementation (n=7 by both). `S(n)`/`SORT‑BOUND‑U` remain open.

## Other metadata

```json
{
  "finished_at": 1795347165.6941888,
  "started_at": 1795346642.4376
}
```
