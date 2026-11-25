# SoringP1: explore FO(TC) strategy programs for exact optimal sorting

210 distinct messages in 5 pages.

## Original issue description

## Goal
Investigate whether the optimal adaptive comparison strategy for n distinct keys can always be encoded by a polynomial-size, polynomial-time executable logical program, especially in a carefully restricted FO(TC) (first-order logic + transitive closure) language. Target the unary threshold language SORT-BOUND-U = {1^n#1^k : S(n) <= k}. This is a distinct approach to compression of *decision rules/programs*, not just state DAGs. Coordinate with umbrella Antonina #301 and GitHub ottojung/soringp1 issue #47 (forgetful framed-DAG certificates).

## Candidate idea
  exists program p  forall total input orders X:
      Run(p,X) correctly sorts and uses at most k comparisons.
Here p specifies an *adaptive* comparison algorithm (not a fixed sorting network). Comparisons with input elements are explicit, charged oracle queries: no direct/free access to X. If programs have polynomial descriptions and a uniform polynomial-time per-input interpreter, correctness can be expressed with a fixed polynomial-time verifier under a universal second-order input-order quantifier. This establishes a Sigma_2^P upper bound for the subclass of strategies so representable. To capture actual S(n), we need a completeness theorem: whenever S(n)<=k, a program of this type of size poly(n+k) exists. Do NOT claim NP or Sigma_2^P membership for unrestricted S(n) without proving completeness.

## Research tasks
1. Define a precise syntax, semantics and cost accounting for an FO(TC)-based *strategy language*: mutable knowledge/state, selecting a next comparison, branching on outcome, output, termination, and worst-case comparison budget.
2. Prove polynomial **combined** evaluation complexity for growing guessed program texts. FO(TC)=NL in *data complexity for each fixed formula* is NOT a combined-time guarantee. Explore bounded-variable/arity logical fragments or a fixed interpreter with explicit uniform polynomial bounds; check expressive power lost by restrictions.
3. Build elementary examples (insertion sort, merge sort, small optimal sorters) in the proposed language, measuring program size and execution/comparison cost, including what a program observes from the unknown order.
4. State a rigorous falsifiable all-n conjecture: optimal S(n)-comparison sorters have polynomial-size programs with polynomial runtime in this language. Seek proof, specific counterexample/family to a proposed restriction, or a barrier. A short program that first exhaustively searches for the optimal tree does NOT satisfy the runtime condition.
5. Examine whether a logical program can simulate forgetful framed DAGs efficiently, and whether programmatic state rules compress any family that explicit DAGs cannot. Review finite-model theory (fixed vs combined FO(TC) checking), comparator/adaptive sorting literature, and known optimal comparison results.
6. Keep existential program choice separate from universal adversarial outcomes; explain why the universal verification step remains within Sigma_2^P only given a uniform polynomial interpreter, not simply by writing FO(TC) source code.

## Deliverable
Short research note: formally specified model, proven soundness/time bound, all-n exact-completeness statement, PROVED vs CONDITIONAL vs REFUTED findings, concrete next experiment. Avoid Lean formalization or irrelevant finite enumeration until an all-n complexity-relevant theorem emerges. Work on billy-dev only if using agents; issue creation alone is not agent execution.

## Last recorded review

{
  "commit": "c2bb64426be535c64874928ea5fd6d04572407c8",
  "rationale": "APPROVE the corrected research note at exact signed commit c2bb64426be535c64874928ea5fd6d04572407c8 (parent 46125a87b0af019be4ba6b38859498db22c64f19; branch is 2 commits ahead of main and 0 behind). Independent re-derivation confirms the fixed-v table evaluator: each TC context has a+2m<=v; memoized body tables feed Floyd-Warshall on N^m nodes, total N^(a+3m)<=N^(2v), with nested subformula tables computed once. The outer verifier now checks sorted output against each universally quantified X, while the program itself sees only charged query answers. B2 has been narrowed to the exact greedy child-e selector and explicit full-frontier enumeration; it no longer presents those as a hardness result for exact minimax. Verified by execution on this exact checkout: python3 -m unittest discover -s tests -v (168 tests, pass), git diff --check, and GPG signature. This approves the bounded research claims only. GitHub Actions has no run for this branch head and no PR is open; do not integrate to main until the applicable exact-head Actions check is green. All-n exact-budget completeness and any class claim for unrestricted SORT-BOUND-U remain open.",
  "recordedAt": "2026-10-24T10:00:29.979Z",
  "reviewer": "Viche Executive",
  "verdict": "approve"
}

## Pages

- [Page 1](page-001.md)
- [Page 2](page-002.md)
- [Page 3](page-003.md)
- [Page 4](page-004.md)
- [Page 5](page-005.md)
