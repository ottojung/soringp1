# antonina-gQ3chIuMpVnEeVuVLEnzeD-rolling

Session: ses_e0c0ea7bfffekha3PDNoZtG5mx
Workspace: /home/lubko/soring-fronts/fotc-program-simulate-framed-dag-overhead-alln
Created: 1795094042746; updated: 1795094296566

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 298 (msg_1f3f3c773001SVuno4Gyr03vun)

**Mathematical finding: constant-overhead simulation is possible; no framed-DAG family forces superconstant FO(TC) program growth.**

**Claim attacked.** For every polynomial-size framed comparison DAG `D` of height at most `k`, is there a fixed-interpreter FO(TC) strategy program `p_D` whose text size is `O(|D|)` and which sorts every input within `k` comparisons? Equivalently, does some family of framed DAGs force superconstant program growth?

**Result (paper proof / deduction).** **Yes:** every such framed DAG can be simulated by a fixed-interpreter FO(TC) program with only constant overhead in text size. No family of polynomial-size framed DAGs forces superconstant growth, at least under the note’s fixed-interpreter/program-as-data convention.

**Why.** A framed DAG is an acyclic dataflow whose node annotations are computed by:

- root annotation: empty poset;
- edge annotation: add the comparison outcome, take transitive closure, apply the stored permutation;
- join annotation: intersect (meet) all feasible incoming annotations.

The interpreter state is exactly the current poset `P` plus a comparison-budget counter. Because node indices are topologically ordered (`v < child`), the annotation of every node can be defined by induction on the node index. In FO(TC) with a fixed formula, define `T(v,r)` for a relation `r` on keys by:

- `T(root,r)` is false;
- for a node `w`, `T(w,r)` holds iff, for every feasible incoming edge `(v,o)` into `w`, the relation in `v` corresponding to `r` under that edge’s inverse transformation is present, i.e. `T(v, f_{v,o}^{-1}(r))`.

This is a fixed-point over pairs `(v,r)` whose dependency is well-founded by node index. Hence FO(TC) can compute `T` with a fixed formula. The program then has one guarded rule:

> if there exists a node `v` such that  
> `(∀r)(T(v,r) ↔ P(r))` and `depth(v) = current_depth`,  
> compare the pair stored for `v`.

All nodes with the same `(P, depth)` are valid: the DAG already guarantees a completion within the remaining budget from each such node, so any existential witness is safe. The text contains only the fixed formula plus the DAG tables (nodes, depths, compare pairs, edges, permutations), so its size is `|D| + O(1)` bits. Thus the overhead is constant, not superconstant.

**Complexity consequence.** Fixed-interpreter programs are at least as succinct as framed DAGs: any polynomial-size framed certificate can be executed by such a program with no asymptotic loss. This does not by itself put `SORT-BOUND-U` in NP, because universal worst-case verification for arbitrary programs remains coNP-complete; it only says the framed-DAG route is not obstructed by a program-vs-DAG succinctness gap.

**Honest limits.**

- This is a paper-level definability argument, not a machine-checked theorem. The FO(TC) syntax for extracting witnesses `x,y` from the existential node and the exact data encoding of permutations are standard but not formalized here.
- It assumes the DAG is acyclic, explicitly lists feasible and infeasible branches, and has topologically ordered node indices, as in `scripts/check_framed_strategy.py`.
- It proves existence of an equivalent sorting strategy with the same height bound, not that the program follows the DAG’s exact node path. Join collisions can choose different witnesses, but all are safe by the DAG’s height bound.
- It does not solve framed-certificate completeness: no all-`n` polynomial-size framed DAG for exact `S(n)` is known, and `SORT-BOUND-U ∈ NP` remains open.
