# antonina-XpvDgXk7piDyQpm0fCYtIU-stroking

Session: ses_e11372184ffeLtB1OegcBr3eEp
Workspace: /home/lubko/soring-fronts/deterministic-exact-s-time-exponent-nlogn
Created: 1795007504076; updated: 1795007856403

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 179 (msg_1eecb78ea0018isda5gIH70Zhx)

# Finding (open; no 2^{O(n log n)} evaluator found, no universal 2^{Omega(n log^2 n)} lower bound proved)

**Environment/context (billy-dev).** Read-only analysis on `billy-dev` in `/home/lubko/soring-fronts/deterministic-exact-s-time-exponent-nlogn` (HEAD state as checked). Studied `AGENTS.md`, `docs/problem.md`, `docs/research-budgeted-dfs.md`, `docs/operations.md`, `docs/literature.md`, `docs/upper-bound.md`, `docs/research-certificates-barriers.md`, `docs/research-hardness-boundaries.md`, `docs/research-winning-frontier-barrier.md`, `docs/research-budget-pruning.md`, `docs/research-time-exponent.md`, `docs/research-compression-next.md`, and board #301 via `python3 /home/lubko/soring301/scripts/board_digest.py --recent 10` / `--contains "S_unary"` / `--contains "2^{O(n log n)}"` (no posted resolution of this exact front found). No Lean or repository changes made (no substantive independently checkable new theorem/counterexample).

**Front attacked (all `n >= 1`, falsifiable).** Is `S_unary(1^n)` computable by a uniform deterministic algorithm in worst-case time `2^{O(n log n)}` (numeric `n`), below the known `2^{O(n log^2 n)}` transcript-bounded DFS bound?
- **Positive falsifier:** explicit uniform deterministic algorithm + correctness and `2^{O(n log n)}` time proof for all `n`.
- **Negative falsifier:** rigorous proof that every uniform exact evaluator of `S_unary` requires `2^{Omega(n log^2 n)}` time on infinitely many `n`.

**Result: neither falsifier established.** The question remains open. I did not find (in the cited repository state/primary literature summaries) a `2^{O(n log n)}` exact evaluator for `S_unary`, and I did not obtain a universal `2^{Omega(n log^2 n)}` lower bound for all exact evaluators. Below are the concrete obstructions and failed/refuted routes identified; claims are labelled [definition]/[literature]/[deduction]/[open] per repo convention.

## 1. Baseline and where the `log^2 n` comes from [definition]+[deduction]

- Model/encodings: `S(n)=min{height(T): T sorts all permutations of n distinct labelled keys adaptively}`; `S_unary(1^n)` returns (binary) `S(n)` on unary input of length `n`; numeric-`n` bounds are the relevant measure here (`docs/problem.md`, `AGENTS.md`).
- Budgeted/transcript DFS for the minimax game `G(n,k)` (`S(n)<=k` iff sorter wins): depth `d <= U(n)=O(n log n)` comparisons, at most `2*B = n(n-1)=O(n^2)` move/answer branches per node, so the standard node-count upper bound is `(2B)^d*poly(n)=2^{O(d log n)} = 2^{O(n log^2 n)}`; polynomial transcript/stack space `O(n log^2 n)` bits (`docs/research-budgeted-dfs.md` §§2–5; `docs/upper-bound.md` for the weaker `2^{O(n^2)}` DP). Computing `S(n)` by monotone threshold search adds only `poly/log n` factors.
- **Analytic obstruction of this bound form [deduction]:** for any argument of the form `T <= (branching)^depth * poly` with depth `>= c1*n log n` (forced by `S(n) >= ceil(log2 n!) = Theta(n log n)`) and worst-case branching `>= n^c2`, `c2>0`, one gets `T >= 2^{Omega(n log^2 n)}` *as that counting bound*. Therefore improving the **transcript-DFS analysis** to `2^{O(n log n)}` would require a proof of effective branching `2^{O(1/log n)}` on the decisive exact searches or a fundamentally different node accounting; this is an obstruction to the current analysis/method form, not a lower bound on the true running time of DFS nor on all algorithms.

## 2. Antichain-root winning-frontier enumeration barrier (method barrier, not time lower bound) [literature]+[deduction]

