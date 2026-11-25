# antonina-nJVAutU5vpht2MTyRi1ajp-neighbors

Session: ses_e44a9696bffe41qV2zW3CtA9WU
Workspace: /home/lubko/soring-fronts/output-polynomial-optimal-tree
Created: 1794144376658; updated: 1794145081912

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 356 (msg_1bb5fdcbb001S4PTuuAQ4irv6L)

**Recovery check.** I found no earlier board post for this front and no repository changes. The worktree is clean on `billy-dev`; the ledger entry is still `running` (live-agent bookkeeping). I posted exactly one new finding to Antonina #301 at `2026-11-08T13:36:13Z`; no duplicate post, commit, or Lean file was created.

## Mathematical finding

I could not disprove the front. The main result is a **one-sided barrier** explaining why its negative horn is out of reach with current techniques.

Define `COMPL(n,C,k)`: `C` is a valid partial comparison-tree prefix on `n` keys and can be completed to a correct height-`≤k` tree. This is the natural prefix-relative strengthening of the constructor; the front is the empty-prefix case.

**Theorem 1 [paper proof].** `COMPL ∈ PSPACE`.

For each hole `h` of `C`, let `P_h` be its transcript poset and `r_h` its residual budget. A completion exists iff every existing leaf is total and correctly labelled, and `F(P_h) ≤ r_h` for every hole. Each predicate `F(P) ≤ d` is the sorter–adversary game, decided by a polynomial-alternation ATM, hence in `APTIME(poly) = PSPACE` (Chandra–Kozen–Stockmeyer). Iterating over the holes preserves polynomial space.

**Theorem 2 [paper proof].** `P = PSPACE` implies the front, with some absolute constant `c`.

If `P=PSPACE`, `COMPL` has a polynomial-time decider. Compute `S(n)`, then build top-down: at each hole, try the `O(n²)` pairs and keep one whose two-child extension `COMPL` accepts. At most `2·n!−1` nodes are expanded; every query has size `poly(n!)`; total time is `poly(n!)`.

**Corollary.** If no output-polynomial constructor exists, then `P ≠ PSPACE`.

So the front’s stated falsifier — an infinite-family lower bound on constructing every optimal tree — cannot be proved without at least proving `P ≠ PSPACE`. This is stronger than “separating value evaluation from witness construction.”

A more targeted sufficient condition is also visible: `COMPL` contains generalized poset sorting `GEN-SORT` as the single-hole case. Hence `GEN-SORT ∈ P ⇒ COMPL ∈ P ⇒` the front. The natural construction route therefore needs a polynomial-time exact generalized-sorting decider, not merely a faster evaluator of unary `S(n)`.

## Concrete upper bound and failed approach

The known top-down construction uses the budgeted DFS as a `CanSort` oracle:

- output tree size: `2·n!−1` nodes, hence `Ω(n! log n)` output bits;
- known construction time: `O(n²·n!·2^{O(n log² n)}) = 2^{O(n log² n)} = (n!)^{O(log n)}`;
- the exposed gap is a factor `log n` in the exponent.

I verified the constructor for `n ≤ 5` (heights `1,3,5,7`, all permutations correct). An `n=6` run exceeded a 3-minute temporary budget, consistent with the exponential oracle cost. The only unconditional lower bound found is `c > 1`, forced by output length.

The failed route is therefore precise: **top-down completion with the existing exact `F` oracle is not output-polynomial**, because each residual completion query is a generalized-poset problem costing `2^{O(n log² n)}`.

## Soundness versus completeness

- **Soundness:** given an explicit tree, correctness and height are checkable in `poly(output)`.
- **Value evaluation:** the budgeted DFS decides `S(n) ≤ k` in `2^{O(n log² n)}`.
- **Completeness/construction:** neither gives an output-polynomial *search* algorithm. The missing object is a completion oracle for arbitrary residual prefixes, i.e. generalized sorting.

General-poset hardness results (Hyafil–Rivest; Laber–Nogueira) concern arbitrary subset tests and do not transfer to pairwise comparison trees. Conversely, they do not supply a constructor.

## Honest limits

- I did **not** construct an output-polynomial algorithm.
- I did **not** prove an unconditional impossibility.
- The barrier is one-sided: `P=PSPACE` is sufficient but not necessary, and the original empty-prefix front could in principle be true even if `COMPL ∉ P`.
- A failure of the front would not by itself separate value from construction in the usual class sense: the known value upper bound is `2^{O(n log² n)}`, above the `2^{ω(n log n)}` threshold of front failure.
- No claim about `SORT-BOUND-U ∈ P` or `∈ NP` is made.

**Effects:** one board post, no repository or Lean changes, clean worktree.

## Output 413 (msg_1bb6146fa001w1HA13Z98sxPsG)

Recovery inspection complete. I did **not** repeat the research prompt or any external action.

**Effects that actually happened**
- Git: worktree is clean on `billy-dev` at `6a96398`; no commits, repo edits, or Lean changes.
- Board #301: exactly **one** matching post from this front, at `2026-11-08T13:36:13Z` (“uniform negative lower bound …”). No duplicate post exists.
- Temporary artifacts only: `/tmp/opencode/board_output_poly.txt` and `/tmp/opencode/build_tree_check.py`.
- Durable ledger: the `output-polynomial-optimal-tree` entry is still `status: "running"` with the live agent ID. That is normal keeper-managed bookkeeping; I did not manually edit it.

**Unfinished work**
None. The mathematical finding, upper bound, failed approach, barrier theorem, and honest limits are already recorded in the single board post.

**Uncertainty**
No external effect is ambiguous. The only pending state is the ledger’s `running` status, which the keeper transitions after agent exit.
