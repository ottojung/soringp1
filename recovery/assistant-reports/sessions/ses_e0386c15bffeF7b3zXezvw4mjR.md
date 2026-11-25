# antonina-jTBbewx7rtcvGE69fRCTVM-ocean

Session: ses_e0386c15bffeF7b3zXezvw4mjR
Workspace: /home/lubko/soring-fronts/framed-dag-exact-position-polynomial-20261121
Created: 1795237166830; updated: 1795237708216

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 667 (msg_1fc816c6c001mJtNJc1Vp5ZG2W)

Posted to #301.

Result summary:

- **n=5:** FJ-schedule framed cert = 199 nodes, depth 6 → checker **REJECT** (`leaf 10 does not sort 1,3`).
- **n=6:** cert = 1055 nodes → checker **REJECT** (`leaf 27 does not sort 1,5`).
- **Exact-position sharing attempt:** keying shared nodes on the full frame signature fails before construction with a **CHILD CONFLICT**: node `(compare [4,1], identity frames)` needs child `(compare [4,2])` with two incompatible frame pairs:
  - `perm_lt [0,1,3,4,2]`, `perm_gt [1,2,3,0,4]`
  - `perm_lt [1,2,4,0,3]`, `perm_gt [0,1,2,4,3]`

Obstruction: zero-comparison insertions in the FJ insertion stage attach a slot move to a preceding comparison edge; that move is positional but its correctness depends on the value state before the edge, not only the outcome prefix. Exact winner positions do not remove this value dependence, so exact-position sharing still forces value-dependent frames. Soundness requires splitting that propagates upward, ruling out a polynomial-size sound framed DAG at exact `F_FJ(n)` height under this schedule. No repo/Lean/CI changes were made.
