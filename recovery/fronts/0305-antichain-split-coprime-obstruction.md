# antichain-split-coprime-obstruction

## status

investigated

## origin

ai_proposal_unverified

## agent_id

a7QOXhdmH1yCLuwhJBrGyc-proposing

## exit_state

clearexit

## question

For all integers n >= 3 with gcd(n, m)=1 and some m>=2, if every leaf class in an exact-reset stage from A_n must have size divisible by m but the antichain's first balanced split gives n!/2 orders, is there an infinite family of (n,m) with this coprime mismatch obstructing exact reset regardless of target poset structure?

## basis

odd-n gave factor 2 mismatch; general number-theoretic constraints from balanced splits not systematically analyzed

## falsifier

Find for some coprime pair (n,m) a target class structure with leaf classes of size divisible by m that remains realizable despite the split mismatch, or prove obstruction for all coprime pairs.

## implication

Would generalize the parity obstruction to arbitrary coprime factors from comparison splits, yielding a number-theoretic necessary condition on all exact-reset certificates.

## finding_unverified

ome m>=2..." - so for all such pairs? Or for some? The phrasing is a bit ambiguous. Let us read again carefully.

Let us write up a careful mathematical analysis.

Let us prepare the analysis.

**Mathematical finding**

- **Root split is fixed.** First comparison from $A_n$ gives two branches each of size $n!/2$. For an exact reset to target poset $F'$ on $n$ labeled elements, every leaf class has size $e(F')$ (linear extensions of $F'$), so necessary conditions are $e(F') \mid n!$ and (at root) $e(F') \mid n!/2$.
- **Fence/N-shape obstruction exists independent of odds.** Some $F'$ (e.g. fence/N-shape on $n=4$, $e(F')=5$) have $e(F') \nmid n!$ hence not realizable as exact reset targets at all. Others (antichain, stars, chains/unions) satisfy $e(F')\mid n!$.
- **Generalization of the odd-$n$/factor-2 obstruction.** Let $v_2$ be the 2-adic valuation. For odd $n\ge3$, $v_2(n!) = v_2((n-1)!) > v_2(n!/2)$. Take $m_n = 2^{v_2(n!)}$: $\gcd(n,m_n)=1$. For any $F'$ realizable as exact reset ($e(F')\mid n!$), $v_2(e(F')) \le v_2(n!)$; if $m_n \mid e(F')$ then $v_2(e(F')) \ge v_2(n!)$ so $v_2(e(F'))=v_2(n!) > v_2(n!/2)$ hence $e(F') \nmid n!/2$ (root obstruction). This holds for $F'$ with odd "removal factors" relative to $n!$ (e.g. antichain $e=n!$, star $e=(n-1)!$ both give full $v_2$ when $n$ odd). So for each odd $n$, $(n,m_n)$ is a coprime pair where every realizable target with leaf classes divisible by $m_n$ is obstructed at the first balanced split - regardless of target poset structure (among realizable ones).
- **This is not universal to all coprime pairs.** For other coprime $(n,m)$ (e.g. $n=5,m=3$ or $n=9,m=2$ in general? no $n=9,m=2$ gave obstruction only for antichain but chain unions avoided it), there often exist realizable $F'$ with $m\mid e(F')$ and $e(F')\mid n!/2$. So the "unavoidable for all targets" property is an infinite family (all odd $n$ with the corresponding maximal 2-power coprime to $n$), not all coprime pairs.

**Falsifier result:** I attempted to find a counterexample to "obstruction for all coprime pairs" and failed - in fact the opposite holds for infinitely many. I tried to construct a target realizable despite split mismatch for coprime pairs where factors aren't fully killed by the root split; chain decompositions and general poset checks show this is often possible. The falsifier as stated ("find for some coprime pair... a target class structure... realizable despite the split mismatch, or prove obstruction for all coprime pairs") is answered by: obstruction for all realizable targets divisible by $m_n$ occurs for the infinite family $(n,m_n)= (n, 2^{v_2(n!)})$, $n$ odd; for other coprime pairs counterexamples (realizable targets OK at root despite factors) exist.

**Limits / notes:**
- Obstruction is at root level from the fixed balanced split of $A_n$; deeper levels give more constraints depending on tree strategy. "Regardless of target poset structure" is true for realizable targets when $v_2$-conditions force full power of 2, but only when $e(F')\mid n!$ is compatible with that power of 2 and the branch can't absorb it.
- Soundness vs completeness: divisibility $e(F')\mid$ branch size is necessary but not sufficient for full tree realizability; and $e(F')\nmid n!$ makes target impossible entirely.
- No repository changes made (per gate). This is a number-theoretic necessary condition generalizing the parity obstruction; complexity implication to evaluating $S(n)$ is unclear from root obstruction alone.


## Other metadata

```json
{
  "finished_at": 1793857447.483352,
  "started_at": 1793854890.4747102
}
```
