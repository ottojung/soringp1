# antonina-FLB1M8pY5k0gWwMGkLrkBf-symbols

Session: ses_e4b631d44ffen1SgugLk60HqCa
Workspace: /home/lubko/soring-fronts/exec-sergeev-effective-bound-20261107
Created: 1794031543030; updated: 1794031595022

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1b49ce4bd001jjHclhjid5YkwY)

I’ll inspect the local paper and the two referenced research documents, then trace Theorem 3’s dependencies and calculate only what the text actually supports. I’ll leave repository files untouched and verify the worktree remains clean.

## Output 50 (msg_1b49d30e3001gURdVBmLu2uOsI)

## Finding

**Theorem 3 does not expose an explicit finite computable upper bound for \(S(n)\) as published.** It gives an asymptotic comparison-count bound, but the constants needed to turn it into a finite bound are hidden in the invoked results and in Theorem 3’s own schedule. This is a limitation of the proof *as stated*, not a claim that its constructive algorithm cannot be made effective with additional work.

### What can be recovered

The paper uses binary logarithms: page 2 says it “skip[s] the base of binary logarithms.” Theorem 3’s proof on pp. 29–30 gives the asymptotic recurrence
\[
S(n)\le \frac n2+S(n/2)+\log(n!)-\log((n/2)!)-\frac n2
       +O\!\left(n\log^{-1/5}n\right),
\]
or, for \(s(n)=S(n)-\log(n!)\),
\[
s(n)\le s(n/2)+O\!\left(n\log^{-1/5}n\right).
\]
These are the recoverable recurrences, not quantified finite inequalities. Equation (45) also has an \(O(\log n)\) remainder.

The proof’s schedule is likewise asymptotic: \(n_0=n/\log n\), \(m\approx\sqrt n/\log n\), and groups indexed by \(k\), with \(L_t=2(n_0+tm)-m\). It invokes Corollary 2 to obtain \(\rho_t=\log L_t+O(\log^{-1/5}n)\) and \(Q_m(\rho_t)\ge L_t\). The paper does not specify integer rounding for these choices, nor an all-\(n\) parity/floor convention for the recurrence.

### Where effectivity fails

The dependency chain is Theorem 3 (pp. 29–30) → Corollary 2 (p. 29) → Theorem 2 (pp. 28–29) → Lemma 2 (pp. 10–12) and Lemma 4 (pp. 26–28).

The decisive gap is already explicit in Theorem 2’s proof: for \(a<100\), (44) holds with “sufficiently large values of the constant hidden behind the symbol \(O\)” (p. 28, proof lines 048–049). No value for that constant is supplied. For \(a\ge100\), the proof gives a parameter schedule, but concludes an asymptotic \(O(a^{-\gamma}2^a)\), not a numerical finite-loss inequality. Corollary 2 carries that \(O\)-term forward. Lemma 2 provides a finite inequality under quantified hypotheses, and Lemma 4 provides parameter choices, but applying them does not remove the unspecified Theorem 2 constant or the missing integer schedule and small-\(a\) bounds.

Consequently, the final recurrence has no published numerical coefficient, threshold, or finite initial basis from which to compute a bound for every \(n\). The paper’s “for any \(n\)” Theorem 3 statement is in big-\(O\) notation; it does not supply those missing quantities. The recurrence’s halving step also leaves odd \(n\) and floor/ceiling details unstated.

### Exact-evaluation window

No concrete \(n\) at which this result narrows an exact-evaluation window relative to Ford–Johnson can be identified from the published proof. The paper’s asymptotic result implies eventual improvement in the \(o(n)\) sense, but its unknown constants and threshold prevent locating where that improvement becomes a usable finite upper bound. This is about comparison counts, not the running time of evaluating \(S(n)\).

### Audit

- **Source:** local ECCC TR20-096 PDF, 31 pages. Relevant passages: p. 2 (log-base convention); pp. 10–12 (Lemma 2); pp. 26–28 (Lemma 4 and Theorem 2 application); p. 29 (Theorem 3 schedule and recurrence); pp. 29–30 (Corollary 2, equation (45), and recurrence closure). Theorem 3 is on PDF p. 29; its proof continues on p. 30.
- **Model:** the paper defines sorting by adaptive pairwise comparison trees, worst-case depth, and distinct inputs (p. 1), matching the sorting-number model. Its result concerns comparisons made by a sorting algorithm, not the computational time to evaluate \(S(n)\).
- **Falsification check:** the invoked statements and their proof passages were inspected, including Lemma 2, Lemma 4, Theorem 2, and Corollary 2. The finite-constant claim fails at the explicit \(a<100\) absorption in Theorem 2; the later \(O\)-terms and omitted rounding/parity details independently prevent an all-\(n\) numerical bound. No constants have been guessed.
- **Corollary numbering:** this local TR20-096 version has Corollaries 1 and 2; no labeled Corollary 3 was found.
- **Repository:** no source edits or other worktree changes were made; `git status --short` was empty.
