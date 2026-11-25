# antonina-uJ2CwAUiU0Ya5WV7uxkUpr-anglo

Session: ses_e05fa55ddffePF4d01qFnbcGYe
Workspace: /home/lubko/soring-fronts/verify-kraft-clean-recurrence-20261120
Created: 1795196037753; updated: 1795196831112

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 121 (msg_1fa0641240010hlRoOQ9fJHCaX)

## Audit result: inconclusive on #301’s specific claim

I couldn’t access the text of Antonina issue #301: the issue URL serves only the app shell, and I found no copy of its definitions or reported root tuples in this checkout. So I can’t responsibly verify the definitions of \(F,e,b,\epsilon,G\), reproduce the \(n\le6\) tuples, or determine whether the recurrence correctly enforces optimal-height constraints.

One logical point is clear in general: **a signed identity does not, by itself, imply a converse based on its unsigned or termwise interpretation.** If the identity contains factors \(1-\pi\), terms with \(\pi>1\) contribute negatively; dropping them, taking absolute values, or arguing that a sum is zero only when every summand vanishes is invalid without additional sign or cancellation control. That observation alone does not establish that #301’s claimed converse is false—the specific definitions and recurrence matter.

For reproducibility, the repository’s existing exact evaluator is `scripts/evaluate.py`. It uses the recurrence
\[
F(P)=1+\min_{x\parallel y}\max(F(P+x<y),F(P+y<x)),
\]
with \(F(P)=0\) for total orders. This is an independent implementation candidate for small-poset minimax values, but it does **not** reproduce #301’s tuples or check its claimed height constraints without the omitted definitions and tuple-generation procedure.

**Limitation:** I have no proof or counterexample for the issue’s precise inference. Please provide the issue text (including definitions, recurrence, tuples, and how height optimality is encoded); then I can audit the algebra and independently check the small cases.

## Output 206 (msg_1fa0756ee0017oywa1Pr9t6pQp)

**No external side effect occurred.** The previous turn did not post to Antonina or change the repository. The worktree is clean (`HEAD (no branch)`). I found durable audit material in `/tmp/opencode/`, including an exact evaluator and a draft post payload; I did **not** send that payload.

I resumed the unfinished small-case check. The initial evaluator’s optimal-height condition was too restrictive: it required every chosen comparison to satisfy \(1+\max(F(\text{children}))=F(P)\). That is not the right constraint at a node reached with inherited height budget. The correct constraint is \(\max(F(\text{children}))\le r-1\), where \(r\) is the remaining budget. I reran the recurrence with this budget-aware condition.

For \(n=2,\dots,6\), the independently coded evaluator returned \((e(\varnothing),S(n),G(\varnothing,S(n)))=(2,1,0),(6,3,0),(24,5,0),(120,7,0),(720,10,0)\). Here \(G\) minimizes the worst-path count of non-Kraft-clean comparisons among strategies fitting the height budget, using the draft’s cleanliness test on both children. The corrected and restrictive recurrences agree on these root values. Also, \(S(n)-\lceil\log_2(n!)\rceil=0\) throughout this range, so these cases do **not** refute the proposed converse.

This is limited experimental evidence, not a proof. In particular, the small cases do not establish the all-\(n\) converse or settle whether the signed \((1-\pi)\) terms permit the claimed inference. I’m stopping without posting: the issue’s exact signed identity and definitions still aren’t available in the durable records, and a root-value check cannot validate that algebraic step.

## Output 403 (msg_1fa116ea9001gWxuhkkgwSNGwU)

## Baseline and status

- **Current main SHA:** `6cddeaa2453d4da2ae0e918e50ba61c71a7da85f`.
- Initial worktree HEAD: `6a96398d937d20977a91b9afa8619cb27feab269` (24 commits stale).
- I read current policy/docs via `git show origin/main:...` and refetched #301 (with `source /home/lubko/.profile`).
- **Stale-baseline effect:** none material here. `git diff 6a96398..origin/main` changes only added research notes/scripts/tests plus one added row in `docs/research-plan.md`; `AGENTS.md`, `docs/problem.md`, `docs/operations.md`, `docs/literature.md`, and `docs/research-sergeev-asymptotic.md` are unchanged. The board was read fresh, not from the stale snapshot.
- **Claim status:** still open. Latest #301 posts are 16:15 original identity/sufficient lemma, 16:51 converse post explicitly saying “Converse remains OPEN”, 17:02 dispatch noting no verified results, and 17:22 verifying only the separate `pi<=1` n=6 falsifier. No post supersedes or resolves the converse.

No board writes, commits, repo changes, or theorem-completion claims were made. Worktree remains clean. Scratch work is only `/tmp/opencode/audit_kraft_v2.py`.

## Definitions checked (current main / #301)

- `F(P)=0` if `P` total; otherwise  
  `F(P)=1+min_{x||y} max(F(P+x<y),F(P+y<x))`.
- `e(P)` = number of linear extensions; `b(P)=ceil(log2 e(P))`; `eps(P)=F(P)-b(P)>=0`.
- `D(n)=S(n)-ceil(log2 n!)=eps(A_n)`.
- Kraft-clean at `P`: **both** children satisfy `e(child) <= 2^(b(P)-1)`.
- `G(P)` in the 16:51 post: minimum worst-case non-clean count among height-`F(P)` strategies, with recurrence restricting to pairs satisfying `1+max(F(children))=F(P)`.

