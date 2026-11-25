# Information, balance, entropy and defect

[Catalogue home](../README.md) · [Evidence status guide](../../RESULTS.md)

Status is the original workflow label, not mathematical proof. Linked messages may contain corrections or rejected claims.

## dyadic-excess-sequence-structure

For Delta(n) = S(n) minus ceil(log2(n!)), using the published exact and lower values for all n where they are known, does Delta behave as O(1) within each dyadic interval \[2^m, 2^(m+1)) and does it stay nondecreasing in n across all known values n &lt;= 22 and 28?

**investigated** · [Full research report](../../fronts/0019-dyadic-excess-sequence-structure.md)
Source manifests: [soring-fronts_dyadic-excess-sequence-structure](../../workspaces/manifests/soring-fronts_dyadic-excess-sequence-structure.json)

## info-bound-tightness-infinite

Is the set {n &gt;= 0 : S(n) == ceil(log2(n!))} infinite, and if not does it have a known largest element or is there a proof it is cofinite?

**investigated** · [Full research report](../../fronts/0025-info-bound-tightness-infinite.md)
Historical reported excerpt: **Conclusion:** Cannot prove finiteness or cofinite equality from the materials reviewed. The most plausible candidate (Fredman’s additive lower bound) needs precise primary-source form + effective constants to be falsifiable as an “all-n obstruction”; absent that, the honest answer is that the set…
Additional board mentions: 3 (use front lookup for exact links)
Source manifests: [soring-fronts_info-bound-tightness-infinite](../../workspaces/manifests/soring-fronts_info-bound-tightness-infinite.json)

## dyadic-slack-monotonicity

Is the excess function D(n)=S(n)-ceil(log2 n!) eventually monotonic on each dyadic interval \[2^p, 2^(p+1)) for all large p, or does it exhibit all-n oscillation across intervals beyond known small drops?

**investigated** · [Full research report](../../fronts/0040-dyadic-slack-monotonicity.md)
Source manifests: [soring-fronts_dyadic-slack-monotonicity](../../workspaces/manifests/soring-fronts_dyadic-slack-monotonicity.json)

## adversarial-entropy-rate-obstruction

Let H_b be the Shannon entropy of the adversary's outcome distribution at comparison nodes b on some strategy for A_n (uniform random linear extension / adversarial worst case for information). Is there an all-n constant ε&gt;0 with E\[∑ H_b / D\] &lt;= 1-ε over optimal-height strategies of any all-n family (adversarial entropy rate bounded below 1), or can some all-n strategy family keep adversarial entropy rate approaching 1 on all paths while achieving height S(n)?

