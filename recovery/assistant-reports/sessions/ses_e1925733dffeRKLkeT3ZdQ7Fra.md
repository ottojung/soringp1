# antonina-vF18fZ62eyPLLNLqQAKcYT-influx

Session: ses_e1925733dffeRKLkeT3ZdQ7Fra
Workspace: /home/lubko/soring301-exec-reset-branch-profile-20261117
Created: 1794874445090; updated: 1794875047657

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 60 (msg_1e6e38ed3001I5OHqF2sJ4hRC3)

Inspected state first (no prior conversation artifacts beyond this prompt context): clean git worktree at `6a96398`, no `exec-report.md` existed, and no evidence of external side effects to avoid duplicating. I did not create Lean files, PRs, or board posts; the only change is the requested `./exec-report.md`.

Wrote concise evidence-labeled analysis to `exec-report.md` covering:
- **Definition/model (from docs):** exact-reset semantics, leaf partition/framing, and extension masses.
- **Stronger necessary condition (deduction/paper proof):** **LM-profile (leaf-mass profile divisibility)** — in any exact-reset tree every node/branch mass `M(v)` along every repeated-comparison path must satisfy `e(F') \mid M(v)` (each node is a disjoint union of `e(F')`-sized framed leaf classes), which is strictly stronger than global `e(F') \mid e(F)` by constraining root/branch mass profiles.
- **(a) Explicit pair distinguished (paper proof/deduction):** non-realizable `A_3 -> V_3` passes global divisibility (`6/2=3`) but violates LM-profile at the balanced antichain root (`3,3` not multiples of `2`), while realizable `A_2 -> C_2` satisfies LM-profile and is realized; thus LM-profile correctly distinguishes/rejects a case global divisibility admits.
- **(b) Insufficiency (deduction, with concrete stress case):** LM-profile is necessary but not characterizing due to (i) comparison-realizable split feasibility beyond arithmetic masses and (ii) exact framed leaf-shape/identity requirements; e.g. `A_4 -> V_4` passes depth-1/root arithmetic profile (`12,12` multiples of `6`) yet that alone does not certify a full exact framed realization.
- **Frontier relation (deduction, not an NP claim):** LM-profile is a local semantic filter that can falsify candidate exact-reset schemas inside framed certificates, but it does not resolve the polynomial-size framed-certificate completeness/soundness gap for exact-budget `S(n)` and implies no NP/coNP/PSPACE membership claim. Includes explicit “not claimed” limits.
