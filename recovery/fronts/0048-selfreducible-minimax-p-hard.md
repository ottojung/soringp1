# selfreducible-minimax-p-hard

## status

investigated

## origin

ai_proposal_unverified

## agent_id

yTOEmRQdzagItZjRLSOlEG-monthly

## exit_state

clearexit

## question

Is the unary threshold language SORT-BOUND-U P-hard under log-space many-one reductions via self-reducibility of the poset minimax recurrence, or does the sparse unary encoding and the antichain structure block all known P-hardness reductions?

## basis

AGENTS.md states SORT-BOUND-U in PSPACE; P/log nonuniform membership and sparsity give Mahaney barriers for NP but leave P-hardness questions open under weaker reductions.

## falsifier

Construct an explicit log-space reduction from some P-complete problem to SORT-BOUND-U preserving the threshold structure, or prove a log-space reduction is impossible given sparsity and the comparison-tree model constraints.

## implication

P-hardness would place SORT-BOUND-U between P and PSPACE and sharpen the complexity classification without requiring a full P!=PSPACE separation or relying on NP membership.

## finding_unverified

ook at frontier ledger.

Let us proceed with the analysis.

**Finding (mathematical):** No logspace many-one reduction from a P-complete language to `SORT-BOUND-U` exists by the standard reduction schema; the obstruction is structural, not just sparsity.

**Obstruction 1 - reduction form forces dependence only on (n,k):** Any logspace (hence polynomial-time) many-one reduction `f` to `SORT-BOUND-U ⊆ {1}^*#\{1\}^*$ is `f(x)=1^{n(x)}\#1^{k(x)}` with `n(x),k(x)` logspace computable. Thus `x \in L \iff S(n(x)) \le k(x)`. For fixed `n`, membership in `L` for all `x` with `n(x)=n` is identical up to the interval of `k(x)` relative to fixed `S(n)` (and `k(x)` must be computable in logspace from `x` to satisfy the reduction). For a P-complete `L \nsubseteq \mathsf{L}` this is generally impossible (would force deciding `L` via computing `n(x),k(x)` and testing `S(n(x))\le k(x)`; if `n(x)` fixed impossible to encode `L` without computing it, if `n(x)` varies still need to align to fixed `S(n)` without already deciding `L`). More directly, `L` would need to be a “logspace threshold” of the fixed function `S` composed with logspace projections — a structure incompatible with P-completeness.

**Obstruction 2 - antichain/symmetric game model:** The “self-reducibility of the poset minimax recurrence” moves through poset states, but the instance is only the antichain of size `n`. `S(n)` depends solely on `n` (symmetric initial state), not on arbitrary encoded data. The allowed moves are only pairwise comparisons building up order constraints (a highly restricted test family) starting from empty poset. This is far weaker than arbitrary tests (Hyafil–Rivest) or arbitrary AND-OR games; embedding an arbitrary circuit/computation requires encoding instance structure, which the antichain provides no way to do. The comparison game is a sorting/identification game, not a universal computation simulator.

**Notes on known barriers:** Sparsity gives Mahaney barriers for NP (many-one) and blocks many-one EXPTIME-hardness (Berman–Hartmanis) — consistent with obstruction to many-one hardness above P as well. P-hardness under logspace many-one reductions is not obviously ruled out by sparsity alone for arbitrary sparse languages in principle, but combined with (1)+(2) it is blocked for this specific function-threshold of `S(n)`. Also `SORT-BOUND-U \in \mathsf{PSPACE}` is known; P-hardness would not imply collapse alone, but the reduction as stated is not constructible and has no obvious bridge.

**Concrete failed approach / exact obstruction:** Trying to “use self-reducibility of the minimax recurrence” reduces to evaluating that recurrence on some poset built from a P-complete instance; to reach `SORT-BOUND-U` one must start from the antichain and the value is `S(n)`. No known construction embeds arbitrary P computations into the antichain comparison game or makes the fixed threshold `S(n)$ encode arbitrary instance satisfiability via logspace-computable `(n(x),k(x))`. I found no explicit logspace reduction and the structural constraints above are blocking.

**Honest limits:** This is a negative/obstruction argument, not a formal proof that `SORT-BOUND-U \notin \mathsf{P\text{-hard}}^L$. A clever encoding might exist in principle, but it would need to circumvent (1) and/or (2) in a non-obvious way. No such construction is known in the literature reviewed, and the antichain symmetry + function-of-n form strongly suggests obstruction. No repository/Lean changes made.

## Other metadata

```json
{
  "finished_at": 1793350380.143967,
  "started_at": 1793349592.1695747
}
```
