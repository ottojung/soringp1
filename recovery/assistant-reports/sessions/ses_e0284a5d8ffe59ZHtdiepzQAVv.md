# antonina-TE23jznd8xFwnPnrnYjCqp-defined

Session: ses_e0284a5d8ffe59ZHtdiepzQAVv
Workspace: /home/lubko/soring-fronts/defect-chain-extremality-alln
Created: 1795254082171; updated: 1795256474339

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1fd7b5c2f001YQauri0lmwyQ16)

I'll start by investigating the repository state, the key documents, and what "billy-dev" refers to.

## Output 17 (msg_1fd7b6c06001YuM2vhwD5JkuC7)

We're on `billy-dev`, clean working tree. Let me read the key documents and find the research board.

## Output 87 (msg_1fd7bf7a30013f1LBA4UN1xiOM)

Let me check the frontier ledger entry for this front, and look for any earlier work from a failed predecessor.

## Output 107 (msg_1fd7c16e2001gMXz3gHq45u6u1)

There's evidence of a predecessor working on this exact front (`extremal_probe*.py`, ~09:34Z). Let me inspect that earlier work carefully to avoid repeating it.

## Output 118 (msg_1fd7c23c50010fNznUv32HZ7pb)

I found a predecessor's scratch work on this exact front (`extremal_probe*.py`). Let me examine the evaluator they used, the repo's relevant notes, and search the primary literature in parallel.

## Output 138 (msg_1fd7d3962001pa67wamk8tN3lL)

I now understand the state well. A predecessor enumerated the extremal question for b≤5, a≤2 but didn't finish or post. Let me study the primary literature and build an independent verification in parallel.

## Output 167 (msg_1fd7e1de6001Q08U1pE7OEvywL)

The primary-source framing is clear (Ford–Johnson 1959, Knuth TAOCP §5.3.1, Hwang–Lin merge bounds). Let me now run a rigorous computational verification with the exact minimax evaluator, extending the predecessor's range and checking my two paper theorems.

## Output 201 (msg_1fd862539001ZlmTh4BDr5OM23)

No external side effects occurred (worktree clean, only a scratch file written). The killed run died on the S(7) evaluator (5040 automorphisms), not the theory. Let me first check whether this chain-extremality fact is already recorded in the project, then rerun a lean verification.

## Output 212 (msg_1fd86bf7f001d1LDOt6o7VkEpy)

The ledger confirms `defect-chain-extremality-alln` is the live `running` front, and the predecessor's enumeration matches my hypothesis. I have two clean paper theorems in mind. Let me verify them with a lean, unbuffered run.

## Output 255 (msg_1fd9702d9001hHj3j0mmdO9mfm)

Good — the killed run still produced valid output: the independent naive minimax matches, and **all** T2 checks pass (including strict gaps at a≥3). The harness cut it at ~265s during T2. Let me run only the fast exhaustive T1 check, reusing memoized evaluators.

## Output 291 (msg_1fd9e250c001sDWljfEwgTaq3c)

The exhaustive check confirms T1 for all labeled posets b≤4 (a≤2/3) and b=5 (a=1); T2 held across all tested (a,b). Now let me verify no board post exists for this front tag, then post the finding once.

## Output 311 (msg_1fd9ebe01001HqJB9ucEsPp4Fq)

Viche's two new posts explicitly leave this front to me. Let me check the comment command syntax and post the finding once.

## Output 322 (msg_1fd9ed716001HZPgac55nL6mtC)

No post exists for this front. Let me post the finding to board #301 exactly once, redirecting the JSON output to a file as the operations doc requires.

## Output 340 (msg_1fd9f678f001bJTs9nSffR0hEU)

The post returned success. Let me verify it appears exactly once on the board.

## Output 360 (msg_1fd9fa0f6001kLh6sc0ZISui49)

## Result

I attacked the live front `defect-chain-extremality-alln` on `billy-dev`, resumed the predecessor's unfinished scratch work, and **refuted the falsifier by proof rather than by finding a counterexample**. No repository/Lean/test/CI changes were made; the worktree is clean at `6a96398`. One board post was made to #301 (10:20:34Z) and verified to appear exactly once.

### Mathematical finding (two all‑n theorems, paper proofs)

Let `F(P)` be the exact adaptive minimax comparisons to identify an unknown linear extension, `S(a)=F(A_a)`, `δ(A_a,B)=F(B⊔A_a)−F(B)−S(a)`, `C_b` the b‑chain (`F=0`, information‑tight), `Z_b` the max‑excess staircase.

**T1 — chain extremality.** For all `a,b≥1` and every b‑element poset `B`:
```
δ(A_a,B) ≤ δ(A_a,C_b).
```
*Proof:* the strategy "sort B optimally (`F(B)` comparisons), then insert A into the resulting chain (`F(C_b⊔A_a)` comparisons)" is a valid decision tree for `B⊔A_a`, so `F(B⊔A_a) ≤ F(B)+F(C_b⊔A_a)`; subtract `F(B)+S(a)` and use `F(C_b)=0`. Hence
```
max_{|B|=b} δ(A_a,B) = δ(A_a,C_b) = F(C_b⊔A_a) − S(a),
```
attained at the information‑tight chain; `Z_b` is one of the dominated hosts. The first falsifier option (`δ(A_a,B)>δ(A_a,C_b)`) is impossible.

**T2 — merge‑insertion growth.** `F(C_b⊔A_a) ≤ Σ_{i=1}^a ⌈log₂(b+i)⌉` by binary insertion of the a free keys into the b‑chain, so `max_B δ ≤ Σ⌈log₂(b+i)⌉ − S(a) = O(a log b)` for fixed `a`. The information bound `log₂ e(C_b⊔A_a)=Σ log₂(b+i)` gives `max_B δ ≥ Σ log₂(b+i) − S(a) = Θ(a log b)`. The second falsifier option (super‑insertion growth) is impossible. The bound is strict below the insertion sum when `S(a)>0` (e.g. `(3,7): 7<8`, `(4,2): 4<5`).

### Independent checks
- A from‑scratch naive minimax (no canonicalization) reproduces `S(1..5)=0,0,1,3,5,7` and agrees with the canonical evaluator.
- Exhaustive over **all** labeled b‑posets for `(1,2),(2,2),(1,3),(2,3),(3,3),(1,4),(2,4)` and `(1,5)` (4231 posets): the maximum always equals the chain value, with `Z_b` strictly below when `a≥2` or `b≥4`.
- Exact `δ(A_a,C_b)` for `a≤3,b≤7` and `a=4,b≤3` satisfies both T2 bounds throughout.

### Honest limits
- These are sound structural laws about the minimax game, **not** completeness results. The R‑table sufficient condition still fails for fixed‑a/large‑b (board 08:02Z/08:05Z); sound extremality is compatible with that method's incompleteness.
- General‑poset statements; the bridge to `S(n)` is the superadditivity recursion, not a new evaluator. No complexity‑class consequence: `SORT-BOUND-U ∈ P/NP` untouched.
- No closed form for `F(C_b⊔A_a)`; `Θ(a log b)` only up to constants; the exhaustive `(2,5)` case did not finish within the harness cap (covered analytically). `S(n)` and `SORT-BOUND-U` remain OPEN.

Consistent with Viche's independently verified bracket `⌈log₂(b+1)⌉−1 ≤ δ(A_1,Z_b) ≤ ⌈log₂(b+1)⌉` (09:43Z): T1 shows `δ(A_1,C_b)=⌈log₂(b+1)⌉` is the exact maximum, so the staircase sits within one comparison of the extremal value.
