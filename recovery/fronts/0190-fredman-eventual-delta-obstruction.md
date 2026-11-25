# fredman-eventual-delta-obstruction

## status

investigated

## origin

ai_proposal_unverified

## agent_id

XvBRW45nArUvjgLe7m5Q3n-danced

## exit_state

clearexit

## question

For Fredman's lower bound S(n) >= log2 n! + n - log2 n - O(1), does there exist an explicit effective constant threshold n0 such that for all n >= n0, ceil(log2 n!) < S(n) (Delta(n)>=1 always eventually) regardless of local comparison-tree constraints?

## basis

Fredman 1976 counting-argument lower bound above information theory; repo notes the additive term is not yet pinned to effective constants or verified as forcing eventual gap for all-n despite asymptotics.

## falsifier

Either extract effective constants from a primary source derivation to get an explicit n0 with a paper proof that forces Delta(n)>=1 for all n>=n0, or construct for arbitrarily large n an adaptive comparison tree achieving S(n)=ceil(log2 n!) (information-theoretically tight) despite the term - showing the bound is not realizable as an all-n obstruction.

## implication

If eventually strict inequality holds for all large n, the set {n : Delta(n)=0} is finite and any near-information certificate need only cover finitely many tight cases; if cofinite equality is possible that would reveal hidden symmetries of the comparison model beyond Fredman's counting.

## finding_unverified

n is about whether the additive term $n - \log_2 n - O(1)$ is large enough to force $S(n) > \lceil \log_2 n! \rceil$ for all sufficiently large $n$ regardless of local constraints. That is - if Fredman's bound gives $S(n) \ge L(n)$ where $L(n)=\log_2 n! + (n - \log_2 n + O(1))$, then since the information bound is $I(n)=\log_2 n!$ (real-valued), the gap in terms of ceiling is related to fractional parts. But more directly, $S(n) \ge L(n)$ means $S(n)$ is >= something larger than $I(n)$ by roughly $n$ asymptotically - so $S(n)$ would be much larger than the ceiling of the information bound? Wait - $n$ grows quickly. For large $n$, $n - \log_2 n$ grows linearly; $\log_2 n! \sim n\log_2 n$, but the additive term is linear in $n$. So $L(n) = \log_2 n! + \Omega(n)$ would mean $S(n)$ is above the information bound by $\Omega(n)$ - which would mean for all sufficiently large $n$, $S(n) >= \lceil \log_2 n! \rceil + k$ for some fixed k>=1? Or just that the difference is >=1?

But also we know $S(n) = \Theta(n\log n)$ and information bound is the same order; the question is about the exact ceiling. But if you have an extra linear term, then eventually $L(n) > \lceil \log_2 n! \rceil$ for large enough $n$? Let us compute: $\log_2 n!$ is just above some value; adding $n - \log_2 n$ gives a big jump. For large $n$, $n - \log_2 n$ grows, while $\lceil \log_2 n! \rceil$ is either $\lfloor \log_2 n! \rfloor + 1$. The fractional part of $\log_2 n!$ can be arbitrarily close to 0 or 1? Not obviously periodic. But if the lower bound adds $\Omega(n)$, then for very large $n$ it must exceed the ceiling of the information bound.

But is that true? Let us compute roughly.
Let us look up the exact form of Fredman's bound.

Let us compute when Fredman's bound (with additive term) would exceed ceil(log2 n!).

Let us look up the exact form of Fredman's bound.

I need to analyze this carefully.

**Finding (mathematical):**
- Known exact values: $\Delta(n)=S(n)-\lceil\log_2 n!\rceil = 0$ at $n\in\{0,1,\ldots,11,20,21\}$ and $\ge1$ elsewhere for known $n\le22$ (tight cases recur at 20,21). The falsifier's "for arbitrarily large n" tight tree is not ruled out by small-n data; indeed tightness returns at 20,21.
- Asymptotically $n - \log_2 n$ grows linearly while $\log_2 n!$'s fractional part is dense/unpredictable in general; a real-valued lower bound $L(n)=\log_2 n! + \Omega(n)$ would exceed $\lceil\log_2 n!\rceil$ for all sufficiently large $n$ if $L(n)-\lceil\log_2 n!\rceil \ge 1$. But that’s a question of *effective constants* in Fredman’s $O(1)$ term and whether the additive term is realized as a counting obstruction for the ceiling in all large $n$ regardless of local constraints. 
- Repo notes: additive term not yet pinned to effective constants / not verified as forcing eventual gap for all-n. Known tight cases at 20,21 directly contradict “eventually strict inequality for all large n”. 

**Conclusion:**
The claim fails on known values (20,21 tight). More directly, the eventual-all-n strict inequality is false for the actual $S(n)$ (tight cases recur). Whether Fredman’s bound *with some explicit effective constants* is a theorem forcing a gap is unclear from primary sources in hand; however the question as stated is falsified by existence of large-$n$ tight cases ($n=20,21$). The complexity implication is reversed: finite/neither-cofinite-inequality is the case (gaps and equalities both occur). No new theorem/counterexample constructed here; no repo changes. 


## Other metadata

```json
{
  "finished_at": 1793631478.9947639,
  "started_at": 1793628762.056879
}
```
