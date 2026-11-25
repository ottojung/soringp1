# antonina-cQWk21s62TGXMxSfwqNzAj-reckoned

Session: ses_e40bff7ddffe92Pd4STL7459jJ
Workspace: /home/lubko/soring-fronts/curator
Created: 1794210007084; updated: 1794211712573

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1bf40085e001J9wmTQ6WSVex3J)

I'll start by studying the repository docs and board state on billy-dev.

## Output 225 (msg_1bf45cf55001pfR55WLe3DH4Zl)

I've reviewed the docs, the 422-entry ledger, and board #301. Before proposing anything, let me test a structural claim that is absent from the ledger: lattice (sub/super)modularity of the exact minimax value `F`.

## Output 304 (msg_1bf4a2e5f001htDvveItShcubr)

A fresh angle is emerging: the *maximum number of permutations a height-b tree can actually sort* (a capacity/coverage function), which is dual to `F`. Let me compute it exactly for small `n`.

## Output 356 (msg_1bf4c2548001OpfDKGHqKSyiSN)

I found a model error in my own coverage recurrence: a leaf at budget 0 can still output one consistent permutation, so `m_0(P)=1`, not `0`. Let me correct and recompute.

## Output 449 (msg_1bf506d2e001z6rgk6jwW1AO5G)

The depth-spread front already proved `s(7)=2`, which blocks the *extendable* variant. But the raw full-tree capacity question is different. Let me test `h(A_7) >= 12` directly.

## Output 467 (msg_1bf50de96001onoTF1K6rdTyTH)

`h(A_7) ≤ 11 < floor(log2 7!) = 12` — a concrete counterexample to the natural capacity-saturation claim. Let me confirm the exact value and check smaller depths.

## Output 512 (msg_1bf575bcf001hxfgujcwMLYOOf)

I have a concrete, checkable disproof of a natural all-n capacity-saturation claim. Let me verify the board-posting interface and then record it.

## Output 593 (msg_1bf58cd9b001z7V9cO11ybcZyH)

Done on `billy-dev`. Here is what I did and what I found.

## Investigation

I studied `AGENTS.md`, `docs/problem.md`, the 422-entry frontier ledger, and the current board #301 (through 2026-11-09), then attacked a natural all-`n` claim that is **not** in the ledger:

> For every finite poset `P` and every `b` with `2^b < e(P)`, a height-`b` comparison tree can sort exactly `2^b` linear extensions ("capacity saturation below the information bound").

I defined the coverage function `m_b(P)` (maximum number of permutations a height-`b` tree correctly sorts) and the full-tree depth `h(n)`, and computed them exactly:
- `m_b(A_n) = 2^b` for every `b < ceil(log2 n!)` for `n <= 6`;
- `h(n) = floor(log2 n!)` for `n <= 6`;
- **counterexample at `n = 7`**: `floor(log2 7!) = 12`, but no full height-12 comparison tree exists from `A_7`. Exact DP gives `h(7) = 11` and `m_12(A_7) = 4048 < 4096 = 2^12`, while `S(7) = 13 = ceil(log2 7!)`.

So the capacity-saturation claim is **false**, and the first failure occurs seven indices before the sorting number itself first exceeds the information bound (`n = 12`). This is distinct from the board's `optimal-tree-depth-spread` result `s(7)=2`, which fixes height `S(n)`; the new obstruction says no full tree of depth `floor(log2 n!)` exists at all.

**Honest limits:** the `n=7` result is a finite exact computation, conditional on the documented recurrence and prune; it is not an all-`n` theorem, not Lean-checked, and makes no complexity-class claim. `h(8)` and the asymptotics remain open.

I posted exactly one board #301 comment for this (`2026-11-09T08:06:48.898Z`, author `SoringP1 curator: partial-sorting-coverage`). No repository or Lean changes were made.

## Curator output

Wrote `/home/lubko/soring-fronts/curator/frontier-candidates.json` with two non-duplicate all-`n` fronts:

1. **`fulltree-capacity-deficit`** — is `d(n) = floor(log2 n!) − h(n)` bounded or unbounded?
2. **`near-optimal-partial-sorting-gap`** — is there an absolute `δ>0` with `m_{S(n)-1}(A_n) ≤ (1−δ)n!`, or can height-`S(n)−1` trees sort a `1−o(1)` fraction?

Both are grounded in the exact coverage computations and explicitly separated from the existing counter, spread, excess, Farkas, and certificate fronts. The JSON validates, all required field lengths are met, and the only new worktree file is the requested `frontier-candidates.json` (untracked, as expected).

## Output 666 (msg_1bf59fa60001qlrLj3T86o7cS2)

Recovery audit complete. No action was repeated.

## Effects confirmed as already done
- **Board #301:** exactly **one** comment exists from this work — `2026-11-09T08:06:48.898Z`, author `SoringP1 curator: partial-sorting-coverage` (4099 chars). A search across pages 1–3 finds **no duplicate**.
- **Deliverable:** `/home/lubko/soring-fronts/curator/frontier-candidates.json` exists, is valid JSON, and contains the two fronts:
  - `fulltree-capacity-deficit`
  - `near-optimal-partial-sorting-gap`
- **No commits:** `HEAD` remains `6a96398`; the reflog shows no activity from this work.
- **No research/repo changes:** `git status` shows only the expected untracked `frontier-candidates.json`. No Lean, docs, tests, or tracked files were modified.

## Uncertain effects
None. The post, the candidate file, and the absence of commits are all directly verified.

## Remaining work
None. The investigation was reported, the counterexample and limits were stated on the board, and the curator JSON is in place. I did not re-post, re-write the file, or touch Git.
