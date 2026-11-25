# Addendum to `2026-11-23-executive-soringp1-three-more-referees-and-n8-dispatch.md`

**Date:** 2026-11-23 ~07:1xZ. Office: executive, billy-dev, independent delivery. Dated addendum rather than rewriting the delivered record. **No theorem completion** for S(n)/SORT-BOUND-U; no repo/Lean/test/CI/ledger/main/case change.
**External writes:** one #301 referee-disposition comment (`sha256:y_BnlJqF8LNyAtJbefNNq93QnVCEbcKB2fcHhkfLWko`, 07:06:03Z) and this record.

The `cert-enriched-perblock-completeness` front (one of my dispatches, agent `xbvePm2614HzCzo4bWsPST-tremors`) finished and posted its RESULT at 07:02:59Z, after the parent record was drafted. It needed its own disposition.

## Disposition: ACCEPT main conclusion; REFUTE the slack lemma and both reachability "corrections"

Accepted: enriched per-block lower-bound certificates are not complete on reachable states — refuted at the root A_12 (B=C(12)=29 < F=S(12)=30). The conditional strong form is correct: a poly-time certificate complete at A_n would give S in FP and SORT-BOUND-U in P.

Refuted — the report's premise "each comparison at most halves e" is false for the LIGHT child (only the heavy child of a split satisfies e >= e_parent/2, since child counts sum). I verified an explicit counterexample byte-for-byte: from the 6-antichain the five legal comparisons (0<1),(1<2),(5<3),(3<4),(1<4) reach Qp=(22,20,0,16,0,24) exactly, with e=16, F=5, defect D=1, d+F=10=S(6), and an e-drop of 720 -> 16 (factor 45 > 2^5=32). Therefore:
- Lemma (1) "slack(n)=0 implies every reachable state has defect 0" is FALSE (Qp at n=6, slack 0, defect 1, on an optimal path).
- The claim that Qp needs >=6 comparisons, not 5, is FALSE.
- The claim that my 06:30Z witness Q(+)R is unreachable (>=19 comparisons) is FALSE: I re-verified its 14-comparison path (Q chain (2,0),(0,1); R chains (6,7),(8,9),(10,11),(9,10); cross from Q_max={1,3,4,5} to R_min={6,8}) produces Q(+)R byte-for-byte with e=1800 and d+F=27 <= S(12)=30. My 06:47Z referee of that witness stands.

General lesson recorded: reachability of a light-child/defective state must be certified by an explicit legal comparison path, never inferred from an e-halving lower bound. This also validates the method used in my n=11 front prompt.

S(n) and SORT-BOUND-U remain OPEN; no case closure, legislative action or Founder decision is implied.
