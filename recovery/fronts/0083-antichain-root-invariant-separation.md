# antichain-root-invariant-separation

## status

investigated

## origin

ai_proposal_unverified

## agent_id

ISLN1gVgGNgHim5FLQ6i5a-groin

## exit_state

clearexit

## question

Does there exist an all-n invariant I(P) computable from a reachable poset P (with P reachable from antichain) that is strictly stronger than the information bound in the sense that for infinitely many optimal-decision paths from antichain, I forces >= c*S(n) comparisons while log2(e(P)) is within o(n) of its maximum for P, for some fixed c>1/ something or just strictly separating?

## basis

Root quantifier distinction (issues #47/#48), Fact 0.2, and n12 nontightness showing scalar invariants fail; focus strictly on antichain root reachability, not general posets.

## falsifier

Show every polynomial-time (or just natural) invariant that is monotonic and adversary-sound is dominated by log2(e(P))+o(n) on all antichain-reachable winning states at budget S(n), or give a counterexample invariant achieving strict separation.

## implication

A nontrivial root-quantified invariant would improve lower bounds on S(n) without attacking arbitrary posets; failure to separate would clarify why information-theoretic invariants have been insufficient.

## finding_unverified

-forcing.** Two-chain (merge) posets give $F(P)=M(a,b) > \lceil \log_2 e(P)\rceil$ in many cases (e.g. $(2,4)$ gives $5>4$), and local gaps $F(P)-\lceil \log_2 e(P)\rceil$ are unbounded along the balanced merge family ($M(m,m)-\log_2 C(2m,m)=\Omega(\log m)$). However: (a) these are arbitrary reachable posets, not necessarily on "optimal-decision paths from antichain" that remain in a regime where $\log_2 e(P)$ is within $o(n)$ of maximum; (b) more directly, an adversary trying to force from root must have a comparison choice for the sorter at every step - a hard local gadget doesn't create a root-forcing invariant unless the root quantifier is satisfied (issue #48 / quantified-root-adversary-proof). The board already records this root-quantifier gap as the obstruction.

4. **"Natural/monotonic/adversary-sound" is the key constraint.** If we require $I$ monotonic under adding relations ($P \subseteq P'$ implies $I(P)\ge I(P')$) and adversary-sound ($I(P)\le F(P)$), then any such $I$ is bounded above in effect by the "hardest" direction consistent with information - but more tightly, the information bound is itself the universal one from leaf counting. The $n=6$ counterexamples show you cannot do better with $(e,\text{width},\#\min,\#\max)$ etc. Combined with (1), this suggests $I(P) \le \log_2 e(P) + o(n)$ for natural invariants on the relevant class, killing any constant-factor separation above $S(n)$ in that asymptotic regime.

### Concrete failed approach
Tried to construct an $I$ from the graded (chain+extra-edges) winning-frontier posets that would see "column constraints" - e.g. track the product/structure beyond $e(P)$. But $e(P)$ for those posets is still $n! / \prod (L!)^?$ times factors from extra edges; computing exact $e(P)$ is nontrivial, but even if we had a better invariant, the frontier barrier means exponentially many states look similar, and more directly the asymptotic counting gives $I(P) \le C(\log_2 e(P) + n)$ impossible to beat $S(n)$ by constant factor given $S(n)=\log_2(n!)+o(n)$. Also no way to satisfy root-forcing against every sorter move.

### Exact obstruction
The project cannot obtain a strict constant-factor separation $c>1$ from any polynomial-time/natural monotonic adversary-sound invariant on infinitely many optimal-decision paths with $\log_2 e(P)=\log_2(n!)-o(n)$ because: (a) $S(n)$ is already $\log_2(n!)+o(n)$ (Sergeev), so $c S(n) > \log_2(n!) + o(n) \ge \log_2 e(P) + o(n)$; (b) all known natural invariants are dominated by $\log_2 e(P)+o(\log_2 e(P)?)$ or more tightly by the information bound plus lower-order terms that don't create a constant factor gap above $S(n)$ in this regime; (c) the root quantifier (issue #48) blocks lifting local gadget lower bounds to "forces on every sorter" from antichain. The winning frontier + non-monotonicity in $e$ + merge non-tightness explain why scalar/information-based invariants fail, but the asymptotic $o(n)$ slack from Sergeev is the precise obstruction to the specific constant-factor claim as stated.

### Recommendation
Do not add new Lean/invariants. The falsifier is effectively true under standard asymptotics: no such strictly separating natural invariant exists for constant $c>1$ in that regime. Focus instead on (1) better upper bounds/evaluators, (2) barriers that rule out whole invariant families with explicit constants, or (3) structural theorems about the root quantifier - areas that can still change what we know about computing $S(n)$ per AGENTS.md.


## Other metadata

```json
{
  "finished_at": 1793398138.3124955,
  "started_at": 1793396651.8517454
}
```
