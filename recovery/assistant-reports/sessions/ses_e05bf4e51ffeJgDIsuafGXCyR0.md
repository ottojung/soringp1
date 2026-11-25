# Literature search halving sortability

Session: ses_e05bf4e51ffeJgDIsuafGXCyR0
Workspace: /home/lubko/soring-fronts/halving-obstruction-infinitude-allr
Created: 1795199906281; updated: 1795200202107

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 5 (msg_1fa40b23a001z2pcdSrajRSXSY)

I'll research this question thoroughly using web searches, then dig into primary sources. Let me start with parallel searches on the key leads.

## Output 28 (msg_1fa40c0c7001qk9rtwgp3Kp0UQ)

The searches got cancelled. Let me retry them.

## Output 39 (msg_1fa40c987001sGiTVeitm4mK7q)

Web search seems unavailable. Let me try fetching directly from search engines and known sources.

## Output 54 (msg_1fa40d539001diCI1vmptIx3Xf)

DuckDuckGo works. Let me run several searches in parallel via that engine.

## Output 73 (msg_1fa40e89e0014UoihBZ3rxDGTj)

I found the key Hanamura–Iwata paper. Let me fetch its details and run more targeted searches on the core concepts.

## Output 92 (msg_1fa412053001tIRNu9QDpMdFS8)

Excellent lead: Peczarski's "Gold Partition Conjecture" concerns exactly S(P) vs log e(P). Let me dig into that and related primary sources.

## Output 111 (msg_1fa41558b001STztJNq3wQ7Neb)

Very helpful. Now let me find the precise literature on "perfectly sortable" / when ceil(log2 e(P)) is attainable, and get the Hanamura–Iwata introduction which likely cites the key results.

## Output 130 (msg_1fa417f82001UU2uzmJB7iXX8J)

Let me try to access the Hanamura–Iwata full text and search for the specific "perfectly sortable" terminology and power-of-two examples.

## Output 149 (msg_1fa41a16a0016rOkRJJ3Lyuw4B)

DuckDuckGo is now showing a captcha. Let me retry the websearch tool and try alternate search endpoints.

## Output 173 (msg_1fa41ba520016Xv9vgWEMeebiu)

Search engines are unreliable now. Let me use academic APIs directly (Semantic Scholar, OpenAlex) to get the Hanamura–Iwata paper's abstract, open-access PDF, and references.

## Output 188 (msg_1fa41cde4001CZ4zR5YZTNKPK0)

Let me resolve the Hanamura–Iwata references via OpenAlex to identify the foundational literature.

## Output 199 (msg_1fa41e179001mbMUT30mY0euwj)

Let me search academic databases systematically for the specific concepts.

## Output 210 (msg_1fa421da5001qxha0C7hyQ2uLJ)

Let me retry search engines after the delay and also query arXiv/Crossref for more specific literature.

## Output 229 (msg_1fa4251b0001f7VU7eMGFk7Dqw)

Let me query Crossref and search for the "efficiency"/pruning terminology and older poset-sorting literature.

## Output 240 (msg_1fa42768d001O1kiiDVbv4d6CF)

Let me check the repo's own literature notes (read-only) for relevant leads, and try to get the Hanamura–Iwata introduction text.

## Output 336 (msg_1fa4338b1001o0Doirsfg2CS9H)

Let me do a final round of targeted searches, including the recent GPC paper and the specific "1-perfect"/binary terminology.

## Output 355 (msg_1fa436167001ylriuQbH6kp1se)

The recent GPC paper uses the term "half-balanced pair" — let me check Peczarski's 2017 "Comments" paper, which may contain the relevant discussion.

## Output 379 (msg_1fa438d8d001dcaMGmIGE5FhCT)

Found an infinite family paper on small balance constants. Let me read both it and Peczarski's 2017 comments.

## Output 394 (msg_1fa43ba960012UxqVOuR4aDjoV)

I have strong literature context now. Let me run a quick in-memory computation (no files) to determine whether small power-of-two counterexamples actually exist, which will help calibrate what is "known."

## Output 405 (msg_1fa44090e0013fF8cewuFdtz7Z)

Let me verify the computation with a focused debug on the small cases before drawing conclusions.

## Output 425 (msg_1fa445a1a001DA3q0YZoh5lAlf)

Let me do one final check for poset-specific optimal-sorting literature by the same authors and older work.

## Output 436 (msg_1fa448518001IlEwG0e2Mlylv3)

Let me check two foundational papers on "how good is the information-theoretic bound" — these are directly relevant.

## Output 465 (msg_1fa44e880001WVgOQ4LmSfeX4w)

## Report: literature check on exact sorting of power-of-two posets

**Bottom line:** I found no published theorem, named result, or explicit example answering your exact question. The *general* phenomenon is well documented, but the restriction `e(P) = 2^r` does not appear in the literature I could access. Below is what is known, what is elementary, and what I verified computationally.

---

### 1. Is exact halving necessary for cost `r`? — Yes (elementary deduction, not a named theorem)

