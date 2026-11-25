# antonina-r4qSEsSjMdjoUL3J5G4QQV-knees

Session: ses_e530ce5f3ffetReaptGhDFEpRu
Workspace: /home/lubko/soring301
Created: 1793902975502; updated: 1793903068595

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 111 (msg_1acf3ffda001e0mO1ed364scKz)

## Finding: the stated asymptotic does not yield an explicit finite window

**Literature:** Sergeev’s ECCC abstract states that \(\log_2(n!)+o(n)\) comparisons suffice, via a group-insertion algorithm. The project note identifies Theorem 3, page 29, of TR20-096 as the source for the sharper \(O(n/(\log n)^{1/5})\) rate. The journal version’s accessible abstract likewise states only the \(o(n)\) result.

**Obstruction:** I could not access the primary proof text in this environment: the ECCC PDF download failed, and the journal page exposes only a preview. So I cannot source-locate proof constants or verify whether intermediate estimates in the proof are effective. In particular, no explicit constant \(C\) or threshold \(n_0\) is established by the accessible source material. The exponent and asymptotic existence claim alone do not provide either.

**Integer budget, conditional on such constants:** If the proof established
\[
S(n)-\lceil\log_2(n!)\rceil\le C\,\frac{n}{(\log_2 n)^{1/5}}
\quad(n\ge n_0),
\]
then an integer search budget would be
\[
K(n)=\left\lceil C\,\frac{n}{(\log_2 n)^{1/5}}\right\rceil,
\]
and the threshold would lie in
\[
[\lceil\log_2(n!)\rceil,\ \lceil\log_2(n!)\rceil+K(n)].
\]
Since \(K(n)=o(n)\) for fixed \(C\), this would narrow the \(O(n)\)-scale range given by a linear-excess upper bound for all \(n\ge n_0\). But without source-supported \(C,n_0\), this is a conditional derivation—not an effective bound or an implemented uniform narrowing.

**Falsification check:** Known values do not challenge the asymptotic: the \(n=12\) excess is \(1\), and the theorem allows an unspecified finite exceptional range. Small values therefore cannot recover the missing constants or threshold.

**Implication:** An effective finite comparison budget would narrow the range of \(k\) relevant to evaluating the unary language `SORT-BOUND-U`; it would not itself give a faster exact evaluator or imply any complexity separation. This investigation is read-only; no repository files or posts were changed.

## Output 155 (msg_1acf477340011T9MIpzYnGHtl7)

Recovery check complete: the prior turn’s work was read-only. Git is clean on `billy-dev`; no commit, post, or other external action occurred. The only temporary artifact was `/tmp/opencode/sergeev.pdf` (the download failed), outside the repository. The investigation’s conclusion remains: explicit constants and thresholds could not be source-verified because the primary proof text was inaccessible. No unfinished side effect needs continuation.
