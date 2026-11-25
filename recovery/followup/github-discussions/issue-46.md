# Issue #46: All-n optimal sorting strategy certificate completeness

Upstream: https://github.com/ottojung/soringp1/issues/46
State: closed
Created: 2026-10-22T19:46:08Z

High-priority research task: give a precise polynomial-time verifier for a symmetry-framed, ranked comparison-strategy DAG and determine what all-n polynomial-size completeness theorem would imply SORT-BOUND-U in NP. Prove that the verifier is sound and does not hide exponential checking. Either prove completeness for optimal antichain-root strategies, or find a rigorous counterexample to a specific proposed compression lemma. Separate reachable from adversarially forced states and general poset F(P) from root S(n). Avoid generic finite enumerations, speculative hardness transfers, and Lean formalization without a uniform complexity-relevant theorem. This GitHub issue is an assignment, not confirmation that an agent is running.

## Comments

### None — ottojung
Comment ID: 6349784375
Upstream: https://github.com/ottojung/soringp1/issues/46#issuecomment-6349784375

Literature triage (2026-10-22): Daniel Rutschmann, *Sorting under Partial Information with Optimal Preprocessing Time via Unified Bound Heaps* (arXiv:2604.12653, April 2026), obtains O(m) preprocessing and O(log e(P)) sorting time. This is asymptotically optimal, **not** a certificate for exact F(P). Likewise van der Hoog–Rutschmann (arXiv:2404.08468) gives Θ(log e(P)) comparisons, not the exact minimax value. Independent research should explicitly ask whether their maintained state (heap / poset decomposition) yields a polynomially checkable **exact** optimal-policy normal form for the antichain root. Test against the 7-key equal-e(P)=60 gadgets with different F(P). Loff–Milovanov (ECCC TR24-034) proves PSPACE-hardness for circuit-presented *general* decision-tree complexity; do not transfer that to the fixed unary sorting language without a uniform reduction. No Lean work until a completeness theorem exists.

---

### None — ottojung
Comment ID: 6352451938
Upstream: https://github.com/ottojung/soringp1/issues/46#issuecomment-6352451938

Superseded by the more precise [issue #47](https://github.com/ottojung/soringp1/issues/47), which now contains (i) a sound polynomial-time checker definition for forgetful, permutation-framed strategies, (ii) an implemented and CI-tested checker merged in [PR #50](https://github.com/ottojung/soringp1/pull/50), and (iii) concrete falsifiers for overly aggressive immediate DAG joins. The **polynomial-size completeness for height S(n)** remains completely open and is actively assigned under #47. Closing this overlapping tracking issue avoids duplicating research prompts; prior literature notes here remain available.

---

