# antonina-sPjXgjY52OtEv31yNUdVpq-transient

Session: ses_e03745cb5ffe3IT0iZNP6P9XyZ
Workspace: /home/lubko/soring-fronts/exec-defect-merge-shape-counterexample-20261121
Created: 1795238372272; updated: 1795241617188

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 778 (msg_1fcbd1290001jCIR0qGrmmhemA)

The finding has been posted to Antonina issue #301 as a single comment (timestamp 2026-11-21T06:13:19.605Z). No repository, Lean, test, or ledger changes were made; all scratch work stayed under /tmp/opencode.

Summary of result:
- No counterexample found to the disjoint-union defect inequality F(A⊔B) ≥ F(A)+F(B)+min(|A|,|B|)+1 in the Merge-shape / local-gap family.
- Search6 evaluated 587 pairs with 0 budget-exceeded and 0 violations; min surplus = 0.
- The stronger variant with +g(A)+g(B) is refuted (121/587 violations, min stronger surplus −1), e.g. a non-tight 5-poset with a singleton: F(A⊔{x}) = F(A)+2.
- Structural reason: a +1 component local gap raises both F(component) and F(union) by one unit (“self-healing”); the min+1 cross-comparison bound absorbs exactly one unit, not the full local gap.

Task complete.
