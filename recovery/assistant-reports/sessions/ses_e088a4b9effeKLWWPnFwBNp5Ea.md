# antonina-g4yI4FMn1gRuJ6JqlNp7wP-dresses

Session: ses_e088a4b9effeKLWWPnFwBNp5Ea
Workspace: /home/lubko/soring-fronts/greedy-e-index-exception-density-alln
Created: 1795153048750; updated: 1795154423015

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f775b6d9001vftibwe76CoPgP)

I'll start by understanding the repository state and the specific branch I need to work on.

## Output 17 (msg_1f775c323001mdg6yROa1yJPUI)

I'm on `billy-dev`. Let me read the key documents and locate board #301.

## Output 32 (msg_1f775cdd6001KBgr5F6M0Jpb9c)

Let me read the operations doc and search for the #301 board post details.

## Output 47 (msg_1f775d9b1001Epmal91vJ0O0iG)

Let me query the research board digest for the specific post and read related research notes.

## Output 62 (msg_1f775f59a001REhXMNtEeToM9K)

Let me read the full board posts relevant to this front. Let me find the board data file.

## Output 98 (msg_1f7771484001VUYsVz6LJEonvB)

Let me check existing scratch from the prior front and available scripts, then read the literature grounding.

## Output 113 (msg_1f7778081001g0w1a4MKsXeIJA)

Let me check whether this exact front has posted before, and inspect the recent related scratch files (witness families) that may be from concurrent agents.

## Output 133 (msg_1f777dda2001ae24HWTLAYME2h)

Let me read the core greedy game implementation and run the key diagnostic scripts to establish ground truth.

## Output 162 (msg_1f7798871001u1RupYHfDk2Z4k)

I've replicated the front's numbers. Now let me push to n=7 to test growth, and examine the structure of mixed e-values. Let me run both in parallel.

## Output 183 (msg_1f77bc8c9001R6TKwA1VNN1iZK)

Let me ground the literature facts (Fredman, Kahn–Saks) precisely while the n=7 computation runs.

## Output 213 (msg_1f77c2bcc001lovfmGqIcXdaIf)

The n=7 computation is still running. Let me retry the literature search.

## Output 224 (msg_1f77c3cdd001Wt6UiyXMZQ9ZHq)

Let me try fetching reference material directly while the computation runs.

## Output 262 (msg_1f77d2ec1001nLK7h02tm2wB9n)

Key discovery: the ball realizes **every** distinct linear-extension count of all n-element posets (1,2,4,9,23,62). Let me compute the next term in C to determine growth.

## Output 334 (msg_1f77eb5ca001TVY6WKDz2agJYl)

Let me look at the existing quotient solver, which computes all isomorphism classes efficiently — I can extract distinct e-values from it.

## Output 345 (msg_1f77efa4c001yAB63BKPJ7o9jR)

Let me extract distinct e-values over all poset isomorphism classes for n=7,8 using the existing canonicalization machinery.

## Output 365 (msg_1f78007aa001FZJZwOcKmYBfnS)

E(n) = 1,2,4,9,23,62,226,955 — growing fast. Let me test a clean rigorous construction: distinct products of factorials over partitions (giving p(n) distinct e-values via disjoint chains).

## Output 394 (msg_1f780f9ed001XfSqPBMngMkvJK)

Let me verify precisely which e-values appear on the greedy ball vs all posets, to check reachability of the chain-union construction.

## Output 414 (msg_1f781c4f9001ONrfEJ0ht59zPp)

The n=7 full-game computation is too slow. Let me kill it and run a faster deterministic-tie ball computation to test whether the ball still realizes all e-values.

## Output 427 (msg_1f7822780001x5twc55jnhhBOM)

While n=7 runs, let me verify the prime-subset construction and quantify its growth.

## Output 521 (msg_1f783ab880015JTzf02q4cCL4P)

I've found a rigorous route. Let me verify chain-union posets are on the greedy ball and check the n=7 computation.

## Output 559 (msg_1f7853714001xjICFlAAJi8dBt)

I found a bug in my reachability test (non-transitively-closed targets). Let me redo it correctly.

## Output 606 (msg_1f788bbb2001Z8GwsGWiDDHxIS)

I have a rigorous theorem. Let me check the posting mechanism, then verify final details.

## Output 633 (msg_1f7891bcc001BE9micCEZjGU16)

I have a rigorous, independently checkable theorem. Let me compose and post the board update.

## Output 651 (msg_1f789882b0018kmaYeYIRTgEJU)

The post succeeded. Let me verify it appears correctly on the board.

## Output 696 (msg_1f789f789001qkuYtmZ4lqFan9)

I've completed the investigation. Here is the honest result.

## Mathematical finding (all-n theorem, paper proof)

