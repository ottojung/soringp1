# antonina-vObquh9MGlnQW86DM83ro8-name

Session: ses_e3b1c02b3ffeq4C2W1cmZn1jLb
Workspace: /home/lubko/soring-fronts/adversary-optimal-state-minimum-growth
Created: 1794304638331; updated: 1794309419304

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1c4e3ffc3001GoHj6CQtk7T7eG)

I'll start by studying the repository contract, problem definition, and the current board state.

## Output 121 (msg_1c4e4e0e00011b4yG5lvSAr9nr)

Now let me examine the frontier ledger for this front and related prior work, to avoid duplication.

## Output 184 (msg_1c4e659c2001ndYOjPElTz91bQ)

Let me look at related prior fronts and search the board for overlapping work.

## Output 195 (msg_1c4ead33d001rTjOfYeL265l7W)

Let me check available solvers and understand the computational landscape.

## Output 236 (msg_1c4f1595a0010EzD4OaFcAfLK0)

Let me examine the prior solver outputs and think about the structure. First, let me look at the existing implementation more carefully and check what exact data we have.

## Output 253 (msg_1c4f237010012keo0K3enR4jUS)

Let me write a clean solver to compute the exact minimum adversary memory for small n, and explore the structure.

## Output 273 (msg_1c4f8b81d0010Kr7Vl431TawzU)

The local search improved 114 → 96. Let me build an exact branch-and-bound solver to pin down the true minimum for n=4 and n=5, and study the structure.

## Output 293 (msg_1c5086d90001uFSuS7JlRVeAEk)

The B&B is slow. Let me think more carefully about the structure and try a smarter exact approach with better lower bounds.

## Output 313 (msg_1c50961d60011IGbwmQs1rE6Kj)

Let me write an exact solver using a hitting-set formulation with strong pruning, and also test a key structural hypothesis about state merging.

## Output 333 (msg_1c518bd18001Y7b2d3N2Ki6GgG)

Let me seed the exact solver with the local-search solution and add a much stronger lower bound based on the level structure.

## Output 344 (msg_1c519ab3d001GcaF8pnAo3l7mX)

Let me first improve the local search to get a strong seed, then run the exact solver with it.

## Output 382 (msg_1c51af5dd0014cdtv0drKQJtMD)

Let me run the exact solver seeded with the best local-search solution, and in parallel compute the entropy adversary's state counts.

## Output 445 (msg_1c52c0b10001KO71zRJVS1cq6K)

## Scope / recovery
- Studied `AGENTS.md`, `docs/problem.md`, and board `#301` context (including the prior `conp-adversary-memory` post at 2026-11-10T08:33Z and current frontier `adversary-optimal-state-minimum-growth`, running on this worktree).
- No repository/Lean/PR changes made (`git status` clean). No board posts or other external side effects were made by this turn. Local experiments were run only under `/tmp/opencode/conpmem2` (reproducible scripts there); the prior `/tmp/opencode/conpmem` artifacts from 08:33Z were inspected, not duplicated.

## Precise question attacked (all-n, falsifiable)
In the adaptive comparison game `G(n,k)` with `k=S(n)-1` (adversary wins iff sorter cannot force a total order within `k` comparisons), model an *explicit* adversary strategy as a closed memory/table: a set of states `M` with `(∅,k)∈M` such that for every `(P,r)∈M` and every sorter move (incomparable pair) there is some orientation/child in `M` [definition, standard strategy-automaton memory]. Claim under test: either (a) `min_{winning strategies} |M|` is superpolynomial in `n` for infinitely many `n`, or (b) some polynomial-in-`n` bound holds for all `n`.

## Mathematical findings

### 1. Small-n exact/upper-bound data (independent of, and consistent with, prior board post) [experiment]
Using a poset-closure minimax solver over labelled posets with budget states `(P,r)` (independent of the linear-extension solver in `/tmp/opencode/conpmem`), for `k=S(n)-1`:

| n | S(n) | k | admissible reachable `(P,r)` states | exact `min |M|` (this run) | best found upper bound `|M|` / distinct posets / unlabeled-poset classes |
|---|---:|---:|---:|---:|---|
| 2 | 1 | 0 | 1 | 1 | 1 / 1 / 1 |
| 3 | 3 | 2 | 13 | 8 | 8 / 8 / 4 |
| 4 | 5 | 4 | 243 | **open here** (B&B improved 114→107 then was interrupted; strong local search found 96) | ≤ 96 / 88 / 15 |
| 5 | 7 | 6 | 7821 | open | ≤ 3559 by linear-extension (LE) adversary / 2818 / 62 (greedy/LS upper bounds not completed here) |

Cross-checks: `n<=3` exact minima 1,8 match the 08:33Z post; admissible counts 243 (n=4), 7821 (n=5) match; level/pair structure matches (`n=4`: levels r=4..0 have 1,12,36,104,90 states with 6,5,4,~2.5 incomparable pairs/state; `n=5`: 1,20,180,820,1940,2650,2210).

