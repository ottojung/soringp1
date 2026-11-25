# antonina-YGls1hMjad5SJru6hPDsiz-hack

Session: ses_e3d183480ffeyIx0SHXrnaMK1I
Workspace: /home/lubko/soring-fronts/height-two-abc-witness-existence
Created: 1794271333457; updated: 1794274350444

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 16 (msg_1c2e7df43001NReJilEsCGFw4P)

I'll start by inspecting the current state: working directory, Git status, and existing durable records, before doing anything external.

## Output 787 (msg_1c315a81b001wDQPLgTNL05420)

## Recovery and state

- Host `billy-dev`; worktree clean at `6a96398`; no repository or Lean changes.
- I checked the board before acting. The 00:24Z `abc-certificate-checking-complexity` post is the distinct **supplied-witness verification** front; the 01:03Z `recursive-abc-exact-height-completeness` post is also distinct. No prior post existed for `height-two-abc-witness-existence`.
- The interrupted turn’s `/tmp` scratch was wiped by the server restart. I reconstructed the verifier and the structural search, reran them, and posted **once** to board #301 at `2026-11-10T01:32:12.421Z` (`sha256:c2JBBAe4...`). I did not repeat any earlier external effect.

## Main finding

For height-two posets, split into minima `A` and maxima `B`. The slave formulas are:
- minimal `x,y`: `slave(x,y)=|U(x)\U(y)|`;
- maximal `x,y`: the dual with `N`;
- mixed nonincident `x,y`: `slave(x,y)=|U(x)|+|N(y)|`, `slave(y,x)=0`.

A **bilateral** pair has at most one slave in both orientations and implies condition A without counting.

**Exact threshold at 12.** Exhaustive enumeration of all bipartite matrices with `a+b≤11` shows:

> Every height-two non-chain poset of order at most 11 has a bilateral pair, hence a condition-A witness with no extension counting.

At order 12 this fails. Two explicit counterexamples (minima `m0..m5`, maxima `M0..M5`; `rows[i]` is the bitmask of minima below `M_i`):

1. **No bilateral pair:**  
   `rows = 41,3,48,29,26,12`  
   string `12:02c004800a000e4007000140000000000000000000000000`  
   `e(P)=1,464,880`; 50 incomparable pairs; every pair has at least 2 slaves in one orientation. It is nevertheless B-certified: `(0,4),(1,5),(6,10),(7,8)` are exactly half-balanced.

2. **No A or B pair at all:**  
   `rows = 62,40,45,52,25,51`  
   string `12:0d000840034005c00e400bc0000000000000000000000000`  
   `e(P)=1,033,128`; 41 ordered pairs have at most one slave, all with `D=2e(P+xy)-e(P)<0` (largest `-29,376`), and no pair has `D=0`.  
   Only C works, via `(x,y,z)=(0,1,7)`:
   ```
   e(P+0<1+1<7) = 454,032
   max{e(P+1<0), e(P+7<1)} = max{463,908, 131,976} = 463,908
   e(P)/2 = 516,564
   ```

So the standard structural/bilateral screen is **sound but incomplete** on height two, and the pair conditions A/B are incomplete too. Any correct algorithm must handle the balanced-triple condition.

## Complexity reading

- The existence problem is in `P^{#P}`: query exact `e(P)`, all `O(n²)` pair counts and `O(n³)` triple counts, then check A/B/C.
- Counting linear extensions of height-two posets is #P-complete (Dittmer–Pak, arXiv:1802.06312), but **#P-hardness of counting does not imply hardness of existence**. P2 is a direct example where all pair tests fail but a triple succeeds.
- Simple padding reductions are blocked by the scaling invariance already recorded in the 00:24Z post: ordinal sums and disjoint unions multiply `e` and every `D` by the same positive factor.
- I did **not** prove polynomial-time decidability, NP-hardness, or #P-hardness.

## Soundness vs completeness, and the `S(n)` implication

A/B/C are sufficient conditions for the Gold Partition Conjecture, not known complete. They are not certificates for `F(P)≤k` or `S(n)≤k`. Therefore:
- a polynomial decider for A/B/C existence would not automatically give a GPC certificate **search** (no search-to-decision reduction is established);
- even full height-two A/B/C universality would not place `SORT-BOUND-U` in P or NP;
- the front’s stated implication to exact unary `S(n)` complexity is invalid.

## Honest limits

The surviving all-n statement is the conjecture:

> Every finite height-two non-chain poset has at least one A/B/C witness.

It is consistent with Gupta’s exhaustive order-14 census (zero open), all random tests through order 16, and the order-11 bilateral threshold. If true, it would prove GPC for height two, a class not in the published GPC list, and make the decision trivial. I did not prove it. The decisive next steps are a proof of height-two A/B/C universality, a height-two open poset at order ≥15, or a hardness construction surviving the scaling invariance.

Artifacts: `/tmp/opencode/h2abc/verify.py` and `/tmp/opencode/h2abc/far_search.go`.
