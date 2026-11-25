# antonina-JeM4g6qvoS8cuPuj1UaZVN-pelican

Session: ses_df8563a24ffeDOfCgifue7rsRI
Workspace: /home/lubko/soring-fronts/tight-info-defectfree-optimal-tree-alln
Created: 1795424896564; updated: 1795425540799

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 187 (msg_207b0ef27001hZdPRE9O1OMJQi)

## Scope / recovery

- **Host**: `billy-dev` (confirmed). Worktree `/home/lubko/soring-fronts/tight-info-defectfree-optimal-tree-alln`, clean at `6a96398`. No repo/Lean/test/CI/board/main changes made; scratch only in `/tmp/opencode`.
- **Read**: `AGENTS.md`, `docs/problem.md`, `docs/literature.md`, `docs/operations.md`, `docs/research-n12-nontightness.md`; Antonina #301 recent/filtered posts (defect-free n7/n8/n9/n10-search/n11-commissioned, referee dispositions, intermediate n11 state).
- **No prior side effects** for this front observed on #301; no result repeated.

## Question (as given)

For every integer `n>=1` with `S(n)=ceil(log2(n!))`, is there a height-`S(n)` adaptive comparison decision tree sorting the `n`-antichain in which every reachable state `P` satisfies `F(P)=ceil(log2(e(P)))` (information-defect zero)?

- **Falsifier**: any tight `n` with a certified argument/exhaustive search showing every height-`S(n)` sorting tree reaches some `P` with `F(P)>ceil(log2(e(P)))`.
- **Complexity implication**: positive => root information tightness propagates to a locally tight optimal certificate on tight instances, constraining exact-search/certificate structure; counterexample => separates global and local information tightness.

## Definitions / model check [definition]

Adaptive worst-case pairwise comparison sorting of `n` distinct labelled keys (`docs/problem.md`). `e(P)` = number of linear extensions of reachable partial order `P`. `F(P)=m(P)` = minimax comparisons to sort `P` (height from `P` in optimal decision tree). Defect `D(P)=F(P)-ceil(log2(e(P)))>=0`. Root tightness is `S(n)=F(antichain_n)=ceil(log2(n!))`.

A "defect-free optimal tree" is a height-`S(n)` tree with `D(P)=0` for every reachable state. This is equivalent to the balanced-split predicate used on board: `g(P)` iff `e(P)<=1` or some incomparable pair gives both children `e(child)<=2^(ceil(log2(e(P)))-1)` and `g(child)` true. [deduction] `g(P)` implies `F(P)=ceil(log2(e(P)))`; conversely `F(P)=ceil(log2(e(P)))` implies some budget-balanced comparison exists, but not directly `g` of children (see gap below).

## Known tight instances [literature + computation]

Using OEIS A036604 S(n) values and exact `ceil(log2(n!))` (computed locally):

| n | ceil(log2 n!) | S(n) | tight? |
|---:|---:|---:|:---:|
| 1-11 | 0,1,3,5,7,10,13,16,19,22,26 | same | yes |
| 12 | 29 | 30 | no |
| 13-19 | 33,37,41,45,49,53,57 | 34,38,42,46,50,54,58 | no (+1) |
| 20 | 62 | 62 | yes |
| 21 | 66 | 66 | yes |
| 22 | 70 | 71 | no |

So the all-`n` claim covers `n<=11,20,21` in the known `n<=22` range, and any future tight `n`. It excludes `n=12` (root gap) — consistent with problem statement.

## Board evidence already present [literature/experiment, as reported]

- n=6: defect-free optimal tree exists (reported in prime-defect-persistence-alln; reproduced by n8/n9 front). Referee accepted n=6/n=7 reproducibility.
- n=7: decisive EXISTS (defectfree-optimal-tree-n7, independently re-derived by Viche with different algorithm). Accepted.
- n=8: EXISTS, 0.389s quotient search, 80639-node witness independently rebuilt by reporter (height assertions 0 bad, 40320 distinct leaves). Referee accepted method/soundness; did not independently re-run n=8.
- n=9: EXISTS, witness-verified by reporter (725759 nodes, 362880 distinct leaves). Referee caveat same as n=8.
- n=10: SEARCH-level EXISTS (6m40s), not witness-verified. Not a checked witness.
- n=11: commissioned, no posted result found.
- n=12: excluded (S(12)=30>29).

I did **not** re-verify n=8/n=9/n=10; I treat them as reported/partly refereed, not as my own independent computation.

## Mathematical attack

### 1) Logical gap (why the claim is nontrivial) [deduction]

Let `r=ceil(log2(e(P)))` and assume `F(P)==r` (locally tight). For an optimal comparison, `r = 1+max(F(P1),F(P2))`, so `F(Pi)<=r-1`. Since `F(Pi)>=ceil(log2(e(Pi)))`, this forces `e(Pi)<=2^(r-1)` — a budget-balanced split exists.

However, this does **not** imply `g(Pi)`: a child may satisfy `F(Pi)<=r-1` either because it is locally tight at level `r-1` (`F(Pi)==ceil(log2(e(Pi)))==r-1`) but has no defect-free extension, or because it has slack (`ceil(log2(e(Pi)))<r-1`) but still cannot be sorted by a power-of-two-balanced-at-every-level tree of height `r-1`. Therefore local tightness does not trivially propagate; the all-`n` claim is a real compositional property, not an immediate consequence of `F(P)==ceil(log2(e(P)))`.

### 2) Exhaustive small-n search for the propagation gap [experiment]

I ran an independent small exhaustive check (Python, scratch `/tmp/opencode/check_defectfree.py`; transitive-closure posets, exact linear-extension DP over subsets, full minimax `F`, and defect-free predicate `g`). It enumerates **all states reachable from the antichain by any comparison sequence** (not all labelled posets):

