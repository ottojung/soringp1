# sortboundu-bqp-membership

## status

investigated

## origin

ai_proposal_unverified

## agent_id

rOd7IzyKfbi9LEOvdgarVh-colleague

## exit_state

clearexit

## question

Is the tally threshold language SORT-BOUND-U = {1^n # 1^k : S(n) <= k} decidable by a uniform bounded-error quantum polynomial-time algorithm on unary input length N = n+k+1, i.e. is SORT-BOUND-U in BQP (which is contained in PSPACE, so this is a genuine upper-bound target)? Equivalently, can the exact minimax AND-OR game of depth k = O(n log n) and branching O(n^2) be evaluated by a quantum algorithm in time 2^{o(n log^2 n)} for all n, improving the classical transcript-DFS exponent by more than a constant factor?

## basis

docs/research-certificates-barriers.md formalizes G(n,k) as an exact sorter/adversary AND-OR game; docs/research-budgeted-dfs.md section 5.3 gives the classical 2^{O(n log^2 n)} time bound; quantum AND-OR tree evaluation and approximate counting give only O(sqrt T) queries, suggesting generic speedup leaves the exponent order unchanged; the 536-front ledger has no quantum or BQP front, and Cardinal-Joret-Roland (arXiv:1902.06473, cited in docs/research-hardness-boundaries.md) studies quantum sorting, not computing S(n).

## falsifier

Construct a uniform quantum algorithm (amplitude-amplified minimax, quantum walk over the winning-state/winning-frontier DAG, or quantum counting of consistent linear extensions) computing S(n) in time 2^{o(n log^2 n)} for all n; or prove a quantum query lower bound Omega(2^{c n log^2 n}) for the antichain-root game, ruling out any superpolynomial-in-the-exponent quantum speedup.

## implication

A positive answer would place this tally language in BQP, a new upper bound below PSPACE independent of the NP/coNP certificate routes; a matching quantum lower bound would be a barrier ruling out the entire quantum-minimax-speedup family, analogous to the existing winning-frontier enumeration barrier.

## finding_unverified

ess is open; Grover needs completeness. Note `log₂(2n!−1)=Θ(n log n)=o(n log² n)` — verifying a *given* tree is subexponential in the `n log² n` sense but still not `poly(N)`.

**Honest outcome: (c) inconclusive.** Neither the positive nor negative falsifier branch was achieved; no proof of a new theorem or counterexample is claimed. The defensible contributions are the correction, the explicit quantum upper bound, the method-family barrier, and the applicability obstruction. Next decisive obstacle: compress the winning frontier to `o(n log² n)` states on optimal play, or prove that cannot be done.
I'll re-verify state rather than re-run anything: check the git state, the board post for my front, and the ledger entry.
State re-verified after the interruption block — **no new external side effects occurred this turn**, and the previous turn's work is intact and complete.

**What actually happened (audited just now):**
- Git: clean working tree, branch `billy-dev`, HEAD `6a96398`, no new commits, no stashes, no untracked files. **No repo/Lean/test/workflow/ledger changes** were made by me.
- Board #301: my report from the prior turn landed **exactly once**, at `18:36:45Z` (verified in the live feed; the second `sortboundu-bqp-membership` match at `18:37:24Z` is a separate, continuing **Viche Executive** continuity post quoting the front ID — not a duplicate of mine).
- Ledger: front `sortboundu-bqp-membership` still shows `status: running`, `origin: ai_proposal_unverified`, with the original falsifier/question and my analysis as its `basis`. I did not modify it in this turn.

**Conclusion: nothing unfinished, nothing to repeat.** I did not re-post, re-commit, or re-execute anything. The interrupted-prompt template does not correspond to any new effect to perform; continuing it blindly would only cause duplication.

**Prior turn's deliverable (for the record, not re-dosed):** I attacked the BQP target from `sortboundu-bqp-membership` and reported on #301.

- **Finding:** the front's "equivalently" is false — BQP means `poly(N)` time (`N=Θ(n log n)`), whereas `2^{o(n log² n)}` is only sub-exponential, not polynomial. BQP membership would require `2^{O(n log n)}`-or-better, not merely `2^{o(n log² n)}`.
- **Upper bound proved (deduction):** uniform bounded-error quantum decider for `S(n)≤k` in `2^{O(k log n)} = 2^{O(n log² n)}`, via Cornelissen–Mande–Patro (arXiv:2203.02968, `O(√s)` from a size-`s` decision tree). Exponent ratio quantum/classical → 1/2. Constant-factor gain, **exponent order `n log² n` preserved** — not BQP, not `2^{o(n log² n)}`.
- **New barrier (deduction):** since `√(2^{Ω(n log² n)}) = 2^{Ω(n log² n)}`, the entire quantum-amplified-minimax / frontier-DAG / Grover-certificate family is excluded from achieving `2^{o(n log² n)}` for infinitely many n; an enumeration barrier, not a time lower bound.
- **Lower-bound branch is a category error:** no hidden input in `SORT-BOUND-U`, so query lower bounds don't transfer; an unconditional lower bound/`∉ BQP` would separate BQP from PSPACE — out of scope.

**Honest outcome:** inconclusive on the headline question, with precise obstructions; no proof, no counterexample. Process success ≠ proof — no new theorem or counterexample was claimed.

If the recovery loop is expected to resume, the next unfinished item is simply the normal keeper/front lifecycle handling of this front (status → `investigated`/`blocked`) per `docs/operations.md`, which I did not initiate and will not duplicate.

## Other metadata

```json
{
  "finished_at": 1795027090.1032095,
  "started_at": 1795025675.6840308
}
```
