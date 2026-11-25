# antonina-wq2wYeVhmx1WcUNmIZkr0J-multitude

Session: ses_e48d03770ffelTFwKn4ZNWguVj
Workspace: /home/lubko/soring-fronts/exec-effective-sergeev-bound-20261107
Created: 1794074724576; updated: 1794074781865

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1b72fcad7001yl2rNI1XkfJr1K)

I’ll inspect the four requested repository documents and the actual theorem proof first, then derive only what the paper’s stated inequalities support. I’ll keep the worktree untouched and report the numerical checks separately from any asymptotic claim.

## Output 31 (msg_1b72fdd35001XltF9wzLfSgYpZ)

The extracted text file is present but not readable as ordinary text through the file reader, so I’m checking its encoding and extracting the PDF directly if necessary. The key issue is whether each asymptotic “sufficiently large” choice and hidden constant is actually bounded by the proof.

## Output 79 (msg_1b730556a001ZaOOkocmhEC64A)

## Outcome

**Negative result:** Sergeev’s proof gives a constructive group-insertion sorting algorithm and an asymptotic recurrence, but it does **not** provide the explicit constants and finite thresholds needed to extract a concrete computable upper bound \(F(n)\) from Theorem 3 as written. Thus there is no source-justified \(F(n)\) here to evaluate numerically. This does not show that such a bound cannot be extracted with additional work.

**Sources checked:** the requested repository documents and Sergeev, ECCC TR20-096 (2020), Theorem 3 and its proof, Corollary 2, and Lemmas 1–2. The PDF’s SHA-256 matches the supplied value, `17901b39ca3f67ac7e40bba7d7864b848d36793824f286fa57eeb78b979f0e88`.

## What the proof establishes

**Literature / paper proof.** Theorem 3 starts with
\[
S(n)\le n/2+S(n/2)+\log(n!)-\log((n/2)!)-n/2
       +O\!\left(n\log^{-1/5}n\right).
\]
Equivalently, for \(s(n)=S(n)-\log(n!)\),
\[
s(n)\le s(n/2)+O\!\left(n\log^{-1/5}n\right),
\]
which yields \(s(n)=O(n\log^{-1/5}n)\).

The proof identifies where that final \(O\)-term comes from:

- The first \(n_0=n/\log n\) smaller elements are inserted by Ford–Johnson at cost \(n+O(n_0)\).
- Groups have size \(m\approx\sqrt n/\log n\). For group \(t\), the target interval has length \(L_t=2(n_0+tm)-m\).
- Corollary 2 supplies a group insertion estimate expressed as \(\rho_t=\log L_t+O(\log^{-1/5}n)\).
- Comparing group insertion costs with the idealized sum leaves an excess \(O(n_0+m)+O((n/2-n_0)\log^{-1/5}n)\).

These are asymptotic estimates, not a finite recurrence with specified numerical constants.

## Where explicitness fails

The most direct gap is Corollary 2: it states
\[
Q_{2m}(a)\ge 2^a-O(a^{-1/5}2^a).
\]
The proof of Theorem 2 sets parameters and bounds terms using \(O(\cdot)\), \(\Theta(\cdot)\), and “for example” asymptotic comparisons, but does not give a single explicit constant and threshold that turn this into a finite inequality for all \(a\ge a_0\). In particular, it says the bound holds for \(a<100\) with a “sufficiently large” hidden constant, without specifying that constant.

Theorem 3 then uses this estimate to assert \(\rho_t=\log L_t+O(\log^{-1/5}n)\), again without a constant or a threshold. It also leaves the \(n_0\)-phase’s \(O(n_0)\) cost unspecified. Consequently the recurrence cannot be made into an explicit all-\(n\) numerical recurrence from the stated proof alone.

Lemmas 1–2 do give explicit formulas once their parameters, strategy, and finite hypotheses are supplied. The universal-strategy section also proposes explicit parameter choices for sufficiently large \(s\). But these do not by themselves fill the missing finite constants and thresholds in Theorem 2’s asymptotic conversion or Theorem 3’s phase-cost accounting. Choosing constants independently of those omitted justifications would invent bounds not established by the paper.

## Requested numerical and falsification checks

Because no paper-justified explicit \(F(n)\) was obtained, numerical values of \(F\) at \(n=12,16,22,23,100,1000\), and comparisons against \(\lceil\log_2(n!)\rceil\) and the Ford–Johnson bound, are **not applicable**. An asymptotic \(O\)-statement is not a finite bound.

The known-value falsification check is therefore conditional: any proposed extracted \(F\) must satisfy \(F(12)\ge30\), \(F(16)\ge46\), \(F(17)\ge50\), and \(F(18)\ge54\). No candidate \(F\) was derived, so none can be tested or claimed to pass.

**Remaining gap:** explicitly quantify the constants and valid finite thresholds in Corollary 2/Theorem 2, then bound the initial insertion phase and all rounding/group remainders in Theorem 3. Only after those steps can one produce and numerically falsify an all-\(n\) bound.

The worktree remained detached at `c865b23968388d59316cc994501508d3782be90a` and clean. No repository files, branches, commits, or posts were changed.
