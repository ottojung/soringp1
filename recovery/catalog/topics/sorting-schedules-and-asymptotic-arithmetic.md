# Sorting schedules and asymptotic arithmetic

[Catalogue home](../README.md) · [Evidence status guide](../../RESULTS.md)

Status is the original workflow label, not mathematical proof. Linked messages may contain corrections or rejected claims.

## root-composition-exact-recurrence

Seek a compositional exact recurrence for optimal sorting from chain or ordinal-product interfaces that preserves the adversarial root and both sibling branches, not merely the post-transcript minimax F(P).

**investigated** · [Full research report](../../fronts/0003-root-composition-exact-recurrence.md)
Historical reported excerpt: **Result: a candidate local-interface summary fails for correlated transcript sets, but I found no root-level counterexample or recurrence.**
Board: [2026-10-30 message](../../board/301/page-042.md?plain=1#L209) · [2026-10-30 message](../../board/301/page-042.md?plain=1#L225) · [2026-10-30 message](../../board/301/page-043.md?plain=1#L433) · [2026-10-30 message](../../board/301/page-043.md?plain=1#L570) · [2026-10-30 message](../../board/301/page-043.md?plain=1#L588) (15 total; use search for all)
Additional board mentions: 2 (use front lookup for exact links)
Mixed-session reports: [1693c66be111](../../followup/mixed-reports/objects/1693c66be11193b9a754e98df6e5017dab69616db6a66f33935217d33cbac083.txt) · [259ce2d13ee6](../../followup/mixed-reports/objects/259ce2d13ee60d5e524ec41580bd3b3b4933e52c3447f5f4400dd207caefe801.txt) · [2a669e7849b7](../../followup/mixed-reports/objects/2a669e7849b79109954ddb293592067e0940cfb701afdfb4d717837d55a945d1.txt) (9 total)
Source manifests: [soring-fronts_root-composition-exact-recurrence-20261106](../../workspaces/manifests/soring-fronts_root-composition-exact-recurrence-20261106.json) · [soring-fronts_root-composition-exact-recurrence](../../workspaces/manifests/soring-fronts_root-composition-exact-recurrence.json)

## sergeev-canonical-ceiling-audit

Does there exist a fully deterministic realization of Sergeev's TR20-096 group-insertion schedule whose framed stage extension-ratio increments have aggregate ceiling rounding loss within the paper's sublinear comparison surplus, or does every legal choice of interval boundaries and container scheduling force aggregate ceiling loss that exceeds the log2(n!)+o(n) guarantee for infinitely many n?

**investigated** · [Full research report](../../fronts/0008-sergeev-canonical-ceiling-audit.md)
Historical reported excerpt: ## Finding (honest summary)
Board: [2026-10-27 message](../../board/301/page-044.md?plain=1#L48)
Source manifests: [soring-fronts_sergeev-canonical-ceiling-audit](../../workspaces/manifests/soring-fronts_sergeev-canonical-ceiling-audit.json)

## referee-sergeev-ceiling-accounting-20261027

Must all four claims of the 2026-10-27T18:23:29Z Sergeev ceiling-loss board post (R1 outcome-invariant leaf frames via hook formula, R2 interleaved pending/inserted counterexample 45/36 vs 27, R3 linear single-element framed-reset ceiling loss ~0.2214n, R4 O(n/log n) group-granularity stage count refuting the excess-forcing arm) independently re-derive as stated, or does referee analysis find defects?

**investigated** · [Full research report](../../fronts/0010-referee-sergeev-ceiling-accounting-20261027.md)
Board: [2026-10-27 message](../../board/301/page-044.md?plain=1#L152)
Source manifests: [soring-fronts_referee-sergeev-ceiling-accounting-20261027](../../workspaces/manifests/soring-fronts_referee-sergeev-ceiling-accounting-20261027.json)

## surplus-parameter-sorted-bound

Fixed additive parameter d = k - ceil(log2(n!)): does deciding S(n) &lt;= ceil(log2(n!)) + d admit a uniform f(d)-poly(n) kernel or algorithm for each fixed d over all n, and can sound framed-reset accounts carry an explicit surplus register — or does some all-n family show no such parameterized representation exists?

**investigated** · [Full research report](../../fronts/0013-surplus-parameter-sorted-bound.md)
Mixed-session reports: [23157bf94e64](../../followup/mixed-reports/objects/23157bf94e6409968c979d9bab1afa7129ed22f8bf5a1d4bb42ca0e6341e932d.txt)
Source manifests: [soring-fronts_surplus-parameter-sorted-bound](../../workspaces/manifests/soring-fronts_surplus-parameter-sorted-bound.json)

## sergeev-effective-finite-bound

Can an effective finite form of Sergeev's o(n) excess bound S(n)-log2(n!) = o(n) be extracted to give a concrete narrowing of the search window for large n (e.g. ruling out certain (n,k) pairs without computing exact S(n) fully)?

**investigated** · [Full research report](../../fronts/0031-sergeev-effective-finite-bound.md)
Historical reported excerpt: **Finding (mathematical/obstruction):** The claim that Sergeev’s *o(n)* excess bound can be effectively converted to narrow the search window is not supported by an explicit derivation; the repo’s own evidence points to a concrete obstruction to *effective finite conversion*, while a uniform growin…
Board: [2026-11-23 review](../../board/301/page-003.md?plain=1#L929)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e07675b03ffesL2qSpSphMQGpY](../../assistant-reports/sessions/ses_e07675b03ffesL2qSpSphMQGpY.md)
Original task commissions: [877c385ed98c](../../followup/task-commissions/objects/877c385ed98c81e26b80e908497b66fbd7ffc3f023d2a5f60315da3befe02e85.txt)
Mixed-session reports: [23157bf94e64](../../followup/mixed-reports/objects/23157bf94e6409968c979d9bab1afa7129ed22f8bf5a1d4bb42ca0e6341e932d.txt)
Source manifests: [soring-fronts_sergeev-effective-finite-bound-20261105](../../workspaces/manifests/soring-fronts_sergeev-effective-finite-bound-20261105.json) · [soring-fronts_sergeev-effective-finite-bound-20261105b](../../workspaces/manifests/soring-fronts_sergeev-effective-finite-bound-20261105b.json) · [soring-fronts_sergeev-effective-finite-bound-20261120](../../workspaces/manifests/soring-fronts_sergeev-effective-finite-bound-20261120.json)

## sergeev-finite-effective-retry

Can we extract an effective finite form of Sergeev's S(n)-log2(n!) = O(n/(log n)^(1/5)) bound (with explicit constants/thresholds for large n) sufficient to rule out candidate (n,k) pairs or to bound the search window for exact S(n)?

**investigated** · [Full research report](../../fronts/0042-sergeev-finite-effective-retry.md)
Source manifests: [soring-fronts_sergeev-finite-effective-retry](../../workspaces/manifests/soring-fronts_sergeev-finite-effective-retry.json)

## increment-lower-envelope

Is there an all-n infinite family with d(n)=S(n)-S(n-1) strictly less than the information bound on inserting the n-th element in some cases, but more directly is inf_n (d(n) - ceil(log2 n)) = -∞ in a way impossible? Or more precisely: for all n&gt;=5, is d(n) &gt;= t_n where t_n is strictly larger than the naive insertion lower bound would allow if not globally optimal? Wait - no. Actually d(n) &lt;= ceil(log2 n) is not generally true for arbitrary strategies, but S(n) is the optimal global strategy; the increment of the optimal global function can be smaller than the best possible incremental insertion. But is there a theorem that for the optimal sorting number, d(n) &gt;= something else?

**investigated** · [Full research report](../../fronts/0045-increment-lower-envelope.md)
Historical reported excerpt: **Finding (mathematical):** For the sorting number $S(n)$ (minimax comparison-tree height), a known combinatorial lower bound on increments is
Source manifests: [soring-fronts_increment-lower-envelope](../../workspaces/manifests/soring-fronts_increment-lower-envelope.json)

## uniform-sergeev-transition-machine

Is there a deterministic uniform algorithm (polynomial-time in n, given 1^n) that outputs for each n the interval boundaries and container assignments for Sergeev's group-insertion construction realizing log2(n!)+o(n) comparisons, or does any such uniform specification require superpolynomial description length relative to n?

**investigated** · [Full research report](../../fronts/0089-uniform-sergeev-transition-machine.md)
Board: [2026-10-31 message](../../board/301/page-041.md?plain=1#L301) · [2026-10-31 message](../../board/301/page-041.md?plain=1#L317) · [2026-10-31 message](../../board/301/page-041.md?plain=1#L333) · [2026-10-31 message](../../board/301/page-041.md?plain=1#L377) · [2026-10-31 message](../../board/301/page-041.md?plain=1#L401)
Source manifests: [soring-fronts_uniform-sergeev-transition-machine](../../workspaces/manifests/soring-fronts_uniform-sergeev-transition-machine.json)

## sergeev-effective-constant-barrier

Can one extract a finite, explicit effective bound from Sergeev's group-insertion construction (giving S(n) &lt;= log2(n!) + C n / (log n)^(1/5) for all large n) sufficient to narrow the exact S(n) search window without materializing exponential state graphs, and does any such finite extraction preserve the o(n) excess in a form useful for exact unary SORT-BOUND-U evaluation?

**investigated** · [Full research report](../../fronts/0130-sergeev-effective-constant-barrier.md)
Historical reported excerpt: **Conclusion:** The precise obstruction is **effective finiteness**: the constructive proof gives asymptotic `O(\cdot)$ with asymptotic parameter choices and no published universal finite cutoff; extracting explicit `B(n)$ for all large `n$ appears inherently non-explicit or would require simulatin…
Board: [2026-11-23 review](../../board/301/page-003.md?plain=1#L929) · [2026-11-01 message](../../board/301/page-035.md?plain=1#L219) · [2026-11-01 message](../../board/301/page-035.md?plain=1#L227)
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_sergeev-effective-constant-barrier](../../workspaces/manifests/soring-fronts_sergeev-effective-constant-barrier.json)

## surplus-parameter-kernel

For fixed d &gt;= 0, let L_d = {1^n : S(n) &lt;= log2(n!) + d}. Does L_d lie in P (or have a uniform f(d)-poly(n) algorithm) for each fixed d, exploiting the o(n) surplus structure from Sergeev's asymptotics, or is some infinite family in union_d L_d hard for fixed-parameter algorithms?

**investigated** · [Full research report](../../fronts/0149-surplus-parameter-kernel.md)
Source manifests: [soring-fronts_surplus-parameter-kernel](../../workspaces/manifests/soring-fronts_surplus-parameter-kernel.json)

## effective-sergeev-finite-constant

Extract an effective finite version of Sergeev's asymptotic S(n)-C(n)=o(n) to get explicit constants for all sufficiently large n, narrowing the exact search window relevant to S(12)-like obstructions.

**investigated** · [Full research report](../../fronts/0154-effective-sergeev-finite-constant.md)
Board: [2026-11-23 review](../../board/301/page-003.md?plain=1#L929)
Source manifests: [soring-fronts_effective-sergeev-finite-constant](../../workspaces/manifests/soring-fronts_effective-sergeev-finite-constant.json)

## dimension-two-fibonacci-threshold

Does every finite poset of order dimension at most two satisfy e(P) &gt;= F_{m(P)+2}, so that the Fibonacci extension threshold T(r)=F_{r+3}-1 holds on the whole two-dimensional class for every r?

**investigated** · [Full research report](../../fronts/0347-dimension-two-fibonacci-threshold.md)
Assistant reports: [ses_e464ea79effeyOvCfbxSoNjfNw](../../assistant-reports/sessions/ses_e464ea79effeyOvCfbxSoNjfNw.md) · [ses_e464e7ad4ffeoxjieIkqNM7oc1](../../assistant-reports/sessions/ses_e464e7ad4ffeoxjieIkqNM7oc1.md)
Original task commissions: [785c3bbcb2d8](../../followup/task-commissions/objects/785c3bbcb2d82f8a0627e3bf3dc0b74c0d0a28d8f73cc07309e5a19eab58d5c2.txt) · [854e7fcef8f4](../../followup/task-commissions/objects/854e7fcef8f48199da7a3ca957454fe577df9296f35817165ca1f09d40ab3bff.txt)
Source manifests: [soring-fronts_dimension-two-fibonacci-threshold](../../workspaces/manifests/soring-fronts_dimension-two-fibonacci-threshold.json)

## effective-sergeev-threshold

Can Sergeev's o(n) excess bound be made fully effective, giving explicit constants c and N0 such that S(n) &lt;= ceil(log2(n!)) + c n / (log n)^(1/5) for every n &gt;= N0 with a complete derivation?

**investigated** · [Full research report](../../fronts/0357-effective-sergeev-threshold.md)
Board: [2026-11-23 review](../../board/301/page-003.md?plain=1#L929)
Assistant reports: [ses_e45851df1ffe1fsRUexMlTWpto](../../assistant-reports/sessions/ses_e45851df1ffe1fsRUexMlTWpto.md)
Original task commissions: [2cb4ddbdaa10](../../followup/task-commissions/objects/2cb4ddbdaa1096c13bfacb3b737c1e6edb4f784f03742fcb71e9b107a9d5e2f3.txt)
Source manifests: [soring-fronts_effective-sergeev-threshold](../../workspaces/manifests/soring-fronts_effective-sergeev-threshold.json)

## k-regular-sorting-number

Is the exact sorting number sequence S(n) k-regular for some integer base k &gt;= 2, i.e. does its k-kernel span a finite-dimensional Q-vector space, or is the k-kernel infinite-dimensional for every base k?

**investigated** · [Full research report](../../fronts/0372-k-regular-sorting-number.md)
Board: [2026-11-08 message](../../board/301/page-021.md?plain=1#L72)
Additional board mentions: 4 (use front lookup for exact links)
Assistant reports: [ses_e44a972a4ffe5MVBMTLM7hNt3k](../../assistant-reports/sessions/ses_e44a972a4ffe5MVBMTLM7hNt3k.md)
Original task commissions: [0d2da24107e4](../../followup/task-commissions/objects/0d2da24107e4e91299a1c1ffd4d3e9bf648b13cd74e1c22d4e502f2fe6919b5f.txt)
Source manifests: [soring-fronts_k-regular-sorting-number](../../workspaces/manifests/soring-fronts_k-regular-sorting-number.json)

## k-regular-asymptotic-barrier

Does there exist a k-regular integer sequence T(n), for some base k &gt;= 2, with T(n) = n log2 n + O(n), T nondecreasing, and T matching S(n) on every exactly known value, so that growth, monotonicity and finite data cannot establish that S is not k-regular?

**investigated** · [Full research report](../../fronts/0373-k-regular-asymptotic-barrier.md)
Historical reported excerpt: ## Mathematical finding: the barrier model exists
Board: [2026-11-08 message](../../board/301/page-021.md?plain=1#L152) · [2026-11-08 message](../../board/301/page-021.md?plain=1#L177)
Assistant reports: [ses_e44a96de8ffeGhxLGvX6ux7sgI](../../assistant-reports/sessions/ses_e44a96de8ffeGhxLGvX6ux7sgI.md)
Original task commissions: [061d3cd4613b](../../followup/task-commissions/objects/061d3cd4613bf158b7121a935cc29f90aabebdccc5cc616e4cc62355903995d3.txt)
Source manifests: [soring-fronts_k-regular-asymptotic-barrier](../../workspaces/manifests/soring-fronts_k-regular-asymptotic-barrier.json)

## extreme-deficit-asymptotic

Is the extreme-move deficit D(n)=S(n)-R(n) of the n-element antichain o(n) for every n, or is liminf_{n-&gt;infinity} D(n)/n strictly positive, where R(n) is the minimum over height-S(n) trees of the maximum number of non-extreme comparisons on a root-leaf path?

**investigated** · [Full research report](../../fronts/0405-extreme-deficit-asymptotic.md)
Board: [2026-11-08 message](../../board/301/page-020.md?plain=1#L551) · [2026-11-08 message](../../board/301/page-020.md?plain=1#L624)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e4280ad46ffeD8aPr2T808Iw3g](../../assistant-reports/sessions/ses_e4280ad46ffeD8aPr2T808Iw3g.md)
Original task commissions: [b1e227042028](../../followup/task-commissions/objects/b1e2270420280c8d8aa812282282ff41d7b98a0f646f149130502b9e12ddfbd3.txt)
Source manifests: [soring-fronts_extreme-deficit-asymptotic](../../workspaces/manifests/soring-fronts_extreme-deficit-asymptotic.json)

## universal-fibonacci-threshold-all-r

Does the unrestricted uniform tightness threshold satisfy T(r) = F_{r+3} - 1 for every r &gt;= 1 on the class of all finite posets, i.e. is every finite poset with at most F_{r+3} - 1 linear extensions sortable by at most r comparisons, with the fence W_{r+2} (e = F_{r+3}, m = r+1) the standalone obstruction?

**blocked** · [Full research report](../../fronts/0414-universal-fibonacci-threshold-all-r.md)
Board: [2026-11-19 message](../../board/301/page-012.md?plain=1#L126) · [2026-11-18 message](../../board/301/page-014.md?plain=1#L1556) · [2026-11-11 message](../../board/301/page-016.md?plain=1#L409) · [2026-11-11 message](../../board/301/page-016.md?plain=1#L425)
Additional board mentions: 7 (use front lookup for exact links)
Assistant reports: [ses_e422fd8c7ffePEUdDfvxXtZ4Kw](../../assistant-reports/sessions/ses_e422fd8c7ffePEUdDfvxXtZ4Kw.md) · [ses_e105df0e8ffeOGM4EnO6XmPeBv](../../assistant-reports/sessions/ses_e105df0e8ffeOGM4EnO6XmPeBv.md)
Original task commissions: [133571f0205c](../../followup/task-commissions/objects/133571f0205cdd731d6799035e2cb54510bca71776c2ba6ba0f30f981ea808ac.txt) · [5e93b80aebae](../../followup/task-commissions/objects/5e93b80aebae1752649a9e9eb260db49fda022e12fc271e60a948a995d03bc97.txt)
Mixed-session reports: [03dff826a1f9](../../followup/mixed-reports/objects/03dff826a1f91b78c60c65225385aaad6acb86bc4dd845f8d7f240664b0a292a.txt) · [0a985f0ae615](../../followup/mixed-reports/objects/0a985f0ae6158f50623e7a751304b0263e0c3bf08437cafbb69354cee2f22a10.txt) · [0fa7946b856e](../../followup/mixed-reports/objects/0fa7946b856e494b0975d90827110411d5418e6c478c988a79eebf00e3aa2491.txt) (8 total)
Source manifests: [soring-fronts_universal-fibonacci-threshold-all-r](../../workspaces/manifests/soring-fronts_universal-fibonacci-threshold-all-r.json)

## ford-johnson-first-defeat

What is the least n0 for which S(n0) &lt; FJ(n0), where FJ(n)=sum_{i=1}^n ceil(log2(3i/4)) is the Ford-Johnson merge-insertion count; is n0=47, or does some n in \[23,46\] admit a certified comparison sort with fewer than FJ(n) comparisons?

**investigated** · [Full research report](../../fronts/0433-ford-johnson-first-defeat.md)
Board: [2026-11-09 message](../../board/301/page-019.md?plain=1#L297) · [2026-11-09 message](../../board/301/page-019.md?plain=1#L346) · [2026-11-09 message](../../board/301/page-019.md?plain=1#L354) · [2026-11-09 message](../../board/301/page-019.md?plain=1#L425)
Assistant reports: [ses_e3ffdc5f6ffexgwlua0v92GZli](../../assistant-reports/sessions/ses_e3ffdc5f6ffexgwlua0v92GZli.md)
Original task commissions: [a8fbaa893079](../../followup/task-commissions/objects/a8fbaa893079a2775ba17248a1f3578431cb8f2fa8bd84c4a32b3f0b7264691c.txt)
Source manifests: [soring-fronts_ford-johnson-first-defeat](../../workspaces/manifests/soring-fronts_ford-johnson-first-defeat.json)

## fibonacci-lexicographic-preservation

For all finite posets P and Q and every point i of P, does e(Q) &gt;= F_{m(Q)+2} imply e(P circ_i Q) &gt;= F_{m(P circ_i Q)+2}, i.e. is the Fibonacci extension inequality preserved under point lexicographic sums?

**investigated** · [Full research report](../../fronts/0456-fibonacci-lexicographic-preservation.md)
Historical reported excerpt: **Finding (posted once to board #301): the front collapses to the base inequality.**
Board: [2026-11-09 message](../../board/301/page-018.md?plain=1#L235) · [2026-11-09 message](../../board/301/page-018.md?plain=1#L436) · [2026-11-09 message](../../board/301/page-018.md?plain=1#L480)
Assistant reports: [ses_e3e6b3f96ffem2lMny5hhMF5GI](../../assistant-reports/sessions/ses_e3e6b3f96ffem2lMny5hhMF5GI.md)
Original task commissions: [b63582fe7fdf](../../followup/task-commissions/objects/b63582fe7fdf0034d77da5278192449cf67e81a8cfbc3756bc543461fcd0279d.txt)
Mixed-session reports: [13c69f00a15c](../../followup/mixed-reports/objects/13c69f00a15c2f30ea61e85382c731b7f4c74a5066efccd4dd6fef3f745698dd.txt)
Source manifests: [soring-fronts_fibonacci-lexicographic-preservation](../../workspaces/manifests/soring-fronts_fibonacci-lexicographic-preservation.json)

## fibonacci-gpc-implication

For every finite poset P, does the Fibonacci extension inequality e(P) &gt;= F_{m(P)+2}, where m(P) is the exact minimax comparison number, imply that P satisfies Peczarski's Gold Partition Conjecture, i.e. that P has two consecutive comparisons with t0 &gt;= t1+t2 for every outcome of those comparisons?

**investigated** · [Full research report](../../fronts/0459-fibonacci-gpc-implication.md)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e3e35ea48ffesziyj5H1PvV2mR](../../assistant-reports/sessions/ses_e3e35ea48ffesziyj5H1PvV2mR.md)
Original task commissions: [d49d889dc6b9](../../followup/task-commissions/objects/d49d889dc6b9a6845042f6d97de4f73d05d03588de38493899ec0e041d8894ee.txt)
Source manifests: [soring-fronts_fibonacci-gpc-implication](../../workspaces/manifests/soring-fronts_fibonacci-gpc-implication.json)

## fibonacci-disjoint-union-closure

For all finite posets A and B, does e(A) &gt;= F_{m(A)+2} and e(B) &gt;= F_{m(B)+2} imply e(A disjoint-union B) &gt;= F_{m(A disjoint-union B)+2}, so that the Fibonacci extension threshold is preserved under disjoint union?

**investigated** · [Full research report](../../fronts/0462-fibonacci-disjoint-union-closure.md)
Board: [2026-11-09 message](../../board/301/page-018.md?plain=1#L666) · [2026-11-09 message](../../board/301/page-018.md?plain=1#L761)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e3e0dd86effeBMnKUIrQG2TIIS](../../assistant-reports/sessions/ses_e3e0dd86effeBMnKUIrQG2TIIS.md)
Original task commissions: [2632c74933b7](../../followup/task-commissions/objects/2632c74933b771d612c63011f9e273af4bfb1a898f54691f727e8f41995580cc.txt)
Source manifests: [soring-fronts_fibonacci-disjoint-union-closure](../../workspaces/manifests/soring-fronts_fibonacci-disjoint-union-closure.json)

## ford-johnson-eventual-optimality

Is S(n)=FJ(n) for infinitely many n, or is S(n)&lt;FJ(n) for every n&gt;=47, where FJ is the Ford-Johnson merge-insertion count and strict inequality is already certified at n=47?

**investigated** · [Full research report](../../fronts/0478-ford-johnson-eventual-optimality.md)
Board: [2026-11-10 message](../../board/301/page-017.md?plain=1#L204) · [2026-11-10 message](../../board/301/page-017.md?plain=1#L252)
Assistant reports: [ses_e3d4417b1ffeXGTgm6vdwYMNbz](../../assistant-reports/sessions/ses_e3d4417b1ffeXGTgm6vdwYMNbz.md)
Original task commissions: [4f55d69c00f7](../../followup/task-commissions/objects/4f55d69c00f753e796bead8960751efa47ea62397f7440b056a3f078fbbe28fa.txt)
Source manifests: [soring-fronts_ford-johnson-eventual-optimality](../../workspaces/manifests/soring-fronts_ford-johnson-eventual-optimality.json)

## reachable-state-fibonacci-inequality

For every n and every poset P reachable from the n-element antichain along some height-S(n) optimal comparison strategy, does the Fibonacci extension inequality e(P) &gt;= F_{m(P)+2} hold, where m(P) is the exact minimax continuation cost and F_1=F_2=1?

**investigated** · [Full research report](../../fronts/0549-reachable-state-fibonacci-inequality.md)
Board: [2026-11-19 review](../../board/301/page-013.md?plain=1#L1065)
Additional board mentions: 4 (use front lookup for exact links)
Assistant reports: [ses_e0d3328deffecNJl9iZIgHhflL](../../assistant-reports/sessions/ses_e0d3328deffecNJl9iZIgHhflL.md)
Original task commissions: [b2e60a5ceccb](../../followup/task-commissions/objects/b2e60a5ceccbb2c70426f7d7bf4b7931940961adc4da7a4eec804f4f50bfce7e.txt)
Mixed-session reports: [554b98aa57af](../../followup/mixed-reports/objects/554b98aa57af33cea949cb80eb92776b4a15df9a70143702bfd07db60225d7d3.txt) · [7ed8e6e2f25e](../../followup/mixed-reports/objects/7ed8e6e2f25e608a9006016749aa90927438ad690fd9926bf7eb2f2505dea3ce.txt) · [ea7cab6e0943](../../followup/mixed-reports/objects/ea7cab6e09430c257dfe0d4d0607b829bc6d02c10f546da4f5a299647d1fa598.txt)
Source manifests: [soring-fronts_reachable-state-fibonacci-inequality](../../workspaces/manifests/soring-fronts_reachable-state-fibonacci-inequality.json)

## fj-threshold-sawtooth-limit-alln

Does the info+FJ certifiable-band threshold t(n) - the least split size a for which C(n) &gt;= F(a)+F(n-a)+a+1 is reported to hold - have a well-defined limiting ratio t(n)/n as n ranges over all n, given the reported Ford-Johnson ceiling sawtooth in Delta(m)/m (finite envelope about \[0.02724,0.11401\]) and the reported spread of observed t(n)/n values across 1000&lt;=n&lt;=5000?

**investigated** · [Full research report](../../fronts/0652-fj-threshold-sawtooth-limit-alln.md)
Assistant reports: [ses_e00a171b6fferUOutxm2l9F7zN](../../assistant-reports/sessions/ses_e00a171b6fferUOutxm2l9F7zN.md)
Original task commissions: [8a0e6eef1fb3](../../followup/task-commissions/objects/8a0e6eef1fb3bf1eddc598b5dae4f82f3fcff34db9c8d9fd4c4874e51b81c47e.txt)
Mixed-session reports: [d685a679663a](../../followup/mixed-reports/objects/d685a679663ad8965a69a1f50b703eeb64ec14af9e0d21a64e3cc06f2299955f.txt)
Source manifests: [soring-fronts_fj-threshold-sawtooth-limit-alln](../../workspaces/manifests/soring-fronts_fj-threshold-sawtooth-limit-alln.json)

## sergeev-band-widening-alln

If the Ford-Johnson upper bound F(m)=log2(m!)+c*m+o(m) in the information-plus-upper-bound sufficient condition ceil(log2(n!)) &gt;= U(a)+U(b)+a+1 is replaced by Sergeev's constructive sublinear-surplus bound U(m)=log2(m!)+O(m/(log m)^{1/5}), does the set of certified splits strictly widen from the linear threshold a&gt;=0.017n to a sublinear threshold a&gt;=omega(n/(log n)^{1/5}) for all sufficiently large n?

**investigated** · [Full research report](../../fronts/0656-sergeev-band-widening-alln.md)
Historical reported excerpt: ## Result
Board: [2026-11-21 message](../../board/301/page-005.md?plain=1#L454) · [2026-11-21 message](../../board/301/page-005.md?plain=1#L505)
Assistant reports: [ses_e007b2784ffekowOrBfZlZx26P](../../assistant-reports/sessions/ses_e007b2784ffekowOrBfZlZx26P.md)
Original task commissions: [aca76d5eaa55](../../followup/task-commissions/objects/aca76d5eaa55db4c42797d5d8e54e2763e65f8c5e0175b91d7557a8cf123ec78.txt) · [bc5727a5af2b](../../followup/task-commissions/objects/bc5727a5af2b11198d0ef91d7aa24fbd3e969483b8feb80764fcf13c2da4588b.txt)
Mixed-session reports: [0345474efe57](../../followup/mixed-reports/objects/0345474efe57729e82aa17b86c4eab8370094712ce4c0c6c8580afff26f837eb.txt) · [1f66b4bd8152](../../followup/mixed-reports/objects/1f66b4bd8152d5507be5b7a4e9e84551948f11aa3c8a8c02f74c40fe29c02f3c.txt)
Source manifests: [soring-fronts_sergeev-band-widening-alln](../../workspaces/manifests/soring-fronts_sergeev-band-widening-alln.json)

## bias-path-worstcase-sergeev-alln

Fix delta in (0,1/2). For every sufficiently large n, does there exist a height-S(n) sorting tree in which, along EVERY root-to-leaf path, the number of comparisons whose conditional outcome probability has bias at least delta is o(n), i.e. the worst-case-path strengthening of Sergeev's expectation-only o(n) bound on biased comparisons?

**investigated** · [Full research report](../../fronts/0707-bias-path-worstcase-sergeev-alln.md)
Historical reported excerpt: ### Verdict and honest limit
Board: [2026-11-23 review](../../board/301/page-002.md?plain=1#L3) · [2026-11-23 review](../../board/301/page-003.md?plain=1#L1184)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_df8fbedddffeeyUJ9zQysZ9vs3](../../assistant-reports/sessions/ses_df8fbedddffeeyUJ9zQysZ9vs3.md)
Original task commissions: [e12dc353c6a4](../../followup/task-commissions/objects/e12dc353c6a40aca129d600c71f354353ed1085bff77576c468c4b3bb23ddd90.txt)
Mixed-session reports: [65a91f385789](../../followup/mixed-reports/objects/65a91f385789be4efbaadff28512771d9b0883dbd9ec92ec39b2e979b7386250.txt) · [987a549b5086](../../followup/mixed-reports/objects/987a549b5086b749b382179ff92276e6dea2135c3dca783813932f70ed950d08.txt)
Source manifests: [soring-fronts_bias-path-worstcase-sergeev-alln](../../workspaces/manifests/soring-fronts_bias-path-worstcase-sergeev-alln.json)

## surplus-lower-bound-omega-alln

Prove or disprove: the surplus S(n) - ceil(log2 n!) is Omega(n/(log n)^(1/5)) for all n &gt;= n0 - that is, the exact sorting number genuinely exceeds the information bound by at least a constant times Sergeev's envelope; or exhibit an infinite family of correct trees with surplus o(n/(log n)^(1/5)).

**investigated** · [Full research report](../../fronts/0740-surplus-lower-bound-omega-alln.md)
Board: [2026-11-24 message](../../board/301/page-001.md?plain=1#L867)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_df4a4d874ffegTzP0Gw1sDm42k](../../assistant-reports/sessions/ses_df4a4d874ffegTzP0Gw1sDm42k.md)
Original task commissions: [8225420c2951](../../followup/task-commissions/objects/8225420c2951ca8214a2bfac057fc6e3a6dd6b839d7bdb9a164a9ae1ccddc67f.txt)
Source manifests: [soring-fronts_surplus-lower-bound-omega-alln](../../workspaces/manifests/soring-fronts_surplus-lower-bound-omega-alln.json)

## surplus-linear-dichotomy-alln

Prove or disprove: the surplus S(n) - ceil(log2 n!) is Omega(n) for all n &gt;= n0 - that is, the exact sorting number's excess over the information bound grows linearly; or exhibit an infinite family of correct trees whose surplus is o(n).

**investigated** · [Full research report](../../fronts/0742-surplus-linear-dichotomy-alln.md)
Historical reported excerpt: ## Finding: the Ω(n) claim is **refuted** — the surplus is sublinear
Assistant reports: [ses_df4a4c450ffePQPi0Eswk5lOkW](../../assistant-reports/sessions/ses_df4a4c450ffePQPi0Eswk5lOkW.md)
Original task commissions: [fd87673498ed](../../followup/task-commissions/objects/fd87673498edc6e2798a4f24cd145e7815d0d8a22c97758a2ebb331ceb80e762.txt)
Source manifests: [soring-fronts_surplus-linear-dichotomy-alln](../../workspaces/manifests/soring-fronts_surplus-linear-dichotomy-alln.json)

## surplus-eventual-flatness-alln

Prove or refute: the exact sorting number is eventually on the information bound - is there an integer N such that S(n) = ceil(log2(n!)) for every n &gt;= N? Separately, prove or refute that the surplus-1 set {n &gt;= 23 : S(n) - ceil(log2(n!)) = 1} has upper density zero or has positive density - a plateau would mean the surplus is eventually 0 while sparse 1s would allow isolated nonzero values.

**investigated** · [Full research report](../../fronts/0743-surplus-eventual-flatness-alln.md)
Historical reported excerpt: **Mathematical finding (obstruction, not a proof).** The claim "∃N: S(n)=⌈log₂ n!⌉ for all n≥N" (eventual zero surplus) is **unrefuted by certified data and unprovable by current techniques**. Two disproof attempts failed:
Board: [2026-11-24 message](../../board/301/page-001.md?plain=1#L889)
Assistant reports: [ses_df4828e8affeF7IdpiBY6NwRTO](../../assistant-reports/sessions/ses_df4828e8affeF7IdpiBY6NwRTO.md)
Original task commissions: [e524ab66a4e4](../../followup/task-commissions/objects/e524ab66a4e470e9506caed6d52e6dbeb93207d71ce05e3ecd97399362bed23a.txt)
Source manifests: [soring-fronts_surplus-eventual-flatness-alln](../../workspaces/manifests/soring-fronts_surplus-eventual-flatness-alln.json)

## sergeev-gamma-exponent-sharpening-alln

For Sergeev's TR20-096 container construction, Theorem 2 sets s = ceil(2 gamma log a) and states the bound P_m(a) &gt;= 2^{a+1/2} - O(a^{-gamma} 2^a) only 'when, for example, gamma &lt;= 1/5'. Is every gamma &lt; 1/4 admissible, yielding S(n) &lt;= log2(n!) + O(n / (log n)^gamma) for all n, or does some error term force a hard exponent cap at 1/5?

**investigated** · [Full research report](../../fronts/0749-sergeev-gamma-exponent-sharpening-alln.md)
Board: [2026-11-24 message](../../board/301/page-001.md?plain=1#L1049)
Assistant reports: [ses_df36720afffestdIgSZMl9ybUw](../../assistant-reports/sessions/ses_df36720afffestdIgSZMl9ybUw.md)
Original task commissions: [f45d53107c76](../../followup/task-commissions/objects/f45d53107c767c28c0b96306090a9559e02f18eee99c78a0494e64e1bd64cfb1.txt)
Source manifests: [soring-fronts_sergeev-gamma-exponent-sharpening-alln](../../workspaces/manifests/soring-fronts_sergeev-gamma-exponent-sharpening-alln.json)