`docs/research-winning-frontier-barrier.md` (paper-level theorem, exact witnesses; model = adaptive comparison sorting, `F(P)` minimax remaining comparisons from partial order `P`, reachable from the `n`-antichain):

- For infinitely many `n`, there is a common comparison depth `t <= k` with `>= 2^{((1/4-o(1)) n (log2 n)^2)}` pairwise **nonisomorphic** reachable partial orders `P` that are winning at budget `k-t` (`F(P) <= k-t`). The note extends this from the information budget `k=ceil(log2 n!)` to the **exact optimal budget `k=S(n)`** using Sergeev's asymptotic `S(n)-log2(n!)=o(n)` [literature, Sergeev ECCC TR20-096 (2020), as cited there].
- **Consequence [deduction]:** any uniform method that must enumerate/output all such reachable winning states at that frontier (even up to isomorphism) requires `2^{Omega(n (log n)^2)} = 2^{Omega(n log^2 n)}` states/time in that enumeration sense.
- **Crucial limitation (stated by the source, preserved here):** this is **not** a time lower bound for computing `S(n)`. A selective or symbolic evaluator need not list the frontier; the theorem excludes only full winning-frontier enumeration methods and does not establish space/time lower bounds for arbitrary solvers, nor NP/PSPACE hardness or any class separation. It therefore blocks one natural route to "small" state exploration but does **not** falsify the existence of some other `2^{O(n log n)}` exact evaluator.

## 3. Failed/refuted local routes to collapsing the search (no exponent gain shown) [deduction]+[experiment, as reported]

- **Within-state automorphism-orbit pruning alone [deduction, `docs/research-time-exponent.md`]:** the staircase height-two family `P_m` on `n=2m` has trivial `Aut(P_m)` and exactly `3*binom(m,2)=Theta(n^2)` incomparable pairs, hence `Theta(n^2)` singleton move-orbits; for odd `n`, `Q_m = P_m (+) C_1` gives the same. Thus automorphism-only move reduction cannot make candidate comparisons subquadratic at every state. This rules out symmetry-alone branching collapse; it is not a time lower bound for computing `S(n)` and does not preclude other pruning/selection.
- **Aut(P) move orbits in practice [experiment, `docs/research-budget-pruning.md`]:** orbit reduction is sound but can increase wall-clock (automorphism computation overhead) and does not change the worst-case exponent; in that prototype the current orbit bookkeeping also sacrifices the polynomial-space guarantee (a streamable variant is not established there).
- **Extension-count cutoff / Hanamura–Iwata base [deduction/literature/experiment, `docs/research-budget-pruning.md`]:** sound and give large **decision-side** speedups (many `False` probes collapse when `d < ceil(log2 e(P))`, e.g. at the root when information-tight), but do not touch the hard `True`/indeterminate cases with `e(P) <= 2^d` and do not improve the asymptotic worst-case exponent.
- **Ordinal-sum allocation [deduction/experiment, `docs/research-budget-pruning.md`, `docs/research-series-decomposition.md`]:** exact (`F(A(+)B)=F(A)+F(B)`) but does not shrink the antichain-root worst-case state space/call count in the reported no-memoization setting (and the root is series-prime).
- **Full poset DP [deduction/literature]:** reaches all `A001035(n)=2^{Theta(n^2)}` labelled posets (`docs/upper-bound.md`, `docs/research-certificates-barriers.md`), worse than the DFS worst-case bound.
- **Generic/general-poset hardness or approximation results do not transfer [literature/deduction, `docs/research-hardness-boundaries.md`, `docs/research-certificates-barriers.md`]:** Hyafil–Rivest/Laber–Nogueira concern arbitrary tests (not the fixed pairwise-comparison family of `S(n)`); Cardinal et al. give constant-factor approximation in query count, not exact `S(P)`/`S(n)` evaluation; Mahaney/related barriers apply to the sparse unary language in specific reduction senses and do not yield an exact-evaluation time lower bound here. Certificate soundness (e.g. a witness for `S(n)<=k`) must be distinguished from completeness/existence of succinct optimal certificates (open; `docs/research-certificates-barriers.md`).

## 4. Why the requested universal negative falsifier was not obtained [open; honest limit]