| n | reachable states | defect `F>ceil` | tight & `g` | tight & not `g` |
|---:|---:|---:|---:|---:|
| 4 | 59 | 0 | 35 | 0 |
| 5 | 699 | 0 | 579 | 0 |
| 6 | 37206 | 3004 | 33482 | 0 |

"tight & not `g`" means `F(P)==ceil(log2(e(P)))` but no height-`ceil(log2(e(P)))` defect-free tree exists from `P`. **Finding: none observed for `n<=6`.** This rules out the simplest falsifier shape (a reachable locally-tight-but-trapped state) at these sizes. It does **not** prove absence for larger `n`; `n=7` full `F` enumeration did not complete within 120s in this naive Python implementation.

### 3) Falsification attempts considered

- **Reachable defect states as falsifier**: invalid by itself. n=6 has 3004 defect reachable states but `g(root)=true`; n=11 has a reported/independently-refereed reachable defect state (the Q/R/P path, D(Q)=1), but that only shows avoidability is nontrivial, not impossible.
- **Forced Merge(2,4)/merge-gap states**: Merge(2,4) has `e=15, ceil=4, F=5` [experiment, n12 note]. A defect-free optimal tree can avoid it if any alternative exists; falsification would need it forced on every optimal tree. I found no such forcing argument.
- **Tight-but-trapped state**: not found for `n<=6`; open for `n>=7`.
- **Large tight n (20,21)**: satisfy precondition but are computationally inaccessible here; no argument either way.

### 4) Structural obstruction to a proof [deduction]

A proof of the all-`n` claim would need a compositional lemma of the form: every locally tight reachable state has a budget-balanced comparison whose children are defect-free-extendable. The natural induction on `r=ceil(log2(e(P)))` fails at the point identified above: `F(Pi)<=r-1` does not force `g(Pi)`. Any proof must additionally control the minimax/defect structure of children, not just extension counts. This is the exact obstruction I could not bridge.

A disproof would need either a certified tight-but-trapped reachable state on every optimal tree of some tight `n`, or an exhaustive optimal-tree obstruction. n=11 is the first unresolved tight case on board; n=20,21 are also tight but far larger.

## Assessment

- **Status: UNRESOLVED (no theorem, no counterexample).**
- **What is established here**: the propagation gap is real (local tightness => balanced split exists, but not obviously defect-free children) [deduction]; exhaustive reachable-state check finds no tight-but-trapped state for `n<=6` [experiment]; the claim is non-vacuous and includes known tight `n=20,21` beyond the small-n board witnesses [literature/computation].
- **What is not established**: no proof that propagation holds for all tight `n`; no counterexample; no independent re-verification of board n=8/n=9 witnesses; n=11 undecided.
- **Limits/honesty**: this does not change S(n) or SORT-BOUND-U. A defect-free tree has `2n!-1` nodes and is not an NP/certificate-complexity object. The small-n Python check is a sanity experiment, not a formal proof artifact. The strongest next decisive case remains n=11 (decides smallest non-defect-free n between 11 and 12 under the reported n<=10 evidence), but n=20,21 remain open tight instances for the all-`n` claim.

## Output 199 (msg_207b1faa4001nlBfQpNP1p46mm)

I'll audit the actual state before doing anything else. No board posts, commits, or external writes were intentionally made in my prior turn — but I'll verify rather than assume.

## Output 231 (msg_207b33ed1001CccbNwmti9nXV6)

I have enough to conclude, but let me do one final local check for any board text unique to my report (no external calls).

## Output 242 (msg_207b370db001w3TuEyD2ooLACy)

## Audit result: no external side effects occurred; no unfinished work to continue

I inspected the conversation, working directory, Git state, and durable task records. Findings:

**Effects that actually happened in the prior turn**
- Read-only operations only: file reads (`AGENTS.md`, docs), `board_digest.py` queries and `antonina board show --json` fetches (reads), and local scratch files in `/tmp/opencode` (`check_defectfree.py`, `board301-p1.json`, `board-*.txt`, `post-*.txt`).
- The turn delivered a complete research report (status: **UNRESOLVED**, with a small-n experiment and the compositional-gap obstruction).

**Effects that did NOT happen**
- **No board post.** Searched all 8 pages of #301 for my front slug `tight-info-defectfree-optimal-tree-alln` and for unique phrases from my report (`tight-but-trapped`, `propagation gap`, `37206`, `33482`) — zero matches. No post by me exists to duplicate or undo.
- **No commit / repo change.** `git status --porcelain` empty; `HEAD = 6a96398`; `git reflog` = clone only. No Lean/test/CI change.
- **No durable record write by me.** The ledger entry for my front shows `status: "running"` with `started_at` set at keeper launch — this is infrastructure state from the front being commissioned, not a side effect of my turn. I made no ledger/bill/case/main change.

**No uncertain effects.** Everything is accounted for: the only artifacts are scratch files under `/tmp/opencode` at timestamps 09:09–09:12 matching the prior turn. Nothing external is in a partial or ambiguous state.

**Unfinished work:** none. The prior turn completed its full deliverable (the falsifiable all‑n question, falsification attempts, small-n exhaustive check, structural obstruction, and honest limits). The research conclusion stands as reported:

- Claim unresolved; no proof, no counterexample.
- Exhaustive reachable-state check for `n≤6`: no locally-tight-but-not-defect-free-extendable state found; defect states exist but are avoidable.
- `n=7` full enumeration did not complete in-budget; `n=11` and tight `n=20,21` remain open; board n=8/n=9 witness claims were not independently re-run by me.

I have taken **no external action** in this turn and will not re-post, re-commit, or repeat the computation. No review item is needed.