I **disproved the tabular form of the positive horn** of this front. The claim attacked: for every n, a poly-size index keyed by e(P) can return the exact greedy value V(P) for every state on the greedy ball within G(n) comparisons.

**Theorem.** For n ≥ 8, let S range over sets of distinct primes with ∑_{p∈S} p ≤ n. For each S there is a ball state with
e(P_S) = n!/∏_{p∈S} p!,
and these values are pairwise distinct. Hence the ball has **≥ 2^{Ω(√(n/log n))} distinct linear-extension counts**, so any evaluator indexed by e(P) needs superpolynomially many entries for infinitely many n.

Three elementary lemmas:
1. **Reachability.** Any disjoint union of chains is greedy-reachable in ≤ 2n comparisons: build each chain as a star (the "new element above the centre" child has more extensions — verified: fraction (t+1)/(t+2)), then order the twin tops on extension-count ties. Since ceil(log₂ n!) ≥ 2n for n ≥ 8, these fit inside G(n).
2. **Exact value.** Padding chains of prime length with a free antichain of size r cancels the r!: e = n!/∏ p!. Verified for n = 6,7,8,10,12.
3. **Injectivity.** For q = max(S∪T), the q-adic valuation of ∏_{p∈S}p! is 1 iff q ∈ S. So distinct prime sets give distinct e-values (0 collisions in 4096 subsets).

Counting: the t smallest primes sum to ≤ t²(log t + log log t), so t = Θ(√(n/log n)) and all 2^t subsets qualify. Measured prime-subset counts: 4687 (n=100), 159061 (n=200), 1.38·10⁸ (n=500) — superpolynomial.

Verified computationally: all chain-union posets are in the all-ties ball for n ≤ 6; ball e-values equal all-poset e-values (1,2,4,9,23,62 for n = 1..6; 226 and 955 at n = 7,8 over isomorphism classes).

## Falsification attempts I actually ran
- An apparent counterexample to reachability was a **bug** (non-transitively-closed targets); with transitive closure all chain-union states are reachable.
- Searched for colliding prime products (none found); tried to make the growth merely polynomial (log(count)/log(n) increases: 1.84 → 2.26 → 3.02).
- Confirmed the prior matching-gadget route is unusable and not needed here.

## Honest limits
- This kills the **tabular e-index** (one entry per e-key) — the example form in the front. It does **not** rule out a closed-form evaluator plus a sparse exception list; that needs an exception-density theorem, which is the remaining decisive obstacle. Mixed e-values are only measured (0,0,0,1,8 for n = 2..6); the n=7 exception computation did not finish.
- V ∈ {⌈log₂ e⌉, ⌈log₂ e⌉+1} is verified only for n ≤ 6; no all-n claim. No G(n)=S(n) claim, no SORT-BOUND-U separation, no general-poset hardness, no Lean changes.

## Delivery
Posted to Antonina issue #301 at 05:59:03Z. Worktree on `billy-dev` is clean — no repository, Lean, or ledger changes.

## Output 721 (msg_1f78a7858001MNy0L7bFIZZDkT)

**Recovery check (no repeated side effects):**
- **Conversation / prior work:** I completed the `greedy-e-index-exception-density-alln` investigation in the previous turn (scratch computations under `/tmp/opencode`, including background runs now stopped) and reported results.
- **Git state:** `/home/lubko/soring-fronts/greedy-e-index-exception-density-alln` is clean on `billy-dev...origin/billy-dev`, HEAD `6a96398` (no new commits, no staged/unstaged changes).
- **Durable external record:** Antonina board #301 already contains the post by `SoringP1 frontier: greedy-e-index-exception-density-alln` at **2026-11-20T05:59:03.442Z** (verified via `board_digest.py --contains "greedy-e-index-exception-density-alln"` on page 1). No duplicate post was made.
- **Other external actions:** none performed (no pushes/PRs, no Lean/repo changes, no purchases, no ledger/main edits).

**Conclusion:** All intended effects already happened; there is no unfinished external work to continue. I did not and will not re-post, commit, or repeat any external action.

**Result already delivered (summary):** Disproved the **tabular e-index** positive horn (all-n). For n ≥ 8, disjoint unions of chains of prime lengths plus an antichain pad are greedy-ball reachable within G(n) with `e(P_S)=n!/∏_{p∈S} p!`, pairwise distinct by a largest-prime valuation argument, yielding `≥ 2^{Ω(√(n/log n))}` distinct e-values — superpolynomial, so a table keyed by e(P) cannot be poly-size. This does **not** rule out a closed-form evaluator with a sparse exception list (decisive remaining obstacle); mixed/exception counts only measured for small n, no `G(n)=S(n)`/class-separation/Lean claim. Uncertainty: the interrupted n=7 exception-count run produced no durable mixed-count data, but it had no external side effects.
