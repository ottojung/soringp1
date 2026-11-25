# cospectral-difference-ordinal-propagation-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

IoC5GAQISgKJy4hs1sOXJ3-freshness

## exit_state

clearexit

## question

Board #301 records an n=7 pair of posets P,Q with e(P)=e(Q)=32 and identical one-step child e-multiset M1=(4,4,14,14,16,16,16,16,16,16,18,18,28,28) but F(P)=5 and F(Q)=6, together with 45360 labelled n=7 posets having two one-step children of equal e but different F. For every such (e,M1)-cospectral, F-different pair, do the ordinal sums P + A_m and Q + A_m with an m-element antichain placed above all elements, and likewise the disjoint unions P disjoint A_m and Q disjoint A_m, remain (e,M1)-cospectral with different F for every m >= 0, or does the F-gap necessarily collapse or the e-deck split at some finite m?

## basis

Board #301 19:31Z and 20:45Z results independently confirm the n=7 cospectral pair and the equal-e-different-F phenomenon; docs/research-orientation-modules.md and docs/research-series-decomposition.md study ordinal-sum composition; the 731-entry ledger has no cospectral-propagation front (cospectral appears only in reachable-depth-two-profile-f-completeness-alln, a different M2 question).

## falsifier

Exhibit one n=7 cospectral F-different pair P,Q and a concrete m for which P+A_m and Q+A_m either cease to share the same e and M1 or acquire equal minimax values; a single explicit finite computation refutes the universal all-m propagation claim.

## implication

If the F-difference propagates through ordinal sums with antichains, the small board witnesses seed infinite families of invariant incompleteness at every larger size, strengthening the barrier against any fixed-depth unannotated-profile certificate; this is general-poset structure only, soundness does not become completeness, and no complexity placement for SORT-BOUND-U follows without a reduction.

## finding_unverified

universal claim is false — but only for disjoint unions

I attacked the front's all‑m propagation claim on the exact n=7 board pair
`P succ=(0x3e,0x0c,0,0,0x04,0x08,0x3e)`, `Q succ=(0x3e,0x0c,0,0,0x0c,0x04,0x1e)` (`e=32`, `M1` equal, `F=5` vs `6`). I built a from‑scratch engine (downset‑DP `e`, memoised minimax `F`, child enumeration for `M1`) in Python plus two independently written C++ runs, and validated it against the board values and `F(A_k)=S(k)` for `k=2..5`.

**Ordinal sums `P⊕A_m` (antichain on top) — claim SURVIVES, and is a theorem.** For every `m≥0`:
- `e=32·m!` for both;
- `M1` identical: P‑internal children contribute `m!·M1(P)=m!·M1(Q)`, A_m‑internal children contribute `e(P)·m!/2=e(Q)·m!/2` (multiplicity `m(m−1)`);
- by the repository's ordinal‑sum additivity (`docs/research-series-decomposition.md` Thm 1) plus `F(A_m)=S(m)`, `F(P⊕A_m)=5+S(m)` and `F(Q⊕A_m)=6+S(m)` — gap exactly 1.

Computed `m=0..3`: `F=5/6, 5/6, 6/7, 8/9`, `M1` equal throughout. So ordinal sums **do** seed an infinite family of `(e,M1)`‑cospectral, F‑different general posets at every size `7+m`.

**Disjoint unions `P⊔A_m` — claim REFUTED by explicit finite computation.**
- `m=0`: cospectral, `F=5/6`.
- `m=1`: `e=256` equal but **M1 decks differ** (brute‑force permutation count): P's cross‑child multiset `(48,48,52,52,122,122,124,132,134,134,204,204,208,208)` vs Q's `(46,46,54,54,128×6,202,202,210,210)` — the e‑deck splits, though `F=8/9` still.
- `m=2`: `e=2304` equal, `M1` splits, and **`F(P⊔A₂)=F(Q⊔A₂)=12`** — the F‑gap **collapses to 0**. Since `2¹¹<2304<2¹²`, `⌈log₂2304⌉=12` is a rigorous lower bound, and both attain it (two C++ runs, ~1.18 M memo states each).

**Exact obstruction [deduction].** `M1` records only one‑step child e‑values. In `P⊕A_m` no cross pair is incomparable, so every child factors through the *shared* invariants `(e(P),M1(P))` and `m` — cospectrality is forced. In `P⊔A_m` the cross pairs `(p,a)` are incomparable, and `e(P⊔A+p<a)` depends on `p`'s rank distribution in a uniform random linear extension of `P`, which `(e,M1)` does **not** determine; P and Q differ there. At `m=2` the merge slack makes the information bound tight, absorbing Q's extra +1 difficulty.

## Honest limits
- **General‑poset structure only.** There is no reduction from the antichain root `A_n`, so **nothing transfers to `S(n)` or `SORT-BOUND-U`**: no class placement, no barrier for the unary language. This is exactly the family the 20:45Z disposition declined to keep commissioning for lack of an `S(n)` bridge.
- **Soundness ≠ completeness.** Board Finding 3 (child `(e,F)`‑deck determines F for `n≤7`) is about soundness *given child F‑values*; the open `M_t` line is about recovering F from descendant extension counts. My result concerns **robustness of the `(e,M1)` equivalence under composition**, not completeness of any certificate. Disjoint sums do **not** yield infinite F‑incompleteness (gap collapses at `m=2`); only ordinal sums do.
- **Reachability untested.** I did not establish that either composed family lies on a k‑safe optimal‑play path from `A_{7+m}` (cf. Lemma D, where the F=6 mate was unreachable), so even the ordinal infinite family is not shown to bear on optimal sorting.

## Side effects
No repository, Lean, test, CI or ledger changes; worktree clean on `billy-dev` at `6a96398`. Scratch only under `/tmp/opencode/cospectral_front`. I posted the full result to board #301 at 21:22Z under the front's slug. `S(n)` and `SORT-BOUND-U` remain open.

## Other metadata

```json
{
  "finished_at": 1795469128.423375,
  "started_at": 1795468014.2821221
}
```
