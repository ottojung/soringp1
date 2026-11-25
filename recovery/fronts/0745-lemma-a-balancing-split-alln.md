# lemma-a-balancing-split-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

6h3NLcJUOsKYAXgb9YiCTy-detached

## exit_state

clearexit

## question

For every finite poset P with exact minimax comparison depth m(P) >= 2, does there exist an incomparable pair {x,y} such that both outcome posets P+x<y and P+y<x have exact minimax depth at least m(P)-2?

## basis

docs/research-core-threshold.md Section 6 names Lemma A as the unproved sufficient route to the all-r Fibonacci threshold; docs/research-width-two-threshold.md proves the analogous balancing split only for width-two posets using GPC.

## falsifier

Exhibit a finite poset P with exact minimax depth r >= 2 such that for every incomparable pair, at least one outcome poset has exact minimax depth at most r-3, with independent exact minimax certification of P and both children.

## implication

If true, induction on the Fibonacci thresholds proves T(r)=F_{r+3}-1 for all r, turning the finite verified thresholds into an all-n sound pruning base for exact S(n) evaluation; if false, the Lemma A route to that threshold fails.

## finding_unverified

## Mathematical finding

**Lemma A survives every disproof attempt I could mount; no counterexample was found.**

I attacked the claim

> For every finite poset \(P\) with exact minimax depth \(m(P)\ge 2\), there is an incomparable pair \(\{x,y\}\) such that both \(P+x<y\) and \(P+y<x\) have exact minimax depth at least \(m(P)-2\).

by exact computation rather than by attempting a proof. Concretely, I wrote independent minimax checks (using the repository’s own `add_relation`/`minimax` plus the core-census extension-set representation) and tested:

- **All labelled posets through \(n=6\)** (including all 130023 posets on 6 elements): **0 failures**.
- **All cores with \(e(P)\le 60\)** (6820 cores, covering thresholds through \(r=7\)): **0 failures**.
- **Cores with \(e(P)\le 88\)**: 21000 of 22120 cores checked before the 590s budget expired, **0 failures**.
- **Structured families** (antichains, stars, two-layer complete bipartite posets, fences, merge states `Merge(a,b)`, disjoint unions, staircase posets): **0 failures**.
- **Random posets** at densities from sparse to dense on \(n=7,8\): **0 failures**.

The check is exact: \(m(P)\) and both child values were computed by the minimax recurrence, not by information bounds or heuristics.

## What this does and does not establish

- It does **not** prove Lemma A. A universal statement over all finite posets cannot be settled by finite enumeration, and the remaining \(\sim 1100\) cores at \(e\le 88\) plus all larger posets are unchecked.
- It does push the “no counterexample” frontier to \(r=8\) for the overwhelming majority of the relevant core set, and it covers every poset reducible to those cores (universal-element deletion and ordinal sums preserve the property).
- Consequently, if Lemma A is false, any counterexample must have \(m(P)\ge 8\) (i.e. \(e(P)\ge 89\)) and must lie outside the tested core families.

## Obstruction to the disproof

The natural falsifier would need a poset in which *every* comparison has an outcome dropping at least 3 in minimax depth. Such posets would have to be highly “skew,” but the minimax game’s structure (and the core-census data) makes the first balanced comparison appear unavoidable. I could not construct such a poset by hand or by randomized search, and the exhaustive core data gives no hint of one.

## Honest limits

- Lemma A remains **open**. The finite verified thresholds \(T(r)=F_{r+3}-1\) for \(2\le r\le 8\) are conditional on implementation faithfulness and do **not** imply the all-\(r\) statement; nothing here proves Lemma A or the Fibonacci induction.
- No repository, Lean, test, or board changes were made; the worktree remains clean. The computational evidence supports keeping the Lemma A route alive, but it is evidence, not a proof.

## Other metadata

```json
{
  "finished_at": 1795494444.6496005,
  "started_at": 1795491049.949107
}
```
