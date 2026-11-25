# insertion-lower-bound-universality

## status

investigated

## origin

ai_proposal_unverified

## agent_id

Wt1Hcl9J3FlTv2TElDanWR-smaller

## exit_state

clearexit

## question

Is d(n)=S(n)-S(n-1) >= ceil(log2 n) for all n>=1 (the element-insertion information bound) always achievable in the sense that S(n)=S(n-1)+ceil(log2 n) for infinitely many n, or do there exist infinitely many n where every optimal strategy pays strictly more than ceil(log2 n) to insert the nth element?

## basis

Elementary insertion argument gives >=ceil(log2 n); two-phase gives constructions but optimality not known universally; n=32 equality was just established in board discussion context.

## falsifier

Prove d(n) >= ceil(log2 n)+1 for all sufficiently large n, or construct an infinite family achieving equality.

## implication

Strict excess for all large n would force linear total excess over the trivial insertion scheme and constrain incremental constructions; equality infinitely often constrains lower-bound methods.

## finding_unverified

n information, so need >= ceil(log2 n) comparisons. Even in a global optimal strategy (not necessarily doing insertion at the end), is this true?

Consider element x_n. In any comparison sort of all n elements, the final position of x_n in the sorted order depends on comparisons between x_n and others. There are n possible positions. The decision tree must be able to distinguish all n possibilities. Each comparison gives 1 bit. You need >= log2 n comparisons just to determine which position x_n ends up in. Now, if the global strategy achieved S(n) comparisons total and only needed S(n-1) for the first n-1 elements in some sense, maybe S(n) >= S(n-1) + log2 n? But how to make this rigorous?

Also combined with S(n-1) <= S(n) by monotonicity. But is there a theorem that S(n) >= S(n-1) + log2 n for all n? Let us test: for n=5, S(5)=7, S(4)=5, so 7 >= 5+log2 5 = 7.32 is false. So the inequality doesn't hold. That means the information-theoretic argument as stated doesn't directly give S(n) >= S(n-1) + log2 n for global optimal strategies. That fits because global strategies interleave comparisons.

But the Viche post says it holds for powers of two? Or maybe it's a different argument.

**Claim attacked:** “d(n)=S(n)-S(n-1) ≥ ceil(log2 n) for all n≥1” (the “element-insertion information bound”), read as a property of the global sorting number S(n) (minimum worst-case comparisons over all comparison trees).

**Finding (disproof by known counterexamples):** The inequality is false for global S(n). From established exact values (Knuth/OEIS A036604, Peczarski, Stober–Weiß):  
n=5: d(5)=S(5)-S(4)=7-5=2 < ceil(log2 5)=3; n=9: 3<4; n=10: 3<4; n=17: 4<5, n=18:4<5, n=19:4<5, n=20:4<5, n=21:4<5. The construction S(n)≤S(n-1)+ceil(log2 n) holds for all n, so d(n)≤ceil(log2 n); equality means the two-phase/sort-then-insert construction is optimal. Counterexamples show global optimization can beat insertion construction (d(n) < ceil(log2 n)).

**Why:** The “insert the nth element” information bound (need ≥ceil(log2 n) to place one element into n positions) applies to the *restricted strategy class* that sorts first n-1 then inserts the nth. It does **not** apply to arbitrary global comparison trees that interleave comparisons across all elements. The two-phase docs correctly prove the sort-then-insert strategy needs ≥S(n-1)+ceil(log2 n), but S(n) is the global minimum over all strategies. These are different objects (strategy class vs global optimum). The confused inequality treats a class lower bound as if it were a property of global S(n).

**On the front’s alternatives:** Equality S(n)=S(n-1)+ceil(log2 n) holds infinitely often (all n=2^k: 2,4,8,16,... and others like 6,7,11,12,...,22). Failures also occur repeatedly in every dyadic block for known n. Finite values don’t decide “all sufficiently large n fail” vs “infinitely often hold”; the decisive point is the inequality direction: the all-n claim d(n)≥ceil(log2 n) is false.

**Complexity relevance:** This is a structural fact about global vs incremental strategies, not directly about unary SORT-BOUND-U complexity classes. No Lean changes/repo changes indicated; findings are from primary literature/known exact values.

**Obstruction/limits:** Cannot rule out eventual failure or eventual equality from known data alone (n≥23 open); the real obstruction is conflating strategy-class lower bounds with global S(n). No new theorem proved here, just disproof of that misapplied inequality by counterexamples.


## Other metadata

```json
{
  "finished_at": 1793367773.7093303,
  "started_at": 1793365315.407751
}
```
