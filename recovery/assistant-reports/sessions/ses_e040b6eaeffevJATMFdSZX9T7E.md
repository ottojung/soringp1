# antonina-RyJ4idf6HOrLUx3oeKqxG3-invisible

Session: ses_e040b6eaeffevJATMFdSZX9T7E
Workspace: /home/lubko/soring-fronts/exec-exponent-shrink-nlogn-2expn-alln
Created: 1795228471752; updated: 1795230060871

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1fbf499880014BQfYFon4rEsyA)

I'll start by getting oriented in the repository and reading the key documents.

## Output 25 (msg_1fbf86284001KvHPE1R0PAWZu1)

Now let me read the winning-frontier barrier, the plan, and the operations/board documents.

## Output 65 (msg_1fbf8885a001c41DNv5mF7embE)

Let me look at the remaining relevant docs and the scripts/tests to understand definitions (transcript bound, winning frontier) and existing tooling.

## Output 93 (msg_1fbfb5635001iCDTqDnQU7bMQQ)

Now I understand the model. Let me now do a concrete data-gathering experiment: compute `S(n)` exactly via the poset minimax DP over all labelled posets (A001035 counts are known: n=2:3, n=3:19, n=4:219, n=5:4231), and check structural invariants of the DP value.

## Output 111 (msg_1fbff422f001x6zPDgKaCqJqIH)

Small bug — let me debug quickly.

## Output 122 (msg_1fbffd736001pLru03B79QaED1)

Found it — the memo was shared across `n`, so the empty poset early-returned without populating the per-`n` `Fs`. Fixing:

## Output 165 (msg_1fc006c130015JAiKovfxjXemy)

The DP confirms `S(n)` for n ≤ 5 (1, 3, 5, 7 — matching the repo values), and shows `F(P)` is **not** determined by simple scalar invariants like `#incomp`. Now let me check the research board and prior work on this front to ground the research.

## Output 180 (msg_1fc0219d2001ckiSAYmEjHhxtC)

The board shows this front is under active investigation (`exec-adversary-method-lb-barrier-20261121`, `exec-s23-search-window-20261121`). Let me now do deeper structural analysis: optimal-play state counts and invariants of the minimax value.

## Output 198 (msg_1fc03fd8a001Jjq2ncynFqNI5E)

The data is solid. This front has siblings on other branches (`time-exponent-nlogn-barrier-alln`, `time-exponent-adversary-alln-20261119`) — let me read those for context on how barriers of this form are approached here.

## Output 218 (msg_1fc0774d2001Or8QR2Jb9o1Iq6)

Let me extend the analysis: winning-frontier sizes at the information budget, and the "one known pair" game value (the `F({a<b})` data).

## Output 236 (msg_1fc08fd72001H2lr18DQq5hIY7)

The data is in. Let me verify the repo's own value table against my DP (cross-check `S(6)` claims) and find the board-posting tool for the report.

## Output 277 (msg_1fc09f99a001FBHG6e0bjUwjDY)

My DP matches the repo's `evaluate.py` exactly (S(2..6) = 1,3,5,7,10). Now let me find the board-posting tool.

## Output 306 (msg_1fc0a4784001aqTU1g10ZcG3Hr)

Before reporting, one more quick hypothesis test: is `F(P) = ceil(log2 e(P))` (the information bound) true for small `n`? Computing linear-extension counts `e(P)` via memoized DP over posets:

## Output 324 (msg_1fc0abf5d001HBKVfMmE5Y9920)

My `compute_e` had an ordering bug. Fixing with a memoized recursion:

## Output 358 (msg_1fc0b44cd001BwGbibhm0ZJof2)

The info-bound hypothesis `F(P) = ceil(log2 e(P))` holds at n≤4 but fails at n=5 — nice structural data point. Let me check the direction of the mismatches:

## Output 369 (msg_1fc0bcb40001cYFxLX7f2K0xb1)

Investigation complete — inconclusive so far (no upper-bound method found, no barrier proof). Per the delivery rules, I'll post this to #301 as a concise update.

## Output 387 (msg_1fc0c7408001GDp9Pk2F9YVTC6)

Let me verify the comment was appended by reading the board digest.

## Output 398 (msg_1fc0c81c8001zGfLNAX0C75yU4)

The report is posted (2026-11-21T03:00:33Z). Let me confirm the worktree state per the delivery rules.

## Output 409 (msg_1fc0cabe2001Fzt2hKxrY1r0UO)

Done — investigation on `billy-dev`, scratch in `/tmp/opencode`, worktree clean, report posted to #301 (`exec-exponent-shrink-20261121`, 03:00Z).

**What I did:**
- Modeled the question as the poset minimax DP (`docs/upper-bound.md`): `F(P) = 0` if total, else `1 + min over incomparable pairs of max(F(P+xy), F(P+yx))`, `S(n) = F(∅)`.
- Enumerated all labelled posets (A001035 counts: 3, 19, 219, 4231 for n=2..5) and computed `F` on every one — cross-validated against `scripts/evaluate.py`: `S(2..6) = 1, 3, 5, 7, 10` ✓.

**Findings (inconclusive, not resolved):**
- **State space is intrinsic to the game**: the DP needs all labelled posets (`2^{Θ(n²)}`); the budgeted DFS gets `2^{O(n log² n)}`.
- `F` is **not** determined by scalar invariants (width, height, #comp, (width,height)) — matches the repo's "five scalar invariants falsified" theme.
- `F({a<b}) = S(n) − 1` at n=4,5, consistent with `F(∅) = 1 + F({a<b})`.
- `F(P) = ceil(log2 e(P))` for all posets at n≤4; at n=5, 120 posets have `F(P) = ceil(log2 e(P)) + 1` — the information-bound gap appears as early as Wells' `S(12)=30 > C(12)=29`.
- Optimal-play states (F decreases by 1 per step along worst-case plays): 181/219 (n=4), 2251/4231 (n=5) — optimal plays visit most posets, so no collapse.
- Winning frontier at the info budget: 120 (n=4, t=3), 1390 (n=5, t=4).

**Obstacles for the report:** no method with exponent `< n log² n` was found (the poset DP looks intrinsic), and no barrier proof yet — the winning-frontier barrier is an *enumeration* barrier at the info budget (`2^{Ω(n log² n)}` transcripts) and is not a time lower bound for selective methods; no adversary lower bound of `Ω(n log n)` transcripts is known.

So: the question remains open — the claim (either `2^{O(n)}` machine or `2^{o(n log n)}`-transcript method) is not falsified, and no exhibiting construction was found either.
