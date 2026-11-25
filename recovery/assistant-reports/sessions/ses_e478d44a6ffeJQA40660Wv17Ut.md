# antonina-ZWU29KdQ6lQClbTKho97PY-brimmed

Session: ses_e478d44a6ffeJQA40660Wv17Ut
Workspace: /home/lubko/soring-fronts/exec-lemmaA-core-20261108
Created: 1794095889288; updated: 1794101596456

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1b872c0fa001PP9Ap5jhr189y0)

I'll start by reading the required docs and understanding the existing infrastructure.

## Output 23 (msg_1b872c9a4001CsWzncOmrDaxXu)

Now let me examine the existing scripts and census code for reuse.

## Output 38 (msg_1b872d4ab001v5Wb5rI51ZvHGG)

Prior scratch exists for this exact task. Let me inspect it and the census implementation.

## Output 114 (msg_1b8739c50001bnedT5YT2xp0v9)

Prior scratch used an extension-cap sweep and stopped at n=8. I'll build a cleaner exact DP over all unlabeled posets, which avoids exponential extension-set minimax. Let me benchmark it.

## Output 140 (msg_1b8749865001fFGZKddlE6qoGW)

Fast. Let me run n=7 and n=8.

## Output 151 (msg_1b87654de001ptDlOoqdRj6teQ)

n=8 complete in 73s with exact m (max m=16=S(8)). Now run n=9 with richer diagnostics.

## Output 179 (msg_1b8769d3a001jE0xwVruZRNrGI)

While n=9 runs, let me independently validate the DP's `add_rel`/minimax against extension sets on small posets.

## Output 225 (msg_1b87cd063001pdGeSh1aryqdq6)

Let me analyze which restricted comparison types achieve the bound, on n≤8 (runs alongside the n=9 job).

## Output 252 (msg_1b87f50de0015V1482B8aGWE8e)

n≤8 shows zero violations, many tight cases (deficit 0). Let me characterize the tight cases while n=9 finishes.

## Output 498 (msg_1b8930017001ReZWlCMdQiEP2W)

n=9 is complete: **no counterexample** (deficit distribution 0:7626, 1:166392, 2:9204; max m=19=S(9)). Now I'll persist exact m and directly test `e(P) ≥ F_{m+2}` on all n≤9.

## Output 519 (msg_1b8936432001sBApV8SCg7V4j2)

While the e-pass runs, let me test whether the *same* balancing comparison that works in A can be lifted to P.

## Output 680 (msg_1b89dd651001omvnEcpdLn9nv0)

While n=9 runs, let me verify the staircase upper-half witness `W_11` (e=144, m=10) for the T(9) upper bound, using backtracking over only the 144 extensions.

## Output 718 (msg_1b89eff73001JIquWAQEFmTNmN)

The slot-count is simple: `R = (# elements incomparable to x) + 1`. Let me test the conjectured lower bound `g ≥ ⌈log₂R⌉−1`.

## Output 774 (msg_1b8af8a1b001fCJYvTdgp7nyii)

n=9 full pass complete: **0 Lemma-A violations, 0 e-inequality violations**. Now the n=9 structural checks.

## Output 915 (msg_1b8bd000a001L2GtpUk4FyEX0d)

Important: the stronger x-comparison sublemma **fails for 8 instances at n=9** (Lemma A itself still holds). That changes the exact unresolved case. Let me test the correct inside-A lifting lemma at n=9.

## Output 983 (msg_1b8c715410016aSbLNdqRgVupP)

The harness restart wiped `/tmp/opencode`. The completed n=9 results are preserved in this conversation; I'll reconstruct the scripts and hashes.

## Output 1047 (msg_1b8c8d502001V14Rqhf1yKQoVK)

All key scripts reconstructed byte-identically (hashes match). I'll persist the captured results before composing the report.

## Output 1058 (msg_1b8c9418a001jwsQSchh5IKDUt)

**Lemma A through n=9: no counterexample, exact reduction, one unresolved lifting lemma**

Work was scratch-only (`/tmp/opencode`); no repo, main, or board changes.

**Method.** I computed exact `m` and `d(P)=max_{a||b} min(m(P+a<b),m(P+b<a))` by a global DP over *all* unlabeled posets: enumerate classes by adjoining a maximal element above every ideal (counts `1,2,5,16,63,318,2045,16999,183231` match), then process by decreasing relation count using `m(P)=1+min_{a||b} max(...)`. No extension-set minimax is used in the main run. Validation: all 405 classes on `n<=6` match brute-force extension-set minimax; 8 random `n=9` classes match the repo's `sortable` minimax; `m(antichain n)=1,3,5,7,10,13,16,19=S(n)` for `n<=9`.

**1. Falsification result.** Exhaustive cutoff: **all 183,231 isomorphism classes with `n<=9`**, exact `m` for every state. **There is no counterexample.** For the 183,222 classes with `m>=2`, `d(P)>=m(P)-2` always. Deficit `d-(m-2)` at `n=9`: `0: 7,626`, `1: 166,392`, `2: 9,204`; no negative value. At `n=8`: `0: 962`, `1: 15,216`, `2: 813`. A counterexample would have deficit `<= -1`; none exists through `n=9`. (Consequently no relation matrix or child-depth table for a counterexample is available.)

**2. Strongest obstruction.** The minimum deficit is exactly **0**, first at `n=3`, `up=(0,4,0)`, `m=2`, `d=0`. Tightness is generic, not confined to chains or ordinal sums: at `n=8`, 657 of 962 tight posets are cores (`m=5..12`); at `n=9`, **5,857 of 7,626 are cores** (`m=4..14`). So the bound is sharp on a broad family; there is no sporadic near-counterexample.

