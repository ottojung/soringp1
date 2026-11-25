# antonina-zsAMFmhFsUuLNWjz1rm0Jp-identity

Session: ses_df6094a3dffe7URaE1FIc6dlzC
Workspace: /home/lubko/soring-fronts/tight-root-defective-detour-necessity-alln
Created: 1795463493109; updated: 1795464903682

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_209f6b7e3001FUiWMKbUjcvI0T)

I'll start by exploring the repository structure and understanding the context, especially what "billy-dev" refers to.

## Output 21 (msg_209f6c1da001oBoV42l8KfNhT2)

I'm on `billy-dev` already with a clean tree. Let me read the core documents and find board #301.

## Output 44 (msg_209f6cfec001tsbLY9nmDc5nPG)

Now let me read the specific front definition, the budget-pruning doc, and the board digest.

## Output 63 (msg_209f6e0ca001Dq15CS3Tvbs0iA)

Let me search the board and docs for the precise definitions of "defect", "delta", "detour", and "repair".

## Output 99 (msg_209f70fae0010bdZMTXxG4BNJc)

Let me look at the existing scripts and my branch's recent commits to understand prior work and avoid duplication.

## Output 114 (msg_209f7dc2a0016jrqQaagMUxwhT)

I now have substantial context. Let me check the primary literature and the primary host ledger for this specific front's precise definitions, then do from-scratch computation.

## Output 129 (msg_209f8b8cd001yHcpDs6go0yc7T)

Let me verify with a from-scratch exact computation. First I'll build the core primitives.

## Output 156 (msg_209fb4476001VpIfMEM7TBLAl2)

Core primitives verified (S(5)=7, S(6)=10). Now let me find the n=6 depth-5 defective-then-repaired witness.

## Output 174 (msg_209fc1ef7001xApKOvNjd1zjV9)

Core witness confirmed: n=6 has a depth-5 state with e=16, L=4, F=5, D=1, repaired at depth 6. Let me build a fast C engine to verify n=7,8 and check defect-free tree existence systematically.

## Output 217 (msg_209fd2afe001RZ5GNC1AtgQfp7)

Go is available. Let me port to Go.

## Output 235 (msg_209fd6f9c001eSObLDn8uNeVrs)

Go works. Now let me run n=7,8,9.

## Output 246 (msg_20a021efc001kj3MRQloNcaY3a)

I found a potential gap in a prior accepted theorem's induction. Let me verify carefully and also compute `g(A_n)` directly (which needs only `e`, not `F`, so it's much cheaper).

## Output 280 (msg_20a0b1f28001Vc8LKCx4NSAf6Y)

## Recovery audit (backend-failure notice)

