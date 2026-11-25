# n23-barrier-decomposition

## status

investigated

## origin

executive_proposed

## agent_id

1RlQ0kcWCmEZv50d5Leehu-dmitri

## exit_state

clearexit

## question

What structural invariant generalizes the n=12 obstruction (where information bound is not met) to force a gap for n>=23 in a way that is checkable without exhaustive backward search over all posets, and can such an invariant yield an improved lower bound on S(n)-log2(n!) that holds for an infinite family?

## basis

Exact values known only up to n<=22 (Stober–Weiß 2023); n=23 open; docs/research-one-ply-obstruction.md, research-n12-nontightness.md discuss obstructions and non-tightness of information bound.

## falsifier

Show the n=12 gap has no infinite-family generalization or find a uniform decomposition that makes n>=23 gaps provably avoidable by some strategy class not captured by current invariants, with explicit counterexample.

## implication

A generalizable obstruction invariant would improve the effective lower bound and constrain search for open values without requiring full enumeration, relevant to exact evaluation of unary SORT-BOUND-U.

## finding_unverified

t F = F(W)+F(C_t)=4 constant while n grows. On antichains P0_n, comparing any pair gives children with e = n!/2, so L0(child)=L0(P0_n)-1, L1(P0_n)=1 + (L0(P0_n)-1)=L0(P0_n) — no gap. Hanamura–Iwata show a poset with e=7 is sortable in ⎡log2 7⎤=3 (tight below). [deduction/experiment/literature]
- **Exact frontier.** Values known up to n≤22 (Stober–Weiß 2023), n=23 open. The budgeted/transcript DFS gives uniform upper bounds for SORT-BOUND-U (PSPACE/EXPTIME depending on encoding) but no known general lower-bound invariant forcing a gap for large n.

### Falsification attempt (concrete)
Tried to construct an all-n invariant I(n)=f(n)-C(n)>0 checkable without exploring poset classes:
- **n-alone scalar (slack/ceiling):** 2^C(n)/n! varies but doesn’t predict state admissibility; fails on monotonicity and doesn’t explain which n reach bad states. Falsified.
- **Local ply on root:** L1 gives 0 on antichains for all n>=1. Cannot force gap on P0_n. 
- **Suffix families:** give fixed gap but irrelevant to antichain root and don’t grow with n; can’t force gap for large n on S(n)=F(P0_n). 
- **Class-based (symmetry/congruence):** matches Peczarski’s observation but is exactly what backward search enumerates (congruence classes of bottleneck posets) — not checkable without exploring the class graph; no known closed form/computable test from n alone.

No counterexample found to “infinite family forced gap”, but no generalizable invariant exists either. The obstruction is the path: the minimax tree reaches “information-bound-missed” states depending on history; you can’t read it off n or a single root scalar without the search.

### Complexity & certificate notes
- Distinguish **soundness** (L0,L1,efficiency admissibility never reject a sortable poset) from **completeness** (they don’t catch all non-sortable). The n=12/n=13 failures are incompleteness of scalar/admissibility tests, not unsoundness.
- Improving effective lower bounds on S(n)-C(n) would help constrain exact evaluation of unary SORT-BOUND-U, but: unary is sparse and in PSPACE; a gap on S(n) alone doesn’t yield P≠PSPACE/NP≠PSPACE without stronger class collapse, and circuit lower bounds are blocked (P/poly). No complexity separation follows.
- One-ply is polynomial-space checkable in principle via capped extension counts per state (pruning) but that’s a heuristic/prune (and computing e(P) is #P-hard in general) — not a cheap closed invariant.

### Concrete obstruction / honest limit
**Exact obstruction:** The generalization fails because (1) root is antichain (L1=P0_n)=L0(P0_n), (2) “hardness” is non-monotone in e(P) and symmetry-dependent (Peczarski), (3) no known function of n or local poset scalar predicts reachability of bottleneck classes, and (4) suffix extensions show you can have constant gaps on poset families but S(n) is the antichain value with no known mechanism forcing unbounded gap without the full Wells/Peczarski search. To guarantee a gap for all n>=23 without exhaustive backward search you’d need either a theorem that antichains reach bad classes for all large n (unproven) or an antichain invariant stronger than L1 (none known). I cannot produce such an invariant or a rigorous counterexample to its existence; the decisive obstacle is the state-graph dependence of the obstruction. 

**No repository changes made.** No Lean, no scripts, no notes added — consistent with “no genuinely substantive, independently checkable new theorem or counterexample” and contract constraints.

## Other metadata

```json
{
  "finished_at": 1793517088.1576297,
  "started_at": 1793516994.5657995
}
```