**investigated** · [Full research report](../../fronts/0060-adversarial-entropy-rate-obstruction.md)
Historical reported excerpt: **Finding (mathematical):** Disprove the “bounded below 1” (gap ε&gt;0, rate ≤ 1−ε) claim for exact optimal-height strategies on the permutation family. Since $S(n)=(1+o(1))\log_2(n!)$ (Fredman/Ford–Johnson/Kahn–Saks improvements), for any strategy $T_n$ with $D(T_n)=S(n)$ and $H_i=h(p_i)\le 1$ we hav…
Board: [2026-10-31 message](../../board/301/page-040.md?plain=1#L300)
Source manifests: [soring-fronts_adversarial-entropy-rate-obstruction](../../workspaces/manifests/soring-fronts_adversarial-entropy-rate-obstruction.json)

## information-gap-monotonicity

Let g(n)=S(n)-⌈log2(n!)⌉ &gt;= 0 be the information-theoretic gap. Is g(n) non-decreasing in n for all sufficiently large n, or does it drop below values at smaller n infinitely often despite Sergeev's o(n) asymptotics?

**investigated** · [Full research report](../../fronts/0065-information-gap-monotonicity.md)
Source manifests: [soring-fronts_information-gap-monotonicity](../../workspaces/manifests/soring-fronts_information-gap-monotonicity.json)

## gap-monotonicity-alln

Is the sorting-number information gap g(n)=S(n)-⌈log2(n!)⌉ non-decreasing in n for all sufficiently large n, or does it decrease infinitely often despite S(n)=log2(n!)+o(n)?

**investigated** · [Full research report](../../fronts/0066-gap-monotonicity-alln.md)
Historical reported excerpt: **Mathematical finding (primary-sources only):**
Source manifests: [soring-fronts_gap-monotonicity-alln](../../workspaces/manifests/soring-fronts_gap-monotonicity-alln.json)

## graph-entropy-rate-monotonicity

Is the Kahn-Kim/Kahn-Saks comparison entropy rate for states on optimal paths non-increasing in some normalized sense for all n &gt;= some N, and would monotonicity of the entropy-driven strategy force a uniform asymptotic form of S(n) or a computable certificate?

**investigated** · [Full research report](../../fronts/0074-graph-entropy-rate-monotonicity.md)
Source manifests: [soring-fronts_graph-entropy-rate-monotonicity](../../workspaces/manifests/soring-fronts_graph-entropy-rate-monotonicity.json)

## gap-monotonicity-eventual

Let g(n)=S(n)-⌈log2(n!)⌉ &gt;= 0 be the information-theoretic gap. Is there some N0 such that for all n &gt;= N0, g(n+1) &gt;= g(n) (eventual monotonicity of the gap), or does the gap decrease infinitely often for large n?

**investigated** · [Full research report](../../fronts/0095-gap-monotonicity-eventual.md)
Source manifests: [soring-fronts_gap-monotonicity-eventual](../../workspaces/manifests/soring-fronts_gap-monotonicity-eventual.json)

## fredman-additive-slack-barrier

For all sufficiently large n, does Fredman's lower bound force S(n) &gt;= ceil(log2(n!)) + f(n) with f(n) &gt;= omega(log log n) that is realizable by a uniform all-n obstruction, or can some comparison model absorb the additive term without extra comparisons?

**investigated** · [Full research report](../../fronts/0098-fredman-additive-slack-barrier.md)
Historical reported excerpt: **FINDING (mathematical, paper-first):** The claim is false as stated.
Source manifests: [soring-fronts_fredman-additive-slack-barrier](../../workspaces/manifests/soring-fronts_fredman-additive-slack-barrier.json)

## exact-optimal-slack-barrier

Does the o(n) information-theoretic slack d(n)=S(n)-ceil(log2 n!) in Sergeev's bound force the exact-optimal winning frontier to be exponentially smaller than at the information budget for all large n?

**investigated** · [Full research report](../../fronts/0126-exact-optimal-slack-barrier.md)
Board: [2026-11-01 message](../../board/301/page-037.md?plain=1#L207) · [2026-11-01 message](../../board/301/page-037.md?plain=1#L247) · [2026-11-01 message](../../board/301/page-037.md?plain=1#L271) · [2026-11-01 message](../../board/301/page-037.md?plain=1#L279) · [2026-11-01 message](../../board/301/page-037.md?plain=1#L287) (9 total; use search for all)
Source manifests: [soring-fronts_exact-optimal-slack-barrier](../../workspaces/manifests/soring-fronts_exact-optimal-slack-barrier.json)

## entropy-loss-floor-optimal

For any sound framed certificate of height exactly S(n) (within o(n) of the information bound log2(n!)), is there an all-n forced lower bound on total forgetting loss lambda_b summing to Omega(n / something) or directly forcing either superpolynomial size or height &gt; S(n)?

**investigated** · [Full research report](../../fronts/0156-entropy-loss-floor-optimal.md)
Source manifests: [soring-fronts_entropy-loss-floor-optimal](../../workspaces/manifests/soring-fronts_entropy-loss-floor-optimal.json)

## kraft-realizability-language-complexity

For unary $N=n+k+1$, is the language $L={1^N mid exists$ a full binary comparison tree of height $le k$ sorting $n}$ (Kraft-admissible height-bounded comparison trees) in $P$ uniformly in all $n,k$ given only $N$?

**investigated** · [Full research report](../../fronts/0157-kraft-realizability-language-complexity.md)
Board: [2026-11-01 message](../../board/301/page-033.md?plain=1#L136) · [2026-11-01 message](../../board/301/page-033.md?plain=1#L144) · [2026-11-01 message](../../board/301/page-033.md?plain=1#L152)
Source manifests: [soring-fronts_kraft-realizability-language-complexity](../../workspaces/manifests/soring-fronts_kraft-realizability-language-complexity.json)

## comparison-basis-information-obstruction

For all sufficiently large n where n! is not a power of two, is there an all-n combinatorial obstruction (beyond simple integer rounding of log2(n!)) forcing S(n) &gt;= ceil(log2(n!)) + 1 due to the comparison (pairwise test) basis constraints on the state graph, independent of specific poset structure counts?

**investigated** · [Full research report](../../fronts/0164-comparison-basis-information-obstruction.md)
Historical reported excerpt: **Finding (disproof):** The all-n claim is false. Known exact values give S(20)=⌈log2 20!⌉ and S(21)=⌈log2 21!⌉ with 20!,21! not powers of two (docs/research-certificates-barriers.md:125), so no universal obstruction forces +1 for all large n in that class—tightness recurs irregularly.
Source manifests: [soring-fronts_comparison-basis-information-obstruction](../../workspaces/manifests/soring-fronts_comparison-basis-information-obstruction.json)

## root-split-divisibility-allposets

For which infinite families of posets {F_n} rooted at the n-antichain is there NO exact comparison tree partitioning Ext(F_n) into leaf classes of equal size e(F'_n) up to framing, due to the integer divisibility of branch extension counts induced by every possible first comparison and its recursive splits, beyond the known odd antichain-to-star case?

**investigated** · [Full research report](../../fronts/0175-root-split-divisibility-allposets.md)
Source manifests: [soring-fronts_root-split-divisibility-allposets](../../workspaces/manifests/soring-fronts_root-split-divisibility-allposets.json)

## comparison-split-modulus-obstruction

Is there an infinite sequence of posets {P_n} on n elements with the property that for every prime power p^e exactly dividing some comparison-split size ratio from P_n, the recursive comparison-split structure forces a contradiction for exact partitioning into any fixed-form leaf classes, creating an all-n obstruction independent of the global n!/product arithmetic?

**investigated** · [Full research report](../../fronts/0178-comparison-split-modulus-obstruction.md)
Source manifests: [soring-fronts_comparison-split-modulus-obstruction](../../workspaces/manifests/soring-fronts_comparison-split-modulus-obstruction.json)

## information-feasibility-coupling-bound

Define for each partial order P the pair (I(P), r(P)) where I(P)=log2(e(P)) is the information content and r(P) is a minimal 'comparison-feasibility' rank (e.g. the forcing rank from some root-to-leaf constraints); show that for all P reachable on any correct sorting path from A_n there is an all-n inequality I(P)+F(P) &gt;= C(n) + f(n,P) that is not implied by Kraft alone and forces a gap for some infinite family.

**investigated** · [Full research report](../../fronts/0182-information-feasibility-coupling-bound.md)
Historical reported excerpt: **Mathematical finding (disproof attempt result):** The inequality claimed in the FRONT is false in general. For any fixed $n\ge4$ and any correct sorting strategy, take a state $P$ with exactly $e(P)=2$ linear extensions one comparison before completion (reachable on every correct path): $I(P)=\lo…
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_information-feasibility-coupling-bound](../../workspaces/manifests/soring-fronts_information-feasibility-coupling-bound.json)

## minimum-split-imbalance-root

For the n-element antichain at root, let beta(n)=min_{optimal strategies T} max_{outcomes of first comparison} (max(F(T_lt),F(T_gt))/(F(T_root)-1)) be the worst-case relative imbalance of the best most balanced optimal first split; is there an all-n proof that beta(n) -&gt; 1 as n-&gt;infty or is inf_n beta(n) &lt; 1 bounded away from 1?

**investigated** · [Full research report](../../fronts/0191-minimum-split-imbalance-root.md)
Board: [2026-11-02 message](../../board/301/page-032.md?plain=1#L363) · [2026-11-02 message](../../board/301/page-032.md?plain=1#L371) · [2026-11-02 message](../../board/301/page-032.md?plain=1#L379) · [2026-11-02 message](../../board/301/page-032.md?plain=1#L387) · [2026-11-02 message](../../board/301/page-032.md?plain=1#L395) (37 total; use search for all)
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_minimum-split-imbalance-root](../../workspaces/manifests/soring-fronts_minimum-split-imbalance-root.json)

## comparison-split-kraft-obstruction

Establish an all-n necessary condition on comparison trees stronger than Kraft/log2(n!) arising from the fact that a pairwise comparison produces a partition into two order ideals in a way not realizable by arbitrary prefix codes, and see if it forces a uniform super-logarithmic gap for some infinite n family relevant to exact S(n).

**blocked** · [Full research report](../../fronts/0199-comparison-split-kraft-obstruction.md)
Board: [2026-11-02 message](../../board/301/page-031.md?plain=1#L163) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L171) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L179) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L204) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L212) (19 total; use search for all)
Additional board mentions: 4 (use front lookup for exact links)
Assistant reports: [ses_e105def02ffeUjWnj4cLjcoV4p](../../assistant-reports/sessions/ses_e105def02ffeUjWnj4cLjcoV4p.md)
Original task commissions: [f37c62834b2b](../../followup/task-commissions/objects/f37c62834b2b98be5c612de7fe94eea340b627993a3cc88a6018e1dfdd0135f3.txt)
Mixed-session reports: [27ee65221e7e](../../followup/mixed-reports/objects/27ee65221e7eb263042318d26dd734e81aa31e632b8a1797488a03cfc0b5c518.txt) · [3f4f3b35bd60](../../followup/mixed-reports/objects/3f4f3b35bd60c6ae609978b0defad0175656dba30d24fc1d535e45018c3c99e6.txt)
Source manifests: [soring-fronts_comparison-split-kraft-obstruction](../../workspaces/manifests/soring-fronts_comparison-split-kraft-obstruction.json)

## divisible-split-obstruction-alln

For the n-element antichain, is there an infinite family of n where every comparison strategy that first achieves the information-theoretic split ratio consistent with some depth-S(n) path produces a subsequent state partition whose linear-extension counts are not all powers-of-two compatible, forcing total height &gt; ceil(log2(n!)) for those n?

**investigated** · [Full research report](../../fronts/0201-divisible-split-obstruction-alln.md)
Historical reported excerpt: **Conclusion:** I find no evidence supporting the claim as stated. The natural generalization of exact-reset (transition divisibility) does not lift cleanly to a universal all-n obstruction for achieving minimum height C(n) on the antichain; tight cases recur (20,21), obstructions appear sporadical…
Board: [2026-11-02 message](../../board/301/page-031.md?plain=1#L204) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L212)
Source manifests: [soring-fronts_divisible-split-obstruction-alln](../../workspaces/manifests/soring-fronts_divisible-split-obstruction-alln.json)

## entropy-balance-tightness-alln

Does the Kahn-Saks graph-entropy / balanced-comparison paradigm force S(n) &gt;= log2(n!) + c*n / something, or can one construct an all-n family of comparison strategies beating entropy-balance predictions to approach log2(n!) closer than o(n) in a structured way?

**investigated** · [Full research report](../../fronts/0202-entropy-balance-tightness-alln.md)
Historical reported excerpt: **Finding:** The Kahn–Saks/Kahn–Kim "balanced comparison / graph entropy" paradigm is **enabling, not forcing**. Kahn–Saks guarantees some balanced comparison exists per poset state (used to build $O(\log e(P))$ strategies); it does not imply that *every* correct sorting strategy has linear entropy…
Source manifests: [soring-fronts_entropy-balance-tightness-alln](../../workspaces/manifests/soring-fronts_entropy-balance-tightness-alln.json)

## costpath-split-imbalance-exact

For every n and every comparison strategy achieving S(n) on the antichain, let r_d be the worst (over all states at depth d on that strategy, along some cost-optimal path from root) ratio e(P)/2^(S(n)-d) of remaining linear extensions to the information-theoretic budget for depth d; is sup_{n, optimal strategies} sup_{d &lt;= S(n)-2} (max(r_d, 1/r_d)) bounded above by some constant c &lt; infinity or can it be Omega(n) for infinitely many n?

**investigated** · [Full research report](../../fronts/0209-costpath-split-imbalance-exact.md)
Historical reported excerpt: **Mathematical finding (all-n, the front `costpath-split-imbalance-exact`):**
Board: [2026-11-03 message](../../board/301/page-030.md?plain=1#L51) · [2026-11-03 message](../../board/301/page-030.md?plain=1#L59) · [2026-11-03 message](../../board/301/page-030.md?plain=1#L77) · [2026-11-03 message](../../board/301/page-030.md?plain=1#L85) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L292) (10 total; use search for all)
Source manifests: [soring-fronts_costpath-split-imbalance-exact](../../workspaces/manifests/soring-fronts_costpath-split-imbalance-exact.json)

## excess-boundedness-alln

Is the information-theoretic excess D(n)=S(n)-⌈log2(n!)⌉ bounded above by some constant C for all sufficiently large n, or does sup_n D(n)=+∞ under the exact adaptive comparison model?

**blocked** · [Full research report](../../fronts/0212-excess-boundedness-alln.md)
Board: [2026-11-03 message](../../board/301/page-030.md?plain=1#L133) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L388) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L396) · [2026-11-03 message](../../board/301/page-031.md?plain=1#L404) · [2026-11-03 message](../../board/301/page-031.md?plain=1#L412) (21 total; use search for all)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e105dee03ffeqrWKFarl2dWOPr](../../assistant-reports/sessions/ses_e105dee03ffeqrWKFarl2dWOPr.md)
Original task commissions: [25ab90a6d089](../../followup/task-commissions/objects/25ab90a6d089d43defee3b3d39a75abd0675d1e92c3e644a50c40e934c2aa6da.txt)
Mixed-session reports: [27ee65221e7e](../../followup/mixed-reports/objects/27ee65221e7eb263042318d26dd734e81aa31e632b8a1797488a03cfc0b5c518.txt) · [3f4f3b35bd60](../../followup/mixed-reports/objects/3f4f3b35bd60c6ae609978b0defad0175656dba30d24fc1d535e45018c3c99e6.txt)
Source manifests: [soring-fronts_excess-boundedness-alln](../../workspaces/manifests/soring-fronts_excess-boundedness-alln.json)

## information-tightness-infinitely-often

Does there exist an infinite sequence of integers n_i -&gt; ∞ with S(n_i) = ⌈log2(n_i!)⌉ (the information bound is exactly achieved), or is equality achieved only finitely many times?

**blocked** · [Full research report](../../fronts/0213-information-tightness-infinitely-often.md)
Board: [2026-11-03 message](../../board/301/page-030.md?plain=1#L133) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L388) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L396) · [2026-11-03 message](../../board/301/page-031.md?plain=1#L404) · [2026-11-03 message](../../board/301/page-031.md?plain=1#L412) (21 total; use search for all)
Additional board mentions: 2 (use front lookup for exact links)
Source manifests: [soring-fronts_information-tightness-infinitely-often](../../workspaces/manifests/soring-fronts_information-tightness-infinitely-often.json)

## branch-mass-telescoping-o-n-excess

Is there an all-n inequality showing that any comparison tree with height &lt;= log2(n!)+o(n) must incur aggregate forgetting/branch-mass telescoping loss &gt;= Omega(n / f(n)) for some slowly growing f, forcing excess &gt;= Omega(n/polylog n)?

**investigated** · [Full research report](../../fronts/0215-branch-mass-telescoping-o-n-excess.md)
Historical reported excerpt: **Mathematical finding (disproof of the front claim):**
Additional board mentions: 2 (use front lookup for exact links)
Source manifests: [soring-fronts_branch-mass-telescoping-o-n-excess](../../workspaces/manifests/soring-fronts_branch-mass-telescoping-o-n-excess.json)

## admissible-split-closure-obstruction

Let A be the closure under transitive composition of all (e(P'),e(P'')) split ratios achievable by a single comparison in some poset P reachable from the antichain. For all sufficiently large n, does every factorization of n! into factors from A that forms a full comparison tree of height &lt;= C(n)+o(n) violate some global consistency condition (not local Kraft/divisibility) forcing excess &gt;= Omega(n/polylog n)?

**investigated** · [Full research report](../../fronts/0217-admissible-split-closure-obstruction.md)
Historical reported excerpt: **Finding (disproof of the front):**
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_admissible-split-closure-obstruction](../../workspaces/manifests/soring-fronts_admissible-split-closure-obstruction.json)

## comparison-graph-entropy-obstruction-alln

For the n-element antichain, is there an all-n family where Körner graph-entropy lower bounds for the comparison identification problem strictly exceed ceil(log2(n!)) by Ω(n) for every deterministic adaptive comparison strategy, and can such a gap be realized without appealing to the potential-function obstructions already ruled out by Sergeev?

**investigated** · [Full research report](../../fronts/0221-comparison-graph-entropy-obstruction-alln.md)
Board: [2026-11-03 message](../../board/301/page-029.md?plain=1#L3) · [2026-11-03 message](../../board/301/page-030.md?plain=1#L429)
Source manifests: [soring-fronts_comparison-graph-entropy-obstruction-alln](../../workspaces/manifests/soring-fronts_comparison-graph-entropy-obstruction-alln.json)

## split-critical-poset-exact-reset

Are there posets P other than the antichain such that every nontrivial comparison from P induces a balanced extension split relative to the gcd of all possible leaf class sizes for any exact reset, and does the class of such split-critical posets form an infinite all-n family with universal exact-reset impossibility?

**investigated** · [Full research report](../../fronts/0225-split-critical-poset-exact-reset.md)
Historical reported excerpt: **Mathematical finding (disproof of the proposed hypothesis):**
Source manifests: [soring-fronts_split-critical-poset-exact-reset](../../workspaces/manifests/soring-fronts_split-critical-poset-exact-reset.json)

## recursive-mass-divisibility-tight-height

For the n-element antichain, define M(T) as the multiset of outcome masses at nodes of a framed comparison tree T; is there an all-n obstruction forcing that for every T with height = ceil(log2 n!) there is some node v and some allowed framed leaf class size e(F') with e(F') not dividing the number of extensions passing through v consistent with any sound framing below v?

**investigated** · [Full research report](../../fronts/0226-recursive-mass-divisibility-tight-height.md)
Source manifests: [soring-fronts_recursive-mass-divisibility-tight-height](../../workspaces/manifests/soring-fronts_recursive-mass-divisibility-tight-height.json)

## excess-constant-bounded-alln

Is there an absolute constant C with S(n) &lt;= ceil(log2(n!)) + C for all n &gt;= 1, or does the excess D(n)=S(n)-ceil(log2(n!)) grow without bound as n-&gt;∞?

**investigated** · [Full research report](../../fronts/0227-excess-constant-bounded-alln.md)
Additional board mentions: 2 (use front lookup for exact links)
Source manifests: [soring-fronts_excess-constant-bounded-alln](../../workspaces/manifests/soring-fronts_excess-constant-bounded-alln.json)

## sergeev-effective-excess-bound

Extract an effective finite version of Sergeev's S(n) - log2(n!) = o(n) bound with explicit constants/functions for large n to narrow the threshold window that exact algorithms must search.

**investigated** · [Full research report](../../fronts/0243-sergeev-effective-excess-bound.md)
Historical reported excerpt: **Finding (paper-level obstruction, no repo/Lean changes):**
Board: [2026-11-23 review](../../board/301/page-003.md?plain=1#L929)
Source manifests: [soring-fronts_sergeev-effective-excess-bound](../../workspaces/manifests/soring-fronts_sergeev-effective-excess-bound.json)

## pigeonhole-split-exponent-shrink

Find a non-enumerative recurrence for the minimax value F(P) exploiting structure (symmetry/decomposition/orbits) giving 2^(O(n log n)) or better uniform time bound avoiding full winning-frontier enumeration.

**investigated** · [Full research report](../../fronts/0245-pigeonhole-split-exponent-shrink.md)
Historical reported excerpt: ### Outcome
Source manifests: [soring-fronts_pigeonhole-split-exponent-shrink](../../workspaces/manifests/soring-fronts_pigeonhole-split-exponent-shrink.json)

## poset-entropy-information-theoretic-lb

Derive an information-theoretic lower bound for S(n) using the actual structure of reachable posets (not just n! permutations) and see if it explains the n=12 gap or forces gaps infinitely often.

**investigated** · [Full research report](../../fronts/0247-poset-entropy-information-theoretic-lb.md)
Historical reported excerpt: **Mathematical finding (report): for every n, the adversarial-ply structural information bound provably collapses to the trivial bound at the antichain root.**
Board: [2026-11-03 message](../../board/301/page-029.md?plain=1#L167)
Source manifests: [soring-fronts_poset-entropy-information-theoretic-lb](../../workspaces/manifests/soring-fronts_poset-entropy-information-theoretic-lb.json)

## comparison-split-algebraic-invariant

Find an algebraic/combinatorial invariant preserved in some form across optimal splits that explains S(n) &gt; ceil(log2(n!)) for specific n (starting from n=12).

**investigated** · [Full research report](../../fronts/0249-comparison-split-algebraic-invariant.md)
Historical reported excerpt: **Mathematical finding (no proof):** there is no known algebraic/combinatorial invariant preserved across optimal splits that explains $S(n)&gt;\lceil\log_2 n!\rceil$ starting at $n=12$; the obstruction is global routing/structural, not a scalar monotone invariant.
Additional board mentions: 3 (use front lookup for exact links)
Source manifests: [soring-fronts_comparison-split-algebraic-invariant](../../workspaces/manifests/soring-fronts_comparison-split-algebraic-invariant.json)

## cheap-zone-excess-unboundedness

Let g(n)=S(n)-ceil(log2 n!) be excess. Given that Delta(m)=ceil(log2 m!)-ceil(log2 (m-1)!) drops below M(m)=ceil(log2 m) exactly in 'cheap' zones (non-power-of-two with fractional parts summing &lt; 1) and excess can rise only there with g(n)-g(n-1)&lt;=1, is g(n) unbounded as n-&gt;∞ or is it bounded for all large n?

**investigated** · [Full research report](../../fronts/0259-cheap-zone-excess-unboundedness.md)
Board: [2026-11-04 message](../../board/301/page-029.md?plain=1#L273) · [2026-11-04 message](../../board/301/page-029.md?plain=1#L281) · [2026-11-04 message](../../board/301/page-029.md?plain=1#L289)
Source manifests: [soring-fronts_cheap-zone-excess-unboundedness](../../workspaces/manifests/soring-fronts_cheap-zone-excess-unboundedness.json)

## ply-kraft-comparison-constraint

For the antichain A_n and any binary comparison tree of height k sorting all permutations, let f_v be the branching/feasibility constraint from the partial-order comparability (not just leaf count); does the comparison-tree validity force a strict all-n strengthening of Kraft/leaf-sum inequalities beyond n! &lt;= 2^k that is independent of linear-extension counts in some regimes?

**investigated** · [Full research report](../../fronts/0260-ply-kraft-comparison-constraint.md)
Historical reported excerpt: **Finding (paper deduction, no repo/Lean changes):** For a binary comparison tree that sorts all permutations from antichain A_n, Kraft inequality \(\sum_{\text{leaves}} 2^{-d_\ell}\le 1\) (hence \(n!\le 2^k\)) is necessary for *any* prefix code regardless of test type. Comparison-validity restrict…
Board: [2026-11-04 message](../../board/301/page-029.md?plain=1#L343) · [2026-11-04 message](../../board/301/page-029.md?plain=1#L351) · [2026-11-04 message](../../board/301/page-029.md?plain=1#L367) · [2026-11-04 message](../../board/301/page-029.md?plain=1#L375) · [2026-11-04 message](../../board/301/page-029.md?plain=1#L391) (7 total; use search for all)
Source manifests: [soring-fronts_ply-kraft-comparison-constraint](../../workspaces/manifests/soring-fronts_ply-kraft-comparison-constraint.json)

## adversary-mixed-strategy-gap

For the minimax game G(n,k), let V(n,k) be the value (sorter wins?). Is there any all-n case where every pure adversary strategy that is 'extension-count balanced' is strictly worse for the adversary than some other pure strategy, but more directly: can the adversary force a win at budget k = S(n)-1 for all large n by using a non-uniform-in-some-way strategy that exploits the comparison-validity constraints in a manner not captured by the information bound or by any known poset invariant, while every strategy following a simple heuristic (e.g. always balance linear extensions) fails?

**investigated** · [Full research report](../../fronts/0263-adversary-mixed-strategy-gap.md)
Board: [2026-11-04 message](../../board/301/page-029.md?plain=1#L375) · [2026-11-04 message](../../board/301/page-029.md?plain=1#L391) · [2026-11-04 message](../../board/301/page-029.md?plain=1#L399) · [2026-11-04 message](../../board/301/page-029.md?plain=1#L415) · [2026-11-04 message](../../board/301/page-029.md?plain=1#L463) (7 total; use search for all)
Source manifests: [soring-fronts_adversary-mixed-strategy-gap](../../workspaces/manifests/soring-fronts_adversary-mixed-strategy-gap.json)

## local-gap-global-complexity-barrier

Since the merge family shows local gaps m(P)-ceil(log2 e(P)) are unbounded as n grows, is there an all-n structural obstruction (not depending on circuit lower bounds) implying that any uniform algorithm must track such unbounded local gaps, forcing SORT-BOUND-U not in DTIME(2^(n^c)) for some c&lt;1 or creating a barrier to subexponential uniform evaluation?

**investigated** · [Full research report](../../fronts/0269-local-gap-global-complexity-barrier.md)
Source manifests: [soring-fronts_local-gap-global-complexity-barrier](../../workspaces/manifests/soring-fronts_local-gap-global-complexity-barrier.json)

## entropy-loss-join-obstruction

For sound framed certificates achieving height k=S(n)=C(n)+o(n), is there an all-n obstruction (from the exponentially large winning frontier) forcing any polynomial-size forgetful DAG to have expected total entropy loss Omega(n) under the auxiliary random walk across some all-n family, making the telescoping identity E\[D\]-log2(n!) &lt;= k-log2(n!) = o(n) incompatible with polynomial size?

**investigated** · [Full research report](../../fronts/0271-entropy-loss-join-obstruction.md)
Historical reported excerpt: **Conclusion:** I could not construct a counterexample, nor did I find a clean proof of the obstruction from the stated evidence. The strongest honest position is: **the obstruction is plausible as a compression bottleneck but not demonstrated**. The decisive test is exactly the falsifier - either …
Source manifests: [soring-fronts_entropy-loss-join-obstruction](../../workspaces/manifests/soring-fronts_entropy-loss-join-obstruction.json)

## optimal-path-prefix-invariant-gap

For all sufficiently large n, does there exist a family of reachable poset states on some minimax-optimal path from the antichain with identical extension-count profiles and identical information bounds yet requiring different worst-case comparison budgets to complete to a total order under optimal play?

**investigated** · [Full research report](../../fronts/0278-optimal-path-prefix-invariant-gap.md)
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_optimal-path-prefix-invariant-gap](../../workspaces/manifests/soring-fronts_optimal-path-prefix-invariant-gap.json)

## pairwise-vs-arbitrary-test-gap

Does the restriction to pairwise comparisons (the sorting test class) create an all-n exponential gap between the height of an optimal adaptive tree for pairwise tests and the information-theoretic/abstract test lower bound in a sense that is not explained by the standard log2(n!) bound, or is the pairwise restriction exactly captured by the minimax game with no additional all-n complexity barrier beyond the known bounds?

**investigated** · [Full research report](../../fronts/0285-pairwise-vs-arbitrary-test-gap.md)
Source manifests: [soring-fronts_pairwise-vs-arbitrary-test-gap](../../workspaces/manifests/soring-fronts_pairwise-vs-arbitrary-test-gap.json)

## comparison-split-kraft-tightness

For the all-n family of comparison-split trees induced by optimal play, is the Kraft sum inequality S = sum 2^{-depth(leaf)} &lt;= 1 always realizable with equality for some infinite subfamily while being strictly subunit on others, and does any infinite family force S &lt;= 1 - c/n^p for fixed c&gt;0,p&gt;=0 preventing a known info-tight construction?

**investigated** · [Full research report](../../fronts/0286-comparison-split-kraft-tightness.md)
Historical reported excerpt: **Conclusion:** The Kraft-sum formulation as stated does not correctly identify the obstruction for comparison-split trees induced by optimal play. The productive direction is split-realizability (e.g. divisibility/modular constraints on $(e(P+uv),e(P+vu))$) rather than the prefix-code Kraft inequa…
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_comparison-split-kraft-tightness](../../workspaces/manifests/soring-fronts_comparison-split-kraft-tightness.json)

## telescoped-entropy-loss-unavoidable

For any sound framed comparison DAG of height exactly S(n) that is a valid certificate for sorting n elements, is the telescoped entropy loss Σ (1 - H_b + λ_b) &gt;= Ω(n / log n) over all sufficiently large n, or can total loss be o(n / log n) uniformly?

**investigated** · [Full research report](../../fronts/0290-telescoped-entropy-loss-unavoidable.md)
Source manifests: [soring-fronts_telescoped-entropy-loss-unavoidable](../../workspaces/manifests/soring-fronts_telescoped-entropy-loss-unavoidable.json)

## information-gap-parameterized

Is the exact computation of S(n) (or deciding S(n) &lt;= k) fixed-parameter tractable when parameterized by the information-theoretic gap g(n,k)=k - ceil(log2(n!)), and can this be separated from unbounded-parameter hardness?

**investigated** · [Full research report](../../fronts/0293-information-gap-parameterized.md)
Mixed-session reports: [23157bf94e64](../../followup/mixed-reports/objects/23157bf94e6409968c979d9bab1afa7129ed22f8bf5a1d4bb42ca0e6341e932d.txt)
Source manifests: [soring-fronts_information-gap-parameterized](../../workspaces/manifests/soring-fronts_information-gap-parameterized.json)

## optimal-play-split-realizability-gap

For all sufficiently large n, is there an all-n family of comparison-split probability profiles that are information-theoretically feasible by Kraft but not realizable by any single comparison in the partial order of any state reachable on some S(n)-optimal minimax path, creating an unavoidable search-time overhead beyond the information bound?

**investigated** · [Full research report](../../fronts/0298-optimal-play-split-realizability-gap.md)
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_optimal-play-split-realizability-gap](../../workspaces/manifests/soring-fronts_optimal-play-split-realizability-gap.json)

## antichain-split-coprime-obstruction

For all integers n &gt;= 3 with gcd(n, m)=1 and some m&gt;=2, if every leaf class in an exact-reset stage from A_n must have size divisible by m but the antichain's first balanced split gives n!/2 orders, is there an infinite family of (n,m) with this coprime mismatch obstructing exact reset regardless of target poset structure?

**investigated** · [Full research report](../../fronts/0305-antichain-split-coprime-obstruction.md)
Historical reported excerpt: **Mathematical finding**
Source manifests: [soring-fronts_antichain-split-coprime-obstruction](../../workspaces/manifests/soring-fronts_antichain-split-coprime-obstruction.json)

## optimal-path-forced-e-gap-family

Is there an explicit infinite family of posets P_{n,d} reachable from A_n within S(n) comparisons along every optimal sorter strategy for those n, such that F(P_{n,d}) - ceil(log2 e(P_{n,d})) &gt;= 1 uniformly, yielding a root-forced local information gap?

**investigated** · [Full research report](../../fronts/0317-optimal-path-forced-e-gap-family.md)
Board: [2026-11-07 message](../../board/301/page-025.md?plain=1#L291)
Source manifests: [soring-fronts_optimal-path-forced-e-gap-family](../../workspaces/manifests/soring-fronts_optimal-path-forced-e-gap-family.json)

## threshold-exponent-entropy-ratio

With rho = sup over finite posets of m(P)/log2 e(P), is the universal threshold f(S(n)+1) equal to n!^{1/rho+o(1)}, and is rho strictly larger than the e=13, m=5 witness ratio 5/log2 13 approximately 1.351?

**investigated** · [Full research report](../../fronts/0322-threshold-exponent-entropy-ratio.md)
Assistant reports: [ses_e486b4c97ffeJ0waIg7zermM0U](../../assistant-reports/sessions/ses_e486b4c97ffeJ0waIg7zermM0U.md)
Original task commissions: [3150adac3b1e](../../followup/task-commissions/objects/3150adac3b1e3e9164163edc066ca83ad8aee98aaaab2c45df414f48427d73c0.txt)
Source manifests: [soring-fronts_threshold-exponent-entropy-ratio](../../workspaces/manifests/soring-fronts_threshold-exponent-entropy-ratio.json)

## excess-element-threshold-alln

Is the minimum ground-set size g(n) of a poset with e(P)&lt;=n! and m(P)&gt;S(n) equal to n+1 for every sufficiently large n, or does every such threshold witness require at least (1+epsilon)n elements?

**investigated** · [Full research report](../../fronts/0323-excess-element-threshold-alln.md)
Assistant reports: [ses_e486b499bffeXhCi8kmnfiEwPh](../../assistant-reports/sessions/ses_e486b499bffeXhCi8kmnfiEwPh.md)
Original task commissions: [78e04d7972e9](../../followup/task-commissions/objects/78e04d7972e9a1385406d9bf7274f6e7b2cae5a9d99a0387a0fc33c4f12e19e5.txt)
Source manifests: [soring-fronts_excess-element-threshold-alln](../../workspaces/manifests/soring-fronts_excess-element-threshold-alln.json)

## extension-greedy-root-gap-bound

Let H(n) be the minimum height over strategies that, from the n-element antichain, always choose a comparison minimizing the larger of the two child linear-extension counts; is S(n) - H(n) bounded by an absolute constant for every n, or does this root greedy gap grow without bound?

**investigated** · [Full research report](../../fronts/0327-extension-greedy-root-gap-bound.md)
Assistant reports: [ses_e47f2b25affeYa0VJKH3kWKXdp](../../assistant-reports/sessions/ses_e47f2b25affeYa0VJKH3kWKXdp.md)
Original task commissions: [e067ddc4a6ae](../../followup/task-commissions/objects/e067ddc4a6aecfb1bb3c2c08a1ff08b81ae747f39c94481a4812c146ecf2d402.txt)
Source manifests: [soring-fronts_extension-greedy-root-gap-bound](../../workspaces/manifests/soring-fronts_extension-greedy-root-gap-bound.json)

## optimal-fibonacci-split-alln

Does every finite poset P with minimax depth m(P) &gt;= 2 admit a minimax-optimal comparison whose worse child has depth exactly m(P)-1 and whose other child also has depth at least m(P)-2, making the board's Lemma A split realizable on a single optimal branch?

**blocked** · [Full research report](../../fronts/0329-optimal-fibonacci-split-alln.md)
Board: [2026-11-23 review](../../board/301/page-003.md?plain=1#L379) · [2026-11-18 message](../../board/301/page-014.md?plain=1#L200) · [2026-11-09 message](../../board/301/page-019.md?plain=1#L566) · [2026-11-08 message](../../board/301/page-022.md?plain=1#L97)
Additional board mentions: 18 (use front lookup for exact links)
Assistant reports: [ses_e478ca269ffer2Yp5t6557uKl7](../../assistant-reports/sessions/ses_e478ca269ffer2Yp5t6557uKl7.md) · [ses_e47383f86ffejotCleBba9p8ug](../../assistant-reports/sessions/ses_e47383f86ffejotCleBba9p8ug.md) · [ses_e19012704ffe1RfPpMp5rKJgRi](../../assistant-reports/sessions/ses_e19012704ffe1RfPpMp5rKJgRi.md) (4 total)
Original task commissions: [0ed533b50271](../../followup/task-commissions/objects/0ed533b50271218f712610613968c18f058e566cd5ed6d2ad583b40e36f6190e.txt) · [1db608b29392](../../followup/task-commissions/objects/1db608b293928595a9b5108fe55e1840d26d1f1c38910d9b57dd2f6ad8e8cb25.txt) · [aacd49b265a7](../../followup/task-commissions/objects/aacd49b265a78938f3da4648831a115670f4a33f0632a9ea468ea2c80bd8720b.txt) (4 total)
Mixed-session reports: [03dff826a1f9](../../followup/mixed-reports/objects/03dff826a1f91b78c60c65225385aaad6acb86bc4dd845f8d7f240664b0a292a.txt) · [0cbb31b940dd](../../followup/mixed-reports/objects/0cbb31b940dda1606fe503fd7452b0b37e45fa842fdaf66b12ac0949177ef978.txt) · [0fa7946b856e](../../followup/mixed-reports/objects/0fa7946b856e494b0975d90827110411d5418e6c478c988a79eebf00e3aa2491.txt) (22 total)
Source manifests: [soring-fronts_optimal-fibonacci-split-alln](../../workspaces/manifests/soring-fronts_optimal-fibonacci-split-alln.json)

## optimal-split-gpc-equivalence

Is the single-optimal-branch property - every finite poset with m(P)&gt;=2 has a minimax-optimal comparison whose child depths are m(P)-1 and at least m(P)-2 - equivalent, for all finite posets, to the Gold Partition Conjecture?

**investigated** · [Full research report](../../fronts/0348-optimal-split-gpc-equivalence.md)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e464ea60cffeh63kGcSWwljjNQ](../../assistant-reports/sessions/ses_e464ea60cffeh63kGcSWwljjNQ.md) · [ses_e464e78f9ffeDJyoCiRSdGbbDP](../../assistant-reports/sessions/ses_e464e78f9ffeDJyoCiRSdGbbDP.md)
Original task commissions: [3bcbefd31ce0](../../followup/task-commissions/objects/3bcbefd31ce02d68e5455ceea36aaf61b7d3a06af2e6a02aa2d69d0689debb05.txt) · [5a77af6f7512](../../followup/task-commissions/objects/5a77af6f7512bd7ddc0527b0f76f037b18d26d0e607172124de587334d05d227.txt)
Source manifests: [soring-fronts_optimal-split-gpc-equivalence](../../workspaces/manifests/soring-fronts_optimal-split-gpc-equivalence.json)

## eventual-information-nontightness

Is S(n) strictly larger than ceil(log2(n!)) for every n &gt;= 22, so that information-tight comparison sorting occurs at only finitely many input sizes?

**investigated** · [Full research report](../../fronts/0354-eventual-information-nontightness.md)
Historical reported excerpt: **Conclusion**
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e45852c74ffeR5033rTDtm7MUh](../../assistant-reports/sessions/ses_e45852c74ffeR5033rTDtm7MUh.md)
Original task commissions: [486409d78392](../../followup/task-commissions/objects/486409d783920027aa98fd7d2b965cf6a310dd7d370b76c0150cc577159960eb.txt)
Source manifests: [soring-fronts_eventual-information-nontightness](../../workspaces/manifests/soring-fronts_eventual-information-nontightness.json)

## s-optimal-tree-average-depth-gap

For every n, let A(n) be the minimum average number of comparisons, under the uniform distribution on the n! inputs, among all comparison trees of height exactly S(n). Is A(n) &lt;= log2(n!) + O(1), or does A(n) - log2(n!) grow without bound?

**investigated** · [Full research report](../../fronts/0363-s-optimal-tree-average-depth-gap.md)
Board: [2026-11-08 message](../../board/301/page-022.md?plain=1#L636) · [2026-11-08 message](../../board/301/page-022.md?plain=1#L658) · [2026-11-08 message](../../board/301/page-022.md?plain=1#L671) · [2026-11-08 message](../../board/301/page-022.md?plain=1#L835)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e45391042ffex8X0cfpht47Ovw](../../assistant-reports/sessions/ses_e45391042ffex8X0cfpht47Ovw.md)
Original task commissions: [5309701abd44](../../followup/task-commissions/objects/5309701abd44a6121e5265cb48c736db01f783526a2038c3d9e1ffd886ec7340.txt)
Source manifests: [soring-fronts_s-optimal-tree-average-depth-gap](../../workspaces/manifests/soring-fronts_s-optimal-tree-average-depth-gap.json)

## minimax-lp-integrality-gap-rate

Let f(n) be the value at the n-antichain of the natural minimax LP relaxation that the newest board post proves satisfies f(n)&lt;S(n) for every n&gt;=3. Is S(n)-f(n) bounded above by an absolute constant or by O(log n), or does it grow without bound?

**investigated** · [Full research report](../../fronts/0366-minimax-lp-integrality-gap-rate.md)
Board: [2026-11-08 message](../../board/301/page-022.md?plain=1#L784) · [2026-11-08 message](../../board/301/page-022.md?plain=1#L820) · [2026-11-08 message](../../board/301/page-022.md?plain=1#L835)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e4515d81dffeC3ILjftaGp11iy](../../assistant-reports/sessions/ses_e4515d81dffeC3ILjftaGp11iy.md)
Original task commissions: [ed1803f49418](../../followup/task-commissions/objects/ed1803f49418ba42b428c0980c1a5697bf292974ff3099e32d0c7b12dc0b2a5c.txt)
Source manifests: [soring-fronts_minimax-lp-integrality-gap-rate](../../workspaces/manifests/soring-fronts_minimax-lp-integrality-gap-rate.json)

## randomized-average-sorting-excess

For every n, let f(n) be the minimum expected number of comparisons of a correct comparison sort under the uniform distribution, equivalently the minimum average leaf depth over all correct trees. Is f(n)-ceil(log2 n!) bounded, or does it grow without bound?

**investigated** · [Full research report](../../fronts/0368-randomized-average-sorting-excess.md)
Board: [2026-11-08 message](../../board/301/page-022.md?plain=1#L929) · [2026-11-08 message](../../board/301/page-022.md?plain=1#L990)
Assistant reports: [ses_e44f6998effeclWtzGlxznYivP](../../assistant-reports/sessions/ses_e44f6998effeclWtzGlxznYivP.md)
Original task commissions: [da94e0a68fc3](../../followup/task-commissions/objects/da94e0a68fc3c759d3e09d8ce5ccaea7971b22713600ea02117ed7a72f67ea6d.txt)
Source manifests: [soring-fronts_randomized-average-sorting-excess](../../workspaces/manifests/soring-fronts_randomized-average-sorting-excess.json)

## logarithmic-information-excess-alln

For the exact sorting number S(n), is S(n) - ceil(log2(n!)) = O(log n) for every n, or is there an infinite family of n on which this excess is at least c log n for some fixed c &gt; 0?

**investigated** · [Full research report](../../fronts/0378-logarithmic-information-excess-alln.md)
Board: [2026-11-08 message](../../board/301/page-021.md?plain=1#L393) · [2026-11-08 message](../../board/301/page-021.md?plain=1#L424) · [2026-11-08 message](../../board/301/page-021.md?plain=1#L485)
Assistant reports: [ses_e44352856ffegrCFTE3fiOpLKt](../../assistant-reports/sessions/ses_e44352856ffegrCFTE3fiOpLKt.md)
Original task commissions: [9518663e7be3](../../followup/task-commissions/objects/9518663e7be37f0b2cbb45a70f51ccb0997af0bedc7015233102ce040f4fad65.txt)
Mixed-session reports: [a943a1a421f1](../../followup/mixed-reports/objects/a943a1a421f10487970deccb17481c2c2d38178c52a2af99ff2922c662db4e10.txt)
Source manifests: [soring-fronts_logarithmic-information-excess-alln](../../workspaces/manifests/soring-fronts_logarithmic-information-excess-alln.json)

## haeupler-heapsort-antichain-excess

When the Haeupler et al. heapsort variant (arXiv:2404.04552v4, Appendix C, as cited in the newest #301 post) is specialized to the n-element antichain, is its comparison-tree height log2(n!) + o(n) for all n, or does it collapse to an insertion/merge family with Omega(n) excess?

**investigated** · [Full research report](../../fronts/0379-haeupler-heapsort-antichain-excess.md)
Historical reported excerpt: **Finding, for the record**
Board: [2026-11-08 message](../../board/301/page-021.md?plain=1#L361) · [2026-11-08 message](../../board/301/page-021.md?plain=1#L377) · [2026-11-08 message](../../board/301/page-021.md?plain=1#L471)
Assistant reports: [ses_e4435234fffeuv1d9IVHZWB4lu](../../assistant-reports/sessions/ses_e4435234fffeuv1d9IVHZWB4lu.md)
Original task commissions: [ec862212f9d9](../../followup/task-commissions/objects/ec862212f9d9645164c07a6d254f9a3871edaedcc92134d1a8213b67e9129b4a.txt)
Mixed-session reports: [a943a1a421f1](../../followup/mixed-reports/objects/a943a1a421f10487970deccb17481c2c2d38178c52a2af99ff2922c662db4e10.txt)
Source manifests: [soring-fronts_haeupler-heapsort-antichain-excess](../../workspaces/manifests/soring-fronts_haeupler-heapsort-antichain-excess.json)

## info-tightness-set-complexity

Is the information-tightness set T = {1^n : S(n) = ceil(log2 n!)} decidable by a uniform polynomial-time algorithm, or is T as hard as exact S(n), so that even the zero-excess indicator encodes the full evaluation difficulty?

**investigated** · [Full research report](../../fronts/0383-info-tightness-set-complexity.md)
Board: [2026-11-08 message](../../board/301/page-021.md?plain=1#L536) · [2026-11-08 message](../../board/301/page-021.md?plain=1#L695)
Assistant reports: [ses_e43ddf36cfferCgIk1sLBtfm5Q](../../assistant-reports/sessions/ses_e43ddf36cfferCgIk1sLBtfm5Q.md)
Original task commissions: [51ac42a08f68](../../followup/task-commissions/objects/51ac42a08f6809982e3638bc87ff2a2539903107827f10553b2fb5eccb2de64c.txt)
Source manifests: [soring-fronts_info-tightness-set-complexity](../../workspaces/manifests/soring-fronts_info-tightness-set-complexity.json)

## fixed-pattern-defect-bound

For every fixed finite poset Q, is the defect D_Q(n)=S(n)-F(Q disjoint-union A_{n-\|Q\|}) bounded by a constant depending only on Q, rather than growing unboundedly with n?

**investigated** · [Full research report](../../fronts/0391-fixed-pattern-defect-bound.md)
Historical reported excerpt: ## Finding: the defect is bounded for every fixed pattern
Board: [2026-11-08 message](../../board/301/page-021.md?plain=1#L953)
Additional board mentions: 4 (use front lookup for exact links)
Assistant reports: [ses_e435b01b9ffev9izmV100AOo7p](../../assistant-reports/sessions/ses_e435b01b9ffev9izmV100AOo7p.md) · [ses_e434c67aaffeggt91NeSl9OLYn](../../assistant-reports/sessions/ses_e434c67aaffeggt91NeSl9OLYn.md)
Original task commissions: [2a8eb13e8442](../../followup/task-commissions/objects/2a8eb13e84421736684993f2c33ebc1dfa9fac9ba9f785c8bc29a4451e2ba3d8.txt)
Mixed-session reports: [653c6bbcdc00](../../followup/mixed-reports/objects/653c6bbcdc0073ddd54e24f077f250373789114d9df13cfcfaf36c4b5d186134.txt)
Source manifests: [soring-fronts_fixed-pattern-defect-bound](../../workspaces/manifests/soring-fronts_fixed-pattern-defect-bound.json)

## binomial-superadditivity-defect

Do all a,b satisfy S(a+b) &gt;= S(a)+S(b)+floor(log2 binomial(a+b,a))-1, a one-bit-slack strengthening of superadditivity that measures the intrinsic cost of merging two unordered blocks?

**investigated** · [Full research report](../../fronts/0392-binomial-superadditivity-defect.md)
Board: [2026-11-08 message](../../board/301/page-021.md?plain=1#L897)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e435afc06ffen4pETcZVrKClZV](../../assistant-reports/sessions/ses_e435afc06ffen4pETcZVrKClZV.md)
Original task commissions: [e85f11df7f1b](../../followup/task-commissions/objects/e85f11df7f1bd8012e2efcaa950ae5d1b787fc840d077f27bafff509a05373d8.txt)
Source manifests: [soring-fronts_binomial-superadditivity-defect](../../workspaces/manifests/soring-fronts_binomial-superadditivity-defect.json)

## single-bit-excess-dichotomy

Is the information-theoretic excess E(n)=S(n)-ceil(log_2 n!) always equal to 0 or 1 for every n, that is, is S(n) &lt;= ceil(log_2 n!)+1 for all n rather than merely S(n)=log_2(n!)+o(n)?

**investigated** · [Full research report](../../fronts/0394-single-bit-excess-dichotomy.md)
Board: [2026-11-21 message](../../board/301/page-007.md?plain=1#L159) · [2026-11-08 message](../../board/301/page-020.md?plain=1#L55) · [2026-11-08 message](../../board/301/page-020.md?plain=1#L76)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e43302ef4ffef2baIPK7RsHL5J](../../assistant-reports/sessions/ses_e43302ef4ffef2baIPK7RsHL5J.md)
Original task commissions: [db35df624a51](../../followup/task-commissions/objects/db35df624a51721f6f22e1f0ba40aa578407036557aa0c74d19108158ce2403d.txt)
Source manifests: [soring-fronts_single-bit-excess-dichotomy](../../workspaces/manifests/soring-fronts_single-bit-excess-dichotomy.json)

## bulk-insertion-information-defect

For a fixed alpha in (0,1), let P(n)=C_{floor(alpha n)} disjoint-union A_{n-floor(alpha n)} and D_alpha(n)=F(P(n))-ceil(log2(n! / floor(alpha n)!)). Is D_alpha(n) bounded by a constant depending only on alpha for all n, or unbounded along an infinite subsequence?

**investigated** · [Full research report](../../fronts/0398-bulk-insertion-information-defect.md)
Historical reported excerpt: **Outcome: the front is not resolved; it is a genuine open dichotomy. No repository or Lean changes. One board post was made (after checking there was no prior post for this front).**
Board: [2026-11-08 message](../../board/301/page-020.md?plain=1#L388) · [2026-11-08 message](../../board/301/page-020.md?plain=1#L409)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e4302cddcffezlTBGnYMA1Klcx](../../assistant-reports/sessions/ses_e4302cddcffezlTBGnYMA1Klcx.md)
Original task commissions: [8ff5c3967448](../../followup/task-commissions/objects/8ff5c3967448ba103eebff90918d01f0330f0bb56de8d3a31edcf83dd517b820.txt)
Source manifests: [soring-fronts_bulk-insertion-information-defect](../../workspaces/manifests/soring-fronts_bulk-insertion-information-defect.json)

## bounded-excess-self-reduction

Is exact S(n) polynomial-time Turing reducible to the bounded-excess predicates E(m)&lt;=d for a fixed d, where E(m)=S(m)-ceil(log2 m!) and m ranges over n together with polynomially many padded sizes?

**investigated** · [Full research report](../../fronts/0408-bounded-excess-self-reduction.md)
Board: [2026-11-09 message](../../board/301/page-019.md?plain=1#L166) · [2026-11-08 message](../../board/301/page-020.md?plain=1#L453)
Assistant reports: [ses_e4280a25bffeX0AUQI35gqyW6t](../../assistant-reports/sessions/ses_e4280a25bffeX0AUQI35gqyW6t.md)
Original task commissions: [63bf1e6ce94a](../../followup/task-commissions/objects/63bf1e6ce94a1ba2da020bc7d0ad46c80dba4549bd8d83b5507f4c4660dd0008.txt)
Mixed-session reports: [1ac266a87a6f](../../followup/mixed-reports/objects/1ac266a87a6ff9c4d01a693b3b87d7fd7bbc50c0efab284fbb175c1ac0bb0b7b.txt)
Source manifests: [soring-fronts_bounded-excess-self-reduction](../../workspaces/manifests/soring-fronts_bounded-excess-self-reduction.json)

## information-theoretic-gap-unboundedness

Does the excess E(n)=S(n)-ceil(log2 n!) grow unboundedly, or is it O(1), for all n under the fixed adaptive comparison model?

**investigated** · [Full research report](../../fronts/0417-information-theoretic-gap-unboundedness.md)
Historical reported excerpt: ## Mathematical finding
Assistant reports: [ses_e42135efaffeL7q9vpqYgimH03](../../assistant-reports/sessions/ses_e42135efaffeL7q9vpqYgimH03.md)
Original task commissions: [d6d3e9b365c4](../../followup/task-commissions/objects/d6d3e9b365c4e70077d93290db883f7857e5ed392b09dc325d2cc195792682a0.txt)
Source manifests: [soring-fronts_information-theoretic-gap-unboundedness](../../workspaces/manifests/soring-fronts_information-theoretic-gap-unboundedness.json)

## farkas-dual-completeness-vs-soundness-gap

Does every near-optimal budget k=S(n)-1 for the faithful state-expanded decision-tree LP admit a polynomial-size Farkas certificate of infeasibility, or is the exponential matching-support obstruction unavoidable for all sound-and-complete dual witnesses?

**investigated** · [Full research report](../../fronts/0420-farkas-dual-completeness-vs-soundness-gap.md)
Historical reported excerpt: ## Mathematical finding
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e41be57b4ffeMN2MhJvXY0TgTq](../../assistant-reports/sessions/ses_e41be57b4ffeMN2MhJvXY0TgTq.md)
Original task commissions: [7fa2cdb54ca9](../../followup/task-commissions/objects/7fa2cdb54ca96e85facdb070e0b0e14deb54b228dbc75389e2d36d79254d6e13.txt)
Source manifests: [soring-fronts_farkas-dual-completeness-vs-soundness-gap](../../workspaces/manifests/soring-fronts_farkas-dual-completeness-vs-soundness-gap.json)

## near-optimal-partial-sorting-gap

Let m_b(A_n) be the maximum number of permutations correctly sorted by any height-b comparison tree on the n-element antichain. Is there an absolute delta&gt;0 such that m_{S(n)-1}(A_n)&lt;=(1-delta)n! for all n, or can height-(S(n)-1) trees sort a 1-o(1) fraction of all permutations as n grows?

**investigated** · [Full research report](../../fronts/0424-near-optimal-partial-sorting-gap.md)
Board: [2026-11-09 message](../../board/301/page-020.md?plain=1#L876) · [2026-11-09 message](../../board/301/page-020.md?plain=1#L1116)
Assistant reports: [ses_e40a570adffeXh6ey51EnPxD4u](../../assistant-reports/sessions/ses_e40a570adffeXh6ey51EnPxD4u.md)
Original task commissions: [dda5c2c91a14](../../followup/task-commissions/objects/dda5c2c91a14234885886eb3a54a97da618da810f4bc2f162e77b430c4d31112.txt)
Source manifests: [soring-fronts_near-optimal-partial-sorting-gap](../../workspaces/manifests/soring-fronts_near-optimal-partial-sorting-gap.json)

## adaptive-network-size-gap

Let N(n) be the minimum number of comparators in a sorting network for n distinct keys and S(n) the exact adaptive comparison number. Is N(n)-S(n) bounded by an absolute constant for all n, or is N(n)-S(n) unbounded as n grows?

**investigated** · [Full research report](../../fronts/0425-adaptive-network-size-gap.md)
Board: [2026-11-09 message](../../board/301/page-020.md?plain=1#L929) · [2026-11-09 review](../../board/301/page-020.md?plain=1#L1011)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e40836b36ffeFHzBviWLfY31p1](../../assistant-reports/sessions/ses_e40836b36ffeFHzBviWLfY31p1.md)
Original task commissions: [1389f99bb1b5](../../followup/task-commissions/objects/1389f99bb1b50f29498156008aadfd27f05cb3571381d14552b3be619da725e8.txt)
Mixed-session reports: [ce9dc9387e61](../../followup/mixed-reports/objects/ce9dc9387e61a8e8a8b7248d059d08277c475d943fa5b216bd8ab19622ab3ee5.txt) · [ee471f4538ec](../../followup/mixed-reports/objects/ee471f4538eccda0afd92908332e862bfe6483586eed773b400520a707785612.txt)
Source manifests: [soring-fronts_adaptive-network-size-gap](../../workspaces/manifests/soring-fronts_adaptive-network-size-gap.json)

## three-chain-insertion-gap

Let F(C_m disjoint-union A_2) be the exact minimax comparison number for a sorted chain of m keys plus two isolated keys. Is F(C_m disjoint-union A_2)-ceil(log2((m+1)(m+2))) bounded by an absolute constant for all m, or does this insertion defect grow without bound?

**investigated** · [Full research report](../../fronts/0427-three-chain-insertion-gap.md)
Board: [2026-11-09 message](../../board/301/page-020.md?plain=1#L979) · [2026-11-09 message](../../board/301/page-020.md?plain=1#L1030) · [2026-11-09 review](../../board/301/page-020.md?plain=1#L1065)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e40836355ffex0DtKir2v164Ru](../../assistant-reports/sessions/ses_e40836355ffex0DtKir2v164Ru.md)
Original task commissions: [202c7b84ea15](../../followup/task-commissions/objects/202c7b84ea151cd88ed59ae32d96e80102a38b7ceac08e1f77677e345a87d69d.txt)
Mixed-session reports: [fe3fd92f3718](../../followup/mixed-reports/objects/fe3fd92f3718abfe982a506548addc1aac3dec02a5437b859ba657c65c82d092.txt)
Source manifests: [soring-fronts_three-chain-insertion-gap](../../workspaces/manifests/soring-fronts_three-chain-insertion-gap.json)

## fixed-free-block-insertion-defect

For every fixed r&gt;=1, is the fixed-free-block insertion defect D_r(m)=F(C_m disjoint-union A_r)-ceil(log2((m+r)!/m!)) at most 1 uniformly in m, or does sup_m D_r(m) grow with r?

**investigated** · [Full research report](../../fronts/0429-fixed-free-block-insertion-defect.md)
Board: [2026-11-09 message](../../board/301/page-019.md?plain=1#L247) · [2026-11-09 message](../../board/301/page-019.md?plain=1#L401)
Assistant reports: [ses_e405b740bffe6MTlKLrxIxMpiL](../../assistant-reports/sessions/ses_e405b740bffe6MTlKLrxIxMpiL.md)
Original task commissions: [93ee2a7b8cba](../../followup/task-commissions/objects/93ee2a7b8cbae0090a1dc0fe9ced6f736b68ae963227957b05191350088068fa.txt)
Mixed-session reports: [1ac266a87a6f](../../followup/mixed-reports/objects/1ac266a87a6ff9c4d01a693b3b87d7fd7bbc50c0efab284fbb175c1ac0bb0b7b.txt)
Source manifests: [soring-fronts_fixed-free-block-insertion-defect](../../workspaces/manifests/soring-fronts_fixed-free-block-insertion-defect.json)

## fixed-pattern-defect-eventual-constancy

For every fixed finite poset Q, is the defect D_Q(n)=S(n)-F(Q disjoint-union A_{n-\|Q\|}) eventually constant as n grows, or does some fixed Q produce an infinite sequence of n on which D_Q(n) changes value?

**investigated** · [Full research report](../../fronts/0436-fixed-pattern-defect-eventual-constancy.md)
Board: [2026-11-09 message](../../board/301/page-019.md?plain=1#L633)
Assistant reports: [ses_e3fb07087ffed89GuO1tGQJBGE](../../assistant-reports/sessions/ses_e3fb07087ffed89GuO1tGQJBGE.md)
Original task commissions: [8b3165f07664](../../followup/task-commissions/objects/8b3165f076647603163b5f5905fa9d68fac5ee7c47f4ac12c099af60e3681afd.txt)
Mixed-session reports: [df71c0aabb45](../../followup/mixed-reports/objects/df71c0aabb45b7d2a909e9d9991546b543692044e22e5e8d7eded8ba98854b33.txt)
Source manifests: [soring-fronts_fixed-pattern-defect-eventual-constancy](../../workspaces/manifests/soring-fronts_fixed-pattern-defect-eventual-constancy.json)

## height-two-information-excess-bound

Is F(P) - ceil(log2 e(P)) at most 1 for every finite poset P of height at most two?

**investigated** · [Full research report](../../fronts/0440-height-two-information-excess-bound.md)
Historical reported excerpt: **Result already delivered, not rerun**
Board: [2026-11-09 message](../../board/301/page-019.md?plain=1#L651) · [2026-11-09 message](../../board/301/page-019.md?plain=1#L776) · [2026-11-09 message](../../board/301/page-019.md?plain=1#L816)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e3f761a60ffe6g9F3hBvGSq3Cf](../../assistant-reports/sessions/ses_e3f761a60ffe6g9F3hBvGSq3Cf.md)
Original task commissions: [e1ba3e4c92a5](../../followup/task-commissions/objects/e1ba3e4c92a5b82b97624416c7b319fc7bcaac13e90f9bf65cf8d0c34543db8d.txt)
Mixed-session reports: [6542a7180a64](../../followup/mixed-reports/objects/6542a7180a644294e603b3ccdbee223b9752c402b8b2266120fe2640224a4206.txt) · [930849325e06](../../followup/mixed-reports/objects/930849325e0653a00c90d6795d348a1bab6c9c810bcf96341c14f678abf3eb9b.txt) · [fe716b2b27d8](../../followup/mixed-reports/objects/fe716b2b27d88a66f770e18eaa77543b784424527a7ddae17283cc8f16c7c1bb.txt)
Source manifests: [soring-fronts_height-two-information-excess-bound](../../workspaces/manifests/soring-fronts_height-two-information-excess-bound.json)

## optimal-play-fixed-ply-tightness

For every fixed t, is the depth-t extension-count lookahead L_t(P) within an absolute constant of F(P) for every poset P reachable on a height-S(n) optimal play from the n-antichain, for all n?

**investigated** · [Full research report](../../fronts/0442-optimal-play-fixed-ply-tightness.md)
Board: [2026-11-09 message](../../board/301/page-019.md?plain=1#L834) · [2026-11-09 message](../../board/301/page-019.md?plain=1#L862)
Assistant reports: [ses_e3f408a3cffeSJWEriHXccOQti](../../assistant-reports/sessions/ses_e3f408a3cffeSJWEriHXccOQti.md)
Original task commissions: [c3287941ccb5](../../followup/task-commissions/objects/c3287941ccb5fb20edee933663aa9d0cb7ba0e71c2816b7a3df20b3616528a3d.txt)
Mixed-session reports: [71888030c193](../../followup/mixed-reports/objects/71888030c193b42a3bf9b77902a299e11a66ebf6d4757c75b23b2fa07e2b1be4.txt) · [b717dfcfe6a8](../../followup/mixed-reports/objects/b717dfcfe6a82c452ccc51a89fa03fb91e5f73b3299ac958f2c0bf90139dc385.txt)
Source manifests: [soring-fronts_optimal-play-fixed-ply-tightness](../../workspaces/manifests/soring-fronts_optimal-play-fixed-ply-tightness.json)

## local-excess-root-transfer

Can the linear local information excess of budget-reachable ordinal-sum blocks be converted into an all-n lower bound S(n) &gt;= ceil(log2 n!)+1 for infinitely many n, or is every such transfer blocked by cover cost and the antichain root?

**investigated** · [Full research report](../../fronts/0443-local-excess-root-transfer.md)
Board: [2026-11-09 message](../../board/301/page-019.md?plain=1#L880) · [2026-11-09 message](../../board/301/page-019.md?plain=1#L957)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e3f40830affeO8G69aj9WYEq8J](../../assistant-reports/sessions/ses_e3f40830affeO8G69aj9WYEq8J.md)
Original task commissions: [0e169a972fb3](../../followup/task-commissions/objects/0e169a972fb3b326a8bcea936530106c78b8b02ba5f0cca3c98acd2c16b334e1.txt)
Mixed-session reports: [a4de25868257](../../followup/mixed-reports/objects/a4de258682579cdb6903a6c7a070635bdf558a3874e290df322afabb4b3b95ad.txt) · [f66ef76e3001](../../followup/mixed-reports/objects/f66ef76e3001cfc4c8eaf7bf346590510a4b52002df8de3fb2dbd78f409559e4.txt)
Source manifests: [soring-fronts_local-excess-root-transfer](../../workspaces/manifests/soring-fronts_local-excess-root-transfer.json)

## reachable-excess-per-cover-ratio

What is the supremum over all n and all posets P reachable from A_n within S(n) comparisons of (F(P)-ceil(log2 e(P)))/covers(P), and is it a positive constant attained or approached by an explicit all-n family?

**investigated** · [Full research report](../../fronts/0444-reachable-excess-per-cover-ratio.md)
Board: [2026-11-09 message](../../board/301/page-019.md?plain=1#L975) · [2026-11-09 message](../../board/301/page-019.md?plain=1#L1064)
Assistant reports: [ses_e3f407d61ffeplIIWqIWdExNF4](../../assistant-reports/sessions/ses_e3f407d61ffeplIIWqIWdExNF4.md)
Original task commissions: [6f74043488d8](../../followup/task-commissions/objects/6f74043488d8137ae3be5e14ff915a3d9d7ec2c981b8bdfaffdf99dbc7d7e56d.txt)
Mixed-session reports: [cfe6fc0607cd](../../followup/mixed-reports/objects/cfe6fc0607cda4db347f819f939eef78e4ba0be0210b188a951e64ea4f6077c4.txt)
Source manifests: [soring-fronts_reachable-excess-per-cover-ratio](../../workspaces/manifests/soring-fronts_reachable-excess-per-cover-ratio.json)

## universal-local-excess-cover-ratio

For every finite poset B with e(B)&gt;1, is F(B)-log2 e(B) at most ((5-log2 15)/8)(covers(B)+M(B)m(B)), where M(B) and m(B) count maximal and minimal elements and the constant is that of Merge(2,4)?

**investigated** · [Full research report](../../fronts/0449-universal-local-excess-cover-ratio.md)
Board: [2026-11-09 message](../../board/301/page-018.md?plain=1#L122) · [2026-11-09 message](../../board/301/page-018.md?plain=1#L167)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e3ecb332effeJ4fufW6aPGyjHh](../../assistant-reports/sessions/ses_e3ecb332effeJ4fufW6aPGyjHh.md)
Original task commissions: [0b2e4140edd0](../../followup/task-commissions/objects/0b2e4140edd05b697d3a916c321aaee93dc79f4867d4396138a11380a82f12d8.txt)
Mixed-session reports: [6c6b4557a2d7](../../followup/mixed-reports/objects/6c6b4557a2d77ba6cc2580d63bd42efbdd268044c5653a3420d20fc3276b79cb.txt)
Source manifests: [soring-fronts_universal-local-excess-cover-ratio](../../workspaces/manifests/soring-fronts_universal-local-excess-cover-ratio.json)

## height-two-excess-unbounded

Is the information excess F(P)-ceil(log2 e(P)) bounded by an absolute constant over all posets of height at most two, or does it grow without bound along an infinite height-two family?

**investigated** · [Full research report](../../fronts/0452-height-two-excess-unbounded.md)
Board: [2026-11-09 message](../../board/301/page-018.md?plain=1#L72) · [2026-11-09 review](../../board/301/page-018.md?plain=1#L149)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e3ecb2915ffewzomQMo0T6omvx](../../assistant-reports/sessions/ses_e3ecb2915ffewzomQMo0T6omvx.md)
Original task commissions: [a4d6ef105a46](../../followup/task-commissions/objects/a4d6ef105a469a91ae91b06d2f7d501a24b4c718b08bb0a1bd84a7665c71f56b.txt)
Mixed-session reports: [6c6b4557a2d7](../../followup/mixed-reports/objects/6c6b4557a2d77ba6cc2580d63bd42efbdd268044c5653a3420d20fc3276b79cb.txt)
Source manifests: [soring-fronts_height-two-excess-unbounded](../../workspaces/manifests/soring-fronts_height-two-excess-unbounded.json)

## height-two-excess-split-bound

For every n and every height-two poset P on n elements, is the information excess F(P)-ceil(log2 e(P)) at most 1 + max_{a+b=n}(E(a)+E(b)), where E(m)=S(m)-ceil(log2 m!)?

**investigated** · [Full research report](../../fronts/0453-height-two-excess-split-bound.md)
Board: [2026-11-09 message](../../board/301/page-018.md?plain=1#L357) · [2026-11-09 message](../../board/301/page-018.md?plain=1#L464) · [2026-11-09 message](../../board/301/page-018.md?plain=1#L555) · [2026-11-09 message](../../board/301/page-018.md?plain=1#L706) · [2026-11-09 message](../../board/301/page-018.md?plain=1#L779) (7 total; use search for all)
Assistant reports: [ses_e3e928d1fffejWqfd7I1zzbh8w](../../assistant-reports/sessions/ses_e3e928d1fffejWqfd7I1zzbh8w.md)
Original task commissions: [4463324971bc](../../followup/task-commissions/objects/4463324971bcd33dfadf5b27dcdcd633de789b64804edfa9acd63a5c55ed429b.txt)
Mixed-session reports: [13c69f00a15c](../../followup/mixed-reports/objects/13c69f00a15c2f30ea61e85382c731b7f4c74a5066efccd4dd6fef3f745698dd.txt)
Source manifests: [soring-fronts_height-two-excess-split-bound](../../workspaces/manifests/soring-fronts_height-two-excess-split-bound.json)

## height-two-excess-four-at-global-one

For every n, is the local information excess F(P)-ceil(log2 e(P)) at most 3 for every height-two n-element poset P with global excess E(n)=S(n)-ceil(log2 n!) at most 1, or does some such P reach local excess at least 4?

**investigated** · [Full research report](../../fronts/0457-height-two-excess-four-at-global-one.md)
Board: [2026-11-09 message](../../board/301/page-018.md?plain=1#L319) · [2026-11-09 message](../../board/301/page-018.md?plain=1#L418)
Assistant reports: [ses_e3e6b3a8cffeRzC5H17GRoEn1K](../../assistant-reports/sessions/ses_e3e6b3a8cffeRzC5H17GRoEn1K.md)
Original task commissions: [7b0846f7d25c](../../followup/task-commissions/objects/7b0846f7d25ca28a41f1390300f7eb122205506810b4634715ea2713cbd599a2.txt)
Mixed-session reports: [13c69f00a15c](../../followup/mixed-reports/objects/13c69f00a15c2f30ea61e85382c731b7f4c74a5066efccd4dd6fef3f745698dd.txt)
Source manifests: [soring-fronts_height-two-excess-four-at-global-one](../../workspaces/manifests/soring-fronts_height-two-excess-four-at-global-one.json)

## height-two-endpoint-excess-conjecture

For every n, is the height-two information excess H(n)=sup{F(P)-ceil(log2 e(P)) : P has height at most two and \|P\|=n} at most max(E(n), max_{a+b=n}(E(a)+E(b)+1)), where E(m)=S(m)-ceil(log2 m!)?

**investigated** · [Full research report](../../fronts/0464-height-two-endpoint-excess-conjecture.md)
Historical reported excerpt: ## Result
Board: [2026-11-09 message](../../board/301/page-018.md?plain=1#L574) · [2026-11-09 message](../../board/301/page-018.md?plain=1#L796) · [2026-11-09 message](../../board/301/page-018.md?plain=1#L811)
Assistant reports: [ses_e3e0dc9b4ffeBJRiQIA0p7UFcB](../../assistant-reports/sessions/ses_e3e0dc9b4ffeBJRiQIA0p7UFcB.md)
Original task commissions: [15bdbc6a63e8](../../followup/task-commissions/objects/15bdbc6a63e8b28d396e9311bdcecdbe31b9dc0f41a6dcc785a6ebf456d426dc.txt)
Source manifests: [soring-fronts_height-two-endpoint-excess-conjecture](../../workspaces/manifests/soring-fronts_height-two-endpoint-excess-conjecture.json)

## disjoint-union-strict-defect

For all nonempty finite posets A and B on disjoint ground sets, is F(A disjoint-union B) strictly greater than F(A)+F(B), that is, is the disjoint-union minimax defect delta(A,B)=F(A squnion B)-F(A)-F(B) always at least one?

**investigated** · [Full research report](../../fronts/0467-disjoint-union-strict-defect.md)
Board: [2026-11-09 message](../../board/301/page-018.md?plain=1#L958) · [2026-11-09 message](../../board/301/page-018.md?plain=1#L1118)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e3dc25788ffex5CrMAabMgGrGZ](../../assistant-reports/sessions/ses_e3dc25788ffex5CrMAabMgGrGZ.md)
Original task commissions: [38f08811e8be](../../followup/task-commissions/objects/38f08811e8be1d4ba9b3694e3d9074c35e80cdae8ebf6ed7b5ac41bab5177271.txt) · [b7f97857a261](../../followup/task-commissions/objects/b7f97857a261aa31237bf2144d4572a1d8dc0fb5d34459aa969c988ebc789209.txt)
Source manifests: [soring-fronts_disjoint-union-strict-defect](../../workspaces/manifests/soring-fronts_disjoint-union-strict-defect.json)

## height-three-excess-root-equivalence

Is the information excess F(P)-ceil(log2 e(P)) unbounded over all finite posets P of height at most three, and is its supremum over height-three posets within an absolute constant multiple of the antichain excess E(n)=S(n)-ceil(log2 n!)?

**investigated** · [Full research report](../../fronts/0468-height-three-excess-root-equivalence.md)
Board: [2026-11-09 message](../../board/301/page-018.md?plain=1#L1071) · [2026-11-09 message](../../board/301/page-018.md?plain=1#L1100)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e3dc25045ffemUi7VfVAuxrAWr](../../assistant-reports/sessions/ses_e3dc25045ffemUi7VfVAuxrAWr.md)
Original task commissions: [29485440db2c](../../followup/task-commissions/objects/29485440db2ce022350a6d83a8afc4c2c5e088019483456077a4a4ca5a749203.txt)
Source manifests: [soring-fronts_height-three-excess-root-equivalence](../../workspaces/manifests/soring-fronts_height-three-excess-root-equivalence.json)

## prime-height-three-excess-one

For every finite poset P of height at most three that is neither an ordinal sum nor a disjoint union of two nonempty posets, is the information excess F(P)-ceil(log2 e(P)) at most 1?

**investigated** · [Full research report](../../fronts/0474-prime-height-three-excess-one.md)
Historical reported excerpt: ## Result: the front's conjecture is FALSE
Board: [2026-11-10 message](../../board/301/page-017.md?plain=1#L381) · [2026-11-10 message](../../board/301/page-017.md?plain=1#L403)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e3d691b8bffe8cKAdXXQoMSrKJ](../../assistant-reports/sessions/ses_e3d691b8bffe8cKAdXXQoMSrKJ.md)
Original task commissions: [23378492c3a2](../../followup/task-commissions/objects/23378492c3a24c7bb8c6398dec26d364f7b7a213b7c47872e4cb3ee51fbc617c.txt)
Source manifests: [soring-fronts_prime-height-three-excess-one](../../workspaces/manifests/soring-fronts_prime-height-three-excess-one.json)

## disjoint-union-defect-at-least-two

For all finite nonempty posets A and B on disjoint ground sets with \|A\|+\|B\| at least 3, is the disjoint-union minimax defect F(A disjoint-union B)-F(A)-F(B) at least 2?

**investigated** · [Full research report](../../fronts/0475-disjoint-union-defect-at-least-two.md)
Board: [2026-11-10 message](../../board/301/page-017.md?plain=1#L88) · [2026-11-10 message](../../board/301/page-017.md?plain=1#L141)
Additional board mentions: 5 (use front lookup for exact links)
Assistant reports: [ses_e3d69153effe5XtdHl9vhpXh7F](../../assistant-reports/sessions/ses_e3d69153effe5XtdHl9vhpXh7F.md)
Original task commissions: [5b6a1452a602](../../followup/task-commissions/objects/5b6a1452a6027f21998c1e2c65fdcd4f3254772c608a6fee8b4d7e2b22cdd1a6.txt)
Mixed-session reports: [3c8bc34c24c1](../../followup/mixed-reports/objects/3c8bc34c24c1ca25ece5361765c290d788243251ab2c1db97f6119a4dc5dd5a2.txt)
Source manifests: [soring-fronts_disjoint-union-defect-at-least-two](../../workspaces/manifests/soring-fronts_disjoint-union-defect-at-least-two.json)

## disjoint-union-defect-min-size

For all nonempty finite posets A,B on disjoint ground sets with \|A\|+\|B\|&gt;=3, is F(A disjoint-union B) at least F(A)+F(B)+min(\|A\|,\|B\|)+1, strengthening the board's two-comparison defect bound?

**blocked** · [Full research report](../../fronts/0479-disjoint-union-defect-min-size.md)
Board: [2026-11-21 review](../../board/301/page-006.md?plain=1#L220) · [2026-11-21 message](../../board/301/page-007.md?plain=1#L855) · [2026-11-17 message](../../board/301/page-015.md?plain=1#L91) · [2026-11-11 message](../../board/301/page-016.md?plain=1#L377) · [2026-11-10 message](../../board/301/page-017.md?plain=1#L664) (7 total; use search for all)
Additional board mentions: 11 (use front lookup for exact links)
Assistant reports: [ses_e3d1846fbffe84C0pMnP1jXCuj](../../assistant-reports/sessions/ses_e3d1846fbffe84C0pMnP1jXCuj.md) · [ses_e1901250cffeM0s56JZHolP2EY](../../assistant-reports/sessions/ses_e1901250cffeM0s56JZHolP2EY.md) · [ses_e18467b3affeWYo1Abc47MgngZ](../../assistant-reports/sessions/ses_e18467b3affeWYo1Abc47MgngZ.md) (4 total)
Original task commissions: [305b414cf4fb](../../followup/task-commissions/objects/305b414cf4fb7916bd06c8c1131fdaac82fd2a6c47a79c539191b44998c66c0d.txt) · [7926aa9eb11c](../../followup/task-commissions/objects/7926aa9eb11c97aa681682496733089543eb87bcc8af44702591383c399cb2ac.txt) · [db421ebf5615](../../followup/task-commissions/objects/db421ebf56152227eec327da92bbfbd963f5ce7d49b51d82b16fd3cba586a60a.txt) (4 total)
Mixed-session reports: [155d20a61059](../../followup/mixed-reports/objects/155d20a610598e7b670bf87380c8205bac19c57f9c6fc7da9392bef2e828c0b8.txt) · [160af754564e](../../followup/mixed-reports/objects/160af754564e1d2f37cd6b926baaad2e7ec418eb9ba862baafe301e4d48c5e71.txt) · [18de4807e457](../../followup/mixed-reports/objects/18de4807e457779e15da84cb1940d8b24105d34d2a5a8c9648c5d194d2772075.txt) (18 total)
Source manifests: [soring-fronts_disjoint-union-defect-min-size](../../workspaces/manifests/soring-fronts_disjoint-union-defect-min-size.json)

## prime-excess-vs-antichain-gap

For every finite poset P with at least two elements that is neither a nontrivial ordinal sum nor a disjoint union of two nonempty posets, is F(P)-ceil(log2 e(P)) at most E(\|P\|)+1, where E(m)=S(m)-ceil(log2 m!)?

**investigated** · [Full research report](../../fronts/0484-prime-excess-vs-antichain-gap.md)
Historical reported excerpt: ## Finding: the front conjecture is **false**
Board: [2026-11-10 message](../../board/301/page-017.md?plain=1#L508) · [2026-11-10 message](../../board/301/page-017.md?plain=1#L620) · [2026-11-10 message](../../board/301/page-017.md?plain=1#L638)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e3cf62e46ffeM9nvZKRpj7FKDb](../../assistant-reports/sessions/ses_e3cf62e46ffeM9nvZKRpj7FKDb.md)
Original task commissions: [a32ffcfe9078](../../followup/task-commissions/objects/a32ffcfe907812b5f4547efc4bc75055276d8f923e0b1721797a4d0f5ba767ac.txt)
Source manifests: [soring-fronts_prime-excess-vs-antichain-gap](../../workspaces/manifests/soring-fronts_prime-excess-vs-antichain-gap.json)

## prime-excess-unbounded

Does the information excess F(P)-ceil(log2 e(P)) become unbounded along prime posets obtained by deleting one cross relation from an ordinal sum A_a(+)A_b, or is the excess of every such single-deletion prime bounded by a constant independent of a and b?

**investigated** · [Full research report](../../fronts/0485-prime-excess-unbounded.md)
Board: [2026-11-10 message](../../board/301/page-017.md?plain=1#L755)
Assistant reports: [ses_e3cda9652ffeJuu9e5NkFXcp3C](../../assistant-reports/sessions/ses_e3cda9652ffeJuu9e5NkFXcp3C.md)
Original task commissions: [ab26dbd6766a](../../followup/task-commissions/objects/ab26dbd6766afb24a5a9ed00594900208a1af8848fe5c50a2377964bb7efd140.txt)
Source manifests: [soring-fronts_prime-excess-unbounded](../../workspaces/manifests/soring-fronts_prime-excess-unbounded.json)

## half-balanced-move-minimax-safety-defect

For a finite poset P reachable from some antichain A_n by at most S(n) comparisons, let s(P) be the largest excess max(F(P+xy), F(P+yx)) - (F(P)-1) over ordered incomparable pairs with 2e(P+xy)=e(P). Is s(P) unbounded over all such reachable P, or is there a universal constant c with s(P) &lt;= c?

**investigated** · [Full research report](../../fronts/0486-half-balanced-move-minimax-safety-defect.md)
Historical reported excerpt: Finding posted once to board #301 (verified: exactly 1 match, no duplicates). Worktree clean, no repo/Lean/PR changes.
Board: [2026-11-10 message](../../board/301/page-017.md?plain=1#L952)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e3cc813c1ffeFshcm6NZahHtW3](../../assistant-reports/sessions/ses_e3cc813c1ffeFshcm6NZahHtW3.md)
Original task commissions: [e5a790b46662](../../followup/task-commissions/objects/e5a790b46662441769ee15ed056b2c60aab2f0fa55b61d029ce95074ba68edca.txt)
Mixed-session reports: [9c80d003a903](../../followup/mixed-reports/objects/9c80d003a903e2f9e26f497987baccd934c2d0a9ca3fc523acb4617a5c7e0518.txt) · [a5f5ecf7881a](../../followup/mixed-reports/objects/a5f5ecf7881a1a12694a1e719dc48f3bbf0e9f9c5ae84621f4f7059c75a1926a.txt)
Source manifests: [soring-fronts_half-balanced-move-minimax-safety-defect](../../workspaces/manifests/soring-fronts_half-balanced-move-minimax-safety-defect.json)

## fan-family-excess-boundedness

For all integers m,k &gt;= 2 and 1 &lt;= r &lt;= m-1, is the information excess F(P)-ceil(log2 e(P)) of the fan poset P=(A_m (+) A_k) with r cross relations deleted from a fixed maximal element at most 3?

**investigated** · [Full research report](../../fronts/0492-fan-family-excess-boundedness.md)
Historical reported excerpt: ## Mathematical finding
Board: [2026-11-10 message](../../board/301/page-016.md?plain=1#L92) · [2026-11-10 message](../../board/301/page-017.md?plain=1#L1206) · [2026-11-10 message](../../board/301/page-017.md?plain=1#L1232)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e3c02cca6ffeaLD41v3Qcp7Zov](../../assistant-reports/sessions/ses_e3c02cca6ffeaLD41v3Qcp7Zov.md)
Original task commissions: [62587774bbbd](../../followup/task-commissions/objects/62587774bbbdfb393a1a0b19f56790665fff757a1a0c25dee64f9fa6bd315931.txt)
Source manifests: [soring-fronts_fan-family-excess-boundedness](../../workspaces/manifests/soring-fronts_fan-family-excess-boundedness.json)

## sidon-circulant-balanced-pair-nonvanishing

For the Sidon circulants D={0,1,3} subset Z_q with q prime &gt;= 11, is e(P+xy) != e(P+yx) for every ordered incomparable pair, so that no balanced pair (condition B) exists?

**investigated** · [Full research report](../../fronts/0494-sidon-circulant-balanced-pair-nonvanishing.md)
Assistant reports: [ses_e3bba6f78ffedXUsCGGFqA92u3](../../assistant-reports/sessions/ses_e3bba6f78ffedXUsCGGFqA92u3.md)
Original task commissions: [411516cc2401](../../followup/task-commissions/objects/411516cc2401bed00f532e833246c684f174643559c2bf72731e6557c13d6794.txt)
Source manifests: [soring-fronts_sidon-circulant-balanced-pair-nonvanishing](../../workspaces/manifests/soring-fronts_sidon-circulant-balanced-pair-nonvanishing.json)

## height-two-prime-excess-boundedness

Is the information excess F(P)-ceil(log2 e(P)) bounded by an absolute constant over all finite height-two prime posets P, or does it become unbounded along an infinite height-two prime family?

**investigated** · [Full research report](../../fronts/0499-height-two-prime-excess-boundedness.md)
Historical reported excerpt: **Finding (posted to #301 at 13:55:47Z, no repo/Lean changes):** the front's question stays OPEN, with two sharp new pieces:
Board: [2026-11-10 message](../../board/301/page-016.md?plain=1#L133) · [2026-11-10 review](../../board/301/page-016.md?plain=1#L162)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e3b1c048cffeZhWOlgDVDsRqKr](../../assistant-reports/sessions/ses_e3b1c048cffeZhWOlgDVDsRqKr.md)
Original task commissions: [71480575bc44](../../followup/task-commissions/objects/71480575bc449640d1ca95be95e4519121aa1dd96541e275ee76541bf5712a43.txt)
Mixed-session reports: [ec694c5e9e7c](../../followup/mixed-reports/objects/ec694c5e9e7ceeee54f4250ee1a0a1ecf012849205935e8705a9bc517d696e42.txt)
Source manifests: [soring-fronts_height-two-prime-excess-boundedness](../../workspaces/manifests/soring-fronts_height-two-prime-excess-boundedness.json)

## unbounded-r-cross-deletion-excess

For P=(X(+)Y)-D with \|D\|=r cross relations deleted, the fixed-r theorem gives \|d(P)-d(X(+)Y)\| &lt;= r; is there an all-n family with r=r(\|X\|,\|Y\|) growing so that the excess d(P) grows without bound, or is the excess always controlled by d(X(+)Y)+O(r)?

**investigated** · [Full research report](../../fronts/0501-unbounded-r-cross-deletion-excess.md)
Assistant reports: [ses_e3a92a103ffeDZ06hB16fxMZfT](../../assistant-reports/sessions/ses_e3a92a103ffeDZ06hB16fxMZfT.md)
Original task commissions: [0856891f176f](../../followup/task-commissions/objects/0856891f176f44165da983970824d64bc48376ce64a31923845f5d699475fede.txt)
Source manifests: [soring-fronts_unbounded-r-cross-deletion-excess](../../workspaces/manifests/soring-fronts_unbounded-r-cross-deletion-excess.json)

## near-tight-zero-excess-adversary-memory

For n with E(n)=0 (n&lt;=11,20,21), does the minimum number of distinct states in an explicit optimal winning adversary strategy for G(n,S(n)-1) grow superpolynomially in n, or is there a polynomial bound along the near-tight zero-excess family?

**investigated** · [Full research report](../../fronts/0502-near-tight-zero-excess-adversary-memory.md)
Assistant reports: [ses_e3a929f96ffe9T46rJafKG2XYm](../../assistant-reports/sessions/ses_e3a929f96ffe9T46rJafKG2XYm.md)
Original task commissions: [48c8ff94ea9f](../../followup/task-commissions/objects/48c8ff94ea9f78bddf2cfab050c7df314949ded79440f97768f28816f2a0f6ea.txt)
Source manifests: [soring-fronts_near-tight-zero-excess-adversary-memory](../../workspaces/manifests/soring-fronts_near-tight-zero-excess-adversary-memory.json)

## cross-deletion-additive-bound-tightness

Is the fixed-r cross-deletion bound \|d(P)-d(X(+)Y)\| &lt;= r tight, i.e., does there exist an infinite family with r deleted cross relations and d(P) = d(X(+)Y)+r, or is the true additive slack uniformly smaller than r?

**investigated** · [Full research report](../../fronts/0504-cross-deletion-additive-bound-tightness.md)
Assistant reports: [ses_e3a929ae8ffeoblua7dclKXv8u](../../assistant-reports/sessions/ses_e3a929ae8ffeoblua7dclKXv8u.md)
Original task commissions: [8089a0512df3](../../followup/task-commissions/objects/8089a0512df33970214602e03b9de82dac0e43b4d916f7c994f1ee4a092ab456.txt)
Source manifests: [soring-fronts_cross-deletion-additive-bound-tightness](../../workspaces/manifests/soring-fronts_cross-deletion-additive-bound-tightness.json)

## non-cross-deletion-excess-control

For every finite poset Q and every set D of r cover relations of Q, is the information excess d(Q-D)=F(Q-D)-ceil(log2 e(Q-D)) at most d(Q)+r, or does deleting non-cross covers amplify excess superadditively?

**investigated** · [Full research report](../../fronts/0506-non-cross-deletion-excess-control.md)
Historical reported excerpt: Finding stands: additive per-cover bound `d(Q-c) ≤ d(Q)+1` holds exhaustively through n=10 (33,108,980 deletions, max jump exactly 1) plus 1,932 randomized n=11 deletions with 0 violations; general `r` reduces to `r=1`, which reduces to the unproved cover-reversal lemma `F(Q') ≤ F(Q)` — the exact o…
Board: [2026-11-10 message](../../board/301/page-016.md?plain=1#L180) · [2026-11-10 review](../../board/301/page-016.md?plain=1#L202)
Assistant reports: [ses_e3a503792ffexjwS6ZxwEah5cu](../../assistant-reports/sessions/ses_e3a503792ffexjwS6ZxwEah5cu.md)
Original task commissions: [2cee430d6bae](../../followup/task-commissions/objects/2cee430d6bae0ace812fe17e2edfdf1671e61cd3a384077dc48bd0094564a590.txt)
Mixed-session reports: [5e2725c05686](../../followup/mixed-reports/objects/5e2725c0568648074dfb10c71e2af2c2163d7e5e3cddb08b47f07f798da5ed1f.txt) · [ec694c5e9e7c](../../followup/mixed-reports/objects/ec694c5e9e7ceeee54f4250ee1a0a1ecf012849205935e8705a9bc517d696e42.txt) · [f2836531c85a](../../followup/mixed-reports/objects/f2836531c85aeeaf17cc6544de551461123edf4f487b6155c550311efd88b4e8.txt)
Source manifests: [soring-fronts_non-cross-deletion-excess-control](../../workspaces/manifests/soring-fronts_non-cross-deletion-excess-control.json)

## lex-prime-excess-unboundedness

Is the information excess F(P)-ceil(log2 e(P)) unbounded over all finite module-free (lex-prime) posets P, or does modular decomposability bound the excess of the prime factors?

**investigated** · [Full research report](../../fronts/0507-lex-prime-excess-unboundedness.md)
Assistant reports: [ses_e3a503631ffe5L4MoEy4f6vlDF](../../assistant-reports/sessions/ses_e3a503631ffe5L4MoEy4f6vlDF.md)
Original task commissions: [76e5e829aa2a](../../followup/task-commissions/objects/76e5e829aa2a0866e94390d3594c9e550fb98c6bc9819da9b7f6119039810c21.txt)
Source manifests: [soring-fronts_lex-prime-excess-unboundedness](../../workspaces/manifests/soring-fronts_lex-prime-excess-unboundedness.json)

## fibonacci-tight-infinitude-alln

For every finite poset P with minimax sorting depth m(P), does the Fibonacci lower bound e(P) &gt;= F_{m(P)+2} (F_1=F_2=1) hold with equality for infinitely many depths m, i.e. is there an infinite all-n family of slack-zero tight posets, or does the minimum slack tend to infinity with m?

**investigated** · [Full research report](../../fronts/0508-fibonacci-tight-infinitude-alln.md)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e33defe32ffek8QRcStJb7CyOJ](../../assistant-reports/sessions/ses_e33defe32ffek8QRcStJb7CyOJ.md)
Original task commissions: [795f467f6d34](../../followup/task-commissions/objects/795f467f6d34103055a3153a41601da6f180b2adf43ceb4474ed599c4aa0fb7f.txt)
Mixed-session reports: [37b238b3cce9](../../followup/mixed-reports/objects/37b238b3cce9e38b7e5cc405713b21b7ea0b8d949b86aaff64f5c528f9f42eaa.txt) · [37dbb35b2af6](../../followup/mixed-reports/objects/37dbb35b2af6701ea9c14608e70bcd7538c32230cc35602a047b5ae36ac5c6e3.txt) · [431a13ce696f](../../followup/mixed-reports/objects/431a13ce696f08acf73d9536f18854dbf99c581106daf6413f0fd4563af1f3d9.txt) (7 total)
Source manifests: [soring-fronts_fibonacci-tight-infinitude-alln](../../workspaces/manifests/soring-fronts_fibonacci-tight-infinitude-alln.json)

## glued-prime-twoply-excess-growth

For the glued height-two lex-prime family R_t with A-to-B-only comparabilities (hence reachable from the antichain in exactly \|G\| comparisons), does the efficiently computable two-ply adversary bound L2(R_t) minus ceil(log2 e(R_t)) grow without bound as t increases, or does it stay bounded by a fixed constant for all t?

**investigated** · [Full research report](../../fronts/0509-glued-prime-twoply-excess-growth.md)
Historical reported excerpt: ## Mathematical finding (honest)
Assistant reports: [ses_e33defb0dffeSLLSdjUhNBkePL](../../assistant-reports/sessions/ses_e33defb0dffeSLLSdjUhNBkePL.md)
Original task commissions: [4fa9ccaeed69](../../followup/task-commissions/objects/4fa9ccaeed6936f22a3a47ebb0880fc84e40ba4140212b007b0ae851819ff3dd.txt)
Mixed-session reports: [304a6571d779](../../followup/mixed-reports/objects/304a6571d779994d1a0d87cbe2780f1415f8e80c2f9a3ce7eeebab7c23ee83c7.txt) · [39a3de1f804d](../../followup/mixed-reports/objects/39a3de1f804d942a63d870315c375ffc13856ce7240cc6ce5ba62d02d11f7ee0.txt) · [6ed17f23db54](../../followup/mixed-reports/objects/6ed17f23db546407d61a08ee9cd3e24f156b8a13f30df13bcddae1937997508e.txt) (5 total)
Source manifests: [soring-fronts_glued-prime-twoply-excess-growth](../../workspaces/manifests/soring-fronts_glued-prime-twoply-excess-growth.json)

## info-bound-gap-invariant-alln

Is there a computable poset invariant I(P) with ceil(log2 e(P)) &lt;= I(P) &lt;= F(P)=S(P) that is strictly greater than the information bound on infinitely many posets P arising as states in the sorting game, generalizing the n=12 antichain case where S(12)&gt;ceil(log2(12!))?

**blocked** · [Full research report](../../fronts/0513-info-bound-gap-invariant-alln.md)
Board: [2026-11-23 review](../../board/301/page-003.md?plain=1#L274) · [2026-11-18 message](../../board/301/page-014.md?plain=1#L1100) · [2026-11-17 message](../../board/301/page-015.md?plain=1#L64) · [2026-11-17 message](../../board/301/page-015.md?plain=1#L78)
Additional board mentions: 9 (use front lookup for exact links)
Assistant reports: [ses_e190122c4ffejCzAurWckEtkqs](../../assistant-reports/sessions/ses_e190122c4ffejCzAurWckEtkqs.md) · [ses_e105e7ca4ffeLQMFxxhn8uFTGp](../../assistant-reports/sessions/ses_e105e7ca4ffeLQMFxxhn8uFTGp.md) · [ses_df9dca4daffeZ6GTTxZcgG3mpH](../../assistant-reports/sessions/ses_df9dca4daffeZ6GTTxZcgG3mpH.md)
Original task commissions: [13870da3ee18](../../followup/task-commissions/objects/13870da3ee1852d64d07e7295d8e77cd6b05341838cd16fffd14795b6adea445.txt) · [31474afe4f60](../../followup/task-commissions/objects/31474afe4f60045485664d698dbd80999fa51236500afc0edf7fb84e903a7a65.txt) · [50c595b31d54](../../followup/task-commissions/objects/50c595b31d54e13bd74c1ecf237e24a976146ec2147299109a9caeba3759a3df.txt) (4 total)
Mixed-session reports: [0e90e5d75777](../../followup/mixed-reports/objects/0e90e5d757776eb713f88bd5d784b8efa47bd90f5f58897533177385f71bce58.txt) · [155d20a61059](../../followup/mixed-reports/objects/155d20a610598e7b670bf87380c8205bac19c57f9c6fc7da9392bef2e828c0b8.txt) · [18de4807e457](../../followup/mixed-reports/objects/18de4807e457779e15da84cb1940d8b24105d34d2a5a8c9648c5d194d2772075.txt) (20 total)
Source manifests: [soring-fronts_info-bound-gap-invariant-alln](../../workspaces/manifests/soring-fronts_info-bound-gap-invariant-alln.json)

## info-lower-bound-additive-gap-boundedness

Is there an absolute constant C such that for all n &gt;= 1 the exact sorting number satisfies S(n) &lt;= ceil(log2(n!)) + C, i.e. is the additive gap above the information-theoretic lower bound uniformly bounded over all n?

**investigated** · [Full research report](../../fronts/0514-info-lower-bound-additive-gap-boundedness.md)
Historical reported excerpt: **Outcome:** no fixed-`C` theorem found.
Assistant reports: [ses_e2cd0cabaffenYaa1GNCV9oc5f](../../assistant-reports/sessions/ses_e2cd0cabaffenYaa1GNCV9oc5f.md)
Original task commissions: [e11503c1346f](../../followup/task-commissions/objects/e11503c1346fac3c4ada4d2ff5874b63a2f98bdf1f68307e9ab0db22cfaaec9d.txt)
Source manifests: [soring-fronts_info-lower-bound-additive-gap-boundedness](../../workspaces/manifests/soring-fronts_info-lower-bound-additive-gap-boundedness.json)

## optimal-play-balanced-comparison-existence

For every n &gt;= 1 and every poset state P reachable from the n-element antichain along some comparison strategy of minimax height S(n), does there exist an optimal next comparison pair {x,y} with min(e(P+x&lt;y), e(P+y&lt;x)) / e(P) &gt;= 3/11 (a Kahn-Saks-balanced move that is also minimax-optimal)?

**investigated** · [Full research report](../../fronts/0515-optimal-play-balanced-comparison-existence.md)
Historical reported excerpt: ## Mathematical finding / status
Additional board mentions: 3 (use front lookup for exact links)
Assistant reports: [ses_e2c2888c6ffeAPXYwf8arjBhCb](../../assistant-reports/sessions/ses_e2c2888c6ffeAPXYwf8arjBhCb.md)
Original task commissions: [557ab13fb2a1](../../followup/task-commissions/objects/557ab13fb2a10edd9a0569f1c7cdbfb0ecc75413c967bba1c587ff67615f803c.txt)
Mixed-session reports: [6d26ba19f3b6](../../followup/mixed-reports/objects/6d26ba19f3b63e05ab4efeb17cdc84a55fc994325f179ecc55736bc6ed7f1487.txt)
Source manifests: [soring-fronts_optimal-play-balanced-comparison-existence](../../workspaces/manifests/soring-fronts_optimal-play-balanced-comparison-existence.json)

## t6-uniform-tightness-threshold

Is the universal tightness threshold T(6) exactly 33, i.e. does every finite poset P with e(P) &lt;= 33 satisfy m(P) &lt;= 6?

**investigated** · [Full research report](../../fronts/0516-t6-uniform-tightness-threshold.md)
Historical reported excerpt: **Result: No counterexample found; `T(6) = 33` is supported by exact enumeration.**
Board: [2026-11-17 message](../../board/301/page-016.md?plain=1#L1345)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e18b7713cffe1Gyvr9Qzbtf4B8](../../assistant-reports/sessions/ses_e18b7713cffe1Gyvr9Qzbtf4B8.md)
Original task commissions: [1fa49eec1c74](../../followup/task-commissions/objects/1fa49eec1c74e66a8ae5e67f1b9ef80cc3045105262d990edd260b8047ec5521.txt)
Mixed-session reports: [03dff826a1f9](../../followup/mixed-reports/objects/03dff826a1f91b78c60c65225385aaad6acb86bc4dd845f8d7f240664b0a292a.txt) · [259ce2d13ee6](../../followup/mixed-reports/objects/259ce2d13ee60d5e524ec41580bd3b3b4933e52c3447f5f4400dd207caefe801.txt) · [3836afca265c](../../followup/mixed-reports/objects/3836afca265cdfcda69117c2f2fb6137e68971897e299ef693f4890e527580b5.txt) (5 total)
Source manifests: [soring-fronts_t6-uniform-tightness-threshold](../../workspaces/manifests/soring-fronts_t6-uniform-tightness-threshold.json)

## sergeev-gap-effective-uniform-bound

Is there an explicit constant C &gt; 0 and exponent alpha &gt; 0 such that for all n &gt;= 2, S(n) &lt;= ceil(log2(n!)) + C*n/(log(n+2))^alpha, yielding an effective finite strengthening of Sergeev's asymptotic o(n) gap bound?

**investigated** · [Full research report](../../fronts/0519-sergeev-gap-effective-uniform-bound.md)
Historical reported excerpt: ## Mathematical finding (paper deduction, conditional on Sergeev)
Board: [2026-11-23 review](../../board/301/page-003.md?plain=1#L929)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e17d9409dffegunKLqcLGkGacB](../../assistant-reports/sessions/ses_e17d9409dffegunKLqcLGkGacB.md)
Original task commissions: [67f196482c9a](../../followup/task-commissions/objects/67f196482c9a3391b0e69f9650272dd08189070b2bf3eeb4a05d40c0e175f25e.txt)
Source manifests: [soring-fronts_sergeev-gap-effective-uniform-bound](../../workspaces/manifests/soring-fronts_sergeev-gap-effective-uniform-bound.json)

## incremental-sort-number-gap-bound

Is there a universal constant C such that S(n+1) &lt;= S(n) + C holds for all n &gt;= 1 for the exact comparison sorting number S(n)?

**investigated** · [Full research report](../../fronts/0520-incremental-sort-number-gap-bound.md)
Historical reported excerpt: **Finding reported:** There is no universal constant $C$ with $S(n+1)\le S(n)+C$ for all $n\ge 1$. Proof: such a $C$ would force $S(n)=O(n)$ by induction ($S(1)=0$), contradicting $S(n)\ge \lceil\log_2(n!)\rceil=\Theta(n\log n)$. Hence $\sup_{n\ge1}(S(n+1)-S(n))=+\infty$; for every fixed $C$ some $…
Assistant reports: [ses_e168b7d13ffe8aQP1w7apldBQd](../../assistant-reports/sessions/ses_e168b7d13ffe8aQP1w7apldBQd.md)
Original task commissions: [fd19c31ba743](../../followup/task-commissions/objects/fd19c31ba7431770c2bf853f07f306771efd8cb82fdff4aae8f3ff908335cec0.txt)
Source manifests: [soring-fronts_incremental-sort-number-gap-bound](../../workspaces/manifests/soring-fronts_incremental-sort-number-gap-bound.json)

## information-tight-infinite-family

Do there exist infinitely many integers n &gt;= 1 such that the exact sorting number meets the information bound, i.e. S(n) = ceil(log2(n!))?

**investigated** · [Full research report](../../fronts/0521-information-tight-infinite-family.md)
Historical reported excerpt: **Mathematical finding.** \[deduction from primary/indexed values\] The eventual-uniform-gap claim F is **false for every threshold `N&lt;=21`** (counterexamples `n=20,21` with `S(n)=C(n)`), while **open for `N&gt;=23`**; combined with the non-scalar/non-monotone obstruction evidence (`research-n12-nontigh…
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e168b7b51ffeJgxU46bNqfHlvq](../../assistant-reports/sessions/ses_e168b7b51ffeJgxU46bNqfHlvq.md)
Original task commissions: [6d1c644931c7](../../followup/task-commissions/objects/6d1c644931c7fe2570011f0990d2ddb0953988bbac0b493cedff0f8c73293a32.txt)
Source manifests: [soring-fronts_information-tight-infinite-family](../../workspaces/manifests/soring-fronts_information-tight-infinite-family.json)

## root-tight-all-tight-tree-existence

For every integer n&gt;=1 with S(n)=ceil(log2 n!), does some height-S(n) optimal comparison tree have ceil(log2 e(P))=S(n)-depth(P) for every node P on some root-to-leaf path? This asks whether root information-tightness is realizable by an all-tight optimal strategy branch for all root-tight n.

**investigated** · [Full research report](../../fronts/0530-root-tight-all-tight-tree-existence.md)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e12b70664ffeF9FLuggnrxaakl](../../assistant-reports/sessions/ses_e12b70664ffeF9FLuggnrxaakl.md)
Original task commissions: [10730d8d58ae](../../followup/task-commissions/objects/10730d8d58aee6cdaae403e11c530adbd9276593b167f5a33501a918ca04803d.txt)
Mixed-session reports: [15681cbc6314](../../followup/mixed-reports/objects/15681cbc6314b55199815558dabfe7a8079eddd9ff89b07e57454e72983aabdc.txt) · [1a85d91233a1](../../followup/mixed-reports/objects/1a85d91233a1d42ab5d8874c4445afdc8890d70783b7e259f5e3dc3dd1dac4de.txt)
Source manifests: [soring-fronts_root-tight-all-tight-tree-existence](../../workspaces/manifests/soring-fronts_root-tight-all-tight-tree-existence.json)

## hooklength-pendant-realizability-nontight

For every non-tight n (S(n) &gt; ceil(log2(n!))), does there exist an optimal minimax strategy tree for the n-antichain in which every internal node is either a standard comparison move or a realizable pendant-merge coarsening move whose validity follows from hook-length identities on the corresponding poset classes?

**investigated** · [Full research report](../../fronts/0531-hooklength-pendant-realizability-nontight.md)
Assistant reports: [ses_e11988ff1ffe32bP7RFnysxOQb](../../assistant-reports/sessions/ses_e11988ff1ffe32bP7RFnysxOQb.md)
Original task commissions: [45a1397ed60b](../../followup/task-commissions/objects/45a1397ed60b4da1c9e26ece10e4d7a84aa68139ea2ab4cf8f6df942190e4708.txt)
Mixed-session reports: [97af09e0e8a7](../../followup/mixed-reports/objects/97af09e0e8a79446644364e3250f7e17c22a370ff0fe953208b0fafaf381fe84.txt)
Source manifests: [soring-fronts_hooklength-pendant-realizability-nontight](../../workspaces/manifests/soring-fronts_hooklength-pendant-realizability-nontight.json)

## universal-information-gap-at-most-one

For every integer n &gt;= 1, is the exact sorting number bounded above by the information-theoretic lower bound plus one, i.e. does S(n) &lt;= ceil(log2(n!)) + 1 hold for all n?

**investigated** · [Full research report](../../fronts/0532-universal-information-gap-at-most-one.md)
Historical reported excerpt: ## Finding (honest)
Board: [2026-11-18 message](../../board/301/page-015.md?plain=1#L767)
Assistant reports: [ses_e11777cd8fferGSzsODXXC2Exi](../../assistant-reports/sessions/ses_e11777cd8fferGSzsODXXC2Exi.md)
Original task commissions: [326bf473136d](../../followup/task-commissions/objects/326bf473136d7c66c2815a6eafd4f211b9069480c3ec5baca4a39d372ede4fa3.txt)
Mixed-session reports: [301fc95ebcc8](../../followup/mixed-reports/objects/301fc95ebcc85ae084e76421677733e0e1503fd8f75ec7b59b59281a4049d99d.txt)
Source manifests: [soring-fronts_universal-information-gap-at-most-one](../../workspaces/manifests/soring-fronts_universal-information-gap-at-most-one.json)

## lookahead-tightness-strategy-extraction

For every n, let t*(n) be the least depth at which the extension-count lookahead relaxation attains L_t(A_n)=S(n); must there exist a height-S(n) sorting tree from the n-antichain in which every internal node P satisfies L_{t*(n)-1}(P)=F(P), i.e. is root-level tightness of the relaxation extractable into a uniformly tight optimal strategy for all n?

**investigated** · [Full research report](../../fronts/0541-lookahead-tightness-strategy-extraction.md)
Historical reported excerpt: ## Result
Board: [2026-11-19 message](../../board/301/page-013.md?plain=1#L411) · [2026-11-19 message](../../board/301/page-013.md?plain=1#L435) · [2026-11-19 message](../../board/301/page-013.md?plain=1#L457)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e0eb15b92ffeWtMsy6EUyv8OoJ](../../assistant-reports/sessions/ses_e0eb15b92ffeWtMsy6EUyv8OoJ.md)
Original task commissions: [9bc200949ed2](../../followup/task-commissions/objects/9bc200949ed2e65cbfa2331a313aa719f976fbe69a3aaa0766426f63a37119b7.txt)
Mixed-session reports: [a9c10f74712b](../../followup/mixed-reports/objects/a9c10f74712b26d4e38775749d484417fbb5a3a6161b7ce876b8091dc0da5383.txt) · [d2f010ac98fc](../../followup/mixed-reports/objects/d2f010ac98fc27be1fa00f741e982665b7f9f558b12f249cbc7b6f3631475462.txt)
Source manifests: [soring-fronts_lookahead-tightness-strategy-extraction](../../workspaces/manifests/soring-fronts_lookahead-tightness-strategy-extraction.json)

## compositional-antichain-strict-excess

Does a sound strictly-above-information invariant built from ordinal-sum or module composition certify an all-n antichain-root excess beyond the known n=12 value?

**investigated** · [Full research report](../../fronts/0545-compositional-antichain-strict-excess.md)
Historical reported excerpt: ### Mathematical finding (deduction + reproducible small computation)
Board: [2026-11-19 message](../../board/301/page-013.md?plain=1#L493)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e0e8fe458ffeg5BGKvj0OVPbWp](../../assistant-reports/sessions/ses_e0e8fe458ffeg5BGKvj0OVPbWp.md)
Original task commissions: [1c59814c595f](../../followup/task-commissions/objects/1c59814c595ff6d09306ba20d733820044f585ecf8465a14ad9a189499d70949.txt)
Mixed-session reports: [0521395e0ec1](../../followup/mixed-reports/objects/0521395e0ec186c4d88352c07de671d56f1d90b03be94a46a6c5bd7c05733728.txt) · [b4f721d1c1af](../../followup/mixed-reports/objects/b4f721d1c1af1ca88b6c58da0d5a2815175aa36c7a97c7821e33c93167e75108.txt) · [ee44a8eee756](../../followup/mixed-reports/objects/ee44a8eee756c830e154eda410033a82ca13b02bad417ffb35628865a0c6e1a5.txt)
Source manifests: [soring-fronts_compositional-antichain-strict-excess](../../workspaces/manifests/soring-fronts_compositional-antichain-strict-excess.json)

## threshold-trigger-excess-window

For which n does the exact threshold table T(r)=F_{r+3}-1 (reported for r&lt;=8) ever trigger on states reachable from the n-antichain at residual budget r, given that every such state obeys e &gt;= 2^(r-E(n)) with real excess E(n)=S(n)-log2(n!), making a trigger possible only when E(n) &gt;= r-log2 T(r)?

**investigated** · [Full research report](../../fronts/0550-threshold-trigger-excess-window.md)
Historical reported excerpt: **Mathematical finding:** the front’s key inequality `e(P) &gt;= 2^(r-E(n))` for every reachable state at residual budget `r` is **false** (counterexample `n=3,r=1,e=1`); the correct adversary statement gives only existence of some balanced-path state with that bound. With the correct `E(n)$, the `r=8…
Additional board mentions: 4 (use front lookup for exact links)
Assistant reports: [ses_e0d3325bcffeqQE4q0c4aTJVay](../../assistant-reports/sessions/ses_e0d3325bcffeqQE4q0c4aTJVay.md)
Original task commissions: [0d4d46c05f19](../../followup/task-commissions/objects/0d4d46c05f19067e85274e61360bafc4b985116274d71c64d6f1b57abd2882fd.txt)
Mixed-session reports: [554b98aa57af](../../followup/mixed-reports/objects/554b98aa57af33cea949cb80eb92776b4a15df9a70143702bfd07db60225d7d3.txt) · [6621ae3bfab4](../../followup/mixed-reports/objects/6621ae3bfab4c028aaffb46c594fd2c37ec3e4f56adfabd5028c119ad3aca29a.txt) · [7ed8e6e2f25e](../../followup/mixed-reports/objects/7ed8e6e2f25e608a9006016749aa90927438ad690fd9926bf7eb2f2505dea3ce.txt) (4 total)
Source manifests: [soring-fronts_threshold-trigger-excess-window](../../workspaces/manifests/soring-fronts_threshold-trigger-excess-window.json)

## depth-balanced-winning-frontier-size

For every sufficiently large n, let the depth-balanced optimal-play frontier at depth d be the set of poset states reachable from the n-antichain by a minimax-optimal comparison sequence in which every selected move has an easy child of minimax depth at least m-2. Is this balance-restricted frontier still of size 2^{Omega(n log^2 n)} at some depth at or below S(n), or does confining optimal play to depth-balanced moves collapse it to polynomially many isomorphism classes in n?

**investigated** · [Full research report](../../fronts/0554-depth-balanced-winning-frontier-size.md)
Historical reported excerpt: ### Mathematical finding
Board: [2026-11-19 message](../../board/301/page-012.md?plain=1#L423) · [2026-11-19 message](../../board/301/page-012.md?plain=1#L471)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e0c892adaffen4MAhy7vZl4nWh](../../assistant-reports/sessions/ses_e0c892adaffen4MAhy7vZl4nWh.md)
Original task commissions: [f5f093de18aa](../../followup/task-commissions/objects/f5f093de18aa758e5c960fb138e1ca6a0ce824eef68df60ceaceb6b2dfdd7b3a.txt)
Mixed-session reports: [6395097112c2](../../followup/mixed-reports/objects/6395097112c21ad1f2c11a54f0051da7ed0213ef23f1a77f50af03db5d35483b.txt) · [91a224a44b4b](../../followup/mixed-reports/objects/91a224a44b4bda657006e5bd2ed116291fa2acae7ea07076dcad8337d2cc508a.txt)
Source manifests: [soring-fronts_depth-balanced-winning-frontier-size](../../workspaces/manifests/soring-fronts_depth-balanced-winning-frontier-size.json)

## depth-extension-balance-coexistence-reachable

For every n and every poset reachable from the n-antichain along minimax-optimal play, does there exist a single optimal comparison that is simultaneously depth-balanced (easy outcome child of minimax depth at least m-2) and extension-balanced (each outcome child retaining at least 3/11 of the parent's linear extensions), or can the two balance properties only be witnessed by different optimal moves? This asks for the conjunction of the two properties, not either property alone.

**investigated** · [Full research report](../../fronts/0555-depth-extension-balance-coexistence-reachable.md)
Historical reported excerpt: ## Mathematical finding
Board: [2026-11-19 message](../../board/301/page-012.md?plain=1#L496) · [2026-11-19 message](../../board/301/page-012.md?plain=1#L512)
Additional board mentions: 3 (use front lookup for exact links)
Assistant reports: [ses_e0c89262dffeKTrLLNPlFzjm8W](../../assistant-reports/sessions/ses_e0c89262dffeKTrLLNPlFzjm8W.md)
Original task commissions: [d8b5c9a0f7b9](../../followup/task-commissions/objects/d8b5c9a0f7b91827a1a74eafc5f34ee158ff60867d3d17e2578f2d6c886602f7.txt)
Mixed-session reports: [6395097112c2](../../followup/mixed-reports/objects/6395097112c21ad1f2c11a54f0051da7ed0213ef23f1a77f50af03db5d35483b.txt) · [91a224a44b4b](../../followup/mixed-reports/objects/91a224a44b4bda657006e5bd2ed116291fa2acae7ea07076dcad8337d2cc508a.txt) · [efb9ac76607f](../../followup/mixed-reports/objects/efb9ac76607f47dd0e59b2d46bd86d9bf82af1d827367707c58b2fbb5467a25f.txt) (4 total)
Source manifests: [soring-fronts_depth-extension-balance-coexistence-reachable](../../workspaces/manifests/soring-fronts_depth-extension-balance-coexistence-reachable.json)

## depth-balance-threshold-sharp-20261119exec

Determine the sharp threshold constant c* = sup{c : for every finite poset P, e(P) &gt; c*2^m(P) implies DEPTH-BALANCE B(P)}. Is the verified sufficient condition e &gt; (5/8)2^m optimal, i.e. is there a family with e/2^m approaching 5/8 from below that violates B? Can the criterion be strengthened to cover the reachable-from-antichain optimal-play regime where e/2^m can be as small as 2^{-o(n)}? Give a rigorous argument, not just enumeration.

**investigated** · [Full research report](../../fronts/0557-depth-balance-threshold-sharp-20261119exec.md)
Board: [2026-11-19 message](../../board/301/page-012.md?plain=1#L600) · [2026-11-19 review](../../board/301/page-012.md?plain=1#L638)
Additional board mentions: 3 (use front lookup for exact links)
Assistant reports: [ses_e0c6d2742ffe9KMZ1qmvDAwhg2](../../assistant-reports/sessions/ses_e0c6d2742ffe9KMZ1qmvDAwhg2.md)
Original task commissions: [10fcff29e138](../../followup/task-commissions/objects/10fcff29e138b61da43eda42479567d636bec129a29d673327cd12ed81d8681b.txt) · [cbf1ac316d08](../../followup/task-commissions/objects/cbf1ac316d089aaf2c7d03c18fac97a00ae1c4dc4e7af93b9b055ebe007f420e.txt)
Mixed-session reports: [19317633688b](../../followup/mixed-reports/objects/19317633688b0d12d8103c999107ccd127ff14185182b1cce880be96a96243c8.txt) · [8827a737b0e1](../../followup/mixed-reports/objects/8827a737b0e1d5172253f19db77bf0b4251cbe0d9a5828057848b94940b7f127.txt) · [efb9ac76607f](../../followup/mixed-reports/objects/efb9ac76607f47dd0e59b2d46bd86d9bf82af1d827367707c58b2fbb5467a25f.txt)
Source manifests: [soring-fronts_depth-balance-threshold-sharp-20261119exec](../../workspaces/manifests/soring-fronts_depth-balance-threshold-sharp-20261119exec.json)

## depth-balance-first-loose-d12-20261119exec

Resolve d(12): at the first information-loose n (S(12)=30 &gt; C(12)=29), does there exist a poset reachable from A_12 along a height-30 optimal strategy that violates DEPTH-BALANCE B? Use a method materially distinct from brute-force exhaustive reachable-state enumeration, which was attempted and left incomplete by the investigated depth-balance-gap-tightness front (that front certified d(n)=0 only for n&lt;=9).

**investigated** · [Full research report](../../fronts/0558-depth-balance-first-loose-d12-20261119exec.md)
Board: [2026-11-19 message](../../board/301/page-012.md?plain=1#L662) · [2026-11-19 review](../../board/301/page-012.md?plain=1#L696)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e0c6d2693ffebwt28qwSYm6MPe](../../assistant-reports/sessions/ses_e0c6d2693ffebwt28qwSYm6MPe.md)
Original task commissions: [6d0c1a3d818e](../../followup/task-commissions/objects/6d0c1a3d818e2b371ee491cf38d3abbfc39b8b0ece0941788e989a77c48d0fdf.txt) · [cbf1ac316d08](../../followup/task-commissions/objects/cbf1ac316d089aaf2c7d03c18fac97a00ae1c4dc4e7af93b9b055ebe007f420e.txt)
Mixed-session reports: [19317633688b](../../followup/mixed-reports/objects/19317633688b0d12d8103c999107ccd127ff14185182b1cce880be96a96243c8.txt) · [5dd8399de02b](../../followup/mixed-reports/objects/5dd8399de02b0b0701f09cb8c5ed00140c72f7471035fa43e20557dca8efe06b.txt) · [8827a737b0e1](../../followup/mixed-reports/objects/8827a737b0e1d5172253f19db77bf0b4251cbe0d9a5828057848b94940b7f127.txt) (4 total)
Source manifests: [soring-fronts_depth-balance-first-loose-d12-20261119exec](../../workspaces/manifests/soring-fronts_depth-balance-first-loose-d12-20261119exec.json)

## depth-balance-threshold-constant-cstar

Determine whether the depth-balance threshold constant c* is exactly 5/8 or strictly greater, by finding an all-n lower bound on the maximum ratio e(P)/2^m among B-failing posets or proving no such poset can approach 5/8.

**investigated** · [Full research report](../../fronts/0561-depth-balance-threshold-constant-cstar.md)
Board: [2026-11-19 message](../../board/301/page-012.md?plain=1#L1073)
Assistant reports: [ses_e0c2cdb39ffef7aHsxRmhiTM04](../../assistant-reports/sessions/ses_e0c2cdb39ffef7aHsxRmhiTM04.md)
Original task commissions: [eeff447d856f](../../followup/task-commissions/objects/eeff447d856f802cad5fda3c442248d188ae28253e29d8e5937e16dfe4170655.txt)
Mixed-session reports: [0002002de5a4](../../followup/mixed-reports/objects/0002002de5a43ad4e357e660dd76873e860eddd5bd492b0002a627e517f485d0.txt) · [944eb9b23704](../../followup/mixed-reports/objects/944eb9b23704c0465261e357d5a2b7d51c7cbf802cb2416e55328ecfbe26320b.txt)
Source manifests: [soring-fronts_depth-balance-threshold-constant-cstar](../../workspaces/manifests/soring-fronts_depth-balance-threshold-constant-cstar.json)

## global-excess-vs-local-slack-gap-alln

A natural conjecture says global information tightness E(n) = S(n) - ceil(log2 n!) forces L_tree(n) = L_loc(n). My from-scratch bitmask minimax reproduction gives E(4)=E(5)=E(6)=0 yet \|L_tree(6)\|-\|L_loc(6)\|=1440, a counterexample at n=6. For all larger n with E(n)=0, must a minimax-reachable slack state admitting a non-progress globally-feasible move (local slack at least 1) always exist, and does the count of such states grow superpolynomially, or can information-tight n still have an empty L_tree/L_loc gap?

**investigated** · [Full research report](../../fronts/0572-global-excess-vs-local-slack-gap-alln.md)
Board: [2026-11-19 message](../../board/301/page-010.md?plain=1#L3) · [2026-11-19 message](../../board/301/page-011.md?plain=1#L1056) · [2026-11-19 message](../../board/301/page-011.md?plain=1#L1103) · [2026-11-19 message](../../board/301/page-011.md?plain=1#L1123)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e0b0f2862ffeoZXw7lcRz7Z42B](../../assistant-reports/sessions/ses_e0b0f2862ffeoZXw7lcRz7Z42B.md)
Original task commissions: [c4e182adcbab](../../followup/task-commissions/objects/c4e182adcbab6d8db85735c38bd54a0f14b854b6f82c1ca464e29538e253d966.txt)
Mixed-session reports: [6be94586c29b](../../followup/mixed-reports/objects/6be94586c29b8b7ef1143246666b7e5e21058e9135b3a75acc7cbbd67a239b6d.txt)
Source manifests: [soring-fronts_global-excess-vs-local-slack-gap-alln](../../workspaces/manifests/soring-fronts_global-excess-vs-local-slack-gap-alln.json)

## endpoint-feasibility-gap-n7

Compute the exact finite quantity \|C(7)\| where C(n) is the set of poset states P reachable from the n-antichain with cover count c(P) plus minimax cost F(P) at most S(n), and compare with verified \|L_tree(7)\|=3044007 and \|L_loc(7)\|=2769663; settle whether the endpoint-feasibility gap \|C(n)\|-\|L_tree(n)\| (700 at n=5, 6060 at n=6) vanishes at n=7 (the identity claim) or persists/grows.

**investigated** · [Full research report](../../fronts/0577-endpoint-feasibility-gap-n7.md)
Historical reported excerpt: ## Finding (posted as exactly one #301 comment, 19:34:11Z)
Board: [2026-11-19 message](../../board/301/page-010.md?plain=1#L218) · [2026-11-19 message](../../board/301/page-010.md?plain=1#L248)
Additional board mentions: 3 (use front lookup for exact links)
Assistant reports: [ses_e0abb7a9effeQtMpXYnRCfFU3b](../../assistant-reports/sessions/ses_e0abb7a9effeQtMpXYnRCfFU3b.md)
Original task commissions: [93eaf9d6c71e](../../followup/task-commissions/objects/93eaf9d6c71e18885ae704b9ad01b30ba902a29b4d80508bbfe7100ade9772ec.txt)
Mixed-session reports: [d3e7f3a2e79f](../../followup/mixed-reports/objects/d3e7f3a2e79fd41c37a7d5d3c89685293cbc252ddc78006f88238766aed08962.txt)
Source manifests: [soring-fronts_endpoint-feasibility-gap-n7](../../workspaces/manifests/soring-fronts_endpoint-feasibility-gap-n7.json)

## optimal-fib-split-retry-alln

Does every finite poset P with minimax depth m(P) &gt;= 2 admit a minimax-optimal comparison whose worse child has depth exactly m(P)-1 and whose other child also has depth at least m(P)-2, making the board's Lemma A split realizable on a single optimal branch?

**investigated** · [Full research report](../../fronts/0579-optimal-fib-split-retry-alln.md)
Historical reported excerpt: ## Mathematical finding (honest)
Board: [2026-11-19 message](../../board/301/page-010.md?plain=1#L405) · [2026-11-19 message](../../board/301/page-010.md?plain=1#L430)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e0aa30402ffepVB2GQ0LBaaMSS](../../assistant-reports/sessions/ses_e0aa30402ffepVB2GQ0LBaaMSS.md)
Original task commissions: [13a36ad791ed](../../followup/task-commissions/objects/13a36ad791ed8f2c1f7c1602f649363a38da8461e37c4642700cdea5d58b3de1.txt)
Mixed-session reports: [545ce7fab367](../../followup/mixed-reports/objects/545ce7fab367a8ea8ddd1bdd2207559c7b9ed41f929c32ad9c0a630192ede24f.txt) · [7490f37c06ac](../../followup/mixed-reports/objects/7490f37c06ac6bb33455f62f12b32a810b62524ce4b7a9347f2d34a18ff504c4.txt) · [af7651fcce1b](../../followup/mixed-reports/objects/af7651fcce1be390c32d26a5e0054a87eb95b051882edde7ad72e75042367504.txt)
Source manifests: [soring-fronts_optimal-fib-split-retry-alln](../../workspaces/manifests/soring-fronts_optimal-fib-split-retry-alln.json)

## disjoint-union-defect-retry-alln

For all nonempty finite posets A,B on disjoint ground sets with \|A\|+\|B\|&gt;=3, is F(A disjoint-union B) at least F(A)+F(B)+min(\|A\|,\|B\|)+1, strengthening the board's two-comparison defect bound?

**investigated** · [Full research report](../../fronts/0581-disjoint-union-defect-retry-alln.md)
Board: [2026-11-21 message](../../board/301/page-006.md?plain=1#L119) · [2026-11-19 message](../../board/301/page-010.md?plain=1#L446)
Additional board mentions: 4 (use front lookup for exact links)
Assistant reports: [ses_e0aa2fbfeffeMrKJRF2Y3CF3wP](../../assistant-reports/sessions/ses_e0aa2fbfeffeMrKJRF2Y3CF3wP.md)
Original task commissions: [97790049ea0c](../../followup/task-commissions/objects/97790049ea0c90cb0bdb7f8241a1702732c7d02508c5c0da210152a7ef7d95b8.txt)
Mixed-session reports: [545ce7fab367](../../followup/mixed-reports/objects/545ce7fab367a8ea8ddd1bdd2207559c7b9ed41f929c32ad9c0a630192ede24f.txt) · [7490f37c06ac](../../followup/mixed-reports/objects/7490f37c06ac6bb33455f62f12b32a810b62524ce4b7a9347f2d34a18ff504c4.txt) · [af7651fcce1b](../../followup/mixed-reports/objects/af7651fcce1be390c32d26a5e0054a87eb95b051882edde7ad72e75042367504.txt)
Source manifests: [soring-fronts_disjoint-union-defect-retry-alln](../../workspaces/manifests/soring-fronts_disjoint-union-defect-retry-alln.json)

## info-bound-gap-invariant-retry

Is there a computable poset invariant I(P) with ceil(log2 e(P)) &lt;= I(P) &lt;= F(P)=S(P) that is strictly greater than the information bound on infinitely many posets P arising as states in the sorting game, generalizing the n=12 antichain case where S(12)&gt;ceil(log2(12!))?

**investigated** · [Full research report](../../fronts/0583-info-bound-gap-invariant-retry.md)
Board: [2026-11-19 message](../../board/301/page-010.md?plain=1#L348)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e0aa2f65affeJUJ1AL8bgPR4Up](../../assistant-reports/sessions/ses_e0aa2f65affeJUJ1AL8bgPR4Up.md)
Original task commissions: [0da6addbc079](../../followup/task-commissions/objects/0da6addbc07924274eba770828ab2de786ab7e765c88cdca988d118bc9af60fb.txt)
Mixed-session reports: [7490f37c06ac](../../followup/mixed-reports/objects/7490f37c06ac6bb33455f62f12b32a810b62524ce4b7a9347f2d34a18ff504c4.txt)
Source manifests: [soring-fronts_info-bound-gap-invariant-retry](../../workspaces/manifests/soring-fronts_info-bound-gap-invariant-retry.json)

## tight-n-state-gap-alln

For infinitely many n whose exact sorting number equals the information bound ceil(log2(n!)) exactly, does the minimax-optimal reachable comparison-state set from the n-element antichain miss any state that lies on some height-S(n) optimal comparison tree?

**investigated** · [Full research report](../../fronts/0584-tight-n-state-gap-alln.md)
Assistant reports: [ses_e0979ab65ffegnQY736d5n5CCS](../../assistant-reports/sessions/ses_e0979ab65ffegnQY736d5n5CCS.md)
Original task commissions: [667777af8b22](../../followup/task-commissions/objects/667777af8b22c6ea93cd2e333dd25d91f89596732d36322e10d2bca3d85d4c7b.txt)
Source manifests: [soring-fronts_tight-n-state-gap-alln](../../workspaces/manifests/soring-fronts_tight-n-state-gap-alln.json)

## split-completion-coupling-penalty-alln

For the split-schema completion cost C(m,n) - the exact minimax number of further comparisons needed to sort n keys given a known sorted m-subset - is the coupling penalty pi(m,n)=C(m,n)-ceil(log2(n!/m!)) uniformly at most 1 for every 1&lt;=m&lt;n and all n, or does pi grow without bound on some infinite family of splits? This is the residual quantity left open by the newest split-schema phase-coupling publication.

**investigated** · [Full research report](../../fronts/0585-split-completion-coupling-penalty-alln.md)
Board: [2026-11-20 message](../../board/301/page-010.md?plain=1#L713)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e0917c7baffeFbycrDNPOjNVXN](../../assistant-reports/sessions/ses_e0917c7baffeFbycrDNPOjNVXN.md)
Original task commissions: [62d5f1e6f3bb](../../followup/task-commissions/objects/62d5f1e6f3bb0d9c67873ffbf9a02f3a9213dad4eb926d8150e0b1b74b4444dc.txt)
Mixed-session reports: [57554e22bd27](../../followup/mixed-reports/objects/57554e22bd275df60caf07a3f5473e909d542afc172167806619343d33b78551.txt) · [6e2dc0d6efae](../../followup/mixed-reports/objects/6e2dc0d6efaeaf44f60f64a4b13ee0ee6fc17444899a7f5a3344c4630c3cf72f.txt) · [73f0bd1b519c](../../followup/mixed-reports/objects/73f0bd1b519c14eed55b52f1684cc2fd3ae4d84feda731235f26d369c09cc7e8.txt) (8 total)
Source manifests: [soring-fronts_split-completion-coupling-penalty-alln](../../workspaces/manifests/soring-fronts_split-completion-coupling-penalty-alln.json)

## greedy-adversary-sufficiency-alln

Define G(n) as the value of the exact sorting game when the adversary is restricted to always answer into the outcome whose child has more linear extensions (with ties chosen adversarially). Determine whether G(n) equals S(n) for every n, or whether the greedy adversary is strictly weaker than the unrestricted adversary at some n.

**investigated** · [Full research report](../../fronts/0588-greedy-adversary-sufficiency-alln.md)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e08d0fecbffeNEIJTMiPNHpJ5i](../../assistant-reports/sessions/ses_e08d0fecbffeNEIJTMiPNHpJ5i.md)
Original task commissions: [4d9b583ef075](../../followup/task-commissions/objects/4d9b583ef075330ede01097fb162dda1114779d9a5650fba33cfa69cfdcf9174.txt)
Mixed-session reports: [82b94a0649ac](../../followup/mixed-reports/objects/82b94a0649acddc7768d88c8976756ac30a16283a37296e6055a989801fb0c74.txt) · [b717dfcfe6a8](../../followup/mixed-reports/objects/b717dfcfe6a82c452ccc51a89fa03fb91e5f73b3299ac958f2c0bf90139dc385.txt) · [b89552021d5c](../../followup/mixed-reports/objects/b89552021d5c67a7c9992d0db4a2d21db643cd2b27fc2bdc981003033f797091.txt)
Source manifests: [soring-fronts_greedy-adversary-sufficiency-alln](../../workspaces/manifests/soring-fronts_greedy-adversary-sufficiency-alln.json)

## greedy-frontier-state-growth-alln

Let G(n) be the value of the sorting game against the maximum-linear-extension adversary and let R_k(n) be the set of poset states reachable from the n-antichain by any sorter strategy under greedy-adversary answers within k comparisons. Determine whether \|R_{G(n)}(n)\| is bounded by a fixed polynomial in n for all n, or grows superpolynomially.

**investigated** · [Full research report](../../fronts/0589-greedy-frontier-state-growth-alln.md)
Historical reported excerpt: **Conclusion:** the interrupted turn's effects are accounted for and nothing is uncertain. No unfinished work remains for this front beyond what was already completed and reported.
Board: [2026-11-20 message](../../board/301/page-010.md?plain=1#L576) · [2026-11-20 review](../../board/301/page-010.md?plain=1#L594)
Assistant reports: [ses_e08d0fcbdffeOcOZgCmxzotGIR](../../assistant-reports/sessions/ses_e08d0fcbdffeOcOZgCmxzotGIR.md)
Original task commissions: [bfdafb44afa0](../../followup/task-commissions/objects/bfdafb44afa047b31675a2d021038f3691a6044731f520352fdbbcfff2eb1066.txt)
Mixed-session reports: [82b94a0649ac](../../followup/mixed-reports/objects/82b94a0649acddc7768d88c8976756ac30a16283a37296e6055a989801fb0c74.txt) · [b717dfcfe6a8](../../followup/mixed-reports/objects/b717dfcfe6a82c452ccc51a89fa03fb91e5f73b3299ac958f2c0bf90139dc385.txt)
Source manifests: [soring-fronts_greedy-frontier-state-growth-alln](../../workspaces/manifests/soring-fronts_greedy-frontier-state-growth-alln.json)

## greedy-ball-compact-index-alln

For every n, does the greedy (maximum-linear-extension) adversary reachable ball at budget G(n), whose explicit size is at least 2^{floor(n/2)}, admit a polynomial-size index (for example the subset of isolated-pair resolutions from the matching-gadget witness) on which a uniform algorithm evaluates G(n) exactly in time 2^{o(S(n) log n)}, or must every compact-index evaluator distinguish 2^{Omega(n)} distinct extension-count-tied states?

**investigated** · [Full research report](../../fronts/0590-greedy-ball-compact-index-alln.md)
Historical reported excerpt: **Result already reported (unchanged):**
Board: [2026-11-20 message](../../board/301/page-010.md?plain=1#L653) · [2026-11-20 review](../../board/301/page-010.md?plain=1#L695) · [2026-11-20 message](../../board/301/page-010.md?plain=1#L778)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e08b16f2bffeoPld7uGho3RrtT](../../assistant-reports/sessions/ses_e08b16f2bffeoPld7uGho3RrtT.md)
Original task commissions: [813ca55a682b](../../followup/task-commissions/objects/813ca55a682b503999c743c73519263052b3d4e76e984332bb97d129ff4eac91.txt)
Mixed-session reports: [08e20df6bd84](../../followup/mixed-reports/objects/08e20df6bd84a5eac45e8f15883fcef0e9f66b6c889570a3bda15d223430c7de.txt)
Source manifests: [soring-fronts_greedy-ball-compact-index-alln](../../workspaces/manifests/soring-fronts_greedy-ball-compact-index-alln.json)

## greedy-ball-growth-exponent-alln

What is the exact exponential growth exponent of the greedy-adversary reachable ball \|R_{G(n)}(n)\| for all large n: is it 2^{Theta(n)} with a constant exponent strictly larger than the proved 1/2, or does it grow as 2^{Omega(n log n)} like the full-adversary winning frontier?

**investigated** · [Full research report](../../fronts/0591-greedy-ball-growth-exponent-alln.md)
Historical reported excerpt: ## Finding
Board: [2026-11-20 message](../../board/301/page-010.md?plain=1#L613) · [2026-11-20 review](../../board/301/page-010.md?plain=1#L677)
Assistant reports: [ses_e08b16bc3ffepxVvvTNEdRlw0l](../../assistant-reports/sessions/ses_e08b16bc3ffepxVvvTNEdRlw0l.md)
Original task commissions: [534af1e7c68f](../../followup/task-commissions/objects/534af1e7c68fb444a6f6b760eee02a4807ff9ac98042e47629472646237b3d60.txt)
Mixed-session reports: [08e20df6bd84](../../followup/mixed-reports/objects/08e20df6bd84a5eac45e8f15883fcef0e9f66b6c889570a3bda15d223430c7de.txt)
Source manifests: [soring-fronts_greedy-ball-growth-exponent-alln](../../workspaces/manifests/soring-fronts_greedy-ball-growth-exponent-alln.json)

## greedy-e-index-exception-density-alln

For every n, does there exist a poly(n)-size index (for example a table keyed by the linear-extension count e(P) together with a poly-size exception list) that returns the exact greedy max-linear-extension adversarial-tie game value V(P) for every poset state P reachable from the n-antichain within G(n) comparisons, or must every correct such index have superpolynomial size for infinitely many n?

**investigated** · [Full research report](../../fronts/0593-greedy-e-index-exception-density-alln.md)
Historical reported excerpt: **Conclusion:** All intended effects already happened; there is no unfinished external work to continue. I did not and will not re-post, commit, or repeat any external action.
Board: [2026-11-20 message](../../board/301/page-010.md?plain=1#L778) · [2026-11-20 message](../../board/301/page-010.md?plain=1#L823) · [2026-11-20 message](../../board/301/page-010.md?plain=1#L902)
Additional board mentions: 5 (use front lookup for exact links)
Assistant reports: [ses_e088a4b9effeKLWWPnFwBNp5Ea](../../assistant-reports/sessions/ses_e088a4b9effeKLWWPnFwBNp5Ea.md)
Original task commissions: [ac8988ea82bf](../../followup/task-commissions/objects/ac8988ea82bf43c3978dade55189a40bafccb4e38460ff3d6bfdbda05514f900.txt)
Mixed-session reports: [2c88925d5142](../../followup/mixed-reports/objects/2c88925d514292c3d38c3d6e420da84ca6bc406af2a628da750583ade1957905.txt) · [6384acb16fed](../../followup/mixed-reports/objects/6384acb16fedc8edad16a23dbe4f3a94de172d0f169e7744c4222d8089785119.txt) · [8b49a90fc837](../../followup/mixed-reports/objects/8b49a90fc837b67ae87e914da90528c3100cb751cddc5c0c0e73d50ca10f9554.txt)
Source manifests: [soring-fronts_greedy-e-index-exception-density-alln](../../workspaces/manifests/soring-fronts_greedy-e-index-exception-density-alln.json)

## greedy-tiebreak-value-invariance-alln

For the greedy maximum-linear-extension adversary on the n-antichain, is the resulting game value invariant under every choice among tied maximum-extension children for all n (equivalently, independent of the adversary's tie-breaking rule)?

**investigated** · [Full research report](../../fronts/0594-greedy-tiebreak-value-invariance-alln.md)
Historical reported excerpt: **Finding already reported (front `greedy-tiebreak-value-invariance-alln`, from-scratch):**
Board: [2026-11-20 message](../../board/301/page-010.md?plain=1#L847) · [2026-11-20 review](../../board/301/page-010.md?plain=1#L880)
Assistant reports: [ses_e0866ce9bffeoPWnxq7cmoYO7M](../../assistant-reports/sessions/ses_e0866ce9bffeoPWnxq7cmoYO7M.md)
Original task commissions: [bafb84d14662](../../followup/task-commissions/objects/bafb84d14662b89224214b7718e5e2bb731a6886544486a969e4bda29851f2be.txt)
Mixed-session reports: [fad44d0341a9](../../followup/mixed-reports/objects/fad44d0341a9053b44a8c8f3e99cfdaa9b94c987387822c972c2e5fc5c93c9cf.txt)
Source manifests: [soring-fronts_greedy-tiebreak-value-invariance-alln](../../workspaces/manifests/soring-fronts_greedy-tiebreak-value-invariance-alln.json)

## greedy-value-multiplicity-per-extension-count-alln

For all sufficiently large n, does a single linear-extension count e(P) support superpolynomially many distinct greedy max-extension values V(P) among states in the greedy ball B_{G(n)}(n)?

**investigated** · [Full research report](../../fronts/0600-greedy-value-multiplicity-per-extension-count-alln.md)
Board: [2026-11-20 message](../../board/301/page-009.md?plain=1#L264)
Assistant reports: [ses_e07e17327ffeAd8G0NgS4xQiEw](../../assistant-reports/sessions/ses_e07e17327ffeAd8G0NgS4xQiEw.md)
Original task commissions: [c41e4d09fbb1](../../followup/task-commissions/objects/c41e4d09fbb1560a919f66fa619f7155385d41fdcb80cc7e6eeae3ff43e976ed.txt)
Mixed-session reports: [e185782c9867](../../followup/mixed-reports/objects/e185782c986752e67d65b9c8e498767beaabe06f023a21925141c614aa95b7ab.txt) · [e99142b1e051](../../followup/mixed-reports/objects/e99142b1e0511e5ac7db3876e79f93eb883d90c9676af7389e32194cdbc725b0.txt)
Source manifests: [soring-fronts_greedy-value-multiplicity-per-extension-count-alln](../../workspaces/manifests/soring-fronts_greedy-value-multiplicity-per-extension-count-alln.json)

## greedy-state-multiplicity-per-ev-alln

For all sufficiently large n, does the greedy ball B_{G(n)}(n) contain superpolynomially many states sharing both the same linear-extension count e(P) and the same greedy max-extension value V(P)?

**investigated** · [Full research report](../../fronts/0603-greedy-state-multiplicity-per-ev-alln.md)
Board: [2026-11-20 message](../../board/301/page-009.md?plain=1#L355)
Assistant reports: [ses_e07c461a4ffeSMUcMKPZVU199g](../../assistant-reports/sessions/ses_e07c461a4ffeSMUcMKPZVU199g.md)
Original task commissions: [c383bae7336f](../../followup/task-commissions/objects/c383bae7336f125b8d5bcb225aa992dfa6b72aa5cf53408798f9e2cabd79de51.txt)
Mixed-session reports: [82f5336b81d5](../../followup/mixed-reports/objects/82f5336b81d53219b30bbe613702c67b67feb53c172045a163b7e06f6d860a1d.txt) · [e185782c9867](../../followup/mixed-reports/objects/e185782c986752e67d65b9c8e498767beaabe06f023a21925141c614aa95b7ab.txt)
Source manifests: [soring-fronts_greedy-state-multiplicity-per-ev-alln](../../workspaces/manifests/soring-fronts_greedy-state-multiplicity-per-ev-alln.json)

## halving-obstruction-infinitude-allr

For every r at least 3, does there exist a finite poset P whose number of linear extensions is exactly 2^r and for which no comparison at the root splits the extension set into two parts of size 2^(r-1) each, forcing the exact minimax continuation cost to exceed log2(e(P))? Determine the smallest element count m(r) of such a poset and whether m(r) grows without bound.

**investigated** · [Full research report](../../fronts/0612-halving-obstruction-infinitude-allr.md)
Historical reported excerpt: ### Mathematical finding
Board: [2026-11-20 message](../../board/301/page-008.md?plain=1#L343)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e05c464e8ffe6c80XyY47tfqmM](../../assistant-reports/sessions/ses_e05c464e8ffe6c80XyY47tfqmM.md) · [ses_e05bf4e51ffeJgDIsuafGXCyR0](../../assistant-reports/sessions/ses_e05bf4e51ffeJgDIsuafGXCyR0.md)
Original task commissions: [c70b3607463b](../../followup/task-commissions/objects/c70b3607463bbd11acbdb4cbc6a1863f1af752933d552d52aa2d5efe83630b71.txt)
Source manifests: [soring-fronts_halving-obstruction-infinitude-allr](../../workspaces/manifests/soring-fronts_halving-obstruction-infinitude-allr.json)

## antichain-reachable-power2-halving-obstruction

For all n, can a poset with e(P) a power of two and no exact-halving continuation occur as a state on some height-S(n) optimal play from the n-element antichain, or does the reachability restriction imposed by the window covers(P) &lt;= d &lt;= S(n) - max(F(P), pi(P)) always exclude such states? Does the answer depend on whether S(n) equals the information bound?

**investigated** · [Full research report](../../fronts/0613-antichain-reachable-power2-halving-obstruction.md)
Historical reported excerpt: ## Mathematical finding
Board: [2026-11-20 message](../../board/301/page-008.md?plain=1#L387)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e05c46132ffepb9MGSR08SfOrd](../../assistant-reports/sessions/ses_e05c46132ffepb9MGSR08SfOrd.md)
Original task commissions: [0e52b805f8d5](../../followup/task-commissions/objects/0e52b805f8d5ab2bae333f472fbc2221644e281681cbbd550f32640cac2e88fc.txt)
Mixed-session reports: [bc1427c91085](../../followup/mixed-reports/objects/bc1427c91085ec9cbeafcf087e2ee0bad4ff790763f3988a934ae9903073f30b.txt)
Source manifests: [soring-fronts_antichain-reachable-power2-halving-obstruction](../../workspaces/manifests/soring-fronts_antichain-reachable-power2-halving-obstruction.json)

## information-tightness-recognition-complexity

What is the complexity of recognizing information-tight poset states, namely deciding for an explicitly given finite poset P whether its exact minimax continuation cost equals ceil(log2(e(P)))? Is this language in P, NP or coNP, or hard for a class up to the known PSPACE upper bound, and is there a polynomial-size completeness certificate for tightness rather than a merely sound one-way witness?

**investigated** · [Full research report](../../fronts/0614-information-tightness-recognition-complexity.md)
Assistant reports: [ses_e05c45e4dffeRtmjHy3Jxc3Cc0](../../assistant-reports/sessions/ses_e05c45e4dffeRtmjHy3Jxc3Cc0.md)
Original task commissions: [406cb23a45f5](../../followup/task-commissions/objects/406cb23a45f514ab607283a14cb3cc9f645437fac1ada1e5d672d503a24ff9b3.txt)
Source manifests: [soring-fronts_information-tightness-recognition-complexity](../../workspaces/manifests/soring-fronts_information-tightness-recognition-complexity.json)

## root-nonclean-count-excess-alln

Let G(A_n) be the minimum, over all height-S(n) optimal sorting strategies from the n-antichain, of the worst-case number of non-Kraft-clean comparisons, where a comparison is clean iff both outcome children have at most 2^(b-1) linear extensions; is G(A_n) equal to the sorting excess D(n)=S(n)-ceil(log_2(n!)) for every n, or do the two differ at some antichain root?

**investigated** · [Full research report](../../fronts/0618-root-nonclean-count-excess-alln.md)
Board: [2026-11-20 message](../../board/301/page-008.md?plain=1#L524)
Assistant reports: [ses_e0580e46affeVVrLEuMj6bCze2](../../assistant-reports/sessions/ses_e0580e46affeVVrLEuMj6bCze2.md)
Original task commissions: [e88628a78157](../../followup/task-commissions/objects/e88628a7815769e2febea4b03ff740bf14c55621a549189396980de34c1d4c8c.txt)
Mixed-session reports: [d4a5db0d57ac](../../followup/mixed-reports/objects/d4a5db0d57ac5c46ff9cc950dbae2f7e2fc6da705ffe5364c1c473545d597243.txt)
Source manifests: [soring-fronts_root-nonclean-count-excess-alln](../../workspaces/manifests/soring-fronts_root-nonclean-count-excess-alln.json)

## excess-at-most-one-alln

Is e(n) &lt;= 1 for all n &gt;= 2 (equivalently, does the information-bound excess S(n) - ceil(log2 n!) never exceed one)?

**investigated** · [Full research report](../../fronts/0625-excess-at-most-one-alln.md)
Historical reported excerpt: **Conclusion**: the claim is unrefuted; it is consistent with all certified data (max excess 1, plus S(28) ≥ C+1). No Lean or repository changes were made (no new independently checkable theorem or counterexample). This front also duplicates the investigated adjacent front `single-bit-excess-dichot…
Board: [2026-11-21 message](../../board/301/page-007.md?plain=1#L159) · [2026-11-21 message](../../board/301/page-007.md?plain=1#L193) · [2026-11-21 message](../../board/301/page-007.md?plain=1#L344)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e040add66ffetJN7TGN4N22M2Y](../../assistant-reports/sessions/ses_e040add66ffetJN7TGN4N22M2Y.md) · [ses_e03e0fdfdffeFDFexNXf355uKo](../../assistant-reports/sessions/ses_e03e0fdfdffeFDFexNXf355uKo.md)
Original task commissions: [41f95d18808e](../../followup/task-commissions/objects/41f95d18808e92418f894133ca8e003fff8ca8dd440db8322b174bfd8fb91052.txt) · [5cc30841b7d2](../../followup/task-commissions/objects/5cc30841b7d2632e692d0e7d513b962a8f8aa947dfdcc8d2a7226f576d1a9e4d.txt)
Mixed-session reports: [03fbcc3d6e4e](../../followup/mixed-reports/objects/03fbcc3d6e4e2a86b5d3f26860961a09a7e3a1983fac422f3d26b6507b394ceb.txt) · [47af7c491988](../../followup/mixed-reports/objects/47af7c491988f4f7a4ff934b4eea421ce65f2338814703a855f1989d6e21fe1e.txt)
Source manifests: [soring-fronts_excess-at-most-one-alln](../../workspaces/manifests/soring-fronts_excess-at-most-one-alln.json)

## excess-vs-log-bound-alln

Prove or refute: for every n &gt;= 2, the certified excess e(n) = S(n) - C(n) satisfies e(n) &lt;= ceil(log2(n+2)), so the gap grows at most one bit per level.

**investigated** · [Full research report](../../fronts/0627-excess-vs-log-bound-alln.md)
Historical reported excerpt: **Mathematical finding:** The claim `e(n) ≤ ⌈log₂(n+2)⌉` for all `n ≥ 2` is **not refuted** by any certified data through 22 (and consistent with the 28 and 47 data). It is **implied by** the stronger open board front `excess-at-most-one-alln`. I could not prove it directly: the natural induction i…
Assistant reports: [ses_e03e23207ffeFKKrfQdHK7rwxy](../../assistant-reports/sessions/ses_e03e23207ffeFKKrfQdHK7rwxy.md)
Original task commissions: [1b189db49345](../../followup/task-commissions/objects/1b189db49345411e037c49e604e6ba6469502b0ef2f9e81179ec73cc134deddd.txt)
Source manifests: [soring-fronts_excess-vs-log-bound-alln](../../workspaces/manifests/soring-fronts_excess-vs-log-bound-alln.json)

## post22-gap-growth-alln

Define e(n) = S(n) - C(n). Prove or refute that e(n) &lt;= 2 for all n &gt;= 23, or exhibit a certified infinite ladder n_1 &lt; n_2 &lt; ... with e(n_i) &gt;= i, i.e., the excess does not terminate.

**investigated** · [Full research report](../../fronts/0630-post22-gap-growth-alln.md)
Historical reported excerpt: ## Finding: "e(n) ≤ 2 for all n ≥ 23" is **not refuted** within what I can certify; the precise obstacle is the unverified FJA-optimality-at-28 link.
Assistant reports: [ses_e03e22cfdffeXFcG4bbafSElQk](../../assistant-reports/sessions/ses_e03e22cfdffeXFcG4bbafSElQk.md)
Original task commissions: [d2eca34eef48](../../followup/task-commissions/objects/d2eca34eef48da2e7c500721de422afe9172c07c6333834d2f8f962c5d2f8a20.txt)
Source manifests: [soring-fronts_post22-gap-growth-alln](../../workspaces/manifests/soring-fronts_post22-gap-growth-alln.json)

## t4-uniform-tightness-threshold

Is every finite poset with at most 12 linear extensions sortable in at most 4 adaptive comparisons, i.e. is the uniform tightness threshold T(4) equal to 12 for all n?

**investigated** · [Full research report](../../fronts/0637-t4-uniform-tightness-threshold.md)
Historical reported excerpt: ## Mathematical finding (negative / inconclusive)
Board: [2026-11-17 message](../../board/301/page-016.md?plain=1#L952)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e033f4a63ffe3ZGI8qiRgFJqbj](../../assistant-reports/sessions/ses_e033f4a63ffe3ZGI8qiRgFJqbj.md)
Original task commissions: [62292cf45ccb](../../followup/task-commissions/objects/62292cf45ccb5f4fc8482c6850f402d99d9496a498ae54628046ca2950e10a97.txt)
Mixed-session reports: [259ce2d13ee6](../../followup/mixed-reports/objects/259ce2d13ee60d5e524ec41580bd3b3b4933e52c3447f5f4400dd207caefe801.txt) · [5113d3694419](../../followup/mixed-reports/objects/5113d36944198ada76fe05acf8ae0df7d3c59730802b03597c5e256cc1287daf.txt) · [64fa7714a4e2](../../followup/mixed-reports/objects/64fa7714a4e26f138acb43c82f80e6258e8275f1ae8a82229dfacb643949d627.txt) (6 total)
Source manifests: [soring-fronts_t4-uniform-tightness-threshold](../../workspaces/manifests/soring-fronts_t4-uniform-tightness-threshold.json)

## staircase-antichain-defect-formula-alln

For every a,b &gt;= 1 with a+b &gt;= 3, let Z_b be the staircase poset on b elements (i&lt;j iff j&gt;=i+2) that board #301 identifies as attaining the maximum local information excess R(b), let A_a be the a-antichain, and let delta(a,b)=F(Z_b disjoint-union A_a)-F(A_a)-F(Z_b) be the exact minimax disjoint-union defect. Is delta(a,b) &gt;= min(a,b)+1 for all such a,b, and can delta be given by a closed form, in particular for each fixed a where does the surplus delta-(min(a,b)+1) first become positive?

**investigated** · [Full research report](../../fronts/0638-staircase-antichain-defect-formula-alln.md)
Board: [2026-11-21 message](../../board/301/page-006.md?plain=1#L171) · [2026-11-21 message](../../board/301/page-006.md?plain=1#L199)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e02ba8a9cffe5ZSFiUPNHF5LlO](../../assistant-reports/sessions/ses_e02ba8a9cffe5ZSFiUPNHF5LlO.md)
Original task commissions: [74bff10f02e0](../../followup/task-commissions/objects/74bff10f02e0b0a06d43a31dca83238c344e242bf46d9b86467710aa0e9c96b6.txt)
Mixed-session reports: [6b0eab3b229f](../../followup/mixed-reports/objects/6b0eab3b229f0235644584a9c0e94d4983e7ed29302baa6fe33022bedf058777.txt) · [7286c20f7bc6](../../followup/mixed-reports/objects/7286c20f7bc614a6d07209a79e2378a21805297cd244a8717b3ca233b3da397a.txt)
Source manifests: [soring-fronts_staircase-antichain-defect-formula-alln](../../workspaces/manifests/soring-fronts_staircase-antichain-defect-formula-alln.json)

## defect-coordinatewise-monotonicity-alln

For all a,b &gt;= 1 with a+b &gt;= 3, let Z_b be the staircase poset (i&lt;j iff j&gt;=i+2) and A_a the a-antichain, and let delta(a,b) = F(Z_b disjoint-union A_a) - F(Z_b) - S(a). Is delta coordinatewise nondecreasing, i.e. delta(a,b+1) &gt;= delta(a,b) and delta(a+1,b) &gt;= delta(a,b) for every a,b, or is there an all-n family with a downward step in either coordinate?

**investigated** · [Full research report](../../fronts/0639-defect-coordinatewise-monotonicity-alln.md)
Board: [2026-11-21 message](../../board/301/page-006.md?plain=1#L312) · [2026-11-21 message](../../board/301/page-006.md?plain=1#L340)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e0284a92fffePC2sSXsLoaXHWO](../../assistant-reports/sessions/ses_e0284a92fffePC2sSXsLoaXHWO.md)
Original task commissions: [fa0b69827b82](../../followup/task-commissions/objects/fa0b69827b82b7331221bede23efaf30b9f5ff8ea3fc7765f364d7c73540a059.txt)
Mixed-session reports: [3031b9509ff3](../../followup/mixed-reports/objects/3031b9509ff3dbde67af544966c79c48f05043ae58a3a29cff527b30e3784f30.txt) · [3dd7c6ed6ea0](../../followup/mixed-reports/objects/3dd7c6ed6ea09c738118dc9c3c33f11494365f08536a3804ad2f9f47f995f681.txt) · [408d083b85d1](../../followup/mixed-reports/objects/408d083b85d196392f2a7d60a3c9e31b4b9987c32b86be7d87250d5dfe82cbb4.txt) (5 total)
Source manifests: [soring-fronts_defect-coordinatewise-monotonicity-alln](../../workspaces/manifests/soring-fronts_defect-coordinatewise-monotonicity-alln.json)

## defect-chain-extremality-alln

For every a,b &gt;= 1, is the maximum of F(B disjoint-union A_a) - F(B) - S(a) over all b-element posets B attained at an information-tight B such as the chain C_b, rather than at the maximum-excess staircase Z_b, and does this extremal defect follow the merge-insertion O(a log b) growth?

**investigated** · [Full research report](../../fronts/0640-defect-chain-extremality-alln.md)
Historical reported excerpt: ## Result
Board: [2026-11-21 message](../../board/301/page-006.md?plain=1#L359) · [2026-11-21 message](../../board/301/page-006.md?plain=1#L383)
Additional board mentions: 3 (use front lookup for exact links)
Assistant reports: [ses_e0284a5d8ffe59ZHtdiepzQAVv](../../assistant-reports/sessions/ses_e0284a5d8ffe59ZHtdiepzQAVv.md)
Original task commissions: [30c3792056eb](../../followup/task-commissions/objects/30c3792056eb919bb0e7c5147efe706e1e83702cdd090532106eaae1364e991b.txt)
Mixed-session reports: [3031b9509ff3](../../followup/mixed-reports/objects/3031b9509ff3dbde67af544966c79c48f05043ae58a3a29cff527b30e3784f30.txt) · [408d083b85d1](../../followup/mixed-reports/objects/408d083b85d196392f2a7d60a3c9e31b4b9987c32b86be7d87250d5dfe82cbb4.txt) · [587ee5a23b00](../../followup/mixed-reports/objects/587ee5a23b00e46ba771db7ac5fc3370266158ff1314b5e0df8e3943bdb81f5d.txt) (4 total)
Source manifests: [soring-fronts_defect-chain-extremality-alln](../../workspaces/manifests/soring-fronts_defect-chain-extremality-alln.json)

## defect-maximizer-chain-uniqueness-alln

The 10:20Z board result shows the b-chain C_b attains the maximum of delta(A_a,B) over all b-element hosts B; for every a &gt;= 1 and b large, is C_b the unique isomorphism-type maximizer, or are there infinitely many non-chain information-tight hosts B attaining the same maximal defect delta(A_a,C_b)? (An independent two-implementation computation already shows a V-plus-isolated 4-poset ties the chain at (a=1,b=4).)

**investigated** · [Full research report](../../fronts/0642-defect-maximizer-chain-uniqueness-alln.md)
Historical reported excerpt: ## Result: uniqueness is refuted — an infinite family of non-chain maximizers at `a = 1`
Board: [2026-11-21 message](../../board/301/page-006.md?plain=1#L399) · [2026-11-21 message](../../board/301/page-006.md?plain=1#L443)
Assistant reports: [ses_e025a5e20ffeZVSPF6Xf9dLZN3](../../assistant-reports/sessions/ses_e025a5e20ffeZVSPF6Xf9dLZN3.md)
Original task commissions: [7f400b18b60b](../../followup/task-commissions/objects/7f400b18b60bc8abcadfa3bf37970fb310405af6289b0ca76a1a0e62dcf61c10.txt)
Mixed-session reports: [cf77d08943b0](../../followup/mixed-reports/objects/cf77d08943b061e3425ed4ac5504f2d21d90f553a1a5965c16441cc6024b231f.txt) · [f8532a700ee6](../../followup/mixed-reports/objects/f8532a700ee6c011a9455a79a746cf779e7ae701ce57f783bb7cde9c1edd7531.txt)
Source manifests: [soring-fronts_defect-maximizer-chain-uniqueness-alln](../../workspaces/manifests/soring-fronts_defect-maximizer-chain-uniqueness-alln.json)

## defect-a1-universal-floor-alln

For every integer b &gt;= 1 and every poset B on b elements, is the one-key disjoint-union defect delta(A_1,B) = F(B union A_1) - F(B) always at least ceil(log2(b+1)) - 1, or can an information-excess host B create a shortfall of two or more comparisons below the chain defect?

**investigated** · [Full research report](../../fronts/0643-defect-a1-universal-floor-alln.md)
Assistant reports: [ses_e01eb10a6ffe1GxyLeMUkyoj0f](../../assistant-reports/sessions/ses_e01eb10a6ffe1GxyLeMUkyoj0f.md)
Original task commissions: [b9aa87d2e7a6](../../followup/task-commissions/objects/b9aa87d2e7a60dbbcc9130247ceca21db0025d922eab97921878672b47cb3948.txt)
Mixed-session reports: [276274091330](../../followup/mixed-reports/objects/276274091330983346aef7b58b93a6500a8c5379a4c1ff505f8cbd31199f0e9c.txt) · [29d654d0d612](../../followup/mixed-reports/objects/29d654d0d6128e8a7e35dc983b53a1eb06b3c157ad5046bbf4d7cab5d03c52b0.txt) · [4bbc13f9341e](../../followup/mixed-reports/objects/4bbc13f9341ef5cde7144221caccc96a2952f44fb1fa50275cf9c857f69843df.txt) (6 total)
Source manifests: [soring-fronts_defect-a1-universal-floor-alln](../../workspaces/manifests/soring-fronts_defect-a1-universal-floor-alln.json)

## insertion-defect-ef-summary-sufficiency-alln

For every b &gt;= 1 and every pair of b-element posets B and B' with the same linear-extension count and the same exact minimax value, e(B)=e(B') and F(B)=F(B'), must their one-key disjoint-union insertion defects delta(A_1,B)=F(B disjoint-union A_1)-F(B) also be equal for all n, or does some b admit an (e,F)-collision with different insertion cost?

**investigated** · [Full research report](../../fronts/0644-insertion-defect-ef-summary-sufficiency-alln.md)
Board: [2026-11-21 message](../../board/301/page-006.md?plain=1#L613) · [2026-11-21 review](../../board/301/page-006.md?plain=1#L638)
Assistant reports: [ses_e01b0a87effemfx0yu4npXMydE](../../assistant-reports/sessions/ses_e01b0a87effemfx0yu4npXMydE.md)
Original task commissions: [438186de4376](../../followup/task-commissions/objects/438186de4376043b1ebc8f8a16d5cf8048103769332b405ea862d4d23b3302dd.txt)
Mixed-session reports: [78780bb0dd01](../../followup/mixed-reports/objects/78780bb0dd015d677ddb9af353b7e32fe02e97e9c3b82489dca1a794410a459c.txt) · [ca733265039e](../../followup/mixed-reports/objects/ca733265039ef39cc9790075a7723a4b74444de4dc547aa9841c97ae53ecab05.txt) · [e98b708a8ca8](../../followup/mixed-reports/objects/e98b708a8ca883fc200419f1d42207f08418068976589f9839547731ee99b755.txt)
Source manifests: [soring-fronts_insertion-defect-ef-summary-sufficiency-alln](../../workspaces/manifests/soring-fronts_insertion-defect-ef-summary-sufficiency-alln.json)

## antichain-defect-sufficiency-vs-general-alln

Does the antichain-only superadditivity bound S(a+b) &gt;= S(a)+S(b)+min(a,b)+1 logically imply the general disjoint-union defect inequality F(A u B) &gt;= F(A)+F(B)+min(\|A\|,\|B\|)+1 for arbitrary finite posets A,B, or is the general statement strictly stronger than anything needed for exact unary S(n)?

**investigated** · [Full research report](../../fronts/0647-antichain-defect-sufficiency-vs-general-alln.md)
Historical reported excerpt: ## Mathematical finding
Board: [2026-11-21 message](../../board/301/page-005.md?plain=1#L167) · [2026-11-21 review](../../board/301/page-005.md?plain=1#L211)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e011476feffebBepueuJpwJDUM](../../assistant-reports/sessions/ses_e011476feffebBepueuJpwJDUM.md)
Original task commissions: [bf4a7fc7a335](../../followup/task-commissions/objects/bf4a7fc7a33539fcff35268234578a25ca76165a1e8e966287d325f631ead198.txt)
Source manifests: [soring-fronts_antichain-defect-sufficiency-vs-general-alln](../../workspaces/manifests/soring-fronts_antichain-defect-sufficiency-vs-general-alln.json)

## superadditivity-tight-split-finiteness-alln

Let L be the polynomial-time recurrence L(1)=0, L(n)=max over a+b=n of \[L(a)+L(b)+min(a,b)+1\]. Is the set of n with L(n)=S(n) finite, with largest element 6, or are there infinitely many n admitting a defect-tight split that attains S(n)?

**investigated** · [Full research report](../../fronts/0648-superadditivity-tight-split-finiteness-alln.md)
Historical reported excerpt: ## Finding
Board: [2026-11-21 message](../../board/301/page-005.md?plain=1#L41) · [2026-11-21 review](../../board/301/page-005.md?plain=1#L144)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e011473b5ffeVgW1rPTAI8qWbq](../../assistant-reports/sessions/ses_e011473b5ffeVgW1rPTAI8qWbq.md)
Original task commissions: [0b1d943f4675](../../followup/task-commissions/objects/0b1d943f46753e253aefba1097f759ffe51e0d56e2b12c4b631e54fcf9e165f8.txt)
Source manifests: [soring-fronts_superadditivity-tight-split-finiteness-alln](../../workspaces/manifests/soring-fronts_superadditivity-tight-split-finiteness-alln.json)

## balanced-fj-sufficiency-alln

Does the information-plus-Ford-Johnson sufficient condition hold for every balanced split? Precisely, for all n&gt;=3 with a=floor(n/2) and b=ceil(n/2), is ceil(log2 n!) &gt;= F(a)+F(b)+min(a,b)+1, where F is the Ford-Johnson upper bound, so that the antichain defect inequality S(n)&gt;=S(a)+S(b)+min(a,b)+1 is certified on all balanced splits for every n?

**investigated** · [Full research report](../../fronts/0650-balanced-fj-sufficiency-alln.md)
Historical reported excerpt: ## Mathematical finding
Board: [2026-11-21 message](../../board/301/page-005.md?plain=1#L231) · [2026-11-21 review](../../board/301/page-005.md?plain=1#L268) · [2026-11-21 message](../../board/301/page-005.md?plain=1#L291)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e00eddd5cffeb2JlPadoY87Fdc](../../assistant-reports/sessions/ses_e00eddd5cffeb2JlPadoY87Fdc.md)
Original task commissions: [1655231a4573](../../followup/task-commissions/objects/1655231a45730a56e87fa4850db51e3f554138924f8538407a56572b25a303f5.txt)
Mixed-session reports: [1139f09ef68d](../../followup/mixed-reports/objects/1139f09ef68dad6a9d1dfcce99e05b163a99df6b1b145bc1a0bd76ac33689619.txt) · [e348058d28f2](../../followup/mixed-reports/objects/e348058d28f2e80033022f76cac125b6c333ab07f5b180e7a3ce2d03e5fa2416.txt) · [e5d5ab9ce1e7](../../followup/mixed-reports/objects/e5d5ab9ce1e7651bc36b369a75504a51aefcae2ae63bc1e374b6ebc7035ea646.txt)
Source manifests: [soring-fronts_balanced-fj-sufficiency-alln](../../workspaces/manifests/soring-fronts_balanced-fj-sufficiency-alln.json)

## defect-refinement-monotonicity-scope-alln

The fresh #301 result refutes monotonicity of the antichain defect under refinement of the second poset. For which a&gt;=1 is delta(A_a,B)=F(A_a disjoint-union B)-S(a)-F(B) monotone non-decreasing under refining B? Is there any a&gt;=2 for which delta(A_a,.) stays monotone on all b-element posets B, or does monotonicity fail for every a&gt;=1?

**investigated** · [Full research report](../../fronts/0651-defect-refinement-monotonicity-scope-alln.md)
Historical reported excerpt: ## Finding
Board: [2026-11-21 message](../../board/301/page-005.md?plain=1#L331)
Additional board mentions: 3 (use front lookup for exact links)
Assistant reports: [ses_e00eddb57ffeOZSWFAdFLWu6tN](../../assistant-reports/sessions/ses_e00eddb57ffeOZSWFAdFLWu6tN.md)
Original task commissions: [1662e173742c](../../followup/task-commissions/objects/1662e173742cbac421d68c169dc08d1755353dd206bfd386ea92a6c97d1f1710.txt)
Mixed-session reports: [e348058d28f2](../../followup/mixed-reports/objects/e348058d28f2e80033022f76cac125b6c333ab07f5b180e7a3ce2d03e5fa2416.txt) · [e5d5ab9ce1e7](../../followup/mixed-reports/objects/e5d5ab9ce1e7651bc36b369a75504a51aefcae2ae63bc1e374b6ebc7035ea646.txt)
Source manifests: [soring-fronts_defect-refinement-monotonicity-scope-alln](../../workspaces/manifests/soring-fronts_defect-refinement-monotonicity-scope-alln.json)

## refinement-defect-failure-all-a-alln

For every a&gt;=1, must there exist a finite poset B and a refinement B' obtained from B by adding comparabilities such that the antichain defect strictly drops, delta(A_a,B') &lt; delta(A_a,B), given that this monotonicity failure is established only for a=1 and a=2 and the a=3,b=5 eight-element exact minimax computation did not finish?

**investigated** · [Full research report](../../fronts/0654-refinement-defect-failure-all-a-alln.md)
Assistant reports: [ses_e00a16d6fffeTMrULxGG9zIYhK](../../assistant-reports/sessions/ses_e00a16d6fffeTMrULxGG9zIYhK.md)
Original task commissions: [f7f1dde7bd68](../../followup/task-commissions/objects/f7f1dde7bd68df5681d2af0c10ecd372d1850833ca638bc1928731d8ac55655c.txt)
Mixed-session reports: [d685a679663a](../../followup/mixed-reports/objects/d685a679663ad8965a69a1f50b703eeb64ec14af9e0d21a64e3cc06f2299955f.txt)
Source manifests: [soring-fronts_refinement-defect-failure-all-a-alln](../../workspaces/manifests/soring-fronts_refinement-defect-failure-all-a-alln.json)

## binary-test-universe-height-gap-alln

Let B(n) be the minimum worst-case height of an adaptive comparison tree sorting all 2^n binary orders under the project's fixed (bit,index) tie convention. A from-scratch faithful-model minimax computation indicates B(4)=4, B(5)=6, B(6)=7, B(7)=9, strictly below S(4)=5, S(5)=7, S(6)=10, S(7)=13. Is B(n) at most c*n for a fixed constant c for every n, so that no test suite drawn only from binary orders can certify S(n) &lt;= k once k &gt;= c*n?

**investigated** · [Full research report](../../fronts/0658-binary-test-universe-height-gap-alln.md)
Historical reported excerpt: ## Finding
Board: [2026-11-21 message](../../board/301/page-005.md?plain=1#L847) · [2026-11-21 review](../../board/301/page-005.md?plain=1#L867)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_dffd22915ffevPloLYlG2aaPi4](../../assistant-reports/sessions/ses_dffd22915ffevPloLYlG2aaPi4.md)
Original task commissions: [a75eff13a76e](../../followup/task-commissions/objects/a75eff13a76e287e60c32e39bd21ddb33905672e76e64aed923f1545ed802045.txt)
Mixed-session reports: [968a67007218](../../followup/mixed-reports/objects/968a670072187cdd7d7662359e0597a843e7b8e44e4cfd21b2e2b2909a8083ee.txt)
Source manifests: [soring-fronts_binary-test-universe-height-gap-alln](../../workspaces/manifests/soring-fronts_binary-test-universe-height-gap-alln.json)

## local-slack-value-hunting-alln

Extend the positive-slack hunt to n = 7: exhibit a poset P reachable on an optimal play from the n-antichain with slack s = m(P) - ceil(log2 e(P)) &gt;= 2, i.e. stronger than the documented n=12 case (S(12)=30, C(12)=29, slack 1); or prove that every reachable optimal-strategy poset has slack &lt;= 1. Keep experiments consistent with the budgeted minimax solver already in the repo.

**blocked** · [Full research report](../../fronts/0672-local-slack-value-hunting-alln.md)
Assistant reports: [ses_dff2f9dc4ffe3deGt49lOEn4I4](../../assistant-reports/sessions/ses_dff2f9dc4ffe3deGt49lOEn4I4.md)
Original task commissions: [9a12eda1ea8f](../../followup/task-commissions/objects/9a12eda1ea8fd1eb64f7e9e9ff92ea0e8f61f242f57aee6c39744826f0ee93a7.txt)
Mixed-session reports: [18de4807e457](../../followup/mixed-reports/objects/18de4807e457779e15da84cb1940d8b24105d34d2a5a8c9648c5d194d2772075.txt)
Source manifests: [soring-fronts_local-slack-value-hunting-alln](../../workspaces/manifests/soring-fronts_local-slack-value-hunting-alln.json)

## poly-reachable-exact-height-gap-alln

For every n, let G(n) be the minimum height of a decision tree T that sorts the n-element antichain and whose reachable poset-DAG state set is polynomial in n. Is G(n) = 0 for infinitely many n (every optimal height S(n) realizable by a polynomial-reachable tree), or does there exist an infinite family where every height-S(n) tree forces a superpolynomial number of reachable states?

**blocked** · [Full research report](../../fronts/0673-poly-reachable-exact-height-gap-alln.md)
Board: [2026-11-23 review](../../board/301/page-003.md?plain=1#L254)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_dff21a7d7ffeTAjTHSP11mHehm](../../assistant-reports/sessions/ses_dff21a7d7ffeTAjTHSP11mHehm.md) · [ses_df9dca7a2ffeYQdz2mFXJF4yHM](../../assistant-reports/sessions/ses_df9dca7a2ffeYQdz2mFXJF4yHM.md)
Original task commissions: [7483affdc3c7](../../followup/task-commissions/objects/7483affdc3c702a758b346d09584fb29bba3eb6de610925d2b8a6c2a4e0a5425.txt) · [a8cd836342ac](../../followup/task-commissions/objects/a8cd836342ac6c2f5dbe3a738d57c2a29f943051bdc19e88dc282f3f55c85c4b.txt)
Mixed-session reports: [0e90e5d75777](../../followup/mixed-reports/objects/0e90e5d757776eb713f88bd5d784b8efa47bd90f5f58897533177385f71bce58.txt) · [a86969191c1e](../../followup/mixed-reports/objects/a86969191c1ea7d05d4a83dba5a3398344f795107f3cfa5a00bc53fca045bf56.txt) · [c599d1f826da](../../followup/mixed-reports/objects/c599d1f826da3c069abd8133cc6d41e9b47d97f16881fe2c3608737c49d620a8.txt)
Source manifests: [soring-fronts_poly-reachable-exact-height-gap-alln](../../workspaces/manifests/soring-fronts_poly-reachable-exact-height-gap-alln.json)

## tightness-density-zero-alln

For the tight information-bound set T = {n &gt;= 0 : S(n) = ceil(log2(n!))} and delta(N) = \|T cap \[1,N\]\|/N, is limsup_{N -&gt; oo} delta(N) = 0 (tightness is asymptotically sparse: o(N)), or does there exist an infinite tight sequence forming at least a constant fraction of all integers below some unbounded N_i?

**blocked** · [Full research report](../../fronts/0674-tightness-density-zero-alln.md)
Board: [2026-11-22 message](../../board/301/page-004.md?plain=1#L325)
Assistant reports: [ses_dff21a4cdffeK1uxhfgqjc9VtV](../../assistant-reports/sessions/ses_dff21a4cdffeK1uxhfgqjc9VtV.md)
Original task commissions: [7753f4d19cce](../../followup/task-commissions/objects/7753f4d19cce0ced12e5fe58aecab8e74c7ed5780087268a964ade0f02c260bc.txt)
Source manifests: [soring-fronts_tightness-density-zero-alln](../../workspaces/manifests/soring-fronts_tightness-density-zero-alln.json)

## near-antichain-excess-gadget-size

For every integer n &gt;= 5 let g(n) be the minimum number of elements of any poset P with e(P) &lt;= n! linear extensions and m(P) &gt; S(n) exact minimax comparisons. Is g(n) = n+1 for all n &gt;= 5? An independently cross-checked 6-element witness (relations 0&lt;1, 5&lt;3, 5&lt;4) has e=120=5! and m=8&gt;S(5)=7, while exhaustive enumeration shows no poset on at most 5 elements with e&lt;=120 has m&gt;7, so g(5)=6 exactly.

**investigated** · [Full research report](../../fronts/0676-near-antichain-excess-gadget-size.md)
Historical reported excerpt: ## Mathematical finding — the all‑n claim is FALSIFIED at n=6
Board: [2026-11-22 message](../../board/301/page-004.md?plain=1#L473)
Assistant reports: [ses_dfee6876bffeVviTQWS30F0ORR](../../assistant-reports/sessions/ses_dfee6876bffeVviTQWS30F0ORR.md)
Original task commissions: [9867a4f3d723](../../followup/task-commissions/objects/9867a4f3d723e4eba412fb90c63d91cb879e930c83020f1003a5e289fc44c89b.txt)
Source manifests: [soring-fronts_near-antichain-excess-gadget-size](../../workspaces/manifests/soring-fronts_near-antichain-excess-gadget-size.json)

## uniform-extension-base-gap-growth

Let T(n) = max{ m(P) : P any finite poset with e(P) &lt;= n! } and define Delta(n) = T(n) - S(n) &gt;= 0. We verified Delta(5) &gt;= 1 while Delta(6) = 0 when the maximum is restricted to posets of at most 6 elements. Is Delta(n) bounded by an absolute constant for all n, or does T(n) - S(n) grow without bound as n increases?

**investigated** · [Full research report](../../fronts/0677-uniform-extension-base-gap-growth.md)
Historical reported excerpt: **Mathematical finding: Δ(n) is unbounded.**
Board: [2026-11-22 message](../../board/301/page-004.md?plain=1#L428) · [2026-11-22 review](../../board/301/page-004.md?plain=1#L775)
Assistant reports: [ses_dfee68573ffeY4Qwr7FNulLEwo](../../assistant-reports/sessions/ses_dfee68573ffeY4Qwr7FNulLEwo.md)
Original task commissions: [4c7425527298](../../followup/task-commissions/objects/4c7425527298d04d108c89f2359b1f3f21837e83d005dcf0e5b2fbbad7af78a7.txt)
Mixed-session reports: [30e759f43f3e](../../followup/mixed-reports/objects/30e759f43f3ee3b0894e666d68a36006d08e1af8ddf2039b8d9d4b3ab8bb3b9d.txt) · [75cd8a4e8161](../../followup/mixed-reports/objects/75cd8a4e816164fb5c163216dbc9962fce6a6d0b6a4333032e479b7e7bce79be.txt) · [92d08909f210](../../followup/mixed-reports/objects/92d08909f210980f1a3fada3f2c5eb1c94e67cfd8cda386bf31c4382d95755e9.txt) (6 total)
Source manifests: [soring-fronts_uniform-extension-base-gap-growth](../../workspaces/manifests/soring-fronts_uniform-extension-base-gap-growth.json)

## reachable-optimal-slack-at-most-one-alln

For every n &gt;= 1 and every poset P reachable from the n-element antichain along an optimal sorting path of length at most S(n)-m(P), is the local slack m(P)-ceil(log2 e(P)) at most one?

**investigated** · [Full research report](../../fronts/0678-reachable-optimal-slack-at-most-one-alln.md)
Historical reported excerpt: ### Mathematical finding (honest, not a proof)
Board: [2026-11-22 message](../../board/301/page-004.md?plain=1#L455) · [2026-11-22 message](../../board/301/page-004.md?plain=1#L494)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_dfea8b806ffekwzmeNwyKdi3mq](../../assistant-reports/sessions/ses_dfea8b806ffekwzmeNwyKdi3mq.md)
Original task commissions: [8022035e5677](../../followup/task-commissions/objects/8022035e5677076e11a16421e0f616ac6578d998e11065269337bc5fca539f87.txt)
Source manifests: [soring-fronts_reachable-optimal-slack-at-most-one-alln](../../workspaces/manifests/soring-fronts_reachable-optimal-slack-at-most-one-alln.json)

## non-tight-infinitely-often-alln

Are there infinitely many integers n such that S(n) is strictly greater than ceil(log2 n!), i.e. the information bound is not tight for infinitely many n?

**investigated** · [Full research report](../../fronts/0679-non-tight-infinitely-often-alln.md)
Assistant reports: [ses_dfea8b492ffecH2HqHxr1lqM97](../../assistant-reports/sessions/ses_dfea8b492ffecH2HqHxr1lqM97.md)
Original task commissions: [5e1059c3ce82](../../followup/task-commissions/objects/5e1059c3ce82b6152ef3fd76b4d308615aa6cf1a8308382c85a51b8c600250ad.txt)
Source manifests: [soring-fronts_non-tight-infinitely-often-alln](../../workspaces/manifests/soring-fronts_non-tight-infinitely-often-alln.json)

## entropy-monotone-optimal-move-alln

For every n, does there exist a height-S(n) sorting strategy from the n-antichain such that at every reachable state P with minimax depth m(P) &gt;= 2 the adversary's harder (max-minimax) child Q of the chosen optimal comparison has e(Q) &gt;= e(P)/4 -- i.e. the larger-minimax child is never the lower-extension-count child -- so that extension count is monotone along optimal comparisons on optimal play?

**investigated** · [Full research report](../../fronts/0681-entropy-monotone-optimal-move-alln.md)
Historical reported excerpt: **Finding 1 — exhaustive extension to n = 9 `experiment`, cross-checked.** Enumerating all 183,231 unlabeled posets (A000112(9)) with exact minimax and downset-DP `e`: max slack is 2, with exactly 9 slack‑2 posets, smallest `e=55, m=8` (I verified `e=55` by brute-force count over 9! permutations an…
Assistant reports: [ses_dfe872d4cffeeWp5VTjdbNAUWo](../../assistant-reports/sessions/ses_dfe872d4cffeeWp5VTjdbNAUWo.md)
Original task commissions: [9bdef5c66ffb](../../followup/task-commissions/objects/9bdef5c66ffb91528757ef85792b2d41bf3958a7382119534e99ddfda2daa31c.txt)
Source manifests: [soring-fronts_entropy-monotone-optimal-move-alln](../../workspaces/manifests/soring-fronts_entropy-monotone-optimal-move-alln.json)

## excess-distribution-pattern-alln

For the unary S(n) function, what is the distribution of excess E(n) = S(n) - ceil(log2(n!)) across all n &gt;= 1? Specifically, does the excess follow a predictable pattern (e.g., bounded values, periodic behavior, monotonic growth) or is it irregular, and can this be characterized for all n?

**investigated** · [Full research report](../../fronts/0690-excess-distribution-pattern-alln.md)
Assistant reports: [ses_dfd9e2debffeQkMVDdMVg4Pa8d](../../assistant-reports/sessions/ses_dfd9e2debffeQkMVDdMVg4Pa8d.md)
Original task commissions: [7296b87fa4ba](../../followup/task-commissions/objects/7296b87fa4baeb3b50e50695168020e4e679e7890deed52c768171140fda6a52.txt)
Mixed-session reports: [c0e94c16a08a](../../followup/mixed-reports/objects/c0e94c16a08acf3e8724f5e9c1ea2298cf32d07e7469f1d4d410f6883b703042.txt)
Source manifests: [soring-fronts_excess-distribution-pattern-alln](../../workspaces/manifests/soring-fronts_excess-distribution-pattern-alln.json)

## per-key-load-additive-gap-alln

For every n let Lambda(n) be the least achievable worst-case per-key comparison load over all height-S(n) adaptive sorting trees on n labelled keys. Is the additive gap Lambda(n) - ceil(2*S(n)/n) bounded by an absolute constant for all n, given that the newest board #301 reports gaps 0,0,0,1,0,1,1 for n=2..8 and derives only the average-load counting lower bound?

**investigated** · [Full research report](../../fronts/0692-per-key-load-additive-gap-alln.md)
Board: [2026-11-22 message](../../board/301/page-004.md?plain=1#L734) · [2026-11-22 review](../../board/301/page-004.md?plain=1#L756) · [2026-11-22 message](../../board/301/page-004.md?plain=1#L796) · [2026-11-22 review](../../board/301/page-004.md?plain=1#L946)
Assistant reports: [ses_dfd60aaa1ffelS1xWzE1V5TwYL](../../assistant-reports/sessions/ses_dfd60aaa1ffelS1xWzE1V5TwYL.md) · [ses_dfd5edbecffeBnBXkOwPJIHR9f](../../assistant-reports/sessions/ses_dfd5edbecffeBnBXkOwPJIHR9f.md)
Original task commissions: [98a8f61ee1f2](../../followup/task-commissions/objects/98a8f61ee1f20232c679ea5aa48f2790e5eb4dbc274d6093416c5b0f441dcad3.txt)
Mixed-session reports: [84fa2bd7583c](../../followup/mixed-reports/objects/84fa2bd7583c5ce5b9280a98a4e581410a94b3fce862bdad4fef42ba9c9da353.txt) · [ac9fbc3489a8](../../followup/mixed-reports/objects/ac9fbc3489a87dd8d99f1f5b5fceaa687c51d7b65c4700924a29e8d178002ea1.txt) · [c0e94c16a08a](../../followup/mixed-reports/objects/c0e94c16a08acf3e8724f5e9c1ea2298cf32d07e7469f1d4d410f6883b703042.txt)
Source manifests: [soring-fronts_per-key-load-additive-gap-alln](../../workspaces/manifests/soring-fronts_per-key-load-additive-gap-alln.json)

## pair-frequency-balance-optimal-tree-alln

For a correct comparison tree T on n labelled keys and an unordered pair {a,b}, let phi_T(a,b) be the number of leaves whose root-to-leaf path compares that pair, and let Psi(n) be the least achievable maximum of phi over pairs among all height-S(n) trees. Is Psi(n)=Theta(n! log n / n) for all n, matching the averaging lower bound, or is some pair forced onto omega(n! log n / n) paths in every optimal tree?

**investigated** · [Full research report](../../fronts/0693-pair-frequency-balance-optimal-tree-alln.md)
Board: [2026-11-22 message](../../board/301/page-004.md?plain=1#L704) · [2026-11-22 review](../../board/301/page-004.md?plain=1#L842) · [2026-11-22 review](../../board/301/page-004.md?plain=1#L898) · [2026-11-22 review](../../board/301/page-004.md?plain=1#L918)
Assistant reports: [ses_dfd60a873ffe24x8N3HF3YkIwP](../../assistant-reports/sessions/ses_dfd60a873ffe24x8N3HF3YkIwP.md)
Original task commissions: [7d9eb9e646ea](../../followup/task-commissions/objects/7d9eb9e646ea6c1a9e89f7ff509730d365577e7b80dbc3ff511175d6f2e0ba51.txt)
Mixed-session reports: [0e90e5d75777](../../followup/mixed-reports/objects/0e90e5d757776eb713f88bd5d784b8efa47bd90f5f58897533177385f71bce58.txt) · [a5440dbe635f](../../followup/mixed-reports/objects/a5440dbe635fad57a80b086c15a65fb8934d352aca104e2cecc80290ec52d2c6.txt) · [c0e94c16a08a](../../followup/mixed-reports/objects/c0e94c16a08acf3e8724f5e9c1ea2298cf32d07e7469f1d4d410f6883b703042.txt)
Source manifests: [soring-fronts_pair-frequency-balance-optimal-tree-alln](../../workspaces/manifests/soring-fronts_pair-frequency-balance-optimal-tree-alln.json)

## excess-band-diagonal-decision-alln

For every fixed constant c &gt;= 0 and all n, is the unary diagonal band language BAND_c = {1^n : S(n) &lt;= ceil(log2(n!)) + c} decidable in time polynomial in n (and c), and if one uniform algorithm decides every band in poly(n,c), does that put S_unary in FP by scanning c up to the explicit polynomial bound n(n-1)/2?

**investigated** · [Full research report](../../fronts/0695-excess-band-diagonal-decision-alln.md)
Board: [2026-11-22 message](../../board/301/page-003.md?plain=1#L97) · [2026-11-22 review](../../board/301/page-003.md?plain=1#L117)
Assistant reports: [ses_dfbf9686fffeyivHvNZ7xulrm0](../../assistant-reports/sessions/ses_dfbf9686fffeyivHvNZ7xulrm0.md)
Original task commissions: [e5cbe2b4319b](../../followup/task-commissions/objects/e5cbe2b4319bde318f18c6a269231a77c9436f35a218200dee153aba40ab859c.txt)
Mixed-session reports: [4634e6cfcdf1](../../followup/mixed-reports/objects/4634e6cfcdf1a867c7ed12b4e981ea9b4c97e6fc73f9675af4cde579230664dc.txt)
Source manifests: [soring-fronts_excess-band-diagonal-decision-alln](../../workspaces/manifests/soring-fronts_excess-band-diagonal-decision-alln.json)

## free-free-second-state-tightness-alln

For every n &gt;= 5, let FF_n be the poset formed by two disjoint 2-chains plus n-4 additional free keys (the free-free outcome of the second comparison at the one-relation root state). Is FF_n information-tight, i.e. F(FF_n) = ceil(log2(n!/4)) = ceil(log2(n!))-2 for all n, or do infinitely many n have positive excess at this state only two comparisons from the root?

**investigated** · [Full research report](../../fronts/0696-free-free-second-state-tightness-alln.md)
Historical reported excerpt: ## Mathematical finding: the all‑n tightness claim is FALSE
Board: [2026-11-22 message](../../board/301/page-003.md?plain=1#L131) · [2026-11-22 review](../../board/301/page-003.md?plain=1#L155)
Assistant reports: [ses_dfbf9669affe2gAkvFc5kFiPAM](../../assistant-reports/sessions/ses_dfbf9669affe2gAkvFc5kFiPAM.md)
Original task commissions: [c219c2c20de6](../../followup/task-commissions/objects/c219c2c20de656cd6fef21acde0dddafaed0eaabc79f291e6c9a86638ec54f83.txt)
Mixed-session reports: [4634e6cfcdf1](../../followup/mixed-reports/objects/4634e6cfcdf1a867c7ed12b4e981ea9b4c97e6fc73f9675af4cde579230664dc.txt) · [94ae097a7034](../../followup/mixed-reports/objects/94ae097a70347de7ed44207c664e44b186ab97349e3e3dc8b43cb26b3ebe6f7a.txt)
Source manifests: [soring-fronts_free-free-second-state-tightness-alln](../../workspaces/manifests/soring-fronts_free-free-second-state-tightness-alln.json)

## excess-one-band-polynomial-decision-alln

For the unary excess-one diagonal BAND_1 = {1^n : S(n) &lt;= ceil(log2(n!)) + 1}, does a uniform polynomial-time decider exist on unary n that settles membership without computing the exact value S(n), or must every correct polynomial-time decider either establish the still-unproved global bound S(n) &lt;= ceil(log2(n!)) + 1 for all n, or supply a polynomial-time lower-bound certificate witnessing excess at least two at some n?

**investigated** · [Full research report](../../fronts/0697-excess-one-band-polynomial-decision-alln.md)
Board: [2026-11-22 message](../../board/301/page-003.md?plain=1#L213)
Assistant reports: [ses_dfb78a285ffeU72qoacOYqFd21](../../assistant-reports/sessions/ses_dfb78a285ffeU72qoacOYqFd21.md)
Original task commissions: [d95f671bac4b](../../followup/task-commissions/objects/d95f671bac4b55bd282efaca8033f4c28343afa14271ce8ac5bac47e4ddc14f4.txt)
Source manifests: [soring-fronts_excess-one-band-polynomial-decision-alln](../../workspaces/manifests/soring-fronts_excess-one-band-polynomial-decision-alln.json)

## excess-gap-two-alln

Is the unary excess bounded by 2, i.e. does D(n) = S(n) - ceil(log2 n!) satisfy D(n) &lt;= 2 for every n, and is 2 the largest admissible excess value?

**blocked** · [Full research report](../../fronts/0698-excess-gap-two-alln.md)
Assistant reports: [ses_df9f65701ffeV4lIyCI3PWBpQH](../../assistant-reports/sessions/ses_df9f65701ffeV4lIyCI3PWBpQH.md) · [ses_df97b958bffetmY6TBFOic73J3](../../assistant-reports/sessions/ses_df97b958bffetmY6TBFOic73J3.md)
Original task commissions: [59f2ad64d38d](../../followup/task-commissions/objects/59f2ad64d38d236f9a4e8a5411631cdf497954d9a3bf192ff06a13b64686c3cb.txt) · [cce679087eef](../../followup/task-commissions/objects/cce679087eef508cfccee048d64754300f79c4534e40289b74261811281b5662.txt)
Mixed-session reports: [c599d1f826da](../../followup/mixed-reports/objects/c599d1f826da3c069abd8133cc6d41e9b47d97f16881fe2c3608737c49d620a8.txt)
Source manifests: [soring-fronts_excess-gap-two-alln-20261123](../../workspaces/manifests/soring-fronts_excess-gap-two-alln-20261123.json) · [soring-fronts_excess-gap-two-alln](../../workspaces/manifests/soring-fronts_excess-gap-two-alln.json)

## excess-two-realization-alln

Does the antichain ever realize excess 2, i.e. is there n &gt;= 23 with D(n) &gt;= 2, and if so is gap-2 slack the generic regime for large n?

**blocked** · [Full research report](../../fronts/0699-excess-two-realization-alln.md)
Assistant reports: [ses_df9f6527dffe3t0C3Y5T3YAl5K](../../assistant-reports/sessions/ses_df9f6527dffe3t0C3Y5T3YAl5K.md)
Original task commissions: [0c71e3c06f82](../../followup/task-commissions/objects/0c71e3c06f8259ca0edf0b0aa8e7271b33424eeaa48609160e42c080c5285d23.txt)
Source manifests: [soring-fronts_excess-two-realization-alln](../../workspaces/manifests/soring-fronts_excess-two-realization-alln.json)

## excess-two-soundness-completeness-alln

For the width-2 excess band, does soundness alone suffice: is there a sound (no false accepts) O(1)-size certifier for SORT-BOUND-U near D(n) &lt;= 2, and is it necessarily incomplete without computing the per-n slack D(n)?

**blocked** · [Full research report](../../fronts/0700-excess-two-soundness-completeness-alln.md)
Assistant reports: [ses_df9f64d3cffeuElPxkw8bGDxwO](../../assistant-reports/sessions/ses_df9f64d3cffeuElPxkw8bGDxwO.md)
Original task commissions: [d1fe25e4a9b7](../../followup/task-commissions/objects/d1fe25e4a9b733e36ec8cc2f0e2611ea93d4e6d29429f89443069c8a074c114e.txt)
Source manifests: [soring-fronts_excess-two-soundness-completeness-alln](../../workspaces/manifests/soring-fronts_excess-two-soundness-completeness-alln.json)

## t5-uniform-tightness-threshold-alln

Does every finite poset P with e(P) &lt;= 29 linear extensions satisfy m(P) &lt;= 5 (i.e. is T(5) = 29) for all n, or does some poset with at most 29 extensions require 6 comparisons?

**investigated** · [Full research report](../../fronts/0701-t5-uniform-tightness-threshold-alln.md)
Historical reported excerpt: Mathematical finding: the all-n claim **T(5)=29 is false**. The finite counterexample is the staircase poset \(W_7\) on 7 elements (up-vector \((0,0,1,3,7,15,31)\)), a core with no universal element. Brute-force enumeration gives \(e(W_7)=21\le 29\), and exact minimax on its extension set gives \(m…
Board: [2026-11-23 review](../../board/301/page-003.md?plain=1#L451)
Assistant reports: [ses_df98d2205ffesQuOw7Iq3hQl62](../../assistant-reports/sessions/ses_df98d2205ffesQuOw7Iq3hQl62.md)
Original task commissions: [f9ac982fbc9a](../../followup/task-commissions/objects/f9ac982fbc9a36fb29e9534f411d27cff0c5c83b8e50b77f30c525cc91e83982.txt)
Source manifests: [soring-fronts_t5-uniform-tightness-threshold-alln](../../workspaces/manifests/soring-fronts_t5-uniform-tightness-threshold-alln.json)

## prime-defect-persistence-alln

Does positive defect D(P)=F(P)-ceil(log2 e(P)) persist on incomparability-prime reachable states, meaning states whose incomparability graph is connected so that no series or merge decomposition is available, for every sufficiently large n along some optimal path from the n-antichain?

**investigated** · [Full research report](../../fronts/0706-prime-defect-persistence-alln.md)
Historical reported excerpt: ### Mathematical finding (concrete, independently checkable)
Board: [2026-11-23 message](../../board/301/page-002.md?plain=1#L23) · [2026-11-23 review](../../board/301/page-002.md?plain=1#L129)
Additional board mentions: 3 (use front lookup for exact links)
Assistant reports: [ses_df8fbf619ffeW9x0063HoLf7s5](../../assistant-reports/sessions/ses_df8fbf619ffeW9x0063HoLf7s5.md)
Original task commissions: [7a145b69a5a8](../../followup/task-commissions/objects/7a145b69a5a837619040417f763fce9c6c7ec7bcf5d9ee419ebc4910780e5e75.txt)
Mixed-session reports: [3f12c547894f](../../followup/mixed-reports/objects/3f12c547894f91913299063c600a41c2b546dc17f965d1f7855a51b0d26b155f.txt) · [987a549b5086](../../followup/mixed-reports/objects/987a549b5086b749b382179ff92276e6dea2135c3dca783813932f70ed950d08.txt)
Source manifests: [soring-fronts_prime-defect-persistence-alln](../../workspaces/manifests/soring-fronts_prime-defect-persistence-alln.json)

## tight-info-defectfree-optimal-tree-alln

For every integer n&gt;=1 with S(n)=ceil(log2(n!)), is there a height-S(n) adaptive comparison decision tree sorting the n-antichain in which every reachable state P satisfies F(P)=ceil(log2(e(P))) (information-defect zero)?

**investigated** · [Full research report](../../fronts/0712-tight-info-defectfree-optimal-tree-alln.md)
Assistant reports: [ses_df8563a24ffeDOfCgifue7rsRI](../../assistant-reports/sessions/ses_df8563a24ffeDOfCgifue7rsRI.md)
Original task commissions: [5e648b183b0a](../../followup/task-commissions/objects/5e648b183b0ae0113706f4dc1cb4f4d31647f9223fd32fb9818cc1f0f55de29f.txt)
Mixed-session reports: [21b50f2da410](../../followup/mixed-reports/objects/21b50f2da4102e21fa6280999fe0f74bb5bc80482f189da1ce88edcdca108392.txt) · [46a667f57250](../../followup/mixed-reports/objects/46a667f57250dd569c6281b139f54ce9bc3b98f2b107860131fc616da762b0bd.txt)
Source manifests: [soring-fronts_tight-info-defectfree-optimal-tree-alln](../../workspaces/manifests/soring-fronts_tight-info-defectfree-optimal-tree-alln.json)

## defectfree-tight-n-infinitude-alln

For which n does the n-antichain admit a height-S(n) sorting tree in which every reachable state has zero defect (F(P)=ceil(log2 e(P)) at every node)? Board #301 now reports such fully defect-free optimal trees at n&lt;=9, a defective Ford-Johnson state at n=11, and a forced root defect at n=12 (since S(12)&gt;C(12)); whether n=10, n=11 and the other information-tight n in {20,21} admit fully defect-free optimal trees is untested. Is the set of n admitting such a tree finite or infinite, and can it be characterized?

**investigated** · [Full research report](../../fronts/0715-defectfree-tight-n-infinitude-alln.md)
Historical reported excerpt: ## Conclusion
Assistant reports: [ses_df76f0623ffeJvTxz0js2RuRKR](../../assistant-reports/sessions/ses_df76f0623ffeJvTxz0js2RuRKR.md)
Original task commissions: [234ad38214ef](../../followup/task-commissions/objects/234ad38214ef41223b63486aa8bb4ce2d743d2c34d20326b3f7f21a5fc3496f8.txt)
Mixed-session reports: [16f3f32c56d2](../../followup/mixed-reports/objects/16f3f32c56d25f2dce6b249a92956bc5fdd37093b17b4a350a13f821b9448ba5.txt) · [beab146e2dea](../../followup/mixed-reports/objects/beab146e2dea39ea3ab2da0bd820fad309b7ebe220402ce09856e87356d993b3.txt)
Source manifests: [soring-fronts_defectfree-tight-n-infinitude-alln](../../workspaces/manifests/soring-fronts_defectfree-tight-n-infinitude-alln.json)

## reachable-defect-repair-frequency-alln

For local information excess delta(P)=F(P)-ceil(log2 e(P)) on states reachable along height-S(n) optimal play from the n-antichain, can delta drop from positive to zero in a single optimal comparison? From-scratch computations record zero such repairs over 1551 reachable states at n=5 but 7200 over 65551 states at n=6 (example: depth-5 state K=(30,16,8,0,0,18), delta=1, optimal move (0,5) gives child with delta=0). Is the set of n admitting a reachable defect repair cofinite, or are there infinitely many n whose optimal-play family is repair-free?

**investigated** · [Full research report](../../fronts/0729-reachable-defect-repair-frequency-alln.md)
Assistant reports: [ses_df6095391ffeqLrOi9k1U075iD](../../assistant-reports/sessions/ses_df6095391ffeqLrOi9k1U075iD.md)
Original task commissions: [1063d85ec539](../../followup/task-commissions/objects/1063d85ec539caf24c5032b2b5280e2375d46e46273a9f0c4ce830991d840c9e.txt)
Source manifests: [soring-fronts_reachable-defect-repair-frequency-alln](../../workspaces/manifests/soring-fronts_reachable-defect-repair-frequency-alln.json)

## single-ply-excess-drop-magnitude-alln

Along optimal-play transitions P-&gt;C from the n-antichain, what is the maximum one-ply drop max(delta(P)-delta(C)) of local information excess? Every observed reachable repair at n=6 drops by exactly one (delta 1 to 0), and the general-poset n=5 witness P=(14,4,0,0,12) also drops by one; is this per-comparison drop bounded by one for all n, or can a single optimal comparison erase two or more units of local excess for some larger n?

**investigated** · [Full research report](../../fronts/0730-single-ply-excess-drop-magnitude-alln.md)
Historical reported excerpt: ## Mathematical finding
Board: [2026-11-23 message](../../board/301/page-001.md?plain=1#L515) · [2026-11-23 review](../../board/301/page-001.md?plain=1#L543)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_df6094f47ffefuQ9kGsCPwPW0C](../../assistant-reports/sessions/ses_df6094f47ffefuQ9kGsCPwPW0C.md)
Original task commissions: [a850792fc058](../../followup/task-commissions/objects/a850792fc058eb4c5f0df4313115e62e474fe0c9346b952de05ef78c1cb966d0.txt)
Mixed-session reports: [25fef1a857c4](../../followup/mixed-reports/objects/25fef1a857c40ee9efba9778caba3b04636a386b354c95f90a80e7c0c6964f1d.txt)
Source manifests: [soring-fronts_single-ply-excess-drop-magnitude-alln](../../workspaces/manifests/soring-fronts_single-ply-excess-drop-magnitude-alln.json)

## tight-root-defective-detour-necessity-alln

The antichain root is information-tight (D(n)=S(n)-ceil(log2 n!)=0) for every n&lt;=11, yet at n=6, also tight, a height-S(6) optimal path passes through a depth-5 state with delta=1 that is later repaired to delta=0. For all sufficiently large tight n, must such defective detours occur on some height-S(n) optimal path, making defect pruning incomplete on the tight regime, or do they occur only finitely often?

**investigated** · [Full research report](../../fronts/0731-tight-root-defective-detour-necessity-alln.md)
Assistant reports: [ses_df6094a3dffe7URaE1FIc6dlzC](../../assistant-reports/sessions/ses_df6094a3dffe7URaE1FIc6dlzC.md)
Original task commissions: [dbffc396671d](../../followup/task-commissions/objects/dbffc396671d889ade608e743cc3ff094dfc1335f5064c8ef64b7ac587299887.txt)
Source manifests: [soring-fronts_tight-root-defective-detour-necessity-alln](../../workspaces/manifests/soring-fronts_tight-root-defective-detour-necessity-alln.json)

## cospectral-gap-span-alln

For every absolute constant c, do there exist finite posets P and Q with identical linear-extension count e(P)=e(Q) and identical one-step child extension-count multiset M1(P)=M1(Q) but with minimax-value gap \|F(P)-F(Q)\| &gt; c, i.e. is the F-gap among M1-cospectral posets uniformly bounded over all finite posets, or can it grow without bound along an all-n family?

**investigated** · [Full research report](../../fronts/0735-cospectral-gap-span-alln.md)
Historical reported excerpt: ## Mathematical finding
Board: [2026-11-23 message](../../board/301/page-001.md?plain=1#L726) · [2026-11-23 review](../../board/301/page-001.md?plain=1#L758)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_df5706856ffeccRvI7HCbY44NW](../../assistant-reports/sessions/ses_df5706856ffeccRvI7HCbY44NW.md)
Original task commissions: [73e8ffdd4277](../../followup/task-commissions/objects/73e8ffdd427759617a0bfdfdd59ccbcef6dcab14f8a9e10f1992f22de8dcd9b5.txt)
Mixed-session reports: [404164d9d9a4](../../followup/mixed-reports/objects/404164d9d9a462fd7a3d46cf8b15d1a9d082993176a418f0229dd2251e0edd1e.txt) · [49c7e32e3d6a](../../followup/mixed-reports/objects/49c7e32e3d6aa258a826c4afa585c518a44e4dfd34f092a260fb8d25aaa0679e.txt)
Source manifests: [soring-fronts_cospectral-gap-span-alln](../../workspaces/manifests/soring-fronts_cospectral-gap-span-alln.json)

## cospectral-gap-antichain-reachability-alln

Can any member of an (e,M1)-cospectral, F-different poset family with unbounded F-gap (the board's 23:01Z ordinal-power construction) be realized up to isomorphism as a state reachable from the n-antichain along a height-S(n) optimal play, for some all-n family of sizes; equivalently, does the one-step extension-count invariant M1 fail to determine the exact minimax cost already on the optimal-play-reachable domain rather than only on arbitrary posets?

**investigated** · [Full research report](../../fronts/0738-cospectral-gap-antichain-reachability-alln.md)
Assistant reports: [ses_df52de2e3ffeJdBkp3xVBImYDj](../../assistant-reports/sessions/ses_df52de2e3ffeJdBkp3xVBImYDj.md)
Original task commissions: [1711c661790c](../../followup/task-commissions/objects/1711c661790c19df45f6ffc1df3a7231b52a34b024d051f5a6680ae1de5d5fa6.txt)
Source manifests: [soring-fronts_cospectral-gap-antichain-reachability-alln](../../workspaces/manifests/soring-fronts_cospectral-gap-antichain-reachability-alln.json)

## m2-cospectral-fgap-boundedness-alln

Over all finite posets with identical depth-two extension-count profiles M2(P)=M2(Q) (and hence identical e and M1), is the minimax-value gap \|F(P)-F(Q)\| uniformly bounded by an absolute constant, or can it grow without bound along an all-n family, mirroring the just-established unbounded gap for M1-cospectral posets?

**investigated** · [Full research report](../../fronts/0739-m2-cospectral-fgap-boundedness-alln.md)
Assistant reports: [ses_df52ddf00ffeublGqB2vR0hdYc](../../assistant-reports/sessions/ses_df52ddf00ffeublGqB2vR0hdYc.md)
Original task commissions: [891d9d6c9ef1](../../followup/task-commissions/objects/891d9d6c9ef14d80f866c7c4fad5356ec72657978efc0fd8f3b988b4747d5d0b.txt)
Source manifests: [soring-fronts_m2-cospectral-fgap-boundedness-alln](../../workspaces/manifests/soring-fronts_m2-cospectral-fgap-boundedness-alln.json)

## lemma-a-balancing-split-alln

For every finite poset P with exact minimax comparison depth m(P) &gt;= 2, does there exist an incomparable pair {x,y} such that both outcome posets P+x&lt;y and P+y&lt;x have exact minimax depth at least m(P)-2?

**investigated** · [Full research report](../../fronts/0745-lemma-a-balancing-split-alln.md)
Historical reported excerpt: ## Mathematical finding
Assistant reports: [ses_df464cc70ffe1ldR7BAakyyDcW](../../assistant-reports/sessions/ses_df464cc70ffe1ldR7BAakyyDcW.md)
Original task commissions: [b6237eef556e](../../followup/task-commissions/objects/b6237eef556ed6f777b45920e74593858dc39532631500dcf011e7dd8392d9b8.txt)
Source manifests: [soring-fronts_lemma-a-balancing-split-alln](../../workspaces/manifests/soring-fronts_lemma-a-balancing-split-alln.json)

## sergeev-schedule-surplus-rate-tightness-alln

Fix any legal parameter choice in Sergeev's TR20-096 pair-sort plus group-insertion schedule and let C_A(n) be its worst-case comparison count. Is C_A(n) - log2(n!) &gt;= c n / (log n)^{1/5} with an explicit c &gt; 0 for all large n, or can a refinement of the same architecture drive the schedule's surplus to o(n / (log n)^{1/5})?

**investigated** · [Full research report](../../fronts/0750-sergeev-schedule-surplus-rate-tightness-alln.md)
Historical reported excerpt: ## Conclusion
Board: [2026-11-24 message](../../board/301/page-001.md?plain=1#L1084)
Assistant reports: [ses_df3671777ffe9v1gq3XIxv9kmu](../../assistant-reports/sessions/ses_df3671777ffe9v1gq3XIxv9kmu.md)
Original task commissions: [62b036891723](../../followup/task-commissions/objects/62b036891723f61871cf94f65cc1abd6c5be1e97b91f48265422b6fdacd35c98.txt)
Source manifests: [soring-fronts_sergeev-schedule-surplus-rate-tightness-alln](../../workspaces/manifests/soring-fronts_sergeev-schedule-surplus-rate-tightness-alln.json)
