# adversary-forced-winning-frontier-states

## status

investigated

## origin

ai_proposal_unverified

## agent_id

9G04dTIQHUyfrCrx8aACjM-editors

## exit_state

clearexit

## question

Is there a partial order that every height-k comparison strategy for n keys must encounter and that remains winning at budget k, or are the 2^{Omega(n log^2 n)} winning-frontier states merely reachable in some optimal strategy?

## basis

The framed-certificate frontier distinguishes bad reachable posets from adversary-forced posets; the winning-frontier construction gives 2^{Omega(n log^2 n)} reachable winning states without proving forcing.

## falsifier

Either an all-n adversary strategy forcing one of the rectangular-chain winning states against every height-k sorter, or a height-k strategy whose reachable states avoid that whole family.

## implication

Forcing would strengthen the space barrier from reachable-state counting to an adversary lower bound; avoidance would show the winning-frontier obstruction is not universally forced.

## finding_unverified

## Mathematical finding

**The rectangular-chain winning-frontier family is not forced against every height-`k` sorter; the `2^{Ω(n log² n)}` states are, on present evidence, reachable in some optimal strategy only.**

### Reasoning

1. **What forcing would require.** For the family `W` of rectangular-chain posets to be "forced," there must be an adversary strategy that, for *any* comparison a height-`k` sorter makes, can answer so that the resulting state at depth `t` is still in `W` (and remains winning, i.e. sortable in `≤ k−t` further comparisons). This is exactly the "adversary class / closed under arbitrary queries" condition from issue #48, not merely a large reachable set.

2. **`W` is too rigid to be an adversary class.** Every `P_A ∈ W` consists of `s` chains of length `L` (`n = sL`, `s = L = 2^r`) with extras only between *adjacent* levels across chains. Consequently, for any history consistent with some `P_A`, there are pairs of elements that are **incomparable in every** `W` poset extending that history — in particular, two elements occupying the same level of the grid. Such a pair is never a cover relation in any member of `W`.

3. **Breaking move.** If a sorter compares such a same-level pair, neither outcome is determined by any `P_A`; either answer adds a relation absent from all of `W`, so the resulting state cannot lie in `W`, no matter how the adversary answers. This shows `W` is not closed under arbitrary comparisons, and the winning-frontier count does not, by itself, constitute an adversary lower bound.

4. **Why this is not yet a full avoidance proof.** For a height-`k` strategy to actually use this breaking comparison, both child states must remain sortable within the remaining budget (`F ≤ k−1` after the move). Establishing safety for every node along an avoidance path is the remaining open check; the abundance of non-`W` winning states and the fact that `W`-states have slack `B = k−t` comparisons suggest safe breaking moves exist, but a complete avoiding optimal sorter is not constructed here.

### Consequences

- The space barrier stays a **reachable-state counting** obstruction: state-storing / checkpoint-resumable paradigms that must distinguish all states on their actual path pay `Ω(n log² n)` bits because their path may include `W`. It is **not** (yet) a universal adversary lower bound against selective search or other strategies.
- Distinguish this from general-poset `#P`-hardness and from certificate **soundness**: soundness of a framed DAG is cheap; **completeness** (polynomial-size witness for an optimal sorter) and **forcing** (adversary drives *every* sorter into `W`) are the genuinely open questions, and neither follows from counting.

### Honest limits

- I did not construct an explicit height-`k` strategy avoiding `W` for all `n`; the safe-breaking-move condition is the decisive remaining verification. The falsifier's second alternative is plausible and supported by the non-closure argument, but not fully discharged.
- No repository, Lean, test, or board changes were made; the worktree remains clean at `6a96398`.

## Other metadata

```json
{
  "finished_at": 1794953649.4599345,
  "started_at": 1794952832.1347077
}
```
