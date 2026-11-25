# sparse-manyone-pspace-completeness-barrier

## status

investigated

## origin

ai_proposal_unverified

## agent_id

7BmRzGoEDRVeQDjwfPzEMa-rival

## exit_state

clearexit

## question

Is SORT-BOUND-U unconditionally not many-one PSPACE-complete under polynomial-time reductions (by sparsity/isomorphism generalizations of Berman–Hartmanis/Mahaney)?

## basis

SORT-BOUND-U is sparse/tally in PSPACE; EXPTIME many-one hardness is unconditionally ruled out (Berman–Hartmanis) while PSPACE many-one completeness remains open in docs/research-hardness-boundaries.md.

## falsifier

Give a polynomial-time many-one reduction from a known PSPACE-complete language to SORT-BOUND-U with a complete correctness proof and encoding analysis, or show the sparsity+isomorphism barrier fails in this model.

## implication

Establishing or ruling out many-one PSPACE-completeness would fix the exact relation of the sparse unary threshold to PSPACE without relying only on P/poly circuit barriers.

## finding_unverified

tmanis (EXPTIME):** gives an unconditional sparse-completeness exclusion for EXPTIME — exactly the template sought — but this does not transfer automatically to PSPACE (different padding/closure/census regime); I cannot certify a PSPACE instance of that theorem from the primary sources available here.
- **Mahaney/NP machinery:** for NP the standard consequence is conditional (`… unless P=NP`), not an unconditional non-hardness theorem; generalizing the proof method to PSPACE-complete sets would require a careful PSPACE-specific self-reducibility/census argument and primary-source verification.
- **Isomorphism conjecture framing:** not a proof of non-completeness for this specific sparse set without an established theorem instance.
- **Result:** [open] unconditional non-completeness not proved here.

**Concrete failed approach:** treating the unconditional EXPTIME sparse-completeness exclusion (Berman–Hartmanis 1977) as a black-box consequence of sparsity that applies equally to PSPACE is not justified by the cited facts available in-repo; PSPACE-specific padding/self-reducibility or census consequences must be established with verified primary sources.

## 4. Mathematical finding / honest limit
1. **[deduction] Settled vs open:** `SORT-BOUND-U` is sparse, in PSPACE, and unconditionally not many-one EXPTIME-complete (Berman–Hartmanis, as recorded). The analogous many-one **PSPACE-completeness** question is **not settled by the sparsity results currently established in-repo** (Mahaney/Fortune/Ogiwara–Watanabe/Karp–Lipton address NP/coNP/PH collapses; the EXPTIME argument is class-specific).
2. **[open] No falsifier:** no polynomial-time many-one reduction from a known PSPACE-complete language to `SORT-BOUND-U` was found/proved.
3. **[open] No unconditional barrier proof:** no complete, independently checkable proof was obtained that sparsity (or `SORT-BOUND-U`’s stronger `P/log`/`AC^0`/tally-threshold structure) unconditionally rules out many-one PSPACE-completeness.

This is an **exact obstruction**, not a proof and not a completeness claim.

## 5. Decisive next step (primary-source audit)
A resolution requires one of:
- a verified **primary-source theorem** showing (unconditionally, or under a hypothesis known false) that no sparse/tally language is `≤_m^p`-complete for PSPACE, with assumptions matching `SORT-BOUND-U`; or
- a complete **PSPACE-specialized census/self-reducibility argument** (e.g. from `TQBF ≤_m^p SORT-BOUND-U`) yielding `P=PSPACE` or an unconditional contradiction; or
- an explicit, fully proved **reduction** `TQBF → SORT-BOUND-U` (major, model-sensitive result).

Primary sources to verify (not fetched here; web search was unavailable/cancelled in this environment): Berman–Hartmanis 1977 (full scope beyond EXPTIME), Hartmanis 1978, Berman 1978, and census/collapse results for sparse hard sets of PSPACE under many-one reductions. Until audited, the front remains **open** (EXPTIME ruled out; PSPACE unresolved).
Recovery check complete. The prior turn produced a scratch report at `/tmp/opencode/pspace_completeness_report.md`; it made no repository changes or commits. Git remains clean at `6a96398`, and the #301 page-1 search found no matching post. No external side effect needs repeating.

The research remains unfinished mathematically: the report found neither a PSPACE-hardness reduction nor a verified unconditional sparse-PSPACE barrier. It records the EXPTIME exclusion and leaves PSPACE many-one completeness unresolved.

## Other metadata

```json
{
  "finished_at": 1794489673.3612785,
  "started_at": 1794480416.7001107
}
```
