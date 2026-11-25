# min-double-drop-count-optimal-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

VamXuC5ihMkWwnP8Yzwqim-bismuth

## exit_state

clearexit

## question

For every n >= 3 let M(n) be the minimum, over all height-S(n) optimal adaptive comparison sorting trees of the n-antichain, of the number of comparisons that possess an outcome child Q with F(Q) <= F(P) - 2 (a minimax double drop). Is M(n) bounded by one fixed constant for infinitely many n, or does M(n) grow without bound (in particular M(n) = Omega(n)) for all sufficiently large n?

## basis

Board #301 (2026-11-23T14:04:48Z) reports the theorem that minimax double drops are unavoidable in every height-S(n) tree for n >= 3, independently re-derived in the 14:08Z referee disposition; Sergeev's S(n) - log2(n!) = o(n) bounds total slack; a full-text scan of the 724-entry frontier ledger found no front counting these events.

## falsifier

Exhibit, for infinitely many n, a height-S(n) decision tree in which the number of double-drop comparisons on every root-to-leaf path is at most a fixed constant c, which refutes any growing lower bound on M(n); conversely, prove M(n) >= c_n with c_n -> infinity to refute the constant upper-bound horn.

## implication

A growing M(n) would force every optimal strategy to dissipate the S(n) - log2(n!) slack in many discrete slack-creating events, refuting exact evaluators and checkable certificates that assume slack is introduced at only O(1) comparisons; a constant bound would license guarded single-drop pruning along nearly all comparisons of the minimax search.

## finding_unverified

force `Omega(n)` double drops on a uniform-random typical path; indeed Markov gives that all but an o(1) fraction of leaves have `o(n)` double drops (choose a threshold `t(n)` with `E[#dd]<<t(n)<<n`).
2. **It does NOT prove M_path is O(1).** The bound controls expectation, not the worst root-leaf path. A worst path could a priori be larger than E[#dd] while still o(n); my small-n data gives M_path=1 through n=6, but I have no all-n worst-path proof.
3. **It does NOT settle M_global.** Total dd-node count can be much larger than expected-per-path count: M_global=2,2,8,48 at n=3..6 while E[#dd] stays below 1. A global Omega(n) or omega(1) lower/upper bound on M_global remains open from this argument alone.
4. **Complexity implication (honest, limited).** The result is a structural theorem about the minimax game: optimal trees cannot dissipate the total `o(n)` information slack through `Omega(n)` expected double-drop events, because each such event has a uniform slack-potential cost >=log2(4/3). This rules out "many discrete slack-creating events on typical paths" as an Omega(n) phenomenon, but it does **not** give a new evaluator, no NP/coNP placement, no separation, and no succinct certificate. The argument is soundness-only in the usual sense (a bound on a quantity), not a completeness/certificate claim.

## Attempted falsification / failed routes [deduction/experiment]

- **Falsify by growing worst-path count**: tried to find n>=7 with M_path>=2. n<=6 gives M_path=1. n=7/n=8 targeted exact search (`good1`, using the `e(P)=2^F(P)` F-synchrony characterization for the zero-dd subtrees) was killed by SIGKILL before completion; no counterexample found, no confirmation obtained. **Inconclusive.**
- **Falsify by Omega(n) expected count**: impossible given the theorem above and Sergeev; a concentrating construction would need E[#dd]=Omega(n) but has only o(n) slack budget.
- **Use total global count as Omega(n)**: small-n global counts grow (2,2,8,48) but this is far from an asymptotic argument; no proof either way.

## Honest limits / exact obstruction

- The central open point is the **worst-path vs expectation gap**. The potential theorem gives `E[#dd]=o(n)` on every height-S(n) tree, which is strong and clean, but the front's M(n) is a minimax-over-trees count; if read as worst path it asks for a pathwise bound, if read as global node count it asks for a much stronger combinatorial quantity. I cannot prove M_path=O(1), cannot prove M_path unbounded, and cannot prove/disprove M_global=Omega(n).
- n=7 exact M_path/M_global is **unresolved here** (search killed; A001035(7)=6,129,859 states makes full enumeration feasible in principle but the targeted good1/F memoization run was interrupted in this environment).
- Sergeev's o(n) is ineffective, so the o(n) in the E[#dd] bound is qualitative.
- No general-poset hardness used; the antichain root / S(n) fixed family is essential.
- No claim about S(n) values, no faster evaluator, no complexity-class placement for `SORT-BOUND-U`.

## Status

**Partial structural result, not a full resolution of the front.** Proved: `E_T[#double drops on a uniform random path] <= (S(n)-log2(n!))/log2(4/3)=o(n)` for every height-`S(n)` optimal tree (paper proof, small-n exact sanity check). This refutes the Omega(n) horn for the expected/typical-path reading and constrains any global Omega(n) claim to be non-typical. Open: worst-path constant/growth (`M_path`) and total-node growth (`M_global`), especially at n>=7.

## Other metadata

```json
{
  "finished_at": 1795452614.8961132,
  "started_at": 1795450108.4353662
}
```
