# antonina-LEsODEfcTCzAID6x3qrYlD-prevented

Session: ses_e03e0fcbcffeukMWDtYpw9YHt8
Workspace: /home/lubko/soring-fronts/exec-exponent-shrink-20261121
Created: 1795231253416; updated: 1795232626776

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1fc1f07500010j0WhWpI79ptiK)

I'll start by reading the context docs and figuring out how the Antonina board is accessed, plus check the repo state.

## Output 41 (msg_1fc225376001L46PuTF0I9sqR2)

Now let me look at the Antonina board tooling and the existing repo scripts.

## Output 77 (msg_1fc2365c9001OJ50cYtZyfFe9P)

I have the digest tool. Now let me find how findings are posted to the board, and read board pages 4-10.

## Output 92 (msg_1fc239b5c0014w4OXh47AM4JiK)

Board pages 1-10 read. Now let me find how findings are posted to the board — checking `board_digest.py`'s data source and other posting mechanisms.

## Output 107 (msg_1fc23b689001hiZo6bEV6HYHGn)

Board pages 1-10 read. Now let me check the `antonina` posting CLI, and start the computational investigation: counting labelled posets and running the memoized DP.

## Output 153 (msg_1fc276886001zxz0pUqapllYFA)

Found a real gcc in the guix store. Let me compile and run the poset counter.

## Output 195 (msg_1fc27fcc50017wCnJXRmZOfP2D)

Counts match the board's A001035 values: 3, 19, 219, 4231, 130023. Now the memoized DP (computes S(n) and counts reachable states).

## Output 206 (msg_1fc280af30015ib7y4lUTzqJIi)

The DP has a reentrancy bug (global `succ` clobbered during recursion). Let me rewrite the DP section with explicit arrays.

## Output 233 (msg_1fc2958c10014tu2c5RKm6MXbQ)

DP now works and matches literature: S(2..6) = 1, 3, 5, 7, 10 ✓. The memoized DP visits all posets (states = A001035: 3,19,219,4231,130023). Let me extend to n=7 in the background and read the winning-frontier barrier doc.

## Output 248 (msg_1fc2a1740001O86Lkoxm5khkwt)

Let me check the DP n=7 run.

## Output 259 (msg_1fc2cdba8001od54rgvAW28aRa)

DP n=7 gives S(7)=12 — but the leaf-counting bound requires S(7) ≥ ceil(log2 7!) = 13, so the DP has a bug. I spot it: `pack` uses 6 bits per element but for n=7 a successor mask can have bit 6 set (7 elements), so the top bit is lost. Fixing to 8 bits/element.

## Output 288 (msg_1fc3021f9001lRQ0h61E1gaw47)

DP n=7 now agrees with literature: S(7)=13, states = 6,129,859. Let me cross-check A001035(7) from OEIS and kick off DP n=8 in the background.

## Output 364 (msg_1fc33d506001ei2kjyd4T0Eofb)

Deliverable complete: a finding note has been posted to Antonina board #301 (comment landed at `2026-11-21T03:43:21Z` by `SoringP1 researcher: exec-exponent-shrink-20261121`). Worktree is clean; no repo/Lean/commit/PR changes.

## Summary

**Exhibit attempt (negative).** Built a memoized poset DP in scratch (`/tmp/opencode/exp/poset_tools.c`) implementing `F(P)=0` if total else `1+min over incomparable {x,y} of max(F(P+x<y),F(P+y<x))`, with `S(n)=F(empty)`. Cross-checked against OEIS A001035 and the repo's literature table:

| n | A001035(n) | S(n) (DP) | log2(states)/n |
|---|---|---|---|
| 2 | 3 | 1 | 0.79 |
| 3 | 19 | 3 | 1.42 |
| 4 | 219 | 5 | 1.94 |
| 5 | 4231 | 7 | 2.41 |
| 6 | 130023 | 10 | 2.83 |
| 7 | 6129859 | 13 | 3.22 |

S(2..7) = 1,3,5,7,10,13 match the research-plan table (S(7)=13, the leaf bound ⌈log₂ 7!⌉=13). The DP state count equals A001035(n), and the exponent proxy grows ≈ 0.47 n — the DP is `2^{Θ(n²)}`, so it is not a `2^{O(n)}` machine and "exponent/n < 1−δ" fails. (A001035(8)=431723379 per OEIS.)

**Barriers reported.**
1. Memoized poset DP class: reachable DP states = all posets (lemma: every poset is reachable from ∅ by a constructive chain of closures; verified for n≤7 since DP states = A001035(n)). Hence DP time ≥ A001035(n) ≈ 2^{0.47 n²} — exponent `Ω(n²) ≥ Ω(n log n)`.
2. Winning-frontier barrier (`docs/research-winning-frontier-barrier.md`): `2^{(1/4−o(1)) n log² n}` nonisomorphic reachable winning posets at budget `S(n)` — any method enumerating them needs `≥ 2^{Ω(n log² n)}` transcripts; exponent `≥ Ω(n log² n) ≥ Ω(n log n)`, so transcript-bound-`2^{o(n log n)}` methods cannot compute S(n) in that class.

**Verdict:** no `2^{O(n)}` machine found; the natural DP is `2^{Θ(n²)}`; the claim "computable in `2^{O(n)}` on all n" remains unexhibited. Next obstacle: a method computing S(n) without enumerating poset states or winning states (budgeted DFS upper bound is `2^{O(n log² n)}`; quotient/structural routes give exactness without state-count gain so far).
