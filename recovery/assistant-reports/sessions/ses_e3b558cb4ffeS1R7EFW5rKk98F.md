# antonina-LOW1WG1NAz7N27MoHbxerf-speranski

Session: ses_e3b558cb4ffeS1R7EFW5rKk98F
Workspace: /home/lubko/soring-fronts/double-deletion-excess-20261110
Created: 1794300867483; updated: 1794304510633

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 511 (msg_1c4e19c21001mWzZO2iH52IfOO)

Done. Summary of the work and result:

## Result

**Fixed-r cross deletions from `A_a(+)A_b` are E-controlled.** For every finite posets `X,Y` and `P=(X(+)Y)-D` with `|D|=r`:

$$|d(P)-d(X(+)Y)| \le r$$

where `d(P)=F(P)-ceil(log2 e(P))`. For `X=A_a, Y=A_b`, since `d(A_a(+)A_b)=E(a)+E(b)+δ` with `δ∈{0,1}`:

$$E(a)+E(b)-r \le d(P) \le E(a)+E(b)+1+r.$$

So no fixed-r deletion family from antichain ordinal sums can have unbounded excess unless `E(n)` is unbounded. The single-deletion equivalence extends to every fixed `r`; the amplification family's growth requires a growing number of deletions.

## Proof sketch

- `e(P)=Σ_{S⊆D} e(O_S)`, where `O_S` is the complete bipartite orientation with pairs in `S` reversed. In `O_S` every cross pair is comparable, so extensions inject into pairs of extensions of `X` and `Y`; hence `e(P)≤2^r e(X)e(Y)`. Also `e(P)≥e(X)e(Y)`.
- `F(P)≥F(X(+)Y)=F(X)+F(Y)` by monotonicity and ordinal-sum additivity.
- `F(P)≤F(X)+F(Y)+r` by sorting `X`, sorting `Y`, then comparing each deleted pair.
- Combining gives the two-sided bound.

For antichain bases, `e(P)≥a!b!+r(a-1)!(b-1)!`, with equality for a matching deletion; matching therefore maximizes the certified lower bound. With published exact `S` for `a,b≤22`, the maximum certified excess is **3**, attained at `(a,b)=(13,14)`/`(14,13)` for `r=2,3` (`e=548826538463723520000` / `551809291390156800000`, `ceil(log2 e)=69`, `F∈[72,74]` / `[72,75]`). For `a` or `b>22`, the unconditional certified bound is ≤1. No certified excess ≥5 exists.

## Verification

- Inclusion-exclusion `e`-count and `e(P)≤2^r a!b!` checked against two independent counters (order-ideal DP, minimal-element recursion) on all patterns with `a,b≤5`, `r≤3`.
- `e(O_S)≤a!b!` checked exhaustively over all orientations of `K_{a,b}` for `a,b≤4`.
- Two-sided theorem checked by exact `F,e` on all antichain deletion patterns `a,b≤4`, `r=1,2`, and on a non-antichain base family.

## Delivery

One board comment posted to issue #301 at `2026-11-10T09:53:25Z`, author `SoringP1 frontier: double-deletion-excess`, confirmed present exactly once. Worktree clean at `6a96398`; no repo/Lean/PR changes. Scratch is under `/tmp/opencode/ddel/` (`counters.py`, `search.py`, `post.md`, `post_result.json`).
