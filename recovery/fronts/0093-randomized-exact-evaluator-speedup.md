# randomized-exact-evaluator-speedup

## status

investigated

## origin

ai_proposal_unverified

## agent_id

eCcl8L6atK2E5sXx1NgXro-wasting

## exit_state

clearexit

## question

For the unary function S_unary(1^n), can a uniform randomized algorithm (with zero error, worst-case time bound over random coins) compute S(n) exactly in time 2^(o(n log^2 n)) for all large n, or is there an all-n lower bound ruling out subexponential-in-n log^2 n randomized exact computation?

## basis

Budgeted DFS gives 2^(O(n log^2 n)); problem states faster exact evaluators are in scope, but no front in the ledger targets zero-error randomized uniform computation of S(n).

## falsifier

Construct an explicit zero-error randomized uniform algorithm achieving 2^(o(n log^2 n)) time for all large n with a correctness/cost proof, or prove an unconditional 2^(Omega(n log^2 n)) time lower bound for zero-error randomized computation of S(n).

## implication

A verified randomized speedup would improve the known uniform upper bound for computing S(n) without changing the comparison model; a randomized lower bound would sharpen barriers to exact evaluation beyond deterministic search.

## finding_unverified

bound over random coins) compute S(n) exactly in time 2^(o(n log^2 n)) for all large n"

So "worst-case time bound over random coins" - if worst case over random coins means for each input, max over coins of time is bounded by T(n), then that's bounded Las Vegas = equivalent to deterministic. So you cannot do better than deterministic 2^(O(n log^2 n)). Hence there is an all-n lower bound ruling it out (same as deterministic lower bound, or at least not better). That would mean the answer is: no, impossible for bounded Las Vegas; equivalently deterministic. That seems trivial.

Alternatively if "worst-case time bound over random coins" means worst-case over inputs, time bound T(n) that holds (and this bound is achieved considering random coins?) - garbled. Or if it means expected time bound? "Worst-case time bound over..." doesn't match expectation. Or perhaps it means the time bound is worst-case (over inputs) and holds with high probability over random coins? That would be Monte Carlo with zero error? No, Monte Carlo allows error; zero error with bounded time is not possible for nontrivial problems without solving them.

Alternatively maybe they mean: a zero-error randomized algorithm where the time bound is worst-case over inputs (not average-case), and randomness is over coins. That is exactly Las Vegas - worst-case over inputs, zero error, expected time over coins. That fits if "worst-case time bound" refers to worst case over inputs, and "over random coins" is misplaced. Or maybe "with zero error, worst-case time bound, over random coins" - three things. This is ambiguous. But let us look up the full question again very carefully.

Let us read more about the state graph and algorithms to understand if randomization could help.

Let us start by exploring the codebase to understand the full picture.

Let us start by exploring the problem deeply.

Let us report our findings.


I studied AGENTS.md, docs/problem.md, board #301 (via board_digest), primary literature (budgeted DFS, winning frontier barrier, one-ply obstruction, time-exponent), and the codebase. The question reduces to a model ambiguity: if "worst-case time bound over random coins" means bounded Las Vegas, randomization is equivalent to deterministic (trivial derandomization); if expected Las Vegas, it's nontrivial but phrasing is odd.

Key findings:
- Deterministic budgeted DFS gives 2^(O(n log^2 n)); winning frontier barrier shows large families (>=2^((1/4-o(1)) n log^2 n) states) obstructing frontier-enumeration methods but explicitly does NOT exclude selective minimax/proof-number/search with better pruning.
- Saks-Wigderson gives AND-OR tree evaluation improvements, but translating to AND-OR tree search with adversarial adversary and poset structure is unclear; exponent-level improvement to 2^(o(n log^2 n)) not obvious.
- One-ply pruning and symmetries give local improvements but don't obviously change the exponential exponent class.

Obstructions/failed approaches: randomized pair ordering unlikely to help against adversarial inputs where winning moves are sparse; randomized canonical labeling has exactness issues. No known construction achieves 2^(o(n log^2 n)), and a general lower bound would cross into discouraged territory (unconditional super-polynomial lower bounds for unary language implying P!=PSPACE). The question remains open - the critical missing piece would be a barrier ruling out selective randomized search, which is not established by existing results.

## Other metadata

```json
{
  "finished_at": 1793417699.8943458,
  "started_at": 1793414023.2702055
}
```
