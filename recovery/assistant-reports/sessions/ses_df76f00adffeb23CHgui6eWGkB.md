# antonina-49LbKREpjKqFGTD8U5Z8sv-learning

Session: ses_df76f00adffeb23CHgui6eWGkB
Workspace: /home/lubko/soring-fronts/constant-alternation-ph-placement-alln
Created: 1795440050093; updated: 1795440466595

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_2089107bb0011DaHfrLRRCGsxc)

I'll start by understanding the repository state, the relevant documents, and what "billy-dev" refers to.

## Output 17 (msg_208911922001f02ygeHAwBKGKL)

Let me use the direct tools available.

## Output 28 (msg_20891291900185AZiwlMfYQjp1)

We're on `billy-dev` with a clean tree. Now let me read the key documents and find board #301 and the certificates/barriers material.

## Output 111 (msg_20891c57e001UVafnhijhw4eF7)

Let me look at related board entries, the ledger entry, and search the literature on tally languages and PH.

## Output 158 (msg_208939560001y1q4E2zCl4YwxK)

Let me examine the board tooling and the remaining relevant docs before finalizing my analysis.

## Output 214 (msg_2089573e6001vjrLgA9qqyOmG0)

No prior post for this front. Let me write up the finding and post it once to board #301.

## Output 243 (msg_20895ef8e0016l8VpFMMLa5zaw)

## Report: constant-alternation / PH placement front (`billy-dev`, worktree clean at `6a96398`)

**Verdict up front.** The question — is `SORT-BOUND-U` in a fixed level of PH, i.e. can the Θ(N)-alternation game `G(n,k)` be replaced by an O(1)-alternation procedure for all n — is **open**. I neither found an O(1) characterization nor proved non-membership. I posted one rigorous partial result and two no-go observations to board **#301** (single write, confirmed). No repository, Lean, test, CI or ledger changes.

### What I attacked
Claim PH-U: ∃ constant i with `SORT-BOUND-U ∈ Σᵢᵖ ∪ Πᵢᵖ`. I tried to prove it (construct O(1) alternations) and to refute it (collapse/no-go), keeping general-poset hardness and certificate *soundness* separate from *completeness*, as required.

### Genuine new theorem — a tight alternation bound for game-style procedures `[deduction]`
Fix a polynomial bound `p(N) ≤ Nᶜ`. A **p-explicit-block** procedure is an ATM that, in each round, existentially guesses a *full explicit decision subtree* `Wⱼ` of depth `bⱼ` (nodes = incomparable pairs, `|Wⱼ| ≤ p(N)`) and universally guesses a path through it, simulating `bⱼ` comparisons; it accepts when the poset becomes total. This is exactly "simulate `G` but let the sorter commit to an explicit adaptive block before adversary answers," and contains the canonical game (`bⱼ=1`).

**Theorem.** Any such procedure deciding `SORT-BOUND-U` on all inputs needs
`t ≥ ⌈log₂ n!⌉/(c·log₂ N) = Ω(N/log N)` round pairs on informative inputs. So for every constant i, large unary inputs force more than i alternations *in this family*.

*Proof.* Each subtree has `2^{bⱼ+1}−1` nodes, so `bⱼ ≤ c·log₂ N`. The transcript is determined by the universal path bits (each `Wⱼ` is a function of prior bits), giving at most `2^{Σbⱼ}` transcripts. Correctness forces distinct permutations to distinct transcripts, so `n! ≤ 2^{Σbⱼ}`, hence `Σbⱼ ≥ ⌈log₂ n!⌉`. Since `log₂ n! = Θ(N)` and `log₂ N = Θ(log n)`, we get `t = Ω(N/log N)`. ∎

Matching upper bound: batching `⌊c log₂ N⌋` comparisons per round via explicit subtree guesses gives an ATM with `O(N/log N)` alternations in polynomial time — so game-style alternation complexity is **Θ(N/log N)**. The naive Θ(N) is improvable but never reaches O(1). This is the concrete "limits of local alternating certificates" result, and it is the one item that is a proof, not an obstacle.

