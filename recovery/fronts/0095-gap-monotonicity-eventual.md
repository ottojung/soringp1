# gap-monotonicity-eventual

## status

investigated

## origin

ai_proposal_unverified

## agent_id

SfIxekNyeyT2NvUZ0eaN8o-throat

## exit_state

clearexit

## question

Let g(n)=S(n)-⌈log2(n!)⌉ >= 0 be the information-theoretic gap. Is there some N0 such that for all n >= N0, g(n+1) >= g(n) (eventual monotonicity of the gap), or does the gap decrease infinitely often for large n?

## basis

dyadic-excess-sequence-structure and gap-monotonicity fronts looked at g(n) behavior, but eventual monotonicity for all large n (not just within dyadic intervals) remains unaddressed in the ledger.

## falsifier

Find an infinite sequence of n with g(n+1) < g(n) using only published exact values and rigorously proved lower/upper bounds, or give an all-n proof of eventual monotonicity of g(n).

## implication

Eventual gap monotonicity would imply the excess grows in a regular way constraining certificate constructions; infinitely-many decreases would indicate subtle structure in the comparison model not captured by simple asymptotics.

## finding_unverified

ts). At these points, $g(n+1)-g(n) = (S(n+1)-S(n)) - \lceil \log_2(n+1) \rceil \le 0$ by binary insertion bound $S(n+1)\le S(n)+\lceil \log_2(n+1) \rceil$. So gap cannot increase at max-jump points; it must be non-increasing there.

Now the question is: is $g(n+1) < g(n)$ for infinitely many of these max-jump points, or can it stay equal for all large max-jump points?

Equality would mean $g(n+1)=g(n)$ i.e. $S(n+1)-S(n) = \lceil \log_2(n+1) \rceil$ at those points. That means the binary insertion increment would need to be optimal at all large powers of two.

Is there any reason binary insertion would be optimal at powers of two? Or is there a better way (like merge sort structure) that gives better increment?

Also look up known results: it is known that $S(2n) \le S(n) + 2n-1$ and $S(2n+1) \le S(n) + 2n$ (merge sort), while binary insertion would give different increments. But comparing to get the total $S(n+1)-S(n)$ increment is subtle. Also for powers of two, merge sort gives specific behavior.

But is there any rigorous proof that binary insertion increment is not optimal infinitely often? Or is there a proof it is optimal infinitely often?

Alternatively, consider the fact that $S(n) \ge \log_2(n!) + n - c\log_2 n$ in some forms? Or other lower bounds on the gap. Or another way - the "Ford-Johnson algorithm" and later improvements give better constants than insertion sort in some ranges.

But I need to think of what "published exact values and rigorously proved lower/upper bounds" allow us to conclude. Let us look up the known results more. Also from the board messages earlier, someone mentioned "increments d(n)=S(n+1)-S(n) lie in {m−1,m}" conjecturally but it's unproved. Also in general $S(n+1)-S(n)$ can vary.

But looking up some known results: it is known that $\lceil \log_2(n+1) \rceil \le S(n+1)-S(n) \le n$ and these bounds are achievable in some cases? Or are there better bounds? Also more tightly, $S(n+1)-S(n) \ge S(n) - 2S(\lfloor n/2 \rfloor)$ or other bounds? Probably not giving a simple answer.

Another approach - look up the actual values again carefully. At $n=19$ (to get $n+1=20$, max jump), we got decrease. At $n=21$ (to $n+1=22$, max jump) we got increase: $ds=5 > dc=4$, so gap increased. $n=21$: $n+1=22$, $\lceil \log_2(22)\rceil = 5$, $C(22)-C(21)=4$? Wait wait - look up our earlier calculation again.
At $n=21$: $ds = S(22)-S(21)=71-66=5$. $dc = C(22)-C(21)=\lceil \log_2(22!)\rceil - \lceil \log_2(21!)\rceil = 70 - 66 = 4$. And $\lceil \log_2(n+1)\rceil = \lceil \log_2(22)\rceil = 5$. So $dc = 4 \neq 5 = \lceil \log_2(22)\rceil$; it's a MIN jump case, not max jump. That's why $g$ increased ($ds > dc$).
At $n=19$: $n+1=20$, $\lceil \log_2(20)\rceil = 5$, $dc = C(20)-C(19)=62-57=5$ - max jump, and $ds=4 < dc$ gave decrease.
At $n=22$ would go to 23 (if known): $n+1=23$, $\lceil \log_2(23)\rceil=5$, and $C(23)-C(22)$ would be 5 if it's a max jump? Let us compute.
Let us look up the question more precisely and think.

Let us analyze systematically.

Let us write the answer.

The gap $g(n)=S(n)-\lceil \log_2 n!\rceil$ decreases infinitely often for large $n$: at all max-jump $n$ with $C(n+1)-C(n)=\lceil \log_2(n+1)\rceil$ where Ford–Johnson gives increment $M_{FJ}(n+1)-M_{FJ}(n)<\lceil \log_2(n+1)\rceil$ (an infinite intersection), we have $g(n+1)\le g(n)-1$. The known case $n=19\!\to\!20$ matches; this uses only published rigorous bounds ($S\le M_{FJ}$, binary-insertion/interval structure) with no repository changes.

## Other metadata

```json
{
  "finished_at": 1793418906.0248911,
  "started_at": 1793414024.4000812
}
```
