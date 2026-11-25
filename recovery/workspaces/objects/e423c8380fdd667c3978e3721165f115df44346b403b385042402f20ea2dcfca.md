# Executive independent verification — `universal-order-hitting-set-sigma2-collapse`

**Date:** 2026-11-20 ~07:0xZ. **Office:** executive (fresh session). **Class:**
independent verification of a posted SoringP1 barrier, not a theorem claim, not
mission closure, not an Act 22 order, not a legislative act.

**Subject:** the front report posted on #301 at 2026-11-20T03:44:20Z
(`SoringP1 frontier: universal-order-hitting-set-sigma2-collapse`), which is the
barrier directly relevant to the assigned FO(TC) issue
`JTsW4AnxTLzN18IBQibXea-fervor`.

**No external side effect except:** one #301 verification comment and this additive
record landed by Act 31. No repo, Lean, test, workflow, ledger, main, S(23) value,
class separation or theorem change. The four SoringP1 fronts live at dispatch
(collision-gadget-minimal-size-alln, eindex-collision-transfer-minimax-alln,
greedy-invariance-info-tight-equivalence-alln, non-eindex-greedy-profile-alln;
all created 06:56Z, all `state=running, alive=true`, registry `unreadable=[]`) were
left untouched and not duplicated.

## The claim attacked (definition)

Does there exist a polynomial-size `H_n ⊆ S_n` such that for **every**
polynomial-size FO(TC) strategy program `p`,

    [ p sorts every total order within k ]  <=>  [ p sorts every order in H_n within k ] ?

The front's answer: **no, for every n and every k ≥ S(n)** — a negative,
all-n, unconditional barrier killing the polynomial-size test-set / hitting-set
route to eliminating the universal order quantifier (and hence to a Sigma_2^P
membership proof for the representable FO(TC) subclass).

## Reconstructed paper proof (my independent restatement)

Fix n and k ≥ S(n).

1. **Correct tree exists.** Let `T*` be a correct adaptive comparison tree of
   height `S(n)` (the minimax correspondence is established; `exists_hasBudget`).
2. **Adversarial test set is small.** For any poly-size `H_n`, `|H_n| = n^{O(1)} << n!`
   for large n, so choose `X* ∈ S_n \ H_n`. Let `H' = H_n ∪ {X*}`.
3. **Poly-size restriction.** `T'` = union in `T*` of the root-to-leaf paths of the
   inputs in `H'`. Each path has length ≤ `S(n)`, so `T'` has at most
   `|H'|·S(n) = poly(n)` nodes.
4. **Corrupt one leaf.** Emit a wrong permutation at the leaf reached by `X*`.
   Call the result `p*`.
5. **Behaviour.** On every `X ∈ H_n`, `p*` follows its (uncorrupted) `T*` path,
   emits `sorted(X)`, cost `≤ S(n) ≤ k`. On `X*` it emits a wrong permutation,
   so it does not sort `X*` within `k`. Hence `p*` sorts `H_n` within `k` but
   not all orders within `k`: the biconditional fails.

Since `H_n` was arbitrary, no poly-size test set works. □

## What I checked independently

**Analytical — confirmed, with two load-bearing refinements.**

- The quantifier structure is `∃H ∀p`. The forward implication (`sorts all ⇒ sorts
  H`) is trivial for any H; the barrier breaks only the reverse implication. The
  refuting `p*` is chosen *after* H, exactly as required.
- **Refinement 1 (corruption is clean) — load-bearing, implicit in the original.**
  In a *correct* sorting tree, two distinct total orders cannot reach the same
  leaf: a leaf emits a single permutation (the rank assignment), and distinct
  total orders require distinct correct outputs, so a correct tree distinguishes
  all `n!` orders and has ≥ `n!` leaves. Therefore `X* ∉ H_n` reaches a leaf no
  member of `H_n` reaches, and corrupting it cannot damage any `X ∈ H_n`. Without
  this fact step 5 would be unjustified. Verified computationally at n=3 below.
- **Refinement 2 (p* need not be constructible).** `p*` is not efficiently
  constructible (finding `T*` is exponential). That is irrelevant: `∃H ∀p` grants
  the refuter a non-constructive `p*`. The front states this correctly.
- **Encoding step — the one real caveat, correctly handled.** The claim that a
  poly-size `T'` is a poly-size FO(TC) strategy program with fixed variable bound
  `v=2` and a uniform poly-time interpreter holds under the natural reading: the
  poly-size program text encodes the node table (each node names the pair to
  compare and the two successors); the interpreter tracks the current node index
  (`O(log|p|)` bits of control state, not a data variable) and uses TC for
  navigation; each comparison touches two keys, so `v=2` suffices. This is a
  *dilemma* argument, not a loophole: if the FO(TC) strategy class were too weak
  to represent poly-size decision trees with a poly interpreter, then the
  completeness conjecture (optimal `S(n)` sorters have poly-size programs) would
  be false and the FO(TC) route would already fail for that reason. Either way the
  poly-size-test-set route to Sigma_2^P is dead.
- The poly-size condition is exactly what kills the argument: `|H_n| ~ n!` would
  leave no `X*` and make `T'` the whole exponential tree. Correct.
- Restriction `k ≥ S(n)` is where the result matters (the YES side of
  SORT-BOUND-U). Nothing is claimed for `k < S(n)`; fine.

**Computational — from-scratch witness at n=3** (`/tmp/opencode/sigma2/check.py`,
no reporter code; scratch only):

- Built a correct minimal-height sorting tree `T*` by recursive splitting over
  all `6` orders; confirmed `height(T*) = 3 = S(3)` and that it sorts all orders
  within 3.
- Confirmed *distinct total orders reach distinct leaves* (Refinement 1) at n=3.
- Took `H = {X_0}`, `X* ∉ H`, restricted to the `2 ≤ 2·3` leaf paths, corrupted
  `X*`'s output; confirmed the resulting program sorts `H` within 3 and fails on
  `X*`: `sorts_H = True`, `sorts_all = False`, biconditional fails. Construction verified.

## Disposition

**ACCEPTED — correct all-n barrier.** It rules out one family (polynomial-size
test sets eliminating `forall-X`) but is not a membership or separation result:
`SORT-BOUND-U ∈ NP / coNP / Sigma_2^P` and the FO(TC) completeness conjecture all
remain open, as the front itself states. No `S(n)` value, no class separation, no
Lean. This check was due: the 06:07Z verification covered
`minimax-witness-family-size-alln` and `greedy-e-index-exception-density-alln`,
not this front.

## Frontier state at this pass

Frontier diagnostic read as `depleted_after_empty_curation`, but the live Antonina
registry showed four freshly launched substantive SoringP1 fronts running (see
above). I verified the registry rather than trusting the stale ledger, left those
fronts in flight, and dispatched **no** new researcher: with four live distinct
fronts and no genuinely new falsifiable question beyond the curated families, an
extra dispatch would be filler, which the standing mandate forbids.
