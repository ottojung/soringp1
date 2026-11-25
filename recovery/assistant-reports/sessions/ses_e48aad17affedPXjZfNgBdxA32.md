# antonina-NWQHVkrbwyjgLB5LmAPuKx-shadow

Session: ses_e48aad17affedPXjZfNgBdxA32
Workspace: /home/lubko/soring-fronts/exec-sergeev-effective-finite-20261107
Created: 1794077175484; updated: 1794077852528

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 48 (msg_1b755708d001G4a53foHjomPNW)

I could not access the primary proof: the ECCC report page confirms TR20-096 and its abstract, but downloading the PDF failed because the connection was reset. Without the text of Theorem 3 and its definitions, I can’t reliably identify the quantitative inequalities or name the first missing constant or lemma. So I can’t establish an explicit all-\(n\) bound \(B(n)\) from the proof.

The abstract’s \(\log_2(n!)+o(n)\) claim alone does not supply effective constants or cutoffs, and it would be wrong to infer them from the asymptotic statement. The repository’s literature baseline records \(S(n)=\lceil\log_2(n!)\rceil\) through \(n=11\), \(S(12)=30\), and exact values through \(n=22\); those are useful checks, not a substitute for auditing Sergeev’s proof. No evaluation-time bound follows from that asymptotic comparison bound either.

If you provide the PDF or a reachable copy, I can trace the proof’s constants and rounding conditions and determine whether they yield an explicit \(B(n)\).

## Output 217 (msg_1b75f478e001MUoYhyqOYtO5T5)

The preserved PDF is the same source: its SHA-256 matches the supplied hash. I inspected its Theorem 3 proof and the preceding lemmas. **I cannot give a proved explicit \(B(n)\) from the written proof**, so I make no claim that the theorem supplies a numerically usable finite bound. This is a gap in the proof’s quantitative presentation, not evidence that the constructive algorithm itself is ineffective.

The first missing input is the **explicit error constant and valid cutoff in Corollary 2**:
\[
Q_{2m}(a)\ge 2^a-Ca^{-1/5}2^a.
\]
The paper writes only \(O(a^{-1/5}2^a)\). Theorem 2 likewise leaves the constants implicit in its error estimates; it handles \(a<100\) by saying the hidden constant can be made “sufficiently large.” More importantly, it chooses \(s=\lceil(2/5)\log_2 a\rceil\), while Lemma 4 requires \(s\ge20\). That choice does not meet the lemma’s stated hypothesis throughout the claimed range. Replacing it with \(\max(20,\lceil(2/5)\log_2 a\rceil)\) may repair the range with adjusted constants, but the paper neither makes that choice nor supplies the resulting uniform estimates. Recovering a constant and cutoff would require additional quantitative work; they are not stated in the primary proof.

Theorem 3 then relies on that unspecified constant to choose each \(\rho_t=\log_2 L_t+O((\log n)^{-1/5})\) and to bound the total excess comparisons. Its recurrence still has an unspecified constant:
\[
s(n)\le s(n/2)+O\!\left(n(\log n)^{-1/5}\right).
\]
To turn this into an explicit all-\(n\) bound requires explicit constants through Corollary 2 and the grouping/rounding estimates, plus a finite base bound and precise integer choices. There is also a factor-of-two bookkeeping issue: Corollary 2 states a bound for \(Q_{2m}\), whereas Theorem 3 uses \(Q_m\) for groups of size \(m\); resolving it by halving the parameter changes the range and needs to be reflected in the choices.

The underlying parameters are partly explicit: Lemma 4 specifies \(s\ge20\), \(d=2^s\), \(\mu=30\cdot2^{-s}\), \(\lambda=20\cdot2^{-s/2}+64\cdot2^{-s}\), and \(\epsilon=(25\cdot2^s)^{-1}\); Lemma 2 gives its condition (17) and rounding convention. But those do not by themselves provide the missing uniform Corollary 2 constant or the all-\(n\) recurrence constant. Thus I cannot responsibly state a \(B(n)\) and claim its proof from this source alone.

As a small-value sanity check, the Ford–Johnson formula printed earlier in the paper gives 30, 46, 50, and 54 for \(n=12,16,17,18\), respectively, agreeing with the known exact values. No bound from the asymptotic group-insertion argument was evaluated here. This is a comparison-count question only; no evaluation-time bound follows.
