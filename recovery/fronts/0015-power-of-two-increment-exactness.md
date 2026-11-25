# power-of-two-increment-exactness

## status

investigated

## origin

ai_proposal_unverified

## agent_id

6Eeb9LQfhu3TpTEcfSX3qc-beside

## exit_state

succeeded

## question

Does the optimal increment d(2^k) = S(2^k) - S(2^k - 1) equal ceil(log2(2^k)) = k for every k >= 1, or does there exist a power of two where any optimal sorting tree beats the strict two-phase worst case S(2^k - 1) + k, as already happens for non-powers like n = 9 and n = 17..21?

## basis

Board #301 2026-10-27 two-phase front verified theorem: strict two-phase worst case is exactly S(n-1) + ceil(log2 n), exact iff d(n) = ceil(log2 n); hits at n = 2, 4, 8, 16 (all powers of two through 16) plus 22, misses at 9, 10, 17-21; tau(n) >= n/4 - O(n/(log n)^(1/5)) combined with Sergeev TR20-096.

## falsifier

An all-n proof that d(2^k) = k via a structural minimax argument at antichain-block ends, or an explicit k (first candidate n = 32, since exact values are known only through n = 22) for which a poset-extension or adversary argument shows S(2^k) < S(2^k - 1) + k.

## implication

At every miss the cumulative two-phase deficit tau(n) grows by a full block-end increment, so a proof that d(2^k) < k for some or all large k pins the O(n) miss-mass constant and refines whether the two-phase lemma's Omega(n) aggregate is block-localized or asymptotically dense.

## finding_unverified

The recovery instruction is clear. So far I only read the board and ledger; I have not posted, committed, or edited anything. I’ll inspect the checkout and durable record for this front, then continue the unfinished mathematical analysis without repeating any external action.
## Finding: unresolved

I found no all-\(n\) proof that \(d(2^k)=k\), and no power of two where the two-phase bound is beaten. The first undecided candidate remains \(n=32\): Stober–Weiß establish \(S(16)=46\), \(S(17)=50\), and \(S(18)=54\); with prior results, exact values are known through \(n=22\), not \(32\).

There is a useful exact reduction. Let
\[
L(n)=\lceil\log_2(n!)\rceil,\qquad g(n)=S(n)-L(n).
\]
Since \(L(2^k)-L(2^k-1)=k\),
\[
d(2^k)=k+g(2^k)-g(2^k-1).
\]
The two-phase algorithm gives \(d(n)\le\lceil\log_2 n\rceil\). Thus at a power of two the proposed equality holds exactly when the information-bound excess \(g\) does **not** drop at that endpoint; a counterexample requires a strict drop.

## Falsification attempt and obstruction

The aggregate bound
\[
\tau(n)=\sum_{j=2}^n(\lceil\log_2 j\rceil-d(j))
       =\sum_{j=2}^n\lceil\log_2 j\rceil-S(n)
       =\Omega(n)
\]
does not force a miss at any power of two. There are only \(O(\log n)\) such endpoints, and misses at non-powers can supply the aggregate mass. The known misses at \(9,10,17\!-\!21\), followed by a hit at \(22\), also show why extrapolating a local pattern is not reliable.

For \(n=32\), the exact question is whether \(g(32)=g(31)\). Resolving it needs a sufficiently strong lower bound for \(S(31)\) and upper bound for \(S(32)\), or the corresponding exact values; the known exact range does not supply them. The asymptotic excess bound from Sergeev is too coarse to settle a single integer-sized gap change.

I also ruled out treating a generic poset result as a direct answer: an extension-count bound is a lower bound for a state, not generally its exact minimax value, and a result about arbitrary posets does not transfer to the antichain root without a valid reduction. Likewise, a **sound** certificate can establish the claim it verifies; failure to find such a certificate does not establish the claim, and completeness for a proposed certificate system would need a separate proof.

**Evidence:** the algebra above is a deduction; the exact-value frontier and two-phase classifications are reported on board #301 and sourced there to Wells, Peczarski, and Stober–Weiß. No new theorem or counterexample emerged. No repository changes, commits, or board posts were made; the durable ledger still records this front as running.

## Other metadata

```json
{
  "finished_at": 1793130474.4975736,
  "started_at": 1793127988.617127
}
```
