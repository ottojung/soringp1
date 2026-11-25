# antonina-ZKj6Fio5xt3TQXIvJq6nyS-capacity

Session: ses_e51ee1476ffeE8Py9oEsfVObOX
Workspace: /home/lubko/soring-fronts/parallel-reversal-congruence-20261106
Created: 1793921772429; updated: 1793921826475

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1ae11eba80013dCx71TqSlqOjI)

I’ll first check the project’s literature and prior research notes for overlap, then retrieve the cited paper and inspect the proof and finite-parameter dependencies. I’ll keep this read-only and won’t post anything externally.

## Output 76 (msg_1ae126b4e001TeyqDbgKlzOhUx)

## Result: the requested finite strengthening is **not established**

**Stop condition:** this is already the open “bound gap” recorded in `docs/research-plan.md` and the “Crucial limitations” section of `docs/research-sergeev-asymptotic.md`. The requested investigation therefore duplicates an active, explicitly catalogued project question. I found no completed proof in the inspected notes, and cannot provide the requested line-by-line finite bound without new estimates.

### Source and what I could verify

- **Primary source/version:** Igor S. Sergeev, *On the asymptotic complexity of sorting*, ECCC TR20-096, posted June 2020. The [ECCC report page](https://eccc.weizmann.ac.il/report/2020/096/) confirms the title, author, report number, date, abstract, and downloadable report.
- The local project note attributes the \(O(n/(\log n)^{1/5})\) surplus to **Theorem 3, page 29**. I could not inspect that proof in this run: direct HTTPS `curl` to the ECCC PDF failed with a connection reset, and the web fetcher rejected the PDF content type. The arXiv title search found no match.
- **Journal version:** Sergeev, *On the Upper Bound of the Complexity of Sorting*, *Computational Mathematics and Mathematical Physics* 61(2) (2021), 329–346, DOI [10.1134/S0965542521020111](https://doi.org/10.1134/S0965542521020111). The DOI metadata was reachable, but not the paper text.

Thus I cannot honestly claim to have read or reconstructed the primary proof, nor identify a specific missing lemma by its exact number. I also cannot confirm from the paper whether it states any explicit finite constants separately from its asymptotic theorem.

### What follows—and what does not

The theorem as recorded in the repository gives an asymptotic surplus for a **group-insertion sorting algorithm**, hence an asymptotic upper bound on adaptive worst-case comparison count. It does not, as recorded, provide constants and a finite threshold usable as a pointwise bound. The project note explicitly says extracting such a bound is a separate task.

Even a finite comparison bound would only give a candidate computable upper endpoint for \(S(n)\): with \(L(n)=\lceil\log_2(n!)\rceil\), it would yield \([L(n),U(n)]\). Whether its width is materially better at finite \(n\) depends on the constants and threshold. Those are precisely the suppressed quantities that need proof; the asymptotic \(O\)-statement alone cannot supply them. The construction is an algorithm for **sorting**, not an evaluation-time result for computing exact \(S(n)\).

I did not test numerical consequences against \(S(n)\le 22\) or the known \(n=23\) bounds: without a verified finite \(U(n)\), that comparison would amount to testing an invented bound.

### Independent-check pointers

- `docs/research-sergeev-asymptotic.md` — theorem attribution and explicit note that finite effectiveness remains open.
- `docs/research-plan.md` — the finite-bound question is already listed as the “bound gap.”
- `docs/literature.md` — exact values through \(n\le22\) and the status of \(n=23\).
- ECCC report page above, then TR20-096 Theorem 3 (reported at p. 29) and the journal version, for a direct proof audit once PDF access is available.

No repository files were changed or external posts made. No claim about resolving `SORT-BOUND-U` is made.

## Output 95 (msg_1ae12b6ac001TAyjQ7n1Vbk2L4)

Working tree is clean; no repository edits, commits, or external posts occurred. The previous read-only investigation is complete and its result stands. No further action needed.
