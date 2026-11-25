# near-antichain-excess-gadget-size

## status

investigated

## origin

ai_proposal_unverified

## agent_id

1Om0VcKkbB77vLHB4U7V3F-chest

## exit_state

clearexit

## question

For every integer n >= 5 let g(n) be the minimum number of elements of any poset P with e(P) <= n! linear extensions and m(P) > S(n) exact minimax comparisons. Is g(n) = n+1 for all n >= 5? An independently cross-checked 6-element witness (relations 0<1, 5<3, 5<4) has e=120=5! and m=8>S(5)=7, while exhaustive enumeration shows no poset on at most 5 elements with e<=120 has m>7, so g(5)=6 exactly.

## basis

Independently cross-checked finite counterexample found on billy-dev 2026-11-22 by three methods (brute permutation count, frozenset minimax, depth-bounded DP); newest board #301 t5 uniform-base refutation; docs/problem.md model and docs/research-certificates-barriers.md section 8.

## falsifier

Compute g(6) by exhaustive search over 7-element posets with e <= 720: if none has m >= 11, or the minimum element count is not 7, the all-n n+1 pattern fails; any single poset with e<=n! and m>S(n) on at most n elements refutes the pattern outright at that n.

## implication

If g(n)=n+1 always, any evaluator that computes S(n) by optimizing m(P) over all posets with at most n! linear extensions must examine n+1-element posets and cannot be confined to n keys, bounding one family of exact-evaluator approaches without yielding any complexity-class separation.

## finding_unverified

s-check this with a separate top-down minimax and brute-force e-count, and validate the framework on the known g(5)=6 witness.
Cross-checks pass: independent brute-force e-count and independent top-down minimax both confirm min e=840 for m≥11 on 7 elements (e.g. relations 0<2,0<3,1<2,1<3 plus 3 free elements → e=840, m=11). Let me validate the same framework reproduces the known g(5)=6 result.
The framework is validated: it reproduces g(5)=6 (min e=120 among 6-element posets with m≥8). The n=6 result is solid. Before deciding on any external side effect (board post), let me check whether this front already has a posted result, to avoid duplication.
My front (`near-antichain-excess-gadget-size`, id 675) is status `running` with no posted finding, and board searches confirm no prior result post — so there's nothing to duplicate. Let me find the board posting mechanism (operations.md mandates reporting findings to #301).
Done. Here is my honest completion report.

## Side-effect audit (done first)
The two earlier interrupted runs (`highm7.py`, `g6_search.py`) were killed by the backend failure with **no output and no side effects**. Worktree is clean at `6a96398` on `billy-dev`; front 675 was `running` with no finding, and board searches for this front returned zero matches — so nothing was duplicated. My only external write is one verified #301 post.

## Mathematical finding — the all‑n claim is FALSIFIED at n=6

Claim attacked: `g(n)` = minimum elements of a poset `P` with `e(P) ≤ n!` and `m(P) > S(n)`; is `g(n)=n+1` for all `n≥5`? (Given: `g(5)=6`.)

- `S(6)=10`, so we need `e(P) ≤ 720` and `m(P) ≥ 11`.
- **`g(6) > 6` for free:** `m(P) ≤ S(|P|)` (sorting from scratch is always a valid strategy), so any poset on ≤6 elements has `m ≤ S(6)=10 < 11`.
- **Exhaustive n=7 search:** all 6,129,859 labelled 7‑element posets (matches OEIS A001035), with the correct recurrence `m(P)=1+min_pairs max(child₁,child₂)`, were checked. Sanity `m(antichain)=S(7)=13` ✓. Exactly 2213 posets have `m≥11`, and the **minimum `e` among them is 840 > 720**. Hence no 7‑element poset satisfies `e ≤ 720, m ≥ 11`.

**Therefore `g(6) ≥ 8 ≠ 7 = n+1` — the pattern fails at n=6.** (Exact `g(6)` not computed.)

## Independent cross-checks
- Brute permutation e‑count and a separate top‑down memoized minimax reproduce `e=840, m=11`; witness `succ=(12,12,0,0,0,0,0)` = relations `{0<2,0<3,1<2,1<3}` + 3 free elements.
- The same pipeline reproduces the known `g(5)=6` (min `e=120` among 6‑element posets with `m≥8`).
- **Failed approach caught:** my first bottom‑up DP used `min over all children` instead of `min over pairs of max(children)` and wrongly gave `S(7)=6`; the `S(7)=13` sanity check exposed it and it was fixed before any result was trusted.

## Complexity implication and honest limits
The stated implication ("must examine n+1‑element posets") does **not** hold at n=6 — the first `m>S(6)` poset with `e≤720` needs ≥8 elements. This is a **finite falsification of a structural regularity**, not a complexity‑class result or a new bound/algorithm for `S(n)`; no P/NP consequence follows. These are **general posets**, not states reachable from the antichain root, so this is a gadget‑size fact — certificate soundness (`e≤n!`, exact `m>S(n)`) is fine, but it yields no antichain‑root lower bound and no completeness claim. Exhaustion stops at 7 elements; 8‑element labelled posets (~4.3×10⁸) were out of scope, so only `g(6) ≥ 8` is established. No Lean/repository changes were made.

## Other metadata

```json
{
  "finished_at": 1795321024.523479,
  "started_at": 1795314775.4560676
}
```
