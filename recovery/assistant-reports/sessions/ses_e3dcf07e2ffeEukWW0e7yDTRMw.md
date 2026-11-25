# antonina-4Ts7tQzb9Cng8Jf2SQngoB-flooding

Session: ses_e3dcf07e2ffeEukWW0e7yDTRMw
Workspace: /home/lubko/soring-fronts/curator
Created: 1794259351623; updated: 1794260154825

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 396 (msg_1c23d1e110015ASuWJbycnhytz)

Wrote 3 new fronts to `frontier-candidates.json` (validated: schema, slug lengths, field minimums, valid JSON). No Lean or other repository changes; only the requested file is untracked.

What I did:
- Read `AGENTS.md`, `docs/problem.md`, `docs/operations.md`, `docs/literature.md`, the research-plan/open-question notes, and the live #301 digest/ledger (466 prior fronts).
- Checked the newest #301 thread: height-two excess, GPC/Fibonacci closure, and the 2026-11-09 superadditivity note.
- Attacked one precise claim myself: strict superadditivity, `F(A⊔B) > F(A)+F(B)` for nonempty `A,B`. I exhaustively enumerated labelled posets with `|A|+|B| ≤ 6` (all pairs for totals ≤6) and found **zero** equality cases. That is evidence only, not a proof and not an all-`n` result.
- Also checked the second-difference law against exact `S(0..22)`; all values lie in `{0,1}`, and the open `S(23)∈{75,76}`, `S(24)∈{80,81}` bounds make `D(23)` range over `{-1,0,1,2}` — a decisive finite test.

Honest limits:
- The strict-defect front is still open; my finite check cannot rule out a larger equality pair. I did not claim the #301 restriction argument is invalid — only that cross-comparison transitivity makes strictness non-obvious.
- The height-three front is a local general-poset question, so I explicitly framed it as a **root bridge/equivalence** question rather than assuming any transfer.
- The second-difference front is a structural `S(n)` claim with no complexity-class consequence by itself.
- None of the three is claimed proved, verified, or known to change the `SORT-BOUND-U` complexity classification.
