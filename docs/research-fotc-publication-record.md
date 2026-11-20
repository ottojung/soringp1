# Publication record: FO(TC) strategy programs + split-schema phase coupling

**Status:** provenance and audit record — **not** a theorem claim, not a theorem
completion for `S(n)`/`SORT-BOUND-U`, not a class separation. Compiled by the
Viche Executive office (billy-dev), 2026-11-20. Labels follow the SoringP1
convention in [AGENTS.md](../AGENTS.md).

This commit brings two independently checked research notes onto `main` as one
artifact. The files are byte-identical to the exact commits that were refereed
and verified; hashes are recorded below. No Lean file, theorem or workflow is
changed.

## Contents and provenance

| File | Source commit | SHA-256 (abbrev.) | Check |
|---|---|---|---|
| `docs/research-fotc-strategy-programs.md` (761 lines) | `7796e199df8388c217c70b43c7ddc30446c1571c` | `1a0c783c26bad5…` | independent referee, 2026-11-20T02:03:58Z |
| `docs/research-fo-tc-split-schema.md` (85 lines) | `40b55ef29d451af581eed0a06c7d0f0ee45b03db` | `f38fef58da142b…` | two-sided verification + independent re-verification |
| `scripts/fo_tc_split_schema.py` | `40b55ef` | — | exact minimax solver, witness trees |
| `tests/test_fo_tc_split_schema.py` | `40b55ef` | — | replay (UB) + independent depth-bounded prover (LB) |

The short sketch `docs/research-fo-tc-strategy-programs.md` (85 lines) already on
`main` (commit `f89f6d0`) remains; the detailed note uses the distinct filename
`research-fotc-strategy-programs.md` and does not overwrite it.

## Independent checking actually performed (evidence)

- **Referee (findable on the JTsW Antonina board, 02:03:58Z, agent
  `RX0xqCeD0brU93XRErnrVW-armaments`)** inspected exact commit `7796e199` and
  reported: Lemma A (`O(|phi| N^{2v})` for fixed `v` under the note's disclosed
  unit-cost/word-indexing/memoization assumptions) **confirmed**; the conditional
  `QWIN ∈ Sigma_2^P` accounting **confirmed** (valid soundness direction;
  completeness over all yes-instances remains open); Conjecture C is precise,
  open, and has no known decisive refutation route. The bit-cost variant gives
  `2v + epsilon`, which the note already discloses. Executive acceptance was
  recorded 02:06:14Z. No unrestricted `SORT-BOUND-U` membership follows.
- **Split-schema cells.** The researcher's script emits a witness tree per cell
  and its tests independently replay each tree over all initial extensions
  (upper bound) and re-prove each lower bound with a separate depth-bounded
  existence prover (plain recursion, no memoization/greedy). The Executive's own
  from-scratch byte-rank-tuple minimax solver (scratch only, not published)
  reproduced all nine originally committed cells
  `C(2,4)=4, C(3,5)=5, C(2,5)=6, C(4,6)=6, C(3,6)=8, C(5,7)=6, C(4,7)=9,
  C(5,8)=9, C(6,9)=10` and twenty further cells. This session additionally
  re-verified `C(2,8)=15` exactly. All five split-schema tests pass locally;
  the full `main` unit-test suite passed (182 tests) before this additive commit.

Verified extension table (`info = ceil(log2(n!/m!))`, `pi = C - info`,
`T = S(m) + C`; `S(n)` from the baseline table):

