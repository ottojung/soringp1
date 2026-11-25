# Executive SoringP1 referee pass — three fresh results (2026-11-23 ~06:16Z)

**Office:** executive, independent delivery on billy-dev; NOT a parliamentary sitting and NOT Clerk intake.
**No theorem completion** is claimed for S(n) or SORT-BOUND-U. No repo/Lean/test/CI/ledger/canonical-main/bill/ballot change by this record.
**External writes:** one #301 referee-disposition comment and this durable record.

## Trigger

Fresh session. Durable state verified before acting: authoritative Constitution,
`government/executive-agenda.md`, `government/antonina-interface.md`, worktree AGENTS.md,
the predecessor's delivered pass record `2026-11-23-executive-soringp1-pass-0608.md`
(delivery `soringp1-pass-0608-20261123` landed on main as `22b103307ed35d0b90ba252c3fa16af4a8abfdb7`),
the frontier ledger (708 fronts), #301 page 1, and live agent list. No live obligations, no open
corrective cases, judiciary mailbox empty, no unsafe holds, all proceed requests addressed to
executive answered, founder-inbox cursors fresh. Four researchers remain running and were preserved.

Three result comments posted on #301 at 06:12–06:13Z, after the predecessor's 06:10Z pass, had no
executive referee disposition. This pass referees them.

## Referee dispositions

1. **`winning-frontier-uniform-alln`** (result 06:12:33Z, author claim (a) "FRONT TRUE, falsifier refuted").
   **Independently confirmed as established, with the author's caveats.** I checked the claim against the
   dated primary doc `/home/lubko/soring301/docs/research-winning-frontier-barrier.md` at HEAD `6a96398`:
   its construction is explicitly restricted to `s=L=2^r`, `n=s^2` (line 109), so the all-sufficiently-large-n
   generalization is genuinely new relative to the documented barrier. I re-derived the parameter arithmetic:
   `s=ceil(sqrt n)`, `t0=n-s`, `B=(s-1)+(n-1)ceil(log2 s) ~= (1/2)n log2 n`,
   `m=S(n)-t0-B ~= (1/2)n log2 n`, `M=Theta(n^{3/2})`, so `log2 C(M,m) ~= m log2(M/m) =
   (1/4)n log2^2 n - O(n log n loglog n)`, while `log2 n! = n log2 n - O(n)` is lower order — giving
   `(1/4-o(1)) n log2^2 n`. The explicit effective threshold (~500) and the honest notation limit
   (n log^2 n = n^{1+o(1)}, not literally n^{1+Omega(1)}) are correctly flagged. It is an enumeration
   barrier only — not a time/space lower bound and not a certificate completeness result — exactly as
   stated. Verdict: accept as a modest genuine strengthening of an existing barrier; it does not touch
   the final theorem.

2. **`lin-ext-oracle-turing-placement-alln`** (result 06:12:33Z, claim (c) honest inconclusive).
   **Accept the inconclusive verdict and the duplicate finding.** I independently verified in the
   authoritative frontier ledger that `uniform-polytime-e-oracle-s-reduction-bridge` exists with status
   `investigated`, `exit_state=clearexit`, recording essentially the same adaptive-derived-poset e-oracle
   question. This corrects my predecessor's 06:10Z commissioning note, which called this front "genuinely
   untried" and named only two *blocked* fronts as nearest — that novelty assessment was wrong. The front
   correctly stopped rather than duplicate completed work. No theorem implications; question stays open.

3. **`gap-two-smt-reattack-alln`** (result 06:13:25Z, claim (c) honest inconclusive).
   **Accept the inconclusive verdict.** The author's stated limits are sound: the exact minimax evaluator
   independently reproduces only n<=8 (literature already knows n<=22), the Z3 strategy-existence encoding
   is validated only to n=5 at the UNSAT boundary, and the n=23 encoding-size count (~3.9e45 reach variables)
   is a genuine obstruction. The OEIS A036604 sequence and `D(n) in {0,1}` for n<=22 are consistent with the
   known record; no gap-2 witness and no stronger-than-information lower bound was produced.
   "Gap at most one" remains a conjecture, neither proved nor refuted.

## No new front this pass

Four researchers are running on distinct fronts (`bias-path-worstcase-sergeev-alln`,
`prime-defect-persistence-alln`, `structural-bound-allornothing-alln`,
`framed-dag-n12-explicit-construction-alln`) plus curator fronts, and the three just-completed results
above. These already cover the open questions in `docs/research-plan.md` (shrinking exponent, framed-DAG
certificates, space, effective Sergeev / bound gap, descriptive complexity). The standing Founder priority
forbids filler and repeat work; a fifth front here would be manufactured, and the predecessor's one new
front this cycle was itself a duplicate. Research agents were not steered, stopped, or duplicated.

S(n) and SORT-BOUND-U remain OPEN. No case closure, legislative action, or Founder decision is implied.
