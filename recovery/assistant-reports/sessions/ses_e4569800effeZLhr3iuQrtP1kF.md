# antonina-6jli1V1s9lfyojFJs79Ihj-funeral

Session: ses_e4569800effeZLhr3iuQrtP1kF
Workspace: /home/lubko/soring-fronts/curator
Created: 1794131787789; updated: 1794132478733

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 472 (msg_1ba9f874b001pXyIJWeSxIWuYa)

{
  "fronts": [
    {
      "id": "bidirectional-backward-frontier-exponent",
      "question": "For the Stober-Weiss bidirectional exact search at budget k, is the pruned backward frontier of posets on n keys at distance at most k from a total order always of size 2^{O(n log n)}, giving a uniform 2^{O(n log n)} exact algorithm for SORT-BOUND-U, or is there an all-n family with backward frontier 2^{Omega(n^2)}?",
      "falsifier": "An explicit all-n family of budgets k_n, for example k_n=C(n)+1, whose pruned backward frontier provably contains 2^{Omega(n^2)} pairwise non-isomorphic posets; or a fully uniform implementation with a proved 2^{O(n log n)} time bound.",
      "implication": "A sub-2^{n log^2 n} uniform algorithm would improve the best known exact evaluator and tighten the unary upper bound; a super-polynomial backward-frontier theorem would show the practical bidirectional method cannot be uniformized without a new state-compression theorem.",
      "basis": "docs/literature.md Stober-Weiss 2023 bidirectional search; docs/problem.md 2^{O(n log^2 n)} budgeted DFS; board #301 notes the non-uniform advice gap; no ledger front asks for the backward frontier's all-n exponent."
    },
    {
      "id": "constant-round-am-sortbound",
      "question": "Does SORT-BOUND-U admit a public-coin interactive proof with O(1) rounds and a polynomial-time verifier (membership in AM), or does every constant-round protocol fail on infinitely many unary inputs because the minimax game's alternation cannot be compressed?",
      "falsifier": "An explicit O(1)-round Arthur-Merlin protocol with perfect completeness and soundness error at most 1/3 for all n,k, or a proof that every constant-round protocol errs on an infinite unary family.",
      "implication": "AM membership would place the unary threshold in the polynomial hierarchy (AM is contained in Pi_2^P), a new upper bound below the known PSPACE bound; a lower bound would separate this minimax language from arbitrary PSPACE games.",
      "basis": "docs/problem.md PSPACE membership; docs/research-certificates-barriers.md soundness-versus-completeness gap; the ledger has alternation-block fronts but no interactive-proof or AM front."
    },
    {
      "id": "density-one-exact-sortnumber",
      "question": "Is there a uniform deterministic polynomial-time algorithm that computes S(n) correctly for all n outside a set of asymptotic density zero, or does every polynomial-time algorithm err on a positive-density set of n?",
      "falsifier": "A fully specified polynomial-time algorithm with a proved density-one correctness set, or a proof that every polynomial-time algorithm errs on a positive-density set of n.",
      "implication": "A density-one algorithm would be a new uniform upper bound weaker than P and would show the hard n are sparse; a positive-density error theorem would rule out generic-case evaluation and strengthen the worst-case barrier.",
      "basis": "docs/problem.md unary encoding and open SORT-BOUND-U in P status; board #301 exact values and Sergeev asymptotics; no density-one or generic-case front in the ledger."
    }
  ]
}

## Output 532 (msg_1baa0f6ec001uoajQZqEREFI4O)

Inspected state on `billy-dev` without repeating any action.

- Working tree: clean except the intended untracked `frontier-candidates.json`.
- `HEAD` unchanged at `6a96398`; no commits or posts were created.
- `frontier-candidates.json` exists, parses as valid JSON, and contains exactly the three proposed fronts with the required fields and length constraints.
- The durable frontier ledger does **not** yet contain those three IDs, so the candidates have not been imported. That import belongs to the deterministic keeper, not this curator turn.
- No uncertain or duplicated external effect remains.

No further work was performed; the prior turn's only durable effect was writing the requested candidates file.
