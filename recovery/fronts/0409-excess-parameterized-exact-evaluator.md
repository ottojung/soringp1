# excess-parameterized-exact-evaluator

## status

investigated

## origin

ai_proposal_unverified

## agent_id

uEpAn6sq79zjLObNN3d8lc-welcome

## exit_state

clearexit

## question

Is there a uniform algorithm computing S(n) in time poly(n)*2^{O(E(n))}, where E(n)=S(n)-ceil(log2 n!) is the information excess, or does every exact evaluator require time 2^{omega(E(n))} on an infinite family?

## basis

Board #301 bulk-insertion-information-defect, single-bit-excess-dichotomy, lookahead-convergence-depth, and the independently checked 2^{O(n log^2 n)} exact evaluator in docs/problem.md.

## falsifier

Give the parameterized evaluator with a proved resource bound, or prove an infinite-family lower bound showing poly(n)*2^{o(E(n))} time is impossible under a stated uniform model.

## implication

Such an FPT-in-excess algorithm would make every O(log n)-excess regime polynomial-time and give a new route to SORT-BOUND-U in P, while a lower bound would show excess is not the right algorithmic parameter.

## finding_unverified

 optimal tree, or any certificate consisting of an explicit comparison tree, has size/time at least
   \[
   2n!-1=2^{(1-o(1))n\log_2 n}=2^{\omega(E(n))}.
   \]
   So no `poly(n)2^{O(E(n))}` algorithm exists in this model.

2. **Complete winning-frontier enumeration.** The independently checked winning-frontier theorem gives, for infinitely many `n=2^{2r}` at the exact optimal budget, at least
   \[
   2^{(1/4-o(1))n(\log_2 n)^2}
   \]
   pairwise nonisomorphic reachable winning posets. Since `E(n)=o(n)`, this is also `2^{\omega(E(n))}`. Complete frontier enumeration is therefore not FPT in `E`.

3. **Extension-count lookahead.** The verified #301 theorem gives `t*(n)>=n-O(log n)` whenever `E(n)>0`. Since `E(n)=o(n)`, any infinite positive-excess family has `t*(n)=\omega(E(n))`. Thus the `t`-ply counting hierarchy with `t=O(E)` cannot be complete.

These are lower bounds for tree output, complete frontier enumeration, and lookahead depth respectively — **not** for computing the single value `S(n)`.

## Concrete failed approach / obstruction

The natural selective recursion also does not immediately work: on the harder child of a comparison the information slack `d-L(P)` cannot increase, but the easier child may have much larger local excess. Thus `E(n)` does not bound the local excess of every subproblem in an exact minimax recursion. A genuinely selective value-only algorithm would need a new branch certificate avoiding both tree/frontier size and `\omega(E)` lookahead depth; none is known.

General-poset hardness and certificate soundness do not transfer to the fixed antichain root, and unary sparsity blocks the usual many-one hardness route.

## Honest limits

I did **not** prove the general lower bound `2^{\omega(E(n))}` for arbitrary uniform value evaluators, nor did I construct an FPT-in-excess evaluator. An FPT algorithm would give a `2^{o(n)}` exact evaluator and, since `E(23),E(24)<=1`, would settle the open values `S(23),S(24)`. So this remains a major open problem, not a solved front.

One board post was made exactly once: `2026-11-08T23:37:38.009Z`, author `SoringP1 frontier: excess-parameterized-exact-evaluator`, id `sha256:1_rzfzGFjG63LcKjRx47JFGuPTWRiaA5_S9breuJ1nI`. No Lean, repository, commit, or ledger changes were made.
Recovery inspection complete. I did **not** repeat the research prompt or any external action.

**Effects actually present**
- Host: `billy-dev`
- Worktree: `/home/lubko/soring-fronts/excess-parameterized-exact-evaluator`
- Git: clean at `6a96398`; no commits, branches, edits, Lean files, or repository changes
- Board #301: exactly **one** post for this front:
  - `2026-11-08T23:37:38.009Z`
  - author `SoringP1 frontier: excess-parameterized-exact-evaluator`
  - id `sha256:1_rzfzGFjG63LcKjRx47JFGuPTWRiaA5_S9breuJ1nI`
- No duplicate board comment exists.
- Scratch artifacts remain only under `/tmp/opencode`.

**Durable task record**
The keeper ledger still marks `excess-parameterized-exact-evaluator` as `status: running`, with `exit_state: null`. I did not edit it, since that transition is keeper-managed.

**Mathematical status**
The prior finding stands: FPT-in-excess is false for explicit-tree/certificate-complete methods and complete winning-frontier enumeration, and the extension-count lookahead depth is not `O(E)`. The general value-only question remains open; no arbitrary-uniform-evaluator lower bound was proved.

**Unfinished work**
None in the research task. No uncertain external effect remains.

## Other metadata

```json
{
  "finished_at": 1794181254.4897292,
  "started_at": 1794180603.5785365
}
```
