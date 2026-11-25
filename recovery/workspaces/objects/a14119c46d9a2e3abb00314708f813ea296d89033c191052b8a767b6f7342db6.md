# Executive independent verification — `greedy-v-width-invariant-alln`

**Date:** 2026-11-20 ~08:3xZ. **Office:** executive (fresh session). **Class:**
independent verification of a posted SoringP1 result — not a theorem claim, not
mission closure, not an Act 22 order, not a legislative act.

**Subject:** the front report posted on #301 at 2026-11-20T08:15:49Z. This was
the one unverified substantive claim left from the previous pass (the
`greedy-v-width-invariant-alln` front; no other seat had checked it).

**External writes only:** one #301 verification comment (posted 08:23:17Z) plus this
additive record, landed by Act 31. No repo, Lean, test, workflow, ledger, main,
S(n) value or class separation change. SoringP1 main `/home/lubko/soring301`
was not modified.

## What the front claims

For all sufficiently large n there are 2^{Ω(√(n/log n))} distinct extension
counts c, each realized by two states in B_{G(n)}(n) with the same
(e,width)=(c,w) but different greedy value V. Hence any (e,width)-keyed
evaluator needs superpolynomially many exceptions. Together with the 06:42Z and
07:33Z fronts, the "extension count + simple structural refinement"
compression family is closed for V.

## Independent method

From-scratch Python `/tmp/opencode/verify_greedy_vwidth.py` (own transitive
closure, subset-DP linear-extension count, memoized greedy max-extension V with
adversarial tie-break, Dilworth width by brute force over subsets, ordinal-sum
construction, exact integer arithmetic). No researcher code reused.

## Results — every load-bearing claim checked

- **Base gadget.** Q1=[14,8,8,0,0,0], Q2=[6,4,0,16,0,0]: e=60 both; V=6 vs 7;
  width=4 vs 3. Matches the front exactly. This is why width separates the
  gadget and cannot be used directly as an (e,width) collision.
- **Ordinal-sum padding.** n=10, S=∅: e(P_10)=e(Q_10)=1440; width=4 both.
  Multiplicativity of e and the width(C_S)≥4 condition verified numerically.
- **V additivity.** Checked independently on antichain_2 ⊕ antichain_2:
  V=2=1+1, e=4=2·2.
- **Depth threshold.** 8n−44 ≤ ceil(log₂ n!) holds exactly for n=700
  (5556 ≤ 5613) and n=1000 (7956 ≤ 8530), with growing margin.
- **Counting.** Low-width subsets (width(C_S)≤3) are O(m³) (at most 3 distinct
  primes summing to m−r), versus 2^{Ω(√(m/log m))} distinct-prime subsets;
  the superpolynomial conclusion follows. Distinctness of e(C_S) by
  largest-prime valuation accepted as a correct valuation argument.

## Limits preserved

- V/e are finite computations, not kernel/Lean-checked; V additivity and
  ordinal-sum formulas are standard deductions checked on small cases.
- Reachability and the depth bound are inherited from the prior fronts' verified
  construction; no independent full BFS was performed at n≥700 (honest limit (ii)
  of the front).
- The result excludes (e,width) and any coarsening that fails to separate Q1
  from Q2; it does NOT exclude an arbitrary clever poly-time evaluator g. The
  general "no such g" question remains OPEN.
- No S(n) value, no class separation, no Lean artifact. SORT-BOUND-U stays
  sparse, in PSPACE and P/poly.

## Conclusion

Accepted as a correct barrier: width does not rescue the e-index compression
route. Together with the 06:42Z and 07:33Z fronts, the "extension count +
simple structural refinement" compression family is closed on the greedy ball.
S(23) stays [75,76]. No new researcher dispatched: all distinct live fronts
from the previous pass are now verified, and no new falsifiable question beyond
the curated families was identified this pass.