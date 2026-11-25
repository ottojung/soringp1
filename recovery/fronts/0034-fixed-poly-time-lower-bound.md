# fixed-poly-time-lower-bound

## status

investigated

## origin

ai_proposal_unverified

## agent_id

Ci3DrtqsrHv7Jh3kS0YIxh-hide

## exit_state

clearexit

## question

For some fixed constant c >= 2, is SORT-BOUND-U not decidable in deterministic time O(N^c) on unary inputs of length N, or is there an all-n construction beating every fixed polynomial?

## basis

docs/problem.md states fixed-polynomial lower bounds like SORT-BOUND-U not in DTIME(N^2) are not blocked by open separation but have no known technique; docs/research-budgeted-dfs.md gives exponential time upper bounds with no general polynomial-time lower bound established.

## falsifier

Prove SORT-BOUND-U in DTIME(N^c) for some fixed c>=2 via a uniform algorithm, or derive an unconditional Omega(N^c) time lower bound for all c from the model without assuming P!=PSPACE.

## implication

Establishing a fixed-polynomial time separation (even if not super-polynomial) would be a nontrivial complexity consequence and is not obviously blocked by PSPACE membership or P/poly circuit triviality.

## finding_unverified

avy search. No known all-$n$ polynomial method. Theorem 6.6 suggests “cheap” combinatorial recurrences are insufficient; need a genuinely efficient, exact, all-$n$ representation of the minimax strategy. I found no path to polynomial time.

**Try to get an unconditional fixed-poly lower bound $\Omega(N^c)$ for all fixed $c$:**
- Time hierarchy gives $\mathrm{DTIME}(N^c) \subsetneq \mathrm{DTIME}(N^{c+\epsilon})$ but the separated language is diagonal/artificial. Applying directly to a natural language is nontrivial. 
- $\mathrm{SORT\!-\!BOUND\!-\!U}$ is sparse + in $\mathrm{P/poly}$; diagonalizing “against all machines of time $N^c$” while preserving consistency with *some* valid $S(n)$ (the true sorting number function) is hard - the diagonal must flip answers without breaking the combinatorial/monotonicity constraints of an actual comparison-sort minimax function. Theorem 6.6 is an explicit warning: you can satisfy those constraints and still be non-P by diagonalization on a constructed $G$. 
- Reductions from time-hierarchy complete problems seem blocked by sparsity/encoding and by the fact that no obvious NP-hardness/PSPACE-hardness is established and many transfers fail (Hyafil–Rivest, binary/unary embedding). Circuit lower bounds don’t help (P/poly trivial). 
- No known technique achieves this for a natural PSPACE language in P/poly; problem states “no known technique”.

### Distinctions (important)
- **Uniform vs nonuniform:** $\in \mathrm{P/log}$ nonuniformly doesn’t imply uniform P (Theorem 6.6). 
- **Certificate soundness vs completeness:** exponential tree is a sound witness in size but not poly; NP membership remains open. Fixed-poly time decidability is different from poly-size verifiability. 
- **General posets vs antichain/sorting:** results about arbitrary posets/tests don’t transfer to pairwise comparisons / fixed antichain root. 
- **Fixed poly vs super-poly:** fixed-poly separation (e.g. not in $\mathrm{DTIME}(N^2)$) is a different question than showing not in P; both have “no known technique” per problem statement.

### Conclusion (honest limits)
- **No disproof found** for either side. 
- **Main obstruction to upper bound:** no all-$n$ exact polynomial method known; exponential DFS is the best uniform bound recorded. Theorem 6.6 shows recurrence arguments are insufficient.
- **Main obstruction to fixed-poly lower bound:** no known diagonalization/reduction technique works for this sparse natural language in $\mathrm{P/poly}\cap \mathrm{PSPACE}$ without assuming stronger separations; time hierarchy gives structure, not a lower bound on a specific combinatorial function. Also need to ensure diagonal is realizable as some valid $S(n)$-consistent function (nontrivial). 
- **Exact obstruction:** **technique gap**, not an obvious theorem blocking it. The complexity consequence (fixed-poly separation) is noted as nontrivial and not obviously blocked, but I cannot derive $\Omega(N^c)$ for all $c$ or construct a poly-time algorithm now. I would not create Lean/repo changes without a substantive independently checkable theorem/counterexample.

**Recommendation:** treat as open; next decisive step would be either (1) find a strong all-$n$ structural characterization of $S(n)$ enabling a poly-time recurrence, or (2) identify a reduction from some fixed-time complete language to $\mathrm{SORT\!-\!BOUND\!-\!U}$ preserving unary sparsity/realizability as a valid comparison-sort function. Neither is obvious from current literature.

## Other metadata

```json
{
  "finished_at": 1793333063.19071,
  "started_at": 1793332089.6632926
}
```
