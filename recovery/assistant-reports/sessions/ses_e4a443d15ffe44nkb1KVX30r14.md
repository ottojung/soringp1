# antonina-cx4mvqLoOit6Nw3YWLPLZk-values

Session: ses_e4a443d15ffe44nkb1KVX30r14
Workspace: /home/lubko/soring-fronts/antichain-advice-minimum-width
Created: 1794050343732; updated: 1794050626119

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 125 (msg_1b5bc5f5e001OyU1Cj4aDWtgo0)

**Finding: no substantive new theorem or counterexample.** The advice question, as stated, does not yet define a minimum advice size or a meaningful impossibility claim.

The key distinction is between a sorting tree’s **behavior** and its **description**. For each \(n\), an optimal tree exists by the definition of \(S(n)\), but that does not give a uniform method for producing it—or for computing \(S(n)\). If “advice” means an arbitrary description of the whole tree, the tree itself is an upper bound on description size, not a useful lower bound: the chosen representation and what the decoder must do are unspecified. If it means advice to a polynomial-time evaluator for \(S(n)\), that is a different model, and the question must specify the advice length, allowed uniform computation, and whether the output is \(S(n)\) or a sorting tree.

A concrete obstruction to the proposed falsifier: a family that is “not reproducible by any uniform polynomial-time procedure” is not, by itself, a separation result. One must first define a representation and show a lower bound against **every** such procedure. And merely having a nonuniform optimal-tree family does not establish advice complexity for exact evaluation of \(S(n)\): producing a tree gives an upper bound on \(S(n)\), not a certificate that no shallower tree exists.

**Literature and model check.** Stober and Weiß, *Lower Bounds for Sorting 16, 17, and 18 Elements* (arXiv:2206.05597v2), study adaptive sorting trees and use a partial backward search as “advice” for their forward search (§4.2, Lemma 4.2). Their result is a bounded-search technique with a stated coverage condition—not a theorem about minimum advice for uniformly evaluating \(S(n)\). In particular, absence from an incomplete table is not generally a sound NO answer; their lemma supplies the extra completeness condition in the covered region. This is advice for a search, not a polynomial-size certificate for exact optimality.

Separately, `docs/problem.md`’s tally-language \(P/poly\) observation concerns nonuniform **decision circuits** for `SORT-BOUND-U`; it says nothing about a minimum advice size for optimal sorting trees, nor does it provide a uniform polynomial-time evaluator. The established \(O(n\log n)\) sorting upper bound concerns the number of comparisons in a tree, not its advice or description length.

So the proposed front does **not** presently support a precise all-\(n\) theorem. The exact obstruction is the missing computational model: advice recipient, tree/evaluator representation, allowed decoder, and whether the target is tree construction or value computation. No repository changes or board post were made.

## Output 312 (msg_1b5bedc6400118OIprDsC9e1Y0)

Recovery check complete. Status of actual effects from the previous turn:

- **Git/worktree:** `git status --short` is empty — no files created, no lean changes, nothing committed. HEAD unchanged at `6a96398`.
- **Board #301:** digest with `--contains` for `antichain-advice`, `minimum-width`, and the front's agent ID (`cx4mvqLoOit6Nw3YWLPLZk`) returns **zero** messages — no post was made by this front.
- **Ledger:** the front `antichain-advice-minimum-width` is still `running` with no recorded exit; no finding was ever posted, so there is no duplicate side effect to avoid — the unfinished work is the mathematical conclusion itself.
- This worktree's `docs/research-encoding-consequences.md` already contains the settled nonuniform results (Thm 3.3 `P/poly` via `S(0..L)`, Thm 3.7 `P/log` via cutoff `t_L`), which bound what the front can add.

I then completed the interrupted analysis. Here is the mathematical finding.

## Finding: the front's dichotomy is ill-posed; each branch is either vacuous or blocked by a documented barrier

**Setup.** Let an "advice scheme for optimal trees" mean: advice `a(n)` plus a decoder producing, for every `n`, a correct adaptive sorting tree of height exactly `S(n)`. Three regimes must be separated (the soundness/completeness distinction applies here, not just to certificates):

1. **Advice-free, decoder may be exponential.** `S` is uniformly computable (memoized minimax over reachable posets, time `2^{O(n²)}`), and the same DP decides sortability of every reachable intermediate poset, so a greedy extraction outputs an optimal tree. **Minimum advice = 0.** The "nonuniform tree advice" reading is therefore degenerate: any positive lower bound would have to first forbid uniform computation, i.e. prove `S` nonzero-advice-incompressible — no such statement is on offer and none is reachable.

2. **Decoder polynomial in `n`.** Then *no* full-tree scheme exists at all, uniform or not. By Lemma 5.1 (`encoding-consequences.md` §5.1), every correct tree has ≥ `n!` leaves, so the output has size `2^{Θ(n log n)}` and any reconstructing decoder runs ≥ `n!` steps. Consequently **both branches of the stated falsifier miss**: "not reproducible by any uniform polynomial-time procedure" is trivially true for *every* optimal tree (and conveys nothing), and its converse is vacuously impossible to satisfy meaningfully. A "recipe" family (e.g. Ford–Johnson, uniform description, `poly(n)` per comparison) is different: for the infinitely many `n` with `F(n) > S(n)` (Manacher; first possible below 47) such a recipe has height `> S(n)` and is a **sound upper bound only** — verifying worst-case height of an arbitrary recipe is itself a general-poset game evaluation (`GEN-SORT`, open per `hardness-boundaries.md` §6), so recipes give completeness of neither the value nor the decision problem.

3. **Decision-language advice (the well-posed reading).** Already settled in the repo: `SORT-BOUND-U ∈ P/log` with cutoff advice `t_L = max{n : n+S(n) ≤ L−1}` (Thm 3.7). The only *new* residual question — whether `o(log L)` advice suffices — cannot be attacked by information counting, because the cutoff sequence is 1-Lipschitz in `L` (`t_{L+1} ∈ {t_L, t_L+1}`) and a stronger decoder could partially compute `t_L` itself; any `Ω(log L)` advice lower bound for this sparse language is an unconditional lower bound against uniform polynomial time of exactly the type `problem.md`'s "Realistic outcomes" section identifies as having no known method.

**Concrete obstruction delivered:** "minimum advice for a uniform family of optimal trees" attains its minimum (0) under any computable-decoder model and is undefined under any poly-time-decoder model; the tally `P/poly` triviality note is untouched either way. The front reduces to the already-documented open row ("program/DAG computing the strategy", `encoding-consequences.md` §5.3) plus the `o(log L)` advice question, which is not separated from the main `SORT-BOUND-U ∈ P` question by any known technique.

**Failed approach on record:** trying to rescue the falsifier via a two-way transfer (tree family ⇒ `S ∈ FP`; `S ∈ FP` ⇒ tree family). The first direction fails because reading the height of an output tree costs `n!`; the second fails because strategy extraction needs sortability decisions on intermediate *reachable* posets, a language strictly beyond the sparse antichain slice (ties to the `GEN-SORT` open status).

**Honest limits.** No new theorem, counterexample, experiment, or primary-source claim beyond the deduction above; `S(n)` beyond `n ≤ 22` remains open (75 ≤ S(23) ≤ 76 per current board). I made no board post (nothing here changes the research picture: it confirms the front as posed has no reachable falsifier), no commit, and no Lean work, per the publication gate. The keeper may mark the front `investigated` on a no-result exit.
