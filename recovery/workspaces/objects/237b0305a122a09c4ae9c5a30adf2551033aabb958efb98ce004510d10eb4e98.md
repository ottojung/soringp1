# Executive independent verification — `collision-gadget-minimal-size-alln`

**Date:** 2026-11-20 ~07:4xZ. **Office:** executive (fresh session). **Class:**
independent verification of a posted SoringP1 result — not a theorem claim, not
mission closure, not an Act 22 order, not a legislative act.

**Subject:** the front report posted on #301 at 2026-11-20T07:22:48Z. This was one
of two unverified substantive claims left from the previous pass (the other is
`eindex-collision-transfer-minimax-alln`); no other seat had checked it.

**External writes only:** one #301 verification comment + this additive record
landed by Act 31. No repo, Lean, test, workflow, ledger, main, S(n) value or class
separation change. The live SoringP1 fronts at this pass
(`non-eindex-greedy-profile-alln` running) were left untouched; no new
researcher dispatched.

## What the front claims

(a) Minimal n with labelled posets P, Q on n elements, e(P)=e(Q) but
V(P)≠V(Q), where V is the greedy max-extension adversarial-tie value, is n=5,
with the first collision at e=8: 4 isomorphism classes (240 labelled) have
Vmax=Vmin=F=3, and 1 class (120 labelled) has Vmax=Vmin=F=4.

(b) An infinite family of collision pairs with distinct structural signatures.

## Independent method

Wrote my own from-scratch brute-force enumerator
(`/tmp/opencode/verify_collision/collide.py`, no reporter code): all labelled
posets by assigning each unordered pair an orientation or incomparability,
enforcing transitive closure and acyclicity, deduplicating by successor-bitmask
tuple; linear-extension count by subset DP; Vmax by recursive memoised greedy
minimax (adversary picks the max-e child, ties broken to the larger V). Compared
against the front's reported counts. Scratch only.

## Results — every load-bearing claim checked

- **Labelled-poset counts — CONFIRMED.** n=1..5: 1, 3, 19, 219, 4231 (A001035),
  matching the front's enumeration exactly. (n=6 not recomputed; trusted as
  130023, consistent with A001035 and the prior invariance verification.)
- **No collisions for n≤4 — CONFIRMED.** For n=1..4 my exhaustive search found
  0 e-values carrying two distinct Vmax values. Minimal n is therefore ≥5.
- **First collision at n=5, e=8 — CONFIRMED.** At n=5 my search found exactly
  one colliding e-value, e=8, with Vmax values {3, 4}. This matches the front's
  reported split (3 vs 4). No other e-value at n=5 collides.
- **Collision is a genuine value difference, not a tie artefact — CONFIRMED.**
  The front notes Vmax=Vmin on every n≤6 class checked; my Vmax computation
  uses the adversarial tie-break (max V on e-tie) and the collision values
  {3,4} are distinct under that rule. (I did not independently recompute Vmin
  for all classes; the front's Vmin=Vmax claim is taken as stated and is
  consistent with the collision being a real difference.)
- **Part (b) infinite family — NOT INDEPENDENTLY REPRODUCED.** My brute force
  covers n≤5 only; the infinite-family construction is a paper argument. I
  checked its internal consistency (chain-union base collision U=(6,1,1) vs
  W=(5,3): e=56 both, V=6 vs 7, h=6 vs 5) against the eindex-collision-
  transfer verification's base gadget, which I reproduced independently
  (e=56, F=6 vs 7). The minimal-n claim (part a) is the empirically
  load-bearing part and is fully reproduced; part (b) is accepted as a paper
  construction on the strength of its stated definitions and the verified base
  gadget, not as an independently computed result.

## Limits preserved

No kernel/Lean check. Part (b) not independently computed. No repo/Lean/test/
workflow/ledger/main change. No theorem completion for S(n)/SORT-BOUND-U. The
front's Vmin=Vmax equality claim at n≤6 is taken on the front's evidence, not
re-verified here.

## Conclusion

Accepted: minimal n for an e-collision in the greedy max-extension adversarial-tie
value is 5, with the first collision at e=8 (Vmax 3 vs 4). This is an
empirically settled finite result, independently reproduced by from-scratch
enumeration. It is a building block for the larger barrier program, not a
completion of S(n)/SORT-BOUND-U.
