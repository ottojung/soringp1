# antonina-QJWKbmbL8BD89QuHa3BVot-irritably

Session: ses_e478c98e0ffeJQl6IvrMoSJ6EI
Workspace: /home/lubko/soring-fronts/threshold-predicate-complexity
Created: 1794095933280; updated: 1794097383225

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1b8736a2800188EcNkxsp9fHDf)

I'll start by studying the repository contract, problem definition, and current board state.

## Output 562 (msg_1b885dd2b001OiGXp2SwAeWgCD)

## Result

I found a genuine hardness reduction, not a polynomial-time procedure.

**Theorem (paper proof, randomized reduction).** Let  
`T(b) = F_{b+3} - 1` and `L_fib = {(P,b) : e(P) <= T(b)}`, with `b` encoded in binary or unary. Then `L_fib` is **PP-hard under Las Vegas polynomial-time many-one reductions**. Consequently:

- if `L_fib ∈ P`, then `PP ⊆ ZPP`, hence `PP = NP` and `PH = NP`;
- if `L_fib ∈ BPP`, then `PP = BPP`.

So the Fibonacci extension base cannot be a polynomial-time pruning rule for `SORT-BOUND-U` unless a major collapse occurs.

## Proof idea

The missing ingredient in a naive reduction is the ability to multiply `e(P)` by a prescribed integer `c`. Without it, a binary search over Fibonacci thresholds only gives a factor-`phi` approximation of `e(P)`, which the known FPRAS already provides and which cannot resolve exact equality.

The multiplier is supplied by Kravitz–Sah, *Linear extension numbers of n-element posets*, Order 38 (2021) 49–66, arXiv:1906.06036:

> every positive integer `m` is `e(M)` for a poset `M` of size `O(log m log log m)`.

For prime `m`, their Stern–Brocot/continued-fraction construction gives a poset of size at most the Euclidean quotient sum `s(m,d)`, and their averaging argument shows a constant fraction of `d` have `s(m,d) = O(log m log log m)`. Sampling `d` randomly makes the construction Las Vegas polynomial time.

Given `(P,K)`:

1. Choose `b = O(n log n)` with `T(b) >= K^4`.
2. Use the strict interval  
   `I = [floor(T/(K+1))+1, floor(T/K)]`;  
   every `c ∈ I` satisfies `cK <= T < c(K+1)`.
3. Sample a prime `c ∈ I` (the interval has length `>= K^2/2`; primes exist by standard gap bounds).
4. Construct `M` with `e(M)=c`.
5. Output `Q = P ⊕ M` and `b`, where `⊕` is the ordinal sum.

Then `e(Q) = c e(P)`, and therefore

`e(Q) <= T(b)  ⇔  e(P) <= K`.

The sizes are polynomial: `log c = O(log K) = O(n log n)`, so `|M| = O(n log^2 n)` and `|Q| = O(n log^2 n)`, while `b = O(n log n)`. In particular `b << |Q|` and `b << S(|Q|)`, so this is not an artifact of an unrealistically huge budget: it lies in the reachable-poset, small-budget regime.

The starting point `L_bin = {(P,K): e(P)<=K}` is PP-hard under Turing reductions because binary search on `K` computes `#LE`, and `#LE` is #P-complete (Brightwell–Winkler).

## Soundness vs completeness

- The predicate `e(P) <= T(b)` is **sound as a base case** only if the threshold theorem `T(r)=F_{r+3}-1` holds. The hardness result is about deciding the predicate; it does not assume soundness.
- It is **not complete** even then. For `n=4`, `S(4)=5`, `T(5)=20`, and the antichain `A_4` has `e=24>20` but is sortable in 5. So even a polynomial-time predicate would not decide all sortable states.
- A hard sufficient base does **not** imply `SORT-BOUND-U ∉ P`; the exact search can avoid it. This result rules out the extension-threshold route, not the whole problem.

## Checks and limits

- Brute-force quotient sums for primes `p <= 1009` confirm `min_d s(p,d) <= log p log log p` (e.g. `p=997`, min `s=16`, bound `13.34`).
- Interval arithmetic for `n <= 10` confirms the strict interval is nonempty and `floor(T/c)=K`.
- A toy ordinal-sum check confirms `e(P)=5, e(M)=4 ⇒ e(P⊕M)=20`.

**Honest limits.** The reduction is randomized, not deterministic many-one. The effective Kravitz–Sah step is a deduction from their existence proof; I did not independently implement the full Stern–Brocot poset construction. The paper proof needs an audit of the prime-`d` search and the construction’s exact count. Deterministic PP-hardness of `L_fib` remains open. The result is for the explicit Fibonacci threshold; the same argument works for any `T(b)=exp(Θ(b))`, while for polynomial `T(b)` the predicate is in P by capped enumeration.

I posted this to board #301 (`SoringP1 frontier: fibonacci-threshold-hardness`) and posted a clarification that it does not conflict with the parallel width-two result: counting extensions of bounded-width posets is polynomial, and the reduction’s `Q` inherits the width of the arbitrary input `P`, so the hardness necessarily leaves the width-two class. The worktree remains clean.

## Output 715 (msg_1b88896f5001zWvqUHcAGecBLw)

## Recovery inspection

I checked the conversation, repository, board, and durable task records before doing anything.

**Effects that did happen**

- Two board #301 comments by `SoringP1 frontier: fibonacci-threshold-hardness`:
  - `2026-11-08T00:18:10.984Z` — main hardness finding, 4190 chars;
  - `2026-11-08T00:18:40.427Z` — width-two clarification, 919 chars.
- Both bodies exactly match the local files `/tmp/fib_threshold_board_post.md` and `/tmp/fib_threshold_followup.md`. There are **no duplicate posts**.
- `/tmp/board_post_result.json`, `/tmp/board_post_followup.json`, and the post files remain.

**Effects that did not happen**

- No repository changes: branch `billy-dev`, HEAD `6a96398`, `git status` clean, no extra worktrees or commits.
- No Lean changes, no PRs, no GitHub issue changes.

**Remaining operational state**

- The frontier ledger entry `threshold-predicate-complexity` still has `status: running`, agent `QJWKbmbL8BD89QuHa3BVot-irritably`. That is this agent; it has not exited yet. I did **not** edit the ledger manually. The keeper should record the clearexit/completion when this session ends.
- I did not re-post or re-run the interrupted prompt.

## Research status

The mathematical work is complete as reported earlier: a Las Vegas reduction from the binary-threshold `#LE` language to the Fibonacci threshold predicate, implying `L_fib ∈ P ⇒ PP = ZPP` (and `PP = NP`, `PH = NP`). The key ingredient is the effective Kravitz–Sah concise-extension-count construction. The honest limits remain: the reduction is randomized, the effective Stern–Brocot construction is a deduction from their existence proof and needs an independent audit, and the result does not prove `SORT-BOUND-U ∉ P`.

Two precision notes on the posted write-up, neither affecting the main theorem:

1. The size inequality `b << |Q|` is asymptotic. For very small `n` (e.g. `n=3`) the budget can be slightly larger than the constructed poset size; finite small cases can be handled directly, and the hardness statement is asymptotic.
2. For binary `b`, `L_fib ∈ PP` uses the trivial cutoff: if `T(b) > n!` the answer is always yes; otherwise `b = O(n log n)` and the Fibonacci threshold has polynomially many bits. So the PP membership claim is correct, though not literally “immediate.”
