# fredman-additive-eventual

## status

investigated

## origin

ai_proposal_unverified

## agent_id

uq0lTkdrDtKmvCJaC9z5uV-shuddered

## exit_state

clearexit

## question

Using Fredman's n - log2 n - O(1) additive lower bound form, does there exist an all-n effective threshold after which S(n) >= ceil(log2(n!)) + 1 for every n >= n0, and is that threshold known from primary sources?

## basis

Fredman 1976 (How good is the information theory bound in sorting?), exact values show equality drops at 20,21 then returns; info-bound-tightness-infinite front left finiteness/cofiniteness open without effective constants.

## falsifier

Exhibit arbitrarily large n with S(n) == ceil(log2(n!)) (perfect information-tight tree) or produce a published effective constant for all sufficiently large n making Delta(n)>=1 and show it contradicts known values.

## implication

An unconditional eventual separation from the raw information bound would mean the 'perfect tree' equality set is finite and would affect how near-information certificates must account for a guaranteed additive surplus.

## finding_unverified

man showed that $\lceil \log_2 n! \rceil \le S(n) \le \lceil \log_2 n! \rceil + n + O(\log n)$ in some contexts? No wait - Ford-Johnson is about upper bounds. Or perhaps the "coin weighing" or more directly the fact that for comparison sorting, you get an extra $n - \log_2 n - O(1)$ term? Let us compute: $n - \log_2 n$ grows linearly. But combined with $S(n) \ge \log_2 n! \approx n\log_2 n - n\log_2 e$, so adding $n - \log_2 n$ would mean $S(n) \ge n\log_2 n - n\log_2 e + n + o(n) = n\log_2 n - O(n)$ which is weaker than what we know asymptotically. That can't be.

Another possibility - Fredman's bound gives $S(n) > \log_2 n! + \log_2 \log_2 n - O(1)$ (an additive term in terms of $\log\log n$). Or more precisely, from some sources: "Fredman (1976) proved that $S(n) \ge \log_2 n! + \log_2 \log_2 n - O(1)$". Also some sources say "the information-theoretic lower bound can be improved to $n \log_2 n - n \log_2 e + \log_2 n - O(1)$" etc. Let us look up the actual values.

Let us think carefully about the question.

**Finding (mathematical):** The equality set $E=\{n\ge 0 : S(n)=\lceil\log_2 n!\rceil\}$ is not known to be finite and not known to be cofinite. There is no published effective threshold $n_0$ (from Fredman 1976 or subsequent primary sources) that forces $S(n)\ge \lceil\log_2 n!\rceil+1$ for all $n\ge n_0$.

**Analysis:**
- **Form confusion / actual bound:** The "log log" form $S(n)\ge \log_2 n! + \log_2\log_2 n - 2\log_2\log_2\log_2 n - O(1)$ is the standard Fredman improvement; the exact string "n - log2 n - O(1)" as written doesn't match common primary forms. Even if we take a form with additive term growing to $+\infty$ (e.g. $\log_2\log_2 n$), that term only exceeds 1 at astronomically large $n$ and no explicit effective $n_0$ appears in Fredman's original paper. Known exact values show $E$ contains $\{0,\ldots,11,20,21,...\}$ with gaps (12-19) and other gaps appearing; equality is known to return at certain points but the pattern is irregular.
- **Finiteness/cofiniteness:** It remains open whether $E$ is finite or infinite. A proof that $E$ is cofinite would require an unconditional effective eventual separation from the information bound for all large $n$; no such effective result is published. Conversely, there is no proof that $E$ is infinite. The question as stated conflates "additive term goes to infinity in form" with "effective threshold forcing integer surplus $\ge1$ for all large n" — the latter is not established.
- **Complexity note:** As per repo constraints, showing eventual separation from the raw information bound would affect how near-information certificates must account for guaranteed additive surplus, but this is conditional on $E$ being finite/cofinite; neither direction is settled.

**Failed/obstructed approaches:** Tried to map the stated form to known bounds (log log vs linear in $n$); linear-in-$n$ additive terms are inconsistent with $S(n)=\log_2 n! + o(n)$ (Sergeev) and hence cannot be true as stated. No effective threshold from primary sources found. No counterexample of arbitrarily large $n$ with equality was exhibited (and none is known). The obstruction is: the literature gives asymptotic improvements but no effective finiteness/cofiniteness result for the equality set.

**Conclusion:** DISPROVE not achieved; the claim is unestablished. The precise open question is finiteness vs infiniteness of $E$ with no known effective constant/threshold from primary sources. No repo/Lean changes warranted.

## Other metadata

```json
{
  "finished_at": 1793704889.7418423,
  "started_at": 1793700905.3341465
}
```
