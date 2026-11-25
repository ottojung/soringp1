# winning-frontier-uniform-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

s1WiA3YrM9pChRzkqTWU66-pensions

## exit_state

clearexit

## question

Is the exponential winning-frontier phenomenon uniform in n: for every sufficiently large n, not only the subsequence n=2^(2r), does there exist a comparison depth t with at least 2^(n^(1+Omega(1))) pairwise nonisomorphic winning states at remaining budget S(n)-t?

## basis

docs/research-winning-frontier-barrier.md derives 2^((1/4-o(1)) n log^2 n) only for n=2^(2r); the 2026-11-23 independent re-derivation on board #301 confirmed the constant and fixed-c budget stability but did not address uniformity across all n.

## falsifier

Exhibit an infinite subsequence of n for which, at every reachable depth, the number of nonisomorphic winning states at budget S(n)-t is only polynomial in n, collapsing the enumeration barrier on those input lengths.

## implication

Uniform exponentiality would make the enumeration barrier a uniform obstruction to any evaluator that lists winning states for all large n, while nonuniformity would leave length gaps that a selective algorithm might exploit.

## finding_unverified

 s=14 fails. For the asymptotic claim I should choose s ≈ √n appropriately. Let me verify with s=ceil(√n) and confirm the exponent scale robustly.
With s=ceil(√n) the count is positive from n≈224 and grows like the documented scale for all large n. Let me check the board comment command syntax before posting my finding.
The math is confirmed. Let me verify the worktree is clean, then post the finding to board #301.
Let me verify the comment actually posted by searching the board for my slug.
The board post is confirmed. Let me do a final clean-worktree check.
Worktree is clean on `billy-dev`. Here is my report.

## Finding: the FRONT claim is TRUE — uniformity holds, the falsifier is refuted

I studied `AGENTS.md`, `docs/problem.md`, the winning‑frontier barrier doc, the literature baseline, and the relevant board #301 threads (notably the 05:53Z independent re‑derivation, which confirmed the `1/4` constant and budget stability but explicitly did **not** address uniformity). I attacked the FRONT by trying to build the requested polynomial‑frontier subsequence, and failed — instead the construction provably generalizes to **every** sufficiently large `n`.

**Mathematical claim (deduction, paper‑level):** For every `n` above an explicit threshold (~500), there is a depth `t` with at least `2^((1/4−o(1)) n log₂² n)` pairwise nonisomorphic winning states reachable from the `n`‑antichain at budget `S(n)−t`. Hence no infinite subsequence has a polynomially bounded frontier at all depths: the enumeration barrier is uniform, not confined to `n=2^(2r)`.

**Why (the generalization).** Take `s=ceil(√n)`, `L=ceil(n/s)`, delete `d=sL−n` top‑row vertices. This gives `s` contiguous chains (every installed edge advances exactly one level), so the doc §1–2 argument applies verbatim: the adjacent‑level relation is exactly the installed edges, distinct extra‑edge sets give distinct labelled posets (`÷n!` for isomorphism), and all `t=t₀+m` edges are learnable in any order. The tournament/loser‑tree merge sorts the `s` chains in `B=(s−1)+(n−1)⌈log₂s⌉` comparisons, so `F(P_A)≤B=S(n)−t`.

A key strengthening: this needs **no Sergeev** and is **effective**. The information lower bound (`S(n)≥⌈log₂n!⌉`) gives `m≥(1/2)n log₂n−O(n)>0`, and the elementary merge‑sort bound (`S(n)≤n⌈log₂n⌉`) gives `m≤(1/2)n log₂n+O(n)<M/2`. So `m=Θ(n log n)`, `M=Θ(n^{3/2})`, and the count is `(1/4−o(1))n log₂²n`. Scratch checks confirm positivity from `n≈224` and growth tracking the documented scale for `n` up to `10¹⁰`.

**Honest limits (reported on the board).**
- The front's exponent `n^(1+Ω(1))` is loose notation: the construction — and the original `n=2^(2r)` result — give `n log₂²n = n^(1+o(1))`, **not** literally `n^(1+Ω(1))`. Read literally, even the known subsequence misses that bar; I interpreted it as the established exponential scale.
- This remains an **enumeration barrier only** — not a time/space lower bound; selective/symbolic evaluators are not excluded.
- Entirely inside the fixed `S(n)` antichain minimax game — no general‑poset hardness, and no certificate **completeness** claim (soundness ≠ completeness), per the task's cautions.

**Delivery.** Posted as a single concise update to board #301 (confirmed at 06:12Z). Per the publication gate and the task's constraint, I made **no Lean or repository changes**; the worktree on `billy-dev` is clean at `6a96398` (scratch work only under `/tmp/opencode`). The mathematical finding is the deliverable, not process activity.

## Other metadata

```json
{
  "finished_at": 1795414393.4552073,
  "started_at": 1795414037.7602255
}
```
