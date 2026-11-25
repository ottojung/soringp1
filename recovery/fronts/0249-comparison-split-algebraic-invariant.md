# comparison-split-algebraic-invariant

## status

investigated

## origin

executive_commissioned

## agent_id

1z0Whd2X2vJJOT7FOmTmn2-faint

## exit_state

clearexit

## question

Find an algebraic/combinatorial invariant preserved in some form across optimal splits that explains S(n) > ceil(log2(n!)) for specific n (starting from n=12).

## basis

Gaps at n>=12 irregular; no known general invariant explains them.

## falsifier

Show the invariant is violated by some known optimal strategy or is equivalent to already-known bounds.

## implication

A general invariant would characterize the gap set and inform lower bounds on search.

## finding_unverified

n gives 1 bit of information in the worst balanced case.

Or perhaps the "graph entropy" or other things. Or maybe related to the "algebraic complexity" - but comparisons are not algebraic operations on values in that sense.

Alternatively, let us look up the full board #301 more if possible through the API style? Or look in commit messages / other files. Also look up the soring301 repo more.
Let us look up more about the structure of states at the critical level for n=12 if possible? Or look up known results about the "split invariant".

**Mathematical finding (no proof):** there is no known algebraic/combinatorial invariant preserved across optimal splits that explains $S(n)>\lceil\log_2 n!\rceil$ starting at $n=12$; the obstruction is global routing/structural, not a scalar monotone invariant.

**Evidence from primary literature + repo experiments:**
- Efficiency pruning is *definitionally equivalent* to the node-level information bound (Wells/Peczarski/Stober–Weiss) — not a stronger invariant ([n12-nontightness §4], `[deduction]`).
- Sortability is not monotone in $e(P)$: at $n=6$ there are pairs with $e(P_1)<e(P_2)$ but $m(P_1)>m(P_2)$ (9960 witnesses). At $n=5$ same $e$ gives different $m$ ($e=8,m\in\{3,4\}$). Peczarski’s $n=13$ $P_{16}/Q'_{16}$ shows fewer extensions can be harder. Any invariant depending only on $e$ (or efficiency/slack ratio) is falsified ([§5 H2/H3], `[experiment]`).
- Forced balanced prefix occurs at tight values too ($n=5,10$) so not predictive of the $n=12$ gap ([H4]). Symmetry neither necessary nor sufficient ([H6]).
- Compositional gaps appear for disjoint-union-of-chains/merge factors (Theorem B gives strict bound e.g. $Merge(2,4), n=6$) but this is a property of series/parallel structure, not obviously “preserved across splits” of the antichain; the global antichain obstruction is established only by exhaustive search (Wells/Stober–Weiss) with no compact published certificate.
- The winning frontier shows exponentially many $(1/4-o(1))n(\log n)^2$ nonisomorphic winning states survive info pruning ([winning-frontier-barrier]) — consistent with large state space, no small invariant.

**Concrete failed approach / exact obstruction:**
Tried to imagine algebraic invariants preserved by splits (group/sign invariants of $S_n$, factorial number system coordinates, poset dimension, shelling polynomials). None survive falsification: comparison splits are local operations producing arbitrary valid partitions depending on strategy/poset; hardness is non-monotonic and global. The only known “invariants” that give bounds are either equivalent to leaf counting or are structural decompositions (merge factors) that don’t transfer to explain the antichain gap as an invariant preserved across optimal splits.

**Complexity/soundness note:** efficiency/info bound is sound; stronger invariants would need to be non-scalar and strategic. Certificate *soundness* vs *completeness* is the issue — current pruning is equivalent to information bound (complete as necessary condition) but not sufficient; no known sound strengthening that’s simple/general. Also unary $SORT\!-\!BOUND\!-\!U \in PSPACE$ means lower bounds on $P/NP$ are equivalent-separation results (out of scope), while upper bounds/structural barriers/certificates are the frontier.

**Honest limits:** no new theorem/counterexample found. The question remains open (literature confirms no human-readable invariant/certificate for $S(12)>29$). No repo/Lean changes proposed.


## Other metadata

```json
{
  "finished_at": 1793726312.9156845,
  "started_at": 1793725001.106176
}
```