Extremal-element comparisons are insufficient. At `n=8` the core `up=(192,224,224,176,128,128,0,0)` has `m=10`, `d=9`, but every comparison involving a maximal element has a child of depth 7 (needed 8); the witness pair is interior. Max–max or min–min comparisons alone give deficit `-1` at `n=5..8` (e.g. `n=5`, `up=(0,24,24,16,0)`, `m=4`, best max–max child min is `1=m-3`).

A stronger obstruction appears at `n=9`: even when the removable maximal element `x` has `g=m(P)-m(P-x)=3`, the `x`-comparisons can all fail. There are **8 such `(P,x)` instances** at `n=9`; example `up=(256,128,448,448,352,256,256,0,0)`, `m=13`, `m(P-x)=10`, `x=7`: the best `(x,y)` has minimum child depth `10=m-3`. Lemma A nevertheless survives through a comparison inside `P-x`. This is exactly the “one child is nearly solved” case.

**3. Proof status.** The following reductions are rigorous:
- Deleting universal elements preserves `(e,m)`, so it suffices to treat cores; comparisons lift back.
- For ordinal sums, `m` is additive. If a factor has `m=1`, it is a 2-antichain after core reduction and either comparison of its two elements gives children of depth `m(P)-1`. If both factors have `m>=2`, induction inside one factor gives children of depth `m(P)-2`. Chains (`m=0`) are ignored. So it suffices to treat ordinal-indecomposable cores.
- Let `P` be such a core, `x` maximal with `A=P-x` a core (Lemma 2 of the core note). If `m(A)>=m(P)-2`, comparing `x` with any `y||x` gives children containing `A`, hence depth `>=m(A)>=m(P)-2`. Therefore **a counterexample must have `g=m(P)-m(A)>=3` for every such `x`**.

The exact remaining step is the inside-`A` lifting lemma:

> **L.** For every core `P`, maximal `x` with `A=P-x` a core, some comparison `(u,v)` inside `A` has both `P`-children of depth `>=m(P)-2`.

`L` implies Lemma A immediately (choose `x` by Lemma 2), together with the reductions above. `L` is trivial when `g=0` (an `A`-witness lifts), and was verified for **all cores through `n=8`** (gap counts `0:1991, 1:10675, 2:13804, 3:6557`; zero failures). The `n=9` run of `L` was interrupted by the harness restart; Lemma A itself was already checked directly at `n=9`. The natural stronger version using `x`-comparisons is **false** (the 8 instances above), so a proof cannot avoid the inside-`A` analysis.

The slot obstruction is precise. `I={a:a<x}` is a proper ideal, `U=A\I` are the elements incomparable with `x`, and `R=|U|+1`. Sorting `A` then binary-searching the insertion slot gives `g<=ceil(log2 R)`. A median `y` leaves at least about `R/2` slots on each side, but when `|U|` is even one branch can lose two bits. At `n=9` there are **127** `g>=3` instances with `|U|` even and `g=ceil(log2 R)` where no pure-slot comparison certifies both children; all 127 are tight (`d=m-2`). Example: `m=11`, `m(P-x)=8`, `|U|=4`, `d=10`, best child min `9=m-2`, `up=(384,384,480,496,352,320,0,0,0)`. The missing bit must come from coupling with `A`; that coupling is the unproved ingredient.

**4. Implications.** The direct check `e(P)>=F_{m+2}` has **zero violations on all classes `n<=9`**. At `n=9`, the minima by `m` are `3,5,8,13,21,34,55` for `m=2..8` (equality at staircases), then `126,259,548,...` for `m=9,10,11`; at `n=8` the `m=7` minimum is `34=F_9`. This supports the inequality but proves nothing for all `n`.

If Lemma A holds, the Fibonacci induction is immediate: an optimal comparison has one child of depth `m-1` (since every comparison has `max child >=m-1`), and Lemma A supplies the other `>=m-2`; hence `e>=F_{m+1}+F_m=F_{m+2}`, and therefore `T(r)>=F_{r+3}-1` for all `r`.

For `T(9)=143`: I independently verified `W_11` has `e=144=F_12`, `m=10` (and `W_12`: `e=233`, `m=11`), so the **upper half `T(9)<=143` is now solid**. Lemma A would also give the lower half, hence `T(9)=143`. Without it, `T(9)` is **not** established here: the lower half needs every core with `e<=143` to have `m<=9`, and such cores may have up to 143 elements. The merged census covers only `e<=88`. The `n<=9` slice is consistent: at `n=9` the minimum `e` with `m=10` is `259>143`, so no size-`<=9` poset meets `e<=143, m>=10`; this neither falsifies nor proves the general inequality.

**Resources.** `n<=9` exhaustive: 183,231 classes; 439.4 s enumeration + 1,385.6 s solve = **30.4 min**; peak RSS **1.58 GB** (DP-only run 1.41 GB). `n=10` not attempted: projected ~20x time and >10 GB, outside the bound. Scripts: `lemmaA_dp.py` `54af91f5…`, `lemmaA_full.py` `d1092ff8…`, `lemmaA_B_n9.py` `8915d63d…`, `lemmaA_L_n9.py` `5838a045…`, `verify_staircases.py` `efca8758…`, `validate_dp.py` `1b379259…` (full SHA-256 in `/tmp/opencode/lemmaA_RESULTS.md`). No theorem is claimed from finite data.
