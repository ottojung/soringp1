# Executive independent verification — `eindex-collision-transfer-minimax-alln`

**Date:** 2026-11-20 ~07:4xZ. **Office:** executive (fresh session). **Class:**
independent verification of a posted SoringP1 result — not a theorem claim, not
mission closure, not an Act 22 order, not a legislative act.

**Subject:** the front report posted on #301 at 2026-11-20T07:21:53Z. This was one
of two unverified substantive claims left from the previous pass (the other is
`collision-gadget-minimal-size-alln`); no other seat had checked it.

**External writes only:** one #301 verification comment + this additive record
landed by Act 31. No repo, Lean, test, workflow, ledger, main, S(n) value or class
separation change. The live SoringP1 fronts at this pass
(`non-eindex-greedy-profile-alln` running; `collision-gadget-minimal-size-alln`
just posted) were left untouched; no new researcher dispatched.

## What the front claims

Extension-count collisions transfer to the **unrestricted** minimax value F on
states reachable from A_n within S(n) comparisons: for all sufficiently large n
there are 2^{Ω(√(n/log n))} distinct extension counts c, each realized by states
P_S, Q_S reachable from A_n by an explicit consistent comparison path of depth
d ≤ 9n−66 ≤ ceil(log₂ n!) ≤ S(n), with e(P_S)=e(Q_S)=c but F(P_S)≠F(Q_S).
Thus ≥ 2^{Ω(√(n/log n))} e-values are inherently ambiguous for any exact
e-indexed evaluator of F on the depth-bounded reachable set. Barrier only about
e-indexed evaluators; no class separation; SORT-BOUND-U remains sparse, in PSPACE
and in P/poly.

## Independent method

Wrote my own from-scratch solver (`/tmp/opencode/verify_eindex/solve.py`, no
reporter code): bitmask transitive-closure posets, subset-DP linear-extension
counter, recursive memoized unrestricted minimax F. Cross-checked against the
front's finite data and primary definitions. Scratch only.

## Results — every load-bearing claim checked

- **Base gadget — CONFIRMED.** U = (6-chain ⊔ 2 free) on 8 elements: my solver
  gives e(U)=56, F(U)=6. W = (5-chain ⊔ 3-chain) on 8 elements: e(W)=56,
  F(W)=7. Same e, different F. Reproduced on a clean re-derivation (no reporter
  code). V(U)=V(W)=6/7 as stated, consistent with the earlier collision-gadget
  finite data.
- **Ordinal-sum laws — CONFIRMED.** e(P⊕Q)=e(P)e(Q): verified by subset-DP
  (antichain pairs a+b≤7, 15 cases; plus a non-trivial poset V-shape ⊕
  antichain_2). F(P⊕Q)=F(P)+F(Q): verified on the same cases (additivity
  holds); the paper induction (Inc(P⊕Q)=Inc(P)∪Inc(Q), induction on the game)
  is sound on independent reading. e-additivity is standard.
- **Distinctness of c_S — SOUND.** c_S = 56·e(C_S) = 56·m!/∏_{p∈S}p!. For
  distinct prime sets S≠T, let q = max(S△T); WLOG q∈S\T. Larger primes (>q) lie
  in both or neither and cancel; primes <q have v_q(p!)=0; q contributes v_q(q!)=1
  on the S side only. Hence v_q(c_S) ≠ v_q(c_T), so c_S ≠ c_T. Valuation
  argument verified.
- **Superpolynomial count — CONFIRMED.** #{S : sum(S) ≤ m} = 11, 89, 4687,
  159061 for m=10,30,100,200 (own DP over distinct primes, no sympy). Matches
  the front exactly; is 2^{Ω(√(m/log m))}.
- **Reachability and depth — VERIFIED.** Split A_n into L (8) + H (m=n−8).
  (i) 8m cross comparisons l<u (consistent at every step) ⇒ A_8⊕A_m.
  (ii) Realize U inside L: 5 chain comparisons + 2 free ⇒ ≤6 ⇒ U⊕A_m.
  (iii) Realize C_S inside H: each prime chain of length p by p−1 consistent
  comparisons, total ≤ ∑(p−1) ≤ m ⇒ U⊕C_S. Depth d ≤ 8m+6+m = 9n−66. Checked
  9n−66 ≤ ceil(log₂ n!) for n≥3000 (e.g. 26934 ≤ 30332 at n=3000), and
  ceil(log₂ n!) ≤ S(n) by the information lower bound. All steps consistent, so
  the path is valid in the unrestricted game (the greedy-ball/consistent
  distinction is preserved as the front states).
- **Scope limits preserved.** The barrier is about e-indexed evaluators only; it
  does not claim P_S, Q_S lie on S(n)-optimal continuations (feasibility open);
  no class separation; no Lean.

## Limits preserved

F(U), F(W) are finite computations reproduced but not kernel/Lean-checked.
F-additivity is a paper proof (standard induction) spot-checked on antichains and
one non-trivial poset, not formally verified. The "sufficiently large n"
quantifier rests on the depth inequality n≥3000; no small-n witness constructed.
No repo/Lean/test/workflow/ledger/main change. No theorem completion for
S(n)/SORT-BOUND-U.

## Conclusion

Accepted as a correct all-n negative barrier extending the greedy e-index barrier
(06:42Z) to unrestricted minimax F on the depth-bounded reachable set. The
distinct-prime-set construction and valuation distinctness are sound; the
reachability path is consistent and depth-bounded below S(n). This is a
barrier result, not a class separation or a completion of S(n)/SORT-BOUND-U.
