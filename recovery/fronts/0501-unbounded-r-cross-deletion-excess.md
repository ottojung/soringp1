# unbounded-r-cross-deletion-excess

## status

investigated

## origin

ai_proposal_unverified

## agent_id

OOAOJ6zNKM3c627OHEi990-signed

## exit_state

clearexit

## question

For P=(X(+)Y)-D with |D|=r cross relations deleted, the fixed-r theorem gives |d(P)-d(X(+)Y)| <= r; is there an all-n family with r=r(|X|,|Y|) growing so that the excess d(P) grows without bound, or is the excess always controlled by d(X(+)Y)+O(r)?

## basis

Newest board #301 double-deletion-excess (2026-11-10T09:53Z) proves |d(P)-d(X(+)Y)| <= r for fixed r and explicitly leaves the growing-r regime open; the ledger has no unbounded-r front.

## falsifier

Exhibit an explicit infinite family with r growing and d(P)-d(X(+)Y) >= c*r for some fixed c>0, or prove a uniform additive control for all growing r.

## implication

A growing family would show the fixed-r E-control is not robust under unbounded deletions, sharpening the prime-excess barrier; a uniform control would isolate the unbounded-r regime as unable to amplify local excess.

## finding_unverified

tact cross relations plus the sorted orders). Thus the undetermined set is a monotone “staircase/rectangle” `R = {i>=i0, j<=j0}` of size `a'b' <= |D| = r`, and all other pairs in `D` are resolved by transitivity. The remaining task is exactly merging the `a'`-suffix of `X` with the `b'`-prefix of `Y` (a monotone boundary), of minimax cost `M(a',b') <= a'+b'-1`. So `F(P) <= F(B)+M(a',b')`. [deduction]
3. **Excess bound.** `d(P)-d(B) = (F(P)-C(P)) - (F(B)-C(B)) <= F(P)-F(B) <= M(a',b')` since `C(P) >= C(B)` (`e(P) >= e(B)`). With `a'b' <= r`: if `a',b'>=1`, `M(a',b') <= a'+b'-1 <= 2√(a'b') <= 2√r` (AM–GM); if one side is 1, `M(1,r') <= ⌈log2(r'+1)⌉ <= ⌈log2(r+1)⌉`. Hence `d(P)-d(B) <= max(2√r, ⌈log2(r+1)⌉, r)` but more tightly `<= 2√r` for `r>=1` in the nondegenerate cases and always `o(r)`; in every case `< c*r` for any fixed `c>0` once `r` is large enough. [deduction]
4. **Tightness direction (not pursued to a theorem).** `M(a',b') - (C(P)-C(B))` can be positive but is bounded by the merge-vs-information gap on a rectangle, expected `O(log r)` in balanced cases and `0` in the fan/size-1 cases; this is consistent with known board families (matchings/fans give `O(1)` or `0` difference). I did not construct an explicit `Θ(√r)` family, only the upper barrier.

## Attempted/considered falsification (and why it fails)

- **Direct linear amplification via “each deleted pair costs 1”:** fails because many deleted pairs become forced by transitivity once `X,Y` are sorted (unresolved set collapses to a monotone rectangle of area `<=r`, cost `M(a',b') <= a'+b'-1`). [deduction]
- **Forcing large `F(P)-F(B)` by adversarial order:** adversary controls extensions but cannot make the unresolved rectangle larger than implied by `D`/monotonicity; after sorting, its size is `a'b' <= r`. [deduction]
- **Forcing large `d(P)-d(B)` by keeping `e(P)≈e(B)`:** `C(P)>=C(B)` so small `e(P)-e(B)` only helps the upper bound; the obstruction is the merge cost, which is `o(r)`. [deduction]
- **General-poset / non-cross intuition:** irrelevant here; result is specific to `P=(X(+)Y)-D` and uses only sorting/merge structure (certificate *soundness* of the information bound `F>=C` is used; no completeness claim). [deduction]
- **Small experiment discriminant:** not run; the rectangle/merge reduction is a complete paper argument for the stated falsifier and small cases cannot distinguish `Θ(√r)` from `Θ(r)` asymptotically.

## Honest limits and scope

- **Not proved:** an exact constant/shape-optimal bound `sup_{|D|=r}(d(P)-d(B)) = Θ(√r)` or `Θ(log r)` (I give `O(√r)` upper, not a matching lower construction). I did **not** produce an explicit family achieving `Θ(√r)` difference, only ruled out `Θ(r)`.
- **Model/care points:** uses `F(B)=F(X)+F(Y)` and standard merge complexity `M(a,b)`; for general posets `X,Y`, “sorting” means determining their linear extension (`F(X),F(Y)`) and the merge is on the resulting total orders. I did not re-derive ordinal-sum additivity here (treated as established, consistent with prior board/standard). No claim about absolute `d(P)` when `d(B)`/`E(n)` is large, and no `S(n)` or `SORT-BOUND-U` complexity bound/separation.
- **Completeness vs soundness:** `C(P)` remains a sound lower bound; no succinct certificate or completeness result is claimed.
- **No repository/Lean/board side effects** were made. If this is to be recorded on #301, it should be posted once (after review for duplication/wording) as a frontier finding; I have not posted it.

## Other metadata

```json
{
  "finished_at": 1794315029.0068634,
  "started_at": 1794313641.435966
}
```