### Constructive route: where O(1) fails `[deduction]`
The natural Σ₂ scheme — guess a poly-size circuit mapping posets to the next pair, universally guess k adversary answers, simulate — is **sound but not known complete**: completeness would require a poly-size circuit computing an *optimal* sorter. Ford–Johnson is poly-size but eventually suboptimal (Sergeev), and optimal strategies for n ≤ 22 come from exhaustive search. The n=12 case (`S(12)=30>29`) refutes the simpler "defect-zero" local certificate family. This is precisely the repo's documented soundness/completeness gap; no completeness theorem exists.

### Why the suggested collapse-based falsifier is not viable `[deduction]`
- Unconditional `SORT-BOUND-U ∉ PH` would imply `PSPACE ≠ PH` (language is in PSPACE by Claim A) — a major open separation; and `PSPACE = PH` itself collapses PH to a finite level (a PSPACE-complete set would lie in some Σᵢ, closed under many-one reductions).
- A conditional "∈ PH ⇒ collapse" needs PH-level hardness; sparsity blocks NP-hardness (Berman/Mahaney ⇒ P=NP) and higher sparse completeness already yields collapses (Ogiwara–Watanabe). No such hardness is established.
- General-poset hardness (Hyafil–Rivest, Laber–Nogueira) and network verification (Parberry) do not transfer to the fixed antichain-root adaptive game.

**Honest limits:** PH-U stands open. The proof covers only explicitly represented local strategies; a succinct circuit strategy escapes the Θ(N/log N) bound, and ruling that out is PH-separation territory. Process here produced one checkable theorem about the *game formulation* and a precise map of the obstruction — not a theorem about the language's PH membership.

## Output 254 (msg_2089627c7001t0IGuNB4JGiRgz)

I'll audit the actual persisted state before doing anything else. No new posts, commits, or writes during this check.

## Output 319 (msg_208973a5400196ryLCWIpBihTH)

## Recovery audit — no new external actions taken

I inspected state only; I did **not** post, commit, push, or modify any record.

**What actually persisted from the previous turn:**

| Effect | Status | Evidence |
|---|---|---|
| Board #301 post | **Happened exactly once**, full body intact | Digest shows 1 match, author `SoringP1 frontier: constant-alternation-ph-placement-alln`, timestamp `2026-11-23T13:26:01.342Z`; the closing phrase of the intended body is present; pages 1–3 contain no second copy |
| Git / commits / branches | **No change** | `git status` clean, HEAD still `6a96398`, reflog shows only the original clone, only `billy-dev` |
| Repo / Lean / tests / CI | **No change** | No files written outside `/tmp/opencode` (`ph_placement_report.txt`, post result/err logs) |
| Ledger | **Unchanged** | Entry `constant-alternation-ph-placement-alln` still `status: running`, `result: null`, `finished_at: null` |

**Backend failure impact:** none observable. The single post persisted in full and the board is currently readable. No duplication risk remains — I will not re-post.

**Unfinished work:** none on my side. The mathematical report was delivered and the sole intended side effect (one #301 post) is confirmed. The "no repository/Lean/test/CI/ledger change" claim in that post is accurate.

**Flagged for review, not guessed at:** the ledger entry for this front is still `running` even though the research turn completed. I left it alone deliberately: (a) my earlier report explicitly declared no ledger change, (b) the keeper owns `running → investigated/blocked` transitions on process exit, and (c) across all 717 ledger entries **none** has a populated `result` field, while 680 are `investigated` and 3 other fronts from the same batch (started within ~2 s of ours) are also still `running`. So `running` with null result is consistent with current convention, not evidence of a lost effect. If the operator expects an explicit `investigated` transition for this front, that is a judgment call for the keeper/operator rather than something I should write into the ledger during recovery.
