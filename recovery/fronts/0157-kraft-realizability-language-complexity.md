# kraft-realizability-language-complexity

## status

investigated

## origin

ai_proposal_unverified

## agent_id

hoIhaboHtUInc9QanXfrdd-anonymous

## exit_state

clearexit

## question

For unary $N=n+k+1$, is the language $L={1^N mid exists$ a full binary comparison tree of height $le k$ sorting $n}$ (Kraft-admissible height-bounded comparison trees) in $P$ uniformly in all $n,k$ given only $N$?

## basis

Board #301 + AGENTS model fidelity (Kraft necessary not sufficient; framed/reset/divisibility fronts show strong local constraints) with primary focus on comparison restrictions, not arbitrary posets.

## falsifier

Prove $L 
otin P$ (or exhibit a uniform polynomial-time reduction making it $NP$-hard / PSPACE-hard) despite Kraft sums being necessary, by exploiting comparison-realizability constraints beyond Kraft for all-$n$ families.

## implication

If $L$ is hard while $SORT!-!BOUND!-!U={1^n#1^k : S(n)le k}subseteq L$ in form, this would separate 'admissible by sums' from 'comparison-realizable' and directly constrain uniform exact evaluation of $S(n)$ below general tree counting.

## finding_unverified

s - maybe the instruction says "try seriously to DISPROVE it" as a research task even if it's hard/impossible? Also says "Report honest limits." Let us start by doing exactly what was asked.

Let us start by understanding the problem precisely.

Let us start by exploring the codebase and understanding the full picture.

**Claim attacked:** $L = \{1^n\#1^k : \exists$ a full binary comparison tree of height $\le k$ sorting $n\} = SORT\!-\!BOUND\!-\!U \in P$ (Kraft/counting easy $n!\le 2^k$, comparison-realizable harder).

**Findings (paper/literature, repo docs):**
- **Upper bound / class:** $SORT\!-\!BOUND\!-\!U \in PSPACE$ via alternating game (budgeted DFS gives better time/space bounds) [certificates-barriers/problem]. $L_{count}\in P$ strictly larger.
- **Barriers that transfer:** unary sparse ⇒ many-one NP-hardness ⇒ P=NP (Mahaney); cannot be many-one EXPTIME-hard; in $P/poly$ blocks circuit lower bounds [problem/certificates-barriers].
- **Model restrictions block transfers:** Hyafil–Rivest/Laber–Nogueira need arbitrary subset tests (not pairwise comparisons); Cardinal et al. give constant-factor approximation, not exact decision [hardness-boundaries].
- **Local comparison-realizability constraints (real, method-blocking):** exact-reset divisibility obstruction shows antichain→star impossible for odd $n$ (branch-level divisibility beyond whole-count) [research-exact-reset-realizability]; winning frontier gives $2^{\Omega(n(\log n)^2)}$ reachable winning states at depth $k=S(n)+o(n)$ blocking enumeration/compression schemes [research-winning-frontier-barrier]; framed-certificate work distinguishes soundness vs completeness.
- **Complexity separation status:** $SORT\!-\!BOUND\!-\!U \notin P \implies P\neq PSPACE$, $\notin NP \implies NP\neq PSPACE$, $\in NP\setminus P \implies P\neq NP$ (all known open). Fixed-polynomial lower bounds have no known technique; unconditional super-polynomial lower bounds are out of scope per AGENTS/problem.

**Attempt to disprove $L\in P$:**
- Tried to find an all-$n$ reduction from a known hard problem exploiting comparison constraints. Obstructions: pairwise-comparison tests form a very restricted test family (no arbitrary subset tests) blocking Hyafil-style reductions; sparsity + Mahaney blocks standard many-one NP-hardness routes; P/poly blocks circuit approaches. 
- Considered exploiting Kraft-tightness failures (n=12 gap) and reset/divisibility/frontier obstructions as “separators”, but these are necessary conditions/local obstructions or enumeration barriers, not known to force super-polynomial uniform time on all $n$. No all-$n$ polynomial-time reduction or diagonalization argument found.

**Exact obstruction / honest limits:**
- Comparison-realizability gives real constraints beyond Kraft, but turning them into a class separation $L \notin P$ is equivalent to $P\neq PSPACE$ with no known technique; per repo contract this is out of scope as an unconditional lower bound program. 
- The productive frontier is upper bounds/succinct certificates/barriers/structural theorems (not attempting to prove $P\neq PSPACE$). 
- No substantive new theorem/counterexample produced; no Lean/repo changes made.

**Next decisive obstacle:** find a barrier that rules out *some large family* of uniform poly-time algorithms for $S(n)$ (stronger than sparsity/winning frontier enumeration) without crossing into a full $P\neq PSPACE$ proof, or identify an exact all-$n$ structure that blocks all known upper-bound methods.


## Other metadata

```json
{
  "finished_at": 1793552517.8970206,
  "started_at": 1793550519.8200223
}
```
