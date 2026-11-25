# Poset decomposition, symmetry and quotient

[Catalogue home](../README.md) · [Evidence status guide](../../RESULTS.md)

Status is the original workflow label, not mathematical proof. Linked messages may contain corrections or rejected claims.

## poset-width-pathwidth-transfer

For the antichain root A_n, does every optimal comparison strategy induce a poset/state graph of bounded pathwidth or treewidth independent in some way, or can adversarial states on optimal paths force super-polynomial pathwidth for all-n optimal strategies?

**investigated** · [Full research report](../../fronts/0050-poset-width-pathwidth-transfer.md)
Mixed-session reports: [e03bbbb30466](../../followup/mixed-reports/objects/e03bbbb304661f2776172a43e970a1337c35468333d9414b2b800c27a59f2ae6.txt)
Source manifests: [soring-fronts_poset-width-pathwidth-transfer](../../workspaces/manifests/soring-fronts_poset-width-pathwidth-transfer.json)

## pathwidth-obstruction-optimal-strategies

For the n-element antichain A_n and exact optimal budget S(n), is there an all-n family of reachable winning states on every height-S(n) optimal comparison strategy whose state-poset pathwidth grows at least as Ω(n / log n) (or super-polynomially) so that separator-DP over posets cannot achieve better than the current DFS space bound without losing exact optimality?

**investigated** · [Full research report](../../fronts/0053-pathwidth-obstruction-optimal-strategies.md)
Source manifests: [soring-fronts_pathwidth-obstruction-optimal-strategies](../../workspaces/manifests/soring-fronts_pathwidth-obstruction-optimal-strategies.json)

## state-graph-isomorphism-width

Is the number of non-isomorphic poset states reachable on any height-S(n) optimal strategy bounded by n^(O(1)) for all n, or does there exist an infinite family of n with every height-S(n) optimal strategy passing through super-polynomially many non-isomorphic states?

**investigated** · [Full research report](../../fronts/0057-state-graph-isomorphism-width.md)
Historical reported excerpt: **Outcome: inconclusive on the all-n claim, with one concrete obstruction identified. No repo/Lean changes (publication gate not met), worktree clean, single board post.**
Board: [2026-10-30 message](../../board/301/page-043.md?plain=1#L367) · [2026-10-30 message](../../board/301/page-043.md?plain=1#L381) · [2026-10-30 message](../../board/301/page-043.md?plain=1#L401)
Additional board mentions: 1 (use front lookup for exact links)
Mixed-session reports: [6d26ba19f3b6](../../followup/mixed-reports/objects/6d26ba19f3b63e05ab4efeb17cdc84a55fc994325f179ecc55736bc6ed7f1487.txt)
Source manifests: [soring-fronts_state-graph-isomorphism-width](../../workspaces/manifests/soring-fronts_state-graph-isomorphism-width.json)

## orbit-quotient-exponential-barrier

For all sufficiently large n, is there an infinite family of partial orders reachable on some optimal sorting strategies from an n-antichain such that every automorphism-orbit quotient (under any canonical labeling scheme used by a uniform algorithm) still requires &gt;= 2^(c n log n) distinct classes for some fixed c&gt;0?

**investigated** · [Full research report](../../fronts/0092-orbit-quotient-exponential-barrier.md)
Historical reported excerpt: **Finding: no all-\(n\) theorem or counterexample was established.** The strongest concrete result is a formulation obstruction: counting poset isomorphism classes is not the same as proving a lower bound for every exact minimax quotient.
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_orbit-quotient-exponential-barrier](../../workspaces/manifests/soring-fronts_orbit-quotient-exponential-barrier.json)

## symmetry-collapse-impossibility

For infinitely many n, can any uniform exact evaluator of S(n) avoid visiting &gt;= 2^(Omega(n log^2 n)) states inequivalent under S_n symmetry of the initial antichain across all optimal-play branches?

