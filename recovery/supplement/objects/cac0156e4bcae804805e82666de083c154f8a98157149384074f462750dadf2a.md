# Executive SoringP1 referee pass — bias-path-worstcase-sergeev (2026-11-23 ~06:25Z)

**Office:** executive, independent delivery on billy-dev; NOT a parliamentary sitting and NOT Clerk intake.
**No theorem completion** is claimed for S(n) or SORT-BOUND-U. No repo/Lean/test/CI/ledger/canonical-main/bill/ballot change by this record.
**External writes:** one #301 referee-disposition comment (`sha256:8DwQa-zG…`, 06:25:32Z) and this durable record.

## Trigger

Fresh dispatch after my 06:16Z referee pass (delivered as `soringp1-pass-0608`→`22b1033` earlier and
`referee-0616`→`b485da47`). Durable state re-verified: worktree AGENTS.md, `government/executive-agenda.md`,
`antonina-interface.md`, #301 page 1, frontier ledger (708 fronts; running count in prompt was stale),
and live agent list. Operational state unchanged and clear: no live obligations, no open corrective cases,
empty judiciary mailbox, no unsafe holds, founder-inbox cursors fresh. `bias-path-worstcase-sergeev-alln`
finished at 06:18:54Z (result posted just after my 06:17Z disposition) with no referee disposition; three
researchers remain running (`prime-defect-persistence`, `structural-bound-allornothing`,
`framed-dag-n12-explicit-construction`) and were preserved.

## Referee disposition: `bias-path-worstcase-sergeev-alln`

**Accept the honest inconclusive verdict; independently confirm the two positive claims.** FRONT (every
optimal tree has o(n) delta-biased comparisons on EVERY root-to-leaf path) not proved; falsifier not
exhibited. Verdict: honest inconclusive with a genuine partial theorem and a sound method obstruction.

Independent evidence I produced (own computation, not the reporter's artifacts):
- Reconstructed correct comparison trees by brute force and verified the per-path identity on every leaf
  for n=3/4/5 (6/24/120 leaves): product of conditional outcome probabilities = 1/n! exactly (max error
  1.7e-18) and sum log2(2 p_i) = D - log2(n!) to machine precision (max error 2.8e-16). The identity holds.
- Verified the partial-positive mechanism: on the "always take >=1/2 child" path every log2(2 p_i)>=0 and
  a delta-biased edge contributes >= a=log2(1+2delta), so biased_count * a <= D - log2(n!) on that path.
  Own trees: n=4,delta=0.2 biased=1 (0.485<=1.415); n=5 biased=3 (1.456<=3.093). With D<=S(n)=log2(n!)+o(n),
  the majority path has <=o(n)/a biased comparisons in every height-S(n) tree — "exists a good path" holds,
  "all paths" does not follow. Reporter states this distinction correctly.
- The exact obstruction (virtual path profile satisfying Kraft/per-path/expectation identities yet forcing
  omega(n) bias; #biased <= (Delta+R)(1/a+1/b)) is a sound explanation that aggregate accounting alone
  cannot settle either horn; the missing ingredient is realizability by an actual poset decision tree.
- Literature premise consistent with the same-day source audit: Sergeev ECCC TR20-096 Thm 3 is a total-count
  bound with no per-path bias theorem and is ineffective. The structural question is new relative to it.

Limitations preserved: no counterexample family, no forcing lemma bounding worst-path minority Kraft surplus
R; small-n non-invariance (n=6) motivates but cannot decide the asymptotic; nothing Lean-checked.

## No new front this pass

Three researchers remain live on distinct fronts plus curator fronts and the recent completed results,
covering the open questions in `docs/research-plan.md`. The Founder forbids filler and repeat work; no agent
was steered, stopped or duplicated, and no research dispatch was made this pass.

S(n) and SORT-BOUND-U remain OPEN. No case closure, legislative action, or Founder decision is implied.
