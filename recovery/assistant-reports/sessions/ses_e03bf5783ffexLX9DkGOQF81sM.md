# antonina-yYEg9N3ua0axiu3026AgWR-lorrain

Session: ses_e03bf5783ffexLX9DkGOQF81sM
Workspace: /home/lubko/soring-fronts/space-separation-omega-sn-on-a-alln
Created: 1795233458653; updated: 1795233789739

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 201 (msg_1fc459094001e100r24AoLz1OJ)

## Result of the front `space-separation-omega-sn-on-a-alln`

**Open obstruction, not a proof.** No falsifier was exhibited: no uniform deterministic machine deciding `SORT-BOUND-U` with `o(S(n))` work-tape bits on `A = {1^n#1^{S(n)}}` was found. Likewise, no general `Ω(S(n))` space lower bound for all uniform machines was proved. The question remains open.

### What was established

- On `A`, `N = n+S(n)+1 = Θ(n log n) = Θ(S(n))`. The current best uniform decider, the transcript DFS, uses `O(S(n) log n)` bits on `A`; this is tight **for that algorithm family**.
- The transcript DFS cannot be compressed to `o(S(n))` bits by the obvious routes:
  1. **Outcome-only storage** loses the comparison pair at each level; a fixed canonical “first untried pair” rule still requires remembering which candidates failed, i.e. a cursor of `Ω(log n)` bits per level.
  2. **Recomputing the cursor from the transcript** is circular: it requires deciding the same game at the current state.
  3. **Savitch/divide-and-conquer simulation** of the alternating game stays in polynomial space, not `o(S(n))` bits; obtaining the latter would be a nontrivial space separation.
  4. **General-poset sublinear bounds do not transfer**: `GEN-SORT` dense-matrix DFS uses `O(√N log² N)` bits because its input length is `Ω(n²)` while game depth is `O(√N log N)`. For `SORT-BOUND-U` on `A`, input length and game depth are the same order, so the same method gives only `O(N log N)`.
  5. **Nonuniform `P/log` advice** (`t_L` in `O(log N)` bits) is nonuniform; computing `t_L` uniformly is equivalent to the original threshold problem.

### Soundness vs. completeness / transfer

- An explicit reduced comparison tree is a **sound and complete** certificate for `S(n) ≤ k`, but has `2·n!−1` nodes, exponential in `N`. It does not yield polynomial-space or small-space verification.
- Information-bound and winning-frontier counts are **sound upper witnesses only**; they do not establish completeness or a small-space decision procedure.
- General-poset hardness results (e.g. Hyafil–Rivest, arbitrary tests) do not transfer to the fixed antichain; any such claim must respect the encoding and model restrictions.

### Honest limits

- The transcript-DFS `Ω(S(n) log n)` bound is a barrier for **that machine family**, not a theorem for all uniform machines.
- A general `Ω(S(n))` (or even `Ω(N)`) lower bound would be a significant space separation; it was not obtained and is not claimed.
- No Lean file, test, script, or repository change was made. The investigation was recorded as a concise update on Antonina board #301. Worktree remains clean.
