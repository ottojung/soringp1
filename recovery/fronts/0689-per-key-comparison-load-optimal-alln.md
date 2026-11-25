# per-key-comparison-load-optimal-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

mbVR7aPNJ9ZTfAzBLz08qf-trend

## exit_state

clearexit

## question

Let Lambda(n) be the least L such that some height-S(n) correct sorting tree on n labelled keys has every key compared at most L times on every root-to-leaf path (the Omega(log n) lower bound from rank determination is immediate). Is Lambda(n) <= c*log n for all n and a fixed c, or does an infinite family force some key into omega(log n) comparisons on some path of every height-S(n) tree?

## basis

docs/problem.md height-optimal adaptive trees and the board #301 succinct-certificate frontier; an independent audit of all 687 ledger fronts found per-key comparison incidence unaddressed (depth-spread and average-depth fronts measure leaf depths, not per-key load along paths).

## falsifier

Compute Lambda(n) exactly with a load-augmented minimax solver for n=6,7 and exhibit an n where every height-S(n) tree has a key of load greater than c*log n, or exhibit for all n a height-S(n) tree with per-key load O(log n) and establish the uniform bound.

## implication

An O(log n) per-key load normal form is a new local structural restriction usable toward polynomial-size succinct strategy certificates (the live NP/coNP frontier for SORT-BOUND-U); an omega(log n) lower bound rules out element-local compositional evaluation routes.

## finding_unverified

nt object from per-key load on a **single** path. Let me add a one-line distinction to my post, then post once with the proper author.
Post succeeded. Let me verify it appears exactly once on the board.
Done. Here is the honest report.

## Recovery audit (per the backend-failure warning)

Before any action I verified: worktree clean at `6a96398` on `billy-dev` (reflog = clone only); my ledger front `per-key-comparison-load-optimal-alln` was `running` with **no finding**; board #301 had **zero** posts matching "per-key"/"Lambda"/"load"/"load-augmented"; and `/tmp/opencode` had **no scratch files** from my front. So the interrupted turn left nothing for this front — nothing was duplicated. The only external side effect I made is **exactly one** #301 comment (verified: 1 matching comment), plus scratch files under `/tmp/opencode`. No commits, Lean, tests, ledger, or repo changes.

## What I built and verified (scratch only)

A load-augmented minimax solver: state = poset (transitive-closure successors) + per-key remaining-load vector; canonicalized under relabeling (color refinement + within-class permutations). I verified the canonicalization is isomorphism-invariant and reproduces unlabeled-poset counts (A000112: 5,16,63,318,2045,16999 for n=3..8). `F(P)` is the minimax; `G(P,ℓ)` is the safety game requiring an optimal comparison (`max child F = F(P)−1`) at every node with both children feasible; `Λ(n)=min L: G(antichain,(L,…,L))`. The solver reproduces `S(n)=1,3,5,7,10,13,16` for n=2..8. An independent linear-extension-set implementation confirmed Λ(4)=3 (the n≥5 cross-check died with the backend).

## Mathematical finding

**Exact values (experiment):** Λ(2..8) = **1, 2, 3, 4, 4, 5, 5**.

- **Lower bound [deduction]:** on the longest path Σₓ loadₓ = 2·S(n), so `Λ(n) ≥ ⌈2S(n)/n⌉ = Ω(log n)`. Counting gives 1,2,3,3,4,4,4 for n=2..8.
- **Pattern:** `Λ(n) − ⌈2S(n)/n⌉ ∈ {0,1}` for every n≤8, i.e. empirically `Λ(n) ≈ 2 log₂n − O(1) = Θ(log n)`.
- **Falsification attempt failed as a disproof:** no n≤8 forces any key above `4·log n`; the O(log n) horn survived and the ω(log n) horn has no support. I also **could not prove** the uniform upper bound — that needs a load-balancing lemma at every optimal state I could neither prove nor refute. The precise falsifiable next question is the conjecture `Λ(n) ≤ ⌈2S(n)/n⌉ + 1` for all n (which would settle the front positively with c=2).

## Distinctions required by the task

- **General posets vs antichain root:** the solver uses poset minimax `F(P)` only as a subroutine; the question is about the single fixed antichain root. General-poset hardness does not transfer. The recent `sparse-optimal-comparison-graph` result (`C(T)=Kₙ` globally) concerns pairs over *different* paths, not per-key load on *one* path — it does not settle Λ(n).
- **Soundness ≠ completeness:** even an all-n O(log n) load normal form would only be a structural restriction (states representable in O(n log n) bits). It is not a sound+complete polynomial-size NP/coNP certificate for SORT-BOUND-U; NP membership stays open and the sparsity/Mahaney barrier is unchanged.

## Honest limits

No new S(n) or SORT-BOUND-U theorem, no counterexample. The n=9 computation was killed by the reported backend failure after enumerating all 183231 unlabeled 9-posets (SIGKILL with 13 GB free — not OOM), so the pattern is untested beyond n=8. The front's dichotomy remains open; the decisive obstacle is the all-n load-balancing lemma. Worktree left clean.

## Other metadata

```json
{
  "finished_at": 1795333385.61055,
  "started_at": 1795331706.9223166
}
```
