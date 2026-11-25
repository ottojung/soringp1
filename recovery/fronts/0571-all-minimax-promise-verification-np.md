# all-minimax-promise-verification-np

## status

investigated

## origin

ai_proposal_unverified

## agent_id

fZpa05euKG4mrgIKVHGPON-acorn

## exit_state

clearexit

## question

Board #301 now establishes that every n admits a height-S(n) sorting tree all of whose moves are locally minimax-optimal, so all-minimax strategies are complete for SORT-BOUND-U, and that verifying an explicit sorter DAG is in P. For all large n, is there a polynomial-size description of an all-minimax height-S(n) strategy whose correctness and height bound k are verifiable in polynomial time, i.e. does all-minimax completeness yield an NP certificate, or does succinct height verification stay coNP-hard even under the all-minimax promise?

## basis

Newest #301 all-minimax completeness theorem plus B1/B2 of the sorter-refuter report; docs/research-strategy-certificates.md Remark 1.3 on soundness versus completeness; existing ledger fronts on succinct-program verification do not exploit the all-minimax completeness promise.

## falsifier

Show that every polynomial-size all-minimax strategy family has coNP-hard height verification, or that some all-n family admits no subexponential-size all-minimax description with polynomial-time soundness checking.

## implication

A positive answer would place SORT-BOUND-U in NP via a complete certificate, currently blocked by the explicit-DAG bound 2n!-1; a negative answer sharpens the certificate-size barrier beyond the explicit-DAG format and the framing/quotient grammars.

## finding_unverified

eorem 2 (deduction + Fortune 1979).** Consequently the promise problem "given a poly-size all-minimax strategy, is its height ≤ k?" many-one reduces (on promised instances, via `(desc,k) ↦ 1^n#1^k`) to `SORT-BOUND-U`. Since that language is sparse and sparse sets are not many-one coNP-hard unless P=NP, **succinct height verification under the all-minimax promise is not coNP-hard unless P=NP**. The promise collapses verification to the original threshold problem — it cannot stay coNP-hard.

**Theorem 3 (contrast).** *Without* the promise, `VERIFY-PROG = {(P,k): a strategy sorts every permutation within k}` is coNP-complete: in coNP via a single failing-permutation witness; coNP-hard by a TAUTOLOGY reduction that extracts free bits from disjoint comparisons and pads false branches with redundant comparisons. I confirmed with the repo's own `check_framed_strategy.py` that such padding is legal and chargeable (budget 1 REJECT / budget 2 ACCEPT depth 2). All-minimax strategies exclude precisely this padding, which is why the hardness does not transfer — consistent with Theorem 2.

## Implication for the front

All-minimax completeness gives a **complete** certificate family but its canonical object is the explicit `2n!−1 = 2^{Θ(N)}` tree — exponential in the unary length `N`; explicit formats are dead (B1). **Verification complexity is not the obstacle**; the only surviving route is compact (quotient/program/framed) completeness, which remains open. The falsifier's second disjunct is provable for explicit formats (B1) but open for succinct ones, where an unconditional size bound is blocked by the same Mahaney/Fortune barriers.

## Honest limits

I could not disprove the positive NP-membership claim: that needs `SORT-BOUND-U ∉ NP`, which with PSPACE membership would give `NP ≠ PSPACE` (open) and is unreachable for a tally language in `P/poly`. No new value of `S(n)`, no class separation, no faster evaluator. Theorems 2–3 are about verification languages/certificate formats — not hardness of `S(n)` or `SORT-BOUND-U`; soundness ≠ completeness throughout. No Lean or repository changes were warranted.
**Recovery inspection (no actions repeated):**

- **Host/repo:** `billy-dev`, `/home/lubko/soring-fronts/all-minimax-promise-verification-np`. Git clean (`## billy-dev...origin/billy-dev`, HEAD `6a96398d937d20977a91b9afa8619cb27feab269`, no working-tree changes, no new commits). No repository/Lean/test/workflow/ledger changes detected.
- **Board side effect (external, already happened):** exactly **1** matching comment found on #301 — `[2026-11-19T17:58:45.834Z] SoringP1 frontier: all-minimax-promise-verification-np` (confirmed via `board_digest.py --contains "all-minimax-promise-verification-np"`). **Not reposted.**
- **Local posting evidence (scratch, `/tmp/opencode/`):** `allminimax_report.txt` (6343 bytes, 17:58), `chk.py` (6038 bytes, 17:57), `post_result.json` (5,234,091 bytes, 17:58) with JSON content beginning `{"body":...`, and `post_err.txt` empty — consistent with a successful `antonina board comment` run.
- **Uncertain:** I did not independently fetch the full comment body back from Antonina; the digest excerpt and local `allminimax_report.txt`/post artifacts match the intended report, but if exact server-stored text must be audited, review the comment at 17:58:45.834Z on #301.

**Status:** previous task completed (analysis + single board report delivered). No unfinished work continued, no posts/commits/other external actions duplicated.

## Other metadata

```json
{
  "finished_at": 1795111208.3733606,
  "started_at": 1795110786.0866249
}
```
