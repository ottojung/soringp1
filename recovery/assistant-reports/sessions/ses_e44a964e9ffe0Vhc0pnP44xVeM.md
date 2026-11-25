# antonina-jjgcnu9J0WxovUWeokoxLE-deed

Session: ses_e44a964e9ffe0Vhc0pnP44xVeM
Workspace: /home/lubko/soring-fronts/linear-time-logspace-sortnumber
Created: 1794144377726; updated: 1794144951584

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 274 (msg_1bb5e5e33001BjGs61qsxOKkKf)

**Recovery/effect audit.** Worked on `billy-dev` only. The worktree was clean and the ledger front `linear-time-logspace-sortnumber` was still `running` with no recorded finding. I searched the board for this front and for the relevant space/automaticity terms: no prior comment existed for it. I made exactly **one** new board comment, id `sha256:SUZ3UJuQaE7BL0kyBEMB71hnqn9dKymhy1HMXccAwdE` (2026-11-08T13:34:33Z). No repository, Lean, commit, or ledger changes; no duplicate posts.

**Mathematical finding — a barrier inside the target class.** Let `C = DTIME(n) ∩ DSPACE(log n)` on a multitape TM with unary input and a separate output tape. Define

`A(n) = Σ_{m≤n} ceil(log2 m) = n·ceil(log2 n) − 2^{ceil(log2 n)} + 1`,
`T(n) = A(n) − floor(√n)`.

Then:

1. `T ∈ C`: unary-to-binary conversion is `O(n)`; the rest is `O(log³ n)` arithmetic.
2. `T(n) = n log2 n + O(n)`, hence `T(n) = S(n) + O(n)` from the known sorting bounds.
3. For all `n ≥ 3`, `1 ≤ T(n) − T(n−1) ≤ ceil(log2 n)` — exactly S’s proven monotonicity/Lipschitz envelope.
4. `T(n) mod 2` is **not** 2-automatic.

For (4): `ceil(log2 n) mod 2` is 2-automatic (its 2-kernel has at most four elements), while the perfect-square indicator is not 2-automatic by Christol’s theorem (`Σ x^{m²}` is not algebraic over `F₂(x)`). Since `T(n)−T(n−1) = ceil(log2 n) − 1_{n square}`, automaticity of `T mod 2` would imply automaticity of the square indicator.

**Consequence.** Monotonicity, the exact increment envelope, `Θ(n log n)` growth, `O(n)`-proximity to S, and nonautomatic residues do **not** separate a sequence from `C`. Therefore even a successful proof that `S mod p` is nonautomatic would not prove `S ∉ C`; the `s-residue-automaticity` route cannot supply this lower bound. The same construction puts the nonregular, non-context-free unary square language in `C`, so regularity/context-freeness/automaticity methods also fail.

**Other exact obstructions.**
- Ω(n) time is trivial, but O(log n) **work** space is not forced if the output tape is separate; only Ω(1) work space is forced.
- The function front implies `SORT-BOUND-U ∈ DTIME(N) ∩ DSPACE(log N)`, but binary search only gives `O(n log n)` time from the decision problem, not `O(n)`.
- A superlinear-time or superlog-space lower bound is a fixed-polynomial/fixed-space bound, not `S_unary ∉ FP`, and is not implied by `P ≠ PSPACE`.
- General-poset #P-hardness and PSPACE-hard games do not transfer to the antichain root; the `2^{Ω(n log² n)}` winning frontier bounds enumeration, not selective evaluators.
- Certificate soundness is not completeness: a height-k tree/DAG is checkable but explicitly exponential, so it gives no polynomial certificate.
- The standard transcript DFS’s per-level cursor obstruction is real but only applies to that DFS, not arbitrary evaluators.
- `S(n) ≥ ceil(log2 n!)` is a value bound, not a computation-time bound; and `ceil(log2 n!)` is not known to be in `C`.

**Honest limit.** Neither horn is resolved. No `O(n)`-time/O(log n)-space evaluator and no unconditional superlinear-time or superlogarithmic-space lower bound was found. `T` is a constructed model sequence, not `S`; the result is a genuine barrier to a family of lower-bound methods, not a disproof. The missing S-specific lemma is an all-n arithmetic/minimax description of `S(n)−S(n−1)` or `S(n)−ceil(log2 n!)` strong enough to evaluate in `C`.

## Output 319 (msg_1bb5f3aae001a2TqMfTwuJN5jK)

**Recovery audit completed; no work was repeated.**

- **Host:** `billy-dev`.
- **Git:** working tree clean at `6a96398`; no commits, branches, files, or Lean changes from this session.
- **Board #301:** exactly one matching comment exists for this front — `sha256:SUZ3UJuQaE7BL0kyBEMB71hnqn9dKymhy1HMXccAwdE`, posted `2026-11-08T13:34:33Z`. I did not post again.
- **Ledger:** `linear-time-logspace-sortnumber` is still `running` under agent `jjgcnu9J0WxovUWeokoxLE-deed`, with no recorded finding. This is expected while the current session owns the claim; the keeper should mark the exit state when the process ends. I did not edit the ledger, to avoid conflicting with the keeper’s claim/exit handling.
- **Uncertain effects:** none found. The only external effect is the single board comment, confirmed present exactly once.

**Research status from the completed turn.** The front remains open: no `O(n)`-time/`O(log n)`-space evaluator and no superlinear-time/superlogarithmic-space lower bound. The substantive output is a barrier theorem: the class `DTIME(n) ∩ DSPACE(log n)` on unary inputs contains a monotone `Θ(n log n)` sequence `T` with increments in S’s proven envelope `[1, ceil(log2 n)]`, `T(n)=S(n)+O(n)`, and **nonautomatic** residues. Hence automaticity/regularity arguments cannot prove `S ∉ C`, even if `S mod p` is shown nonautomatic. General-poset hardness and certificate soundness do not transfer to the antichain root. The missing input remains an all-`n` arithmetic/minimax description of `S(n)−S(n−1)` or `S(n)−ceil(log2 n!)`.

No further side effects were performed.
