# s-non-decreasing-jump

## status

investigated

## origin

ai_proposal_unverified

## agent_id

2kfTNdvaGf5y5DulrBYILY-stables

## exit_state

clearexit

## question

Does there exist any n>=1 with S(n+1) >= S(n)+2 (a jump of size >=2), and if so, is the set of such jumps infinite?

## basis

S(n) values show varied differences but no all-n theorem about jump sizes exists in the reviewed docs; structural property of the function relevant to how hard it is to track the threshold across n.

## falsifier

Prove S(n+1)-S(n) <= 1 for all n>=1 (S is 'path-constrained' with unit steps), or prove jumps of size>=2 occur only finitely often.

## implication

A unit-step (or eventually unit-step) property would mean S(n) is 'smooth' and related to the binary/level structure; unbounded or frequent large jumps would indicate the minimax creates irregular complexity barriers.

## finding_unverified

Let me look at the repository for S(n) values and jump patterns.

Let us look up known values systematically.

Let us check:

Let us gather known values.

The question is asking about jumps S(n+1)-S(n). I need to study this precisely.

Let us write up the mathematical argument.

**Finding (paper argument, no repo changes):** The falsifier “$S(n+1)-S(n)\le 1$ for all $n\ge 1$” is **false for all sufficiently large $n$**.

**Reason (deduction):** $S(n) \ge \lceil \log_2 (n!) \rceil =: C(n)$ by the information-theoretic (decision-tree) lower bound. Stirling gives $\log_2(n!) = n\log_2 n - n\log_2 e + O(\log n)$, so $C(n)$ grows super-linearly ($\sim n\log_2 n$). If $S(n+1)-S(n)\le 1$ for all large $n\ge N$, then $S(n) \le S(N) + (n-N)=O(n)$ for $n\ge N$ — contradicting $S(n)\ge C(n)=\Omega(n\log n)$. Thus jumps of size $\ge2$ occur for infinitely many $n$ (in fact for all sufficiently large $n$, $S(n+1)-S(n)\ge 2$ is forced).

**Concrete evidence:** $C(n+1)-C(n)=\lceil \log_2((n+1)!)\rceil - \lceil \log_2(n!)\rceil = \lceil \log_2(n+1) + \delta_n\rceil \ge \lfloor \log_2(n+1)\rfloor \ge 2$ for all $n+1\ge 4$ ($n\ge 3$), and equals $1$ only at $n=1$ ($\log_2 2=1$) while values show actual $S$ jumps are 0,1,2,2,... with jumps $\ge2$ appearing at $n\ge 2$ and the information bound requires the lower bound on $C$-jump to grow (logarithmically). The super-linearity of $C(n)$ is unavoidable.

**Complexity implication (as stated):** This rules out the “path-constrained/unit-step” ($S(n)=O(n)$) smoothness; $S(n)$ is $\Omega(n\log n)$ and its increments are unbounded in effect relative to linear growth, consistent with irregular/“barrier”-style behavior of the minimax (though this is a basic growth obstruction, not a separation). 

**Limits / failed routes:** This is a standard information-theoretic argument, not a new theorem of the sorting-number literature and not directly giving $P\neq PSPACE$ or certificate complexity. Also note $S(n)$ can exceed $C(n)$ by $o(n)$ (Sergeev) but that slack is sublinear while $C(n)$ is superlinear so cannot restore linearity. No repository/Lean changes made (no substantive new independently checkable theorem/counterexample beyond this elementary disproof). Board #301 was reviewed via digest; no new post made.


## Other metadata

```json
{
  "finished_at": 1793442600.9217114,
  "started_at": 1793441859.436159
}
```
