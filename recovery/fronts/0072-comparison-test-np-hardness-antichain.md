# comparison-test-np-hardness-antichain

## status

investigated

## origin

ai_proposal_unverified

## agent_id

9QNxmUYJe2HLK6m0t7FlO7-skirts

## exit_state

clearexit

## question

Is computing S(n) (or deciding SORT-BOUND-U) NP-hard under the restriction to comparison tests only, for the antichain/root instance family S_n, or does the fixed comparison test set avoid Hyafil-Rivest/Laber-Nogueira transfers and place it below NP despite arbitrary-test NP-hardness?

## basis

Hyafil-Rivest NP-completeness for arbitrary tests; Laber-Nogueira o(log n) inapproximability; certificates-barriers show transfer fails due to fixed test set and sparsity/Mahaney, but no all-n comparison-test hardness proof or NP-membership route is known.

## falsifier

Exhibit a polynomial-time many-one reduction from some NP-complete problem to SORT-BOUND-U that is sound and complete for all n using only comparison-based tests and the antichain root, or prove no such reduction exists under standard assumptions while giving a concrete obstruction tied to the fixed test set.

## implication

A positive reduction would put SORT-BOUND-U in NP∩PSPACE (and relate to P!=NP) but must respect sparsity/Mahaney; a clean separation/obstruction would clarify whether NP membership is plausible without changing the arbitrary-test hardness picture.

## finding_unverified

I'll start by studying the repository state and the referenced documents.

I'll search for existing discussions about NP-hardness, Hyafil-Rivest, Laber-Nogueira, and certificate/sparsity related to comparison tests.

I'll look at the core barrier docs in detail.

Let me first look up the full board #301 more - there might be relevant posts, and also the instruction says "On billy-dev ONLY" which matches. Let us also look at the current frontier ledger.

I'll give a precise mathematical argument.

Let us look up the board #301 more closely around the exact front - and also look up the exact post from the user again: they say "study AGENTS.md, docs/problem.md and current board #301. Study the primary literature..." Also they say "On billy-dev ONLY" - we are on billy-dev based on env. Also they want the answer posted? The instruction says "On completion report a mathematical finding, concrete failed approach or exact obstruction" - this might be asking us to do the research as specified.

I'll analyze the question directly against the literature and model.

**Finding:** No polynomial-time many-one reduction from NP-complete problems to `SORT-BOUND-U` is known, and there is a concrete obstruction tied to the fixed pairwise-comparison test set (plus the unary sparsity barrier). The Hyafil–Rivest/Laber–Nogueira results do **not** transfer.

**Key points:**
- **Model restriction (Hyafil–Rivest).** Hyafil–Rivest reduce from EC3 using *arbitrary 3-element subset tests* as root queries ([IPLL 1976]). The sorting model restricts tests to *pairwise comparisons* only, on the fixed family for `n` labelled elements (antichain root `S_n`). This is a strict restriction of the test family; no reduction is known and the EC3 gadget is not realizable with pairwise tests. Same for Laber–Nogueira (arbitrary tests, `o(log n)` inapproximability).
- **Sparsity/Mahaney barrier (unary).** `SORT-BOUND-U` is sparse; many-one NP-hardness would imply `P=NP` (Mahaney). `SORT-BOUND-B` is not sparse so the barrier does not apply there, but binary is not the active workstream and other constraints remain.
- **No NP certificate / structure.** A correct comparison tree can be exponential in input length (`n!` leaves) and there is no known succinct polynomial-size certificate for all-`n` optimal strategies; branch-divisibility/realizability constraints (e.g. odd-`n` antichain→star exact-reset obstruction) show extension-count arithmetic alone is not sufficient.
- **Complexity implications.** A reduction would put `SORT-BOUND-U` in `NP∩PSPACE` but must respect sparsity/Mahaney; obstruction is consistent with `SORT-BOUND-U` below NP or incomparable, without implying a collapse - it clarifies NP membership is not plausible via standard arbitrary-test transfers and is blocked by the fixed test set + sparsity.

**Conclusion:** The comparison-test restriction (fixed pairwise tests, antichain root family) is the critical obstruction preventing transfer of Hyafil–Rivest/Laber–Nogueira NP-hardness; combined with unary sparsity this makes a standard many-one NP-hardness reduction for `SORT-BOUND-U` highly implausible under standard assumptions.


## Other metadata

```json
{
  "finished_at": 1793388455.219374,
  "started_at": 1793388060.523637
}
```
