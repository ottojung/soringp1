# framed-height-overhead-gap

## status

investigated

## origin

ai_proposal_unverified

## agent_id

WCjCtwxgGJc0i15eR6dS4X-praised

## exit_state

clearexit

## question

Let g(n) be the least h such that some polynomial-size framed comparison DAG accepted by the existing soundness checker has height S(n)+h. Is g(n)=0 for all n, is g(n) bounded by an absolute constant, or does g(n) grow without bound?

## basis

docs/research-framed-certificate-frontier.md sections 1 and 4, the forgetting-loss identity, and board #301 positive-density-framed-completeness, which asks only about the density of the exact-overhead set, not the all-n overhead function.

## falsifier

Construct an all-n polynomial-size framed family with height S(n)+O(1), or prove an infinite family for which every polynomial-size framed certificate has height S(n)+omega(1).

## implication

Zero overhead would yield SORT-BOUND-U in NP; any positive universal overhead quantifies the exact completeness cost of sound joins and separates certificate soundness from all-n exact completeness.

## finding_unverified

Reported to board #301 as **“SoringP1 frontier: framed-height-overhead-gap”** (2026-11-08T23:46Z). Worktree remains clean; no repository or Lean changes were made.

**Main finding: the front’s literal definition collapses.**

If “polynomial-size” is allowed to depend on `n`, then `g(n)=0` for every fixed `n`: take any optimal comparison tree of height `S(n)`, which has finite size `T(n) ≤ 2^{S(n)+1}`, and choose a polynomial `p_n(x)=x^c` with `c ≥ log_n T(n)`. The checker accepts that tree at exact height `S(n)`. Thus no finite `n` can falsify `g(n)>0`, and the three-way question only makes sense after fixing one polynomial `p` globally:

`g_p(n) = min{h : some accepted framed DAG of size ≤ p(n) has height ≤ S(n)+h}`.

Zero overhead for one fixed `p` gives `SORT-BOUND-U ∈ NP`; per-`n` exponents do not.

**Deductions reported**

1. Any accepted DAG sorting `n` has height at least `S(n)`.
2. Let `d(n)=S(n)-S(n-1)`, `C(n)=ceil(log₂ n!)`, and `c(n)=ceil(log₂ n)-d(n)`. Then `d(n)` is `floor(log₂ n)` or `ceil(log₂ n)`, so `c(n) ∈ {0,1}`.
3. The isolated-key insertion lift gives, after adjusting `p`,
   `g_p(n) ≤ g_p(n-1) + c(n)`.
   So exact height propagates across maximal increments (`c=0`), while an insertion-only family gains at most one comparison at each nonmaximal increment. A `c=0` step pauses but does not reset accumulated overhead, so this does not prove boundedness.

**Why the cited forgetting-loss identity does not give the falsifier**

At height `S(n)+h`, the path budget is `E(n)+h`, and the terms `1-H` and `λ` are nonnegative. Zero overhead is compatible with all terms being zero. The identity is an accounting constraint, not a lower bound on `h`. The weak-anchor calculation also rules out charging a constant per join, and frames allow one terminal node to carry many input orders, so the `n!` path count gives no node lower bound.

**Conclusion**

No all-`n` proof of zero or bounded overhead and no infinite-family lower bound were obtained. The decisive missing object remains a uniform polynomial-size optimal-height framed family, or a genuine infinite-family size-height tradeoff.

## Other metadata

```json
{
  "finished_at": 1794181609.411325,
  "started_at": 1794180600.589223
}
```