Primary-source checks: `docs/problem.md` confirms the adaptive-tree model; `docs/literature.md` and OEIS A036604 confirm exact `S(n)` through 22; ECCC TR20-096 confirms Sergeev’s `log2(n!)+o(n)` is a **sorting upper bound**, not a converse certificate or an evaluation-complexity result.

## Audit of the signed identity and converse

### 1. One correction to the identity as worded

The 16:15 post says the identity holds for “any correct decision tree of height `r`”. That is false. It requires the comparison at each step to be **minimax-optimal** and the adversary to follow a maximizing child, so that `F(parent)=1+F(child)`.

For a non-optimal comparison, only `F(parent) <= 1+F(adversary child)` holds, so one gets a slack `Delta=F(parent)-1-F(child)<=0` and

`eps(parent) = (1-pi)+eps(child)+Delta`, not equality.

**Explicit counterexample [deduction + experiment]** from my from-scratch search over all posets `n<=4`:

`P=(0,0,0,3)`, `e=8`, `b=3`, `F=3`, pair `(0,2)`.  
Adversary child `C=(0,0,5,3)` has `e=5`, `F=3`, `b=3`, so `pi=0`.  
Then `eps(P)=0`, but `(1-pi)+eps(C)=1+0=1`.  
The pair is non-optimal: `1+max(2,3)=4 > F(P)=3`. In a correct tree of height 4 using it, the signed sum exceeds `eps(P)`.

Over all optimal pairs for `n<=4` (400 checked) the one-step identity had zero failures. So the telescoping identity is valid on minimax-optimal play, not arbitrary correct trees.

### 2. Signed terms invalidate the *inference*, not necessarily the converse statement

For an optimal step with adversary child `C`, `pi=b(parent)-b(C)>=0`. Let `N` be the non-clean indicator at the step.

- If `pi=0`, then `b(C)=b(parent)`, so the adversary child exceeds the Kraft threshold; hence the comparison is non-clean and `N=1`.
- If `pi=1`, the positive loss is `0`, `N>=0`.
- If `pi>=2`, the term `1-pi` is negative; such a step may be clean (`N=0`) if both children are below threshold.

Thus pointwise `N >= (1-pi)^+ >= 1-pi`, and along an optimal adversary path

`sum N >= sum(1-pi)^+ >= sum(1-pi) = D(n)`.

This gives exactly the **sufficient** direction: if every path has at most `c` non-clean steps, then `D(n)<=c`. The converse would need an **upper** bound `sum N <= D(n)`, which is the opposite inequality. Negative `pi>=2` terms can subsidize positive-loss steps, so the signed identity alone cannot produce it.

Concrete n=6 subsidy, independently recomputed:

`P=(30,16,8,0,0,0)`: `e=36`, `F=6`, `b=6`.  
Comparison `(1,5)` has children with `(e,F)=(20,5)` and `(16,5)`, threshold `2^5=32`, so it is **Kraft-clean**, yet the worse child gives `pi=6-4=2`, i.e. signed loss `-1`. Along the board’s height-10 path, the prefix drops are `[1,1,1,1]`, the `(1,5)` step is clean with drop `2`, and a later drop `0` contributes `+1`; total signed loss `0=D(6)`, but that path has at least one non-clean step, so `sum N >= 1 > D(6)`.

This shows the signed terms genuinely break the attempted converse inference. It does **not** refute the converse existence statement, because the independently computed `G(A_6)=0`: another optimal tree can avoid all non-clean steps.

## n<=6 root-tuple verification [experiment]

From-scratch implementation in `/tmp/opencode/audit_kraft_v2.py`: matrix-style transitive closure, subset-DP extension counting, exact minimax `F`, and two non-clean minimizers:

- `G_local`: board recurrence, locally minimax at every node.
- `H_budget`: exact relaxation for a strategy of total height `<=r`, using `max(F(children))<=r-1`.

Output of `python3 /tmp/opencode/audit_kraft_v2.py`:

| n | e(A_n) | F=S(n) | b | D | G_local | H_budget |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| 2 | 2 | 1 | 1 | 0 | 0 | 0 |
| 3 | 6 | 3 | 3 | 0 | 0 | 0 |
| 4 | 24 | 5 | 5 | 0 | 0 | 0 |
| 5 | 120 | 7 | 7 | 0 | 0 | 0 |
| 6 | 720 | 10 | 10 | 0 | 0 | 0 |

This reproduces the reported tuples `(2,1,1,0,0)` through `(6,10,10,0,0)` and confirms the optimal-height condition is encoded correctly at the root. Exhaustive comparison of `G_local` vs `H_budget` over all posets `n<=5` found no differences; `n=6` was checked at the root only, not over all 130,023 states.

**Definitional caveat:** the board recurrence recursing into `G(child)` enforces local minimax optimality at every node. The literal converse asks for a height-`S(n)` strategy, where a smaller-`F` sibling may have slack. `H_budget` is the exact recurrence for that relaxation. They agree on all checked roots and all states `n<=5`, but equivalence at `n>=7` is not proved. A future falsification using `G>D` would need to justify that local optimality at siblings is without loss of generality.

## Bottom line

- The sufficient Kraft-clean lemma is sound.
- The signed ceiling-loss identity is sound **only for optimal minimax play**, not “any correct tree”.
- The signed terms `(1-pi)` **do invalidate** the claimed converse inference: they yield only `sum N >= D`, never `sum N <= D`.
- The converse itself remains **open and not superseded**.
- Small cases `n<=6` give no counterexample; they are consistent with `G(A_n)=D(n)=0`.

No repo, Lean, CI, ledger, test, or board changes were made.
