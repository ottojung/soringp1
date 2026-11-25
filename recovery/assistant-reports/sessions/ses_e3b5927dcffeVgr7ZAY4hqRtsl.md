# antonina-jmYAJMcaX7Jp0wwor6HRdY-chairs

Session: ses_e3b5927dcffeVgr7ZAY4hqRtsl
Workspace: /home/lubko/soring-fronts/sidon-verify-20261110
Created: 1794300631135; updated: 1794300947271

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 135 (msg_1c4ab649e001RZ9W9AdeaO1bqt)

**Verification complete and posted to #301** as `Viche Executive referee` (`antonina board comment --id 301 ...`, RC=0). Independent implementation in `/tmp/opencode/sidonref/sidon_verify.py` (no prior scripts reused; no repo/Lean/PR changes).

**[definition]** Sidon circulant poset, `D={0,1,3}` in `Z_q`: minima `A_j=j`, maxima `B_i=q+i`, `B_i>A_j` iff `(i-j) mod q ∈ D`. `D(x,y)=e(P+x<y)-e(P+y<x)=2*e(P+x<y)-e(P)`. **[deduction]** Translation `τ_t` (within-part +t mod q) is an automorphism, so `D(τ_t x,τ_t y)=D(x,y)`; verified by canonical reps (first element → index 0): 36 orbits × 11 = 396, covering all ordered incomparable pairs.

**[experiment] Methods:** (A) height-2 `(S,r)` bitmask DP over minima subsets / placed enabled maxima; (B) general linear-extension subset DP over all `2q` elements, `f(mask)=∑ f(mask\{v})` over valid maxima-in-mask `v`.

| Item | Verdict | Evidence |
|---|---|---|
| q=11 `e(P)=16174936626710400` | **CONFIRMED** | A and B both `16174936626710400`. |
| q=11 `D!=0` for all ordered incomparable pairs (no balanced pair) | **CONFIRMED** | 396/396 pairs via 36 symmetry reps; 36 subset-DP computations, `zero_pairs_count=0`. |
| q=11 min-min sign pattern `D_1<0, D_d>0 (2≤d≤5), D_d<0 (6≤d≤9), D_{10}>0` | **CONFIRMED (direction convention)** | For `(A_0,A_d)`, `D_fwd=e(P+A_0<A_d)-e(P+A_d<A_0)` = `d=1:+336253135680, 2:-290526834240, 3:-341986924800, 4:-32193339840, 5:-336721250880, 6:+336721250880, 7:+32193339840, 8:+341986924800, 9:+290526834240, 10:-336253135680`. So `D_rev(d)=-D_fwd` has signs `(-,+,+,+,+,-,-,-,-,+)`, matching stated pattern; claim’s `D_d` corresponds to `D_rev`. |
| q=13 `e(P)=764257252943441836800` | **CONFIRMED** | Method A gives `764257252943441836800` (exact). |
| q=13 all-pairs scan, q=17 e/scan, q=19 | **INCONCLUSIVE** | Not recomputed (resources/time); no q=13 subset-DP cross-check or pair scan. |

**Commands:** `cd /tmp/opencode/sidonref && python3 sidon_verify.py` (q=11 full), plus ad-hoc q=13/q=11 min-min prints via `python3 - <<'PY' ... PY` using the same module. Worktree left clean.
