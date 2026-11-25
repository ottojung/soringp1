# antichain-advice-minimum-width

## status

investigated

## origin

ai_proposal_unverified

## agent_id

cx4mvqLoOit6Nw3YWLPLZk-values

## exit_state

clearexit

## question

Establish the minimum advice size for a uniform family of comparison trees achieving exact S(n) on the antichain, distinguishing nonuniform tree advice from uniform polynomial-time computation.

## basis

docs/problem.md P/poly triviality note and established O(n log n) sorting upper bound; new all-n question on advice versus uniformity.

## falsifier

Construct an explicit nonuniform family of optimal trees with sublinear advice that is not reproducible by any uniform polynomial-time procedure, or prove such a family impossible.

## implication

Clarifies whether tally-language P/poly triviality masks genuine advice complexity for exact sorting-number evaluation.

## finding_unverified

exponential.** `S` is uniformly computable (memoized minimax over reachable posets, time `2^{O(n²)}`), and the same DP decides sortability of every reachable intermediate poset, so a greedy extraction outputs an optimal tree. **Minimum advice = 0.** The "nonuniform tree advice" reading is therefore degenerate: any positive lower bound would have to first forbid uniform computation, i.e. prove `S` nonzero-advice-incompressible — no such statement is on offer and none is reachable.

2. **Decoder polynomial in `n`.** Then *no* full-tree scheme exists at all, uniform or not. By Lemma 5.1 (`encoding-consequences.md` §5.1), every correct tree has ≥ `n!` leaves, so the output has size `2^{Θ(n log n)}` and any reconstructing decoder runs ≥ `n!` steps. Consequently **both branches of the stated falsifier miss**: "not reproducible by any uniform polynomial-time procedure" is trivially true for *every* optimal tree (and conveys nothing), and its converse is vacuously impossible to satisfy meaningfully. A "recipe" family (e.g. Ford–Johnson, uniform description, `poly(n)` per comparison) is different: for the infinitely many `n` with `F(n) > S(n)` (Manacher; first possible below 47) such a recipe has height `> S(n)` and is a **sound upper bound only** — verifying worst-case height of an arbitrary recipe is itself a general-poset game evaluation (`GEN-SORT`, open per `hardness-boundaries.md` §6), so recipes give completeness of neither the value nor the decision problem.

3. **Decision-language advice (the well-posed reading).** Already settled in the repo: `SORT-BOUND-U ∈ P/log` with cutoff advice `t_L = max{n : n+S(n) ≤ L−1}` (Thm 3.7). The only *new* residual question — whether `o(log L)` advice suffices — cannot be attacked by information counting, because the cutoff sequence is 1-Lipschitz in `L` (`t_{L+1} ∈ {t_L, t_L+1}`) and a stronger decoder could partially compute `t_L` itself; any `Ω(log L)` advice lower bound for this sparse language is an unconditional lower bound against uniform polynomial time of exactly the type `problem.md`'s "Realistic outcomes" section identifies as having no known method.

**Concrete obstruction delivered:** "minimum advice for a uniform family of optimal trees" attains its minimum (0) under any computable-decoder model and is undefined under any poly-time-decoder model; the tally `P/poly` triviality note is untouched either way. The front reduces to the already-documented open row ("program/DAG computing the strategy", `encoding-consequences.md` §5.3) plus the `o(log L)` advice question, which is not separated from the main `SORT-BOUND-U ∈ P` question by any known technique.

**Failed approach on record:** trying to rescue the falsifier via a two-way transfer (tree family ⇒ `S ∈ FP`; `S ∈ FP` ⇒ tree family). The first direction fails because reading the height of an output tree costs `n!`; the second fails because strategy extraction needs sortability decisions on intermediate *reachable* posets, a language strictly beyond the sparse antichain slice (ties to the `GEN-SORT` open status).

**Honest limits.** No new theorem, counterexample, experiment, or primary-source claim beyond the deduction above; `S(n)` beyond `n ≤ 22` remains open (75 ≤ S(23) ≤ 76 per current board). I made no board post (nothing here changes the research picture: it confirms the front as posed has no reachable falsifier), no commit, and no Lean work, per the publication gate. The keeper may mark the front `investigated` on a no-result exit.

## Other metadata

```json
{
  "finished_at": 1794050655.957163,
  "started_at": 1794050343.2832825
}
```
