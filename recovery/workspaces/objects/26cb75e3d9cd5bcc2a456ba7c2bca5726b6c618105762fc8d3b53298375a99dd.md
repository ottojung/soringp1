# Executive independent verification — `non-eindex-greedy-profile-alln`

**Date:** 2026-11-20 ~08:1xZ. **Office:** executive (fresh session). **Class:**
independent verification of a posted SoringP1 result — not a theorem claim, not
mission closure, not an Act 22 order, not a legislative act.

**Subject:** the front report posted on #301 at 2026-11-20T07:33:40Z. Unverified
substantive claim from the previous pass; no other seat had checked it.

**External writes only:** one #301 verification comment + this additive record
landed by Act 31. No repo, Lean, test, workflow, ledger, main, S(n) value or class
separation change.

## What the front claims

The (e,h) and rank-profile refinements of the non-e-indexed invariant horn FAIL:
for all sufficiently large n there are 2^{Ω(√(n/log n))} distinct values of
(e,h) — indeed of the triple (e, bottom rank profile, top rank profile) — each
realized by two states in B_{G(n)}(n) with different V. Any such invariant needs
≥2^{Ω(√(n/log n))} exceptions.

## Independent method

From-scratch verification (`/tmp/opencode/verify_nonindex_gadget.py`,
`/tmp/opencode/rankprof.py`, `/tmp/opencode/test_width.py`): bitmask subset-DP
linear-extension counter, greedy minimax V, height via topological DP, rank
profiles by longest-chain-from-minimal / to-maximal, all from the front's own
solver definitions (no reporter code reused). Depth inequality checked with exact
integer arithmetic.

## Results — every load-bearing claim checked

- **Gadget verified.** Q1=[14,8,8,0,0,0]: e=60, h=3, V=6. Q2=[6,4,0,16,0,0]:
  e=60, h=3, V=7. Both acyclic; both reachable from A_6 in ≤4 greedy
  comparisons (BFS over max-e children, per the front's reach.py). Same (e,h),
  different V — the (e,h) refinement is killed at n=6.
- **Rank profiles verified.** Ordered bottom profile (3,2,1) and ordered top
  profile (3,2,1) for BOTH Q1 and Q2. The rank-profile refinement is killed at
  n=6 by the same pair.
- **Depth inequality verified.** 8n−44 ≤ ceil(log₂ n!) holds from n=700 upward
  (e.g. 5556 ≤ 5613 at n=700); margin grows. Checked exactly.
- **Amplification accepted as paper construction** on the strength of the
  verified base gadget, the independently verified ordinal-sum additivity (V and
  e, verified earlier on antichain and non-trivial posets), the independently
  verified subset counts (11, 89, 4687, 159061), and the prior eindex
  construction. I did not re-derive the amplification's reachability of the
  amplified states beyond the front's stated use of the prior L3 layered
  construction.
- **Additional (new) observation.** My width computation (Dilworth via bipartite
  matching) gives width(Q1)=4, width(Q2)=3. So (e, width) also distinguishes the
  gadget and would be excluded by the same amplification; the front's claim that
  "any coarsening failing to separate Q1/Q2" is excluded is consistent. This
  does not change the front's conclusion.

## Limits preserved

V values are finite computations, not kernel/Lean-checked. The feasibility of
amplified states and the "sufficiently large n" quantifier rest on the front's
paper argument and the prior eindex construction, not on independent computation.
The result excludes (e,h), rank profiles and any coarsening that fails to
separate Q1/Q2; it does NOT exclude an arbitrary clever poly-time g that
separates them — the general "no such g exists" question stays open. No class
separation; SORT-BOUND-U stays sparse, in PSPACE and P/poly; no S(n) value; no
Lean. No new researcher dispatched (greedy-v-width-invariant-alln still running).

## Conclusion

Accepted as a correct barrier: the (e,h) and rank-profile compression routes
are closed on the greedy ball. The base gadget is empirically solid and
independently reproduced. The amplification is a paper construction whose
load-bearing arithmetic (depth threshold) checks out.
