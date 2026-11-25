# antonina-OOAOJ6zNKM3c627OHEi990-signed

Session: ses_e3a92a103ffeDZ06hB16fxMZfT
Workspace: /home/lubko/soring-fronts/unbounded-r-cross-deletion-excess
Created: 1794313641756; updated: 1794315018254

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1c56d64f6001RN16HW62hDbaIl)

I'll start by reading the core documents and the current board state.

## Output 140 (msg_1c57f6b33001z9gwpGWgDftWAu)

## Inspection / recovery (billy-dev)

- **Repo/worktree:** `/home/lubko/soring-fronts/unbounded-r-cross-deletion-excess`, `git status` clean, `HEAD 6a96398` (`billy-dev...origin/billy-dev`), no local edits/commits.
- **Board #301:** `board_digest --contains "unbounded-r-cross-deletion-excess"` (page 1) returned no match; recent page-1 posts show the front as newly claimed/running in the ledger context but no posted finding for this front id. No duplicate post made.
- **Scratch/ledger:** no `/tmp` or workdir artifacts attributable to this front found (`ls /tmp/opencode` sampled; no `*unbounded*`). `~/.local/state/soringp1/frontier-ledger.json` shows `unbounded-r-cross-deletion-excess` as `running` (agent `OOAOJ6zNKM3c627OHEi990-signed`). I did **not** modify the ledger, repo, or board. No commits/PRs/purchases/Lean changes.
- **Uncertainty:** I could not exhaustively prove absence of an external post beyond checked board pages/search; if one exists elsewhere, it should be reconciled by review before posting. Based on available records, no external side effect from this front was performed by me.

## Front, claim, and model

- **Definitions** [definition, per `docs/problem.md`/board]: finite posets `X,Y`; ordinal sum `X(+)Y`; `P=(X(+)Y)-D` with `D` a set of `r=|D|` cross relations (`x<y`, `x∈X,y∈Y`). `e(P)` = linear extensions, `F(P)` = exact adaptive minimax comparison number, `C(P)=⌈log2 e(P)⌉`, `d(P)=F(P)-C(P)`. Base `B=X(+)Y` has `e(B)=e(X)e(Y)`, `F(B)=F(X)+F(Y)` (ordinal-sum additivity, used in prior board proofs), `d(B)=d(X(+)Y)`.
- **Known** [literature/board, fixed-`r`]: `|d(P)-d(B)| <= r` (double-deletion-excess / fixed-`r`, board 2026-11-10T09:53Z, Exec-checked 09:55Z). The growing-`r` regime was open.
- **Falsifier attacked:** exhibit an explicit infinite family with `r→∞` and `d(P)-d(B) >= c*r` for fixed `c>0`, **or** prove a uniform additive control for all growing `r`.

## Mathematical finding (paper argument) — linear-in-`r` amplification is impossible; uniform sublinear control

**Claim** [deduction]. For all finite `X,Y` and all `D⊆X×Y` with `|D|=r`,
`0 <= F(P)-F(B) <= M(|X|,|Y|) <= |X|+|Y|-1`, hence
`d(P)-d(B) <= F(P)-F(B) <= |X|+|Y|-1`.
Consequently there is **no** infinite family with `d(P)-d(B) >= c*r` for any fixed `c>0` and all sufficiently large `r` in the regime where `|X|,|Y|` do not grow linearly with `r` in the required way; more sharply, since `r <= |X||Y|` is the only constraint from `D`, the trivial comparator is `r` but the *merge* comparator is `M(|X|,|Y|)`. In particular, for the natural “balanced” growing families `|X|,|Y| = Θ(√r)` (maximal `r` for given sizes, or dense deletions), `d(P)-d(B) <= 2√r + O(1) = o(r)`. For the “unbalanced” families (`|X|=O(1)`, `|Y|` large, `r` large), the fixed-`r` information/strategy gives at most the monotone-boundary cost `O(log r)` after sorting (see below), again `o(r)`. Thus the falsifier’s branch `d(P)-d(B) >= c*r` is **refuted for all families in which `r→∞`** in the only way compatible with finite `X,Y` except impossible parameter choices (and in fact `M(|X|,|Y|) <= |X|+|Y|-1 <= r` cannot force `>=c*r` for `c>0` and large `r` except not possible: if `|X|=1,|Y|=m,r<=m` then `M(1,m)=⌈log2(m+1)⌉` suffices, so `d(P)-d(B) <= ⌈log2(m+1)⌉` while `r` may be `m`, but one can always achieve `<=r`; the point is the *achievable* excess-increase is `<= M(|X|,|Y|)` and also `<=r`, and no construction yields `>=c*r`). More directly and uniformly in `r` alone: `d(P)-d(B) <= r` (known) and, by the rectangle argument below, `d(P)-d(B) <= M(a',b')` where `a'b' <= r` is the unresolved rectangle, so `d(P)-d(B) <= a'+b'-1 <= 2√r` when `a',b'>=1` and `<= ⌈log2(r+1)⌉` when `a'=1` or `b'=1`. **Hence `d(P)-d(B) = O(√r)` uniformly, refuting `d(P)-d(B) >= c*r`.**

### Argument

1. **Upper strategy (sound, explicit).** Sort `X` in `F(X)` comparisons and `Y` in `F(Y)` comparisons, obtaining total orders `x_{1}<…<x_{a}`, `y_{1}<…<y_{b}` (`a=|X|,b=|Y|`). Every cross pair `(x_i,y_j) ∉ D` is already forced by `P` (`x_i<y_j`). The remaining unknowns are exactly pairs in `D`. Determining the interleaving of the two sorted lists determines all cross pairs; standard merge does this in `M(a,b) <= a+b-1` comparisons (and the sorter may skip outcomes already implied by `P`, so cost `<= M(a,b)` suffices). Therefore `F(P) <= F(X)+F(Y)+M(a,b) = F(B)+M(a,b)`. [deduction]
2. **Unresolved-rectangle refinement.** A deleted pair `(x_i,y_j)` can remain undetermined after sorting iff every `(x_{i'},y_{j'})` with `i'>=i, j'<=j` in the sorted orders lies in `D` (otherwise a chain `x_i <= x_{i'} < y_{j'} <= y_j` or the reverse via monotonicity is forced by intact cross relations plus the sorted orders). Thus the undetermined set is a monotone “staircase/rectangle” `R = {i>=i0, j<=j0}` of size `a'b' <= |D| = r`, and all other pairs in `D` are resolved by transitivity. The remaining task is exactly merging the `a'`-suffix of `X` with the `b'`-prefix of `Y` (a monotone boundary), of minimax cost `M(a',b') <= a'+b'-1`. So `F(P) <= F(B)+M(a',b')`. [deduction]
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
