# antonina-xfJlkzwZjzoITg29eylOED-feelings

Session: ses_e52918a94ffeq055kmtEQr6KUj
Workspace: /home/lubko/soring-fronts/exact-s12-fo-tc-nonframed-20261105
Created: 1793911059829; updated: 1793911154103

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1ad6e7596001pjUt1RWrw5IpH1)

I’ll audit the theorem from the primary source first, then separate what its asymptotic notation formally implies from what the proof techniques may permit one to extract. I’ll also check the requested finite-value comparisons against the repository’s recorded exact data.

## Output 73 (msg_1ad6f272b001BGcaJhwZv36Fe6)

## Extraction audit

**Primary source located:** Igor Sergeev, *On the asymptotic complexity of sorting*, ECCC TR20-096, posted 22 June 2020. The [ECCC report page](https://eccc.weizmann.ac.il/report/2020/096/) links the primary report at [`/report/2020/096/download`](https://eccc.weizmann.ac.il/report/2020/096/download). Its abstract states that the number of pairwise comparisons is \(\log_2(n!)+o(n)\), achieved by a group-insertion sorting algorithm.

**Limitation:** I could retrieve the report landing page, but not the PDF text in this session. The ECCC download endpoint returned a PDF that the available fetch tool could not render, and direct download failed. I did not establish a trusted journal version. So I cannot responsibly cite theorem/proof page numbers or claim to have audited the proof’s individual constants.

### What the published asymptotic statement does—and does not—give

The abstract’s \(o(n)\) statement means that for every \(\varepsilon>0\), there is some threshold \(n_0(\varepsilon)\) such that the excess is at most \(\varepsilon n\) for all \(n\ge n_0(\varepsilon)\). It does **not** give a numerical \(n_0\), nor a numerical excess bound at any specified \(n\).

Likewise, a bound of the form
\[
S(n)-\lceil\log_2(n!)\rceil
\le C\,n/(\log n)^{1/5}
\]
would need a numerical \(C\), a specified logarithm base, and any threshold beyond which it holds. Without these, it supplies no numerical finite bound for a chosen \(n\). This is a blocker in the *statement as available here*, not evidence that the proof cannot yield effective constants.

The requested proof-constructiveness check therefore remains unresolved: obtaining the actual report text is necessary to identify every asymptotic estimate in the argument and determine whether its constants and thresholds can be tracked. Even if the proof is algorithmic or constructive, that alone does not mean the published theorem records usable numerical constants.

### Finite comparisons

The repo’s literature baseline records exact \(S(n)\) for all \(n\le22\), and specifically \(S(12)=30\) versus \(\lceil\log_2(12!)\rceil=29\), so the \(n=12\) gap is 1 (`docs/literature.md`, lines 8–19). I cannot compare a candidate numerical bound against those values because no candidate constants or threshold have been extracted.

**Bottom line:** the available primary-source landing page establishes the \(o(n)\) abstract claim, but not the requested finite extraction. No numerical finite bound follows from that asymptotic statement alone. The decisive next step is obtaining the report PDF (or a verified journal text) and auditing its proof line by line; I have not established that the underlying proof is ineffective.

## Output 82 (msg_1ad6f6779001iHEjIoRRn7SdPi)

I’ll first check the workspace and Git state for any durable task artifacts or changes, then I’ll resume only the uncompleted source/proof audit. I will not post or edit anything.

## Output 131 (msg_1ad6fa670001385w9oOHPboTFq)

## Recovery check

Git is on `billy-dev`; status shows one untracked file, `docs/exact-s12-fo-tc-nonframed.md`. It is unrelated to this audit and I left it untouched. I found no TR20-096 PDF or task artifact in the workspace, and no indication of any external post or commit from the previous turn.

## Source and extraction status

The repository’s existing note identifies the precise result as **Theorem 3, page 29** of Igor S. Sergeev, *On the asymptotic complexity of sorting*, ECCC TR20-096 (2020):  
\[
S(n)=\log_2(n!)+O\!\left(\frac{n}{(\log n)^{1/5}}\right).
\]
It also identifies a journal version: *On the Upper Bound of the Complexity of Sorting*, *Computational Mathematics and Mathematical Physics* 61(2) (2021), 329–346, [DOI 10.1134/S0965542521020111](https://doi.org/10.1134/S0965542521020111). The DOI resolves to the bibliographic record, but I could not retrieve proof text from either version in this session: ECCC’s download is PDF-only to the available fetcher, and the DOI page returned citation metadata. Relevant existing source locations are `docs/research-sergeev-asymptotic.md:3–23` and `docs/research-winning-frontier-barrier.md:157–162`.

So the requested **individual asymptotic constants, thresholds, and proof-level constructive audit remain unfinished**. I cannot claim from this retrieval that Sergeev’s proof lacks effective constants or is nonconstructive.

## What follows rigorously from the available theorem statement

Big-O asserts the existence of constants \(C>0\) and \(n_0\) such that the stated inequality holds for \(n\ge n_0\). With neither value specified, it does not yield a numerical bound at any chosen \(n\), nor a numerical finite cutoff. In particular, converting it into a finite bound requires at least an explicit \(C\), an explicit threshold \(n_0\), and a fixed logarithm convention. The theorem’s constructive algorithm does not, by itself, publish those values.

For \(n\ge n_0\), if such constants were supplied, the integer gap would satisfy
\[
0\le S(n)-\lceil\log_2(n!)\rceil
\le \left\lfloor C\,n/(\log n)^{1/5}\right\rfloor,
\]
since \(S(n)\) is integral and \(\lceil\log_2(n!)\rceil\ge\log_2(n!)\). For \(n<n_0\), a separate finite bound or direct computation would be needed.

The requested finite comparison is consequently not numerical: the literature note records exact values for all \(n\le22\), with the \(n=12\) gap equal to \(30-29=1\), but no extracted candidate bound can be checked against them. Sources for those finite facts are recorded in `docs/literature.md:8–19`.

**Conclusion:** the asymptotic theorem as recorded gives no numerical finite bound. Whether the proof can be made effective—and the exact constants/thresholds if so—still requires the theorem and proof text; that is the unresolved blocker, not a proven ineffectiveness result.