- Inspected: git status/branch/HEAD, board digest, frontier ledger, `/tmp/opencode` scratch.
- Git: `billy-dev` at `6a96398`, clean worktree, no commits/stash/branch changes made by me.
- External side effects by me: **none** (no #301 post, no PR, no commit, no purchase, no ledger write). Scratch only in `/tmp/opencode` (`detour_core.py`, `detour_search.py`, `detour.go`, `gonly.go`); n=9 `gonly` run was SIGKILLed, no external effect.
- Frontier ledger shows `tight-root-defective-detour-necessity-alln` as `running` (agent `zsAMFmhFsUuLNWjz1rm0Jp-identity`); I did not modify it.

## Front (as given)

> The antichain root is information-tight (`D(n)=S(n)-ceil(log2 n!)=0`) for every `n<=11`, yet at `n=6`, also tight, a height-`S(6)` optimal path passes through a depth-5 state with `delta=1` that is later repaired to `delta=0`. For all sufficiently large tight `n`, must such defective detours occur on some height-`S(n)` optimal path, making defect pruning incomplete on the tight regime, or do they occur only finitely often?  
> Falsifier: Show that for all large tight `n` every height-`S(n)` tree stays defect-free on all optimal paths, or exhibit infinitely many tight `n` carrying a defective-then-repaired optimal path with exact `e` and `F` computed from scratch.

## Model / definitions [definition]

- `P` = finite poset on `n` labelled keys (transitive closure). `A_n` antichain.
- `e(P)` = number of linear extensions. `L(P)=ceil(log2 e(P))`, information bound.
- `F(P)` = exact minimax remaining comparisons (SUPI): `F(total)=0`, else `F(P)=1+min_{x||y} max(F(P+x<y),F(P+y<x))`. `S(n)=F(A_n)`.
- Defect `D(P)=F(P)-L(P)>=0`. Tight/information-tight `n`: `D(A_n)=0`, i.e. `S(n)=L(A_n)=ceil(log2 n!)`.
- A move is **height-optimal/admissible** at depth `d` in a height-`S(n)` tree if both children `C` satisfy `F(C)<=S(n)-d-1` (equivalently `d+1+F(C)<=S(n)`).
- **Defect-based pruning** (the candidate evaluator heuristic): reject a state when `D(P)>0` / `L(P)>remaining`. This is **sound as a lower bound** (`F>=L`) but **not a priori complete** as a search decision: `D(P)>0` does not imply `F(P)>remaining`.
- **Defective detour** (front wording): a height-`S(n)` optimal path passing through a state with `D=1` later repaired to `D=0`. Since any completed optimal path ends at a leaf (`e=1,D=0`), “eventually repaired” is trivial for any feasible state; the mathematically relevant content is: a **defective but feasible** state lies on some height-`S(n)` optimal path.

## From-scratch recomputation [experiment]

Independent Python/Go code in `/tmp/opencode` (no repo script reused). Posets as transitive-closure successor bitmasks; `e` by order-ideal subset DP; `F` by memoized minimax; `g` by recursive sound defect-free certificate (`g(P): e==1 or exists incomparable pair with both children e<=2^(L-1) and g`).

| n | n! | `L(A_n)` | `S(n)=F(A_n)` | `D(A_n)` tight? | `g(A_n)` |
|---:|---:|---:|---:|---:|---:|
| 5 | 120 | 7 | 7 | 0 yes | true |
| 6 | 720 | 10 | 10 | 0 yes | true |
| 7 | 5040 | 13 | 13 | 0 yes | true |
| 8 | 40320 | 16 | 16 | 0 yes | true |

`g` is the standard sound certificate: `g(P)=>F(P)=L(P)` by induction [deduction, routine; also the accepted local predicate on board]. It is **not** known complete (`F=L => g` is open; the 13:51Z/14:19Z #301 thread gives a sharp necessary condition but not completeness).

## n=6 witness (confirmed) [experiment]

Exhaustive admissible BFS from `A_6`, budget `S(6)=10`, using exact `F`:

- Reachable admissible states: 66991, max depth 8.
- Defective admissible states: depth 5 has 19140 states, 1440 defective (`D>=1`).
- Found defective-then-repaired admissible path:
  - depth 0..4: `D=0`
  - depth 5: `D=1, e=16, L=4, F=5`, succ rows `(30,16,8,0,0,18)`
  - depth 6: `D=0, e=1, L=0, F=0`, succ rows `(62,16,58,50,0,18)` (leaf)

This confirms the prompt's n=6 example: a defective-but-feasible state occurs on some height-`S(6)` optimal path. It is **not** a counterexample to defect-free optimal-tree existence, because `g(A_6)=true` gives a complete defect-free height-10 tree.

## n=7 observation (partial) [experiment]

Exhaustive admissible BFS from `A_7`, budget 13, exact `F`: 3,044,007 admissible states. Defective admissible states occur at depths 3–9 (1680, 18480, 44520, 181440, 126000, 50400, 5040 respectively). Thus defective-but-feasible detours exist on some height-`S(7)` optimal paths. I did **not** test whether *every* height-`S(7)` optimal path/strategy hits a defective state; `g(A_7)=true` means at least one defect-free optimal tree exists.

## Mathematical finding (what is actually settled here)

1. **Soundness/completeness split is the real issue.** [deduction] Defect pruning `L(P)>remaining => infeasible` is sound because `F>=L`. The converse `D(P)>0 => infeasible at tight remaining` is false whenever a defective state is feasible (`F(P)<=remaining < ?` no: feasibility is `F(P)<=remaining`; defect means `F(P)>=L(P)+1`). So defective-but-feasible states are exactly `L(P) < F(P) <= remaining`. Such a state is a counterexample to *completeness* of defect pruning on that branch, but not to existence of another defect-free branch.

2. **The n=6 detour is real but does not settle the front.** [experiment+deduction] It falsifies “every height-`S(6)` optimal path is defect-free” only in the weak sense that *some* optimal path contains a defective node; it does **not** falsify existence of a defect-free height-`S(6)` optimal tree (`g(A_6)=true`). The front’s implication should be read carefully: “defect-based pruning cannot be a complete evaluator on tight n…” is true **if interpreted as pruning every `D>0` state on every search path**; it is false if interpreted as “no defect-free optimal tree exists”.

3. **For all known tight n with exact small-n check here (`n<=8`), `g(A_n)=true`.** [experiment] This gives an explicit defect-free height-`S(n)` optimal certificate for `n=5..8` (and n<=4 trivial). It is consistent with defect pruning being complete *as a certificate language* on these roots, while incomplete as a pathwise heuristic.

4. **No all-n theorem obtained.** I did **not** prove either horn:
   - Not proved: infinitely many tight `n` have a defective-then-repaired optimal path with exact `e,F` from scratch beyond the small-n evidence (I only have `n=6,7` exact pathwise evidence; `n=7` has defective admissible states, trivially repaired at leaves).
   - Not proved: for all large tight `n`, every height-`S(n)` tree stays defect-free on all optimal paths. This would actually be stronger than needed and is false in spirit already at `n=6`; the meaningful strong form is “every height-`S(n)` *optimal tree* has some defective node” or its negation “some height-`S(n)` tree is defect-free”.
   - Not proved: existence/nonexistence of defect-free optimal trees for large tight `n`, which is equivalent to the `S(n)=ceil(log2 n!)` asymptotic tightness question only under the unproved completeness conjecture `C: F=L => g`.

## Concrete failed approach / exact obstruction

- **Failed/blocked as a proof route:** use the `g` necessary-condition/induction to get all-n completeness or infinitude. The accepted 14:19Z theorem gives only a necessary condition (`e(P) > 3*2^(L-2)` forces `g` for defect-free `P`); the dangerous region `e(P) <= 3*2^(L-2)` remains open. A counterexample to completeness would need a defect-free `P` with no balanced defect-free pair and `L>=5`.
- **Exact obstruction:** the front conflates two different properties: (a) pathwise presence of defective-but-feasible states, and (b) nonexistence of any fully defect-free height-`S(n)` optimal tree. (a) is easy locally and already occurs at `n=6,7`; (b) is the hard completeness/tightness question. Moreover “all sufficiently large tight n” is unstable as a domain because infinitude of tight `n` (`S(n)=ceil(log2 n!)`) is itself open; known exact tight set through the literature cited in-repo is `n<=11,20,21` in small ranges, but asymptotic status is open.
- **Computational limit:** exact `F` exhaustive over all labelled posets becomes expensive past `n=7/8` in this scratch implementation; `g(A_9)` was killed (SIGKILL) in the quick run, so I do not claim `n=9`.

## Bottom line

**No new all-n theorem or counterexample.** The precise defensible result is: from-scratch computation confirms the `n=6` defective-but-feasible detour and shows defective-but-feasible admissible states also occur at tight `n=7`, while `g(A_n)` holds for `n<=8`, so defect pruning is sound but pathwise incomplete; however the front’s infinite/finitary dichotomy remains open because it hinges on the unproved completeness of the defect-free certificate (`F=L => g`) and/or the open asymptotic tightness of `S(n)=ceil(log2 n!)`.
