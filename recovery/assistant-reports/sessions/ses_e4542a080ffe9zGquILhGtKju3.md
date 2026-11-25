# antonina-tKiIEQVFCF446r1ksJanMD-angio

Session: ses_e4542a080ffe9zGquILhGtKju3
Workspace: /home/lubko/soring-fronts/curator
Created: 1794134335370; updated: 1794134926893

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1babd5fc4001QzglW88Yh63y9v)

I'll start by studying the repository context and then look for a genuinely new research direction grounded in the current board state.

## Output 268 (msg_1bac647db001x8jcNsdO1byDK7)

Wrote `/home/lubko/soring-fronts/curator/frontier-candidates.json` (3 new fronts; schema, ID uniqueness, and length checks pass). No commit, no Lean, no board post; the only change is the untracked candidates file.

**Proposed fronts**

1. `s-p-recursive-exact-sequence` — Is `S(n)` P-recursive/holonomic with bounded order and degree? A positive explicit recurrence would give a poly-time evaluator (hence `SORT-BOUND-U ∈ P`); non-holonomy would rule out every finite-order exact formula. Absent from all 360 ledger entries.
2. `s-polynomial-size-lp-exact-value` — Is `S(n)` the optimum of an explicit poly-size rational LP? Positive ⇒ `S_unary ∈ FP`/P; an extension-complexity lower bound would rule out convex-relaxation evaluators. No LP/SDP/extension-complexity front exists in the ledger.
3. `s-optimal-tree-average-depth-gap` — Among height-`S(n)` trees, is the minimum average depth `≤ log2(n!) + O(1)`? I ran an independent exact DP for `n≤6`: it reproduces `S=(0,1,3,5,7,10)` and gives average-depth excesses `0, 0, 0.0817, 0.0817, 0.0264, 0.0859`.

**Honest limits**

- The `n≤6` average-depth computation is small-instance evidence, not an all-`n` result; it only shows the entropy gap is tiny where `S(n)=C(n)`.
- Front 3 is the weakest: its `O(1)` alternative is *implied by* bounded excess, so the genuinely new content is the unbounded alternative; I flagged this in the basis rather than overclaiming independence.
- Fronts 1–2 rest on conditional implications, not proofs. I did not establish non-holonomy, LP lower bounds, or any complexity-class separation.
- I did not investigate general-poset hardness results as evidence about `S(n)`; no reduction back to the antichain root was assumed.
