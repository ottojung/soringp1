# Results, barriers and evidence status

[Archive home](README.md) · [Longer synthesis](SYNTHESIS.md) · [Open questions](OPEN-QUESTIONS.md) · [Corrections](CORRECTIONS.md) · [Complete catalogue](catalog/README.md)

This register is a reading guide, not an assertion that all archived claims
have been proved. Every row distinguishes its mathematical scope from its
evidence. Historical independent reviews are identified as such; archival
integration is not a fresh Lean kernel replay or peer review.

**Notation:** `A_n` is the n-element antichain; `S(n)=F(A_n)`.
`F(P)` is the optimal remaining worst-case comparison count from a poset
`P`; `e(P)` counts its linear extensions; `L(P)=ceil(log2 e(P))`;
`D(P)=F(P)-L(P)`. The root decision problem has unary input length
`N=n+k+1`. See the [precise model](../docs/problem.md).

## Established repository baseline

| ID | Claim | Evidence and scope |
|---|---|---|
| K01 | Comparison-tree model, existence and attainment, information bound, monotonicity, elementary upper bound, minimax correspondence | Existing Lean kernel theorems; [inventory](../docs/kernel-results.md) |
| K02 | S(0..6) = 0, 0, 1, 3, 5, 7, 10 | Existing Lean kernel theorems; [inventory](../docs/kernel-results.md) |
| A01 | Exact partial-order DP in time 2^O(n²) | Paper/algorithm argument; [upper bound](../docs/upper-bound.md) |
| A02 | Unary threshold in PSPACE; binary threshold in EXPSPACE | Paper/algorithm argument; [certificate and class barriers](../docs/research-certificates-barriers.md) |
| A03 | Transcript-only exact threshold DFS: 2^O(N log N) time, O(N log N) work bits; unary numeric evaluation: 2^O(n log² n) time, O(n log² n) bits | Paper proof and implementation; [budgeted DFS](../docs/research-budgeted-dfs.md) |
| A04 | Sound information and symmetry pruning | [Budget pruning](../docs/research-budget-pruning.md); no general asymptotic exponent gain established |
| B01 | Sparse unary threshold language: many-one NP-hardness implies P=NP; no many-one EXPTIME-hardness | [Hardness boundaries](../docs/research-hardness-boundaries.md), [encoding consequences](../docs/research-encoding-consequences.md) |
| B02 | Huge winning frontier, even at exact optimum on the constructed family | Paper theorem, about explicit enumeration of **all** such states; [construction and scope](../docs/research-winning-frontier-barrier.md) |
| B03 | Explicit optimal binary comparison tree has n! reachable leaves | Elementary counting, not a lower bound for succinct certificates; [framed certificates](../docs/research-framed-certificate-frontier.md) |
| C01 | Sound permutation-framed DAG verifier and polynomial-size merge-sort/rank-envelope constructions | [Certificate grammar and proofs](../docs/research-framed-certificate-frontier.md); exact-optimal all-n completeness remains open |
| C02 | FO(TC) fixed-variable evaluation and checked strategy-program examples | [FO(TC) strategy notes](../docs/research-fo-tc-strategy-programs.md), [split schemas](../docs/research-fo-tc-split-schema.md), [publication record](../docs/research-fotc-publication-record.md), [full board thread](board/JTsW4AnxTLzN18IBQibXea-fervor/README.md) |
| S01 | Ordinal-sum exactness; orientation and parallel decomposition investigations | [Series decomposition](../docs/research-series-decomposition.md), [orientation modules](../docs/research-orientation-modules.md), [parallel duality](../docs/research-parallel-duality.md) |
| S02 | One-ply information lower bound, structural merge-factor lower bounds, finite strict witnesses | [One-ply obstruction](../docs/research-one-ply-obstruction.md), [structural lower bounds](../docs/research-structural-lower-bounds.md) |
| S03 | Necessary realizability window; sufficiency fails in small cases | [Archived realization note](../notes/research-realizability-window.md), [exact reset investigation](../docs/research-exact-reset-realizability.md) |
| L01 | Known exact S(n) values through 22; S(12)=30 versus L(A_12)=29; sublinear optimal surplus in the cited literature | [Literature and source caveats](../docs/literature.md), [asymptotic note](../docs/research-sergeev-asymptotic.md) |

## Substantive late research preserved in the archive

These results were reported and in many cases independently checked during the
original project. Read the exact linked report for its assumptions.