A proof that **every** uniform exact evaluator of `S_unary` needs `2^{Omega(n log^2 n)}` time on infinitely many `n` would be a strong unconditional time lower bound against all algorithms for a specific natural function (the minimax value of an explicit game). I found no such argument in the studied material and no technique available here to establish it:
- The strongest relevant structural barrier identified is the `2^{Omega(n log^2 n)}` winning-frontier *enumeration* count at exact-optimal budget (§2), but it explicitly does not rule out selective/symbolic evaluation.
- `SORT-BOUND-U` is in PSPACE (indeed much stronger known explicit bounds hold; `docs/problem.md`, `docs/research-budgeted-dfs.md`) and, as a tally language, in `P/poly` (`AGENTS.md`), so unconditional super-polynomial lower bounds for it run into major open-separation territory; a `2^{Omega(n log^2 n)}`-vs-`2^{O(n log n)}` separation for all evaluators is, a fortiori, beyond current methods available in this analysis. I do **not** claim such a separation is impossible, only that it is unproved and unsupported by a known method.

## 5. Assessment against the front

- **`2^{O(n log n)}` algorithm (positive falsifier):** not found/constructed; no representation or exact search scheme with a proved `2^{O(n log n)}` node/state bound for all `n` was identified. Known exact methods give `2^{O(n log^2 n)}` time (`docs/research-budgeted-dfs.md`) or worse (`2^{O(n^2)}` DP). [open]
- **`2^{Omega(n log^2 n)}` for every evaluator (negative falsifier):** not proved. Established only as a barrier for frontier-enumeration methods and as the analytic bottleneck of transcript-branching counting (§§1–2), not universally. [open]
- **Falsification attempt summary:** I tried to attack the positive side by checking standard improvement routes (symmetry/duality/orbit move reduction, information/cutoff/base pruning, ordinal decomposition, full-state compression, general-poset/certificate transfer, frontier size implications) against the antichain-root exact-evaluation goal; each either fails to transfer, is sound without asymptotic exponent gain, or yields a method-specific (not universal) obstruction. No counterexample `n` to "improvable below `2^{O(n log^2 n)}`" was produced, and none is implied.

**Concrete next decisive obstacle (if pursued).** Any genuine `2^{O(n log n)}` uniform exact evaluator must avoid both (i) the `2^{Theta(n log^2 n)}`-scale branching-accounting regime and (ii) dependence on enumerating the `2^{Omega(n log^2 n)}` exact-optimal winning frontier; equivalently it would need a provably complete representation/search over only `2^{O(n log n)}` *decision-relevant* objects (or a different algebraic characterization of `F(empty_n)=S(n)`) with polynomial-time local transitions — a property not currently known for optimal-play states (`docs/research-certificates-barriers.md` §8, "optimal-play state count" open). Conversely, a universal lower bound would require a model-sensitive argument excluding all selective/symbolic exact evaluations, for which no known technique applies here.

## Output 347 (msg_1eece31d60016184kGN1ZaNEZV)

**Recovery complete.**

Side-effect audit:
- **Git/worktree:** clean at `6a96398`; no commits, branches, stashes, or file changes. Verified.
- **Board #301:** exactly **one** new comment posted for this front at `2026-11-18T13:17:22Z` (author `SoringP1 frontier: deterministic-exact-s-time-exponent-nlogn`); verified present once via `board_digest --contains`. No duplicate post.
- **Ledger:** left as `running` (keeper-managed reconciliation); not hand-edited, to avoid conflicting records.

Unfinished work performed now (single action): posted the concise mathematical finding/obstruction report for front `deterministic-exact-s-time-exponent-nlogn`. No further side effects.

**Outcome already delivered (summary):** The question — whether `S_unary(1^n)` is computable in uniform deterministic time `2^{O(n log n)}` below the known `2^{O(n log^2 n)}` transcript-DFS bound — remains **open**. Neither falsifier was established: no `2^{O(n log n)}` algorithm constructed, and no universal `2^{Omega(n log^2 n)}` lower bound proved for all exact evaluators. The report records the concrete obstructions (analytic branching-depth accounting; `2^{Omega(n log^2 n)}` winning-frontier enumeration barrier that explicitly does not exclude selective/symbolic evaluation; refuted symmetry/cutoff/ordinal/full-DP routes) and honest limits. No Lean or repository changes.
