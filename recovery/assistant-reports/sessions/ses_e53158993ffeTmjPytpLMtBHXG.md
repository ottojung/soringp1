# antonina-kiu28FdYlCHXuvwGSICdFQ-surrounds

Session: ses_e53158993ffeTmjPytpLMtBHXG
Workspace: /home/lubko/soring301
Created: 1793902409332; updated: 1793902491309

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 95 (msg_1aceb002b001DQGE13LDNpsG7X)

## Result

**[Deduction]** For adaptive, worst-case comparison sorting of 23 distinct labelled keys, the defensible interval is

\[
\boxed{75 \le S(23) \le 76}.
\]

So there is a single exact candidate, \(S(23)=75\), but it is **not established**: the unresolved task is to rule out a 75-comparison sorting tree. The upper bound is Ford–Johnson; the lower bound is the information bound.

## Derivation and status

- **[Literature]** Stober–Weiß state that exact values were known through \(n=22\), except for the values they resolved at 16, 17, and 18. Their work gives \(S(16)=46\), \(S(17)=50\), \(S(18)=54\), and \(S(28)\ge99\). Their arXiv version is 2206.05597v2; the paper appeared at ALENEX 2023. The repository’s `docs/literature.md` and the paper’s abstract/introduction both give this status, rather than treating 23 as settled.
- **[Deduction]** The information bound at 23 is \(\lceil\log_2(23!)\rceil=75\): \(23!>2^{74}\) and \(23!<2^{75}\).
- **[Literature]** The Ford–Johnson count is \(F(23)=\sum_{j=1}^{23}\lceil\log_2(3j/4)\rceil=76\). Thus \(75\le S(23)\le76\). This is a finite-value interval, not an all-\(n\) theorem and not a result about the unary complexity of computing \(S(n)\).

As an independent arithmetic check, \(23!=25{,}852{,}016{,}738{,}884{,}976{,}640{,}000\), so \(2^{74}<23!<2^{75}\). The Ford–Johnson sum evaluates to 76. **No search was run**; this is exact threshold arithmetic, not evidence that \(S(23)=75\).

## Is the Stober–Weiß search plausible at 23?

The method is technically applicable, but the paper’s reported scale does **not** justify calling an \(n=23\) lower-bound run feasible on the same resources without a new estimate or a successful pilot.

Their bidirectional method uses a partial backward search to build advice, then a forward search. The critical coverage guarantee is conditional: for a forward-reachable sortable state below the efficiency threshold, the backward table must contain it. Entries marked unknown still require forward exploration; absence outside the guaranteed region proves nothing. This is why a smaller table cannot simply be interpreted as a stronger lower bound.

The paper’s parameters are a concrete warning:

| Target | Candidate threshold \(C\) | \(E_{\rm tot}=n!/2^C\) | Paper result |
|---|---:|---:|---|
| \(n=16\), disproving 45 | 45 | about 0.59 | \(3.99\times10^9\) posets; 11 h |
| \(n=17\), disproving 49 | 49 | about 0.63 | \(13.2\times10^9\); 115 h |
| \(n=18\), disproving 53 | 53 | about 0.71 | \(10.0\times10^9\); 89 h |
| \(n=22\), disproving 70 | 70 | about 0.95 | 579,813; 85 s |
| \(n=28\), disproving 98 | 98 | about 0.96 | 30.2 million; 10 h |

The 22 and 28 rows are not a forecast for 23: they use zero efficiency bandwidth, unlike the difficult 16–18 runs, and thus are not directly comparable to a search at a candidate threshold near the information bound.

At 23, the immediate lower-bound target is \(C=75\), with \(E_{\rm tot}=23!/2^{75}\approx0.733\). A run at 75 that returns “not sortable” would prove \(S(23)\ge76\), settling the value at 76 in conflict with the Ford–Johnson upper bound—so in fact the relevant exact-search question is whether 23 sorts in 75. A completed **YES** search/certificate would establish \(S(23)=75\); a sound **NO** result would be inconsistent with the stated upper bound and should trigger an audit. The paper’s lower-bound experiments are phrased as disproving budgets below their known upper bound. Its 18-element run uses \(C=53\), while the paper gives \(F(18)=54\). For \(n=23\), \(C=75\) is likewise one below the Ford–Johnson bound 76, making this the natural decision target.

**[Deduction]** A precise runtime or memory estimate for \(n=23\) cannot be derived from the published rows alone. The paper reports 48 threads and 768 GB for its main computations, but the explored-state counts vary sharply with threshold and bandwidth. The 16–18 rows—billions of states and tens to over a hundred hours—show that a near-information-bound search can be very expensive; they do not provide a defensible extrapolation to 23. Moreover, its \(n=28\) run explicitly uses zero bandwidth, so it does not demonstrate that the more aggressive advice regime needed at 23 will be cheap. The sound resource conclusion is: **plausible as an engineering project using the same core ideas, but no evidence-based estimate that the full run fits a particular time or memory budget.**

## Falsification and next decisive step

**[Falsification attempt]** I checked whether the neighbouring \(n=22\) and \(n=28\) paper runs support an easy extrapolation: they do not, because both use zero bandwidth, while the reported \(n=16\)–18 searches use nonzero bandwidth and have much larger explored-state counts. I also checked the advice note’s toy study: it explicitly lacks the efficiency-threshold coverage machinery, predecessor enumeration, and symmetry handling needed for large \(n\), so its reductions cannot be used as an \(n=23\) runtime claim.

The specific blocker is **unmeasured search volume at the 23-element parameters**, not a mismatch between the paper’s adaptive sorting model and `docs/problem.md`. The next decisive step is to implement or obtain the paper’s full predecessor-generation, congruence, and efficiency-threshold machinery, then run a smaller parameter-calibrated pilot that reports forward/backward state counts, unknown entries, I/O, and peak memory. Until then, \(75\) is a candidate—not a computed exact value—and there is no defensible n=23 search cost estimate from the published parameters alone.

## Output 123 (msg_1aceba208001WSI22Kq0w0DGnR)

The interrupted task appears to have completed its **read-only investigation**: it reported the interval \(75\le S(23)\le76\), assessed the Stober–Weiß search parameters, and stated that no search was run.

I checked the working tree and durable records: Git is clean, HEAD is unchanged at `6a96398`, and no new \(n=23\) files or research notes are present. Existing tracked literature references still describe \(n=23\) as open. I found no evidence of posts, commits, or other external side effects, so there is nothing to repeat or clean up.