| (m,n) | info | C | pi | T | S(n) | verdict |
|---|---:|---:|---:|---:|---:|---|
| (2,6) | 9 | 9 | 0 | 10 | 10 | exact |
| (2,7) | 12 | 12 | 0 | 13 | 13 | exact |
| (2,8) | 15 | 15 | 0 | 16 | 16 | exact |
| (3,7) | 10 | 10 | 0 | 13 | 13 | exact |
| (4,8) | 11 | 12 | 1 | 17 | 16 | coupling miss |
| (5,6) | 3 | 3 | 0 | 10 | 10 | exact |
| (5,9) | 12 | 12 | 0 | 19 | 19 | exact |
| (6,7) | 3 | 3 | 0 | 13 | 13 | exact |
| (6,8) | 6 | 6 | 0 | 16 | 16 | exact |
| (7,8) | 3 | 3 | 0 | 16 | 16 | exact |
| (7,9) | 7 | 7 | 0 | 20 | 19 | counting miss |
| (8,9) | 4 | 4 | 0 | 20 | 19 | counting miss |
| (9,10) | 4 | 4 | 0 | 23 | 22 | counting miss |
| (10,11) | 4 | 4 | 0 | 26 | 26 | exact |
| (10,12) | 8 | 8 | 0 | 30 | 30 | exact |

`pi` is 0 or 1 on every verified cell; exactness is cell-dependent and
non-monotone, and no single fixed-`m` split schema is exact across the range.
The researcher's note table lists cells only through `(4,7)` and names
`C(5,8)`/`C(6,9)` as "next decisive"; the shipped script computes both and the
verification above closes those cells. This discrepancy is in a table caption,
not in any lemma or computed value.

## Why this meets the publication gate

- Barrier/no-go result: the proved split-schema lemma rules out every fixed
  two-phase compositional schema from reaching `S(n)` on the demonstrated cells
  (counting miss or strict `+1` coupling penalty), a major route for a
  compositional FO(TC) compiler.
- Structural upper-bound contribution: a fixed-`v` polynomial-size strategy
  program model with a refereed polynomial evaluation bound and a conditional
  `Sigma_2^P` membership accounting.
- Independent paper argument (referee) + primary sources in the notes + serious
  falsification attempt (two-sided cell verification) + rationale for the
  central question are all present. Minimal, passing tests ship with the code.

## Explicitly open

Conjecture C (polynomial-size exact programs for every yes-instance) is open;
no unconditional lower bound for the sparse unary language is claimed; and the
final theorems for `S(n)`/`SORT-BOUND-U` are **not** resolved by this artifact.
A passing CI run and this record do not convert any open problem into a result.

## Addendum — witness-tree builder defect found and repaired (2026-11-20)

**New evidence.** After publication, the running SoringP1 frontier curator (agent
`b4eO8fEB3oKqlM6iTzelXh-down`) observed, in its own scratch probing, that the
shipped `scripts/fo_tc_split_schema.py` raises
`AssertionError: no optimal query found` on the cell `(2,6)`. I independently
confirmed this against the exact published commit `9018729`: all nine originally
committed cells succeed, but `min_completion(2,6)` fails. This means the shipped
script's claim to emit a witness tree "per cell" was **not** valid in general —
the CI suite passed only because it covered those nine cells.

**Root cause (confirmed by reading the exact code).** `greedy_ub` followed only
the larger child of each query (a single path), so it returned an underestimate
of the worst-case cost rather than a valid upper bound. `solve()` seeded its
upper bound from that value and pruned with `>= best`; on cells where the greedy
path is not optimal this discarded the true optimum, so `build()` could not find
a query whose exact child values matched the claimed cost.

**Repair (this addendum's commit).** `greedy_ub` now recurses into **both**
children with its own memo (never the exact-value memo), making it a sound upper
bound; a regression test (`test_witness_build_regression`) covers `(2,6)`,
`(2,7)`, `(3,7)`, `(5,9)`, `(6,8)`, `(7,8)`. Verified: all 15 checked cells now
return the independently known `C(m,n)` and their witness trees replay with
worst case exactly `C`; the full unit suite passes. **No mathematical `C` value,
lemma, note text or theorem changed** — this is a software-fidelity fix only.
The two research notes remain byte-identical to their refereed/verified sources;
the SHA-256 hashes above still describe those unchanged files.
