# antonina-Lx5jEz67574FH2on9GFA3G-penalties

Session: ses_e3bba64adffekD0QXGF1bjhgLN
Workspace: /home/lubko/soring-fronts/upper-inequality-height-two-restriction
Created: 1794294258987; updated: 1794300254912

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 1442 (msg_1c49ef4fb001mf7cNpj2eHnPLZ)

## Front report: `upper-inequality-height-two-restriction`

**Question.** Does `(U)  alpha(P) <= C(covers(P)+psi(m_P,M_P))`, with `C=(5-log2 15)/8`, `alpha=F-log2 e`, hold for every finite poset of height at most two?

**Outcome: no counterexample found; the all-`n` claim remains open.** The result is a mixture of exact finite computation, a concrete failed induction, and a precise structural obstruction. There is no proof and no `S(n)`/`SORT-BOUND-U` consequence.

### 1. Exhaustive exact computation through n=10

I enumerated every unlabelled height-two poset with `nauty genposetg` and an independent digraph6 parser, then computed exact `e`, `covers`, `m`, `M`, `psi`, and exact minimax `F` with the existing nauty-quotient DP (`/tmp/opencode/fonly`). Counts: **164, 557, 2223, 10766** at `n=7,8,9,10`.

**No height-two poset with `n<=10` violates `(U)`.** The maximum ratio `alpha/D` is decreasing:

| n | max `alpha/D` | maximizer data |
|---|---|---|
| 7 | 0.098904 | `e=420, covers=5, m=M=4, D=13, F=10` |
| 8 | 0.092353 | `e=1568, covers=7, m=5,M=3, D=15, F=12` |
| 9 | 0.091924 | `e=12600, covers=6, m=5,M=4, D=15, F=15` |
| 10 | 0.087306 | `e=88200, covers=8, m=M=5, D=18, F=18` |

All are well below `C=0.1366386755`. The largest `(U)` excess at `n=10` is `-0.807`.

### 2. n=11 partial result

I generated all **64,956** unlabelled height-two posets at `n=11`. The crude upper bound `alpha <= S(11)-log2 e` with `e >= a!b!` leaves 200 candidates with positive crude excess. The top candidate (`e=831600, covers=6, m=6,M=5, D=17`) is a disjoint union of a 3-point star and a 4-edge matching. Its exact `F` is bounded by

`F <= F(star)+F(matching)+M(3,8) = 1+12+8 = 21`,

where `M(3,8)=8` is the exact two-chain merge cost (computed by a profile DP; it reproduces the known values `M(2,4)=5`, `M(5,5)=9`, `M(6,6)=11`). Since `log2 e = 19.665`, `alpha <= 1.335 < C*D = 2.323`. The crude leader is safe. The full `n=11` space was not exhausted.

### 3. Concrete failed approach: the `D`-induction is blocked on height two

For a height-two poset, adding a relation between two minima (or two maxima) creates exactly one cover and lowers `psi` by 1 (when `m,M>=2`), so `D_i = D`. Adding a cross relation creates one cover and leaves `psi` unchanged, so `D_i = D+1`. Therefore the induction step

`1 + log2 p_i + C(D_i-D) <= 0`

for a minima/maxima comparison forces `p_i <= 1/2` on the majority branch, i.e. `p_i = 1/2` exactly. The route closes **iff** the poset has two minima or two maxima with a perfectly balanced extension split `e_1=e_2`. No such balanced pair is guaranteed (distinct neighbourhoods give `e_1 != e_2`), so the cover-destruction induction with potential `D=covers+psi` is blocked already on height two. This is a different obstruction from the general-poset `n=5` failure at `P=(16,16,17,23,0)`.

### 4. `(U)` is not closed under disjoint union

For components with `(m,M)=(2,4)` and `(3,1)`, `psi` is 6 and 3, but their disjoint union has `(m,M)=(5,5)` and `psi=10`. So `D` is not additive, and `F(A squnion B)` can exceed `F(A)+F(B)+2` by a large amount. A necessary-condition search over all pairs (53,429) and triples (10,046) of height-two posets with total `n<=11`, using the superadditivity lower bound `F(A squnion B) >= F(A)+F(B)+2`, found **no** potential `(U)` violation.

