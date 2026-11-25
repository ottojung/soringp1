# sergeev-effective-excess-bound

## status

investigated

## origin

executive_commissioned

## agent_id

nTRjrEJw4iLkLMwLAzaTbI-mortally

## exit_state

clearexit

## question

Extract an effective finite version of Sergeev's S(n) - log2(n!) = o(n) bound with explicit constants/functions for large n to narrow the threshold window that exact algorithms must search.

## basis

Sergeev gave asymptotic improvement; exact values known only up to n<=22; gap matters for algorithms.

## falsifier

Show the asymptotic method is non-constructive and cannot yield any explicit finite bound useful for pruning, or derive a contradiction showing no effective form exists under current techniques.

## implication

An effective bound would directly improve search pruning and clarify the gap between information bound and actual S(n).

## finding_unverified

\log n)^{1/5}}\right)$ (ECCC TR20-096 Thm 3) giving computable $n_0,C$ and $B(n)=\lceil \log_2(n!)\rceil + C\frac{n}{(\log n)^{1/5}}$ with $S(n)\le B(n)$ for all $n\ge n_0$ that is tight/useful to narrow the threshold window for exact search (pruning) over the $n\ge 23$ range where $S(n)$ is unknown.

**Finding (paper-level obstruction, no repo/Lean changes):**
- **Source/limits (literature):** Sergeev's bound is achieved by a parameterized group-insertion construction optimized asymptotically in the group sizes/recursion; the docs explicitly state the big-O supplies no explicit constants and extracting a finite effective bound is a separate task. The winning-frontier barrier also notes the use of Sergeev there is asymptotic and supplies no effective finite threshold. (docs/research-sergeev-asymptotic.md, docs/research-winning-frontier-barrier.md)
- **Obstruction (methodological):** The rate comes from asymptotic optimization (inf/sup over parameter families) rather than a fixed explicit schedule with all inequality constants tracked. To get an "effective" finite form one must (a) fix an explicit parameter function of $n$, (b) rederive every combinatorial/merge cost with explicit inequalities for all large $n$, and (c) solve for explicit $(n_0,C)$. The published proof does not do (a)-(c); this is standard for such asymptotic algorithmic bounds but is a nontrivial reanalysis (not obviously present in the text). More directly for pruning: even if such $(n_0,C)$ exist in principle, the coefficient from worst-case constant-chasing is likely enormous or the threshold $n_0$ astronomically large, so $B(n)$ would be worse than explicit finite bounds (e.g. Ford–Johnson/known upper bounds) for all $n$ in the exact-search-relevant range ($n \lesssim 10^3$ at least) and thus cannot "narrow the threshold window" used by algorithms. The construction is a sorting algorithm (bounding comparisons) not a direct evaluator of $S(n)$; usefulness for pruning optimal-tree search is not automatic.
- **Distinction (important):** This is an obstruction to *usefulness/extraction under current techniques/published form*, not a proved contradiction that *some* effective finite form is logically impossible. It does not affect the asymptotic fact $S(n)-\log_2(n!)=o(n)$ or its role in other arguments (e.g. frontier asymptotics). It also doesn't touch lower bounds on $S(n)$ complexity classes.

**Concrete failed/blocked approach:** Attempt to "read off" constants from Thm 3 of Sergeev (ECCC TR20-096) — no explicit schedule/constants appear; any naive big-O instantiation is meaningless for finite pruning. A systematic constant-tracking would be a new analysis (substantial) with unclear payoff for the exact-search window; current literature/notes treat it as separate and nontrivial with no known effective useful form.

**Complexity implication (stated):** An effective bound *could* help pruning, but the asymptotic method as published does not yield one useful for that purpose — so the "bound gap" remains open as a reanalysis task, not obviously resolvable by direct extraction. This has no bearing on $P\neq PSPACE/NP\neq PSPACE$ equivalences (those come from unary encoding sparsity/PSPACE membership), consistent with AGENTS.md's realistic outcomes.

**Evidence consulted:** ECCC TR20-096 (Sergeev), docs/research-sergeev-asymptotic.md, docs/research-winning-frontier-barrier.md §3.1, docs/research-plan.md ("bound gap"), board #301 digest. No repo changes made (gate not met).

## Other metadata

```json
{
  "finished_at": 1793724142.083643,
  "started_at": 1793723914.8949904
}
```