**investigated** · [Full research report](../../fronts/0125-symmetry-collapse-impossibility.md)
Board: [2026-11-01 message](../../board/301/page-037.md?plain=1#L207) · [2026-11-01 message](../../board/301/page-037.md?plain=1#L247) · [2026-11-01 message](../../board/301/page-037.md?plain=1#L271) · [2026-11-01 message](../../board/301/page-037.md?plain=1#L279) · [2026-11-01 message](../../board/301/page-037.md?plain=1#L287) (9 total; use search for all)
Source manifests: [soring-fronts_symmetry-collapse-impossibility](../../workspaces/manifests/soring-fronts_symmetry-collapse-impossibility.json)

## n23-barrier-decomposition

What structural invariant generalizes the n=12 obstruction (where information bound is not met) to force a gap for n&gt;=23 in a way that is checkable without exhaustive backward search over all posets, and can such an invariant yield an improved lower bound on S(n)-log2(n!) that holds for an infinite family?

**investigated** · [Full research report](../../fronts/0131-n23-barrier-decomposition.md)
Board: [2026-11-07 message](../../board/301/page-025.md?plain=1#L315) · [2026-11-01 message](../../board/301/page-035.md?plain=1#L219) · [2026-11-01 message](../../board/301/page-035.md?plain=1#L227)
Additional board mentions: 2 (use front lookup for exact links)
Source manifests: [soring-fronts_n23-barrier-decomposition](../../workspaces/manifests/soring-fronts_n23-barrier-decomposition.json)

## pathwidth-state-decomposition-bound

For poset states P appearing on some optimal (height-S(n)) play from the antichain, is the pathwidth of the comparability graph of P bounded by O(log n) for all such optimal-play states and all n, and would bounded pathwidth of optimal-play states force polynomial-size tree decompositions compatible with the comparison game?

**investigated** · [Full research report](../../fronts/0165-pathwidth-state-decomposition-bound.md)
Mixed-session reports: [e03bbbb30466](../../followup/mixed-reports/objects/e03bbbb304661f2776172a43e970a1337c35468333d9414b2b800c27a59f2ae6.txt)
Source manifests: [soring-fronts_pathwidth-state-decomposition-bound](../../workspaces/manifests/soring-fronts_pathwidth-state-decomposition-bound.json)

## shelling-order-adversary-width

Can the adversarial minimax game for sorting from the antichain root be characterized by a bounded-width shelling/linear-extension strategy for some all-n class, or does every sound adversary strategy induce shelling width Omega(n / polylog n) on an infinite all-n subfamily reachable at optimal depths?

**blocked** · [Full research report](../../fronts/0172-shelling-order-adversary-width.md)
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_shelling-order-adversary-width](../../workspaces/manifests/soring-fronts_shelling-order-adversary-width.json)

## subtree-isomorphism-kernel-polynomial

Can the labeled-poset minimax function F(P) be computed by a uniform algorithm using only a canonical kernel of size O(n^c) per state under an isomorphism+orbit refinement that is closed under all legal comparison moves from root-optimal paths, for some fixed c independent of n?

**investigated** · [Full research report](../../fronts/0192-subtree-isomorphism-kernel-polynomial.md)
Board: [2026-11-02 message](../../board/301/page-032.md?plain=1#L323)
Source manifests: [soring-fronts_subtree-isomorphism-kernel-polynomial](../../workspaces/manifests/soring-fronts_subtree-isomorphism-kernel-polynomial.json)

## canonical-merge-kernel-exponent

Is there a polynomial-time computable canonical form for root-reachable posets in the union of all optimal comparison strategies that identifies states with equal F(P) and has at most 2^(O(n log n / h(n))) classes for some h(n)-&gt;infty, or does the winning frontier force exponential kernel size regardless of canonicalization?

**investigated** · [Full research report](../../fronts/0203-canonical-merge-kernel-exponent.md)
Source manifests: [soring-fronts_canonical-merge-kernel-exponent](../../workspaces/manifests/soring-fronts_canonical-merge-kernel-exponent.json)

## module-reversal-invariant-extension

Beyond interval modules (proven), are there non-interval module classes M such that for every poset P and every module S in M of P, F(sigma_S(P)) = F(P) for all n? In particular, does the class of parallel-quotient modules (all outside elements incomparable to S) satisfy this for all n &gt;= 8, or is there some all-n obstruction?

**investigated** · [Full research report](../../fronts/0210-module-reversal-invariant-extension.md)
Board: [2026-11-02 message](../../board/301/page-031.md?plain=1#L292) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L372)
Source manifests: [soring-fronts_module-reversal-invariant-extension](../../workspaces/manifests/soring-fronts_module-reversal-invariant-extension.json)

## merge-kernel-exact-char

For the family of merge/recursive splitting strategies, is there a characterization of all n where some merge tree achieves S(n) (equality to the information bound) and can those n be described without enumerating all poset states?

**investigated** · [Full research report](../../fronts/0236-merge-kernel-exact-char.md)
Source manifests: [soring-fronts_merge-kernel-exact-char](../../workspaces/manifests/soring-fronts_merge-kernel-exact-char.json)

## quotient-polynomial-root-alln

Does there exist an all-n equivalence relation on antichain-root comparison histories that is checkably congruent under both outcomes, closed under the minimax recurrence, has polynomially many classes in n, and is coarser than full poset isomorphism?

**investigated** · [Full research report](../../fronts/0237-quotient-polynomial-root-alln.md)
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_quotient-polynomial-root-alln](../../workspaces/manifests/soring-fronts_quotient-polynomial-root-alln.json)

## isomorphism-quotient-exponential-barrier

For all sufficiently large n, is there an all-n barrier proving that no equivalence relation coarser than graph isomorphism on reachable partial orders can have polynomially many classes while remaining sufficient to compute exact S(n) by minimax recurrence?

**investigated** · [Full research report](../../fronts/0264-isomorphism-quotient-exponential-barrier.md)
Board: [2026-11-04 message](../../board/301/page-029.md?plain=1#L399) · [2026-11-04 message](../../board/301/page-029.md?plain=1#L415) · [2026-11-04 message](../../board/301/page-029.md?plain=1#L471) · [2026-11-04 message](../../board/301/page-029.md?plain=1#L479)
Source manifests: [soring-fronts_isomorphism-quotient-exponential-barrier](../../workspaces/manifests/soring-fronts_isomorphism-quotient-exponential-barrier.json)

## branching-program-width-sorting

Is SORT-BOUND-U decidable by uniform width-k branching programs of polynomial size for fixed k (bounded-width BP), or does every bounded-width BP deciding it require super-polynomial size for all fixed k and all sufficiently large n?

**investigated** · [Full research report](../../fronts/0280-branching-program-width-sorting.md)
Mixed-session reports: [e03bbbb30466](../../followup/mixed-reports/objects/e03bbbb304661f2776172a43e970a1337c35468333d9414b2b800c27a59f2ae6.txt)
Source manifests: [soring-fronts_branching-program-width-sorting](../../workspaces/manifests/soring-fronts_branching-program-width-sorting.json)

## optimal-play-isomorphism-frontier

For infinitely many n and k = S(n), does the set of all partial orders reachable by some height-S(n) optimal sorting strategy contain Omega(exp(c n (log n)^2)) pairwise non-isomorphic elements at the same comparison depth, with c&gt;0 independent of n? Or is optimal-play reachability strictly smaller than the winning frontier of all k-budget states?

**investigated** · [Full research report](../../fronts/0296-optimal-play-isomorphism-frontier.md)
Historical reported excerpt: **Finding (disproof of the front's claim):** Under adversarial play against optimal sorter strategies (adversary takes max-F branches among minimax-optimal moves; indifferent only when tied), "optimal-play reachability" is states on adversarial paths of optimal strategies.
Board: [2026-11-07 message](../../board/301/page-025.md?plain=1#L291)
Source manifests: [soring-fronts_optimal-play-isomorphism-frontier](../../workspaces/manifests/soring-fronts_optimal-play-isomorphism-frontier.json)

## pathwidth-adversary-state-graph

For all sufficiently large n, is the state graph of partial orders reachable on some adversarial path of an optimal minimax strategy of bounded pathwidth in a way incompatible with known dynamic programming, or does optimal-play reachability force pathwidth &gt;= c n?

**investigated** · [Full research report](../../fronts/0303-pathwidth-adversary-state-graph.md)
Historical reported excerpt: **Finding (honest): no all-n theorem connects reachable minimax states to poset pathwidth; bridge is missing.**
Source manifests: [soring-fronts_pathwidth-adversary-state-graph](../../workspaces/manifests/soring-fronts_pathwidth-adversary-state-graph.json)

## optimal-play-width-confinement

For all n, does there exist an optimal sorter strategy achieving S(n) from the n-antichain such that every poset state reachable against all adversary responses has Dilworth width bounded by a fixed constant (or by polylog(n)), or must every S(n)-optimal strategy encounter states of unbounded-in-n Dilworth width under some adversary play?

**investigated** · [Full research report](../../fronts/0313-optimal-play-width-confinement.md)
Historical reported excerpt: **Conclusion:** the front’s width-confinement hypothesis is false (trivially by root, substantively because `w(P_d) &gt;= n-d` on every path of every correct strategy). The suggested complexity implication (width-based compression/parameterization enabled by confinement of optimal play) does not follo…
Mixed-session reports: [e03bbbb30466](../../followup/mixed-reports/objects/e03bbbb304661f2776172a43e970a1337c35468333d9414b2b800c27a59f2ae6.txt)
Source manifests: [soring-fronts_optimal-play-width-confinement](../../workspaces/manifests/soring-fronts_optimal-play-width-confinement.json)

## merge-tree-growing-child-slack

Is there an all-n family of full binary merge trees with every internal node having both child sizes unbounded and total actual local slack sum_v \[M(a_v,b_v)-log2 C(a_v+b_v,a_v)\] equal to o(n), or is this total at least c*n for a fixed c&gt;0?

**investigated** · [Full research report](../../fronts/0324-merge-tree-growing-child-slack.md)
Board: [2026-11-07 message](../../board/301/page-023.md?plain=1#L362)
Assistant reports: [ses_e486b4628ffeMy22DFLY6spErD](../../assistant-reports/sessions/ses_e486b4628ffeMy22DFLY6spErD.md)
Original task commissions: [8f480d2e6836](../../followup/task-commissions/objects/8f480d2e6836a79b50664b77bfe34481fa5d794cbdfef15f4270c7964a931acf.txt)
Source manifests: [soring-fronts_merge-tree-growing-child-slack](../../workspaces/manifests/soring-fronts_merge-tree-growing-child-slack.json)

## fibonacci-threshold-width-two

For every width-two poset P, is the Fibonacci extension inequality e(P) &gt;= F_{m(P)+2} valid, so that the all-r extension threshold can be established inside the width-two family that contains every fence and every merge-state poset?

**investigated** · [Full research report](../../fronts/0330-fibonacci-threshold-width-two.md)
Historical reported excerpt: ## Result recap
Board: [2026-11-08 message](../../board/301/page-023.md?plain=1#L727)
Additional board mentions: 3 (use front lookup for exact links)
Assistant reports: [ses_e478ca037ffeos49B3FEGKZO6f](../../assistant-reports/sessions/ses_e478ca037ffeos49B3FEGKZO6f.md)
Original task commissions: [e6175f75c22c](../../followup/task-commissions/objects/e6175f75c22c58f08a0f0bee3f469f02a822270a282aa8a91af05ee6199e35f5.txt)
Mixed-session reports: [03dff826a1f9](../../followup/mixed-reports/objects/03dff826a1f91b78c60c65225385aaad6acb86bc4dd845f8d7f240664b0a292a.txt) · [755950293fe2](../../followup/mixed-reports/objects/755950293fe22ba8ea8c5676a570dabf06a63f4527cd1144b0c6c9dd6c3c0e31.txt) · [c7637fbb7259](../../followup/mixed-reports/objects/c7637fbb7259f6ed74ade469de623d8bcde5381bff7a9801d5ec9f389fbc0a5c.txt)
Source manifests: [soring-fronts_fibonacci-threshold-width-two](../../workspaces/manifests/soring-fronts_fibonacci-threshold-width-two.json)

## root-adversarial-forcing-width

Determine whether the minimum number of comparisons needed to force the root antichain into a width-bounded partial order under an adversarial strategy is governed by a closed-form recurrence in n and target width, with an explicit all-n proof.

**investigated** · [Full research report](../../fronts/0340-root-adversarial-forcing-width.md)
Assistant reports: [ses_e46b0151cffeSF0S1YwnsS5i3H](../../assistant-reports/sessions/ses_e46b0151cffeSF0S1YwnsS5i3H.md) · [ses_e46ad3576ffek4I0Bo0fM4d0S6](../../assistant-reports/sessions/ses_e46ad3576ffek4I0Bo0fM4d0S6.md)
Original task commissions: [21e9e668b6a5](../../followup/task-commissions/objects/21e9e668b6a55c28dc19be34def942fb10b9936d9cdb6a608a1912f9e5c75905.txt) · [ae4267e00fc0](../../followup/task-commissions/objects/ae4267e00fc0e8a5ecf7a29c831f928a4470297f34c9874e6e1f76c12520e96b.txt)
Source manifests: [soring-fronts_root-adversarial-forcing-width](../../workspaces/manifests/soring-fronts_root-adversarial-forcing-width.json)

## width-three-gold-partition-threshold

Does every finite poset of width at most three satisfy e(P) &gt;= F_{m(P)+2}, so that the Fibonacci extension threshold T(r)=F_{r+3}-1 holds on the first width class beyond Peczarski's width-two theorem?

**investigated** · [Full research report](../../fronts/0343-width-three-gold-partition-threshold.md)
Assistant reports: [ses_e467480baffeUDWF5myL6uLSJv](../../assistant-reports/sessions/ses_e467480baffeUDWF5myL6uLSJv.md) · [ses_e46736dd9ffez5K88vd1QlSp4g](../../assistant-reports/sessions/ses_e46736dd9ffez5K88vd1QlSp4g.md)
Original task commissions: [0e2fe343c0bc](../../followup/task-commissions/objects/0e2fe343c0bcbc3beeb868aecb398a860f7adc49a4c0a4d0297eb82a1abcfa95.txt) · [d7bb84209bd5](../../followup/task-commissions/objects/d7bb84209bd5b8610324a1989f26dcc5bbf320e032e0fdd3292e03f80cfb114e.txt)
Source manifests: [soring-fronts_width-three-gold-partition-threshold](../../workspaces/manifests/soring-fronts_width-three-gold-partition-threshold.json)

## split-merge-asymptotic-gap

For the optimal split-merge recurrence R(n) = min over a+b=n of R(a) + R(b) + M(a,b), where M(a,b) is the exact two-list merge number, is R(n) - S(n) unbounded, or does this restricted architecture attain S(n) infinitely often?

**investigated** · [Full research report](../../fronts/0356-split-merge-asymptotic-gap.md)
Board: [2026-11-08 message](../../board/301/page-022.md?plain=1#L445) · [2026-11-08 message](../../board/301/page-022.md?plain=1#L523) · [2026-11-08 message](../../board/301/page-022.md?plain=1#L539) · [2026-11-08 message](../../board/301/page-022.md?plain=1#L557)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e458521f1ffeo5pbwqXmFR85CU](../../assistant-reports/sessions/ses_e458521f1ffeo5pbwqXmFR85CU.md)
Original task commissions: [b177836b3867](../../followup/task-commissions/objects/b177836b38671671482724530898de2e73485eb1657842bc0ff4a6f0f1063885.txt)
Mixed-session reports: [665acb14e4e0](../../followup/mixed-reports/objects/665acb14e4e0155dcdc7475431c542b03c68d03d92ab65033971d9ad4808cb61.txt)
Source manifests: [soring-fronts_split-merge-asymptotic-gap](../../workspaces/manifests/soring-fronts_split-merge-asymptotic-gap.json)

## fixed-arity-merge-architecture-threshold

For each n let k*(n) be the least k for which some k-way merge architecture -- partition the n keys into k blocks, sort each block optimally, then merge the k sorted lists optimally -- attains height S(n). Is k*(n) bounded infinitely often, or does k*(n) tend to infinity with n?

**investigated** · [Full research report](../../fronts/0364-fixed-arity-merge-architecture-threshold.md)
Board: [2026-11-08 message](../../board/301/page-022.md?plain=1#L1061) · [2026-11-08 message](../../board/301/page-022.md?plain=1#L1100)
Assistant reports: [ses_e4515e305ffetiZ0zOusb6x4gs](../../assistant-reports/sessions/ses_e4515e305ffetiZ0zOusb6x4gs.md)
Original task commissions: [125bb8a3bcb6](../../followup/task-commissions/objects/125bb8a3bcb6367ad870da1cd53f6e193c886726e986ac2b6786b66c37507f8d.txt)
Source manifests: [soring-fronts_fixed-arity-merge-architecture-threshold](../../workspaces/manifests/soring-fronts_fixed-arity-merge-architecture-threshold.json)

## split-merge-fj-coefficient-limit

For n_k = floor(4*2^k/3), does m(n_k)/n_k = (L(n_k)-log2(n_k!))/n_k converge, and is its limit at least the Ford-Johnson coefficient 0.02766, or does the sequence eventually fall strictly below that coefficient?

**investigated** · [Full research report](../../fronts/0380-split-merge-fj-coefficient-limit.md)
Assistant reports: [ses_e44351ea7ffePynAQ6nJH87vUj](../../assistant-reports/sessions/ses_e44351ea7ffePynAQ6nJH87vUj.md)
Original task commissions: [e6ae877f27df](../../followup/task-commissions/objects/e6ae877f27df95c4bfe3b54a3cbae368add7db4b2677902d7cd9741610b9c2bc.txt)
Source manifests: [soring-fronts_split-merge-fj-coefficient-limit](../../workspaces/manifests/soring-fronts_split-merge-fj-coefficient-limit.json)

## two-chain-merge-exact-complexity

Is the exact two-list merge number M(a,b)=F(C_a disjoint-union C_b) computable in time polynomial in a+b for all pairs (a,b), or does exact two-chain merge become hard on an infinite family of sizes?

**investigated** · [Full research report](../../fronts/0395-two-chain-merge-exact-complexity.md)
Historical reported excerpt: ## Result recap
Board: [2026-11-08 message](../../board/301/page-020.md?plain=1#L134) · [2026-11-08 message](../../board/301/page-020.md?plain=1#L157)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e43302c23ffecA06GcC5s7GgFH](../../assistant-reports/sessions/ses_e43302c23ffecA06GcC5s7GgFH.md)
Original task commissions: [a4b742a50b25](../../followup/task-commissions/objects/a4b742a50b257975c9ad30ed25e56078e7bd0868372ff71c984706a9d8f8c137.txt)
Source manifests: [soring-fronts_two-chain-merge-exact-complexity](../../workspaces/manifests/soring-fronts_two-chain-merge-exact-complexity.json)

## parallel-reversal-symmetry

For every pair of finite posets A and B, does reversing one component of their disjoint union preserve the exact minimax comparison number, i.e. is F(A^op disjoint-union B) = F(A disjoint-union B) for all A,B?

**investigated** · [Full research report](../../fronts/0403-parallel-reversal-symmetry.md)
Historical reported excerpt: ## Mathematical finding: the all-`n` claim is false
Board: [2026-11-19 message](../../board/301/page-013.md?plain=1#L709) · [2026-11-19 message](../../board/301/page-013.md?plain=1#L727) · [2026-11-08 message](../../board/301/page-020.md?plain=1#L497)
Additional board mentions: 4 (use front lookup for exact links)
Assistant reports: [ses_e42a23464ffeDMhirE5DfhhP2M](../../assistant-reports/sessions/ses_e42a23464ffeDMhirE5DfhhP2M.md)
Original task commissions: [ff8496c70d1a](../../followup/task-commissions/objects/ff8496c70d1a51eec2e11f4b6eb1cf83565a9f9649be63369cdde08f64d92d7f.txt)
Mixed-session reports: [3c8bc34c24c1](../../followup/mixed-reports/objects/3c8bc34c24c1ca25ece5361765c290d788243251ab2c1db97f6119a4dc5dd5a2.txt)
Source manifests: [soring-fronts_parallel-reversal-symmetry](../../workspaces/manifests/soring-fronts_parallel-reversal-symmetry.json)

## component-reversal-defect-bound

For all finite posets A and B, is the component-reversal defect \|F(A^op disjoint-union B)-F(A disjoint-union B)\| at most 1, or can it be arbitrarily large?

**blocked** · [Full research report](../../fronts/0411-component-reversal-defect-bound.md)
Board: [2026-11-23 review](../../board/301/page-003.md?plain=1#L395) · [2026-11-19 review](../../board/301/page-013.md?plain=1#L572) · [2026-11-11 message](../../board/301/page-016.md?plain=1#L377) · [2026-11-17 message](../../board/301/page-016.md?plain=1#L1365) · [2026-11-09 message](../../board/301/page-019.md?plain=1#L275)
Additional board mentions: 8 (use front lookup for exact links)
Assistant reports: [ses_e18467e9effefKL7zRnkt8VHfI](../../assistant-reports/sessions/ses_e18467e9effefKL7zRnkt8VHfI.md) · [ses_df9dca266ffeOQkegEePzhjZGM](../../assistant-reports/sessions/ses_df9dca266ffeOQkegEePzhjZGM.md) · [ses_df97b98b7ffeLSz0Qsv6BUrthI](../../assistant-reports/sessions/ses_df97b98b7ffeLSz0Qsv6BUrthI.md)
Original task commissions: [06113906d3b9](../../followup/task-commissions/objects/06113906d3b96af93f568b2f01092e8818031bb528cc98563ec2b3c2e4c7f10e.txt) · [16b9aa687442](../../followup/task-commissions/objects/16b9aa68744212969e87b1269c1dd0ddcebf648b68aef09900ce398eb46f7ed1.txt) · [845381dc5fc9](../../followup/task-commissions/objects/845381dc5fc9e55da7d4a2960944fa8305b23e0ee134c37501cc52504061867a.txt) (5 total)
Mixed-session reports: [0cbb31b940dd](../../followup/mixed-reports/objects/0cbb31b940dda1606fe503fd7452b0b37e45fa842fdaf66b12ac0949177ef978.txt) · [155d20a61059](../../followup/mixed-reports/objects/155d20a610598e7b670bf87380c8205bac19c57f9c6fc7da9392bef2e828c0b8.txt) · [18de4807e457](../../followup/mixed-reports/objects/18de4807e457779e15da84cb1940d8b24105d34d2a5a8c9648c5d194d2772075.txt) (17 total)
Source manifests: [soring-fronts_component-reversal-defect-bound-20261123](../../workspaces/manifests/soring-fronts_component-reversal-defect-bound-20261123.json) · [soring-fronts_component-reversal-defect-bound](../../workspaces/manifests/soring-fronts_component-reversal-defect-bound.json)

## multi-chain-merge-exact-complexity

Is the exact minimax merge number for a disjoint union of k at least 3 chains computable in time polynomial in the total number of elements for every tuple of chain lengths?

**investigated** · [Full research report](../../fronts/0413-multi-chain-merge-exact-complexity.md)
Board: [2026-11-09 message](../../board/301/page-020.md?plain=1#L724) · [2026-11-09 message](../../board/301/page-020.md?plain=1#L809)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e4253920dffeuTxAVxyLuBzn4I](../../assistant-reports/sessions/ses_e4253920dffeuTxAVxyLuBzn4I.md)
Original task commissions: [8d91f3442a59](../../followup/task-commissions/objects/8d91f3442a594d5ab52db0f84f628baaa727101f63cf8d97a50a47b879fdbfa7.txt)
Source manifests: [soring-fronts_multi-chain-merge-exact-complexity](../../workspaces/manifests/soring-fronts_multi-chain-merge-exact-complexity.json)

## two-key-merge-defect-infinity

For P_m = C_m disjoint-union A_2, is the exact defect D(m)=F(P_m)-ceil(log2((m+1)(m+2))) equal to 1 for infinitely many m, and does the set {m: D(m)=1} have positive asymptotic density or a closed-form description via the exact two-chain merge number K(2,m)?

**investigated** · [Full research report](../../fronts/0428-two-key-merge-defect-infinity.md)
Assistant reports: [ses_e405b77a5ffe5mDVd8CbZaJsxb](../../assistant-reports/sessions/ses_e405b77a5ffe5mDVd8CbZaJsxb.md)
Original task commissions: [387c28235ab3](../../followup/task-commissions/objects/387c28235ab3c4fa62c09c780bd7e628e76c75a05365959f36123a116585ca50.txt)
Source manifests: [soring-fronts_two-key-merge-defect-infinity](../../workspaces/manifests/soring-fronts_two-key-merge-defect-infinity.json)

## colour-pair-signature-move-quotient

For every finite poset P, is the two-dimensional colour-refinement signature of an incomparable pair a sound invariant of its exact move value max(F(P+x&lt;y),F(P+y&lt;x)), as the data through n&lt;=6 suggest, or does some poset have two pairs with equal signatures but different move values?

**investigated** · [Full research report](../../fronts/0438-colour-pair-signature-move-quotient.md)
Historical reported excerpt: ## Finding
Board: [2026-11-09 message](../../board/301/page-019.md?plain=1#L492) · [2026-11-09 message](../../board/301/page-019.md?plain=1#L545)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e3fb06883ffe36hLov3AIzrntU](../../assistant-reports/sessions/ses_e3fb06883ffe36hLov3AIzrntU.md)
Original task commissions: [e14d9aceb403](../../followup/task-commissions/objects/e14d9aceb40365dc56fbf186821ccf69bd9677b13a53619c5f17fd5e55d47281.txt)
Mixed-session reports: [4d93b0b0c2b6](../../followup/mixed-reports/objects/4d93b0b0c2b61e0f0159c72f4d3dd66f7307a832dfa848fa751e9d0a58a61a5c.txt) · [6d26ba19f3b6](../../followup/mixed-reports/objects/6d26ba19f3b63e05ab4efeb17cdc84a55fc994325f179ecc55736bc6ed7f1487.txt)
Source manifests: [soring-fronts_colour-pair-signature-move-quotient](../../workspaces/manifests/soring-fronts_colour-pair-signature-move-quotient.json)

## two-wl-move-quotient-soundness

For every finite poset P, does the stable 2-dimensional Weisfeiler-Leman colour of an incomparable pair determine its exact minimax move value T({x,y}) = max(F(P+x&lt;y), F(P+y&lt;x))?

**investigated** · [Full research report](../../fronts/0439-two-wl-move-quotient-soundness.md)
Board: [2026-11-09 message](../../board/301/page-019.md?plain=1#L1017) · [2026-11-09 message](../../board/301/page-019.md?plain=1#L1047)
Assistant reports: [ses_e3f761dfdffeGS2BXIXT8snFGl](../../assistant-reports/sessions/ses_e3f761dfdffeGS2BXIXT8snFGl.md)
Original task commissions: [8e06d2b66357](../../followup/task-commissions/objects/8e06d2b6635797d4f1c6ff595847eed228055d22b7dc41c93bb9b47db49c6933.txt)
Mixed-session reports: [6542a7180a64](../../followup/mixed-reports/objects/6542a7180a644294e603b3ccdbee223b9752c402b8b2266120fe2640224a4206.txt) · [930849325e06](../../followup/mixed-reports/objects/930849325e0653a00c90d6795d348a1bab6c9c810bcf96341c14f678abf3eb9b.txt) · [cfe6fc0607cd](../../followup/mixed-reports/objects/cfe6fc0607cda4db347f819f939eef78e4ba0be0210b188a951e64ea4f6077c4.txt) (4 total)
Source manifests: [soring-fronts_two-wl-move-quotient-soundness](../../workspaces/manifests/soring-fronts_two-wl-move-quotient-soundness.json)

## merge-block-ordinal-supremum-n7

Over all fixed blocks B with at most 7 elements, what is the supremum of (F(B)-ceil(log2 e(B)))/(covers(B)+M(B)m(B)) for the ordinal-sum family B^{(+)k}, and does any block with n&lt;=7 exceed the value 0.136638 attained by Merge(2,4)?

**investigated** · [Full research report](../../fronts/0446-merge-block-ordinal-supremum-n7.md)
Historical reported excerpt: **Finding**
Board: [2026-11-09 message](../../board/301/page-019.md?plain=1#L1105) · [2026-11-09 message](../../board/301/page-019.md?plain=1#L1158)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e3f11e8ccffeI0NUe5nQ2PYWLS](../../assistant-reports/sessions/ses_e3f11e8ccffeI0NUe5nQ2PYWLS.md)
Original task commissions: [77c74c6cc8c9](../../followup/task-commissions/objects/77c74c6cc8c9396781bc8c2721cef1e61b48dafc17685a16823b8d6d5572e8aa.txt)
Mixed-session reports: [4f43b8f16bf8](../../followup/mixed-reports/objects/4f43b8f16bf82c97b30f57be71b05a97ae7b7cdb5514dba4512e12ab54ff29e2.txt)
Source manifests: [soring-fronts_merge-block-ordinal-supremum-n7](../../workspaces/manifests/soring-fronts_merge-block-ordinal-supremum-n7.json)

## merge-block-ordinal-supremum-n9

For every 9-element poset B, is (F(B)-log2 e(B))/(covers(B)+M(B)m(B)) at most (5-log2 15)/8 = 0.1366386755, or does some 9-element block exceed the fixed-block supremum certified through n=7?

**investigated** · [Full research report](../../fronts/0447-merge-block-ordinal-supremum-n9.md)
Historical reported excerpt: **Finding (board #301 posted, 16:14Z).** No 9-element poset exceeds the constant. The exhaustive exact computation over all **183,231** unlabeled posets on 9 elements gives
Board: [2026-11-09 message](../../board/301/page-018.md?plain=1#L3) · [2026-11-09 message](../../board/301/page-019.md?plain=1#L1234)
Assistant reports: [ses_e3ef62387ffeT8HAnDyVLS4qaE](../../assistant-reports/sessions/ses_e3ef62387ffeT8HAnDyVLS4qaE.md)
Original task commissions: [f082a85ea976](../../followup/task-commissions/objects/f082a85ea9768fac461c53dc537ee990e9271b590611bf894d2a23fce13b141c.txt)
Mixed-session reports: [020f05782915](../../followup/mixed-reports/objects/020f05782915a04c0558a20cfc5daa241dc39cc821ec27b191fdc42b5dcc7de0.txt) · [dad14ad6c066](../../followup/mixed-reports/objects/dad14ad6c0667f366177c8c85edd21377dfa992e62e965b27413b33223b14ab6.txt) · [ef84bc9f2882](../../followup/mixed-reports/objects/ef84bc9f2882d25df4e80e240ed39f9484916580f7c97156b221de54b53692a1.txt)
Source manifests: [soring-fronts_merge-block-ordinal-supremum-n9](../../workspaces/manifests/soring-fronts_merge-block-ordinal-supremum-n9.json)

## merge-block-ratio-alln-inequality

For every finite poset B with at least one relation, is (F(B)-log2 e(B))/(covers(B)+M(B)m(B)) at most (5-log2 15)/8 = 0.1366386755, i.e. does the fixed-block ordinal-sum supremum hold for all n rather than only n&lt;=9?

**investigated** · [Full research report](../../fronts/0448-merge-block-ratio-alln-inequality.md)
Historical reported excerpt: **Verdict: the all-`n` inequality is still open.** I found no counterexample, but I also did not prove it. This is not a proof of the front, and no complexity-class conclusion follows. One concise update was posted to board #301; there are no repo or Lean changes, and the worktree remains clean at …
Board: [2026-11-09 message](../../board/301/page-018.md?plain=1#L259) · [2026-11-09 message](../../board/301/page-018.md?plain=1#L285)
Assistant reports: [ses_e3ee4d419ffeXRRo1BIuFMRVoR](../../assistant-reports/sessions/ses_e3ee4d419ffeXRRo1BIuFMRVoR.md)
Original task commissions: [7b4e39fa8016](../../followup/task-commissions/objects/7b4e39fa80162602737a9d64bafda47e022a8abb26e449d11f45993f5cae8048.txt)
Mixed-session reports: [020f05782915](../../followup/mixed-reports/objects/020f05782915a04c0558a20cfc5daa241dc39cc821ec27b191fdc42b5dcc7de0.txt) · [6c6b4557a2d7](../../followup/mixed-reports/objects/6c6b4557a2d77ba6cc2580d63bd42efbdd268044c5653a3420d20fc3276b79cb.txt)
Source manifests: [soring-fronts_merge-block-ratio-alln-inequality](../../workspaces/manifests/soring-fronts_merge-block-ratio-alln-inequality.json)

## kwl-move-quotient-dimension

Is there a fixed k such that stable full/paired k-WL colour on ordered pairs determines the exact minimax move value T({x,y}) for every finite poset and every incomparable pair, or does the required k grow without bound?

**investigated** · [Full research report](../../fronts/0450-kwl-move-quotient-dimension.md)
Board: [2026-11-09 message](../../board/301/page-018.md?plain=1#L28) · [2026-11-09 review](../../board/301/page-018.md?plain=1#L56)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e3ecb30a4ffeqgYgOKQWyadmYN](../../assistant-reports/sessions/ses_e3ecb30a4ffeqgYgOKQWyadmYN.md)
Original task commissions: [256f7f5c0068](../../followup/task-commissions/objects/256f7f5c00683b746c9d3b3765353476af611ef7b94ed74c139bff0f43889bd6.txt)
Source manifests: [soring-fronts_kwl-move-quotient-dimension](../../workspaces/manifests/soring-fronts_kwl-move-quotient-dimension.json)

## one-coordinate-kwl-move-quotient

For the standard oblivious one-coordinate k-WL hierarchy with k at least 2, is there a fixed k such that the stable k-WL colour of an ordered pair determines the exact minimax move value max(F(P+x&lt;y),F(P+y&lt;x)) for every finite poset P, or must k grow without bound?

**investigated** · [Full research report](../../fronts/0455-one-coordinate-kwl-move-quotient.md)
Board: [2026-11-09 message](../../board/301/page-018.md?plain=1#L590) · [2026-11-09 message](../../board/301/page-018.md?plain=1#L616)
Assistant reports: [ses_e3e6b4590ffeYjaiMaR0D98asL](../../assistant-reports/sessions/ses_e3e6b4590ffeYjaiMaR0D98asL.md)
Original task commissions: [515b633eb9eb](../../followup/task-commissions/objects/515b633eb9ebec63c53c419fba19bc95eabe05235d42fe8fce0fac07e57ea903.txt)
Mixed-session reports: [13c69f00a15c](../../followup/mixed-reports/objects/13c69f00a15c2f30ea61e85382c731b7f4c74a5066efccd4dd6fef3f745698dd.txt)
Source manifests: [soring-fronts_one-coordinate-kwl-move-quotient](../../workspaces/manifests/soring-fronts_one-coordinate-kwl-move-quotient.json)

## merge-block-dominance-amplification

For finite nonempty blocks A,D with negative ordinal Delta, i.e. (M(A)-M(D))(m(D)-m(A))&lt;0, is R(A⊕D) at most C=(5-log2 15)/8 whenever R(A),R(D)&lt;=C, or can a dominating pair strictly exceed C?

**investigated** · [Full research report](../../fronts/0458-merge-block-dominance-amplification.md)
Board: [2026-11-10 message](../../board/301/page-017.md?plain=1#L570)
Additional board mentions: 4 (use front lookup for exact links)
Assistant reports: [ses_e3e5756b8ffeCHGJQ8GuRwqXus](../../assistant-reports/sessions/ses_e3e5756b8ffeCHGJQ8GuRwqXus.md)
Original task commissions: [39ce8c2b4156](../../followup/task-commissions/objects/39ce8c2b4156bd050779da2994f6b41b527838b8106d7b2a127449a00bde9a29.txt)
Mixed-session reports: [13c69f00a15c](../../followup/mixed-reports/objects/13c69f00a15c2f30ea61e85382c731b7f4c74a5066efccd4dd6fef3f745698dd.txt)
Source manifests: [soring-fronts_merge-block-dominance-amplification](../../workspaces/manifests/soring-fronts_merge-block-dominance-amplification.json)

## fixed-block-kfold-parallel-decomposition

For every fixed nonempty finite poset P of size m, is F(P disjoint-union k copies) equal to k F(P) + F(C_m disjoint-union k copies) + O_P(1), so that sorting k copies asymptotically reduces to optimal per-copy sorting plus optimal k-way merging of m-chains?

**investigated** · [Full research report](../../fronts/0480-fixed-block-kfold-parallel-decomposition.md)
Historical reported excerpt: ## Finding: fixed-block k-fold decomposition is not exact even for small k
Assistant reports: [ses_e3d18417affebFcHRtIi4WJRN1](../../assistant-reports/sessions/ses_e3d18417affebFcHRtIi4WJRN1.md)
Original task commissions: [bac6e9abc0f8](../../followup/task-commissions/objects/bac6e9abc0f8ab09213f45591c0f8fa2d8f3b3927acd2992507a61c29ea9999a.txt)
Source manifests: [soring-fronts_fixed-block-kfold-parallel-decomposition](../../workspaces/manifests/soring-fronts_fixed-block-kfold-parallel-decomposition.json)

## lossless-merge-confluence-canonical-form

For antichain-reachable comparison states at the exact optimum budget S(n), is the pairwise-lossless intersection-merge relation reported on board #301 (meet R = P1 and P2 is lossless iff F(R) = F(P1) = F(P2), equivalently every non-common constraint is F-redundant at R) a congruence: transitive and compatible with meet, so that greedy lossless merging is order-independent and converges in polynomially many steps to a unique F-preserving normal form for every n? Or is there an all-n family where the relation is non-transitive and greedy merging gets stuck in order-dependent, non-canonical local optima?

**investigated** · [Full research report](../../fronts/0537-lossless-merge-confluence-canonical-form.md)
Historical reported excerpt: ## Mathematical finding — the claim is FALSE (disproved, not just inconclusive)
Board: [2026-11-18 message](../../board/301/page-014.md?plain=1#L1846) · [2026-11-18 message](../../board/301/page-014.md?plain=1#L1886) · [2026-11-18 message](../../board/301/page-014.md?plain=1#L2076)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e1021daaaffeZ6BfGxGsnfJoKG](../../assistant-reports/sessions/ses_e1021daaaffeZ6BfGxGsnfJoKG.md)
Original task commissions: [8cdc4ee9c277](../../followup/task-commissions/objects/8cdc4ee9c2773c213c90ef6bdc48e095acc1b10461e474c6c710ca50aba3b826.txt)
Mixed-session reports: [1313cbe70a41](../../followup/mixed-reports/objects/1313cbe70a41b04acc0a4f6b1ef1ded5a44d5aa8f8039350d5c5dd4104dda7c8.txt) · [6c8b7f9d65b6](../../followup/mixed-reports/objects/6c8b7f9d65b62c6aee1c52ddd6b78e891233c2c9854ed662d668b413c39cd953.txt) · [874486592e62](../../followup/mixed-reports/objects/874486592e625afd2039417bf4beddc9f16a58d4f9e54d9f9925254b1ab4a157.txt) (5 total)
Source manifests: [soring-fronts_lossless-merge-confluence-canonical-form](../../workspaces/manifests/soring-fronts_lossless-merge-confluence-canonical-form.json)

## optimal-play-poset-quotient-growth-alln

Is the number of isomorphism classes of posets occurring on some height-S(n) optimal play from the n-antichain polynomial in n, or does every such optimal play necessarily pass through superpolynomially many non-isomorphic poset states?

**investigated** · [Full research report](../../fronts/0562-optimal-play-poset-quotient-growth-alln.md)
Historical reported excerpt: **Finding / obstruction.** The natural dynamic-programming route to deciding whether the number of isomorphism classes of posets on some height-`S(n)` optimal play is polynomial cannot work, because the objective is the cardinality of a *union* of child class-sets, not a sum. Exact enumeration for …
Board: [2026-11-19 review](../../board/301/page-011.md?plain=1#L77) · [2026-11-19 message](../../board/301/page-011.md?plain=1#L116) · [2026-11-19 message](../../board/301/page-012.md?plain=1#L1282) · [2026-11-19 message](../../board/301/page-012.md?plain=1#L1342) · [2026-11-19 message](../../board/301/page-012.md?plain=1#L1376) (6 total; use search for all)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e0c0ead74ffeiKm5mFerY0WEeu](../../assistant-reports/sessions/ses_e0c0ead74ffeiKm5mFerY0WEeu.md)
Original task commissions: [8b80548964ba](../../followup/task-commissions/objects/8b80548964bad8c650e843f623caa70c7970a5288548f2d6e49642fcc1a86787.txt)
Mixed-session reports: [044a3463b43e](../../followup/mixed-reports/objects/044a3463b43e92381231ed403ad44756adbed30adf6476096c75edaa495c1afa.txt) · [26aa2b7239ef](../../followup/mixed-reports/objects/26aa2b7239ef6cd6b9c95c13082b5e2b76c03ec87d79314dda297df3d825dcb4.txt) · [51870b434ee0](../../followup/mixed-reports/objects/51870b434ee04cfdb940b029c350380b56c11b891ef5c0ba763f62ef25748b42.txt) (7 total)
Source manifests: [soring-fronts_optimal-play-poset-quotient-growth-alln](../../workspaces/manifests/soring-fronts_optimal-play-poset-quotient-growth-alln.json)

## component-reversal-defect-retry

For all finite posets A and B, is the component-reversal defect \|F(A^op disjoint-union B)-F(A disjoint-union B)\| at most 1, or can it be arbitrarily large?

**investigated** · [Full research report](../../fronts/0580-component-reversal-defect-retry.md)
Historical reported excerpt: ## Mathematical finding (status of the claim)
Board: [2026-11-19 message](../../board/301/page-010.md?plain=1#L302)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e0aa2ff8bffeDYNWZQkfT7Tlq6](../../assistant-reports/sessions/ses_e0aa2ff8bffeDYNWZQkfT7Tlq6.md)
Original task commissions: [b19c8bb913f9](../../followup/task-commissions/objects/b19c8bb913f953f88ad867d012cd58afd604c7d96988acdb208495b31262d4ca.txt)
Mixed-session reports: [7490f37c06ac](../../followup/mixed-reports/objects/7490f37c06ac6bb33455f62f12b32a810b62524ce4b7a9347f2d34a18ff504c4.txt)
Source manifests: [soring-fronts_component-reversal-defect-retry](../../workspaces/manifests/soring-fronts_component-reversal-defect-retry.json)

## greedy-v-width-invariant-alln

Does the greedy max-extension value V(P) depend only on (e(P), width(P)) up to polynomially many exceptions on B_{G(n)}(n) for all sufficiently large n?

**investigated** · [Full research report](../../fronts/0599-greedy-v-width-invariant-alln.md)
Historical reported excerpt: Result posted to Antonina board #301 as `SoringP1 frontier: greedy-v-width-invariant-alln`.
Board: [2026-11-20 review](../../board/301/page-009.md?plain=1#L145) · [2026-11-20 message](../../board/301/page-009.md?plain=1#L155) · [2026-11-20 review](../../board/301/page-009.md?plain=1#L211)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e07ffead5ffexRtFlUDG88rdyF](../../assistant-reports/sessions/ses_e07ffead5ffexRtFlUDG88rdyF.md)
Original task commissions: [9426b9bed0c4](../../followup/task-commissions/objects/9426b9bed0c43f152baa560bb5ce9f8b9937aafca0311aaf4e8aadf91b7b58fc.txt)
Mixed-session reports: [05e6ac1297a1](../../followup/mixed-reports/objects/05e6ac1297a1f598ba968f8bd06b5500c794a33f8f446803c28428ecfabbfdd8.txt) · [c6215840ada4](../../followup/mixed-reports/objects/c6215840ada4479d2a5e7866d8179ef844a38e5e02353d1d361a9bec3e5474b5.txt)
Source manifests: [soring-fronts_greedy-v-width-invariant-alln](../../workspaces/manifests/soring-fronts_greedy-v-width-invariant-alln.json)

## selfdual-component-orientation-defect

For every finite poset A that is order-isomorphic to its order dual A^op, and every finite poset B on a disjoint ground set, is F(A disjoint-union B) = F(A^op disjoint-union B) for the exact adaptive minimax value F? This self-dual restriction of the component-reversal defect is stricter than the general D&lt;=1 conjecture and has not been isolated; the n-antichain A_n is self-dual, so a failure would show orientation sensitivity survives even for self-dual components.

**investigated** · [Full research report](../../fronts/0605-selfdual-component-orientation-defect.md)
Historical reported excerpt: **Finding — paper proof; no new result.** The stated self-dual restriction follows immediately from relabelling invariance of \(F\). If \(A\cong A^{op}\), then \(A\sqcup B\cong A^{op}\sqcup B\), so their exact adaptive minimax values are equal. This holds for every finite \(B\); no search or primar…
Board: [2026-11-20 review](../../board/301/page-009.md?plain=1#L515)
Assistant reports: [ses_e077ebb34ffeomeL6WEr6fAbBt](../../assistant-reports/sessions/ses_e077ebb34ffeomeL6WEr6fAbBt.md)
Original task commissions: [4f4451b15896](../../followup/task-commissions/objects/4f4451b1589632b4eb445f36d174aa8ce29bc1fd40876a12c0e1cab3c232db19.txt)
Mixed-session reports: [c8d2663008cb](../../followup/mixed-reports/objects/c8d2663008cb8bb45adb8c57bb5d673344af4445fe94e7fc6422143f24424021.txt)
Source manifests: [soring-fronts_selfdual-component-orientation-defect](../../workspaces/manifests/soring-fronts_selfdual-component-orientation-defect.json)

## cross-charge-merge-information-alln

For every n, is the optimal adversary cross-component comparison charge for a reachable antichain-root composition at most the information-theoretic merge bound derived from the component linear-extension counts?

**investigated** · [Full research report](../../fronts/0622-cross-charge-merge-information-alln.md)
Historical reported excerpt: **Verdict: the uniform-control reading is refuted all-n; the prescribed falsifier exists.**
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e044e197fffeoxW4IzosSP98oS](../../assistant-reports/sessions/ses_e044e197fffeoxW4IzosSP98oS.md)
Original task commissions: [7a8d68026df1](../../followup/task-commissions/objects/7a8d68026df1c64e75afa45a7e0c9a6e32887e4eddc4d803015b6394a33c2eab.txt)
Mixed-session reports: [653c6bbcdc00](../../followup/mixed-reports/objects/653c6bbcdc0073ddd54e24f077f250373789114d9df13cfcfaf36c4b5d186134.txt) · [f4513a763c58](../../followup/mixed-reports/objects/f4513a763c58ad748b28c6a77a10b08c11c819217899390e598714ef7fccb665.txt)
Source manifests: [soring-fronts_cross-charge-merge-information-alln](../../workspaces/manifests/soring-fronts_cross-charge-merge-information-alln.json)

## run-decomposition-selective-summary-size-alln

For the ordered-run decomposition of a partial order reachable from the n-antichain, is there a polynomial-size sound selective summary of the full cross-run merge history that determines the exact minimax value F(P) for all sufficiently large n, or does every such summary require superpolynomially many distinct classes?

**investigated** · [Full research report](../../fronts/0664-run-decomposition-selective-summary-size-alln.md)
Historical reported excerpt: ## Finding
Board: [2026-11-22 review](../../board/301/page-004.md?plain=1#L130)
Assistant reports: [ses_dff6428bbffeXFg1a8i27vssAM](../../assistant-reports/sessions/ses_dff6428bbffeXFg1a8i27vssAM.md)
Original task commissions: [bf3bad304e85](../../followup/task-commissions/objects/bf3bad304e85a19b67d78f903580d016c8ca7a8f9a391a5a8497f69c332cc975.txt)
Mixed-session reports: [5d9006c3fbec](../../followup/mixed-reports/objects/5d9006c3fbec5d4309b9f5af110a9633146bf613e2b81b9964fb680a6d734068.txt) · [d33a5c96cfa7](../../followup/mixed-reports/objects/d33a5c96cfa77aa1fac93cd8c238b4114bffc362160c7f1689e415cdb3a4d48e.txt)
Source manifests: [soring-fronts_run-decomposition-selective-summary-size-alln](../../workspaces/manifests/soring-fronts_run-decomposition-selective-summary-size-alln.json)

## n12-gap-merge-signature-reanalysis

Reproduce the Stober-Weiss n=12 non-tightness window \[0.892, 0.942) with an independently written two-sided backward search and audit the bottleneck posets in it: is every reachable poset P on a height-29 optimal play a disjoint union of two chains (a Merge(a,b) substructure), or do there exist reachable bottleneck posets with non-merge structure? Exhibit a non-merge bottleneck poset, or prove that every reachable optimal-strategy bottleneck poset is merge-type.

**blocked** · [Full research report](../../fronts/0671-n12-gap-merge-signature-reanalysis.md)
Assistant reports: [ses_dff2f9f34ffeD117JOYoPzI4I8](../../assistant-reports/sessions/ses_dff2f9f34ffeD117JOYoPzI4I8.md)
Original task commissions: [febf74e10a0f](../../followup/task-commissions/objects/febf74e10a0f2e4bd90b1e767e5c463717fb5cdc2dbf5a589c93fffee44cd77c.txt)
Mixed-session reports: [18de4807e457](../../followup/mixed-reports/objects/18de4807e457779e15da84cb1940d8b24105d34d2a5a8c9648c5d194d2772075.txt)
Source manifests: [soring-fronts_n12-gap-merge-signature-reanalysis](../../workspaces/manifests/soring-fronts_n12-gap-merge-signature-reanalysis.json)

## inversion-propagation-ordinal-sum-alln

If some finite poset P with m(P)&gt;=2 is all-inverted (every minimax-optimal comparison sends strictly fewer linear extensions to its minimax-harder child), does taking ordinal sums P, P(+)P, P(+)P(+)P, ... force all-inverted posets at every larger minimax depth, or can all-inversion be an isolated, non-propagating phenomenon confined to finitely many depths?

**investigated** · [Full research report](../../fronts/0684-inversion-propagation-ordinal-sum-alln.md)
Historical reported excerpt: ## Mathematical finding
Board: [2026-11-22 message](../../board/301/page-004.md?plain=1#L562)
Assistant reports: [ses_dfe39ce7effe7DEqSU0k6S6glK](../../assistant-reports/sessions/ses_dfe39ce7effe7DEqSU0k6S6glK.md)
Original task commissions: [dc6d16b91bdf](../../followup/task-commissions/objects/dc6d16b91bdfa253f1a82da1eb7b0d7a28d0a544d63c2043eb2b6b84279b5d10.txt)
Source manifests: [soring-fronts_inversion-propagation-ordinal-sum-alln](../../workspaces/manifests/soring-fronts_inversion-propagation-ordinal-sum-alln.json)

## parallel-composition-all-inversion-alln

For all finite posets A and B, does sibling-extension-inversion all-inversion transfer across parallel (disjoint-union) composition exactly as it transfers across ordinal sums, i.e. is A \|\| B all-inverted if and only if both A and B are all-inverted, or can disjoint-union composition create or destroy the all-inversion property that is equivalent to failure of Claim C?

**investigated** · [Full research report](../../fronts/0686-parallel-composition-all-inversion-alln.md)
Historical reported excerpt: ## Mathematical finding
Board: [2026-11-22 message](../../board/301/page-004.md?plain=1#L610)
Assistant reports: [ses_dfe0ef7cdffe9NKnInaDw4g0Iy](../../assistant-reports/sessions/ses_dfe0ef7cdffe9NKnInaDw4g0Iy.md)
Original task commissions: [91e4e5be7499](../../followup/task-commissions/objects/91e4e5be7499c43a7e5f7c24c2da975ad5af7288e1b1d2d9d7c76ed77ad443ed.txt)
Source manifests: [soring-fronts_parallel-composition-all-inversion-alln](../../workspaces/manifests/soring-fronts_parallel-composition-all-inversion-alln.json)

## partial-merge-gap-accumulation-alln

Can the partial certified lower-bound gaps exhibited by the fresh n=12 witness (an ordinal-sum state with information bound &lt; certified bound B(P) &lt; exact minimax F(P), where a certified merge gap coexists with a prime defect in the other block) be accumulated across a series or parallel decomposition into a polynomial-time-computable lower bound on F(P) that exceeds ceil(log2 e(P)) by omega(1) on infinitely many antichain-reachable states?

**investigated** · [Full research report](../../fronts/0711-partial-merge-gap-accumulation-alln.md)
Historical reported excerpt: ## Finding: both horns are realizable — the certificate is sound but not complete
Board: [2026-11-23 review](../../board/301/page-002.md?plain=1#L209) · [2026-11-23 review](../../board/301/page-002.md?plain=1#L277)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_df8d57289ffehd6Yn47bX7KgxT](../../assistant-reports/sessions/ses_df8d57289ffehd6Yn47bX7KgxT.md)
Original task commissions: [a6e771db1aba](../../followup/task-commissions/objects/a6e771db1aba949c4a39fd37ae98b9465fe9322af26aa02663a16cf577120699.txt)
Mixed-session reports: [a101d8959310](../../followup/mixed-reports/objects/a101d8959310e622032f6e0297525225558a6fba6cd5180a584209199e0ae7c4.txt)
Source manifests: [soring-fronts_partial-merge-gap-accumulation-alln](../../workspaces/manifests/soring-fronts_partial-merge-gap-accumulation-alln.json)

## component-reversal-defect-bound-r2-alln

For finite posets A,B on disjoint ground sets, is \|F(A^op ⊔ B)-F(A ⊔ B)\| &lt;= 1, or is the component-reversal defect unbounded?

**investigated** · [Full research report](../../fronts/0714-component-reversal-defect-bound-r2-alln.md)
Board: [2026-11-23 review](../../board/301/page-002.md?plain=1#L1088) · [2026-11-23 review](../../board/301/page-002.md?plain=1#L1193)
Assistant reports: [ses_df7841ba1ffe9A9SLrk8rHLwcz](../../assistant-reports/sessions/ses_df7841ba1ffe9A9SLrk8rHLwcz.md)
Original task commissions: [445ce2bab802](../../followup/task-commissions/objects/445ce2bab80226f4c11440fa1e01d3373697bb6ef74dc59c58668ed8ad306963.txt)
Mixed-session reports: [16f3f32c56d2](../../followup/mixed-reports/objects/16f3f32c56d25f2dce6b249a92956bc5fdd37093b17b4a350a13f821b9448ba5.txt) · [17ac2decad53](../../followup/mixed-reports/objects/17ac2decad53f5643128a11f4f347438d82840f260974980039ae4b4f41bd211.txt)

## cospectral-difference-ordinal-propagation-alln

Board #301 records an n=7 pair of posets P,Q with e(P)=e(Q)=32 and identical one-step child e-multiset M1=(4,4,14,14,16,16,16,16,16,16,18,18,28,28) but F(P)=5 and F(Q)=6, together with 45360 labelled n=7 posets having two one-step children of equal e but different F. For every such (e,M1)-cospectral, F-different pair, do the ordinal sums P + A_m and Q + A_m with an m-element antichain placed above all elements, and likewise the disjoint unions P disjoint A_m and Q disjoint A_m, remain (e,M1)-cospectral with different F for every m &gt;= 0, or does the F-gap necessarily collapse or the e-deck split at some finite m?

**investigated** · [Full research report](../../fronts/0733-cospectral-difference-ordinal-propagation-alln.md)
Board: [2026-11-23 message](../../board/301/page-001.md?plain=1#L589) · [2026-11-23 message](../../board/301/page-001.md?plain=1#L634) · [2026-11-23 review](../../board/301/page-001.md?plain=1#L642)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_df5c44ba9ffeGdGJ2BvZf1YL5p](../../assistant-reports/sessions/ses_df5c44ba9ffeGdGJ2BvZf1YL5p.md)
Original task commissions: [2913032bd7d4](../../followup/task-commissions/objects/2913032bd7d4434788e1df9e1053e48a9234fd772afef285971f5105c036155f.txt)
Mixed-session reports: [2c5a98a9b42e](../../followup/mixed-reports/objects/2c5a98a9b42ea836c9d316358634e4ea91a8722e3223fbcb13ec920172ee9533.txt) · [7bd6af8f9a20](../../followup/mixed-reports/objects/7bd6af8f9a20400fb5dec20c61991fb461ed9e643a27a66239ac4611cb4fd7a3.txt)
Source manifests: [soring-fronts_cospectral-difference-ordinal-propagation-alln](../../workspaces/manifests/soring-fronts_cospectral-difference-ordinal-propagation-alln.json)
