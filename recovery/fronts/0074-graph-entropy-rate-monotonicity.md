# graph-entropy-rate-monotonicity

## status

investigated

## origin

ai_proposal_unverified

## agent_id

c7cIcVhqzVO5MeMnoLD0Dy-artist

## exit_state

clearexit

## question

Is the Kahn-Kim/Kahn-Saks comparison entropy rate for states on optimal paths non-increasing in some normalized sense for all n >= some N, and would monotonicity of the entropy-driven strategy force a uniform asymptotic form of S(n) or a computable certificate?

## basis

Kahn-Saks 3/11-8/11 theorem and Kahn-Kim entropy sorting give constant-factor algorithms; but exact relation between entropy and S(n) is loose and no all-n monotonicity/obstruction is established.

## falsifier

Find an infinite family of states reachable on some optimal sorting strategies (or prove their existence for all large n) where the normalized entropy gain of every allowed comparison decreases below any fixed rate after some point, contradicting a uniform rate bound needed for a polynomial certificate.

## implication

Establishing or ruling out entropy-rate monotonicity affects whether information-theoretic greedy strategies can be made optimal/uniform or whether they hit an all-n obstruction relevant to evaluating S(n).

## finding_unverified

f $P$ and $|P|$.

**Consequence for the front:**
- The falsifier claims there is an infinite family (or all large $n$) where the normalized entropy gain of *every allowed comparison* decreases below any fixed rate. Kahn–Saks is the opposite: *every* non-total state has *some* allowed comparison with normalized gain $\ge \delta>0$. The strategy that always picks such a comparison achieves $S_{greedy}(P) \le \frac{1}{\delta}\log_2 e(P) = O(\log n!) = O(n\log n)$, giving the constant-factor information-theoretic bound (later made polynomial-time by Kahn–Kim/Cardinal et al.).  
- "Monotonicity of the entropy-driven strategy" is not the point — the uniform *guaranteed minimum (over best choice) gain* is what matters. Also note: the *optimal exact* strategy need not use good comparisons at every step; the gap between $S(P)$ and $\log_2 e(P)$ is exactly what allows exact optimality to differ from the information-theoretic greedy strategy (Fredman/non-tightness).  
- There is no known all-$n$ obstruction to the *existence* of constant-gain comparisons; the obstruction is to making that strategy exact or to turning it into a polynomial certificate for $S(n)\le k$.

**Certificate soundness vs completeness (important):**
- A certificate "there is a strategy using only 3/11-8/11 comparisons" is *sound* for $O(n\log n)$ but gives only a constant-factor bound, not exact $S(n)$.  
- Completeness for exact $S(n)$ fails badly: the optimal exact tree can be worse than some log-$e$-based bound in choice but better in total? No — worse choice now can be better later, but more directly $S(P)$ is not determined by $e(P)$ (witnessed by different posets same $e$ different $S$, see §5 in hardness-boundaries). Also you cannot read off exact $S(n)$ from $e$-values alone.  
- Counting $e(P)$ is #P-complete (Brightwell–Winkler) but again not equivalent to exact $S(P)$; the real issue is non-tightness of the information bound, not #P-hardness of counting.

**Complexity implications (honest):**
- Ruling out the falsifier (as done by Kahn–Saks) means information-theoretic greedy methods are not blocked by a vanishing gain rate; the barrier to exact evaluation remains elsewhere (state explosion / the minimax recurrence over all posets, sparsity/Mahaney constraints on unary, etc.).  
- This does *not* force a polynomial uniform form of $S(n)$ and does *not* yield a polynomial certificate for $SORT\!-\!BOUND\!-\!U$. The constant-factor algorithm is for approximation of the *strategy length relative to log e*, not for deciding exact $S(n)\le k$ in polynomial time.

**Failed approaches / exact obstruction:** I did not find a paper argument supporting the falsifier; the direct counter-argument is Kahn–Saks. No obvious infinite family construction works because of the uniform $[3/11,8/11]$ guarantee. Any attempt to "normalize differently" (e.g. by $n$, or by current number of incomparable pairs) would need to be careful: gain in *absolute* comparisons might behave differently, but "normalized entropy gain" in the information-theoretic sense used by Kahn–Saks/Kahn–Kim is the log-$e$ reduction which is uniformly >=δ. The obstruction is: you cannot have vanishing log-$e$ gain when every state still has a 3/11-8/11 comparison.

**Recommendation:** Drop this falsifier. Productive directions per AGENTS.md: improve uniform exact evaluators (space/time) or find barriers/certificates for *exact* $S(n)$, not attack a claim directly refuted by Kahn–Saks. No repo/Lean changes warranted.

## Other metadata

```json
{
  "finished_at": 1793388212.6517653,
  "started_at": 1793388061.232307
}
```
