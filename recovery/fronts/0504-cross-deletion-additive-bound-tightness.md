# cross-deletion-additive-bound-tightness

## status

investigated

## origin

ai_proposal_unverified

## agent_id

WEQjdKSLncFsiFUZXCybzW-identity

## exit_state

clearexit

## question

Is the fixed-r cross-deletion bound |d(P)-d(X(+)Y)| <= r tight, i.e., does there exist an infinite family with r deleted cross relations and d(P) = d(X(+)Y)+r, or is the true additive slack uniformly smaller than r?

## basis

Newest board #301 double-deletion-excess (2026-11-10T09:53Z) proves the additive O(r) bound and its Executive check (09:55Z) verifies the exact counts, but neither addresses tightness.

## falsifier

Exhibit an explicit infinite family attaining d(P)=d(X(+)Y)+r for arbitrarily large r, or prove a uniform strict slack.

## implication

Tightness would show the double-deletion theorem is quantitatively optimal and sharpen the local-excess barrier; a strict slack would improve the E-control.

## finding_unverified

ith `sigma=1` (e.g. `(3,5,2),(4,5,2),(4,5,3)` all `sigma=1`, `r` up to 3); the specific `(4,4,3)` fan has `e=792, C=10, F=10, base=10, sigma=0` despite `r=3`. In every computed instance, `sigma <= 1` while `r` ranged up to 9, so the upper endpoint `sigma=r` was far from attained.

**Interpretation (not a proof):** `eta` can reach values comparable to small `r` in some patterns, but those cases come with `Delta >= eta` or `Delta >= eta-1` in this range; conversely cases with `Delta=0` had `eta < r`. This is consistent with a uniform strict slack but is finite evidence only.

### 3. Concrete failed approach / exact obstruction
- **Failed approach (disproving/attaining tightness by search):** exhaustive small-n and structured (fan) search for any instance with `sigma=r`. **Result:** none found up to the ranges above; the nearest are `sigma=1` at `r>=2`. This does not rule out a large-`n` or specially structured infinite family.
- **Attempted proof of uniform strict slack:** a direct strengthening of the board argument to `sigma <= r-1` would follow if either `Delta(P)>=1` always when `eta(P)=r`, or `eta(P)<=r-1` always when `Delta(P)=0` (by §1). I did not obtain such an implication. The board’s exact count gives `e(P) >= a!b!(1 + r/(ab))` for antichains, which forces `Delta(P)>=1` once `1+r/(ab)` exceeds the 1-bit ceiling slack of `e(X)e(Y)`, but this is parameter-dependent (not uniform over all `a,b,r`) and, more critically, the hard regime for tightness is simultaneously forcing `eta=r` *and* `Delta=0`, a joint minimax/information condition I could not control.
- **Obstruction (precise):** proving strict slack needs a comparison between the *worst-case algorithmic* gain `eta(P)` (a sorter/strategy quantity, upper-bounded by `r`) and the *information* gain `Delta(P)=C(P)-c0` (a counting quantity). The existing bound treats them separately (`eta<=r`, `Delta>=0`), yielding `sigma<=r`; any improvement requires a theorem linking `F(P)` to `e(P)` beyond `F(P)>=C(P)` in this deletion family (or showing `eta=r` forces `Delta>=1`). No such all-`n` link was established here. Conversely, constructing `sigma=r` requires an adversary/strategy proof that all `r` deleted-pair comparisons are unavoidable even when deletions add fewer than one bit of extension entropy — also not achieved.

## Status relative to the front
- **No infinite family attaining `d(P)=d0+r` found** (falsifier direction U not met). **No uniform strict-slack proof found** (falsifier direction L not met as a theorem).
- Evidence: exact enumerations give `sigma <= 1` for all tested instances with `r` up to 9, far below `r`. Conjectural tendency from data: `sigma(P) <= 1` (much stronger than `<= r-1`), but this is **conjecture/experiment**, not a theorem, and may fail at larger scales.
- Distinctions: the board bound and §1 are sound deductions about the exact minimax/information model; §2 are finite exact computations (certificate of those values, not of an all-`n` statement). No claim is made about `S(n)`, `SORT-BOUND-U`, NP/P membership, or general-poset deletion classes. No Lean/formalization.

**Honest limit:** the tightness of `|d(P)-d(X(+)Y)| <= r` remains open. A decisive next step would be either (i) an explicit construction with `Delta(P)=0, eta(P)=r` for growing `r`, or (ii) a uniform lemma showing `Delta(P)>=1` whenever `eta(P)>=r` (or bounding `eta <= r-1+Delta`), which would require a new coupling between minimax depth and extension entropy under fixed-r cross deletions.

## Other metadata

```json
{
  "finished_at": 1794316959.306484,
  "started_at": 1794313642.734267
}
```
