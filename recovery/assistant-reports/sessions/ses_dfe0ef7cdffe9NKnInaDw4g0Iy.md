# antonina-UyQSJ4FJ9C3tHILLnem1BQ-susan

Session: ses_dfe0ef7cdffe9NKnInaDw4g0Iy
Workspace: /home/lubko/soring-fronts/parallel-composition-all-inversion-alln
Created: 1795328903417; updated: 1795330654425

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 13 (msg_201f8755a001wOMXxHLrKzYcsO)

I'll start by inspecting the current state carefully — git status, the key docs, and any durable task records — before deciding what work remains.

## Output 24 (msg_201f87ee6001OQbMi0PoPofFId)

Clean worktree on `billy-dev`. Let me study the key documents and find board #301 and any prior work records.

## Output 35 (msg_201f889df001jDz2DHfVVZiAF3)

Let me read the core problem doc, operations, and locate "board #301" and the "all-inversion"/"Claim C" concepts.

## Output 54 (msg_201f89dce0012ftiTATxLeoQ11)

Let me read the board digest (board #301) and check durable task records / ledger state.

## Output 65 (msg_201f8adbd001xmqvH2YogSjA3M)

I need the full text of the ordinal-sum propagation post to understand the exact definitions. Let me pull it.

## Output 85 (msg_201f8d1b00015GCjI1fvcwW5ZS)

Let me fetch the full body of the ordinal-sum propagation post via a scratch script.

## Output 96 (msg_201f8e431001RMtn7mBvb1Ljq8)

I now understand the model. Let me check prior scratch work to reuse code and avoid duplicating side effects.

## Output 107 (msg_201f9a0c4001CgfRN5c8RWz1Xp)

There's prior scratch work on this exact front. Let me inspect it and check whether a board post was already made.

## Output 122 (msg_201f9b24e001V1ccc3da65WGE0)

Let me check whether this front already posted to the board and whether prior scratch produced output.

## Output 158 (msg_201fa0c290011i2AlygFe6zwap)

No board post from this front and ledger status is `running` with no finding — so the work is unfinished. The scratch scripts were created but never produced output. Let me establish a baseline by running them (with time caps).

## Output 169 (msg_201fa64b8001iyBhPGYBtrMaYq)

Let me understand "Claim C" precisely — there may be multiple notions.

## Output 180 (msg_201fa7b23001ckgs6MD7vZW4Sk)

The doc's "Claim C" is about succinct certificates. The inversion fronts reference a different "Claim C" — let me read the sibling front's post.

## Output 191 (msg_201fa8cb2001eGzsrQwinPCr7u)

I now understand the full theory. Key observation: since no all-inverted poset exists through n=9 (Claim C open), the parallel-composition equivalence is **vacuously true** if Claim C holds, and any falsifier would refute Claim C. Let me do a rigorous local analysis to find where parallel composition genuinely differs from ordinal sum. First, let me verify the n=6 cross-comparison inversion witness and study local transfer.

## Output 209 (msg_201fd2406001eKZ2UtZg93Eya2)

Let me rerun with a larger tool timeout.

## Output 227 (msg_20204a4320014tnmI8jkMaVFye)

The computation was killed (memory blowup) alongside the backend failure notice. Let me re-audit state — no external side effects should be repeated — then run a much leaner, targeted computation.

## Output 238 (msg_20205413a001Hpnaj4kg5jLzZG)

State is clean; no board post from this front. The partial output confirmed a key fact: **cross comparisons in a disjoint union can be inversions** (witness `W = {0} || Q`, pair (0,3)). Now let me run a lean, memory-bounded set of experiments.

## Output 290 (msg_2020a79c8001Kg3CV4dW4nKv8U)

The lean experiments are decisive. Key findings:

- **Forced-tie lemma** verified (20/20 symmetric cross pairs in `A||A` are ties, 0 inversions) — and it has a clean automorphism proof.
- **All 20 symmetric cross pairs are optimal** in `A||A` for `|A|≤3`, so `A||A` is never all-inverted there.
- **Cross-comparison inversions exist** in disjoint unions (witness `W`).
- **m-order preservation**: 0 reversals in 66 tests — a failed local approach, not a proof.

Let me confirm the posting mechanism before writing the single board report.

## Output 308 (msg_2020b35d0001dhRNAbk4UKICPy)

Let me write the board report to a file and post it once.

## Output 328 (msg_2020b8a0f001kbR9AwdM8gUl3J)

Post succeeded. Let me verify it landed exactly once and that no repo changes occurred.

## Output 339 (msg_2020ba0530013mkAK7S2sLRDyA)

Done. Here is the honest outcome of this front.

## Mathematical finding

**1. Exact obstruction (deduction).** The front's equivalence
`allinv(A‖B) = allinv(A) ∧ allinv(B)` is *hostage to the open Claim C* (the sibling fronts' conjecture that every poset with `m≥2` has a non-inverted optimal comparison):
- If Claim C holds, `allinv` is empty everywhere → both sides always false → the equivalence is **vacuously true**.
- Every possible falsifier exhibits an all-inverted poset (either `A‖B`, or `A` and `B`) → it **refutes Claim C**.

So the front cannot be settled without settling Claim C (verified only through n=9). Consequently the advertised complexity payoff is blocked: Gallai modular decomposition would still need the all-inversion status of each prime node, i.e. exact `m`, `e` and the optimal-pair set — the PSPACE-level minimax game plus #P-hard counting. This is a *soundness-only* general-poset observation, not a completeness/complexity theorem.

**2. Unconditional structural theorem (paper proof).** If a poset `P` has an automorphism `σ` swapping an incomparable pair `p=(x,y)`, then `σ` is an isomorphism `P+xy ≅ P+yx`, so `p` is a **forced tie, never an inversion**. Applied to `A‖B` with `A≅B`, every diagonal cross pair `(a, φ(a))` is a forced tie. Thus parallel composition has a concrete mechanism to *destroy* all-inversion that ordinal sums lack (where every optimal comparison is within-block). Verified exhaustively for all unlabeled `A` with `|A|≤3`: 20/20 diagonal pairs are forced ties (0 inversions) **and all 20 are optimal**, so `A‖A` is never all-inverted in that range. A falsifier follows *if* an all-inverted `A` with a diagonal optimal cross pair exists — none is known.

**3. Concrete cross-comparison inversion (experiment).** `W=(0,0,2,2,6,14) = {0} ‖ Q` (n=6) has an optimal cross-block pair `(0,3)` whose hard child has `e=14 < 16`. This refutes the naive analogue of the ordinal-sum theorem's property (i) for disjoint unions: parallel composition admits both optimal cross comparisons and cross-comparison inversions. `W` is not all-inverted (1 of 8 optimal pairs).

## Concrete failed approach / exact limit

I tried to lift a non-inverted optimal pair from `A` to `A‖B` to prove the create direction. Extension-count order *is* preserved (both children scale by `binom(a+b,a)·e(B)`), but minimax order need not be (ordinal sum has `m` additive; parallel composition does not). An exhaustive check of 66 within-block comparisons found 0 m-order reversals and 0 tie-breaks — so no small witness and no proof either way; and even preservation wouldn't guarantee optimality at `A‖B`. General optimality of diagonal cross pairs needs `m` at `|A|=4` unions (A001035(8) = 431,723,379 states) and is infeasible; one such run was killed by the backend failure with no side effects.

## Honest limits / S(n)

All findings are general-poset structural facts. No all-inverted poset exhibited, no Claim C progress, no new `S(n)` bound, no placement of `SORT-BOUND-U` below PSPACE, and no evaluator pruning invariant (`e` is #P-complete; finding optimal pairs *is* the minimax game). The front is **not** resolved — its only possible falsifiers refute the open Claim C.

**Effect audit:** worktree clean at `6a96398` on `billy-dev`; no Lean/repo/test/CI/ledger changes; scratch files only in `/tmp/opencode`; exactly one board #301 post landed (06:57Z), after confirming none from this front existed beforehand. Nothing duplicated.
