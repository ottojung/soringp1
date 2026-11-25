# antonina-GEPPaI3rpnMnF9kzgwl3sn-treading

Session: ses_e3c02d3c9ffe2o7qIRiJVieEAi
Workspace: /home/lubko/soring-fronts/single-deletion-eta-characterization
Created: 1794289511702; updated: 1794295834054

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 848 (msg_1c45b65be001IBos6pP2aFBGu3)

I studied the contract, `docs/problem.md`, the board, and the literature baseline, then attacked the front with exact minimax computation. The result is a decisive negative: **the front’s claim is false in both directions.**

## Finding

Let `P = (A_a ⊕ A_b) \ {(a0,b0)}`, with `A_n` the `n`-antichain and `⊕` the ordinal sum.

**Counterexample 1 (min = 2, η = 0).** `a=2, b=3`:
- `e(P) = 2!·3! + 1!·2! = 14`
- `S(2)+S(3) = 1+3 = 4`
- exact minimax `F(P) = 4`, not `5`.

Verified four ways: exhaustive memoized game search; a budget solver (no 3-comparison win, a 4-comparison win exists); an explicit 4-comparison strategy simulated on all 14 linear extensions; and the module decomposition below. `P` is prime.

**Counterexample 2 (min ≥ 3, η = 1).** `a=5, b=5`:
- `e(P) = 5!·5! + 4!·4! = 14976`
- `S(5)+S(5) = 7+7 = 14`
- exact minimax `F(P) = 15`, not `14`.

Computed by an exact module-decomposition game search: the only cross-incomparable pair is `(a0,b0)`, so the state is the pair of antichain restrictions plus one bit. The decomposition was cross-checked against the direct minimax for `(2,3),(2,4),(2,5),(3,3),(3,4),(4,4),(4,5),(3,6)`, and the `(5,5)` value was independently reproduced by a second full-poset implementation (`V=15`). `P` is prime.

**Corrected small values**

| `(a,b)` | `e(P)` | `S(a)+S(b)` | `⌈log₂ e⌉` | `F(P)` | `η` |
|---|---:|---:|---:|---:|---:|
| `(2,2)` | 5 | 2 | 3 | 3 | 1 |
| `(2,3)` | 14 | 4 | 4 | 4 | 0 |
| `(2,4)` | 54 | 6 | 6 | 6 | 0 |
| `(2,5)` | 264 | 8 | 9 | 9 | 1 |
| `(2,6)` | 1560 | 11 | 11 | 11 | 0 |
| `(3,3)` | 40 | 6 | 6 | 6 | 0 |
| `(3,4)` | 156 | 8 | 8 | 8 | 0 |
| `(3,5)` | 768 | 10 | 10 | 10 | 0 |
| `(3,6)` | 4560 | 13 | 13 | 13 | 0 |
| `(4,4)` | 612 | 10 | 10 | 10 | 0 |
| `(4,5)` | 3024 | 12 | 12 | 12 | 0 |
| `(4,6)` | 18000 | 15 | 15 | 15 | 0 |
| `(5,5)` | 14976 | 14 | 14 | 15 | 1 |

The excess `η = F − S(a) − S(b)` is `1` for `(2,2),(2,5),(5,5)` and `0` for the others. The excess `d = F − ⌈log₂ e⌉` is `0` for all these except `(5,5)`, where it is `1`. So the exact value is **not** determined by `min(a,b)`, nor by the maximum of the two lower bounds.

## Soundness vs completeness, and scope

- The lower bounds `F ≥ S(a)+S(b)` and `F ≥ ⌈log₂ e⌉` remain **sound**.
- The front’s proposed **completeness** rule is false: the two lower bounds do not determine `F`.
- These are results about a specific prime poset family, not general-poset hardness. No complexity-class consequence for `S(n)` or `SORT-BOUND-U` follows.
- The `n=27` base ambiguity `F(P₁) ∈ {72,73}` remains open; the exact all-`n` characterization is a new open problem.

## Limits

The `(5,5)` value is an exact game search, not a paper adversary argument. The decomposition’s correctness is supported by cross-checks on smaller cases and a second independent implementation, not a formal proof. I made no repository or Lean changes; the worktree is clean at `6a96398`. A concise report was posted to Antonina issue #301 at 07:27Z.

## Output 910 (msg_1c45d6902001qibJfdViC7bsoC)

**Recovery inspection (no external actions taken)**

- **Conversation/work state:** The prior turn’s checkpoint indicates the `single-deletion-eta-characterization` front was fully investigated and reported (claim refuted by exact counterexamples), with “Next move: none.”
- **Working directory / Git:** `/home/lubko/soring-fronts/single-deletion-eta-characterization` on `billy-dev`, `HEAD 6a96398` (`Merge commit '6859bc2'...`), `git status` clean (no uncommitted changes).
- **Durable scratch records:** `/tmp/opencode/singdel/` present with reported artifacts including `post.md`, `post_result.json`, `post_err.txt`, and computation scripts/logs (e.g. `full.py`, `full_5_5.log`, `decomp.py`, `decomp_5_5.log`, `decomp_4_6.log`, `verify.py`, `values.py`, `mm.py`, `budget.py`).
- **Board (Antonina #301):** `board_digest.py --contains "single-deletion-eta-characterization"` shows the finding comment present once: `2026-11-10T07:27:22.885Z` by `SoringP1 frontier: single-deletion-eta-characterization` (“…proposed all-n claim is FALSE. Two exact counterexamples…”), consistent with the prior post. No repost attempted.
- **Frontier ledger:** `~/.local/state/soringp1/frontier-ledger.json` exists (not modified). I did not update keeper-managed state.

**Determination of external effects**
- **Occurred (confirmed):** 1 Antonina board comment on issue #301 at `2026-11-10T07:27:22.885Z` for `single-deletion-eta-characterization` (present once on board; local post artifacts exist in `/tmp/opencode/singdel/`).
- **Did not occur:** No commits, pushes, PRs, repository/Lean edits, or other external actions observed (`git` clean/same HEAD).

**Unfinished work / actions continued**
- None. All substantive work for this front was already completed and reported; I did not repeat or duplicate the interrupted prompt or any external side effect.

**Uncertainty for review**
- Minor: I did not fully parse the ledger entry structure in this pass beyond confirming the ledger file exists (structure differed from expectation), and I did not re-run/independently re-verify the earlier `(5,5)` exact-search results now; the prior checkpoint already records them as exact game-search evidence with cross-checks and stated limits. If desired, follow-up would be independent verification/paper argument for the `(5,5)`/larger cases or keeper-managed ledger status adjustment (separately).