**Honest limit:** no exact minimum obtained for `n>=4` in this run (branch-and-bound not completed), and `n>=6` not computed. These data do **not** establish or refute superpolynomial growth (insufficient range, and only bounds at n=4,5).

### 2. The admissible winning region is not poset-type sparse (structural obstruction, n<=5) [experiment]+[deduction]
For each `n∈{3,4,5}`, the set of unlabeled-isomorphism classes of posets appearing among admissible adversary-winning reachable states is exactly **A000112(n)-1 = 4,15,62** — i.e. **every non-total poset type on `n` elements** occurs somewhere in the winning region (per-level canonical counts: n=4 gives 1,1,3,6,6 classes at r=4..0; n=5 gives 1,1,4,11,27,32,31).

- Consequence [deduction]: there is **no** restriction to a special proper subclass of poset types that characterizes admissible/winning states in general; any memory model that stores (or must distinguish) states by their poset isomorphism type has an ambient universe of size `A000112(n)=2^{Θ(n^2)}` (Kleitman–Rothschild) already at the type level. This is stronger in form than “many states exist”: it says the *variety* is complete.
- The LE-balancing explicit adversary (answer by larger `e(P')`, restricted to winning children) is a simple, uniform-in-description rule and, on this data, its reachable closure also spans all 15/62 non-total canon classes for n=4,5 (122 states/15 classes; 3559/62). The best n=4 strategy found here (≤96 states) still uses **all 15** canon classes.
- Important distinction [definition]: “all types admissible/reachable” does **not** imply “all types unavoidable by every winning strategy.” Because the adversary may choose among multiple winning orientations, a minimal strategy could in principle avoid some types; this run gives no such avoidance (and no proof of impossibility of avoidance). Establishing a *forced* superpolynomial set of non-equivalent states would require a per-strategy lower bound (see obstruction).

### 3. Why the front remains open (exact obstruction)
- **General-state (enumerative) barrier exists but is not the claim:** winning-frontier / A001035-scale phenomena give `2^{Θ(n^2)}` labelled posets total and large winning families, but (as in `docs/research-winning-frontier-barrier.md` and prior board analyses) enumeration/counting of *possible* winning states does **not** lower-bound the memory of a *selective* strategy, nor rule out a poly-size description that computes answers on-the-fly. Certificate SOUNDNESS of a given small table is easy to check; COMPLETENESS/existence of a small table for all `n` is the hard direction.
- **State-merging minimization is the bottleneck:** for a fixed game graph it is a monotone closure/hitting-set minimization (each included `(state,pair)` must hit at least one winning child). I could not complete exact minimization for `n>=4` within budget (n=4: 243 states, 4 levels of pair-constraints; B&B showed progress but no certificate of optimality), so even the *finite* minimum at n=4 is not certified here beyond `96 ≤ M(4,4) ≤ 114` combined with prior bounds.
- **Labeling vs quotient:** an “explicit strategy table” against a labelled sorter is sensitive to element labels/pairs; quotienting by `S_n` is exact for poset values but a table indexed only by unlabeled type + budget is not, by itself, a complete interface unless it also specifies the pair/label mapping. A polynomial bound would need a uniform, checkable representation (not merely a count), which is not constructed.

### 4. Failed / inconclusive approaches (this pass)
- **Exact B&B for n=4:** improved upper bound 114→107 but did not terminate with optimality; not a proof (killed/interrupted). **Failed to certify** the minimum.
- **LE-balancing adversary as compact certificate:** gives a short *rule*, but its explicit reachable *table* is already 122 states (n=4) and 3559 (n=5) in this representation — not evidence for a poly-size explicit table, and (as a balancing heuristic) not by itself a proof of optimality except where minimax-verified (here winning region was enforced, so it is a valid winning strategy instance, but large).
- **Claim “all 2^{Θ(n^2)} poset types forced”:** refuted as stated — only *admissibility* of all types shown for n<=5, not per-strategy necessity.

## Complexity implication (careful)
- A proven superpolynomial lower bound on the minimum size of any explicit/checkable winning-adversary strategy representation (of a specified complete format) would obstruct explicit-table coNP-style witnesses for `SORT-BOUND-U` *in that format*, sharpening the adversary-memory/certificate barrier; it would **not** by itself separate uniform complexity classes or settle `SORT-BOUND-U ∉ NP/coNP` (cf. certificates-barriers, Mahaney/sparsity context in `docs/problem.md`).
- A polynomial-size, uniformly checkable explicit optimal adversary for all `n` would be a candidate compact refutation witness format for the relevant instances, but none is exhibited and the n<=5 type-completeness above is evidence of difficulty (not a proof of impossibility).

## Falsifier status
Neither branch of the falsifier is achieved: no infinite superpolynomial forced family exhibited, and no polynomial-size explicit optimal adversary for all `n` constructed/proved. Result is an **obstruction + small-n structural evidence**: the winning region spans all unlabeled poset types already at n<=5 (ambient 2^{Θ(n^2)}), the natural explicit-table memory is already nontrivial (≥96 states at n=4 in best found closure), and exact minima/any all-`n` theorem remain open.
