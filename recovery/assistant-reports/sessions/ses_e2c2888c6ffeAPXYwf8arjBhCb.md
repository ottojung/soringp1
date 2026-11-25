# antonina-MoGnFiMoDG1X5Gnn1MkQSh-average

Session: ses_e2c2888c6ffeAPXYwf8arjBhCb
Workspace: /home/lubko/soring-fronts/optimal-play-balanced-comparison-existence
Created: 1794555475825; updated: 1794564681057

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 165 (msg_1d463084d001hyQ1lJR51F7yn8)

## Task / recovery check (billy-dev)
- Read: `AGENTS.md`, `docs/problem.md`, `docs/literature.md`, `docs/operations.md`, `docs/research-frontier.json`; checked git state (`billy-dev...origin/billy-dev`, clean worktree, recent commits unrelated) and board #301 digest (`python3 /home/lubko/soring301/scripts/board_digest.py --recent 7`). No prior conversation state, no repo changes, no commits, and no board posts made by this turn. Scratch computation only in `/tmp` (not retained as a repository artifact).

## Precise claim attacked (all `n`)
**Model (definition).** `P` is a strict partial-order state on `n` distinct labelled keys (transitive closure of comparisons). `e(P)=|Ext(P)|` is the number of linear extensions. `F(P)` is the minimax remaining worst-case comparison count
- `F(P)=0` if `P` is total,
- `F(P)=1 + min_{x‖y} max(F(P+x<y), F(P+y<x))` otherwise,
with `S(n)=F(\varnothing_n)` (`docs/problem.md`, `docs/upper-bound.md`, A24/`S_eq_adv_univ` context). A pair `{x,y}` is **minimax-optimal** at `P` if it attains `F(P)`, and **3/11-balanced** if `min(e(P+x<y),e(P+y<x))/e(P) >= 3/11`.

**Front.** For every `n>=1` and every poset state `P` reachable from the `n`-element antichain along some comparison strategy of minimax height `S(n)` (i.e. reachable by a path of minimax-optimal moves in the union of all optimal root strategies), does there exist an optimal next comparison `{x,y}` with `min(e(P+x<y),e(P+y<x))/e(P) >= 3/11`?

**Falsifier.** Some `n` and such optimal-reachable `P` with every incomparable pair satisfying `min(e(P+x<y),e(P+y<x))/e(P) >= 3/11` having `1 + max(F(P+x<y), F(P+y<x)) > F(P)` (equivalently, every 3/11-balanced move is strictly non-optimal).

## Primary-literature / model distinctions
- **Kahn–Saks 1984, "Balancing poset extensions"** (Order 1(2):113–126; also STOC 1984 context): every finite poset that is not a chain has an incomparable pair with `3/11 <= Pr[x<y|P] <= 8/11`, i.e. a 3/11-balanced comparison exists in *every* poset state. This is a **general-poset balance/existence** result (sound for the probability split), not a statement about minimax optimality `F(P)` or about optimal antichain-root reachability. (Linial's 1/3–2/3 conjecture remains stronger/open; not needed here.)
- **Certificate SOUNDNESS vs completeness:** Kahn–Saks gives a sound local heuristic/witness that a balanced split exists; the front asks for a much stronger *normal-form completeness* property of exact optimal play — that one can always realize minimax height `S(n)` while choosing a balanced move at every optimal-reachable state. Existence of some balanced pair and existence of some optimal pair do not by themselves imply a common pair.
- **General-poset vs antichain-root:** the quantification is restricted to states reachable from the antichain along *some* height-`S(n)` root strategy. A counterexample would have to occur on such an optimal-reachable state (stronger than "some poset exists" unless that poset is shown optimal-reachable), and conversely positive evidence on arbitrary posets would not suffice without the reachability/optimality constraint. I did not assume a general-poset-to-antichain transfer.

## Disproof attempts

### 1) Analytic/information objection (no disproof found)
For any pair, `F(P_i) >= ceil(log2 e(P_i))` (information lower bound). A 3/11-balanced pair keeps `max(e(P+x<y),e(P+y<x)) <= (8/11)e(P)`, so its child information lower bounds are, if anything, *favored* relative to a highly unbalanced split (which can force one child to retain most extensions). Meanwhile `F(P)=1+min_{x‖y} max(F(P+x<y),F(P+y<x))` depends on exact minimax values of both children, not just extension counts. This yields no separation in either direction and no all-`n` counterexample construction: Kahn–Saks prevents an "all-balanced-pairs make one child total" shortcut once `e(P)` is nontrivial, but does not control `F` tightly enough to force a non-optimal balanced move.

### 2) Computational falsification attempt (experiment, discriminating)
Exhaustive check in `/tmp` (Python; exact `F` by minimax DP over all reachable labelled posets, linear-extension counts by subset DP, union over **all** optimal moves at each reached state = every state reachable along *some* height-`S(n)` strategy):

| n | `S(n)` | all reachable posets | optimal-reachable states | non-total checked | states where no 3/11-balanced move is minimax-optimal |
|---|---:|---:|---:|---:|---:|
| 5 | 7 | 4231 | 1551 | 1431 | 0 |
| 6 | 10 | 130023 | 65551 | 64831 | 0 |

`n<=5` reproduces the stated evidence (1551 states). `n=6` extends it to the full optimal-reachable union and finds **no counterexample** (no state where every pair with `min(e(P+x<y),e(P+y<x))/e(P) >= 3/11` has `1+max(F(P+x<y),F(P+y<x)) > F(P)`).

## Mathematical finding / status
- **Finding (negative/inconclusive on the front):** I found **no falsifier** and **no proof**. The all-`n` claim remains **open**.
- **What was seriously tried:** primary-source/model separation (Kahn–Saks balance existence is not minimax-optimality completeness), an information-lower-bound sanity check for a forced separation (inconclusive, leans against an easy disproof), and an exhaustive optimal-reachable-state search extended to `n=6` (65551 states, 0 counterexamples). No structural theorem was obtained that would imply all-`n` truth.
- **Concrete obstruction / honest limits:** A proof would need a global invariant linking extension-balance (Kahn–Saks 3/11 split) to the exact minimax value `F` along *every* optimal-reachable antichain-root state for all `n`; I do not have such an invariant. A disproof would require an explicit optimal-reachable state (hence an explicit height-`S(n)` witnessing path) whose every 3/11-balanced split is minimax-suboptimal; exhaustive search found none for `n<=6`, but this is finite evidence only. I did **not** verify the union-of-all-optimal-strategies reachability against a stronger "reachable on some fixed optimal policy under adversarial optimal replies" refinement beyond the standard `1+max(F(child1),F(child2))==F(P)` optimal-move characterization used here, though this is the natural minimax-DAG notion consistent with the prompt. No independently checkable new all-`n` theorem/counterexample emerged, so no Lean/repository changes are warranted.

**Complexity implication (conditional, as stated):** a positive all-`n` answer would be a structural pruning/normal-form constraint confining optimal root strategies to Kahn–Saks-balanced moves (relevant to exact evaluators/succinct strategy descriptions) but would **not** by itself yield a complexity-class separation for unary `S(n)`; a refutation would separate extension-balance heuristics from exact antichain-root optimality. Current status: unresolved.
