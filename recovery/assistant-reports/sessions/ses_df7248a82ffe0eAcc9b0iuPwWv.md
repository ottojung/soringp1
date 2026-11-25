# antonina-s89XZxRMLHMMv9avxOJvod-necks

Session: ses_df7248a82ffe0eAcc9b0iuPwWv
Workspace: /home/lubko/soring-fronts/lemmaD-cospectral-n7-20261123
Created: 1795444929990; updated: 1795447142950

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 13 (msg_208e2e737001paRUTNkfHS2kLU)

I'll start by inspecting the current state thoroughly before any external action, as required by the recovery instructions.

## Output 28 (msg_208e305dd001H81Ghgjvide0D7)

There's substantial scratch including files from ~14:42-14:49 that appear related to this exact task. Let me inspect those and check whether the board comment was already posted.

## Output 47 (msg_208e318d0001N95IqWpKgczL9G)

No prior board post exists with this exact slug/author — only the prompt file and a scratch script (`oneply_check.py`) exist. Let me read the project docs, prior-art board posts, and existing n=7 scratch code to understand what's already been tried.

## Output 70 (msg_208e34de7001Q3F3gQtizMz4nQ)

Let me examine the board prior art and recent scratch outputs to understand what's already established, then decide the computational approach.

## Output 85 (msg_208e3c1cf0013HAdJ8gUfSpDTz)

I have a clear picture now. No prior post with this slug exists; the n=6 result (154 keys, 0 conflicts) is the baseline; a full n=7 enumeration (~6.1M labeled posets) is computationally feasible. Let me write an independent exhaustive C++ checker.

## Output 195 (msg_208e6956a001CXxm9XuH5LvWlm)

Compiled successfully. Let me validate at n=6 against the known baseline before running n=7.

## Output 206 (msg_208e6a80b001l3Hfcg0SaVuwLm)

The generator was wrong (only 4824 posets — it only produced posets whose edges go from lower to higher index). Since e, M1, and F are all isomorphism-invariant, I can equivalently enumerate all labeled posets via a complete BFS from the antichain with transitive closure and dedup. Let me rewrite with a memoized recursive solver.

## Output 224 (msg_208e79a45001tkFtD0W7CfLZCK)

n=6 validation matches the known baseline exactly: 130,023 states, S(6)=10, 0 conflicting keys (155 keys = the known 154 non-total keys + 1 total-order key). Now the decisive n=7 run.

## Output 235 (msg_208e9388f0011xJnJwF6uoYF4W)

A **counterexample exists at n=7**. But my conflict printout has a cosmetic bug (it prints the NEW poset's F for both). I must verify rigorously with two independent implementations before reporting. Let me write a fully independent Python verifier using brute-force permutation counts and a world-set minimax.

## Output 255 (msg_208e9a98e001Z4iLaJDe2sZisu)

The counterexample is verified by two independent implementations. Now let me fix the cosmetic print bug and get exact counts (distinct keys with differing F), plus data for the reachability bonus.

## Output 287 (msg_208ebec8d001OxZA6aeyBqGl1b)

Exactly **one** conflicting signature key (e=32), with F values {5,6}. Let me investigate the bonus reachability question: at σ=0 along optimal play, F(P)=13−d exactly; a poset with e=32 needs d≥8, so the F=6 member (needing d=7) cannot be optimal-play reachable. Let me verify reachability by BFS over F-optimal moves.

## Output 355 (msg_208f1890a001NV3EIg4JaB473W)

My BFS used only F-optimal pairs (missing σ>0 states reachable via the "easy" child). Let me correct it to full k-safe reachability (both children viable within budget 13).

## Output 373 (msg_208f3797d001D9aMn7nK9w0xR8)

The corrected BFS reproduces the prior front's exact reachable-state count (3,044,007), validating it. Neither witness is reachable. Let me check whether **any** of the 5040 F=5 posets with the conflicting signature is optimal-play reachable, to make the bonus statement precise.

## Output 453 (msg_208f7726000117TKQIsqDk2xNh)

Nuanced bonus result: 2,520 reachable states share the conflicting signature, but the numeric bound (e=32 ⇒ d≥8 ⇒ F≤5) forces all reachable ones to have F=5; the F=6 mate is unreachable. Let me verify a reachable example independently.

## Output 464 (msg_208f79b2f001CsJiXVkSO6wo1N)

Verified. Now let me confirm state and find the exact board-posting mechanism before making my single external write.

## Output 484 (msg_208fc5c6f001f77fhajvMmQ3TD)

No prior post with this slug exists on the board. Let me compose the single comment and post it via the Antonina CLI.

## Output 511 (msg_208fceec0001HscEFtIKk1wBf4)

The post succeeded. Let me verify it appears on the board exactly once with the correct author.

## Output 531 (msg_208fd1a2d001JQ4ktzEqmxtnXD)

Done. Here is the final report.

## Finding: Lemma D is **FALSE** at n=7 — explicit counterexample found, verified, and posted

**Decision.** The commissioned question is settled: there exist two posets on 7 labeled elements with equal `e`, equal one-step child-e multiset `M1`, but different minimax value `F`. This refutes the extension-count-only selector in the general (all-states) sense at n=7 and reopens the barrier that the n=6 result appeared to close.

### The counterexample
Successor rows (bit j of row i = i<j, transitively closed):

- **P (F=5):** `[0x3e, 0x0c, 0x00, 0x00, 0x04, 0x08, 0x3e]`
  relations: 0<1,2,3,4,5; 1<2,3; 4<2; 5<3; 6<1,2,3,4,5
- **Q (F=6):** `[0x3e, 0x0c, 0x00, 0x00, 0x0c, 0x04, 0x1e]`
  relations: 0<1,2,3,4,5; 1<2,3; 4<2,3; 5<2; 6<1,2,3,4

Both: `e = 32`, `M1 = (4,4,14,14,16,16,16,16,16,16,18,18,28,28)` (14 entries = 2×7 incomparable pairs). `F(P)=5`, `F(Q)=6`.

**Two independent implementations agree:** e via subset-DP and brute-force count over all 7! permutations (both 32); F via C++ transitive-closure memoized minimax and Python world-set minimax over frozensets of the 32 linear extensions (both 5 and 6). Transitivity checked directly.

### Exhaustive n=7 computation
- 6,129,859 labeled posets (= A001035(7)); S(7)=13; e(A₇)=5040.
- 914 distinct `(e,M1)` keys (913 non-total + 1 total-order key). My n=6 run reproduces the known baseline exactly (130,023 states, 155 keys = 154+1, 0 conflicts).
- **Exactly 1 key mixes F values** — the one above, F∈{5,6}, with 5,040 F=5 posets conflicting against the first-seen F=6 representative.

### Bonus — optimal-play reachability
The k-safe BFS from A₇ within budget 13 visits 3,044,007 states (matching the independent 14:17Z e-greedy computation). 2,520 reachable states carry the conflicting signature, but all have F=5: since e=32 forces depth d≥8 and viability d+F≤13 forces F≤5, the F=6 mate is unreachable. So Lemma D **restricted to optimal-play states** is not refuted at n=7 — the ambiguity is between reachable states and an unreachable one.

### Scope / side effects
No theorem completion for S(n)/SORT-BOUND-U; no complexity-class consequence; no repo/Lean/test/CI/ledger/canonical-main change. Worktree clean at `6a96398`; scratch only under `/tmp/opencode`. Recovery audit found no prior post with this slug. **Exactly one** #301 comment was posted (author `SoringP1 frontier: lemmaD-cospectral-n7-20261123`, 2026-11-23T15:18:36Z) — confirmed as the only external write.
