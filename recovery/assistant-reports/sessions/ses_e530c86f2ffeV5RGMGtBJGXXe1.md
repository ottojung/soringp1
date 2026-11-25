# antonina-YKdbENAXOQA2LPdYsyB8JJ-brazil

Session: ses_e530c86f2ffeV5RGMGtBJGXXe1
Workspace: /home/lubko/soring301
Created: 1793902999823; updated: 1793903097329

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 96 (msg_1acf4601a001UrPRzg5iXbxVCY)

## Finding

**Status: paper argument; no new theorem about the uniform sorting-number problem.** The local frontier identifies the issue as `fo-tc-policy-interpreter`. The Antonina board lookup failed in this environment, so I could not inspect its originating issue or verify the specific abandoned \(n=8\) two-phase witness attempt.

The key distinction is **describing a policy** versus **certifying its worst-case behavior from the antichain**. FO(TC) evaluation on one input order can tell us what a fixed formula does on that structure. It does not, by itself, establish that the induced adaptive policy sorts *every* one of the \(n!\) orders within \(k\) comparisons.

### Natural explicit encoding and the quantifiers it must cover

For an input \(1^n\#1^k\), a direct encoding could give a deterministic policy formula \(\varphi\), together with its signature and semantics, over structures encoding a comparison history: the labels \(1,\ldots,n\), the comparisons made so far, and the resulting partial order. Its output must specify either an incomparable pair to compare or a sorted output. The policy interpreter starts at the empty relation and updates the history according to each adversary answer.

A sound depth verifier must establish, for **every** permutation \(\pi\in S_n\), that the run induced by \(\varphi\) on \(\pi\) terminates with the correct sorted order within \(k\) comparisons. Equivalently, in the game semantics, it must certify that the policy’s comparison choice is valid at every history reachable from the antichain and that **both** answer branches continue to certified histories, with all leaves correct and at depth at most \(k\).

The permutation quantifier can be written as a polynomial-space check: enumerate permutations one by one, simulate the policy, and check the run. But this is not a polynomial-time verifier merely because each individual FO(TC) evaluation is polynomial-time. There are \(n!\) runs. Nor does the policy’s formula alone provide a polynomial-size certificate that compresses their universal correctness.

### Does a restricted grammar give polynomial certificates?

For the unrestricted grammar, I found no general polynomial-size witness with a completeness proof. The obvious complete witness is an explicit adaptive decision tree: it covers every order and its height can be checked, but it has at least \(n!\) reachable leaves. That is not polynomial in the unary input length on the informative range.

A plausible restricted format is a **proof-carrying policy**: the policy description plus a polynomial-size inductive invariant over histories, with a locally checkable condition that (i) holds at the antichain root, (ii) is preserved under both feasible comparison outcomes, and (iii) implies sortedness within the remaining budget. Such an invariant would be sound if the checker verifies those closure and terminal conditions. But this is only a *candidate format*, not a completeness result: no argument here shows that every policy of worst-case depth at most \(k\)—or even every optimal sorting policy—has such a polynomial-size invariant. Restricting the policy grammar to formulas that happen to admit one does not establish a certificate for all yes-instances.

**Obstruction to the proposed inference:** FO(TC)’s polynomial-time evaluation concerns one encoded structure. The root claim has a universal quantifier over input orders (or, equivalently, all feasible adversary paths), and the policy’s behavior may branch on prior outcomes. No polynomial-size representation of that universal obligation follows just from the policy being FO(TC)-definable.

A complete, sound polynomial-size verifier for yes-instances \(S(n)\le k\), with polynomial-time checking measured against \(N=n+k+1\), would give `SORT-BOUND-U ∈ NP`. That would be a genuine upper-bound result. This analysis does **not** give such a verifier, does not establish non-membership in NP, and makes no lower-bound claim.

### Sources and next falsifiable step

- Local `docs/research-frontier.json`, entry `fo-tc-policy-interpreter`: records the sharp question and the proposed consequence for `SORT-BOUND-U`.
- `docs/research-plan.md`, §“Descriptive complexity”: distinguishes FO(PFP) from a proposed FO(LFP)/ESO upper-bound advance and warns against inferring a smaller-class definition from a compact informal recursion.
- `docs/research-certificates-barriers.md`, §§0, 2, 4 (especially Claim C): fixes the adaptive-tree game and unary encoding; explains why explicit trees do not give polynomial-size witnesses.
- Chandra, Kozen & Stockmeyer, “Alternation,” *JACM* 28(1), 1981, DOI [10.1145/322234.322243](https://doi.org/10.1145/322234.322243): primary source for `APTIME = PSPACE`, the relevant established upper-bound route—not a polynomial-certificate result.
- `docs/operations.md`, §“Research board”: identifies Antonina issue #301 and the local digest procedure. The digest could not run here, so the board-originating issue remains unverified.

**Falsifiable next step:** fix a precise FO(TC) policy syntax, history encoding, and size measure, then either prove that every height-\(\le k\) policy has a polynomial-size locally checkable inductive invariant in that format, or exhibit a policy family for which the chosen invariant format requires superpolynomial size. The first outcome would support the NP upper bound; failure of one format alone would not rule out other certificates.

## Output 105 (msg_1acf4c752001QceOI4GwnO20W0)

I’ll check the local conversation artifacts, repository state, and relevant durable records first. I won’t retry the board lookup or post anything; the prior task was read-only.

## Output 134 (msg_1acf4e39e0017C0MfS2nfcJ79P)

Recovery check complete. The prior turn’s research was read-only; it did **not** post to Antonina, edit files, commit changes, or run Lean. Git reports a clean worktree on branch `billy-dev`. No local conversation or task-record files were found.

The local frontier still lists `fo-tc-policy-interpreter`; no durable record indicates that work was marked complete. The prior answer covered the argument and source references, but the Antonina-originating issue and the claimed abandoned \(n=8\) attempt remain unverified because the backend lookup failed. I did not retry it. Please review those two details against the board when Antonina recovers.
