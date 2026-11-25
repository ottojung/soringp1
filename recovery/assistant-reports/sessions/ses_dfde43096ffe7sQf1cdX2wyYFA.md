# antonina-XEodjvpgTdo5n7Kd0uW0yG-chaos

Session: ses_dfde43096ffe7sQf1cdX2wyYFA
Workspace: /home/lubko/soring-fronts/sparse-optimal-comparison-graph-alln
Created: 1795331706818; updated: 1795332517493

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 13 (msg_202233ff9001GTckp6Ln857dOV)

I'll start by orienting myself carefully — checking git state, working directory contents, and durable records before doing anything that could repeat side effects.

## Output 28 (msg_20223545f001dhhAGDBg2Dri3F)

I'm on `billy-dev` with a clean tree. Now let me read the key documents and discover how the research board is accessed.

## Output 51 (msg_202236472001oWY4eXqz9O7lof)

Now let me check the durable task records (frontier ledger) and the research board digest to see what's already happened — this is the key "resume safely" step.

## Output 66 (msg_202237b33001iNjWW0FOnHScvb)

Let me search the board and ledger specifically for this front (sparse comparison graph / distinct pairs / restricted edges) and check for any interrupted-turn artifacts.

## Output 81 (msg_20223a7b6001ZtdgetBW5kL8dh)

A front `sparse-optimal-comparison-graph-alln` is already `running` with no finding. Let me inspect its ledger entry in detail, check for scratch artifacts from an interrupted turn, and search the board for any post from this front.

## Output 96 (msg_20223cd50001nUFts788uPjWPS)

Let me pin down the front's start time and check for any scratch files created around then (signatures of an interrupted turn).

## Output 107 (msg_20223e311001dBG58R75nEfy6l)

Recovery audit is clean: the front started at 07:15Z, there are no scratch files from it, no board post matching it, no ledger finding, and the worktree is clean at `6a96398`. No prior side effects to duplicate. I'll proceed fresh. Let me study the literature and the available solver scripts in parallel.

## Output 126 (msg_202250d12001bWEEGXUqtHNmZ3)

Web search was cancelled (transient). Let me retry once, and meanwhile write a scratch solver to compute g(n) exactly for small n — this directly discriminates the two hypotheses.

## Output 153 (msg_202257f8a001lGyhA16gOHsVJF)

A decisive structural fact is emerging. Let me verify it computationally (n=6 with one pair forbidden) and check whether the board already contains this observation (to avoid duplicating a known finding).

## Output 168 (msg_2022611f8001k3TFIBmnS2rGQ0)

The theorem is confirmed computationally for n≤6. Let me make one attempt to reach the literature (websearch is being cancelled; try direct fetch), then I'll write up the finding.

## Output 206 (msg_20226c705001CoEP47f7X3cafm)

I have a decisive result. Let me check the exact board-posting mechanism before making my single external write.

## Output 233 (msg_202271b7e001PKwX85ef2xpjTu)

I have a decisive, fully checked result. Let me write the board post to a scratch file and make my single external write to Antonina issue #301.

## Output 251 (msg_202279064001XNvvGYmm10Hvbr)

Let me verify the comment actually landed (exactly once) via the board digest.

## Output 262 (msg_20227a9ab001AyI8h1jHI4uJ6C)

Done. Here is the honest outcome.

## Recovery audit (before any action)
- On `billy-dev`, clean worktree at `6a96398`; ledger front `sparse-optimal-comparison-graph-alln` was `running` with `finding=None`, started 07:15:06Z.
- No board post, commit, ledger update, or scratch file from this front existed (board searches for the front id, "distinct-pair", "comparison graph", "sparsification" all returned 0). The backend failure therefore left **no side effects to duplicate**.

## Mathematical finding — the sparse horn is falsified, by a stronger all-n theorem

**Theorem.** For every `n ≥ 2` and **every** correct comparison sorting tree `T` (optimality is *not* needed), the set of pairs `T` compares on at least one root-to-leaf path is the **complete graph** `K_n`. Hence

`g(n) = C(n,2) = Θ(n²)` for all `n ≥ 2`, and `S_G(n) = S(n)` iff `G = K_n`; if `G` omits even one pair, no correct tree exists at all (`S_G(n) = ∞`).

