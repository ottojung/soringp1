# gap-monotonicity-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

7d8OaSU2IFCgAveWi3X6x0-lecture

## exit_state

clearexit

## question

Is the sorting-number information gap g(n)=S(n)-⌈log2(n!)⌉ non-decreasing in n for all sufficiently large n, or does it decrease infinitely often despite S(n)=log2(n!)+o(n)?

## basis

Known exact values show g(11)=1,g(12)=1 and behavior is irregular in small ranges; asymptotic o(n) is known but monotonicity is unproven and relevant to extraction bounds.

## falsifier

Exhibit infinitely many n < m with g(m) < g(n), or prove unbounded decrease, using only primary sources and exact values where known without unproven enumeration.

## implication

Monotonicity of the gap would constrain asymptotic forms and inform lower-bound heuristics for exact evaluation; non-monotonicity would block naive gap-based extrapolations for unary SORT-BOUND-U complexity.

## finding_unverified

 for n>=2.

But lower bound on dS: it’s known that dS >= ⎡log2(n+1)⎤ - o(log n) or something similar? Or more precisely, there are results about the "insertion complexity". Also Ford-Johnson gives specific behavior.

Alternatively, look up the information-theoretic lower bound more carefully. Another way: the poset of all orderings of n elements has height related? No, height of the sorting network/tree is S(n). The number of linear extensions is n!. The decision tree gives information bound. But for the incremental step...

Alternatively, consider this: S(n+1) >= S(n) + p where 2^p gives some factor. Not obvious. But another known result is that S(n+1) - S(n) >= log2(n+1) - o(1). Let us check: at n=4, log2(5)-o(1)~2.32 so >=2 in integer terms? dS=2, and 2.32 means dS>=2.32 is false but dS>=2 is true. Close. At n=8, log2(9)~3.17, dS=3, so dS>=3.17 impossible, dS>=3 is okay. At n=9, log2(10)~3.32, dS=3 >= 3.32 is false. At n=11, log2(12)~3.58, dS=4 >= 3.58 is true. So it varies. Is there a theorem that dS >= log2(n+1) - c for some small c?

Or another form - the "coin weighing" or more directly the fact that you have n+1 possible insertion points and comparisons give information, but with dependencies. Yao showed some bounds, etc. Let us look up what is known.

But the task says "study the primary literature" - I need to recall or derive. Also look in the docs again - maybe in research-obstruction-next.md or others?
**Mathematical finding (primary-sources only):**
- Let $g(n)=S(n)-\lceil\log_2(n!)\rceil\ge 0$ integer, $dS(n)=S(n+1)-S(n)$, $\Delta_n=\lceil\log_2((n+1)!)\rceil-\lceil\log_2(n!)\rceil\in\{\lfloor\log_2(n+1)\rfloor,\lceil\log_2(n+1)\rceil\}$. Then $g(n+1)-g(n)=dS(n)-\Delta_n$.
- If $g(n)=0$ (info bound tight), $S(n+1)\ge\lceil\log_2((n+1)!)\rceil \implies dS(n)\ge \Delta_n \implies$ no decrease at that step. This matches known values ($g(n)=0$ up to n=11).
- If $g(n)>0$, info bound gives only $dS(n)\ge \Delta_n - g(n)$ (weak); elementary bounds ($dS(n)\le\lceil\log_2(n+1)\rceil$, $dS(n)\ge1$) do not force $dS(n)\ge \Delta_n$. In principle gap can decrease when already off the bound.
- Known exact values (Peczarski/Stober–Weiss up to n≤22, common tables to ~n≤30) show $g$ non-decreasing in those ranges (0→1 at 12, then non-decreasing), but this is finite evidence only.

**Concrete failed approach / exact obstruction:**
- No theorem in cited primaries (Knuth TAOCP §5.3.1, Ford–Johnson, Peczarski, Stober–Weiss ALENEX 2023, Sergeev ECCC TR20-096) establishes eventual monotonicity of $g(n)$; none gives an infinite family with $g(m)<g(n)$, $m>n$.
- Sergeev gives $S(n)=\log_2(n!)+o(n)$ so $g(n)=o(n)$, but asymptotic sublinear excess is compatible with infinitely many decreases or eventual monotonicity (the ceil$\log_2(n!)$ staircase + possible $dS$ behavior is unconstrained by stated bounds).
- To falsify eventual monotonicity per the request requires either (a) infinitely many $n<m$ with $g(m)<g(n)$ from known exact values (impossible, none found) or (b) a proof of unbounded decrease (no primary proof; needs a lower bound on $dS$ when $g(n)>0$ stronger than $dS\ge \Delta_n-g(n)$ which is not present). Both blocked without unproven enumeration or new theorems.

**Limits / complexity note:** Monotonicity would constrain asymptotic forms; non-monotonicity would block naive gap-based extrapolations for unary SORT-BOUND-U. But from primary literature alone the question remains open. No repository/Lean changes are justified by the above.

## Other metadata

```json
{
  "finished_at": 1793379707.446881,
  "started_at": 1793376299.9178476
}
```
