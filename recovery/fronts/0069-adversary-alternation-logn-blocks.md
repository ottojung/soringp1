# adversary-alternation-logn-blocks

## status

investigated

## origin

ai_proposal_unverified

## agent_id

gSn4p9uRiokNl6b3eUyd3K-crazy

## exit_state

clearexit

## question

For the minimax game underlying S(n) (unary SORT-BOUND-U), is there an all-n strategy-compression into O(log n) alternation blocks that preserves the exact value S(n) and admits a polynomial-size (in input length N) witness/checker, or must every exact strategy require omega(log N) alternation depth?

## basis

APTIME=PSPACE (alternating TM), unary horizon gives polynomial alternations in S(n); board fronts on alternation depth but running; need falsifiable all-n claim distinct from fixed polynomial height.

## falsifier

Exhibit an explicit all-n family of posets/paths on which any exact strategy that fits into O(log n) blocks requires exponential blowup in the size of the block description, or give a constructive O(log N)-block exact strategy for all n.

## implication

A positive O(log N)-block compression would place SORT-BOUND-U into some level of PH (or give a stronger certificate class); a universal super-log alternation obstruction would rule out fixed-level PH membership and sharpen the PSPACE frontier for unary S(n).

## finding_unverified

Yet:** No identified candidate family, construction, or known obstruction specific to this phrasing. Need to formalize the model of "blocks" before falsification attempt.

## Next Move
1. **Formalize the Model:** Model `G(n,k)` ATM alternation carefully (round = ∃ pair, ∀ branch). Define "alternation block" operationally (e.g. a sequence of rounds treated as one block with bounded alternation, or a strategy compressed to O(log N) alternation phases) and see what witness/checker complexity follows. Relate to `APTIME=PSPACE`.
2. **Connect to Existing Certificates:** Analyze framed DAGs (`check_framed_strategy.py`, research-framed-certificate-frontier.md) and state quotients for compressibility. Test whether joins create block structure or if the "absent canonical object" is the obstruction.
3. **Formulate Falsifiable Claim:** Propose a precise all-n claim (e.g. for some explicit family any exact O(log N)-block strategy requires exponential block-description size, or a universal obstruction) with concrete falsifier and complexity implication (PH vs PSPACE), then attempt disproof against known barriers (sparsity doesn’t block, explicit tree/DAG size does).

## Relevant Files
- `/home/lubko/soring-fronts/adversary-alternation-logn-blocks/AGENTS.md` – research contract, constraints, Lean policy
- `/home/lubko/soring-fronts/adversary-alternation-logn-blocks/docs/problem.md` – model, encodings, realistic outcomes
- `/home/lubko/soring-fronts/adversary-alternation-logn-blocks/docs/research-certificates-barriers.md` – `G(n,k)`, ATM → PSPACE, sparsity, lack of succinct certificates
- `/home/lubko/soring-fronts/adversary-alternation-logn-blocks/docs/research-decision-encoding.md` – unary vs binary, alternation notes
- `/home/lubko/soring-fronts/adversary-alternation-logn-blocks/docs/research-framed-certificate-frontier.md` – framed DAGs, soundness vs completeness
- `/home/lubko/soring-fronts/adversary-alternation-logn-blocks/docs/research-state-compression.md` – quotienting, compression limits
- `/home/lubko/soring-fronts/adversary-alternation-logn-blocks/scripts/budgeted_dfs.py` – `G(n,k)` reference implementation
- `/home/lubko/soring-fronts/adversary-alternation-logn-blocks/scripts/check_framed_strategy.py` – framed DAG verifier
- `/home/lubko/soring-fronts/adversary-alternation-logn-blocks/scripts/research_frontier.py` – frontier/agent orchestration
- `/home/lubko/soring301/scripts/board_digest.py` – Antonina issue #301 inspection
Continue if you have next steps, or stop and ask for clarification if you are unsure how to proceed.
Let us look up the exact docs more.

## Done
- Explored repo (AGENTS.md, docs/problem.md, docs/research-certificates-barriers.md, docs/research-framed-certificate-frontier.md, docs/research-state-compression.md) and scripts (budgeted_dfs.py, check_framed_strategy.py).
- Mapped model: G(n,k), ATM view (sorter ∃, adv ∀), unary N=n+k+1 → PSPACE; sparsity/Mahaney barrier; no poly certificate for explicit tree; framed DAGs/compression open.
- Inspected Antonina #301; this front active with others. Searched all soring-fronts for "alternation.*block" — no local definition found.

## State
- Terminology "alternation blocks" (asked in objective) not defined in local docs/scripts. Unclear if ATM quantifier blocks or strategy compression blocks.
- Next: formalize operational definition of "alternation blocks" for G(n,k), relate to framed strategies/compression, form falsifiable all-n claim, try to disprove against known barriers.

## Other metadata

```json
{
  "finished_at": 1793396833.0788782,
  "started_at": 1793378916.2402642
}
```
