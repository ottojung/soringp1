# antonina-TQRiPLiniuS1NhA8B24H7n-allowed

Session: ses_e4253920dffeuTxAVxyLuBzn4I
Workspace: /home/lubko/soring-fronts/multi-chain-merge-exact-complexity
Created: 1794183556654; updated: 1794185885134

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 484 (msg_1bdceadc10019uLEqEN9t5uPtP)

On **billy-dev**, worktree clean at `6a96398`. I studied `AGENTS.md`, `docs/problem.md`, the current board #301 context, the two-chain prior front, and the accessible primary material (Hwang–Lin 1972, Hwang 1980, Li–Sun–Zhang ISAAC 2016 abstract). I posted the result to Antonina issue #301. No repository or Lean changes were made.

## Verdict

The front remains open: I found neither a polynomial-time exact algorithm for all multi-chain tuples nor an infinite family with a super-polynomial lower bound under a uniform model. What I did establish is a precise barrier to the variable-`k` interpretation and two finite counterexamples that eliminate natural compositional routes.

## Mathematical findings

**1. For variable `k`, the front contains exact `S(n)` [paper proof].**  
Take the tuple `(1,1,...,1)` with `k=n` chains. Its disjoint union is the antichain `A_n`, so the exact multi-chain merge number is exactly `S(n)`. Therefore a polynomial algorithm for all tuples with variable `k>=3` would give `S_unary ∈ FP`, hence `SORT-BOUND-U ∈ P`. This is not a disproof—the front could only be true by solving a major open problem—but it shows the front is not an intermediate target under that reading.

For fixed `k`, that reduction does not apply. Fixed `k=3` already contains the family `(m,1,1)=C_m ⊔ A_2`, for which no closed form is known.

**2. Exact two-chain values are sound but not compositionally complete [exact finite computation].**  
Let `B` be the minimum over binary merge trees of the sum of exact two-chain merge numbers. Every such tree is a valid strategy, so `F <= B` is sound. But at `(2,2,2)`:

- `B = M(2,2) + M(4,2) = 3 + 5 = 8`
- exact minimax gives `F(2,2,2) = 7`
- the information bound is also `7`.

So the three-way merge is information-tight, while every binary composition loses one comparison. Current `k=2` exact results cannot be composed to solve `k>=3`; genuine joint interleaving is required. This is a concrete soundness/completeness gap for the natural pairwise-merge certificate family.

**3. The tempting singleton reduction fails [exact finite computation].**  
For many small pairs, `F(C_a ⊔ C_b ⊔ C_1) = M(a,b)+3`, suggesting a reduction from two-chain to three-chain. It is false:

- `(3,6,1)`: exact `F = 11`, but `M(3,6)+3 = 10`; information bound `10`.
- `(5,5,1)`: exact `F = 13`, but `M(5,5)+3 = 12`; information bound `12`.

In both cases the exact value is `info+1`, so neither `M+constant` nor `max(M+3, info)` is complete.

All reported exact values were checked by two independent minimax implementations with different state encodings. These are finite experiments, not a proof of a complexity lower bound.

## Honest limits

- No polynomial algorithm was found.
- No unconditional super-polynomial lower bound was obtained; for variable `k` this would imply a breakthrough on computing `S(n)`.
- No primary source resolving the computational complexity of exact adaptive multi-list merging was found. Parallel multiway-merging literature concerns a different model and was not imported.
- General-poset hardness was not used; it does not transfer to chain unions.
- The decisive next step remains either a genuine joint multiway algorithm with correctness and cost proof, or a hardness family. The `(2,2,2)` example shows any candidate must be truly multiway; the all-ones tuple shows the variable-`k` version cannot be easier than exact `S(n)`.

## Output 586 (msg_1bdcfbdda001BE9kTyu5NCsBfX)

On **billy-dev**, current working directory unchanged at `/home/lubko/soring-fronts/multi-chain-merge-exact-complexity`, git worktree clean at `6a96398`.

## External actions already performed (verified)
- **One** board post to Antonina issue #301 at `2026-11-09T00:56:48.076Z`, author `SoringP1 frontier: multi-chain-merge-exact-complexity`  
  - Present as a single unique message on page 1; checked page 2 for duplicates (none found).
  - Body is complete, including the all-ones-tuple reduction, the `(2,2,2)` binary-composition counterexample, `(3,6,1)` and `(5,5,1)` singleton-reduction counterexamples, results summary, and honest limits.
- Result file `/tmp/opencode/mcm/post_result.json` is the response from that single comment.

No commits, PRs, file edits in the repository, or other external actions were performed. Worktree clean.

## Durable task records
- Antonina issue #301 remains open as expected for ongoing project tracking.
- The research front in `/home/lubko/.local/state/soringp1/frontier-ledger.json` is still `running` with our agent ID (`TQRiPLiniuS1NhA8B24H7n-allowed`) and no recorded finding yet. That is normal: the keeper marks a front `investigated`/`blocked` from the agent's exit state, not immediately after a board comment, and is not something I should hand-edit.

## Unfinished work
None remaining.

## Other observations (for review, not action)
- Another unrelated process (`fmini` executing in `/tmp` under a different front, PID 21065) is active on billy-dev. I did not start or alter it.
- All new local artifacts—exact chain-merge computations and the board post text—live only under `/tmp/opencode/mcm/`; nothing was written into the repository.

## Summary of the mathematical result already posted
Short version of the completed front:
- **No** polynomial-time exact algorithm found, and no super-polynomial family proven.
- Precise barrier: the all-ones tuple `(1,1,...,1)` reduces exact `S(n)` polynomially to a variable-`k` multi-chain merge.
- Concrete counterexample: `F(2,2,2)=7` while any binary composition of exact two-chain merge numbers costs at least `8`, showing pairwise-merge certificates are sound but not complete.
- Failed reduction: a syntactically augmenting two-chain→three-chain law like `F(a,b,1)=M(a,b)+3` is false; counterexamples at `(3,6,1)` and `(5,5,1)`, where the exact value is `info+1`, not `M(a,b)+constant`.

All finite computations are explicitly labeled as finite exact calculations, not a lower-bound theorem.
