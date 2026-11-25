# sergeev-framed-compilation

## status

investigated

## origin

executive_manual

## agent_id

5YhPIhB8ElT61uanRQDJ8i-foresaw

## exit_state

clearexit

## question

Can Sergeev's group-insertion comparison sorter be compiled into a framed comparison DAG of height log2(n!) + o(n) with polynomially many framed states satisfying the checker grammar for all n? If not, pinpoint the exact obstruction (container state, interval scheduling, or join constraints).

## basis

Sergeev ceiling audits on board #301; certificate frontier says polynomial global control states remain open.

## falsifier

Give a complete compilation accepted by scripts/check_framed_strategy.py for large n with verified height/cost, or a rigorous proof that some required join is impossible due to frame incompatibility.

## implication

Would connect a known asymptotic sorter to certificate completeness at near-optimal height.

## finding_unverified

 way that resists collapsing to a small family of global control states under permutation frames. The obstruction is **global join constraints / frame incompatibility** arising from **coupled container state**, rather than just local insertion costs.

### Concrete attempt / falsification status
- **No complete compilation accepted by `scripts/check_framed_strategy.py` exists** for large $n$ achieving height $\log_2(n!)+o(n)$ with polynomial nodes (to my knowledge from the repo/docs). The checker exists and is used on small cases; the frontier is explicitly open.
- **A rigorous disproof in full generality is not obvious from first principles here.** The standard tools: the grammar is sound but not obviously complete; Parberry’s coNP-completeness is for arbitrary networks (different model), not directly ruling this out. Mahaney/sparsity are about class membership barriers, not about frame-compileability of a particular algorithm. The most defensible mathematical obstruction from the literature in-repo is the **polynomial global control states** / **join constraints from coupled containers**.
- **Most plausible exact obstruction:** there is no family of polynomially many slot-frame annotations $\{R_v\}$ closed under the required transitions and intersection joins that can represent all reachable coupled-container configurations of Sergeev’s group-insertion while achieving total excess $o(n)$. In other words, **frame incompatibility at joins** (forced by coupled interval/container states) prevents polynomial sharing; any sound framed DAG matching the asymptotic height must either use exponentially many states or introduce large forgetting loss that breaks $o(n)$ excess. The repo’s frontier calls for falsifying a proposed grammar or specifying one — currently no such grammar is known to exist and the structure strongly suggests the join constraint is the blocker.

### Complexity implication
If it were true (polynomial framed DAG at near-optimal height for all-n), that would yield a polynomial-size, checkable certificate for $S(n)\le \log_2(n!)+o(n)$ and connect Sergeev to certificate completeness — a major step toward $SORT-BOUND-U \in NP$ (still short of equality to $S(n)$ in general, and subject to all model caveats). Conversely, a rigorous proof of the obstruction above would mean the asymptotic algorithm does **not** automatically give NP certificates via this grammar; it would sharpen the boundary between “good comparison strategy” and “succinct checkable certificate” without implying P≠PSPACE or NP≠PSPACE.

### Honest limits
- I did not construct a counterexample certificate or a formal proof of impossibility. The obstruction is structural (from docs/literature in repo): coupled containers + intersection joins + permutation frames make polynomial global states non-obvious and unachieved. 
- Distinction: soundness of the checker is separate from completeness of the grammar for some optimal strategy; general-poset hardness results don’t transfer directly to $S(n)$ without reduction.
- No repository/Lean changes made (as requested). 

**Concrete next decisive test (to actually disprove):** attempt to model the first few levels of Sergeev’s group structure for some fixed $n$ as a framed DAG and see where joins force either exponential branching or loss of the $o(n)$-excess invariant; if impossible for a concrete case that’s a small falsifier, but all-n is the claim. The clean mathematical answer is the join/compatibility obstruction above.

## Other metadata

```json
{
  "finished_at": 1793560231.9596875,
  "started_at": 1793559716.015225
}
```