### 5. The `a=2` subclass

For height-two posets with exactly two minima, `F - ceil(log2 e) <= 1` for all `n=7..10` (counts 28, 43, 62, 86). If this persists, then `alpha <= 2`, and `(U)` would follow for `a=2` for all `n>=15`; combined with exhaustive `n<=10`, only `n=11..14` would remain. This is a finite observation, not a proof.

### 6. Honest limits

- No all-`n` proof and no counterexample.
- The exact obstruction is the **merge-cost gap** in the sort-then-merge decomposition `F <= S(a)+S(b)+M(G)`: `M(G)` is not bounded tightly enough in terms of `E` and `e` to close `(U)`.
- `n=11` is not exhaustive; the dense subset and the top crude candidates are safe.
- This is a structural minimax statement about height-two posets. It is **not** a certificate result: the information bound is sound but not complete, and general-poset results (Fredman, Kahn–Saks) do not transfer.
- No `S(n)`, `SORT-BOUND-U`, P/NP/PSPACE, or certificate-completeness consequence is claimed.

**Board post:** Antonina issue #301, 2026-11-10 08:34Z, author `SoringP1 frontier: upper-inequality-height-two-restriction`. Worktree clean at `6a96398`; no repository or Lean changes. Scratch: `/tmp/opencode` (`filter_h2.cpp`, `h2_roots_*.txt`, `h2_meta_*.txt`, `h2_F_*.txt`, `comps11_*`, merge DP).

## Output 1495 (msg_1c4a0c491001XEHlAHbogCML0v)

**Recovery inspection (no actions taken that duplicate side effects)**

- **Host / repo:** `billy-dev`, `/home/lubko/soring-fronts/upper-inequality-height-two-restriction` on `billy-dev...origin/billy-dev`, worktree clean, HEAD `6a96398` (“Merge commit '6859bc2' into research/exact-reset-tree-realizability-20261027”). No uncommitted changes and no new commits beyond that state.
- **Durable artifacts present (scratch):** `/tmp/opencode/fonly{,.cpp}`, `/tmp/opencode/filter_h2{,.cpp}`, height-two data `h2_roots_{7..11}.txt` (165/558/2224/10767/64957 lines), `h2_meta_{7..11}.txt` (164/557/2223/10766/64956), exact results `h2_F_{7..10}.txt` (164/557/2223/10766), plus `board_post_upper_h2.md` and `board_post_result.json` (all consistent with the prior run).
- **External side effect (board #301) — already performed, not repeated:** `/tmp/opencode/board_post_result.json` records the posted finding for front `upper-inequality-height-two-restriction` with `"state":"open"`, `"updatedAt":"2026-11-10T08:34:52.247Z"` (recordedAt `2026-10-19T03:34:52.169Z` in payload; verdict/record fields present as stored). The stored body matches `board_post_upper_h2.md` (exhaustive height-two `n<=10`: no `(U)` violation, max `alpha/D` 0.098904/0.092353/0.091924/0.087306; `n=11` partial 64,956 classes with top crude candidate shown safe; D-induction/balanced-split obstruction on height two; `(U)` not closed under disjoint union; `a=2` subclass observation; honest limits). **I did not repost.**

**Determination**
- **Completed effects:** computation/enumeration artifacts in `/tmp/opencode` and the Antonina board #301 findings post above. No repository or Lean changes were made (and none are present).
- **Unfinished (research-blocked, not a failed side effect):** no all-`n` proof or counterexample for `(U)`; merge-cost gap in `F <= S(a)+S(b)+M(G)` not tight enough to close it; `n=11` not fully exhaustive (exact minimax on remaining dense/candidate subsets expensive). `a=2` subclass remains a finite observation only.
- **No actions taken now:** nothing safe/necessary to resume without risking duplicate external effects or speculative work; the prior report stated “next move: none required” for that request. Per contract, no Lean/repo changes without a substantive, independently checkable new theorem or counterexample.

**Uncertainties for review (not guessed):** I could not independently re-query Antonina board #301 from this environment beyond the local `board_post_result.json` record; the record indicates the post/update occurred, but if authoritative confirmation is needed it should be verified against the live board before any further posting. No commits, PRs, or other external actions were detected or performed.
