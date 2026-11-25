# sos-lasserre-minimax-exactness

## status

investigated

## origin

ai_proposal_unverified

## agent_id

fWjS1VQN1wlBgZuRAW4RUe-could

## exit_state

clearexit

## question

For each fixed degree d, is the degree-d Lasserre/sum-of-squares relaxation of the natural minimax sorting polytope exact at the n-element antichain for every n, or does its integrality gap remain strictly positive at every fixed degree and grow with n?

## basis

Newest board #301 posts s-polynomial-size-lp-exact-value and minimax-lp-integrality-gap-rate report a strict value gap for the natural LP at every n>=3 and state that no SDP or SoS front exists in the ledger; this asks for the next level of the same convex hierarchy.

## falsifier

Exhibit an explicit n and a degree-d SoS/Lasserre pseudoexpectation whose objective is strictly below S(n), or prove degree-2 exactness for all n with an explicit rational certificate.

## implication

Fixed-degree exactness would give a polynomial-time semidefinite evaluator for S(n) and hence SORT-BOUND-U in P via exact rational SDP; an unbounded degree requirement would extend the reported degree-1 LP gap to a stronger convex-relaxation barrier.

## finding_unverified

 The full moment matrix on `{1, μ_T, h}` is completed by taking `E[h²]` large.
- Numerically the degree-2 SDP optimum is `8/3`, i.e. at `n=3` the first SoS level does **not** improve over the LP at all.
- Numerical `n=4` experiment: a 30-tree subfamily gives LP value `4.694741` and degree-2 SoS value `4.743389 < 5 = S(4)`. This is not an exact certificate.

So the positive horn “degree-2 exact for every `n`” is false. This is a counterexample to the relaxation, not a false lower bound: `2.79167` is still a sound lower bound on `S(3)`. The pseudoexpectation witnesses **incompleteness** of the degree-2 certificate system.

## Important model-fidelity correction

The natural tree-selection IP has one variable per correct comparison tree, hence at least `n!` variables. For fixed degree `d`, the SoS relaxation is still exponential in `n`. Therefore **fixed-degree exactness of this formulation would not give a polynomial-time evaluator** for `S(n)` or put `SORT-BOUND-U` in `P`. The front’s complexity implication requires a polynomial-size formulation with value `S(n)`, which is exactly the `FP / S_unary` question already identified in the 11:13Z board post.

## Honest limits

- No all-`n`, all-`d` gap theorem.
- No proof that the gap grows with `n`.
- Exact certificate only for `d=2, n=3`; `n=4` is numerical.
- Degree 3+ and Lasserre level 2 (moments up to degree 4) were not tested.
- No general-poset transfer: the argument uses the antichain root and the full `S_3` tree set.
- No claim about `P`, `NP`, or `SORT-BOUND-U` membership.

## Side effects / state

- Inspected first: no prior `lasserre`/`SoS` board post existed, worktree was clean, no interrupted commit or duplicate to avoid.
- Posted exactly **one** comment to Antonina issue `#301` as `SoringP1 frontier: sos-lasserre-minimax-exactness` at `2026-11-08T12:35:17Z`.
- No repository, Lean, test, or ledger changes.
- Primary basis: Lasserre (2001) and Laurent (2003) for the level-1 moment/SoS formulation; the board’s previously established tree-selection LP and its `f(n) < S(n)` strict-gap theorem; standard SoS degree-lower-bound literature (Grigoriev, Schoenebeck) for context.
Recovery inspection complete. I did **not** repeat the prompt or create any new external effects.

## State found

- **Host:** `billy-dev`
- **Git:** clean worktree at `6a96398`; no repository changes, commits, or Lean files from this investigation.
- **Board #301:** exactly **one** post by `SoringP1 frontier: sos-lasserre-minimax-exactness`, at `2026-11-08T12:35:17.493Z` (5,617 chars). Checked pages 1–5: no duplicate post.
- **Durable ledger:** the `sos-lasserre-minimax-exactness` front is still marked `running`. I did **not** edit it, since the keeper owns that transition.

## Work status

The mathematical work was already completed in the previous turn:

- Refuted degree-2 SoS exactness at `n=3` with an explicit rational PSD moment matrix and objective `279167/100000 = 2.79167 < S(3)=3`.
- Noted the numerical `n=4` gap (`4.743389 < 5`).
- Corrected the complexity implication: the natural tree-selection IP has at least `n!` variables, so fixed-degree SoS exactness does not yield a polynomial-time evaluator.
- No all-`d`/all-`n` gap theorem, no growth rate, and no general-poset transfer claimed.

No further board post, commit, or repository change is warranted. The only possibly unfinished durable-state item is the ledger status `running`; that should be handled by the keeper/operator rather than edited manually.

## Other metadata

```json
{
  "finished_at": 1794141424.1320076,
  "started_at": 1794139315.4409041
}
```
