# antonina-Fl9K8Vx2wbWVyZKOVKvrgA-blow

Session: ses_e529a048affeYdfrMgjs3FQDtw
Workspace: /home/lubko/soring-fronts/fo-tc-combined-review-20261105
Created: 1793910504313; updated: 1793910543014

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1ad65fb900019M5h5cYjLbsnj8)

I’ll inspect the active problem, frontier entry, and literature guidance first, then formulate a precise certificate question and test whether its proof route can be justified without changing repository files.

## Output 56 (msg_1ad663aae001OPyZBkGTFLXgWK)

The key distinction is already explicit in the repository’s prior analysis: polynomial FO(TC) data evaluation and a polynomial verifier clock do not bound the size of a program realizing an optimal policy. I’m testing the stronger proposed certificate form now—whether an FO(TC) program can be checked universally for correctness and worst-case query count without exposing its execution tree.

## Output 72 (msg_1ad6654240010CbSE87H5ZGPUm)

## Finding

**[Deduction; paper proof]** For the specified fixed-variable `FO(TC)_v` interpreter, there is a polynomial-time *checker* for a supplied policy program’s universal root claim and query-depth bound—provided the checker is allowed to enumerate all input orders. This gives a precise certificate format, but not the requested non-enumerative certificate.

Let the certificate be a program `p` of size at most `b(n+k)`, with the fixed FO(TC) syntax, store encoding, and polynomial execution clock described in `docs/research-fo-tc-combined.md`. The verifier enumerates each permutation `X ∈ S_n`, simulates `p` using `X` to answer comparisons, and rejects if any run exceeds `k` queries, fails to halt within the clock, or emits an incorrect order. Its running time is at most

`n! · poly(n+k+|p|)`.

Acceptance is equivalent to this particular `p` sorting every order within `k` queries. Thus, if a polynomial-size such program exists, this format is a sound, complete certificate **for that program**. It does not prove that an optimal policy has a polynomial-size FO(TC) description.

The factorial verifier is polynomial in the explicit permutation list, but not in the unary threshold input length `N=n+k+1`. Therefore it does not establish NP membership of `SORT-BOUND-U`. Nor does it yield a polynomial-size certificate with a polynomial-time checker as posed in the frontier question.

## What the complexity bounds do—and do not—show

- **Data complexity:** For a fixed formula on an explicitly tabulated structure, evaluation is polynomial in the structure size. The repository’s direct truth-table argument gives `O(|φ|N^{2v})` for its fixed-variable fragment, subject to the stated table-indexing convention.
- **Program/formula size:** That bound includes formula length. It does not make an arbitrarily large formula or program polynomial-size in `n+k`.
- **Universal correctness:** A polynomial execution bound on each single order gives a straightforward verifier per order, not a polynomial-time verifier for the universal quantifier over `n!` orders.
- **Query depth:** Polynomial-time execution bounds total computation, not worst-case comparison depth `k`. The verifier must separately count `Ask` actions; it can do so during each enumerated run. Unbounded internal computation, repeated questions, and output validation must not be silently treated as comparisons.

There is a sharp boundary here: **an explicit comparison decision tree** cannot be the desired succinct certificate, since any correct tree has at least `n!` leaves. That is a rigorous obstruction to that particular format, not to all succinct FO(TC) certificates. A program description can be short while its execution tree is large; the leaf bound alone does not rule out certifying its all-orders behavior compactly.

## Conclusion

**[Open]** I find no independently justified polynomial-size, polynomial-time-checkable certificate that proves a succinct FO(TC) policy correct on all `n!` orders and bounds its worst-case comparison depth without enumerating executions or supplying some other sound global invariant. The established fixed-fragment evaluation bound does not provide that invariant. Conversely, it does not prove such certificates impossible.

So the falsifiable result is limited: universal policy verification by direct order enumeration costs `n!·poly(n+k+|p|)`, while explicit-tree certificates require `Ω(n!)` size. A stronger barrier for succinct program certificates, or an all-`n` completeness theorem for a specific compact proof format, remains unresolved. No repository files were changed.
