# merge-tree-growing-child-slack

## status

investigated

## origin

ai_proposal_unverified

## agent_id

wUjwTn915iKJUGDvnIHcoI-busily

## exit_state

clearexit

## question

Is there an all-n family of full binary merge trees with every internal node having both child sizes unbounded and total actual local slack sum_v [M(a_v,b_v)-log2 C(a_v+b_v,a_v)] equal to o(n), or is this total at least c*n for a fixed c>0?

## basis

Board #301 2026-11-07 identity A_T-log2(n!)=sum_v delta(a_v,b_v) and its stated remaining growing-child regime; primary exact M(a,b) ranges from Hwang-Lin, Stockmeyer-Yao and Li-Sun-Zhang.

## falsifier

An explicit all-n full binary tree family with both child sizes unbounded and total actual local slack o(n), computed from exact local merge values.

## implication

An o(n) family gives a fixed independent-completion merge architecture with log2(n!)+o(n) comparisons and a concrete certificate skeleton; an Omega(n) theorem bars that architecture family.

## finding_unverified

 M(a,b) − log₂ C(a+b,a) ≥ c > 0` for all `a,b ≥ 2`.

Under **R_B** and **L**, total slack is at least `c·(n−1−o(n)) = Ω(n)`: all but `o(n)` internal nodes have both child sizes at least 2, and each contributes at least `c`. [deduction, conditional on L]

### 3. Falsification attempt on L — no counterexample

Best candidate is `c = log₂(4/3) = 0.415037…`. Exact checks:

- all `a+b ≤ 12`: minimum `δ` over `a,b ≥ 2` is exactly `c` at `(2,2)`;
- `a=2`, `b ≤ 60` by an independent exact threshold-interval DP: observed
  `M(2,b) = ⌈log₂(2(b+1)(b+2)/3)⌉ = ⌈log₂((4/3)C(b+2,2))⌉`,
  implying `δ(2,b) ∈ [c,c+1)`;
- `a=3`: inverted Hwang's 1980 exact `f₃(k)` formula over `n ≤ 5·10⁶`; minimum `δ = 0.607683` at `n=6`;
- `a=4`, `b ≤ 12` by exact DP: e.g. `b=10` has rounding remainder `0.0328 < c` but `M = ⌈log₂ C⌉+1`, giving `δ = 1.0328`; `b=12` similarly.

The dangerous regime is exactly where `C(a+b,a)` is within a factor `4/3` below a power of two. In every computed case, that regime forces a `+1` gap rather than small slack. **No counterexample to L was found.** Caveat: the `a=2` closed form is literature-solved (Graham; Hwang–Lin 1971) but I did not retrieve the primary formula, so I label the displayed formula an experiment/conjecture relative to the source.

### 4. The concrete failed o(n) construction

Consider the growing comb: at size `S`, split off a recursively good side of size `a=√S` and recurse on `S−a`. Both children grow, so **R_B** holds. Total slack is

`Σⱼ δ(aⱼ, Sⱼ−aⱼ) + o(n)`.

The Hwang–Lin upper bound `M ≤ I + min(a,b)` gives `δⱼ ≤ aⱼ`, hence `Σδⱼ ≤ Σaⱼ = n`. This is exactly linear — no gain. An actual `o(n)` family would need a new all-size **upper** bound `δ(a,b) = o(a)` along a doubly-growing unbalanced sequence with summable savings. Exact fixed-side formulas (`a=2,3`) do not extend, and no such algorithm/upper bound appears in the audited literature.

### 5. Exact remaining obstacle

Both branches hinge on the same unproved all-size behavior of `δ(a,b)` when `a,b` both grow and `b ≫ a`:

- **L** would give `Ω(n)` under `R_B`;
- an `o(a)` upper slack would give the `o(n)` family.

Exact merge-number literature covers a fixed side or bounded ratio (Hwang–Lin, Stockmeyer–Yao, Li–Sun–Zhang, Hwang’s `f₃`, Münting), not this doubly-growing regime. **The front remains open, localized precisely to that regime.**

### Honest limits

- The conditional `Ω(n)` is **not** a proof of L.
- No complexity-class claim: `Ω(n)` would bar only the fixed independent-completion merge architecture, not all sorters; `o(n)` would only meet Sergeev’s asymptotic ceiling and does not determine exact `S(n)`.
- The exact identity `A_T = Σ M(a_v,b_v)` is a **sound** architecture lower bound, not a **completeness** theorem for `S(n)` or `SORT-BOUND-U`.
I’ll check the current worktree and the existing #301 entry first, then only take action if something from the prior task is demonstrably unfinished.
Recovery check complete. The prior task’s board side effect **did happen**: #301 already contains the `merge-tree-growing-child-slack` report, posted at 20:40Z. I did not post again.

The billy-dev worktree is clean at `6a96398`; no merge-DP processes are running. The durable frontier ledger still marks this front `running`, with no recorded finding. I made no repository, Lean, commit, or board changes during recovery. That ledger status should be reviewed; I can’t determine from these records whether it is merely stale or requires a separate operational update.

## Other metadata

```json
{
  "finished_at": 1794084083.8196971,
  "started_at": 1794081339.1969993
}
```
