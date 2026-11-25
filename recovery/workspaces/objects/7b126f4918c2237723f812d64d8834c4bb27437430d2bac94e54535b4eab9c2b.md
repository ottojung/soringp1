# Executive independent verification — two greedy-ball fronts — 2026-11-20 ~05:17Z

**Author:** Executive (session `vmjHeHAanEHVJEuhrnLwq3-saved`)
**Class:** independent verification / audit disposition — **not** a theorem claim,
**not** mission closure, **not** an Act 22 order, **not** a legislative act.
**Scope:** independently check the two #301 results posted at 05:01:00Z and
05:04:20Z that follow from the exp-lower-bound result verified earlier this cycle.

## Results checked and verdicts

Both are **accepted** as correct, honestly caveated, and NOT resolutions of the
SoringP1 headline theorems (`S(n)` / `SORT-BOUND-U` remain open; `S(23)`=[75,76]).

### 1. `greedy-ball-growth-exponent-alln` (05:01:00Z)
Claim: in the **adversarial-tie** model, `|R_{G(n)}(n)| >= n! = 2^{Theta(n log n)}`
for all `n>=2`, refuting a `2^{O(n)}` upper bound.

Verified independently:
- Proof structure sound: `e(P)` is `S_n`-invariant and greedy transitions are
  equivariant; the antichain is fixed by every relabeling, so the ball is
  `S_n`-invariant. The game strategy reaches a total order `T` within `G(n)`
  comparisons under any fixed greedy tie-break, so `T` is in the ball; a total
  order has trivial stabiliser, giving all `n!` relabelings. No `G(n)=S(n)` used.
- Own transitive-closure solver: unrestricted value matched known `S(n)` =
  1,3,5,7 for `n=2..5`; adversarial-tie ball sizes 3,19,219,4231 exactly matched
  the report; all `n!` total orders present (2/2, 6/6, 24/24, 120/120).
- Process transparency: my first solver omitted transitive closure and returned
  `C(n,2)` = 1,3,6,10; caught against the hard bound `G(n) <= S(n)`, fixed, then
  accepted.

Concur with limits: model-specific (adversarial ties); the earlier deterministic
`2^{floor(n/2)}` is a smaller distinct object; enumeration obstruction not a time
lower bound; exponent window `[n log2 n - O(n), O(n log^2 n)]` not pinned; no
certificate consequence; no class separation; no new `S(n)` value.

### 2. `greedy-ball-compact-index-alln` (05:04:20Z)
Claim: the matching gadget's `2^m` tied states collapse to `m+1` isomorphism and
value classes, so that gadget cannot force `2^{Omega(n)}` separation.

Verified independently:
- Canonical iso classes via minimum sorted relabeled edge tuple over `S_n`:
  exactly `m+1` for `n=4,6,8` (3,4,5). `e(P_T)=n!/2^t` depends only on `t=|T|`.
- Process transparency: my first canonicalization compared frozensets with `<`
  (subset order) and miscounted `2^m`; fixed to sorted tuples, obtained `m+1`.

Concur with limits: this refutes only the gadget-sourced negative horn, not the
positive horn (no poly-size subexponential evaluator exhibited); the full ball is
not claimed to collapse; a non-symmetric exponential tied family is not excluded;
no class separation; `G(n)=S(n)` (separate running front) not settled.

## External writes this cycle
- #301 verification for `greedy-frontier-state-growth-alln` — 04:31:02Z.
- #301 verification for `greedy-ball-growth-exponent-alln` — 05:16:43Z.
- #301 verification for `greedy-ball-compact-index-alln` — 05:16:49Z.
- This additive record. Each post confirmed exactly once on page 1, 0 on page 2.

No dispatch, merge, or repo/Lean/CI/main change. Research remains open.
