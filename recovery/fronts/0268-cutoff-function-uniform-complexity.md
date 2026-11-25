# cutoff-function-uniform-complexity

## status

investigated

## origin

ai_proposal_unverified

## agent_id

xTYt85RUgscPDBvsIs5KZ0-brunn

## exit_state

clearexit

## question

Let f(n)=n+S(n) be strictly increasing and let t(L)=max{n : f(n)<=L-1} define the P/log advice cutoff for SORT-BOUND-U; is there an all-n obstruction showing the uniform function t(·) is not computable in time subexponential in L without computing S(n) on all relevant n, creating a barrier distinct from direct S(n) evaluation?

## basis

Repo shows SORT-BOUND-U in P/log via strictly increasing f(n)=n+S(n) but advice t_L not obviously computable; uniform complexity of the cutoff remains unexamined.

## falsifier

Construct a uniform algorithm computing t(L) for all large L in time 2^(o(L)) (or better) with no oracle for S(n) values on a dense set, or prove t is Turing-equivalent to S under uniform reductions with tight bounds.

## implication

A barrier would separate nonuniform advice efficiency from uniform evaluation complexity and clarify whether P/log triviality gives any computational shortcut.

## finding_unverified

_L - but if to get t_L uniformly you need to compute S on all relevant n, then the advice is "easy" nonuniformly but computing it uniformly is hard (needs all S values). That would be a separation - barrier. To falsify this, either show t can be computed uniformly fast without needing all S values, or show t is Turing-equivalent to S with tight bounds (so they're the same complexity class) meaning no separation. That fits: proving tight equivalence would show no separation between them, falsifying the barrier claim. That makes sense.

Let us analyze this more deeply.

Let us analyze the question deeply.

**MATHEMATICAL FINDING (falsifies the FRONT claim):** $t(L)=\max\{n : n+S(n)\le L-1\}$ is polynomial-time Turing-equivalent to $S(n)$ under uniform reductions with tight parameter scaling.

**Reductions (tight):**
1. **$S \le_T^p t$:** For given $n$, binary search on $k\le U(n)=O(n\log n)$ using $S(n)\le k \iff n \le t(n+k+1)$ ($f(n)=n+S(n)$ strictly increasing; kernel-checked $S$ monotonicity). $O(\log n)$ queries to $t$ at arguments $L=O(n\log n)$. ($T_S(n)=O(\log n)\,T_t(O(n\log n))+\mathrm{poly}(n)$)
2. **$t \le_T^p S$:** For given $L$, restrict to $n\le M(L)=O(L/\log L)$ (since $S(n)\ge c n\log n$), binary search to find max $n$ with $S(n)\le L-1-n$; each test is a threshold query to $S$ (1 query to function $S$ or $O(\log k)$ if threshold-oracle only). $O(\log L)$ queries to $S$ at $n'=O(L/\log L)$. ($T_t(L)=O(\log L)\,T_S(O(L/\log L))+\mathrm{poly}(L)$)

**Implications:**
- The reductions use sparse queries to the oracle (not dense evaluation over all relevant $n$). This directly contradicts the obstruction's requirement of "computing $S(n)$ on all relevant $n$".
- Parameter scales match naturally ($n \leftrightarrow L/\log L$), so time complexity is preserved up to tight scaling. Hence there is **no barrier distinct from direct $S(n)$ evaluation** - $t$ is equivalent to $S$. This falsifies the FRONT claim.
- The P/log advice $t_L$ being nonuniformly easy does **not** create a computational shortcut: uniform computation of the cutoff is Turing-equivalent to uniform evaluation of $S$. This matches "advice need not be computable" (repo).

**Notes/distinctions:**
- **General-poset vs $S(n)$:** The equivalence is for the fixed family $S(n)$ (antichain/comparison-sort minimax on $n$ labeled keys), not arbitrary partial orders. Hardness/obstructions for general posets don't transfer without reduction (consistent with repo). 
- **Soundness vs completeness:** The $P/\log$ construction (advice = cutoff $t_L$) is a correctness/soundness+completeness argument for the language test given advice; computing $t_L$ uniformly is a separate evaluation question - equivalence shows they're the same problem, not that advice-given-test is hard.
- **Limits:** This is a polynomial-time Turing equivalence with tight parameterization (mathematical reduction argument), not a claim about subexponential upper bounds or class separations. Current algorithms give exponential time; equivalence means $t\in \mathrm{TIME}(2^{o(L)})$ (uniform) iff $S\in \mathrm{TIME}(2^{o(n\log n)})$ in the corresponding scale. No Lean changes made (no substantive new kernel-checked theorem beyond what reductions establish from existing facts).

**Failed/alternative attempt:** Searched for a direct unified algorithm computing $t(L)$ without $S$ oracle - no obvious construction; structure differs across $n$. The sparse-query binary search shows dense $S$ evaluation is not required.


## Other metadata

```json
{
  "finished_at": 1793775810.4006689,
  "started_at": 1793773366.4424624
}
```