If `e(P) = 2^r` and `S(P) = r`, the worst-case decision tree has depth `≤ r` and must have `2^r` distinct leaves (one per linear extension), so it is a *perfect* binary tree: the root splits `2^(r−1)/2^(r−1)`, and the same holds recursively at every internal node. The same argument shows recursively that cost `r` is equivalent to existence of a complete halving tree.

For `e(P)` *not* a power of two this fails (there is slack in the tree), which is exactly why Hanamura–Iwata's result is nontrivial.

Terminology in the literature: an incomparable pair with `e(P+xy) = e(P+yx) = e(P)/2` is a **"half-balanced pair"** (Peczarski 2017; Gupta 2026). I did not find the necessity direction stated explicitly, but the *sufficiency* direction is standard: Peczarski (2017, §3) and Gupta (2026, §2) use a half-balanced pair as an immediate certificate.

### 2. Do power-of-two posets with no halving exist? — Yes in fact; explicit small examples are easy to generate, but I found none published

- My in-memory enumeration (all upward DAGs on `n` labelled vertices, exact `e(P)` by ideal DP, exact `S(P)` by minimax recursion) found:
  - `n=5`: **16** posets with `e=8, S=4` (e.g. Hasse edges `0<3, 0<4, 1<2, 1<4, 2<3`).
  - `n=6`: **512** posets with `e=16, S=5` (e.g. edges `0<1, 0<3, 1<5, 2<3, 3<4`).
  - `n=7`: random search found `e=32, S=6` (edges `0<1, 0<3, 0<4, 0<5, 1<3, 1<5, 1<6, 2<4, 3<4, 5<6`).
  - At `n=5`, all `e=8, S=3` posets have a half-balanced pair; all counterexamples lack one — consistent with §1.
- Infinite family: ordinal sums of any counterexample give `e(P⊕Q)=e(P)e(Q)` and `S` additive, so `k` copies of the `e=8, S=4` example give `e=2^(3k), S=4k`. Trivial once one example exists.
- **Caveat:** these are my computations reported as *experiment/deduction*, not literature. I found no paper that publishes these small examples or an infinite power-of-two family.

### 3. Closest published results (all about the general, non-power-of-two case)

- **Exact halving failure in general:** Linial, *The information-theoretic bound is good for merging*, SIAM J. Comput. 13 (1984) 795–801 — "in many situations such an efficient query which splits the compatible solutions into two sets of equal size does not exist"; proves a constant-factor `C = (log₂((1+√5)/2))⁻¹ = log₂φ ≈ 1.44` for width-2 posets (the origin of the GPC constant). Theorem 1.1: the worst merging problems requiring `n` comparisons have exactly `F_n` (Fibonacci) extensions — again not powers of two. [PDF](https://www.cs.huji.ac.il/~nati/PAPERS/inf_th_merging.pdf)
- **Balance constant / 1/3–2/3 conjecture:** δ(P) < 1/2 implies *no* exact-halving pair. Known infinite families with δ bounded away from 1/2: the 3-element poset `T` (δ=1/3); Saks/Brightwell worst-balanced posets; Peczarski, *The worst balanced partially ordered sets—ladders with broken rungs*, Experimental Mathematics (2019); Evan Chen, *A Family of Partially Ordered Sets with Small Balance Constant*, EJC 25(4) (2018) #P4.43, family `P(5k,5k)` with δ → κ ≈ 0.3489. None have `e(P)` a power of two.
- **Gold Partition Conjecture (GPC):** Peczarski, Order 23 (2006) 89–95, `S(P) ≤ log_φ e(P)`; verified through 14 elements by Gupta, arXiv:2607.23926 (2026). Upper bound, not a characterization of attainability.
- **Minimum-comparison sorting framework:** Knuth TAOCP vol. 3 §5.3.1 (efficiency `E(P)=n!/(2^c e(P))`); Stober–Weiß, arXiv:2206.05597 (Observation 2.2: `e(P)>2^r` ⇒ not sortable in `r`). Hanamura–Iwata, IPL 111 (2011) 365–369, *Posets with seven linear extensions sortable by three comparisons* ([DOI](https://doi.org/10.1016/j.ipl.2011.01.004)) — shows `ceil(log₂ e(P))` achieved for `e=7`. Fredman, TCS 1 (1976), *How good is the information theory bound in sorting?* is the foundational reference I could not retrieve in full.

### 4. Honest assessment

- **Known / trivial:** exact halving at the root (and recursively) is necessary for cost `r` when `e=2^r`; sufficient if a complete halving tree exists; the general "ITB not always attainable" phenomenon and infinite families with no half-balanced pair are published.
- **Not found:** any statement characterizing *when* `S(P)=log₂ e(P)` for power-of-two posets; any published `e=8/16/32` counterexample; any published infinite power-of-two family; any named theorem for this. The question looks like a clean elementary observation plus a small computational fact, not a rediscovery of a known theorem — but I cannot prove a negative from exhaustive search, and I did not obtain the full text of Hanamura–Iwata or Fredman 1976 (both paywalled; Hanamura–Iwata's references are all about minimum-comparison sorting of *n* elements, not power-of-two posets).

No files were modified.