| ID | Finding | Evidence / limit |
|---|---|---|
| P01 | Same e=32 and M1 deck, different minimax costs 5 and 6 on seven elements | [Independent witness](board/301/page-001.md?plain=1#L195); arbitrary posets, not forced root states |
| P02 | Ordinal repetition amplifies the M1-cospectral minimax gap without bound | [Referee](board/301/page-001.md?plain=1#L758); direct square check 10 vs 12, all-k deduction uses ordinal additivity |
| P03 | Exhaustive 16,999-class n=8 census has two mixed-F M1 keys and no mixed-F M2 keys | [Independent census](board/301/page-001.md?plain=1#L614); n=9 census reported but not rerun by final referee |
| P04 | Immediate child-e score can tie optimal and suboptimal comparisons | [Referee and correction](board/301/page-001.md?plain=1#L58); deeper extension counts distinguish the n=6 witnesses |
| P05 | M2 separates the known M1 collision; a depth-2 completeness question remains | [Independent review](board/301/page-001.md?plain=1#L421), [ordinal-lift review](board/301/page-001.md?plain=1#L776); higher-depth preservation not fully established |
| D01 | A fully F-synchronous optimal subtree exists iff e(P)=2^F(P) | [Independent paper proof](board/301/page-002.md?plain=1#L1231); impossible at A_n for n>=3 |
| D02 | For every comparison, harder child H satisfies D(P)-D(H)<=1 | [Independent refinement](board/301/page-001.md?plain=1#L543); D may rise, and this bound does not cover the light child |
| D03 | A defect-free root with e(P)>3·2^(L(P)-2) has two defect-free children at any optimal comparison | [Historical proof](board/301/page-001.md?plain=1#L3), [new scope correction](CORRECTIONS.md#recursive-g-completeness); recursive g conclusion only for minimal counterexample argument |
| D04 | Information-tight A_6 can reach a positive-defect state at depth five with F=5 | [Independent counterexample](board/301/page-002.md?plain=1#L329); existential defect-free tree is a different question |
| D05 | Ford–Johnson at n=11 has a defect-positive state with e=31,185 and F=16 | [Independent witness](board/301/page-002.md?plain=1#L885); does not rule out another height-26 tree |
| D06 | For FF_n (two disjoint 2-chains), F(FF_n)>=S(n)-2 | [Independent proof](board/301/page-003.md?plain=1#L155); defect at least root defect |
| D07 | Second comparison need not use two free keys in every optimal strategy | [Independent n=7 counterexample](board/301/page-004.md?plain=1#L1021); no all-n forced-prefix normal form |
| D08 | Ordinal sums separate rounding surplus and uncertified prime-defect mass | [Identity and witnesses](board/301/page-002.md?plain=1#L277); sound but incomplete lower bound, no general optimal-root transfer |
| D09 | Enriched per-block certificate incomplete already at A_12 (29 vs 30) | [Referee](board/301/page-002.md?plain=1#L329); not a lower bound against all certificate schemes |
| D10 | Chain-installation information threshold log2(4/3) at 2-to-3 chain extension | [Independent derivation](board/301/page-001.md?plain=1#L110); information viability is not exact minimax viability |
| C03 | ABC local-certificate closure fails on some optimally reachable n=8 and n=9 states | [Original experiment and data](quarantine/antichain-abc/README.md), [report](quarantine/antichain-abc/post.md); existence of some all-certified optimal tree not refuted |
| C04 | Explicit polynomial-sized full-tree blocks require Omega(N/log N) alternation blocks | [Independent proof](board/301/page-002.md?plain=1#L932); only this explicit-block representation |
| C05 | Polynomial-size exact-optimal policy circuits would imply unary threshold in Sigma_2^p | [Conditional argument](board/301/page-002.md?plain=1#L1026); circuit existence open |
| E01 | Entropy accounting bounds expected number of fixed-biased comparisons; almost all leaves have sublinear such counts under sublinear optimal surplus | [Independent derivation](board/301/page-002.md?plain=1#L261); not a worst-case-path guarantee |
| E02 | Integer sequence a_n=o(n) is P-recursive iff eventually periodic | [Historical independent paper review](board/301/page-001.md?plain=1#L336); application to D(A_n) conditional on sublinear surplus; neither periodicity nor nonperiodicity proved |

## Evidence conventions

- **Kernel-checked:** a theorem in the existing Lean library, not an agent
  statement that Lean passed.
- **Paper proof / deduction:** a mathematical argument with explicit
  assumptions; historical reviews are recorded but do not replace reading it.
- **Independently reproduced finite computation:** a second implementation
  checked a witness or a specified census; never extrapolate it to all n.
- **Conditional / conjecture / open:** the antecedent, claimed completeness,
  or generalization is still unresolved.
- **Refuted / corrected:** read the narrower surviving statement and the
  original failed argument. See [corrections](CORRECTIONS.md).
- **Workflow labels** such as investigated, blocked, clearexit, or succeeded
  are not mathematical evidence.

This is a selected register of the principal findings. The [complete thematic
catalogue](catalog/README.md) includes all 750 recorded research directions;
the [board catalogue](catalog/board/README.md) includes all archived messages,
including many smaller results not repeated here.