**Proof (self-contained).** Fix keys `a,b` and an input where `a` is immediately before `b` in sorted order; let `L` be its leaf. The inputs reaching `L` are exactly the linear extensions of the poset `P` = transitive closure of the path's comparisons. Correctness forces `P` to be a total order. If `a,b` were never compared on that path, then `a <_P b` must be derived by transitivity through a chain `a = z₀ < z₁ < … < z_t = b` with `t ≥ 2`, giving `a < z₁ < b` — contradicting adjacency. Equivalently (exchange form): swap `a,b` in the input; since no third key lies between them and they are never compared with each other, every comparison outcome is unchanged, so the tree outputs the same order on both inputs and fails on one.

**Independent check.** Exhaustive minimax over edge subsets: `g(2)=1, g(3)=3, g(4)=6, g(5)=10`; forbidding one pair makes sorting impossible at `n=4,5,6`.

## Required distinctions (addressed explicitly)
- **General posets don't transfer.** For a starting poset `Q`, the same proof forces exactly the pairs that can be consecutive in *some* linear extension of `Q`. At the antichain root every pair qualifies (hence `K_n`); from a chain, none do. This is a statement about the antichain root of `S(n)`, not a general-poset hardness result.
- **Soundness ≠ completeness.** Checking consecutive pairs of a *claimed* order (n−1 comparisons) is a cheap verification certificate that presupposes the answer; it does not produce a tree that *discovers* the order. Framed-DAG/succinct certificates therefore say nothing about the tree's global edge set.
- **Complexity implication.** The proposed exponent-shrinking route (cut root branching from Θ(n²) to O(n log n) allowed pairs) is **dead**: no sparse allowed-pair set can sort at all. This rules out exactly that route; it yields no new bound for `S(n)` and does not affect symmetry-quotient, compression, or certificate approaches.

## Honest limits
- The theorem is elementary and classical (standard exercise; exchange argument appears in StackOverflow Q251068); I claim **no novelty and no new complexity theorem** for `S(n)` or `SORT-BOUND-U`. The front's dense horn is true but degenerate: the stronger statement holds for *every* correct tree, not just optimal ones.
- Serious falsification attempts: merge-insertion graph (binary-insertion pivots cover the whole chain over all inputs ⇒ dense), general-poset reductions (no bridge back to `S(n)`), and direct refutation of the theorem (blocked by adjacency). `websearch` was repeatedly cancelled; I used `docs/literature.md` plus a direct fetch of the comparison-sort model/value table.

**External writes:** exactly one board comment on Antonina #301 at 07:28Z (verified: 1 unique match). No Lean, repository, ledger, test, or CI changes; worktree remains clean.

## Output 274 (msg_20227d079001zaXT1wDxA3NR1D)

Understood. I will not repeat the post. Let me re-inspect the actual state to confirm what happened in the previous turn and whether anything remains unfinished.

## Output 289 (msg_20227fd02001qBqq5OqBhBudHK)

Confirmed. Let me do one final check for any newer board instruction directed at this front that would constitute unfinished work.

## Output 300 (msg_20228139a001xjPB2tsFd1Kwa7)

## Inspection result: work already complete — no action taken this turn

**Effects that actually happened in the previous turn (verified, not assumed):**
- **Exactly one external write:** a board comment on Antonina #301 at `2026-11-22T07:28:01.784Z`, authored `SoringP1 researcher: sparse-optimal-comparison-graph-alln`. The query for that front id returns **1 unique match** — no duplicate.
- **Scratch only:** `/tmp/opencode/sparse_g.py`, `sparse_post.md`, `sparse_post_result.json` (plus empty stderr).
- **No other side effects:** git tree clean on `billy-dev` at `6a96398` (HEAD unchanged, no commits, no repo/Lean/test/CI changes). Ledger front `sparse-optimal-comparison-graph-alln` remains `running` with `finding=None` — untouched, as with the other fronts' reports.

**Unfinished work:** none. The previous turn completed the research task: it proved the decisive all-n theorem (every correct comparison tree compares all `C(n,2)` pairs, so `g(n)=Θ(n²)` and the sparse-allowed-pair route is impossible), ran the exhaustive small-n falsification checks, and posted the result with honest limits. The newest board message is that very post; there is no follow-up request directed at this front.

I have therefore **not** re-posted, not touched the ledger, and not created any commit or repository change. Nothing is uncertain enough to require review. If you want the ledger front flipped to `investigated`, that is a deliberate new action — say so and I will do it once.
