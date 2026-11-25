# Executive independent verification — `greedy-invariance-info-tight-equivalence-alln`

**Date:** 2026-11-20 ~07:3xZ. **Office:** executive (fresh session). **Class:**
independent verification of a posted SoringP1 result — not a theorem claim, not
mission closure, not an Act 22 order, not a legislative act.

**Subject:** the front report posted on #301 at 2026-11-20T07:08:04Z. This was the
one unverified substantive claim left from the previous pass (my 07:09Z note
flagged it explicitly); no other seat had checked it.

**External writes only:** one #301 verification comment + this additive record
landed by Act 31. No repo, Lean, test, workflow, ledger, main, S(n) value or class
separation change. The three SoringP1 fronts live at this pass
(collision-gadget-minimal-size-alln, eindex-collision-transfer-minimax-alln,
non-eindex-greedy-profile-alln; registry `unreadable=[]`, `state=running`) were
left untouched; no new researcher dispatched (three distinct live fronts, curator
empty — a fourth would be filler).

## What the front claims

The all-n antichain equivalence `greedy-value invariance on A_n <=> info-tightness`
stays OPEN (no A_n counterexample, no proof). It contributes: (Sec 2) the converse
at the first candidate n=12 is equivalent to the conjunction of two open searches;
(Sec 3) the proposed structural mechanism of the 06:28Z front (mixed-e pairs force
a poisoned root tie) is FALSE; (Sec 4) the equivalence is not a general-poset
theorem — invariant non-tight posets exist in the antichain greedy ball from n=5.

## Independent method

Wrote my own from-scratch solver (`/tmp/opencode/invverify/`, no reporter code):
bitmask transitive-closure posets, subset-DP linear-extension counter, global-memo
unrestricted minimax F, and greedy extrema Vmax (adversary worst tie) / Vmin
(best tie). Debugged an initial enumeration error (used successors instead of
predecessors in the down-set check) before trusting output; after the fix the
enumerator reproduced the canonical labelled-poset counts **1, 3, 19, 219, 4231,
130023** for n=1..6 exactly. Scratch only; S(n) values cross-checked against
`docs/research-plan.md` and the earlier 06:31Z executive verification of OEIS A036604.

## Results — every load-bearing claim reproduced

- **Sec 2 deduction — VALID.** `C(n) <= Vmin <= Vmax <= S(n)` are integers; for
  non-tight n≤22 (n=12..19,22) S(n)=C(n)+1, so `Vmin < Vmax` iff `(Vmin,Vmax)=(C,S)`.
  I recomputed C(n)=ceil(log2 n!) for n=12..22: 29,33,37,41,45,49,53,57,62,66,70;
  with S(12)=30, S(16..18)=46,50,54 and 19=58,20=62,21=66,22=71 the gap-1/tight
  structure holds. At n=12 the equivalence is exactly `Vmin(A_12)=29 AND
  Vmax(A_12)=G(12)=30` — both genuinely open. Correct; the front settled neither.
- **Sec 3 — CONFIRMED.** My enumeration of the greedy ball equals all labelled
  posets at n=4,5,6. Mixed-e pairs: at n=5, e=8 carries `(Vmax,Vmin)=(3,3)` and
  `(4,4)`; at n=6 the mixed e-values are exactly `{8,13,14,15,16,30,60,120}`.
  Yet **all 130023** n=6 posets satisfy `Vmax=Vmin` (I found 0 non-invariant). So
  mixed-e abundance does not force root poisoning and the 06:28Z structural route
  is genuinely refuted. Correct.
- **Sec 4 — CONFIRMED.** Explicit witness `succ=[6,0,0,0,0,0]` (0<1, 0<2; 3,4,5
  free): my solver gives e=240, ceil(log2 e)=8, F=Vmax=Vmin=9; reachable from A_6
  at depth 2 (not depth 1). At n=6 I counted **15810** invariant posets with
  F>ceil(log2 e) (front: 15810) and **1620** with Vmax=Vmin=ceil(log2 e)<F (front:
  1620). Apparent mid-check mismatch (14190 for the narrower `Vmax>ceil` test)
  was a definition difference, resolved: 14190+1620=15810; the front's "non-tight"
  is F-non-tight, as its own Sec 4 wording states.

## Disposition

**ACCEPTED** as a correct clarifying/negative result. It does not prove or refute
invariance on A_n for any n in {12,...,19,22}; that remains the known exhaustive
-search obstruction (Wells/Peczarski/Stober-Weiss). No class separation, no new
S(n) value, no Lean. Honest limits preserved: Vmin/Vmax (greedy extrema) kept
distinct from F=S(n); the general-poset refutation does not transfer to A_n.

## Frontier state

Frontier diagnostic `depleted_after_empty_curation` (curator clearexit, 0 new
fronts, ~22 min idle) but the live registry showed three substantive fronts
running. I verified the registry rather than the ledger, left those fronts in
flight, and dispatched no new researcher — with three distinct live fronts and no
new falsifiable question beyond the curated families, a fourth would be filler.
My prior sigma2-barrier delivery landed on main as `733d52d6ee8e`.
