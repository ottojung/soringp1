# antonina-KVSVClll9IJZSqtdWGHWz8-labyrinth

Session: ses_dff2fa562ffeIUANkmWthBpBAp
Workspace: /home/lubko/soring-fronts/t5-uniform-base-extension-alln
Created: 1795309984500; updated: 1795313673688

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 563 (msg_2010886f5001ZblToqk1MKXLie)

## Result: T(5) = 29 is refuted (on n = 7)

**Mathematical finding.** The claim “every poset P with e(P) ≤ 29 has m(P) ≤ 5” (the all‑n gloss of T(5)=29) is false. Exhaustive enumeration of labelled posets on 7 elements with e(P) ≤ 32 (reverse BFS from total orders by cover‑relation removal, deduplicated: 1,871,310 posets) found **261,240 posets with m(P) ≥ 6**, the smallest extension count being **e(P) = 21**. Hence the first failing e on n = 7 is 21, not 30, and T(5) (all n) is at most 20.

**Falsifier (user’s literal horn, e(P) ≥ 30, m(P) ≥ 6).**  
P = (100, 20, 0, 22, 4, 68, 0) on 7 elements (succ‑bitmask, transitively closed). Independently verified: e(P) = 30, exact minimax m(P) = 6.

**Stronger witness.** P = (62, 48, 56, 16, 0, 0, 58) on 7 elements: e(P) = 21, m(P) = 6 (exact minimax; transitively closed).

**Method.** e(P) via subset‑DP linear‑extension count (memoized); m(P) via the minimax game value (memoized DP); bounded check m(P) ≥ 6 ⟺ not sortable within 5 comparisons (F(P,5) false), cross‑checked by exact minimax on witnesses. F verified on known posets (total → True; H3 e=8 m=4 → True; A4 e=24 m=5 → True; A5 e=120 m=7 → False).

**Honest limits.** (1) Only n = 7 enumerated; the n ≤ 6 certificate (T(5)=29 for n ≤ 6, first failing e = 30) stands. (2) All‑n T(5) ≤ 20; n ≥ 8 may push the first failing e lower — proposed follow‑up: same reverse‑BFS on n = 8 with E_BOUND = 21/32. (3) No repo/Lean/test/CI changes; scratch only. (4) The backward‑search pruning table’s budget‑5 base is not 29 all‑n and must be indexed by n.

**Reported.** Single concise update posted to Antonina board #301 (author `SoringP1 researcher: t5-uniform-base-extension-alln`, 2026‑11‑22T02:13:59Z). Worktree remains clean.
