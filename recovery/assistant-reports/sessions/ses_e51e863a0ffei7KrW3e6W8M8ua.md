# antonina-lPG8mL56zr7uDttOwK6bAh-cents

Session: ses_e51e863a0ffei7KrW3e6W8M8ua
Workspace: /home/lubko/soring-fronts/parallel-reversal-congruence-20261106
Created: 1793922145378; updated: 1793922165317

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 60 (msg_1ae17cd20001u0LKX5M5ogyQz2)

The question is whether a **sound, polynomial-time checkable** adversary invariant can force a comparison obstruction from the initial n-element antichain under *every* sorting strategy. Based on the repository's existing research notes:

- **`research-one-ply-obstruction.md`** defines the one-ply bound `L1(P)`, which is sound (`L0 ≤ L1 ≤ F`) and can be strictly stronger than leaf counting (smallest witness `W = (26,0,10,0,8)`, `e=8`, `L0=3`, `L1=4=F`). However, computing `L1` requires exact linear-extension counts `e(P)`, which is **#P-complete**; the note explicitly states it is *not* polynomial-time computable and makes no P/NP claim.
- **`research-obstruction-next.md`** shows that low-dimensional scalar invariants (`(e,width)`, `(e,width,#min,#max)`) all fail to determine `m(P)`, and that merge-type substructures do not explain the frontier witness. There is no known compact invariant that forces obstruction from the antichain for all `n`.
- **`research-structural-lower-bounds.md`** establishes `e(P)` alone does not determine `S(P)` (Prop 5.1, `n=5`, `e=8` pair), and `SORT-BOUND-U ∈ P/log` only nonuniformly.

**Conclusion (option (c)):** This is already blocked/resolved as an open frontier with evidence. No polynomial-time checkable invariant is known; any such invariant would decide `S(n)` in polynomial time, which is exactly the open question. The distinction between (i) a hard reachable poset and (ii) a poset an adversary can force against every height-k root strategy is preserved throughout — the one-ply bound `L1` addresses (ii) but is not polynomial-time. No repository edits or external posts made. Independent-check pointers: `scripts/one_ply_obstruction.py`, `tests/test_one_ply_obstruction.py`, `scripts/obstruction_probe.py`. No claim of final `SORT-BOUND-U` resolution.
