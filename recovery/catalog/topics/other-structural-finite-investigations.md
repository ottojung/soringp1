# Other structural / finite investigations

[Catalogue home](../README.md) · [Evidence status guide](../../RESULTS.md)

Status is the original workflow label, not mathematical proof. Linked messages may contain corrections or rejected claims.

## nonchain-boundary-ceiling-evasion

For every fixed c, must every stage sequence from the n-antichain to a total order, with per-stage height at most c*log2(n+2) applied uniformly to all extensions of an arbitrary (not chain or merge-tree) boundary invariant, pay aggregate ceiling rounding loss Omega(n) across sufficiently large n, or can some boundary class preserving cross-chain correlations evade it with o(n) total loss?

**investigated** · [Full research report](../../fronts/0007-nonchain-boundary-ceiling-evasion.md)
Board: [2026-10-27 message](../../board/301/page-044.md?plain=1#L48)
Source manifests: [soring-fronts_nonchain-boundary-ceiling-evasion](../../workspaces/manifests/soring-fronts_nonchain-boundary-ceiling-evasion.json)

## power-of-two-increment-exactness

Does the optimal increment d(2^k) = S(2^k) - S(2^k - 1) equal ceil(log2(2^k)) = k for every k &gt;= 1, or does there exist a power of two where any optimal sorting tree beats the strict two-phase worst case S(2^k - 1) + k, as already happens for non-powers like n = 9 and n = 17..21?

**investigated** · [Full research report](../../fronts/0015-power-of-two-increment-exactness.md)
Historical reported excerpt: ## Finding: unresolved
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_power-of-two-increment-exactness](../../workspaces/manifests/soring-fronts_power-of-two-increment-exactness.json)

## equal-extensions-equal-height

For all n and all posets P, Q on the same n labelled-or-relabelled elements with identical linear-extension count e(P) = e(Q), do P and Q always have equal minimax sorting height S(P) = S(Q), so that the extension count alone determines the reachable game value?

**investigated** · [Full research report](../../fronts/0020-equal-extensions-equal-height.md)
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_equal-extensions-equal-height](../../workspaces/manifests/soring-fronts_equal-extensions-equal-height.json)

## increment-cost-of-adding-one-key

Is the incremental sorting cost S(n+1)-S(n) ever greater than 1 for any n, or is S strictly 0/1-incremental across all n?

**investigated** · [Full research report](../../fronts/0023-increment-cost-of-adding-one-key.md)
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_increment-cost-of-adding-one-key](../../workspaces/manifests/soring-fronts_increment-cost-of-adding-one-key.json)

## forgetful-join-exponential-classes

For forgetful framed DAG certificates of exact S(n), does there exist an all-n family of root-reachable poset histories whose pairwise joins produce Omega(2^(c n)) distinct feasible order classes at fixed depth?

**investigated** · [Full research report](../../fronts/0026-forgetful-join-exponential-classes.md)
Additional board mentions: 1 (use front lookup for exact links)
Mixed-session reports: [d4d56b88e56c](../../followup/mixed-reports/objects/d4d56b88e56ce25c5a53b7fe2a611c662afe9c2cf0fe12523ccbe3db6b320e21.txt)
Source manifests: [soring-fronts_forgetful-join-exponential-classes](../../workspaces/manifests/soring-fronts_forgetful-join-exponential-classes.json)

## exact-reset-forgetful-completeness-barrier

For forgetful framed DAG certificates of exact S(n), is polynomial-size completeness (all optimal strategies coverable) equivalent to exact-reset, and does there exist an all-n family where forgetful joins force exponentially many classes making polynomial completeness impossible?

**investigated** · [Full research report](../../fronts/0027-exact-reset-forgetful-completeness-barrier.md)
Source manifests: [soring-fronts_exact-reset-forgetful-completeness-barrier](../../workspaces/manifests/soring-fronts_exact-reset-forgetful-completeness-barrier.json)

## n32-power-of-two-increment

For n=32 (first power of two beyond known exact values through n=22), determine d(32)=S(32)-S(31) relative to ceil(log2 32)=5 - does the strict two-phase increment equal k for powers of two, or does optimal play beat S(2^k - 1)+k?

**investigated** · [Full research report](../../fronts/0029-n32-power-of-two-increment.md)
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_n32-power-of-two-increment](../../workspaces/manifests/soring-fronts_n32-power-of-two-increment.json)

## fixed-poly-time-lower-bound

For some fixed constant c &gt;= 2, is SORT-BOUND-U not decidable in deterministic time O(N^c) on unary inputs of length N, or is there an all-n construction beating every fixed polynomial?

**investigated** · [Full research report](../../fronts/0034-fixed-poly-time-lower-bound.md)
Historical reported excerpt: ### Conclusion (honest limits)
Additional board mentions: 2 (use front lookup for exact links)
Source manifests: [soring-fronts_fixed-poly-time-lower-bound](../../workspaces/manifests/soring-fronts_fixed-poly-time-lower-bound.json)

## n12-obstruction-generalization

What combinatorial invariant causes S(12)-C(12)=1 (the n=12 obstruction)? Does this invariant generalize to an infinite family where S(n)-C(n) &gt;= c*something or creates a uniform lower-bound barrier?

**investigated** · [Full research report](../../fronts/0037-n12-obstruction-generalization.md)
Historical reported excerpt: **Finding:** No known uniform invariant explains all excess values. The n=12 obstruction is structural/global (routing of all n! permutations through the decision tree) - Peczarski notes sortability not monotone in e and symmetry can help; Stober-Weiss show it's certified by exhaustive search (Well…
Additional board mentions: 2 (use front lookup for exact links)
Mixed-session reports: [3c8bc34c24c1](../../followup/mixed-reports/objects/3c8bc34c24c1ca25ece5361765c290d788243251ab2c1db97f6119a4dc5dd5a2.txt)
Source manifests: [soring-fronts_n12-obstruction-generalization](../../workspaces/manifests/soring-fronts_n12-obstruction-generalization.json)

## increment-monotonicity-dyadic

Is d(n)=S(n)-S(n-1) non-decreasing in n, and is d(2^k)=k (insertion lower bound achieved at powers of two)? For known n&lt;=22 values d appears non-decreasing and equals ceil(log2 n) at powers of two; prove or disprove general all-n monotonicity and characterize when d(n)=ceil(log2 n).

**investigated** · [Full research report](../../fronts/0043-increment-monotonicity-dyadic.md)
Historical reported excerpt: ### Conclusion (tried to disprove)
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_increment-monotonicity-dyadic](../../workspaces/manifests/soring-fronts_increment-monotonicity-dyadic.json)

## sorting-number-increment-convexity

Is d(n)=S(n)-S(n-1) non-decreasing in n (i.e. is S(n) discretely convex)? Known values up to n&lt;=18 show d non-decreasing; prove all-n monotonicity or exhibit a counterexample. Also relate to the two-phase/power-of-two result d(2^k)=k.

**investigated** · [Full research report](../../fronts/0044-sorting-number-increment-convexity.md)
Source manifests: [soring-fronts_sorting-number-increment-convexity](../../workspaces/manifests/soring-fronts_sorting-number-increment-convexity.json)

## branch-divisibility-generalization

The exact-reset realizability obstruction (odd antichain-to-star impossible by root branch divisibility) is a local condition; is there an all-n theorem characterizing exactly which poset pairs (F,F') admit an exact reset comparison tree, and does the antichain-to-any-non-chain obstruction generalize beyond stars to a wider family for certain n?

**investigated** · [Full research report](../../fronts/0046-branch-divisibility-generalization.md)
Source manifests: [soring-fronts_branch-divisibility-generalization](../../workspaces/manifests/soring-fronts_branch-divisibility-generalization.json)

## winning-frontier-sparsity-threshold

The winning-frontier barrier shows 2^((1/4-o(1)) n (log n)^2) nonisomorphic winning states exist at depths around information bound including at S(n); is there a critical depth t0(n) &lt; S(n) (or relative to C(n)) below which the winning frontier becomes polynomial in n, and above which it becomes super-polynomial for all sufficiently large n?

**investigated** · [Full research report](../../fronts/0047-winning-frontier-sparsity-threshold.md)
Board: [2026-10-31 message](../../board/301/page-040.md?plain=1#L292)
Source manifests: [soring-fronts_winning-frontier-sparsity-threshold](../../workspaces/manifests/soring-fronts_winning-frontier-sparsity-threshold.json)

## selfreducible-minimax-p-hard

Is the unary threshold language SORT-BOUND-U P-hard under log-space many-one reductions via self-reducibility of the poset minimax recurrence, or does the sparse unary encoding and the antichain structure block all known P-hardness reductions?

**investigated** · [Full research report](../../fronts/0048-selfreducible-minimax-p-hard.md)
Historical reported excerpt: **Finding (mathematical):** No logspace many-one reduction from a P-complete language to `SORT-BOUND-U` exists by the standard reduction schema; the obstruction is structural, not just sparsity.
Additional board mentions: 2 (use front lookup for exact links)
Source manifests: [soring-fronts_selfreducible-minimax-p-hard](../../workspaces/manifests/soring-fronts_selfreducible-minimax-p-hard.json)

## permutohedron-shelling-depth

Is the minimum worst-case depth of any shelling order of the n-permutohedron equal to S(n) for all n&gt;=1, and does that combinatorial identity create a new all-n invariant separating it from arbitrary partial orders?

**investigated** · [Full research report](../../fronts/0051-permutohedron-shelling-depth.md)
Historical reported excerpt: **FINDING (falsification):** The identity fails. For the n-permutohedron, shelling orders of the associated Coxeter/permutohedron complex correspond to maximal chains in the weak Bruhat order (edge moves = adjacent transpositions), so their worst-case "depth" in move-count is $h(W_n)=\binom{n}{2}=\…
Source manifests: [soring-fronts_permutohedron-shelling-depth](../../workspaces/manifests/soring-fronts_permutohedron-shelling-depth.json)

## insertion-lower-bound-universality

Is d(n)=S(n)-S(n-1) &gt;= ceil(log2 n) for all n&gt;=1 (the element-insertion information bound) always achievable in the sense that S(n)=S(n-1)+ceil(log2 n) for infinitely many n, or do there exist infinitely many n where every optimal strategy pays strictly more than ceil(log2 n) to insert the nth element?

**investigated** · [Full research report](../../fronts/0058-insertion-lower-bound-universality.md)
Historical reported excerpt: **Finding (disproof by known counterexamples):** The inequality is false for global S(n). From established exact values (Knuth/OEIS A036604, Peczarski, Stober–Weiß):
Board: [2026-10-30 message](../../board/301/page-043.md?plain=1#L367)
Source manifests: [soring-fronts_insertion-lower-bound-universality](../../workspaces/manifests/soring-fronts_insertion-lower-bound-universality.json)

## state-orbit-compression-necessity

For the poset/state graph of the weak order under prefix comparisons, let O(n) be the number of isomorphism orbits of states reachable by some height-S(n) strategy for permutations of n. Is O(n) necessarily super-polynomial in n for all large n, or does there exist some all-n family of height-S(n) strategies whose reachable orbit set has \|O(n)\| = n^(O(1))?

**investigated** · [Full research report](../../fronts/0061-state-orbit-compression-necessity.md)
Historical reported excerpt: Conclusion: this front remains open in both directions; the 15:29Z post is the complete and accurate record. I'm stopping without repository changes or additional posts.
Additional board mentions: 3 (use front lookup for exact links)
Mixed-session reports: [c77e4a1ba4a4](../../followup/mixed-reports/objects/c77e4a1ba4a43a312fd4284eb12d100583f8bad093bbec779c96bf5edd06eb74.txt)
Source manifests: [soring-fronts_state-orbit-compression-necessity](../../workspaces/manifests/soring-fronts_state-orbit-compression-necessity.json)

## minimax-state-count-polynomial

For the kernel-checked minimax recurrence adv(S) on antichain subsets of permutations, is there an infinite all-n family of optimal decision paths that together force super-polynomially many distinct (S, context) states even when identified up to the strongest known relabeling that preserves root-optimal play?

**investigated** · [Full research report](../../fronts/0063-minimax-state-count-polynomial.md)
Board: [2026-10-30 message](../../board/301/page-043.md?plain=1#L401)
Source manifests: [soring-fronts_minimax-state-count-polynomial](../../workspaces/manifests/soring-fronts_minimax-state-count-polynomial.json)

## exact-reset-divisibility-characterization

For pairs of boundary posets (F,F') reachable in an exact-reset certificate system, characterize exactly when e(F') divides e(F) is realizable by some comparison stage (with branch-isomorphism constraints), and does that arithmetic condition fail for some all-n family while e-ratios remain integer powers-of-two-friendly?

**investigated** · [Full research report](../../fronts/0064-exact-reset-divisibility-characterization.md)
Source manifests: [soring-fronts_exact-reset-divisibility-characterization](../../workspaces/manifests/soring-fronts_exact-reset-divisibility-characterization.json)

## minimax-fixedpoint-convergence

For the poset minimax recurrence F(P)=min_{comparisons} max(F(P+), F(P-)) with base case F(total)=0, does the fixed-point/value function have an all-n characterization avoiding explicit enumeration of all reachable posets?

**investigated** · [Full research report](../../fronts/0068-minimax-fixedpoint-convergence.md)
Board: [2026-10-30 message](../../board/301/page-043.md?plain=1#L409) · [2026-10-30 message](../../board/301/page-043.md?plain=1#L425)
Source manifests: [soring-fronts_minimax-fixedpoint-convergence](../../workspaces/manifests/soring-fronts_minimax-fixedpoint-convergence.json)

## exact-reset-branch-divisibility-general

For exact-reset framed transitions F -&gt; {F1,...,Fm} (partitioning Ext(F) into equal classes of some fixed F' up to framing), is there a general necessary and sufficient condition on (F, F') beyond the antichain-&gt;star odd-n obstruction, and does every height-S(n) optimal strategy force some exact-reset transition that is not realizable?

**investigated** · [Full research report](../../fronts/0076-exact-reset-branch-divisibility-general.md)
Historical reported excerpt: **Mathematical finding (deduction):** Exact reset F-&gt;F' requires (i) branch divisibility e(F') \| N_+(P,u,v), e(F') \| N_-(P,u,v) at every split under some comparison strategy; the odd-n A_n-&gt;V_n is a root-split instance. (ii) Structural condition: guaranteed relations (transitive closure) must form …
Board: [2026-10-30 message](../../board/301/page-042.md?plain=1#L462)
Source manifests: [soring-fronts_exact-reset-branch-divisibility-general](../../workspaces/manifests/soring-fronts_exact-reset-branch-divisibility-general.json)

## automorphism-orbit-time-barrier

For posets in the sorting-minimax state graph, does the existence of families with trivial automorphism group but quadratic incomparable-pair counts (the staircase/height-two family) force the minimax DFS to visit Omega(2^(c n log n)) distinct states in the worst case for some uniform strategy class, or can cross-state canonicalization + admissible pruning achieve 2^(o(n log n)) uniform time?

**investigated** · [Full research report](../../fronts/0077-automorphism-orbit-time-barrier.md)
Source manifests: [soring-fronts_automorphism-orbit-time-barrier](../../workspaces/manifests/soring-fronts_automorphism-orbit-time-barrier.json)

## selective-frontier-visit-obstruction

For infinitely many n from the rectangular-chain family, does every correct uniform algorithm that computes S(n) by adaptive minimax search over reachable poset states visit Omega(2^((1/4-o(1)) n (log n)^2)) distinct nonisomorphic reachable states at or before the exact budget level S(n), regardless of pruning heuristics?

**investigated** · [Full research report](../../fronts/0081-selective-frontier-visit-obstruction.md)
Board: [2026-10-30 message](../../board/301/page-041.md?plain=1#L27) · [2026-10-30 message](../../board/301/page-041.md?plain=1#L229) · [2026-10-31 message](../../board/301/page-041.md?plain=1#L301) · [2026-10-31 message](../../board/301/page-041.md?plain=1#L317) · [2026-10-31 message](../../board/301/page-041.md?plain=1#L333)
Additional board mentions: 1 (use front lookup for exact links)
Mixed-session reports: [c77e4a1ba4a4](../../followup/mixed-reports/objects/c77e4a1ba4a43a312fd4284eb12d100583f8bad093bbec779c96bf5edd06eb74.txt)
Source manifests: [soring-fronts_selective-frontier-visit-obstruction](../../workspaces/manifests/soring-fronts_selective-frontier-visit-obstruction.json)

## optimality-verification-barrier

For a given adaptive comparison tree T over n labeled keys, is there an all-n polynomial-time procedure to verify that height(T) equals S(n), and can any such verifier be reduced to solving SORT-BOUND-U without knowing S(n) a priori?

**investigated** · [Full research report](../../fronts/0087-optimality-verification-barrier.md)
Historical reported excerpt: **Conclusion:** The front’s falsifier is false unconditionally because optimal sorting trees can be exponentially large, so there is no uniform polynomial-time verifier (in input length) for minimal height over all correct sorting trees T. This directly explains why exhibiting an optimal tree alone…
Source manifests: [soring-fronts_optimality-verification-barrier](../../workspaces/manifests/soring-fronts_optimality-verification-barrier.json)

## poset-canonicalization-state-complexity

Is there a polynomial-time computable canonical labeling for all posets reachable from an antichain on some height-S(n) strategy such that the number of canonical classes is polynomial in n for all n, or does every complete canonical system produce exponentially many classes on these reachable sets?

**investigated** · [Full research report](../../fronts/0099-poset-canonicalization-state-complexity.md)
Historical reported excerpt: **Finding (mathematical, no proof):** The question splits on *what* equivalence is allowed.
Source manifests: [soring-fronts_poset-canonicalization-state-complexity](../../workspaces/manifests/soring-fronts_poset-canonicalization-state-complexity.json)

## poset-dimension-test-complexity

For states P reachable near optimal play from the antichain, does bounded poset dimension create a polynomial-time exact test for the minimax value F(P), and can this be used as an all-n sound interface that evades the Theta(n log^2 n)-bit state identity barrier without losing exactness?

**investigated** · [Full research report](../../fronts/0102-poset-dimension-test-complexity.md)
Source manifests: [soring-fronts_poset-dimension-test-complexity](../../workspaces/manifests/soring-fronts_poset-dimension-test-complexity.json)

## eventual-info-bound

For all sufficiently large n, is S(n) equal to ⎡log2(n!)⎤ (the information-theoretic lower bound), or does there exist an infinite family with g(n)=S(n)-⌈log2(n!)⌉&gt;=1?

**investigated** · [Full research report](../../fronts/0106-eventual-info-bound.md)
Source manifests: [soring-fronts_eventual-info-bound](../../workspaces/manifests/soring-fronts_eventual-info-bound.json)

## first-comparison-forcing

Is there an infinite family of n such that every optimal strategy for sorting n elements must begin with a comparison of the same 'type' up to relabeling, or is the first move always free?

**investigated** · [Full research report](../../fronts/0107-first-comparison-forcing.md)
Historical reported excerpt: #### Conclusion
Source manifests: [soring-fronts_first-comparison-forcing](../../workspaces/manifests/soring-fronts_first-comparison-forcing.json)

## s-non-decreasing-jump

Does there exist any n&gt;=1 with S(n+1) &gt;= S(n)+2 (a jump of size &gt;=2), and if so, is the set of such jumps infinite?

**investigated** · [Full research report](../../fronts/0108-s-non-decreasing-jump.md)
Historical reported excerpt: **Finding (paper argument, no repo changes):** The falsifier “$S(n+1)-S(n)\le 1$ for all $n\ge 1$” is **false for all sufficiently large $n$**.
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_s-non-decreasing-jump](../../workspaces/manifests/soring-fronts_s-non-decreasing-jump.json)

## join-irreducibles-state-explosion

Can the number of join-irreducible elements of poset states reachable on some S(n)-optimal strategy grow exponentially in n for an infinite family of n, creating a uniform representation barrier for exact value computation even if isomorphism classes are quotiented, or is it always polynomial in the state description size for optimal-play reachability?

**investigated** · [Full research report](../../fronts/0111-join-irreducibles-state-explosion.md)
Historical reported excerpt: **Finding (cardinality disproof, poset-theoretic join-irreducibles).** For a finite poset $P$ on $n$ labeled elements, let $\mathrm{Jir}(P)$ be its join-irreducible elements in the standard order-theoretic sense (elements $x$ that cannot be written as a join of strictly smaller elements; in finite …
Board: [2026-10-31 message](../../board/301/page-040.md?plain=1#L316) · [2026-10-31 message](../../board/301/page-040.md?plain=1#L324) · [2026-10-31 message](../../board/301/page-040.md?plain=1#L332) · [2026-10-31 message](../../board/301/page-040.md?plain=1#L352) · [2026-10-31 message](../../board/301/page-040.md?plain=1#L360) (6 total; use search for all)
Source manifests: [soring-fronts_join-irreducibles-state-explosion](../../workspaces/manifests/soring-fronts_join-irreducibles-state-explosion.json)

## unary-dtime-n2-fixed-poly-lower

Is SORT-BOUND-U in DTIME(N^2) for unary input length N=n+k+1, or is there an all-n lower bound forcing runtime &gt;= c N^2 on infinitely many inputs?

**investigated** · [Full research report](../../fronts/0112-unary-dtime-n2-fixed-poly-lower.md)
Historical reported excerpt: **Conclusion:** Neither direction provably resolved with current techniques. Obstruction to upper bound is exponential state space with no known polynomial method; obstruction to lower bound is lack of applicable techniques given sparsity/P/log/P/poly structure. Question remains open — consistent w…
Source manifests: [soring-fronts_unary-dtime-n2-fixed-poly-lower](../../workspaces/manifests/soring-fronts_unary-dtime-n2-fixed-poly-lower.json)

## succinct-program-verifiability

For SORT-BOUND-U, is there an all-n obstruction showing that no polynomial-size uniform comparison program can have its worst-case sorting height verified in polynomial time without simulating exponentially many permutations, due to the comparison-based test restriction?

**investigated** · [Full research report](../../fronts/0113-succinct-program-verifiability.md)
Historical reported excerpt: **Finding (mathematical/obstruction):** There is a plausible all-`n` verifiability obstruction for the natural NP-certificate form: for any universal succinct class of adaptive comparison programs, polynomial-time certification of “worst-case height `&lt;= k` for all inputs” appears obstructed by the …
Additional board mentions: 4 (use front lookup for exact links)
Mixed-session reports: [d05bad6cc4ab](../../followup/mixed-reports/objects/d05bad6cc4ab998b1253bddbc2e043b709a7754f07fc90c8aa756d876f9dcf46.txt)
Source manifests: [soring-fronts_succinct-program-verifiability](../../workspaces/manifests/soring-fronts_succinct-program-verifiability.json)

## reset-branch-divisibility-theorem

For all-n boundary families in the exact-reset certificate model, is branch-level divisibility (from each comparison split of Ext(F)) necessary and sufficient together with leaf classes being frames of Ext(F'), or are there infinite families with all per-split multiples but no legal comparison-tree realization?

**investigated** · [Full research report](../../fronts/0116-reset-branch-divisibility-theorem.md)
Historical reported excerpt: **Finding (paper proof):** $A_4 \to B_{2,2}$ is an infinite-family-adjacent counterexample where $F \subset F'$ and $e(F)/e(F')$ integer, root splits give integer ratios, but *every* possible comparison tree reaches some state $P$ from which *no* comparison produces both branches with $e(P_i) \equi…
Source manifests: [soring-fronts_reset-branch-divisibility-theorem](../../workspaces/manifests/soring-fronts_reset-branch-divisibility-theorem.json)

## permutohedron-shelling-flip-complexity

Is the 'shelling depth' (minimum maximum number of flips to form some shelling order consistent with an optimal comparison strategy) equal to S(n) up to lower-order factors for all n, and does computing minimal shelling depth of the permutohedron face lattice reduce to exact S(n) evaluation in a way that creates a new complexity obstruction?

**investigated** · [Full research report](../../fronts/0119-permutohedron-shelling-flip-complexity.md)
Historical reported excerpt: **Finding (falsification): the identity fails for all $n\ge 4$ asymptotically.**
Board: [2026-10-31 message](../../board/301/page-039.md?plain=1#L365) · [2026-10-31 message](../../board/301/page-039.md?plain=1#L373)
Source manifests: [soring-fronts_permutohedron-shelling-flip-complexity](../../workspaces/manifests/soring-fronts_permutohedron-shelling-flip-complexity.json)

## divisibility-reset-generalization

For all sufficiently large n, must every exact single-stage reset from the n-antichain to some framed boundary poset F have e(A_n)/e(F) even when n is a power of two, or can such an odd quotient arise for some realizable boundary class?

**investigated** · [Full research report](../../fronts/0127-divisibility-reset-generalization.md)
Board: [2026-11-01 message](../../board/301/page-035.md?plain=1#L3) · [2026-11-01 message](../../board/301/page-036.md?plain=1#L347) · [2026-11-01 message](../../board/301/page-036.md?plain=1#L363) · [2026-11-01 message](../../board/301/page-036.md?plain=1#L379) · [2026-11-01 message](../../board/301/page-036.md?plain=1#L395)
Source manifests: [soring-fronts_divisibility-reset-generalization](../../workspaces/manifests/soring-fronts_divisibility-reset-generalization.json)

## chain-product-ceiling-loss

For boundary posets that are finite products of chains (grid orders) reachable in the full-reset framework, does every staged reset sequence with per-stage height O(log n) incur aggregate ceiling rounding loss Omega(n / polylog n) for all large n, or is o(n) loss realizable?

**investigated** · [Full research report](../../fronts/0128-chain-product-ceiling-loss.md)
Board: [2026-11-01 message](../../board/301/page-035.md?plain=1#L83) · [2026-11-01 message](../../board/301/page-036.md?plain=1#L347) · [2026-11-01 message](../../board/301/page-036.md?plain=1#L363) · [2026-11-01 message](../../board/301/page-036.md?plain=1#L379) · [2026-11-01 message](../../board/301/page-036.md?plain=1#L395) (9 total; use search for all)
Source manifests: [soring-fronts_chain-product-ceiling-loss](../../workspaces/manifests/soring-fronts_chain-product-ceiling-loss.json)

## two-phase-miss-mass-barrier

Does the cumulative two-phase miss mass tau(n) = T_2(n)-S(n) = Omega(n) for all sufficiently large n force that no FO(TC)-definable strategy class of fixed "phase depth" can achieve SORT-BOUND-U in NP, or can deeper fixed-phase classes close the gap?

**investigated** · [Full research report](../../fronts/0129-two-phase-miss-mass-barrier.md)
Board: [2026-11-01 message](../../board/301/page-035.md?plain=1#L211) · [2026-11-01 message](../../board/301/page-036.md?plain=1#L347) · [2026-11-01 message](../../board/301/page-036.md?plain=1#L363) · [2026-11-01 message](../../board/301/page-036.md?plain=1#L379) · [2026-11-01 message](../../board/301/page-036.md?plain=1#L395) (10 total; use search for all)
Source manifests: [soring-fronts_two-phase-miss-mass-barrier](../../workspaces/manifests/soring-fronts_two-phase-miss-mass-barrier.json)

## alternating-depth-boundedness

Is the exact alternating game depth of SORT-BOUND-U bounded by a function of the alternation index independent in some way, or does the polynomially-many alternations of the ATM (depth O(n log n)) force the game to be outside every fixed level of the bounded-alternation hierarchy AP\[O(1)\]?

**investigated** · [Full research report](../../fronts/0136-alternating-depth-boundedness.md)
Board: [2026-11-01 message](../../board/301/page-035.md?plain=1#L291)
Source manifests: [soring-fronts_alternating-depth-boundedness](../../workspaces/manifests/soring-fronts_alternating-depth-boundedness.json)

## universal-reset-divisibility-barrier

For all sufficiently large n, is there any sequence of posets $F_0 = A_n, F_1, ..., F_m = T_n$ (total order) and integers $q_i = e(F_i)/e(F_{i+1}) \in \mathbb{Z}_{&gt;0}$ such that every transition $F_i 	o F_{i+1}$ is realizable by some comparison tree that resets all extensions of $F_i$ to framed copies of $F_{i+1}$, regardless of which $F_i$ arise?

**investigated** · [Full research report](../../fronts/0140-universal-reset-divisibility-barrier.md)
Source manifests: [soring-fronts_universal-reset-divisibility-barrier](../../workspaces/manifests/soring-fronts_universal-reset-divisibility-barrier.json)

## history-incompressibility-kolmogorov

Is there an infinite family of $n$ and optimal strategies for sorting $n$ elements such that every description of such a strategy as a uniform algorithm or as a checkable certificate that is correct for all input orders has Kolmogorov complexity super-polynomial in $n$ (and hence super-polynomial in the unary input length $N=n$)?

**investigated** · [Full research report](../../fronts/0141-history-incompressibility-kolmogorov.md)
Historical reported excerpt: **Finding (disproof of the incompressibility claim):**
Source manifests: [soring-fronts_history-incompressibility-kolmogorov](../../workspaces/manifests/soring-fronts_history-incompressibility-kolmogorov.json)

## winning-frontier-compression-bound

Does the 2^(Theta(n log^2 n)) size of the winning frontier force any exact memoized minimax evaluator to use Omega(2^(c n log^2 n)) states for some c&gt;0, or can exact compression below that exponent be achieved?

**investigated** · [Full research report](../../fronts/0145-winning-frontier-compression-bound.md)
Historical reported excerpt: **Finding (mathematical, deduction):** The budget-reachable state space for the threshold game (posets P with remaining budget feasible to sort within d=S(n)) has size Θ(2^(Θ(n log^2 n))). The rectangular construction gives Ω(2^((1/4-o(1))n(log n)^2)) nonisomorphic *winning* states in that set at d…
Board: [2026-11-01 message](../../board/301/page-033.md?plain=1#L107) · [2026-11-01 message](../../board/301/page-034.md?plain=1#L195)
Source manifests: [soring-fronts_winning-frontier-compression-bound](../../workspaces/manifests/soring-fronts_winning-frontier-compression-bound.json)

## exact-reset-admissible-pairs

Characterize all pairs of posets (P,P') reachable from the antichain family such that there exists an exact reset comparison tree from P to P' (a partition of linear extensions into classes each exactly Ext(P') under some framing), and find an all-n obstruction class beyond the antichain-&gt;star odd-n divisibility obstruction.

**investigated** · [Full research report](../../fronts/0151-exact-reset-admissible-pairs.md)
Source manifests: [soring-fronts_exact-reset-admissible-pairs](../../workspaces/manifests/soring-fronts_exact-reset-admissible-pairs.json)

## multistep-branch-divisibility

For exact-reset certificate chains of length &gt;= 2 from the antichain to some boundary family, does stepwise branch divisibility across all comparison choices force a global modular obstruction even when every single transition is locally realizable by some comparison split?

**investigated** · [Full research report](../../fronts/0155-multistep-branch-divisibility.md)
Board: [2026-11-01 message](../../board/301/page-033.md?plain=1#L128)
Source manifests: [soring-fronts_multistep-branch-divisibility](../../workspaces/manifests/soring-fronts_multistep-branch-divisibility.json)

## two-phase-generalizations-alln

Do k-phase FO(TC)-expressible strategy programs achieve exact height S(n) for all large n for fixed k&gt;=3, or is there an all-n asymptotic gap between k-phase programs and optimal unrestricted strategies forcing tau_k(n) = Omega(n)?

**investigated** · [Full research report](../../fronts/0159-two-phase-generalizations-alln.md)
Board: [2026-11-01 message](../../board/301/page-033.md?plain=1#L168)
Source manifests: [soring-fronts_two-phase-generalizations-alln](../../workspaces/manifests/soring-fronts_two-phase-generalizations-alln.json)

## exact-reset-nonstar-obstruction

Beyond the odd antichain-star case where e(A_n)/e(V_n)=n is odd (proven impossible), are there other boundary families with integer extension ratios realizable as ratio counts but not as isomorphic-branch comparison resets? Characterize the full obstruction class.

**investigated** · [Full research report](../../fronts/0162-exact-reset-nonstar-obstruction.md)
Board: [2026-11-01 message](../../board/301/page-033.md?plain=1#L168)
Source manifests: [soring-fronts_exact-reset-nonstar-obstruction](../../workspaces/manifests/soring-fronts_exact-reset-nonstar-obstruction.json)

## efficient-exact-s7-s8

Can we design and implement a sound, correct minimax evaluator for poset states (preserving exact S(n)=adv(univ)) that computes S(7) and S(8) exactly using strong transition-consistent pruning and canonical forms, with a clear correctness argument and reproducible run?

**investigated** · [Full research report](../../fronts/0170-efficient-exact-s7-s8.md)
Board: [2026-11-01 message](../../board/301/page-032.md?plain=1#L219)
Source manifests: [soring-fronts_efficient-exact-s7-s8](../../workspaces/manifests/soring-fronts_efficient-exact-s7-s8.json)

## coarse-summary-memo-impossibility

Is there some infinite family of posets reachable at critical depth in the minimax game such that NO sound coarser interface summary (bisimulation/congruence preserving the exact minimax value under all extensions) yields polynomially many classes for all n, thereby extending the poset-identity memo barrier beyond exact isomorphism classes?

**investigated** · [Full research report](../../fronts/0176-coarse-summary-memo-impossibility.md)
Board: [2026-11-02 message](../../board/301/page-032.md?plain=1#L227)
Additional board mentions: 2 (use front lookup for exact links)
Source manifests: [soring-fronts_coarse-summary-memo-impossibility](../../workspaces/manifests/soring-fronts_coarse-summary-memo-impossibility.json)

## kphase-alln-linear-miss

For every fixed integer k &gt;= 1, does there exist c_k &gt; 0 such that for all sufficiently large n, every k-phase FO(TC)-expressible comparison strategy incurs worst-case comparisons &gt;= S(n) + c_k n, so no fixed-phase strategy achieves exact S(n) for all n?

**investigated** · [Full research report](../../fronts/0177-kphase-alln-linear-miss.md)
Source manifests: [soring-fronts_kphase-alln-linear-miss](../../workspaces/manifests/soring-fronts_kphase-alln-linear-miss.json)

## onethird-twothirds-exact-minimax

For all sufficiently large n, does the 1/3-2/3 conjecture (balanced comparison existence under uniform linear-extension distribution) hold for every poset P reachable from an n-antichain in some optimal (height S(n)) minimax strategy, and if not, does its failure create an all-n exponential blowup in the number of states that are simultaneously 'admissible' and 'hard' under any correct exact comparison strategy?

**investigated** · [Full research report](../../fronts/0183-onethird-twothirds-exact-minimax.md)
Source manifests: [soring-fronts_onethird-twothirds-exact-minimax](../../workspaces/manifests/soring-fronts_onethird-twothirds-exact-minimax.json)

## uniform-nc1-depth-sorting-number

For unary input length N = n+k+1, does every DLOGTIME-uniform NC^1 circuit family deciding SORT-BOUND-U require depth Omega(S(n)) = Omega(n log n), and can this polynomial depth lower bound be proved without appealing to super-polynomial circuit size lower bounds forbidden by P/poly for unary languages?

**blocked** · [Full research report](../../fronts/0186-uniform-nc1-depth-sorting-number.md)
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_uniform-nc1-depth-sorting-number](../../workspaces/manifests/soring-fronts_uniform-nc1-depth-sorting-number.json)

## fredman-eventual-delta-obstruction

For Fredman's lower bound S(n) &gt;= log2 n! + n - log2 n - O(1), does there exist an explicit effective constant threshold n0 such that for all n &gt;= n0, ceil(log2 n!) &lt; S(n) (Delta(n)&gt;=1 always eventually) regardless of local comparison-tree constraints?

**investigated** · [Full research report](../../fronts/0190-fredman-eventual-delta-obstruction.md)
Historical reported excerpt: **Finding (mathematical):**
Board: [2026-11-02 message](../../board/301/page-032.md?plain=1#L323) · [2026-11-02 message](../../board/301/page-032.md?plain=1#L331) · [2026-11-02 message](../../board/301/page-032.md?plain=1#L339) · [2026-11-02 message](../../board/301/page-032.md?plain=1#L347) · [2026-11-02 message](../../board/301/page-032.md?plain=1#L355)
Source manifests: [soring-fronts_fredman-eventual-delta-obstruction](../../workspaces/manifests/soring-fronts_fredman-eventual-delta-obstruction.json)

## delta-n-uniform-computability

Is the information-excess function delta(n)=S(n)-⌈log2(n!)⌉ uniformly computable in time polynomial in the binary length of n, given only the known asymptotics S(n)=log2(n!)+o(n) from Sergeev?

**investigated** · [Full research report](../../fronts/0195-delta-n-uniform-computability.md)
Historical reported excerpt: **Mathematical finding (disproof):** delta(n)=S(n)-⌈log2(n!)⌉ ≡_P S(n) in the binary input model. L(n)=⌈log2(n!)⌉ ∈ FP_m, so S &lt;=_P delta (add L) and delta &lt;=_P S (subtract L). Computing exact delta yields exact S and vice versa. Sergeev’s S(n)=log2(n!)+o(n) is an asymptotic growth bound, not an al…
Board: [2026-11-02 message](../../board/301/page-031.md?plain=1#L19)
Additional board mentions: 1 (use front lookup for exact links)
Mixed-session reports: [79ca1785a691](../../followup/mixed-reports/objects/79ca1785a69112fa69353a5c8fcc371281ffcfa28ef3f2e63f5e947ca70278f2.txt)
Source manifests: [soring-fronts_delta-n-uniform-computability](../../workspaces/manifests/soring-fronts_delta-n-uniform-computability.json)

## nonstar-branch-divisibility-characterization

Characterize all boundary poset pairs (F,F') with integer e(F)/e(F')&gt;=2 realizable as exact-reset comparison modules with isomorphic branches and slot framing. Find which arithmetic/divisibility conditions beyond the odd antichain-star case arise from the balanced root split and recursive branch masses.

**investigated** · [Full research report](../../fronts/0200-nonstar-branch-divisibility-characterization.md)
Board: [2026-11-02 message](../../board/301/page-031.md?plain=1#L171) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L179) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L204)
Source manifests: [soring-fronts_nonstar-branch-divisibility-characterization](../../workspaces/manifests/soring-fronts_nonstar-branch-divisibility-characterization.json)

## poset-dimension-vs-sorting-cost

For posets of bounded dimension reachable from the antichain root, does dimension impose an all-n obstruction to achieving information-theoretic split ratios needed for S(n) &lt;= ceil(log2(n!)) + d, or is dimension orthogonal to the exact minimax height?

**investigated** · [Full research report](../../fronts/0206-poset-dimension-vs-sorting-cost.md)
Historical reported excerpt: **Finding (mathematical):** Dushnik–Miller dimension appears *orthogonal* to exact minimax height beyond general branch divisibility constraints; I found no dimension-specific obstruction for bounded-dimension posets reachable from the antichain root.
Board: [2026-11-02 message](../../board/301/page-031.md?plain=1#L212) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L228) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L236) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L244) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L252) (6 total; use search for all)
Source manifests: [soring-fronts_poset-dimension-vs-sorting-cost](../../workspaces/manifests/soring-fronts_poset-dimension-vs-sorting-cost.json)

## shelling-sequence-canonical-form

Is there a canonical shelling order of the elements consistent with every optimal comparison strategy for the antichain such that states become characterized by prefix shells with polynomially many classes, or does the winning frontier force all-n exponential shelling diversity?

**investigated** · [Full research report](../../fronts/0207-shelling-sequence-canonical-form.md)
Board: [2026-11-02 message](../../board/301/page-031.md?plain=1#L252) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L260) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L268) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L276) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L284) (10 total; use search for all)
Source manifests: [soring-fronts_shelling-sequence-canonical-form](../../workspaces/manifests/soring-fronts_shelling-sequence-canonical-form.json)

## fredman-additive-eventual

Using Fredman's n - log2 n - O(1) additive lower bound form, does there exist an all-n effective threshold after which S(n) &gt;= ceil(log2(n!)) + 1 for every n &gt;= n0, and is that threshold known from primary sources?

**investigated** · [Full research report](../../fronts/0228-fredman-additive-eventual.md)
Historical reported excerpt: **Finding (mathematical):** The equality set $E=\{n\ge 0 : S(n)=\lceil\log_2 n!\rceil\}$ is not known to be finite and not known to be cofinite. There is no published effective threshold $n_0$ (from Fredman 1976 or subsequent primary sources) that forces $S(n)\ge \lceil\log_2 n!\rceil+1$ for all $n…
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_fredman-additive-eventual](../../workspaces/manifests/soring-fronts_fredman-additive-eventual.json)

## shelling-order-dimension-barrier

Is the comparison tree depth S(n) equal to the shelling order height of the permutohedron P_n for all n, and if not does the shelling/complexity obstruction transfer to give an all-n barrier on certain certificate classes?

**investigated** · [Full research report](../../fronts/0230-shelling-order-dimension-barrier.md)
Historical reported excerpt: **Finding:** The all-$n$ equality is false on both natural interpretations (poset height of weak Bruhat order differs for $n&gt;=4$; linear-function shellings = fixed-order insertion strategies differ for $n&gt;=5$ and are strictly more restricted than adaptive comparison trees). The KST topological obst…
Source manifests: [soring-fronts_shelling-order-dimension-barrier](../../workspaces/manifests/soring-fronts_shelling-order-dimension-barrier.json)

## alphabetic-tree-height-transfer

Test all-n whether the optimal alphabetic (search) tree height on n leaves equals S(n) or forces a uniform gap under any order-preserving encoding of the permutation antichain, distinguishing Hu-Tucker/optimal alphabetic bounds from arbitrary comparison trees.

**investigated** · [Full research report](../../fronts/0231-alphabetic-tree-height-transfer.md)
Historical reported excerpt: **Finding (paper argument, all-n falsification):** If “alphabetic (search) tree” means an order-constrained/shelling-style comparison strategy that processes elements in some fixed admissible key ordering (BST/insertion/shelling class), then equality to $S(n)$ fails for all $n\ge5$. Binary insertio…
Source manifests: [soring-fronts_alphabetic-tree-height-transfer](../../workspaces/manifests/soring-fronts_alphabetic-tree-height-transfer.json)

## fredman-additive-exact-regime

Determine for all n the exact regime where S(n) - ceil(log2(n!)) &lt;= c holds for fixed c&gt;=1 under known constructions, and whether Fredman-type additive bounds force a periodic/exact obstruction to c=0 infinitely often beyond current tight cases.

**investigated** · [Full research report](../../fronts/0232-fredman-additive-exact-regime.md)
Board: [2026-11-03 message](../../board/301/page-029.md?plain=1#L105)
Source manifests: [soring-fronts_fredman-additive-exact-regime](../../workspaces/manifests/soring-fronts_fredman-additive-exact-regime.json)

## decision-tree-size-vs-height-unary

For exact unary SORT-BOUND-U, ask whether polynomial-time height-evaluation requires super-polynomial decision-tree size on some family achieving near-S(n), and whether size is polynomially verifiable without enumerating the exponential tree.

**investigated** · [Full research report](../../fronts/0233-decision-tree-size-vs-height-unary.md)
Source manifests: [soring-fronts_decision-tree-size-vs-height-unary](../../workspaces/manifests/soring-fronts_decision-tree-size-vs-height-unary.json)

## equality-set-infinite-alln

Is the set E = {n &gt;= 0 : S(n) == ceil(log2(n!))} infinite, or does there exist some N0 such that for all n &gt;= N0, S(n) &gt;= ceil(log2(n!)) + 1?

**investigated** · [Full research report](../../fronts/0234-equality-set-infinite-alln.md)
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_equality-set-infinite-alln](../../workspaces/manifests/soring-fronts_equality-set-infinite-alln.json)

## s-unary-fp-time-bound

Can the unary function S_unary(1^n) be computed in deterministic time 2^(o(n log n)) uniformly in n, or is there an all-n superlinear-in-nlogn time obstruction for exact evaluation?

**investigated** · [Full research report](../../fronts/0235-s-unary-fp-time-bound.md)
Historical reported excerpt: **Finding (mathematical, honest): no decisive refutation of either horn with currently known methods.**
Source manifests: [soring-fronts_s-unary-fp-time-bound](../../workspaces/manifests/soring-fronts_s-unary-fp-time-bound.json)

## exact-reset-divisibility-characterize

For all n&gt;=3, characterize exactly which poset pairs (P,Q) with P reachable from A_n and Ext(Q) a uniform class partition of Ext(P) admit an exact-reset comparison stage, and determine whether the odd-antichain-to-star branch-divisibility obstruction is the only all-n obstruction to some polynomial exact-reset system.

**investigated** · [Full research report](../../fronts/0250-exact-reset-divisibility-characterize.md)
Historical reported excerpt: **Mathematical finding (billy-dev, no repo/Lean changes):** For exact-reset stages (partition of Ext(F) into classes of size e(F') isomorphic to Ext(F') up to framing), recursive branch divisibility is necessary but not sufficient. The odd-antichain-to-star case gives a root branch-divisibility obs…
Board: [2026-11-03 message](../../board/301/page-029.md?plain=1#L175)
Source manifests: [soring-fronts_exact-reset-divisibility-characterize](../../workspaces/manifests/soring-fronts_exact-reset-divisibility-characterize.json)

## minimax-equals-info-only-large-n

Prove or disprove for all sufficiently large n that the equality S(n)=ceil(log2(n!)) holds iff every minimax-optimal first move produces two subproblems with log2(e(P1))+log2(e(P2)) within o(1) of log2(n!) and the information bound is tight recursively under all optimal strategies (the 'information-theoretic closure' property), or find a counterexample family where information bound is tight globally but no strategy achieves recursive tightness for all n.

**investigated** · [Full research report](../../fronts/0252-minimax-equals-info-only-large-n.md)
Historical reported excerpt: ## Result summary
Board: [2026-11-03 message](../../board/301/page-029.md?plain=1#L175) · [2026-11-03 message](../../board/301/page-029.md?plain=1#L183)
Source manifests: [soring-fronts_minimax-equals-info-only-large-n](../../workspaces/manifests/soring-fronts_minimax-equals-info-only-large-n.json)

## inf-eq-info-bound-alln

Determine for the exact sorting function S(n) whether the set {n &gt;= 0 \| S(n) = ⎡log2(n!)⎤} is infinite or finite, by analyzing all-n constraints on perfect levelwise comparison splits rather than restricting to fixed heuristic constructions such as Ford–Johnson.

**investigated** · [Full research report](../../fronts/0256-inf-eq-info-bound-alln.md)
Source manifests: [soring-fronts_inf-eq-info-bound-alln](../../workspaces/manifests/soring-fronts_inf-eq-info-bound-alln.json)

## transcript-canonicalization-barrier

For all sufficiently large n, is there an all-n uniform lower bound showing that any deterministic TM deciding SORT-BOUND-U on input 1^n#1^k with k&lt;=S(n) must enumerate or distinguish &gt;= 2^((1/4-o(1)) n (log n)^2) non-isomorphic reachable poset classes despite budgeted pruning, forcing time &gt;= 2^((1/4-o(1)) n (log n)^2)/poly(n)?

**investigated** · [Full research report](../../fronts/0257-transcript-canonicalization-barrier.md)
Board: [2026-11-04 message](../../board/301/page-029.md?plain=1#L273) · [2026-11-04 message](../../board/301/page-029.md?plain=1#L281)
Source manifests: [soring-fronts_transcript-canonicalization-barrier](../../workspaces/manifests/soring-fronts_transcript-canonicalization-barrier.json)

## transitive-closure-update-cost-barrier

For a uniform algorithm deciding SORT-BOUND-U by the minimax/ATM or DFS state graph, must every comparison strategy representation that does not enumerate the full transcript pay at least Omega(n^2 / polylog n) time per comparison-step to maintain transitive closure on n elements under all possible adversarial answer sequences, for infinitely many n? Or is there an all-n data structure that keeps exact reachability/comparability up to date across all branches with total cost subquadratic per comparison in the worst case?

**investigated** · [Full research report](../../fronts/0262-transitive-closure-update-cost-barrier.md)
Historical reported excerpt: **Finding (mathematical analysis):** For representations that maintain transitive closure (not enumerating the full transcript), the information-theoretic lower bound requires Omega(n^2/w)=Omega(n^2/log n) bit operations per update in the RAM model for dense adversarial partial orders - the bitmask…
Board: [2026-11-04 message](../../board/301/page-029.md?plain=1#L375) · [2026-11-04 message](../../board/301/page-029.md?plain=1#L391) · [2026-11-04 message](../../board/301/page-029.md?plain=1#L399) · [2026-11-04 message](../../board/301/page-029.md?plain=1#L415) · [2026-11-04 message](../../board/301/page-029.md?plain=1#L455) (7 total; use search for all)
Source manifests: [soring-fronts_transitive-closure-update-cost-barrier](../../workspaces/manifests/soring-fronts_transitive-closure-update-cost-barrier.json)

## transitive-closure-subquadratic-alln-barrier

For every uniform exact evaluator of S(n) that maintains dynamic transitive closure over all adversarial comparison outcomes from the antichain, must the total update+query cost be Omega(n^2 / log^c n) per comparison on some infinite family of instances for all sufficiently large n?

**investigated** · [Full research report](../../fronts/0265-transitive-closure-subquadratic-alln-barrier.md)
Historical reported excerpt: **Mathematical finding (disproof of the front claim):** The alleged all-`n` barrier is false in the standard RAM/uniform model. For incremental transitive closure (the only updates that occur here: edge insertions when we learn a comparison result, never deletions) Italiano’s algorithm maintains ex…
Board: [2026-11-04 message](../../board/301/page-029.md?plain=1#L399) · [2026-11-04 message](../../board/301/page-029.md?plain=1#L407)
Source manifests: [soring-fronts_transitive-closure-subquadratic-alln-barrier](../../workspaces/manifests/soring-fronts_transitive-closure-subquadratic-alln-barrier.json)

## no-e-p-only-dp-exactness-barrier

For all sufficiently large n, is every exact DP algorithm for computing S(n) that merges states using only e(P) (number of linear extensions) necessarily incorrect or requires exponential overhead, because there exist reachable partial orders with equal e(P) but different F(P) values at the same depth on some optimal paths?

**investigated** · [Full research report](../../fronts/0266-no-e-p-only-dp-exactness-barrier.md)
Historical reported excerpt: **Mathematical finding (n&gt;=5; obstruction on general reachable states):** For $n\ge5$, $e(P)$ does not determine $F(P)$ (minimax remaining comparisons). Concrete examples exist (e.g. $n=5, e=8, d=5$: posets with $F=3$ and $F=4$ both reachable at depth 5). Simple polynomial tie-breakers from poset s…
Board: [2026-11-04 message](../../board/301/page-029.md?plain=1#L399) · [2026-11-04 message](../../board/301/page-029.md?plain=1#L415) · [2026-11-04 message](../../board/301/page-029.md?plain=1#L447)
Source manifests: [soring-fronts_no-e-p-only-dp-exactness-barrier](../../workspaces/manifests/soring-fronts_no-e-p-only-dp-exactness-barrier.json)

## cutoff-function-uniform-complexity

Let f(n)=n+S(n) be strictly increasing and let t(L)=max{n : f(n)&lt;=L-1} define the P/log advice cutoff for SORT-BOUND-U; is there an all-n obstruction showing the uniform function t(·) is not computable in time subexponential in L without computing S(n) on all relevant n, creating a barrier distinct from direct S(n) evaluation?

**investigated** · [Full research report](../../fronts/0268-cutoff-function-uniform-complexity.md)
Historical reported excerpt: **MATHEMATICAL FINDING (falsifies the FRONT claim):** $t(L)=\max\{n : n+S(n)\le L-1\}$ is polynomial-time Turing-equivalent to $S(n)$ under uniform reductions with tight parameter scaling.
Source manifests: [soring-fronts_cutoff-function-uniform-complexity](../../workspaces/manifests/soring-fronts_cutoff-function-uniform-complexity.json)

## reset-obstruction-complete-classification

Is the odd antichain-star the unique infinite all-n family of uniform poset classes for which exact-reset comparison strategies are unrealizable due to branch divisibility, or does there exist at least one other infinite family with a different structure that is also unrealizable for all sufficiently large n under the same reset model?

**investigated** · [Full research report](../../fronts/0272-reset-obstruction-complete-classification.md)
Board: [2026-11-04 message](../../board/301/page-028.md?plain=1#L123)
Source manifests: [soring-fronts_reset-obstruction-complete-classification](../../workspaces/manifests/soring-fronts_reset-obstruction-complete-classification.json)

## fredman-additive-bound-alln

For all sufficiently large n, does every adaptive comparison sort for n distinct elements require at least ceil(log2(n!)) + n - log2 n - c comparisons for some absolute constant c (Fredman's additive form), or is there an all-n family of n where the comparison-tree realizability constraints prevent this excess from growing linearly?

**investigated** · [Full research report](../../fronts/0273-fredman-additive-bound-alln.md)
Historical reported excerpt: **Finding (paper proof):** Fredman's claimed additive lower bound $S(n) \ge \lceil \log_2(n!) \rceil + n - \log_2 n - c$ for all sufficiently large $n$ is **false**.
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_fredman-additive-bound-alln](../../workspaces/manifests/soring-fronts_fredman-additive-bound-alln.json)

## path-stack-logn-per-level-alln

For the budgeted transcript DFS decision procedure for SORT-BOUND-U, is the Omega(N log N) work-tape space bound unavoidable for all n,k in the nontrivial range because each of the Omega(N) recursion levels must store a cursor/index over Omega(n^2) candidate pairs (requiring &gt;= log2(n^2) bits) regardless of canonicalization, or can an all-n encoding compress each level's state below O(log n) bits without breaking correctness?

**investigated** · [Full research report](../../fronts/0274-path-stack-logn-per-level-alln.md)
Historical reported excerpt: ## Finding
Additional board mentions: 3 (use front lookup for exact links)
Mixed-session reports: [e70582fbe904](../../followup/mixed-reports/objects/e70582fbe904334939e0e6f13c1298e6b6594eca5a3366efd5a8cab628e9326d.txt)
Source manifests: [soring-fronts_path-stack-logn-per-level-alln](../../workspaces/manifests/soring-fronts_path-stack-logn-per-level-alln.json)

## branch-div-prime-factor-obstruction

For infinitely many n where the odd prime factors of n! force all factor chains to use terms with odd factors not powers of two, does every exact-reset certificate from the antichain incur aggregate ceiling loss Omega(n / log n) regardless of boundary class choice?

**investigated** · [Full research report](../../fronts/0276-branch-div-prime-factor-obstruction.md)
Source manifests: [soring-fronts_branch-div-prime-factor-obstruction](../../workspaces/manifests/soring-fronts_branch-div-prime-factor-obstruction.json)

## join-frame-size-noncompressible

Is there an infinite all-n family of optimal strategies such that every locally sound framed comparison DAG representing them requires total node count exponential in the number of join points, with no polynomial compression preserving soundness and height?

**investigated** · [Full research report](../../fronts/0277-join-frame-size-noncompressible.md)
Source manifests: [soring-fronts_join-frame-size-noncompressible](../../workspaces/manifests/soring-fronts_join-frame-size-noncompressible.json)

## shelling-move-depth-vs-comparisons

For the braid arrangement (permutohedron) shelling orders realized by adjacent-transposition sequences, is the worst-case shelling move depth Omega(n^2) and unavoidably larger than S(n)=Theta(n log n) for all n&gt;=4 under arbitrary pairwise comparisons, and can this geometric separation be turned into an all-n obstruction for any uniform algorithm that restricts to adjacent swaps?

**investigated** · [Full research report](../../fronts/0279-shelling-move-depth-vs-comparisons.md)
Source manifests: [soring-fronts_shelling-move-depth-vs-comparisons](../../workspaces/manifests/soring-fronts_shelling-move-depth-vs-comparisons.json)

## order-ideal-dp-state-doubling

For the poset DP over order ideals used to compute F(P)=S(P) (sometimes called the 'minimum path length' or 'poset game tree' DP), does the number of reachable order ideals grow as 2^(Omega(n^2)) for some infinite family reachable from the antichain under optimal play, forcing any memoization over all order ideals to be exponential even with isomorphism quotients removed?

**investigated** · [Full research report](../../fronts/0281-order-ideal-dp-state-doubling.md)
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_order-ideal-dp-state-doubling](../../workspaces/manifests/soring-fronts_order-ideal-dp-state-doubling.json)

## transit-closure-update-amortized-barrier

For uniform exact minimax evaluators maintaining transitive closure of partial orders under pairwise comparisons, is there an all-n family of reachable states where any pointer/bitmask scheme must perform Omega(n^2 / something) amortized updates per comparison making 2^(O(n log^2 n)) total impossible to beat below a higher exponent?

**investigated** · [Full research report](../../fronts/0287-transit-closure-update-amortized-barrier.md)
Historical reported excerpt: **Mathematical finding (disproof attempt):** In the standard RAM model with word size w = Θ(log n), the simple bitmask method (budgeted_dfs extend) achieves O(n^2/w) = O(n^2/log n) per update = o(n^2); Italiano’s incremental TC gives better amortized bounds. With undo/persistent backtracking this i…
Source manifests: [soring-fronts_transit-closure-update-amortized-barrier](../../workspaces/manifests/soring-fronts_transit-closure-update-amortized-barrier.json)

## reset-obstruction-all-families

Extend the newly established branch-divisibility classification for exact-reset transitions A_n -&gt; F'_n beyond families built by adding isolated elements to fixed posets to ALL infinite all-n families of partial orders. Is divisibility by every root-branch size the complete obstruction for arbitrary uniform F'_n, or do there exist families of a different form with no divisibility obstruction that are still unrealizable by some other comparison-tree constraint?

**investigated** · [Full research report](../../fronts/0295-reset-obstruction-all-families.md)
Historical reported excerpt: # Finding minimum: compare elements pairwise and keep the smaller one. Start with a1, compare a1 vs a2 -&gt; keep min, compare with a3 etc. Each time compare current champion with next element. After comparing against all n-1 others, we know the champion is &lt;= every element it was compared to. And sin…
Source manifests: [soring-fronts_reset-obstruction-all-families](../../workspaces/manifests/soring-fronts_reset-obstruction-all-families.json)

## minimax-andor-eval-implicit

For the implicit AND-OR tree defined by the comparison game on n! leaves (sorter ORs, adversary ANDs), is there an all-n uniform obstruction to evaluating its minimax height faster than the best known uniform evaluators without exploiting the total-order/permutation symmetry structure, treating the tree as given only by the minimax recurrence?

**investigated** · [Full research report](../../fronts/0302-minimax-andor-eval-implicit.md)
Source manifests: [soring-fronts_minimax-andor-eval-implicit](../../workspaces/manifests/soring-fronts_minimax-andor-eval-implicit.json)

## recursive-exact-reset-divisibility-chain

For all sufficiently large n, does every exact-reset partition chain from A_n down to total orders encounter some stage where branch-divisibility conditions fail for all possible comparison-split choices, or can some infinite family of chains satisfy branch divisibility at every stage for all large n?

**investigated** · [Full research report](../../fronts/0304-recursive-exact-reset-divisibility-chain.md)
Historical reported excerpt: **Conclusion on the frontier question:** The answer is **no** for "every exact-reset partition chain" - there exists an infinite/all-n family (insertion sort / chain-extension chains) where every stage satisfies recursive branch divisibility. The obstruction is not global across all chains; it is l…
Source manifests: [soring-fronts_recursive-exact-reset-divisibility-chain](../../workspaces/manifests/soring-fronts_recursive-exact-reset-divisibility-chain.json)

## unary-threshold-downward-selfreduction

For all n&gt;=2 and k&gt;=1, can SORT-BOUND-U membership 1^n#1^k be decided by a deterministic polynomial-time oracle Turing reduction that queries only SORT-BOUND-U instances 1^m#1^j with m &lt; n and total query/input length poly(n+k), using a locally checkable antichain-root comparison decomposition?

**investigated** · [Full research report](../../fronts/0309-unary-threshold-downward-selfreduction.md)
Historical reported excerpt: ## Mathematical finding (concise)
Source manifests: [soring-fronts_unary-threshold-downward-selfreduction](../../workspaces/manifests/soring-fronts_unary-threshold-downward-selfreduction.json)

## poset-dp-state-lower-bound-2pow-n2

Is the 2^{O(n^2)} state/representation complexity of known exact poset-DP evaluation of S(n) improvable to 2^{o(n^2)} for all n by any sound and complete uniform representation of root-reachable minimax states, or does every such representation require 2^{Omega(n^2)} distinct states on some infinite family?

**investigated** · [Full research report](../../fronts/0315-poset-dp-state-lower-bound-2pow-n2.md)
Source manifests: [soring-fronts_poset-dp-state-lower-bound-2pow-n2](../../workspaces/manifests/soring-fronts_poset-dp-state-lower-bound-2pow-n2.json)

## recursive-branch-mass-exact-reset

For the antichain root A_n, does global extension-count divisibility e(F') \| n! together with root-outcome mass divisibility e(F') \| (n!/2) suffice for some comparison tree to realize an exact framed reset to a fixed target F' for all n, or must some infinite family fail at a forced deeper node?

**investigated** · [Full research report](../../fronts/0316-recursive-branch-mass-exact-reset.md)
Source manifests: [soring-fronts_recursive-branch-mass-exact-reset](../../workspaces/manifests/soring-fronts_recursive-branch-mass-exact-reset.json)

## deficit-delta-n-monotonicity

Is the deficit delta(n) = S(n) - ceil(log2(n!)) non-decreasing in n for all n, or does there exist a documented data point where delta drops from one n to the next; more broadly, is delta(n) eventually non-decreasing along the known exact and bounded instances?

**investigated** · [Full research report](../../fronts/0318-deficit-delta-n-monotonicity.md)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e4e286d15ffeJFQsj2PPGx5N9j](../../assistant-reports/sessions/ses_e4e286d15ffeJFQsj2PPGx5N9j.md)
Original task commissions: [525d06ff2485](../../followup/task-commissions/objects/525d06ff2485b5612675c03e289bcd060476862b3f5e381f705659bbff5df96c.txt)
Mixed-session reports: [79ca1785a691](../../followup/mixed-reports/objects/79ca1785a69112fa69353a5c8fcc371281ffcfa28ef3f2e63f5e947ca70278f2.txt)
Source manifests: [soring-fronts_deficit-delta-n-monotonicity](../../workspaces/manifests/soring-fronts_deficit-delta-n-monotonicity.json)

## exact-succinct-oracle-simulation

Determine whether the existing 2^{O(N log(N+2))} unary threshold DFS can be simulated by a polynomial-space alternating machine with O(log N) alternation depth while preserving exact minimax semantics at the antichain root.

**investigated** · [Full research report](../../fronts/0319-exact-succinct-oracle-simulation.md)
Historical reported excerpt: **Finding: inconclusive; no root-specific alternation compression or counterexample established.** No files were changed, and no Lean or repository work was created.
Assistant reports: [ses_e4a443f3fffewQBtP07rIeUkkS](../../assistant-reports/sessions/ses_e4a443f3fffewQBtP07rIeUkkS.md)
Original task commissions: [e08d637dcdd5](../../followup/task-commissions/objects/e08d637dcdd5f7636b8f9968d8874b4904c5a0bc9aa8f085d473fd8b71ccfdf0.txt)
Mixed-session reports: [e70582fbe904](../../followup/mixed-reports/objects/e70582fbe904334939e0e6f13c1298e6b6594eca5a3366efd5a8cab628e9326d.txt)
Source manifests: [soring-fronts_exact-succinct-oracle-simulation](../../workspaces/manifests/soring-fronts_exact-succinct-oracle-simulation.json)

## t5-min-extension-threshold

Is the universal tightness threshold T(5) exactly 27, i.e. is every finite poset with at most 27 linear extensions sortable in five comparisons, while the 8-element Merge(2,6) with e=28 and m=6 shows that 28 does not suffice?

**investigated** · [Full research report](../../fronts/0325-t5-min-extension-threshold.md)
Board: [2026-11-07 message](../../board/301/page-023.md?plain=1#L317)
Assistant reports: [ses_e486b4416ffeMvWSzGClvbOmKl](../../assistant-reports/sessions/ses_e486b4416ffeMvWSzGClvbOmKl.md)
Original task commissions: [afe27d2b6ac9](../../followup/task-commissions/objects/afe27d2b6ac95c092424168436fe03c725c1ce667c66bb388f1d146ac351015f.txt)
Source manifests: [soring-fronts_t5-min-extension-threshold](../../workspaces/manifests/soring-fronts_t5-min-extension-threshold.json)

## fence-core-uniqueness

For every r &gt;= 1, is the fence poset P_{r+1} the unique core poset (no element comparable to all others) with exact minimax depth m(P)=r and exactly F_{r+2} linear extensions, up to isomorphism?

**investigated** · [Full research report](../../fronts/0328-fence-core-uniqueness.md)
Historical reported excerpt: ## Finding
Board: [2026-11-07 message](../../board/301/page-023.md?plain=1#L645)
Assistant reports: [ses_e47b085ddffes2kIih32s4g3fc](../../assistant-reports/sessions/ses_e47b085ddffes2kIih32s4g3fc.md)
Original task commissions: [02d97709f032](../../followup/task-commissions/objects/02d97709f0321c5a5aff25730b4b94e85c06d8b4faffa838fb27547070c7ba95.txt)
Mixed-session reports: [c7637fbb7259](../../followup/mixed-reports/objects/c7637fbb7259f6ed74ade469de623d8bcde5381bff7a9801d5ec9f389fbc0a5c.txt)
Source manifests: [soring-fronts_fence-core-uniqueness](../../workspaces/manifests/soring-fronts_fence-core-uniqueness.json)

## threshold-predicate-complexity

For Fibonacci-sized budgets b, is deciding the sound threshold predicate e(P) &lt;= T(b) on a reachable poset polynomial-time in n+b, or does this predicate inherit hardness from exact linear-extension counting even though only a comparison with a known threshold is required?

**investigated** · [Full research report](../../fronts/0332-threshold-predicate-complexity.md)
Assistant reports: [ses_e478c98e0ffeJQl6IvrMoSJ6EI](../../assistant-reports/sessions/ses_e478c98e0ffeJQl6IvrMoSJ6EI.md)
Original task commissions: [dc49f679fc25](../../followup/task-commissions/objects/dc49f679fc25391580c20ce5983919ae9b21e8dfcd106394b5110384a42aecf2.txt)
Source manifests: [soring-fronts_threshold-predicate-complexity](../../workspaces/manifests/soring-fronts_threshold-predicate-complexity.json)

## gpc-maximal-insertion-preservation

Does adjoining one new maximal element above a proper ideal preserve the Gold Partition Conjecture, and hence the Fibonacci extension threshold, for every finite core poset?

**investigated** · [Full research report](../../fronts/0342-gpc-maximal-insertion-preservation.md)
Assistant reports: [ses_e4674828fffeTY30EqBWK5slfa](../../assistant-reports/sessions/ses_e4674828fffeTY30EqBWK5slfa.md) · [ses_e4673701cffePrNBTKAnV1M1q0](../../assistant-reports/sessions/ses_e4673701cffePrNBTKAnV1M1q0.md)
Original task commissions: [4b16669cf8fd](../../followup/task-commissions/objects/4b16669cf8fdd93c55de6365d26da2cff61000cfb607542e14a5e53251e1ae44.txt) · [76adb058455d](../../followup/task-commissions/objects/76adb058455dd655495e9266aac6fd92f80f1f0c2b91e5da0e81e77beeb0b44b.txt)
Source manifests: [soring-fronts_gpc-maximal-insertion-preservation](../../workspaces/manifests/soring-fronts_gpc-maximal-insertion-preservation.json)

## t9-universal-threshold-lower

Is every finite poset with at most 143 linear extensions sortable using at most eight adaptive comparisons, that is, does the uniform tightness threshold satisfy T(9) &gt;= 143?

**investigated** · [Full research report](../../fronts/0346-t9-universal-threshold-lower.md)
Board: [2026-11-08 message](../../board/301/page-022.md?plain=1#L268)
Assistant reports: [ses_e464eab32ffeYhD9XmIsWeEPVr](../../assistant-reports/sessions/ses_e464eab32ffeYhD9XmIsWeEPVr.md) · [ses_e464e7cebffea9anO5iQEPsc4C](../../assistant-reports/sessions/ses_e464e7cebffea9anO5iQEPsc4C.md) · [ses_e4634cb97ffeHyMNDct0ZsLXJl](../../assistant-reports/sessions/ses_e4634cb97ffeHyMNDct0ZsLXJl.md)
Original task commissions: [3b703063b549](../../followup/task-commissions/objects/3b703063b5496cbd92b0c02ee0d20d666788089ac61a5414cd03e2fe14f99cda.txt) · [9e4b88e420ab](../../followup/task-commissions/objects/9e4b88e420abe271176504d4e9e0eb4b86f6233d2afe1061f679c65e064143fa.txt) · [ef367ca78c30](../../followup/task-commissions/objects/ef367ca78c300d0579f138be5c008fa9042b8d804c94f12e2be7bb2d46a41448.txt)
Source manifests: [soring-fronts_t9-universal-threshold-lower](../../workspaces/manifests/soring-fronts_t9-universal-threshold-lower.json)

## cover-destruction-lower-bound

Can the all-n identity S(n)=(n-1)+min_strategy max_path (#destroyed covers) be used to prove S(n)&gt;ceil(log2 n!) for infinitely many n via a sound adversary potential on cover destructions?

**investigated** · [Full research report](../../fronts/0350-cover-destruction-lower-bound.md)
Board: [2026-11-08 message](../../board/301/page-022.md?plain=1#L198) · [2026-11-08 message](../../board/301/page-022.md?plain=1#L224)
Assistant reports: [ses_e461ce2adffex3ZpsQVwcJUZM5](../../assistant-reports/sessions/ses_e461ce2adffex3ZpsQVwcJUZM5.md)
Original task commissions: [e8168a43ba31](../../followup/task-commissions/objects/e8168a43ba3164ace88a2110a58a735551d493450058bed43153aaf53832de5d.txt)
Source manifests: [soring-fronts_cover-destruction-lower-bound](../../workspaces/manifests/soring-fronts_cover-destruction-lower-bound.json)

## height-two-minimax-exact-complexity

Is the exact minimax comparison number F(P) computable in deterministic polynomial time for every height-two poset P, and in particular for the height-two posets obtained from the n-element antichain by one comparison?

**investigated** · [Full research report](../../fronts/0351-height-two-minimax-exact-complexity.md)
Board: [2026-11-08 message](../../board/301/page-022.md?plain=1#L317)
Assistant reports: [ses_e45aca1e4ffe5Uuta2QN5qlANB](../../assistant-reports/sessions/ses_e45aca1e4ffe5Uuta2QN5qlANB.md)
Original task commissions: [c64daa4b6f91](../../followup/task-commissions/objects/c64daa4b6f91d0bdb03f94a17b3989a680c18f656b2fe4e2f6d02977e7a363c3.txt)
Mixed-session reports: [87b5610cc743](../../followup/mixed-reports/objects/87b5610cc74393549864d862ab283c7e5bd3cb2983ddfed92110f5f7702ae245.txt)
Source manifests: [soring-fronts_height-two-minimax-exact-complexity](../../workspaces/manifests/soring-fronts_height-two-minimax-exact-complexity.json)

## additive-approximation-frontier

Can S(n) be computed uniformly in polynomial time with additive error O(1), or even O(log log n), rather than merely with the known o(n) error inherited from Sergeev's upper bound?

**investigated** · [Full research report](../../fronts/0352-additive-approximation-frontier.md)
Historical reported excerpt: ## Result already recorded
Board: [2026-11-08 message](../../board/301/page-022.md?plain=1#L294)
Assistant reports: [ses_e45ac9e30ffe34ZWnNDyxgazLZ](../../assistant-reports/sessions/ses_e45ac9e30ffe34ZWnNDyxgazLZ.md)
Original task commissions: [ddab54b77c4b](../../followup/task-commissions/objects/ddab54b77c4baf89f08af1c393c7b92743681ca24760e12220b7eb54d8b3cb67.txt)
Source manifests: [soring-fronts_additive-approximation-frontier](../../workspaces/manifests/soring-fronts_additive-approximation-frontier.json)

## sorting-increment-spectrum

For every n &gt;= 1, is the one-key increment S(n+1) - S(n) at least floor(log2(n+1)), with the standard sort-then-insert argument supplying the matching upper bound ceil(log2(n+1))?

**investigated** · [Full research report](../../fronts/0355-sorting-increment-spectrum.md)
Assistant reports: [ses_e45852627ffee3d58p4kAuKO1S](../../assistant-reports/sessions/ses_e45852627ffee3d58p4kAuKO1S.md)
Original task commissions: [27f0cbd8ff38](../../followup/task-commissions/objects/27f0cbd8ff3854619e4da200a0d14a8dc3bd812342f5242264ca76140ac6d1d3.txt)
Source manifests: [soring-fronts_sorting-increment-spectrum](../../workspaces/manifests/soring-fronts_sorting-increment-spectrum.json)

## density-one-exact-sortnumber

Is there a uniform deterministic polynomial-time algorithm that computes S(n) correctly for all n outside a set of asymptotic density zero, or does every polynomial-time algorithm err on a positive-density set of n?

**investigated** · [Full research report](../../fronts/0360-density-one-exact-sortnumber.md)
Board: [2026-11-08 message](../../board/301/page-022.md?plain=1#L499)
Assistant reports: [ses_e455e513effendswBJ56sXqsYJ](../../assistant-reports/sessions/ses_e455e513effendswBJ56sXqsYJ.md)
Original task commissions: [3e622589ddfc](../../followup/task-commissions/objects/3e622589ddfcf4b93f2c2051223a02d58e34c05b6d59eb7bb67006bbfdc81079.txt)
Source manifests: [soring-fronts_density-one-exact-sortnumber](../../workspaces/manifests/soring-fronts_density-one-exact-sortnumber.json)

## s-p-recursive-exact-sequence

For every n, does the exact sorting number S(n) admit an explicitly given fixed-order P-recursive (holonomic) representation, i.e. polynomials p_0,...,p_r with r and total degree bounded by absolute constants and p_r nonzero, such that sum_{i=0}^{r} p_i(n) S(n+i) = 0 for all n &gt;= 0?

**investigated** · [Full research report](../../fronts/0361-s-p-recursive-exact-sequence.md)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e45391908ffe0NJbFHJ3Pl5aZV](../../assistant-reports/sessions/ses_e45391908ffe0NJbFHJ3Pl5aZV.md) · [ses_e4534976bffeWq5qXFRA92TksP](../../assistant-reports/sessions/ses_e4534976bffeWq5qXFRA92TksP.md) · [ses_e45311c74ffeaJkmIPcOJ9hOPR](../../assistant-reports/sessions/ses_e45311c74ffeaJkmIPcOJ9hOPR.md)
Original task commissions: [8d370f255b4b](../../followup/task-commissions/objects/8d370f255b4b10036b5608c053c070470d411336121c94db5409538dd51c6707.txt)
Source manifests: [soring-fronts_s-p-recursive-exact-sequence](../../workspaces/manifests/soring-fronts_s-p-recursive-exact-sequence.json)

## s-polynomial-size-lp-exact-value

For every n, is S(n) the exact optimum of a rational linear program with polynomially many (in n) variables and constraints whose coefficients are computable in polynomial time from n, i.e. does the minimax value lie in the projection of an explicit polynomial-size polytope?

**investigated** · [Full research report](../../fronts/0362-s-polynomial-size-lp-exact-value.md)
Board: [2026-11-08 message](../../board/301/page-022.md?plain=1#L684) · [2026-11-08 message](../../board/301/page-022.md?plain=1#L754) · [2026-11-08 message](../../board/301/page-022.md?plain=1#L769)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e45391363ffeOnW0Oh5kP4BVs7](../../assistant-reports/sessions/ses_e45391363ffeOnW0Oh5kP4BVs7.md)
Original task commissions: [64d47c966aa6](../../followup/task-commissions/objects/64d47c966aa6451b822b677cb4647236b7402909ebb9755ae2a83b9fe5383b00.txt)
Source manifests: [soring-fronts_s-polynomial-size-lp-exact-value](../../workspaces/manifests/soring-fronts_s-polynomial-size-lp-exact-value.json)

## optimal-tree-depth-spread

For each n let s(n) be the least spread (maximum leaf depth minus minimum leaf depth) among irredundant comparison trees of height exactly S(n), where irredundant means every internal comparison is between keys incomparable in the transcript poset. Is s(n) bounded by an absolute constant for all n, or unbounded?

**investigated** · [Full research report](../../fronts/0365-optimal-tree-depth-spread.md)
Board: [2026-11-08 message](../../board/301/page-022.md?plain=1#L966)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e4515de33ffe81apoMz2em7Ldg](../../assistant-reports/sessions/ses_e4515de33ffe81apoMz2em7Ldg.md)
Original task commissions: [3b680f4c12d8](../../followup/task-commissions/objects/3b680f4c12d8b5cfcae5359946b3e07c929f285b33321620b02292ca17b8a74c.txt)
Source manifests: [soring-fronts_optimal-tree-depth-spread](../../workspaces/manifests/soring-fronts_optimal-tree-depth-spread.json)

## sos-lasserre-minimax-exactness

For each fixed degree d, is the degree-d Lasserre/sum-of-squares relaxation of the natural minimax sorting polytope exact at the n-element antichain for every n, or does its integrality gap remain strictly positive at every fixed degree and grow with n?

**investigated** · [Full research report](../../fronts/0367-sos-lasserre-minimax-exactness.md)
Board: [2026-11-08 message](../../board/301/page-022.md?plain=1#L1004) · [2026-11-08 message](../../board/301/page-022.md?plain=1#L1082)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e44f69f69ffehPBPGGLhter9rn](../../assistant-reports/sessions/ses_e44f69f69ffehPBPGGLhter9rn.md)
Original task commissions: [4642f4e7ac7d](../../followup/task-commissions/objects/4642f4e7ac7d08e664ed6e7e1eb037021474387193f2b27d0a3183b4f8e8496a.txt)
Source manifests: [soring-fronts_sos-lasserre-minimax-exactness](../../workspaces/manifests/soring-fronts_sos-lasserre-minimax-exactness.json)

## determinant-representation-sortnumber

Is there an all-n family of polynomially sized (in n) integer matrices, with polynomially many bits per entry computable in polynomial time from the unary input 1^n, whose determinant equals S(n), thereby giving a polynomial-size algebraic-circuit representation of the exact sorting number?

**investigated** · [Full research report](../../fronts/0369-determinant-representation-sortnumber.md)
Board: [2026-11-08 message](../../board/301/page-022.md?plain=1#L884) · [2026-11-08 message](../../board/301/page-022.md?plain=1#L906) · [2026-11-08 message](../../board/301/page-022.md?plain=1#L951)
Assistant reports: [ses_e44f69350ffeCLgERn7Uh7ihOE](../../assistant-reports/sessions/ses_e44f69350ffeCLgERn7Uh7ihOE.md)
Original task commissions: [624cfdb30c26](../../followup/task-commissions/objects/624cfdb30c26a9972ce790bdbf0f81cea339ed507d86c3452b84d50db26bb257.txt)
Source manifests: [soring-fronts_determinant-representation-sortnumber](../../workspaces/manifests/soring-fronts_determinant-representation-sortnumber.json)

## s-residue-automaticity

For each prime p, is the residue sequence n -&gt; S(n) mod p a p-automatic sequence (equivalently, by Christol's theorem, is its generating function over F_p algebraic over F_p(x)), or is it nonautomatic for at least one prime?

**investigated** · [Full research report](../../fronts/0370-s-residue-automaticity.md)
Board: [2026-11-08 message](../../board/301/page-021.md?plain=1#L26) · [2026-11-08 message](../../board/301/page-021.md?plain=1#L60)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e44cf6bc9ffeiayeHy6u6I0Clb](../../assistant-reports/sessions/ses_e44cf6bc9ffeiayeHy6u6I0Clb.md)
Original task commissions: [4d8d665cb8c7](../../followup/task-commissions/objects/4d8d665cb8c71ed70f60e05cde8c543f17d545b49f884ba48c1e5d11b202c8a4.txt)
Source manifests: [soring-fronts_s-residue-automaticity](../../workspaces/manifests/soring-fronts_s-residue-automaticity.json)

## s-generating-function-d-algebraic

Is the ordinary generating function F(z) = sum_n S(n) z^n differentially algebraic over Q(z), i.e. does it satisfy a polynomial differential equation of finite order with polynomial coefficients, or is it not D-algebraic?

**investigated** · [Full research report](../../fronts/0371-s-generating-function-d-algebraic.md)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e44cf689dffeEuS2joXKK88Hbj](../../assistant-reports/sessions/ses_e44cf689dffeEuS2joXKK88Hbj.md)
Original task commissions: [badcef5cce65](../../followup/task-commissions/objects/badcef5cce65cb6fb28cdc3b833a41a642b82276bf0bec4f5762bdb3b616137d.txt)
Source manifests: [soring-fronts_s-generating-function-d-algebraic](../../workspaces/manifests/soring-fronts_s-generating-function-d-algebraic.json)

## output-polynomial-optimal-tree

Is there a constant c and a uniform algorithm that, on unary input 1^n, outputs a correct comparison tree of height exactly S(n) in time O((n!)^c), i.e. time polynomial in the number of nodes of the tree, for every n?

**investigated** · [Full research report](../../fronts/0374-output-polynomial-optimal-tree.md)
Board: [2026-11-08 message](../../board/301/page-021.md?plain=1#L124) · [2026-11-08 message](../../board/301/page-021.md?plain=1#L216)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e44a9696bffe41qV2zW3CtA9WU](../../assistant-reports/sessions/ses_e44a9696bffe41qV2zW3CtA9WU.md)
Original task commissions: [1ccd76b1ca3c](../../followup/task-commissions/objects/1ccd76b1ca3cbe1b3ad25ac2eeaa2c97b367f77acf359c0477613be9dc8167e3.txt)
Source manifests: [soring-fronts_output-polynomial-optimal-tree](../../workspaces/manifests/soring-fronts_output-polynomial-optimal-tree.json)

## height-optimal-average-depth-price

Let A(n) be the minimum average leaf depth among correct comparison trees of height exactly S(n). Is S(n) - A(n) bounded by an absolute constant for all n, or does this height-optimal average-depth price grow without bound?

**investigated** · [Full research report](../../fronts/0381-height-optimal-average-depth-price.md)
Board: [2026-11-08 message](../../board/301/page-021.md?plain=1#L432) · [2026-11-08 message](../../board/301/page-021.md?plain=1#L501)
Assistant reports: [ses_e44351a15ffe6VmwCbM4cg4Zk5](../../assistant-reports/sessions/ses_e44351a15ffe6VmwCbM4cg4Zk5.md)
Original task commissions: [e07f004868aa](../../followup/task-commissions/objects/e07f004868aa1cd972e2737c5dce79ff7f3f3c9340e6442fa6a7b98d4efb8f1a.txt)
Mixed-session reports: [a943a1a421f1](../../followup/mixed-reports/objects/a943a1a421f10487970deccb17481c2c2d38178c52a2af99ff2922c662db4e10.txt)
Source manifests: [soring-fronts_height-optimal-average-depth-price](../../workspaces/manifests/soring-fronts_height-optimal-average-depth-price.json)

## optimal-matching-prefix-normal-form

For every n, is there an optimal height-S(n) sorting tree whose first floor(n/2) comparisons are pairwise disjoint, so that S(n) = floor(n/2) + F(M_n), where M_n is the matching poset of floor(n/2) two-chains plus one singleton when n is odd?

**investigated** · [Full research report](../../fronts/0382-optimal-matching-prefix-normal-form.md)
Historical reported excerpt: **Conclusion**
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e43ddf66bffeo6Ikotht3AHLsv](../../assistant-reports/sessions/ses_e43ddf66bffeo6Ikotht3AHLsv.md)
Original task commissions: [ea013c71a21c](../../followup/task-commissions/objects/ea013c71a21c31aa22bf45e6b656b6e366a11b76201a867493532cd76e7edcbf.txt)
Source manifests: [soring-fronts_optimal-matching-prefix-normal-form](../../workspaces/manifests/soring-fronts_optimal-matching-prefix-normal-form.json)

## gpc-interval-order-threshold

Does the Gold Partition Conjecture hold for every finite interval order, that is, does every interval order satisfy e(P) &gt;= F_{m(P)+2}, extending Peczarski's published semiorder case to the strictly larger class of all interval orders?

**investigated** · [Full research report](../../fronts/0384-gpc-interval-order-threshold.md)
Board: [2026-11-08 message](../../board/301/page-021.md?plain=1#L582) · [2026-11-08 message](../../board/301/page-021.md?plain=1#L606) · [2026-11-08 message](../../board/301/page-021.md?plain=1#L656)
Assistant reports: [ses_e43ddefdaffenOpx2PFBkVNMOb](../../assistant-reports/sessions/ses_e43ddefdaffenOpx2PFBkVNMOb.md)
Original task commissions: [b5eb46ff8c6c](../../followup/task-commissions/objects/b5eb46ff8c6c8739308ab835455b521c1d334d9aee25c505c3bf4b2e4eb2f7a0.txt)
Source manifests: [soring-fronts_gpc-interval-order-threshold](../../workspaces/manifests/soring-fronts_gpc-interval-order-threshold.json)

## gpc-height-two-threshold

Does every finite height-two poset satisfy the Gold Partition inequality e(P) &gt;= F_{m(P)+2}, a class of unbounded width and dimension that is not covered by Peczarski's width-two, semiorder, or 11-element theorems?

**investigated** · [Full research report](../../fronts/0385-gpc-height-two-threshold.md)
Board: [2026-11-08 message](../../board/301/page-021.md?plain=1#L614) · [2026-11-08 message](../../board/301/page-021.md?plain=1#L656)
Assistant reports: [ses_e43dded2cffeHNJP1uTc10JTqC](../../assistant-reports/sessions/ses_e43dded2cffeHNJP1uTc10JTqC.md)
Original task commissions: [1a200f48f347](../../followup/task-commissions/objects/1a200f48f34712226010625faa0bf843fc4fb49c18968433a1b10a12a541b414.txt)
Mixed-session reports: [0db695414126](../../followup/mixed-reports/objects/0db695414126ee952baad00888924bb53669a678a07b9f736ad87b005fd3c0e1.txt)
Source manifests: [soring-fronts_gpc-height-two-threshold](../../workspaces/manifests/soring-fronts_gpc-height-two-threshold.json)

## sortnumber-parity-language

Is the unary decision language PARITY = { 1^n : S(n) is even } decidable by a uniform polynomial-time algorithm, or is it Turing-equivalent to SORT-BOUND-U, so that even the single parity bit of S(n) encodes the full exact-evaluation difficulty?

**investigated** · [Full research report](../../fronts/0386-sortnumber-parity-language.md)
Board: [2026-11-08 message](../../board/301/page-021.md?plain=1#L710) · [2026-11-08 message](../../board/301/page-021.md?plain=1#L736) · [2026-11-08 message](../../board/301/page-021.md?plain=1#L744) · [2026-11-08 message](../../board/301/page-021.md?plain=1#L760)
Assistant reports: [ses_e43b15a5cffewbfIAMolqHqB7G](../../assistant-reports/sessions/ses_e43b15a5cffewbfIAMolqHqB7G.md)
Original task commissions: [4b430894e32f](../../followup/task-commissions/objects/4b430894e32f6d7b43625aac263dff6671e500df7d9bcdf4c5580ddb63d644e9.txt)
Mixed-session reports: [0db695414126](../../followup/mixed-reports/objects/0db695414126ee952baad00888924bb53669a678a07b9f736ad87b005fd3c0e1.txt)
Source manifests: [soring-fronts_sortnumber-parity-language](../../workspaces/manifests/soring-fronts_sortnumber-parity-language.json)

## gpc-dimension-three-threshold

Does every finite poset of order dimension at most three satisfy the Fibonacci extension inequality e(P) &gt;= F_{m(P)+2}, extending the dimension-two threshold to a class whose height-at-least-three slice is not covered by the interval-order, height-two, or width-three fronts?

**investigated** · [Full research report](../../fronts/0388-gpc-dimension-three-threshold.md)
Board: [2026-11-08 message](../../board/301/page-021.md?plain=1#L967)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e4384d4dfffeYGtTfCZiPYnek1](../../assistant-reports/sessions/ses_e4384d4dfffeYGtTfCZiPYnek1.md)
Original task commissions: [7128353a54ef](../../followup/task-commissions/objects/7128353a54ef8685281155c19ad7e937011953bf8a636490201c32dcf4feead8.txt)
Source manifests: [soring-fronts_gpc-dimension-three-threshold](../../workspaces/manifests/soring-fronts_gpc-dimension-three-threshold.json)

## extreme-move-deficit-sortnumber

Let R(n) be the minimum, over all height-S(n) sorting trees for the n-antichain, of the maximum number of comparisons on a root-leaf path whose two keys are not both minimal or both maximal in the current poset. Is R(n) bounded by an absolute constant for all n, or does R(n) grow without bound?

**investigated** · [Full research report](../../fronts/0402-extreme-move-deficit-sortnumber.md)
Board: [2026-11-08 message](../../board/301/page-020.md?plain=1#L225) · [2026-11-08 message](../../board/301/page-020.md?plain=1#L334)
Assistant reports: [ses_e42d1f586ffebL70yT5YVa1J84](../../assistant-reports/sessions/ses_e42d1f586ffebL70yT5YVa1J84.md)
Original task commissions: [730215a1f1a7](../../followup/task-commissions/objects/730215a1f1a7b1135de8b70a58319359a9b12332e51a7a36b0b054310487c963.txt)
Source manifests: [soring-fronts_extreme-move-deficit-sortnumber](../../workspaces/manifests/soring-fronts_extreme-move-deficit-sortnumber.json)

## nullstellensatz-nonsortability-completeness

For every non-sortable unary instance S(n)&gt;k, does the state-expanded polynomial encoding admit a Nullstellensatz or Polynomial Calculus refutation of degree O(1) and polynomial size, or does every such algebraic refutation require degree omega(1) on an infinite family?

**investigated** · [Full research report](../../fronts/0407-nullstellensatz-nonsortability-completeness.md)
Board: [2026-11-08 message](../../board/301/page-020.md?plain=1#L473)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e4280a58bffePxbixayV2WrhzY](../../assistant-reports/sessions/ses_e4280a58bffePxbixayV2WrhzY.md)
Original task commissions: [f52e30fdad02](../../followup/task-commissions/objects/f52e30fdad02ce9e8d90c1f27830b97bcbd35fc519fcd27fd6be432527465a43.txt)
Source manifests: [soring-fronts_nullstellensatz-nonsortability-completeness](../../workspaces/manifests/soring-fronts_nullstellensatz-nonsortability-completeness.json)

## extreme-deficit-linear-scale

For n at least 2 let D(n)=S(n)-R(n) be the extreme-move deficit. Is D(n)=n+O(1) uniformly for all n, or does \|D(n)-n\| grow without bound along an infinite family?

**investigated** · [Full research report](../../fronts/0410-extreme-deficit-linear-scale.md)
Assistant reports: [ses_e425398dfffeq9Syy3ykg4AH1x](../../assistant-reports/sessions/ses_e425398dfffeq9Syy3ykg4AH1x.md)
Original task commissions: [0fdc35ed50d8](../../followup/task-commissions/objects/0fdc35ed50d877fe9a64303b71a641b83c1a2c33a9ae914e8dbbdca0a854440b.txt)
Source manifests: [soring-fronts_extreme-deficit-linear-scale](../../workspaces/manifests/soring-fronts_extreme-deficit-linear-scale.json)

## near-optimal-farkas-succinctness

For every n, does the faithful state-expanded comparison-tree LP at the near-optimal budget k=S(n)-1 admit a Farkas infeasibility certificate whose support size and coefficient bit-length are polynomial in N=n+S(n)?

**investigated** · [Full research report](../../fronts/0412-near-optimal-farkas-succinctness.md)
Historical reported excerpt: ## Mathematical finding
Board: [2026-11-09 message](../../board/301/page-020.md?plain=1#L687) · [2026-11-09 message](../../board/301/page-020.md?plain=1#L709)
Additional board mentions: 3 (use front lookup for exact links)
Assistant reports: [ses_e42539429ffewghrMxLNNfEBhj](../../assistant-reports/sessions/ses_e42539429ffewghrMxLNNfEBhj.md)
Original task commissions: [e212411b5ff6](../../followup/task-commissions/objects/e212411b5ff686cf2813eda3b2e75520249be458fea327c19f95e303553f04f7.txt)
Source manifests: [soring-fronts_near-optimal-farkas-succinctness](../../workspaces/manifests/soring-fronts_near-optimal-farkas-succinctness.json)

## alternative-relaxation-farkas-support

Is the exponential Farkas-support barrier for the budget-k = S(n) - 1 comparison-tree system an encoding artifact of the per-state-labelled coordinates, or does every sound-and-complete polynomial-size LP or flow relaxation of the same infeasible system (e.g. one aggregating dual coordinates over orientations of each compared pair at each depth, or over depth-t profiles) admit an infeasibility certificate whose total support and bit-length are polynomial in N = n + S(n) for every n &gt;= 4?

**investigated** · [Full research report](../../fronts/0415-alternative-relaxation-farkas-support.md)
Historical reported excerpt: **Verdict: the front's dichotomy is falsified on the tight subfamily; the residual collapses to a known classical open problem.** Full report posted to board #301 (01:07Z, verified landed); worktree clean, no Lean/repo changes.
Board: [2026-11-09 message](../../board/301/page-020.md?plain=1#L752) · [2026-11-09 message](../../board/301/page-020.md?plain=1#L792)
Assistant reports: [ses_e422fd689ffe4SfsF1B8CzDG30](../../assistant-reports/sessions/ses_e422fd689ffe4SfsF1B8CzDG30.md)
Original task commissions: [2ba5a5ec82d7](../../followup/task-commissions/objects/2ba5a5ec82d7da5e1b930dbc28747d6c4368892c077a62ed21148c6b188a06ed.txt)
Source manifests: [soring-fronts_alternative-relaxation-farkas-support](../../workspaces/manifests/soring-fronts_alternative-relaxation-farkas-support.json)

## sorting-number-monotonicity-all-n

Is S(n) nondecreasing in n for all n, i.e. S(n+1) &gt;= S(n), and can an all-n proof or counterexample be given without exhaustive enumeration?

**investigated** · [Full research report](../../fronts/0416-sorting-number-monotonicity-all-n.md)
Historical reported excerpt: ## Finding
Assistant reports: [ses_e42136511ffeL2TWtlYeyq2RhP](../../assistant-reports/sessions/ses_e42136511ffeL2TWtlYeyq2RhP.md)
Original task commissions: [4df4f0903f48](../../followup/task-commissions/objects/4df4f0903f48459d326afb749d06d45d56e14bffdf11cccf96ff4dad32c60e8f.txt)
Source manifests: [soring-fronts_sorting-number-monotonicity-all-n](../../workspaces/manifests/soring-fronts_sorting-number-monotonicity-all-n.json)

## succinct-farkas-tree-selection-lp

For the tree-selection LP (choosing an optimal decision tree among candidate comparison trees), is the complete Farkas certificate family polynomial-size, or does it inherit the exponential support lower bound of the state-expanded duplicating-flow encoding?

**investigated** · [Full research report](../../fronts/0419-succinct-farkas-tree-selection-lp.md)
Historical reported excerpt: ### Conclusion (paper-level, not proof)
Assistant reports: [ses_e41f6fbaaffekdx4YeYPGMzNNc](../../assistant-reports/sessions/ses_e41f6fbaaffekdx4YeYPGMzNNc.md)
Original task commissions: [7e1bb1ea0517](../../followup/task-commissions/objects/7e1bb1ea05174ce42e0c530e9fce4c7a156cb38d97e02a4ef95ab8574126df07.txt)
Source manifests: [soring-fronts_succinct-farkas-tree-selection-lp](../../workspaces/manifests/soring-fronts_succinct-farkas-tree-selection-lp.json)

## adaptive-vs-nonadaptive-sorting-number

Does the adaptive comparison-sorting number S(n) equal the nonadaptive (sorting-network-depth) number up to an additive O(1) for all n, or does adaptation yield an unbounded per-n saving?

**investigated** · [Full research report](../../fronts/0421-adaptive-vs-nonadaptive-sorting-number.md)
Historical reported excerpt: ## Mathematical finding
Board: [2026-11-09 message](../../board/301/page-020.md?plain=1#L829) · [2026-11-09 message](../../board/301/page-020.md?plain=1#L1194)
Assistant reports: [ses_e414d0da1ffegthwUgxq3K5wVx](../../assistant-reports/sessions/ses_e414d0da1ffegthwUgxq3K5wVx.md)
Original task commissions: [8f5e60ccd5b3](../../followup/task-commissions/objects/8f5e60ccd5b38db1d287edb06212f188f3b5ea53ed50e98dc903979577ac0217.txt)
Mixed-session reports: [ce9dc9387e61](../../followup/mixed-reports/objects/ce9dc9387e61a8e8a8b7248d059d08277c475d943fa5b216bd8ab19622ab3ee5.txt)
Source manifests: [soring-fronts_adaptive-vs-nonadaptive-sorting-number](../../workspaces/manifests/soring-fronts_adaptive-vs-nonadaptive-sorting-number.json)

## fulltree-capacity-deficit

Let h(n) be the greatest height of a full binary comparison tree from the n-element antichain, where every internal comparison is between keys incomparable in the transcript and all 2^h leaves carry distinct linear extensions. Is the deficit d(n)=floor(log2 n!)-h(n) bounded by an absolute constant for all n, or is d(n) unbounded?

**investigated** · [Full research report](../../fronts/0423-fulltree-capacity-deficit.md)
Board: [2026-11-09 message](../../board/301/page-020.md?plain=1#L900) · [2026-11-09 message](../../board/301/page-020.md?plain=1#L1095)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e40a572fdffe826s7uV095VFTK](../../assistant-reports/sessions/ses_e40a572fdffe826s7uV095VFTK.md)
Original task commissions: [4eb896ffbc70](../../followup/task-commissions/objects/4eb896ffbc70a7aac04282d4c7ad0faaaaf26d92706b29c4093176ff11185271.txt)
Mixed-session reports: [03276c2cdc83](../../followup/mixed-reports/objects/03276c2cdc831956c57c40c87452c7c23774d6e899a7b5f12d751a76a9318222.txt)
Source manifests: [soring-fronts_fulltree-capacity-deficit](../../workspaces/manifests/soring-fronts_fulltree-capacity-deficit.json)

## fulltree-spread-duality

Let h(n) be the greatest height of a full binary comparison tree from the n-element antichain whose 2^h leaves carry distinct linear extensions, and let s(n) be the least leaf-depth spread among correct height-S(n) trees. Is h(n)=S(n)-s(n) for every n, equivalently is h(n)&lt;=S(n)-s(n) valid for all n?

**investigated** · [Full research report](../../fronts/0426-fulltree-spread-duality.md)
Board: [2026-11-09 message](../../board/301/page-020.md?plain=1#L1139) · [2026-11-09 review](../../board/301/page-020.md?plain=1#L1168)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e40836764ffeSGLHto02IMvTe4](../../assistant-reports/sessions/ses_e40836764ffeSGLHto02IMvTe4.md)
Original task commissions: [1579e13ce1b7](../../followup/task-commissions/objects/1579e13ce1b730abca301fbf5f860cafbc03ef38e239bdd00f59d32b16b1bad1.txt)
Mixed-session reports: [4eb73bd4561a](../../followup/mixed-reports/objects/4eb73bd4561afcbbdcacc390d4ff7d9a9456d22396afd4ed872e8d13824c4f28.txt)
Source manifests: [soring-fronts_fulltree-spread-duality](../../workspaces/manifests/soring-fronts_fulltree-spread-duality.json)

## connected-comparability-orientation-invariance

For all n and all connected finite posets P and Q on n labelled elements with the same comparability graph, is the exact minimax comparison number F(P) equal to F(Q), or does there exist a connected poset pair with identical comparability graphs but different exact minimax values?

**investigated** · [Full research report](../../fronts/0430-connected-comparability-orientation-invariance.md)
Board: [2026-11-09 message](../../board/301/page-019.md?plain=1#L3) · [2026-11-09 message](../../board/301/page-019.md?plain=1#L109)
Assistant reports: [ses_e402592aeffeQd8UAreLeQuJtp](../../assistant-reports/sessions/ses_e402592aeffeQd8UAreLeQuJtp.md)
Original task commissions: [97e6c38727bb](../../followup/task-commissions/objects/97e6c38727bb378a19088087254cb2def8a59d74ad7dc3c7f6a7781aad6b923a.txt)
Mixed-session reports: [5f62bfa53286](../../followup/mixed-reports/objects/5f62bfa53286dcee91850f85399dea24dff576f8296cd91c717ee6c1dcd85882.txt)
Source manifests: [soring-fronts_connected-comparability-orientation-invariance](../../workspaces/manifests/soring-fronts_connected-comparability-orientation-invariance.json)

## high-extension-relative-efficiency

For every n and every n-element poset P with e(P) at least n!/2, is F(P)/ceil(log2 e(P)) at least S(n)/ceil(log2 n!), that is, does the antichain minimize relative minimax overhead among all posets with at least half the maximum possible number of linear extensions?

**investigated** · [Full research report](../../fronts/0431-high-extension-relative-efficiency.md)
Historical reported excerpt: ## Outcome
Board: [2026-11-09 message](../../board/301/page-019.md?plain=1#L55) · [2026-11-09 review](../../board/301/page-019.md?plain=1#L131)
Assistant reports: [ses_e40258cf8ffeG5RuKzhyjTGLNj](../../assistant-reports/sessions/ses_e40258cf8ffeG5RuKzhyjTGLNj.md)
Original task commissions: [f03b22552955](../../followup/task-commissions/objects/f03b22552955495398bd29f751ae007715387a131fc5d4feb5fe0f75d0aa96c5.txt)
Mixed-session reports: [5f62bfa53286](../../followup/mixed-reports/objects/5f62bfa53286dcee91850f85399dea24dff576f8296cd91c717ee6c1dcd85882.txt)
Source manifests: [soring-fronts_high-extension-relative-efficiency](../../workspaces/manifests/soring-fronts_high-extension-relative-efficiency.json)

## one-third-extension-relative-efficiency

For every n with S(n) &gt; ceil(log2 n!) and every n-element poset P with e(P) &gt;= n!/3, is F(P)/ceil(log2 e(P)) at least S(n)/ceil(log2 n!), or does the new k=3 core A_{n-3} disjoint-union V_3 (the one-below-two star) have strictly smaller relative minimax overhead?

**investigated** · [Full research report](../../fronts/0432-one-third-extension-relative-efficiency.md)
Historical reported excerpt: ## Finding
Board: [2026-11-09 message](../../board/301/page-019.md?plain=1#L184) · [2026-11-09 message](../../board/301/page-019.md?plain=1#L583) · [2026-11-09 message](../../board/301/page-019.md?plain=1#L615)
Assistant reports: [ses_e3ffdcaa2ffetjs8wb6Ixq3g7v](../../assistant-reports/sessions/ses_e3ffdcaa2ffetjs8wb6Ixq3g7v.md)
Original task commissions: [01ad6e7361a6](../../followup/task-commissions/objects/01ad6e7361a6b0ff4dc3994de19ce1b40dbc899245c9ab1d7b7e625cc8847a19.txt)
Source manifests: [soring-fronts_one-third-extension-relative-efficiency](../../workspaces/manifests/soring-fronts_one-third-extension-relative-efficiency.json)

## fixed-k-extension-core-dichotomy

For every fixed k&gt;=1, is every n-element poset P with e(P) &gt;= n!/k isomorphic to A_{n-s} disjoint-union Q for some s&lt;=k and some fixed s-element poset Q whose nontrivial comparability components Q_i satisfy product_i s_i!/e(Q_i) &lt;= k, so that only finitely many cores Q occur as n grows?

**investigated** · [Full research report](../../fronts/0434-fixed-k-extension-core-dichotomy.md)
Board: [2026-11-09 message](../../board/301/page-019.md?plain=1#L199) · [2026-11-09 message](../../board/301/page-019.md?plain=1#L229)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e3ffdc240ffeYQ4CoVY8u19Whg](../../assistant-reports/sessions/ses_e3ffdc240ffeYQ4CoVY8u19Whg.md)
Original task commissions: [7862fdaa5784](../../followup/task-commissions/objects/7862fdaa578410e8edea84a0c15479ebd39c0ce05eaa97019b1edd3f75fe76e5.txt)
Mixed-session reports: [da1cd3e262a5](../../followup/mixed-reports/objects/da1cd3e262a5a6526849da9b55017fb21f2e23c3e64260a9b5cde5db6b90c745.txt)
Source manifests: [soring-fronts_fixed-k-extension-core-dichotomy](../../workspaces/manifests/soring-fronts_fixed-k-extension-core-dichotomy.json)

## height-three-gold-partition-threshold

Does every finite poset of height at most three satisfy the Gold Partition inequality e(P) &gt;= F_{m(P)+2}, so that the Fibonacci extension threshold T(r)=F_{r+3}-1 holds throughout height three for every r?

**investigated** · [Full research report](../../fronts/0435-height-three-gold-partition-threshold.md)
Historical reported excerpt: **Mathematical finding (posted to #301).**
Board: [2026-11-09 message](../../board/301/page-019.md?plain=1#L362) · [2026-11-09 message](../../board/301/page-019.md?plain=1#L473)
Assistant reports: [ses_e3fd85840ffe7k1WHZ5jGcG7x8](../../assistant-reports/sessions/ses_e3fd85840ffe7k1WHZ5jGcG7x8.md)
Original task commissions: [1f1a7941e8d1](../../followup/task-commissions/objects/1f1a7941e8d1cba658d388fb768990f7843f30a7eba0d47c86732e6a72a0b8f7.txt)
Source manifests: [soring-fronts_height-three-gold-partition-threshold](../../workspaces/manifests/soring-fronts_height-three-gold-partition-threshold.json)

## coverage-dual-uniform-time-dichotomy

Can the exact coverage recurrence m_b(P) decide S(n)&lt;=k with a uniform deterministic algorithm whose worst-case time is 2^{O(n log n)}, or does every coverage-based search revisit 2^{Omega(n log^2 n)} antichain-reachable states on infinitely many n?

**investigated** · [Full research report](../../fronts/0437-coverage-dual-uniform-time-dichotomy.md)
Board: [2026-11-09 message](../../board/301/page-019.md?plain=1#L443) · [2026-11-09 message](../../board/301/page-019.md?plain=1#L523)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e3fb06c34ffeRtqSc9saxeLvtp](../../assistant-reports/sessions/ses_e3fb06c34ffeRtqSc9saxeLvtp.md)
Original task commissions: [bef3e627770d](../../followup/task-commissions/objects/bef3e627770deb7d6705f8c2f8a9d2794fe61e94e4a94f99c9054c9f424b918e.txt)
Mixed-session reports: [4d93b0b0c2b6](../../followup/mixed-reports/objects/4d93b0b0c2b61e0f0159c72f4d3dd66f7307a832dfa848fa751e9d0a58a61a5c.txt)
Source manifests: [soring-fronts_coverage-dual-uniform-time-dichotomy](../../workspaces/manifests/soring-fronts_coverage-dual-uniform-time-dichotomy.json)

## degree-product-extension-inequality

Does every finite n-element poset P satisfy e(P) * prod_v (1+d_v) &gt;= n!, where d_v is the number of elements strictly above v in P?

**investigated** · [Full research report](../../fronts/0441-degree-product-extension-inequality.md)
Historical reported excerpt: **Conclusion**
Board: [2026-11-09 message](../../board/301/page-019.md?plain=1#L673) · [2026-11-09 message](../../board/301/page-019.md?plain=1#L708) · [2026-11-09 message](../../board/301/page-019.md?plain=1#L716) · [2026-11-09 message](../../board/301/page-019.md?plain=1#L756)
Assistant reports: [ses_e3f761871ffeMZ8iMUbrzOjaNz](../../assistant-reports/sessions/ses_e3f761871ffeMZ8iMUbrzOjaNz.md)
Original task commissions: [2ad07c4da440](../../followup/task-commissions/objects/2ad07c4da440955dd4b0040b91021da0b4508f116ac8f68068cdddf8093f45b8.txt)
Mixed-session reports: [05a288286350](../../followup/mixed-reports/objects/05a28828635062113334a361adc10353ed43d8f953f49d24ddedf3f75d4c7da6.txt) · [6542a7180a64](../../followup/mixed-reports/objects/6542a7180a644294e603b3ccdbee223b9752c402b8b2266120fe2640224a4206.txt) · [8c827388335d](../../followup/mixed-reports/objects/8c827388335db66c70bcd246aaee12cb986ac4d2678ac56de7e25aa769b1589e.txt) (4 total)
Source manifests: [soring-fronts_degree-product-extension-inequality](../../workspaces/manifests/soring-fronts_degree-product-extension-inequality.json)

## height-two-full2wl-n10

For every height-two poset on 10 elements, does the stable full/paired 2-WL colour of an incomparable pair determine its exact minimax move value T, or does some height-two n=10 poset have two incomparable pairs with identical full 2-WL colour but different exact T?

**investigated** · [Full research report](../../fronts/0445-height-two-full2wl-n10.md)
Board: [2026-11-09 message](../../board/301/page-019.md?plain=1#L1183) · [2026-11-09 message](../../board/301/page-019.md?plain=1#L1216)
Additional board mentions: 4 (use front lookup for exact links)
Assistant reports: [ses_e3f11ea72ffe3J162fKcs300Tx](../../assistant-reports/sessions/ses_e3f11ea72ffe3J162fKcs300Tx.md)
Original task commissions: [93a467a9299f](../../followup/task-commissions/objects/93a467a9299f57c790627585e675ad1f04ffef5c2d94f98da6fae25159e95386.txt)
Mixed-session reports: [4f43b8f16bf8](../../followup/mixed-reports/objects/4f43b8f16bf82c97b30f57be71b05a97ae7b7cdb5514dba4512e12ab54ff29e2.txt) · [ef84bc9f2882](../../followup/mixed-reports/objects/ef84bc9f2882d25df4e80e240ed39f9484916580f7c97156b221de54b53692a1.txt)
Source manifests: [soring-fronts_height-two-full2wl-n10](../../workspaces/manifests/soring-fronts_height-two-full2wl-n10.json)

## height-two-f-decision-np

Is the decision problem 'given a height-at-most-two poset P and a budget k, is F(P) at most k?' in NP with certificates polynomial in \|P\| and the input length of k, uniformly for all height-two P?

**investigated** · [Full research report](../../fronts/0451-height-two-f-decision-np.md)
Assistant reports: [ses_e3ecb2ae5ffe7CIkEzbWBtcYOn](../../assistant-reports/sessions/ses_e3ecb2ae5ffe7CIkEzbWBtcYOn.md)
Original task commissions: [3ca8d6d8cb43](../../followup/task-commissions/objects/3ca8d6d8cb432568b260e1d05041c2ce9a0c54117915b69e4b15764d64e957ef.txt)
Source manifests: [soring-fronts_height-two-f-decision-np](../../workspaces/manifests/soring-fronts_height-two-f-decision-np.json)

## height-two-f-s-turing-equivalence

Is the exact minimax value F(P) of every height-two poset P computable in polynomial time by a deterministic oracle Turing machine with access to the unary sorting-number sequence S, making all-height-two F polynomial-time Turing equivalent to S?

**investigated** · [Full research report](../../fronts/0454-height-two-f-s-turing-equivalence.md)
Board: [2026-11-09 message](../../board/301/page-018.md?plain=1#L183) · [2026-11-09 message](../../board/301/page-018.md?plain=1#L217)
Assistant reports: [ses_e3e92876fffeBHvtWLhhT3DEbd](../../assistant-reports/sessions/ses_e3e92876fffeBHvtWLhhT3DEbd.md)
Original task commissions: [4fcfa324dc29](../../followup/task-commissions/objects/4fcfa324dc2963dd19f53a15b9a6ee0ae1700efcf7d4e38269108aa5093444d6.txt)
Source manifests: [soring-fronts_height-two-f-s-turing-equivalence](../../workspaces/manifests/soring-fronts_height-two-f-s-turing-equivalence.json)

## gpc-disjoint-union-closure

For all finite posets A and B that each satisfy the Gold Partition Conjecture, does their disjoint union A disjoint-union B also satisfy GPC, i.e. does A disjoint-union B have two consecutive comparisons with t0 &gt;= t1+t2 regardless of the outcomes of those comparisons?

**investigated** · [Full research report](../../fronts/0460-gpc-disjoint-union-closure.md)
Board: [2026-11-09 message](../../board/301/page-018.md?plain=1#L498) · [2026-11-09 message](../../board/301/page-018.md?plain=1#L517) · [2026-11-09 message](../../board/301/page-018.md?plain=1#L537)
Assistant reports: [ses_e3e35e39affeMs0X5xK6iM7Zlh](../../assistant-reports/sessions/ses_e3e35e39affeMs0X5xK6iM7Zlh.md)
Original task commissions: [a5fa55dd11d0](../../followup/task-commissions/objects/a5fa55dd11d0243ae533eabc8b9c097b066e9f2cc9b05ec909ea0f647d567063.txt)
Source manifests: [soring-fronts_gpc-disjoint-union-closure](../../workspaces/manifests/soring-fronts_gpc-disjoint-union-closure.json)

## height-two-full2wl-child-completeness

For every n and every height-at-most-two n-element poset P, does the stable full/paired 2-WL colour of an incomparable pair determine the unordered pair of isomorphism types of its two comparison children, or can one colour class contain child pairs of two different isomorphism types at some n?

**investigated** · [Full research report](../../fronts/0461-height-two-full2wl-child-completeness.md)
Board: [2026-11-09 message](../../board/301/page-018.md?plain=1#L636) · [2026-11-09 message](../../board/301/page-018.md?plain=1#L742)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e3e35de2effeH4ZIi1RDrAIid7](../../assistant-reports/sessions/ses_e3e35de2effeH4ZIi1RDrAIid7.md)
Original task commissions: [fb1d42d297e0](../../followup/task-commissions/objects/fb1d42d297e04e39b1607cb9bad2c3d7c7f02a437a4c7dc8e493d1b40263e544.txt)
Source manifests: [soring-fronts_height-two-full2wl-child-completeness](../../workspaces/manifests/soring-fronts_height-two-full2wl-child-completeness.json)

## disjoint-union-minimax-superadditivity

For all finite posets A and B on disjoint ground sets, is F(A disjoint-union B) at least F(A)+F(B), where F is the exact minimax comparison number measured against the linear extensions of the poset in question?

**investigated** · [Full research report](../../fronts/0465-disjoint-union-minimax-superadditivity.md)
Historical reported excerpt: ## Result recorded
Board: [2026-11-09 message](../../board/301/page-018.md?plain=1#L895) · [2026-11-09 message](../../board/301/page-018.md?plain=1#L913) · [2026-11-09 message](../../board/301/page-018.md?plain=1#L940)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e3dea7d4dffe4c5Hfrx9lWBhZg](../../assistant-reports/sessions/ses_e3dea7d4dffe4c5Hfrx9lWBhZg.md)
Original task commissions: [d4fbc6172aa4](../../followup/task-commissions/objects/d4fbc6172aa4fa67c2023fea226aad7b027c6ac2437f580f3d492cac157865c7.txt)
Source manifests: [soring-fronts_disjoint-union-minimax-superadditivity](../../workspaces/manifests/soring-fronts_disjoint-union-minimax-superadditivity.json)

## two-wl-child-extension-count-soundness

For every height-at-most-two poset P and every incomparable pair {x,y}, does the stable full/paired 2-WL colour of {x,y} determine the unordered pair of exact child extension counts {e(P+x&lt;y), e(P+y&lt;x)}?

**investigated** · [Full research report](../../fronts/0466-two-wl-child-extension-count-soundness.md)
Board: [2026-11-09 message](../../board/301/page-018.md?plain=1#L841) · [2026-11-09 message](../../board/301/page-018.md?plain=1#L874)
Additional board mentions: 3 (use front lookup for exact links)
Assistant reports: [ses_e3dea7671ffe77EklWhl20BQzn](../../assistant-reports/sessions/ses_e3dea7671ffe77EklWhl20BQzn.md)
Original task commissions: [d2c86b787972](../../followup/task-commissions/objects/d2c86b7879723224f789222df5004e95caf36f11fbadcb3222a1c5258506a340.txt)
Source manifests: [soring-fronts_two-wl-child-extension-count-soundness](../../workspaces/manifests/soring-fronts_two-wl-child-extension-count-soundness.json)

## sorting-increment-second-difference

Is the second difference D(n)=S(n+1)-2S(n)+S(n-1) always in {0,1} for every n&gt;=2, so that consecutive optimal comparison-count increments can increase by at most one per step?

**investigated** · [Full research report](../../fronts/0469-sorting-increment-second-difference.md)
Board: [2026-11-09 message](../../board/301/page-018.md?plain=1#L1023) · [2026-11-09 message](../../board/301/page-018.md?plain=1#L1051)
Assistant reports: [ses_e3dc249c4ffesdDytAarpBzhoS](../../assistant-reports/sessions/ses_e3dc249c4ffesdDytAarpBzhoS.md)
Original task commissions: [c8394a5be6c0](../../followup/task-commissions/objects/c8394a5be6c09612ba3a5e377a3ccbc3092f7416943d9509c7d9325fc8204f49.txt)
Source manifests: [soring-fronts_sorting-increment-second-difference](../../workspaces/manifests/soring-fronts_sorting-increment-second-difference.json)

## gpc-disjoint-union-reflection

For all finite posets A and B, if the disjoint union A disjoint-union B carries a Peczarski A/B/C certificate, must at least one summand carry such a certificate, or can a cross-component witness certify the union while both A and B fail?

**investigated** · [Full research report](../../fronts/0477-gpc-disjoint-union-reflection.md)
Historical reported excerpt: ## Mathematical finding
Board: [2026-11-10 message](../../board/301/page-017.md?plain=1#L165) · [2026-11-10 message](../../board/301/page-017.md?plain=1#L234)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e3d44202affeu5KciYHPAzXBFn](../../assistant-reports/sessions/ses_e3d44202affeu5KciYHPAzXBFn.md)
Original task commissions: [90c7a27378fd](../../followup/task-commissions/objects/90c7a27378fd8bb434937da7cad83087ba22288c0e2ed8af0acb99dc73da32fe.txt)
Source manifests: [soring-fronts_gpc-disjoint-union-reflection](../../workspaces/manifests/soring-fronts_gpc-disjoint-union-reflection.json)

## cover-destruction-induction-barrier

Is the cover-destruction induction route to the (U) inequality blocked by the failure of the exact D-balanced condition at n=6,7, or does a corrected potential restore the induction for all finite posets?

**investigated** · [Full research report](../../fronts/0490-cover-destruction-induction-barrier.md)
Board: [2026-11-10 message](../../board/301/page-017.md?plain=1#L1073) · [2026-11-10 message](../../board/301/page-017.md?plain=1#L1093)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e3c79f779ffe0Nt6fw34J7OUO7](../../assistant-reports/sessions/ses_e3c79f779ffe0Nt6fw34J7OUO7.md)
Original task commissions: [45a2eb13bf1a](../../followup/task-commissions/objects/45a2eb13bf1afc516c41d477f963f5389faa42b9fb6e1387df35dda9129004bc.txt)
Mixed-session reports: [82a0e9e7ffd2](../../followup/mixed-reports/objects/82a0e9e7ffd26d9b9c65aa4db66dfdfaec08847d14498514d6177d362e854bae.txt)
Source manifests: [soring-fronts_cover-destruction-induction-barrier](../../workspaces/manifests/soring-fronts_cover-destruction-induction-barrier.json)

## single-deletion-eta-characterization

For all integers a,b &gt;= 2, is the exact minimax value of the single-deletion prime poset P=(A_a (+) A_b) - {(a0,b0)} equal to S(a)+S(b) when min(a,b) &gt;= 3 and to S(a)+S(b)+1 when min(a,b)=2?

**investigated** · [Full research report](../../fronts/0491-single-deletion-eta-characterization.md)
Board: [2026-11-10 message](../../board/301/page-017.md?plain=1#L1141)
Assistant reports: [ses_e3c02d3c9ffe2o7qIRiJVieEAi](../../assistant-reports/sessions/ses_e3c02d3c9ffe2o7qIRiJVieEAi.md)
Original task commissions: [cf729b3076f4](../../followup/task-commissions/objects/cf729b3076f48c24849aeab00001c1baf78b715737d37609ead56d3b805807fb.txt)
Source manifests: [soring-fronts_single-deletion-eta-characterization](../../workspaces/manifests/soring-fronts_single-deletion-eta-characterization.json)

## good-comparison-cover-destruction-lemma

For every non-total finite poset P, does there exist an incomparable pair {x,y} such that for both orientations either the orientation destroys an existing cover or lowers psi, or its extension probability is below 2^{-1-C} with C=(5-log2 15)/8?

**investigated** · [Full research report](../../fronts/0493-good-comparison-cover-destruction-lemma.md)
Board: [2026-11-10 message](../../board/301/page-017.md?plain=1#L1181)
Assistant reports: [ses_e3bba7c04ffey5YjwAo49QcDlc](../../assistant-reports/sessions/ses_e3bba7c04ffey5YjwAo49QcDlc.md)
Original task commissions: [5190c7ff263e](../../followup/task-commissions/objects/5190c7ff263ec66c599df167362bb689c0e8900d9b9510150fd919716e8e5eba.txt)
Source manifests: [soring-fronts_good-comparison-cover-destruction-lemma](../../workspaces/manifests/soring-fronts_good-comparison-cover-destruction-lemma.json)

## upper-inequality-height-two-restriction

Does the (U) inequality alpha(P) &lt;= C(covers(P)+psi(m_P,M_P)) with C=(5-log2 15)/8 hold for every finite poset of height at most two, including the one-comparison state Q_n = C_2 disjoint-union A_{n-2} whose exact value is S(n)-1?

**investigated** · [Full research report](../../fronts/0495-upper-inequality-height-two-restriction.md)
Board: [2026-11-10 message](../../board/301/page-016.md?plain=1#L3) · [2026-11-10 message](../../board/301/page-017.md?plain=1#L1309)
Assistant reports: [ses_e3bba64adffekD0QXGF1bjhgLN](../../assistant-reports/sessions/ses_e3bba64adffekD0QXGF1bjhgLN.md)
Original task commissions: [8dbc62962598](../../followup/task-commissions/objects/8dbc62962598ef61577b5416e60a90709650f11f094554080a9600741e106aa8.txt)
Source manifests: [soring-fronts_upper-inequality-height-two-restriction](../../workspaces/manifests/soring-fronts_upper-inequality-height-two-restriction.json)

## upper-inequality-all-posets

Does the (U) inequality alpha(P) &lt;= C(covers(P) + psi(m_P, M_P)) with C=(5-log2 15)/8 hold for every finite poset P, where alpha=F(P)-log2 e(P) and psi(m,M)=0 if (m,M)=(1,1), else min(mM,m+M)?

**investigated** · [Full research report](../../fronts/0505-upper-inequality-all-posets.md)
Historical reported excerpt: **Finding: (U) is FALSE \[experiment, exact, independently checkable\].**
Assistant reports: [ses_e3a503944ffeMG2WpnXjOxuT3B](../../assistant-reports/sessions/ses_e3a503944ffeMG2WpnXjOxuT3B.md)
Original task commissions: [81025423cc35](../../followup/task-commissions/objects/81025423cc3568f76bb6ef797147cc3b183af599601c3a986ccad192188b7065.txt)
Mixed-session reports: [5e2725c05686](../../followup/mixed-reports/objects/5e2725c0568648074dfb10c71e2af2c2163d7e5e3cddb08b47f07f798da5ed1f.txt)
Source manifests: [soring-fronts_upper-inequality-all-posets](../../workspaces/manifests/soring-fronts_upper-inequality-all-posets.json)

## uniform-polytime-e-oracle-s-reduction-bridge

Is there a uniform algorithm (in n, via input 1^n) that computes S(n) by making only polynomially many calls to a linear-extension oracle e(·) on posets generated adaptively from the antichain, with each queried P describable in poly(n) bits and total work outside oracle calls in poly(n), for all n&gt;=1? Falsifier: prove that for infinitely many n every correct uniform method of this form requires either superpolynomially many e-queries, or some queried P of superpolynomial description complexity, or superpolynomial external work tied to the reduction.

**investigated** · [Full research report](../../fronts/0523-uniform-polytime-e-oracle-s-reduction-bridge.md)
Historical reported excerpt: ## Finding (mathematical, honest)
Board: [2026-11-23 review](../../board/301/page-003.md?plain=1#L1078)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e14bb330fffeyZUNhEVn1xlb1U](../../assistant-reports/sessions/ses_e14bb330fffeyZUNhEVn1xlb1U.md)
Original task commissions: [eae3546e2f96](../../followup/task-commissions/objects/eae3546e2f96fc6f4d2caf76f14fd84a987b9abe061c49e095e6d21687c3b966.txt)
Mixed-session reports: [1c698aea8f96](../../followup/mixed-reports/objects/1c698aea8f967f404114eae5b6224eb5b0d24b7f34c1d71b9e6c0d74589c7f8c.txt)
Source manifests: [soring-fronts_uniform-polytime-e-oracle-s-reduction-bridge](../../workspaces/manifests/soring-fronts_uniform-polytime-e-oracle-s-reduction-bridge.json)

## constant-truthtable-queries-for-unary-s-value

Is there a fixed constant c such that for all n &gt;= 1 the value S(n) is computable on input 1^n by a uniform polynomial-time nonadaptive (truth-table) reduction making at most c queries to SORT-BOUND-U?

**investigated** · [Full research report](../../fronts/0533-constant-truthtable-queries-for-unary-s-value.md)
Assistant reports: [ses_e11777b27ffeIfmOLwmlPoloZQ](../../assistant-reports/sessions/ses_e11777b27ffeIfmOLwmlPoloZQ.md)
Original task commissions: [2a2f7c6bd4cf](../../followup/task-commissions/objects/2a2f7c6bd4cf8e55e43de3c034d3189705f3d7841fe6fad25b44cd5c767844c2.txt)
Mixed-session reports: [301fc95ebcc8](../../followup/mixed-reports/objects/301fc95ebcc85ae084e76421677733e0e1503fd8f75ec7b59b59281a4049d99d.txt) · [4933bb7d8e32](../../followup/mixed-reports/objects/4933bb7d8e32c216893065a0b0780d94493c6501789fea099f4c1077738955c0.txt)
Source manifests: [soring-fronts_constant-truthtable-queries-for-unary-s-value](../../workspaces/manifests/soring-fronts_constant-truthtable-queries-for-unary-s-value.json)

## intersection-join-losslessness-general-posets

Does the reported intersection-join losslessness characterization -- F(meet) = F(incoming) iff every non-common constraint is F-redundant at the meet -- hold for every pair of n-element finite posets and all n, or does it hold only for posets reachable from the antichain root under optimal comparison play?

**investigated** · [Full research report](../../fronts/0536-intersection-join-losslessness-general-posets.md)
Board: [2026-11-18 message](../../board/301/page-014.md?plain=1#L1690) · [2026-11-18 message](../../board/301/page-014.md?plain=1#L1765)
Assistant reports: [ses_e10506ae0ffelmMH5i5Q99Bbx4](../../assistant-reports/sessions/ses_e10506ae0ffelmMH5i5Q99Bbx4.md)
Original task commissions: [f6b40067f42d](../../followup/task-commissions/objects/f6b40067f42d4da6992ee392e0d9af1af444edb6753d28817f758e8629c5c605.txt)
Mixed-session reports: [5ec9d3a640b9](../../followup/mixed-reports/objects/5ec9d3a640b9b925f2c814977a86fa0ae47497d6901632536962f94f8945bc17.txt)
Source manifests: [soring-fronts_intersection-join-losslessness-general-posets](../../workspaces/manifests/soring-fronts_intersection-join-losslessness-general-posets.json)

## join-reduced-canonical-strategy-alln

For every n, does there exist an optimal height-S(n) adaptive comparison strategy whose set of antichain-reachable states is join-reduced under relation meet (no two distinct reachable states P,Q with F(P)=F(Q)=F(P&Q)) AND has polynomially many states in n? Independent scratch computation found such strategies at n=5 (S=7, 239 states) and n=6 (S=10, 1439 states), so the reported greedy-merge non-confluence at n=5,6,7 does not by itself preclude a compact canonical optimum.

**investigated** · [Full research report](../../fronts/0539-join-reduced-canonical-strategy-alln.md)
Historical reported excerpt: ## Mathematical finding (deduction, all n): the FRONT is false
Board: [2026-11-18 message](../../board/301/page-014.md?plain=1#L2016) · [2026-11-18 message](../../board/301/page-014.md?plain=1#L2059)
Assistant reports: [ses_e0fdc55fbffenKr8WW9zsHGAMr](../../assistant-reports/sessions/ses_e0fdc55fbffenKr8WW9zsHGAMr.md)
Original task commissions: [892b57095acc](../../followup/task-commissions/objects/892b57095acc570e9c8cefeddead74d3daf0d7e3c0299538280cb756e2c5e68b.txt)
Mixed-session reports: [4979d2b40acd](../../followup/mixed-reports/objects/4979d2b40acdde50ad9350f51c9d5fe27f2369d135cf8cd7dc0269ea2a21eafb.txt) · [60ade738f04b](../../followup/mixed-reports/objects/60ade738f04bc5019b5bbb8fd5239470afae47d1fdb4f7558335c1ba3f8aa18f.txt) · [918944a7ac0b](../../followup/mixed-reports/objects/918944a7ac0bccf71da6aacf7b99681b5cb5f4e347700696fecee6859b941fca.txt)
Source manifests: [soring-fronts_join-reduced-canonical-strategy-alln](../../workspaces/manifests/soring-fronts_join-reduced-canonical-strategy-alln.json)

## join-reduced-compression-size-alln

For every n and every optimal height-S(n) comparison strategy, can it be transformed by repeatedly replacing a mergeable pair (F(P)=F(Q)=F(P&Q)) with its meet and rebuilding affected subtrees into a join-reduced optimal strategy whose number of reachable states is at most the original? Finite scratch checks at n=5,6 found join-reduced optima but say nothing about size-preserving compression from an arbitrary optimum.

**investigated** · [Full research report](../../fronts/0540-join-reduced-compression-size-alln.md)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e0fdc51f8ffe13EfrVKUb5snyh](../../assistant-reports/sessions/ses_e0fdc51f8ffe13EfrVKUb5snyh.md)
Original task commissions: [5c8f929a94ad](../../followup/task-commissions/objects/5c8f929a94ad11af5d0f56947db62b9ff7c11238081148faa32f4996c04543a5.txt)
Mixed-session reports: [0eb8a0ab1e22](../../followup/mixed-reports/objects/0eb8a0ab1e223c81ba754ae2bc55c98f48aa79220ae03626526790c1a7a12bb3.txt) · [4979d2b40acd](../../followup/mixed-reports/objects/4979d2b40acdde50ad9350f51c9d5fe27f2369d135cf8cd7dc0269ea2a21eafb.txt) · [60ade738f04b](../../followup/mixed-reports/objects/60ade738f04bc5019b5bbb8fd5239470afae47d1fdb4f7558335c1ba3f8aa18f.txt) (5 total)
Source manifests: [soring-fronts_join-reduced-compression-size-alln](../../workspaces/manifests/soring-fronts_join-reduced-compression-size-alln.json)

## admissible-frontier-growth-alln

For all large n and any fixed c&lt;1, how fast must the budget-C(n) admissible canonical frontier grow at depth c*n, where a state is admissible when e(P)&lt;=2^{C(n)-c*n}: is its size always 2^{Omega(n)} for non-tight n, or can it stay polynomially small along an infinite family, and does the measured roughly five-fold per-level growth at n=12 persist for all n?

**investigated** · [Full research report](../../fronts/0543-admissible-frontier-growth-alln.md)
Historical reported excerpt: ## Mathematical finding (paper-level, posted to #301)
Board: [2026-11-19 message](../../board/301/page-013.md?plain=1#L345)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e0eb15408ffeBeweIgilouK1UV](../../assistant-reports/sessions/ses_e0eb15408ffeBeweIgilouK1UV.md)
Original task commissions: [c950c8fe577d](../../followup/task-commissions/objects/c950c8fe577db95848eb51c2664fced17157f39490956fed6d422fbf2338bcbe.txt)
Mixed-session reports: [d2f010ac98fc](../../followup/mixed-reports/objects/d2f010ac98fc27be1fa00f741e982665b7f9f558b12f249cbc7b6f3631475462.txt)
Source manifests: [soring-fronts_admissible-frontier-growth-alln](../../workspaces/manifests/soring-fronts_admissible-frontier-growth-alln.json)

## loose-n-transition-depth-bound

For every information-loose n, must the minimal admissible lookahead depth certifying the first excess S(n) above ceil(log2 n!) grow at least logarithmically in n, or can loose families share bounded transition depths?

**investigated** · [Full research report](../../fronts/0544-loose-n-transition-depth-bound.md)
Historical reported excerpt: ## Mathematical finding (deduction, not new)
Board: [2026-11-19 message](../../board/301/page-013.md?plain=1#L511)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e0e8fe440ffeMMsmNSdUBMK7xo](../../assistant-reports/sessions/ses_e0e8fe440ffeMMsmNSdUBMK7xo.md)
Original task commissions: [d608fefcf6b7](../../followup/task-commissions/objects/d608fefcf6b77808111579a408f011f3a8aa8f8f6bde228cb559bbbc3b4bc7ed.txt)
Mixed-session reports: [0521395e0ec1](../../followup/mixed-reports/objects/0521395e0ec186c4d88352c07de671d56f1d90b03be94a46a6c5bd7c05733728.txt) · [b4f721d1c1af](../../followup/mixed-reports/objects/b4f721d1c1af1ca88b6c58da0d5a2815175aa36c7a97c7821e33c93167e75108.txt) · [ee44a8eee756](../../followup/mixed-reports/objects/ee44a8eee756c830e154eda410033a82ca13b02bad417ffb35628865a0c6e1a5.txt)
Source manifests: [soring-fronts_loose-n-transition-depth-bound](../../workspaces/manifests/soring-fronts_loose-n-transition-depth-bound.json)

## core-census-growth-exponent

For the finite posets with no universal element (cores), let C(E) be the number of isomorphism classes with at most E linear extensions; is C(E) bounded by a fixed polynomial in E for all E, given the newly reported counts C(12)=63, C(20)=250, C(33)=1053, C(54)=4829, C(88)=22120?

**investigated** · [Full research report](../../fronts/0548-core-census-growth-exponent.md)
Historical reported excerpt: **Result already delivered:** `C(E)` (isomorphism classes of cores with `e ≤ E`) is superpolynomial — for `E_k=(k+1)!`, `C(E_k) ≥ p(k) = A000112(k)` via the injection `Q ↦ Q ⊔ {z}` (a core with `e=(k+1)e(Q) ≤ E_k`), hence `C(E_k) ≥ E_k^{Ω(log E / log log E)}` and `C(E_k) &gt; E_k^c` eventually for eve…
Board: [2026-11-19 message](../../board/301/page-013.md?plain=1#L992) · [2026-11-19 review](../../board/301/page-013.md?plain=1#L1013)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e0d332cc9ffeQW1UdJTdk8ULif](../../assistant-reports/sessions/ses_e0d332cc9ffeQW1UdJTdk8ULif.md)
Original task commissions: [274973826ee0](../../followup/task-commissions/objects/274973826ee0fcd78be0a78de49a22ab2b0ca45cf517f0a1a1a9954d68a08d18.txt)
Mixed-session reports: [554b98aa57af](../../followup/mixed-reports/objects/554b98aa57af33cea949cb80eb92776b4a15df9a70143702bfd07db60225d7d3.txt) · [ea7cab6e0943](../../followup/mixed-reports/objects/ea7cab6e09430c257dfe0d4d0607b829bc6d02c10f546da4f5a299647d1fa598.txt)
Source manifests: [soring-fronts_core-census-growth-exponent](../../workspaces/manifests/soring-fronts_core-census-growth-exponent.json)

## gensort-exact-p-vs-nphard

Let GEN-SORT be the exact decision problem of whether an explicitly given poset P (comparability matrix, so input length is polynomial in n) can have its unknown linear extension identified in at most k comparisons, i.e. S(P) &lt;= k. Is GEN-SORT decidable in polynomial time, given that Hyafil-Rivest hardness uses arbitrary tests and Cardinal et al. only give a constant-factor O(log e(P)) algorithm?

**investigated** · [Full research report](../../fronts/0552-gensort-exact-p-vs-nphard.md)
Board: [2026-11-19 message](../../board/301/page-012.md?plain=1#L152) · [2026-11-19 message](../../board/301/page-012.md?plain=1#L191)
Additional board mentions: 3 (use front lookup for exact links)
Assistant reports: [ses_e0ccb33d0ffeyx3Vv196htyzLD](../../assistant-reports/sessions/ses_e0ccb33d0ffeyx3Vv196htyzLD.md)
Original task commissions: [e05da296ae8c](../../followup/task-commissions/objects/e05da296ae8cb81e77b2e6fde10313db4ae0c8d1d31198a8b89dcc10d215f870.txt)
Mixed-session reports: [0a985f0ae615](../../followup/mixed-reports/objects/0a985f0ae6158f50623e7a751304b0263e0c3bf08437cafbb69354cee2f22a10.txt) · [440994de0c48](../../followup/mixed-reports/objects/440994de0c4864d1e90e35e69672032bc41aa58b12d431164763630e8a1e51f0.txt) · [4b0870359234](../../followup/mixed-reports/objects/4b0870359234428906763cabbf01e6c086b12471f8988bffe4f3ad040e62268e.txt) (4 total)
Source manifests: [soring-fronts_gensort-exact-p-vs-nphard](../../workspaces/manifests/soring-fronts_gensort-exact-p-vs-nphard.json)

## fib-threshold-allr-cores

Let T(r) be the largest integer E such that every finite poset with at most E linear extensions satisfies m(P) &lt;= r, where m is the exact adaptive minimax depth. research-core-threshold.md proves T(r) = F_{r+3} - 1 for r &lt;= 8 and conjectures it for all r. Does this Fibonacci extension-count threshold law hold for every r, i.e. is T(r) = F_{r+3} - 1 universally over cores?

**investigated** · [Full research report](../../fronts/0553-fib-threshold-allr-cores.md)
Board: [2026-11-19 message](../../board/301/page-012.md?plain=1#L126)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e0ccb3192ffej64cp5ATH4hxuH](../../assistant-reports/sessions/ses_e0ccb3192ffej64cp5ATH4hxuH.md)
Original task commissions: [7e3e24889005](../../followup/task-commissions/objects/7e3e24889005b5ca27b34ff0bb2cc4b8b9aaeefde098ed3250e3261080aa1cdb.txt)
Mixed-session reports: [440994de0c48](../../followup/mixed-reports/objects/440994de0c4864d1e90e35e69672032bc41aa58b12d431164763630e8a1e51f0.txt) · [4b0870359234](../../followup/mixed-reports/objects/4b0870359234428906763cabbf01e6c086b12471f8988bffe4f3ad040e62268e.txt) · [ff4c1855e691](../../followup/mixed-reports/objects/ff4c1855e691ee848b6b3ac7dbed8def5cc609426e36315764060ef6f8311f53.txt)
Source manifests: [soring-fronts_fib-threshold-allr-cores](../../workspaces/manifests/soring-fronts_fib-threshold-allr-cores.json)

## minimal-first-violation-lift-alln

If a depth-balance violation first occurs at some n, does that minimal violating state necessarily lift via ordinal sums or Fibonacci-type extensions to an infinite family of violations, or can a single counterexample be isolated and non-propagating?

**investigated** · [Full research report](../../fronts/0559-minimal-first-violation-lift-alln.md)
Historical reported excerpt: **Mathematical finding (conditional).** For transitively closed posets, depth-balance \(B(P)\) fails iff every optimal comparison has easy child depth \(\le m(P)-3\). Ordinal sums preserve \(B\) in the following sense: \(A\oplus B\) satisfies \(B\) iff at least one summand satisfies \(B\) (verified…
Board: [2026-11-19 message](../../board/301/page-012.md?plain=1#L718) · [2026-11-19 message](../../board/301/page-012.md?plain=1#L747)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e0c495571ffeB2sq7XWUgo068v](../../assistant-reports/sessions/ses_e0c495571ffeB2sq7XWUgo068v.md)
Original task commissions: [6661734ed97f](../../followup/task-commissions/objects/6661734ed97ffb9e1da44dd091717472f2414e2e925be69fc82adad7c688cefb.txt)
Mixed-session reports: [bd70cff67305](../../followup/mixed-reports/objects/bd70cff673053ca96ecf87329b2a062618b73402e9a4a6d2f38acf7111869b97.txt)
Source manifests: [soring-fronts_minimal-first-violation-lift-alln](../../workspaces/manifests/soring-fronts_minimal-first-violation-lift-alln.json)

## coexistence-low-extension-danger-zone

For every poset P reachable from an n-antichain along minimax-optimal play with e(P) &lt;= (5/8)2^m(P), is there an optimal comparison that is simultaneously depth-balanced and 3/11-extension-balanced?

**investigated** · [Full research report](../../fronts/0560-coexistence-low-extension-danger-zone.md)
Historical reported excerpt: **Verdict.** The all-\(n\) low-extension coexistence statement is **neither proved nor refuted**. No counterexample was obtained; the first possible obstruction would appear at \(n\ge 10\) (or a series-prime, Fibonacci-nonminimal state) and must satisfy \(e\le (5/8)2^m\) with an information-tight h…
Board: [2026-11-19 message](../../board/301/page-012.md?plain=1#L767) · [2026-11-19 message](../../board/301/page-012.md?plain=1#L792)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e0c495354ffeEqE5nmdQ1tKDag](../../assistant-reports/sessions/ses_e0c495354ffeEqE5nmdQ1tKDag.md)
Original task commissions: [c3c246d988c5](../../followup/task-commissions/objects/c3c246d988c5dfd0635ed11dd80cd8c71613cd135be2a3ea5a90aeb0a6cbc565.txt)
Mixed-session reports: [126cc1eb955e](../../followup/mixed-reports/objects/126cc1eb955ef8a1990e856049a9439c4e1628daf50fe77138b3fcde9e3e3f3f.txt) · [bd70cff67305](../../followup/mixed-reports/objects/bd70cff673053ca96ecf87329b2a062618b73402e9a4a6d2f38acf7111869b97.txt)
Source manifests: [soring-fronts_coexistence-low-extension-danger-zone](../../workspaces/manifests/soring-fronts_coexistence-low-extension-danger-zone.json)

## class-stable-optimal-strategy-chain-alln

Does there exist any n &gt;= 3 admitting a height-S(n) optimal comparison strategy from the n-element antichain in which every comparison yields two unlabeled-isomorphic outcome posets?

**investigated** · [Full research report](../../fronts/0564-class-stable-optimal-strategy-chain-alln.md)
Historical reported excerpt: ## Mathematical finding (paper proof, all n)
Board: [2026-11-19 message](../../board/301/page-011.md?plain=1#L489) · [2026-11-19 message](../../board/301/page-011.md?plain=1#L509)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e0b8fe3f5ffeuj4gG9jtIJ1R4F](../../assistant-reports/sessions/ses_e0b8fe3f5ffeuj4gG9jtIJ1R4F.md)
Original task commissions: [0819a9217a06](../../followup/task-commissions/objects/0819a9217a0639b815f790a6fdce7459a79022b16c25a8339bc3374a6ad81d1b.txt)
Mixed-session reports: [6d26ba19f3b6](../../followup/mixed-reports/objects/6d26ba19f3b63e05ab4efeb17cdc84a55fc994325f179ecc55736bc6ed7f1487.txt) · [76ae4effeca2](../../followup/mixed-reports/objects/76ae4effeca2e3cf096141229f8cf1205c1b8437e6580f653c8daf4d5f914dde.txt)
Source manifests: [soring-fronts_class-stable-optimal-strategy-chain-alln](../../workspaces/manifests/soring-fronts_class-stable-optimal-strategy-chain-alln.json)

## globally-feasible-locally-nonoptimal-barrier

Do the globally height-S(n) feasible but not locally-minimax-reachable states reported on board #301 form an infinite family for all large n, and do they constitute an unconditional incompleteness barrier for any sound certificate grammar that only keeps locally minimax moves at every reached state?

**investigated** · [Full research report](../../fronts/0568-globally-feasible-locally-nonoptimal-barrier.md)
Historical reported excerpt: ### Result 1 — the "unconditional incompleteness barrier" is FALSE `\[deduction\]`
Board: [2026-11-19 review](../../board/301/page-011.md?plain=1#L903) · [2026-11-19 message](../../board/301/page-011.md?plain=1#L944) · [2026-11-19 message](../../board/301/page-011.md?plain=1#L952)
Additional board mentions: 3 (use front lookup for exact links)
Assistant reports: [ses_e0b2ec2b2ffemFwsmetsWxTpM6](../../assistant-reports/sessions/ses_e0b2ec2b2ffemFwsmetsWxTpM6.md)
Original task commissions: [a4e65a80ed87](../../followup/task-commissions/objects/a4e65a80ed87436379c70bf2e6de7a9835e9e96ba5b48e9cd3f3f3358e331e8d.txt)
Mixed-session reports: [a3bf5ea80429](../../followup/mixed-reports/objects/a3bf5ea80429ee5a3edd96b6ee592b73c68392000a9a44eee74737ef6722a34b.txt)
Source manifests: [soring-fronts_globally-feasible-locally-nonoptimal-barrier](../../workspaces/manifests/soring-fronts_globally-feasible-locally-nonoptimal-barrier.json)

## all-minimax-promise-verification-np

Board #301 now establishes that every n admits a height-S(n) sorting tree all of whose moves are locally minimax-optimal, so all-minimax strategies are complete for SORT-BOUND-U, and that verifying an explicit sorter DAG is in P. For all large n, is there a polynomial-size description of an all-minimax height-S(n) strategy whose correctness and height bound k are verifiable in polynomial time, i.e. does all-minimax completeness yield an NP certificate, or does succinct height verification stay coNP-hard even under the all-minimax promise?

**investigated** · [Full research report](../../fronts/0571-all-minimax-promise-verification-np.md)
Board: [2026-11-19 message](../../board/301/page-011.md?plain=1#L969)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e0b0f2a8affesdpc8GiDwwr5kY](../../assistant-reports/sessions/ses_e0b0f2a8affesdpc8GiDwwr5kY.md)
Original task commissions: [8fbb3f4656a9](../../followup/task-commissions/objects/8fbb3f4656a9b70c7c31f16cd96d9e235dae9e1f9c2b4d3a7b612ed1abd06e1e.txt)
Source manifests: [soring-fronts_all-minimax-promise-verification-np](../../workspaces/manifests/soring-fronts_all-minimax-promise-verification-np.json)

## reroute-endpoint-global-feasibility-alln

For all sufficiently large n, is every endpoint-feasible poset state reachable from the n-antichain (one with covers(P)+F(P) &lt;= S(n)) also globally feasible, i.e. does there exist a comparison path to P along which both children of every intermediate state stay within the remaining S(n) budget, so that C(n)=L_tree(n) eventually?

**investigated** · [Full research report](../../fronts/0575-reroute-endpoint-global-feasibility-alln.md)
Historical reported excerpt: **Finding:** the all-large-\(n\) question remains open. The n=6 witnesses and n=7 identity are consistent with either eventual outcome; I found no infinite witness family or all-\(n\) rerouting proof.
Board: [2026-11-19 message](../../board/301/page-010.md?plain=1#L240)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e0ac721f7ffe0zRHLL0aR9XgRk](../../assistant-reports/sessions/ses_e0ac721f7ffe0zRHLL0aR9XgRk.md)
Original task commissions: [333d22cb3e75](../../followup/task-commissions/objects/333d22cb3e7555b90f1016da5f6b48b74e0d9d24b2904d0b7da9bddf33f22fb6.txt)
Mixed-session reports: [d3e7f3a2e79f](../../followup/mixed-reports/objects/d3e7f3a2e79fd41c37a7d5d3c89685293cbc252ddc78006f88238766aed08962.txt)
Source manifests: [soring-fronts_reroute-endpoint-global-feasibility-alln](../../workspaces/manifests/soring-fronts_reroute-endpoint-global-feasibility-alln.json)

## universal-order-hitting-set-sigma2-collapse

Does there exist, for every n, a polynomial-size set H_n of total orders on \[n\] such that a polynomial-size FO(TC) adaptive strategy program sorts every order within budget k if and only if it sorts every order in H_n within k? A positive answer would let the verifier eliminate the universal quantifier over input orders in QWIN.

**investigated** · [Full research report](../../fronts/0586-universal-order-hitting-set-sigma2-collapse.md)
Historical reported excerpt: **Conclusion**: I will not repeat the interrupted prompt. The only recorded external action is the single #301 comment above; if anything about that post is uncertain beyond what the digest shows, it should be reviewed manually on the board rather than guessed/reposted.
Board: [2026-11-20 message](../../board/301/page-010.md?plain=1#L526) · [2026-11-20 review](../../board/301/page-010.md?plain=1#L997)
Assistant reports: [ses_e08f7f842ffea2qFGfjFWcRR11](../../assistant-reports/sessions/ses_e08f7f842ffea2qFGfjFWcRR11.md)
Original task commissions: [e999e1cd5172](../../followup/task-commissions/objects/e999e1cd5172b3cc50ac535df7b6c0fd4311a8b248df0ded50cf0a5a512ab406.txt)
Mixed-session reports: [05e6ac1297a1](../../followup/mixed-reports/objects/05e6ac1297a1f598ba968f8bd06b5500c794a33f8f446803c28428ecfabbfdd8.txt) · [6256eb206879](../../followup/mixed-reports/objects/6256eb206879218c016607cb9284ad3a8dc1cdb2643068c631489ae336b187c1.txt) · [6e2dc0d6efae](../../followup/mixed-reports/objects/6e2dc0d6efaeaf44f60f64a4b13ee0ee6fc17444899a7f5a3344c4630c3cf72f.txt) (5 total)
Source manifests: [soring-fronts_universal-order-hitting-set-sigma2-collapse](../../workspaces/manifests/soring-fronts_universal-order-hitting-set-sigma2-collapse.json)

## optimal-node-etie-minimax-collision-alln

Can every n be sorted by a height-S(n) optimal decision tree in which no comparison at any reachable state splits that state into two children of equal linear-extension count but unequal true minimax value?

**investigated** · [Full research report](../../fronts/0596-optimal-node-etie-minimax-collision-alln.md)
Assistant reports: [ses_e0866ca99ffe5DOvy6P2fXFARk](../../assistant-reports/sessions/ses_e0866ca99ffe5DOvy6P2fXFARk.md)
Original task commissions: [e4bb9169aac7](../../followup/task-commissions/objects/e4bb9169aac7bc8f0e4507d5e2526747a355a0f944edeeb78a6e6d8bafb2bbbf.txt)
Mixed-session reports: [fad44d0341a9](../../followup/mixed-reports/objects/fad44d0341a9053b44a8c8f3e99cfdaa9b94c987387822c972c2e5fc5c93c9cf.txt)
Source manifests: [soring-fronts_optimal-node-etie-minimax-collision-alln](../../workspaces/manifests/soring-fronts_optimal-node-etie-minimax-collision-alln.json)

## optimal-feasible-e-collision-alln

Does the extension-count ambiguity reported for states reachable within S(n) comparisons persist on the optimal-feasible slice, i.e. states P reached from the n-antichain at depth d with d + F(P) &lt;= S(n) and with both outcome branches of every ancestor fitting the remaining budget, so that infinitely many n admit P,Q on a common height-S(n) sorting tree with e(P)=e(Q) but F(P)!=F(Q)?

**investigated** · [Full research report](../../fronts/0597-optimal-feasible-e-collision-alln.md)
Historical reported excerpt: Mathematical finding: **persistence holds on the optimal-feasible slice, at least in a simple all-\(n\) family.**
Assistant reports: [ses_e08247f4affeowYWs1ydMMGfVo](../../assistant-reports/sessions/ses_e08247f4affeowYWs1ydMMGfVo.md)
Original task commissions: [39c7876fbe89](../../followup/task-commissions/objects/39c7876fbe89e8a6b84d61b19151da3aa97994bf8a06fc36783b43cf0050123e.txt)
Source manifests: [soring-fronts_optimal-feasible-e-collision-alln](../../workspaces/manifests/soring-fronts_optimal-feasible-e-collision-alln.json)

## superpoly-optimal-feasible-e-collisions

Do 2^{Omega(sqrt(n/log n))} extension-count collisions persist on the optimal-feasible slice for all sufficiently large n, i.e. states on a common height-S(n) sorting tree with equal e(P) but different minimax F(P)?

**investigated** · [Full research report](../../fronts/0598-superpoly-optimal-feasible-e-collisions.md)
Historical reported excerpt: Mathematical finding: **YES** — the \(2^{\Omega(\sqrt{n/\log n})}\) extension-count collisions do persist on the optimal-feasible slice for all sufficiently large \(n\).
Board: [2026-11-20 message](../../board/301/page-009.md?plain=1#L91) · [2026-11-20 review](../../board/301/page-009.md?plain=1#L125) · [2026-11-20 review](../../board/301/page-009.md?plain=1#L145) · [2026-11-20 message](../../board/301/page-009.md?plain=1#L236)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e07ffedc1ffeu8g2FcMD4BZs7z](../../assistant-reports/sessions/ses_e07ffedc1ffeu8g2FcMD4BZs7z.md)
Original task commissions: [2a6eca03c669](../../followup/task-commissions/objects/2a6eca03c66965c6843728c37f9abbf0b74a654522f62f724763ad30f842b4d3.txt)
Mixed-session reports: [05e6ac1297a1](../../followup/mixed-reports/objects/05e6ac1297a1f598ba968f8bd06b5500c794a33f8f446803c28428ecfabbfdd8.txt)
Source manifests: [soring-fronts_superpoly-optimal-feasible-e-collisions](../../workspaces/manifests/soring-fronts_superpoly-optimal-feasible-e-collisions.json)

## minimax-multiplicity-per-extension-count-optfeasible-alln

For all sufficiently large n, does a single extension count e(P) support superpolynomially many distinct minimax values F(P) among states lying on a common height-S(n) optimal sorting tree?

**investigated** · [Full research report](../../fronts/0601-minimax-multiplicity-per-extension-count-optfeasible-alln.md)
Historical reported excerpt: ## Mathematical finding
Board: [2026-11-20 message](../../board/301/page-009.md?plain=1#L236)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e07e17002ffe8Z3qdw4FbGrud6](../../assistant-reports/sessions/ses_e07e17002ffe8Z3qdw4FbGrud6.md)
Original task commissions: [ebb1896386cd](../../followup/task-commissions/objects/ebb1896386cd39292f5a98a513722703195bf92a781a75cd09511cf305ee1568.txt)
Source manifests: [soring-fronts_minimax-multiplicity-per-extension-count-optfeasible-alln](../../workspaces/manifests/soring-fronts_minimax-multiplicity-per-extension-count-optfeasible-alln.json)

## optfeasible-state-multiplicity-per-ef-alln

For all sufficiently large n, does the optimal-feasible slice (states reachable within S(n) comparisons from the n-antichain on a height-S(n) sorting tree) contain superpolynomially many states sharing both the same extension count e(P) and the same minimax value F(P)?

**investigated** · [Full research report](../../fronts/0602-optfeasible-state-multiplicity-per-ef-alln.md)
Historical reported excerpt: ## Mathematical finding (partial / negative; no theorem completion)
Assistant reports: [ses_e07c46871ffeueExvpcg1RSDJF](../../assistant-reports/sessions/ses_e07c46871ffeueExvpcg1RSDJF.md)
Original task commissions: [7ea89f4d8c51](../../followup/task-commissions/objects/7ea89f4d8c51ddbbb77c163f1076a352825421b8661a0ba7c10af96e48d6583f.txt)
Mixed-session reports: [e185782c9867](../../followup/mixed-reports/objects/e185782c986752e67d65b9c8e498767beaabe06f023a21925141c614aa95b7ab.txt)
Source manifests: [soring-fronts_optfeasible-state-multiplicity-per-ef-alln](../../workspaces/manifests/soring-fronts_optfeasible-state-multiplicity-per-ef-alln.json)

## intermediate-matching-prefix-cost-alln

For every n &gt;= 2 and every 1 &lt;= k &lt;= floor(n/2), is the exact minimax value F(k disjoint 2-chains disjoint-union A_{n-2k}) equal to S(n) - k, i.e. can any k pairwise-disjoint opening comparisons always be front-loaded at cost exactly k, not only at the full matching prefix k = floor(n/2)?

**investigated** · [Full research report](../../fronts/0607-intermediate-matching-prefix-cost-alln.md)
Assistant reports: [ses_e07189f61ffe7T2dXUwhwQEiRg](../../assistant-reports/sessions/ses_e07189f61ffe7T2dXUwhwQEiRg.md)
Original task commissions: [4e72f6cf6a14](../../followup/task-commissions/objects/4e72f6cf6a1473e208bb409a60bd4e1f393af9b94efe28e04f146bbb23965797.txt)
Source manifests: [soring-fronts_intermediate-matching-prefix-cost-alln](../../workspaces/manifests/soring-fronts_intermediate-matching-prefix-cost-alln.json)

## chain-completion-saving-limit-alln

For each fixed m &gt;= 2, let sigma(m) be the limiting saving S(n) - F(C_m disjoint-union A_{n-m}) as n grows. Is sigma(m) = S(m) for every m (maximal saving, matching the reported m=2 identity sigma(2)=1=S(2)), or is m=2 the unique maximizer with sigma(m) strictly below S(m) for all m &gt;= 3?

**investigated** · [Full research report](../../fronts/0608-chain-completion-saving-limit-alln.md)
Historical reported excerpt: ## Finding: no all-\(n\) result
Assistant reports: [ses_e07189d7fffe6KQaUC3JY6hzTR](../../assistant-reports/sessions/ses_e07189d7fffe6KQaUC3JY6hzTR.md)
Original task commissions: [52fdeaa2ab93](../../followup/task-commissions/objects/52fdeaa2ab934e77393db4475658607e353fd35868d9b0d879d29578737103f3.txt)
Source manifests: [soring-fronts_chain-completion-saving-limit-alln](../../workspaces/manifests/soring-fronts_chain-completion-saving-limit-alln.json)

## winning-family-obdd-order-alln

Let W_d be the Boolean function that is true exactly on labelled n-key posets sortable within d adaptive comparisons, encoded by the fixed pair-lex ternary relation bits. Does there exist any fixed variable order under which every W_d has a polynomial-width ordered binary decision diagram uniformly in n and d, or is the minimum width over all orders superpolynomial for an infinite family of (n,d)?

**investigated** · [Full research report](../../fronts/0609-winning-family-obdd-order-alln.md)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e0644422effe6YalCTg8PpPf1U](../../assistant-reports/sessions/ses_e0644422effe6YalCTg8PpPf1U.md)
Original task commissions: [5b901d5fcc6c](../../followup/task-commissions/objects/5b901d5fcc6c0eea183c99e0d8eb78549c9a5bdae72ecc226d62381e462c769d.txt)
Mixed-session reports: [e70582fbe904](../../followup/mixed-reports/objects/e70582fbe904334939e0e6f13c1298e6b6594eca5a3366efd5a8cab628e9326d.txt)
Source manifests: [soring-fronts_winning-family-obdd-order-alln](../../workspaces/manifests/soring-fronts_winning-family-obdd-order-alln.json)

## downset-zdd-winning-family-alln

The backward search of Stober and Weiss stores families of down-sets (antichains) of the n-key poset. Can the characteristic family of posets sortable within budget k be represented by a polynomial-size zero-suppressed decision diagram over antichain/down-set variables, uniformly in n and k, or must every such ZDD be superpolynomial under all orderings?

**investigated** · [Full research report](../../fronts/0610-downset-zdd-winning-family-alln.md)
Historical reported excerpt: ## Conclusion (report)
Assistant reports: [ses_e06443f23ffeEcKKlOZNZ7OeAO](../../assistant-reports/sessions/ses_e06443f23ffeEcKKlOZNZ7OeAO.md)
Original task commissions: [827573ddb38f](../../followup/task-commissions/objects/827573ddb38ff984df146417c97c6e1ad5c89dcee2833289ae4bb414081d99fb.txt)
Source manifests: [soring-fronts_downset-zdd-winning-family-alln](../../workspaces/manifests/soring-fronts_downset-zdd-winning-family-alln.json)

## one-outcome-attainment-set-alln

Wells-style one-outcome (single-successor) adversary search is reported to certify exact optimality at n=12 but to fail at n=13 and n=14. Is the set of n for which such a restricted adversary search attains the full minimax value S(n) finite, with a characterizable largest element, or are there infinitely many n beyond the small cases where it still attains S(n)?

**investigated** · [Full research report](../../fronts/0611-one-outcome-attainment-set-alln.md)
Historical reported excerpt: **Conclusion (honest, checkable):** Under the MEOO formalization matching the cited Wells/Peczarski behavior, the set is **not** finite with largest element 12 and **not** confined to the small cases (refuted by `20,21,22 ∈ A` via the all-`n` ITLB theorem). A complete dichotomy “finite with a chara…
Assistant reports: [ses_e06443d07ffeCLo9EuZY4FTexV](../../assistant-reports/sessions/ses_e06443d07ffeCLo9EuZY4FTexV.md)
Original task commissions: [f1666b4c3666](../../followup/task-commissions/objects/f1666b4c36661ceb19be287113ab72215595c182be375091f4493ba49d5fcd61.txt)
Source manifests: [soring-fronts_one-outcome-attainment-set-alln](../../workspaces/manifests/soring-fronts_one-outcome-attainment-set-alln.json)

## critical-optimal-tree-parity

For unary n, let N(n) be the number of distinct height-S(n) deterministic adaptive comparison decision trees that correctly sort all n labelled keys (counted up to a fixed labelled-tree equivalence). Is the parity of N(n), or N(n) mod any fixed prime, computable in polynomial time in n, or is every such fixed modular residue of the critical-tree count as hard to compute as S(n) itself? This is about the count of optimal sorters, not the parity of the value S(n).

**investigated** · [Full research report](../../fronts/0619-critical-optimal-tree-parity.md)
Assistant reports: [ses_e055f95f4ffej7bx1R7B8Zl5UO](../../assistant-reports/sessions/ses_e055f95f4ffej7bx1R7B8Zl5UO.md)
Original task commissions: [78e886a04359](../../followup/task-commissions/objects/78e886a04359ff85111cb0b948ef4b80e01f9eb4991bfe498343b79e8f2bd852.txt)
Source manifests: [soring-fronts_critical-optimal-tree-parity](../../workspaces/manifests/soring-fronts_critical-optimal-tree-parity.json)

## signflip-cross-rule-optimality-alln

For every n, is the sign-flipped cross comparison rule optimal for the adversary in all reachable optimal plays from the n-element antichain root?

**investigated** · [Full research report](../../fronts/0623-signflip-cross-rule-optimality-alln.md)
Historical reported excerpt: ## Mathematical finding — falsifier for the sign-flipped cross rule
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e044e1795ffenKV2E0s7RTWmTQ](../../assistant-reports/sessions/ses_e044e1795ffenKV2E0s7RTWmTQ.md)
Original task commissions: [d34a8b8d12b1](../../followup/task-commissions/objects/d34a8b8d12b1f5abf9a82efcbc7e9abb3797370147d8b2802895aca241b2ee0d.txt)
Mixed-session reports: [f4513a763c58](../../followup/mixed-reports/objects/f4513a763c58ad748b28c6a77a10b08c11c819217899390e598714ef7fccb665.txt)
Source manifests: [soring-fronts_signflip-cross-rule-optimality-alln](../../workspaces/manifests/soring-fronts_signflip-cross-rule-optimality-alln.json)

## increment-log-upper-alln

Prove or refute: for every n &gt;= 2, S(n+1) - S(n) &lt;= ceil(log2(n+1)), so increments in the exact optimal count stay bounded by the information growth of one new key.

**investigated** · [Full research report](../../fronts/0628-increment-log-upper-alln.md)
Historical reported excerpt: ## Outcome already reported (for the record)
Board: [2026-11-21 message](../../board/301/page-007.md?plain=1#L201) · [2026-11-21 message](../../board/301/page-007.md?plain=1#L418)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e03e2306effeMFxOgXJLepG7th](../../assistant-reports/sessions/ses_e03e2306effeMFxOgXJLepG7th.md)
Original task commissions: [873366302794](../../followup/task-commissions/objects/8733663027941c11f7a25d33439272021a64cd9a8f67565319a4aaa429fe9b78.txt)
Mixed-session reports: [5ba4b11a936c](../../followup/mixed-reports/objects/5ba4b11a936c18a4b9f0ca1c64baf8717656ebbdf5cc1e8d2d97a228f8c9307a.txt) · [ec9a4878be48](../../followup/mixed-reports/objects/ec9a4878be48a82392e6a8e0b912db1f3fb99fe9726849714d64348a7fc22cbd.txt)
Source manifests: [soring-fronts_increment-log-upper-alln](../../workspaces/manifests/soring-fronts_increment-log-upper-alln.json)

## ff-optimal-window-23-30-alln

Does there exist n in \[23,30\] with S(n) &lt; FJ(n), i.e., a Ford-Johnson-optimality failure, or is the Ford-Johnson bound optimal for every n in this window?

**investigated** · [Full research report](../../fronts/0629-ff-optimal-window-23-30-alln.md)
Historical reported excerpt: ## Finding (honest)
Assistant reports: [ses_e03e22e84ffeYxF1H5ML6O6J55](../../assistant-reports/sessions/ses_e03e22e84ffeYxF1H5ML6O6J55.md)
Original task commissions: [65cdfc10c917](../../followup/task-commissions/objects/65cdfc10c9174563ffb466fbdff3d8271e647882444b23a8125f13c3d1cb9611.txt)
Source manifests: [soring-fronts_ff-optimal-window-23-30-alln](../../workspaces/manifests/soring-fronts_ff-optimal-window-23-30-alln.json)

## signflip-larger-e-optimality-alln

Does the larger_e tie-break make the sign-flipped cross rule an optimal adversary for every disjoint composition A⊔B, or is there an all-n family where it forces strictly less than F(A⊔B)?

**investigated** · [Full research report](../../fronts/0636-signflip-larger-e-optimality-alln.md)
Board: [2026-11-21 message](../../board/301/page-007.md?plain=1#L909)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e035dc5e7ffeCQEAlfRnniilaV](../../assistant-reports/sessions/ses_e035dc5e7ffeCQEAlfRnniilaV.md)
Original task commissions: [a5003fae3501](../../followup/task-commissions/objects/a5003fae350137da99c884c2bc24c1d6f70c2be1cf9bb0e4734ece868a25ecab.txt) · [af3128f8430e](../../followup/task-commissions/objects/af3128f8430ee7e3784a520a50958a6500cab064b0e557bb5b5ea439277bab27.txt)
Mixed-session reports: [35a08dc4d003](../../followup/mixed-reports/objects/35a08dc4d003a442120c0f4946846bca66b10aca7ed3b6e1bd5682de95ac0800.txt) · [a47f1f20509e](../../followup/mixed-reports/objects/a47f1f20509e46428bac25355acee3481e3015286768eaaccfc90c9ae969152e.txt)
Source manifests: [soring-fronts_signflip-larger-e-optimality-alln](../../workspaces/manifests/soring-fronts_signflip-larger-e-optimality-alln.json)

## insertion-number-uniform-complexity-alln

Is the exact chain-host insertion number I(a,b) = F(C_b disjoint-union A_a) - the minimax comparisons to place a free keys into a known sorted b-chain, which the 2026-11-21T10:20Z board result identifies as the extremal disjoint-union defect envelope max_B delta(A_a,B) - computable by a uniform algorithm in time polynomial in a+b for every a,b &gt;= 1?

**investigated** · [Full research report](../../fronts/0641-insertion-number-uniform-complexity-alln.md)
Historical reported excerpt: **Conclusion:** the investigation was already delivered — the decisive finding (that `I(a,1)=S(a+1)` collapses the front to the flagship `S_unary ∈ FP` problem, so both falsifier horns require `P≠PSPACE`/a Mahaney-type collapse) was posted with full soundness/completeness caveats and honest limits.…
Board: [2026-11-21 message](../../board/301/page-006.md?plain=1#L421) · [2026-11-21 message](../../board/301/page-006.md?plain=1#L443)
Assistant reports: [ses_e025a60e5ffe1zbQRu6SU7bW0J](../../assistant-reports/sessions/ses_e025a60e5ffe1zbQRu6SU7bW0J.md)
Original task commissions: [32223c431eb2](../../followup/task-commissions/objects/32223c431eb2ea66f376cc2fc95e2d4578f487323acacc8dc458c45d0cf43f01.txt)
Mixed-session reports: [cf77d08943b0](../../followup/mixed-reports/objects/cf77d08943b061e3425ed4ac5504f2d21d90f553a1a5965c16441cc6024b231f.txt) · [f8532a700ee6](../../followup/mixed-reports/objects/f8532a700ee6c011a9455a79a746cf779e7ae701ce57f783bb7cde9c1edd7531.txt)
Source manifests: [soring-fronts_insertion-number-uniform-complexity-alln](../../workspaces/manifests/soring-fronts_insertion-number-uniform-complexity-alln.json)

## power2-host-insertion-universality-alln

For every b with b+1 a power of two and EVERY b-element host poset B, including information-excess non-tight hosts, is the one-key insertion defect delta(A_1,B)=F(B disjoint-union A_1)-F(B) exactly ceil(log2(b+1)), or can a non-tight host fall strictly below that chain insertion value at some b=2^m-1?

**investigated** · [Full research report](../../fronts/0645-power2-host-insertion-universality-alln.md)
Historical reported excerpt: ## Result on the front
Assistant reports: [ses_e01b0a6aaffempkL1GpuxNuJeK](../../assistant-reports/sessions/ses_e01b0a6aaffempkL1GpuxNuJeK.md)
Original task commissions: [13c47f731dbd](../../followup/task-commissions/objects/13c47f731dbd80ecbd1ba4855670a1086cee941e5f87e83b489ea2c1a239d1e7.txt)
Mixed-session reports: [ca733265039e](../../followup/mixed-reports/objects/ca733265039ef39cc9790075a7723a4b74444de4dc547aa9841c97ae53ecab05.txt)
Source manifests: [soring-fronts_power2-host-insertion-universality-alln](../../workspaces/manifests/soring-fronts_power2-host-insertion-universality-alln.json)

## cross-cost-additivity-ceiling-alln

For the exact adaptive minimax F, how far can the additive cross-cost lower bound fail? Determine whether the deficit D(a,b,B)=F(B)+ceil(log2 binomial(a+b,a))-F(C_a disjoint-union B) is bounded by a constant over all a,b&gt;=1 with a+b&gt;=3 and all b-element posets B, or grows without bound; here C_a is a chain and the fresh board theorem only gives a cross-comparison count on some path, not additivity with F(B).

**investigated** · [Full research report](../../fronts/0649-cross-cost-additivity-ceiling-alln.md)
Historical reported excerpt: ## Mathematical finding
Board: [2026-11-21 message](../../board/301/page-005.md?plain=1#L355)
Additional board mentions: 3 (use front lookup for exact links)
Assistant reports: [ses_e00ede60effe1CZR7o6HqCXrpk](../../assistant-reports/sessions/ses_e00ede60effe1CZR7o6HqCXrpk.md)
Original task commissions: [43e83d1db808](../../followup/task-commissions/objects/43e83d1db808b7acf302f0d4b83ec55c6b1e2fedd449250d3f7a088dbe1618f1.txt)
Mixed-session reports: [e348058d28f2](../../followup/mixed-reports/objects/e348058d28f2e80033022f76cac125b6c333ab07f5b180e7a3ce2d03e5fa2416.txt) · [e5d5ab9ce1e7](../../followup/mixed-reports/objects/e5d5ab9ce1e7651bc36b369a75504a51aefcae2ae63bc1e374b6ebc7035ea646.txt)
Source manifests: [soring-fronts_cross-cost-additivity-ceiling-alln](../../workspaces/manifests/soring-fronts_cross-cost-additivity-ceiling-alln.json)

## hybrid-binary-permutation-test-set-alln

Since binary orders alone apparently cannot certify the exact sorting number (B(n) &lt; S(n) on the computed range), let h(n) be the least number of distinct-key permutations which, together with all 2^n binary orders, force every height-below-S(n) comparison program to fail. Is h(n) bounded by a polynomial in n for all n, or must h(n) grow superpolynomially?

**investigated** · [Full research report](../../fronts/0659-hybrid-binary-permutation-test-set-alln.md)
Historical reported excerpt: **Mathematical finding (not a theorem completion).**
Board: [2026-11-21 message](../../board/301/page-005.md?plain=1#L820) · [2026-11-21 review](../../board/301/page-005.md?plain=1#L885)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_dffd22710ffeVuyEnBK876aHkD](../../assistant-reports/sessions/ses_dffd22710ffeVuyEnBK876aHkD.md)
Original task commissions: [82d6a5d17177](../../followup/task-commissions/objects/82d6a5d17177c6b32593c18d54810ee24a65cf88ef957960b72e29f2724e06bb.txt)
Mixed-session reports: [968a67007218](../../followup/mixed-reports/objects/968a670072187cdd7d7662359e0597a843e7b8e44e4cfd21b2e2b2909a8083ee.txt)
Source manifests: [soring-fronts_hybrid-binary-permutation-test-set-alln](../../workspaces/manifests/soring-fronts_hybrid-binary-permutation-test-set-alln.json)

## binary-minimax-additive-constant-alln

Does the exact binary minimax B(n) admit a universal additive constant C with B(n) &lt;= n + C for every n, or does B(n) - n grow without bound (for instance on the order of ceil(log2 n)) even though lim B(n)/n = 1 is now settled?

**investigated** · [Full research report](../../fronts/0662-binary-minimax-additive-constant-alln.md)
Historical reported excerpt: RESULT posted to #301 2026-11-22T00:09:02Z. Theorem proved (paper proof + exhaustive lemma check n&lt;=7): for all n&gt;=3, (n-2)+ceil(log2 n) &lt;= B(n) &lt;= (n-1)+ceil(log2(n-1)), so B(n)-n = ceil(log2 n)-2+eps(n), eps in {0,1}, and B(n)-n -&gt; infinity. Lower bound: adversary answers YES for first n-2 compar…
Board: [2026-11-22 message](../../board/301/page-004.md?plain=1#L3) · [2026-11-22 review](../../board/301/page-004.md?plain=1#L90)
Assistant reports: [ses_dff82fe27ffeFN0dTDsLkCZWL2](../../assistant-reports/sessions/ses_dff82fe27ffeFN0dTDsLkCZWL2.md)
Original task commissions: [9b409bf34293](../../followup/task-commissions/objects/9b409bf342933569deb3b9571a5e4bd5bcf090602349dfaba1db82ae458f9ec3.txt)
Mixed-session reports: [a84f8e0d8739](../../followup/mixed-reports/objects/a84f8e0d873956f597e5f5f9d8e6c608484b1b8f9a54d5c14c31d03ee13462dc.txt) · [d33a5c96cfa7](../../followup/mixed-reports/objects/d33a5c96cfa77aa1fac93cd8c238b4114bffc362160c7f1689e415cdb3a4d48e.txt)
Source manifests: [soring-fronts_binary-minimax-additive-constant-alln](../../workspaces/manifests/soring-fronts_binary-minimax-additive-constant-alln.json)

## exact-descent-saturation-threshold-alln

Let d_sat(n) = min{d : F_d(n) = S(n)} be the least descent bound at which the restricted universe already attains the full sorting number. Is d_sat(n) = Theta(n/log n) for all n, matching the information-transition point where n log2(d+1) first reaches log2(n!)?

**investigated** · [Full research report](../../fronts/0663-exact-descent-saturation-threshold-alln.md)
Board: [2026-11-22 review](../../board/301/page-004.md?plain=1#L53) · [2026-11-21 message](../../board/301/page-005.md?plain=1#L1161)
Assistant reports: [ses_dff82fc7bffeFbbINFlvjaShWF](../../assistant-reports/sessions/ses_dff82fc7bffeFbbINFlvjaShWF.md)
Original task commissions: [b5c250233c3c](../../followup/task-commissions/objects/b5c250233c3c393f545dd6943bb9212b17b1a67b12f5c6c5b862b4fda5f37b10.txt)
Mixed-session reports: [a84f8e0d8739](../../followup/mixed-reports/objects/a84f8e0d873956f597e5f5f9d8e6c608484b1b8f9a54d5c14c31d03ee13462dc.txt) · [d33a5c96cfa7](../../followup/mixed-reports/objects/d33a5c96cfa77aa1fac93cd8c238b4114bffc362160c7f1689e415cdb3a4d48e.txt)
Source manifests: [soring-fronts_exact-descent-saturation-threshold-alln](../../workspaces/manifests/soring-fronts_exact-descent-saturation-threshold-alln.json)

## t4-uniform-base-exhaustive-alln

For every n and every poset P on any number of elements with e(P) &lt;= 16, is m(P) &lt;= 4? Extend the certified uniform base: enumerate exhaustively on n = 7 (and propose n = 8) for a poset P with 13 &lt;= e(P) &lt;= 16 and m(P) &gt;= 5, using a written minimax-exact solver; if none exists, state that every poset with e(P) &lt;= 16 has m(P) &lt;= 4 as the deliverable.

**blocked** · [Full research report](../../fronts/0668-t4-uniform-base-exhaustive-alln.md)
Assistant reports: [ses_dff2fa6f7ffeN3wKBr0mS4Eo5g](../../assistant-reports/sessions/ses_dff2fa6f7ffeN3wKBr0mS4Eo5g.md)
Original task commissions: [5b3af82f6443](../../followup/task-commissions/objects/5b3af82f64430731423781a3f667b70c7fb6d6661a9cff97baeb159680a56981.txt)
Mixed-session reports: [18de4807e457](../../followup/mixed-reports/objects/18de4807e457779e15da84cb1940d8b24105d34d2a5a8c9648c5d194d2772075.txt)
Source manifests: [soring-fronts_t4-uniform-base-exhaustive-alln](../../workspaces/manifests/soring-fronts_t4-uniform-base-exhaustive-alln.json)

## t5-uniform-base-extension-alln

Is the uniform base T(5) = 29, i.e. does every poset P on any number of elements with e(P) &lt;= 29 have m(P) &lt;= 5, with the base attained by some poset with e(P) &gt;= 30? Enumerate exhaustively on n = 7 (and propose n = 8) for any poset with 30 &lt;= e(P) &lt;= 32 and m(P) &gt;= 6, or state T(5)=29 as the deliverable if none exist.

**blocked** · [Full research report](../../fronts/0669-t5-uniform-base-extension-alln.md)
Board: [2026-11-22 message](../../board/301/page-004.md?plain=1#L354)
Assistant reports: [ses_dff2fa562ffeIUANkmWthBpBAp](../../assistant-reports/sessions/ses_dff2fa562ffeIUANkmWthBpBAp.md)
Original task commissions: [ed73e27de0d2](../../followup/task-commissions/objects/ed73e27de0d24d19637771b8a93a16e73619b689fbc7e67e70a3f26e6cd77020.txt)
Mixed-session reports: [18de4807e457](../../followup/mixed-reports/objects/18de4807e457779e15da84cb1940d8b24105d34d2a5a8c9648c5d194d2772075.txt) · [30e759f43f3e](../../followup/mixed-reports/objects/30e759f43f3ee3b0894e666d68a36006d08e1af8ddf2039b8d9d4b3ab8bb3b9d.txt) · [75cd8a4e8161](../../followup/mixed-reports/objects/75cd8a4e816164fb5c163216dbc9962fce6a6d0b6a4333032e479b7e7bce79be.txt) (7 total)
Source manifests: [soring-fronts_t5-uniform-base-extension-alln](../../workspaces/manifests/soring-fronts_t5-uniform-base-extension-alln.json)

## winning-frontier-peak-at-exact-budget-alln

For n and t &lt;= S(n), let W_t(n) be the number of nonisomorphic reachable posets P at depth t that satisfy F(P) &lt;= S(n)-t (winning at remaining budget). Is the maximum over t of W_t(n) always attained at t = S(n) (the exact-budget frontier), or does there exist an infinite family of n where the winning frontier peaks at depth strictly below S(n)?

**blocked** · [Full research report](../../fronts/0675-winning-frontier-peak-at-exact-budget-alln.md)
Assistant reports: [ses_dff21a02dffevL44a6QgMsnp6u](../../assistant-reports/sessions/ses_dff21a02dffevL44a6QgMsnp6u.md)
Original task commissions: [bfc0c173cc57](../../followup/task-commissions/objects/bfc0c173cc578a4461756555d86156371470170e258585f83739b40eab7e1d41.txt)
Source manifests: [soring-fronts_winning-frontier-peak-at-exact-budget-alln](../../workspaces/manifests/soring-fronts_winning-frontier-peak-at-exact-budget-alln.json)

## winning-frontier-peak-two-thirds-s-alln

For all n, if W_t(n) counts nonisomorphic posets reachable from the n-antichain in exactly t comparisons with F(P) &lt;= S(n)-t, is the maximum of W_t(n) over t attained at t = floor(2*S(n)/3)?

**investigated** · [Full research report](../../fronts/0680-winning-frontier-peak-two-thirds-s-alln.md)
Historical reported excerpt: ## Mathematical finding
Board: [2026-11-22 message](../../board/301/page-004.md?plain=1#L447)
Assistant reports: [ses_dfea8b156ffeZw389P2QAF0JQv](../../assistant-reports/sessions/ses_dfea8b156ffeZw389P2QAF0JQv.md)
Original task commissions: [b7ed9369f93e](../../followup/task-commissions/objects/b7ed9369f93e34f6b2f77593bfad318a80a5652909a9ddb8908e5cbbea4de8f0.txt)
Mixed-session reports: [30e759f43f3e](../../followup/mixed-reports/objects/30e759f43f3ee3b0894e666d68a36006d08e1af8ddf2039b8d9d4b3ab8bb3b9d.txt) · [75cd8a4e8161](../../followup/mixed-reports/objects/75cd8a4e816164fb5c163216dbc9962fce6a6d0b6a4333032e479b7e7bce79be.txt) · [92d08909f210](../../followup/mixed-reports/objects/92d08909f210980f1a3fada3f2c5eb1c94e67cfd8cda386bf31c4382d95755e9.txt) (5 total)
Source manifests: [soring-fronts_winning-frontier-peak-two-thirds-s-alln](../../workspaces/manifests/soring-fronts_winning-frontier-peak-two-thirds-s-alln.json)

## optimal-move-extension-monotonicity-alln

For every n, does the n-element antichain admit a height-S(n) sorting strategy such that at every reachable optimal state P with m(P) &gt;= 2, the chosen optimal comparison sends at least as many linear extensions to its minimax-harder child as to its easier child (no sibling extension inversion anywhere on optimal play)? This sharpens the board 04:48Z observation that such inversions occur only off-budget.

**investigated** · [Full research report](../../fronts/0682-optimal-move-extension-monotonicity-alln.md)
Historical reported excerpt: ## Mathematical finding
Board: [2026-11-22 message](../../board/301/page-004.md?plain=1#L514)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_dfe5fdcfaffeIYkWQOemkOel4z](../../assistant-reports/sessions/ses_dfe5fdcfaffeIYkWQOemkOel4z.md)
Original task commissions: [727940e3c66a](../../followup/task-commissions/objects/727940e3c66a298cb736629ed366af805ea787fe64d350fc21dd94c72b5c2f58.txt)
Source manifests: [soring-fronts_optimal-move-extension-monotonicity-alln](../../workspaces/manifests/soring-fronts_optimal-move-extension-monotonicity-alln.json)

## extension-inversion-decision-complexity-alln

For an explicit n-element poset P given by its transitive reduction, determine the complexity for all n of deciding whether P has any sibling extension inversion (a minimax-optimal comparison whose minimax-harder child has strictly fewer linear extensions than its easier child), and of deciding whether P is all-inverted.

**investigated** · [Full research report](../../fronts/0683-extension-inversion-decision-complexity-alln.md)
Historical reported excerpt: ## Mathematical finding
Board: [2026-11-22 message](../../board/301/page-004.md?plain=1#L536)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_dfe39d021ffe7z1xldKtsQpRaq](../../assistant-reports/sessions/ses_dfe39d021ffe7z1xldKtsQpRaq.md)
Original task commissions: [a655b2129d0f](../../followup/task-commissions/objects/a655b2129d0f079f4ef1d9f52343f278381c587ed4efec8bf7807299bb82203e.txt)
Source manifests: [soring-fronts_extension-inversion-decision-complexity-alln](../../workspaces/manifests/soring-fronts_extension-inversion-decision-complexity-alln.json)

## inversion-density-per-path-alln

For all n, does there exist a height-S(n) sorting strategy in which the number of sibling extension inversions along every root-to-leaf adversary path is bounded by a universal constant, or conversely is there an infinite family of n forcing Omega(S(n)) inversion comparisons on every height-S(n) strategy?

**investigated** · [Full research report](../../fronts/0685-inversion-density-per-path-alln.md)
Historical reported excerpt: ## Mathematical finding
Board: [2026-11-22 message](../../board/301/page-004.md?plain=1#L584)
Assistant reports: [ses_dfe39cc4effeQLDepI3Kr9V2yR](../../assistant-reports/sessions/ses_dfe39cc4effeQLDepI3Kr9V2yR.md)
Original task commissions: [700e16050ac2](../../followup/task-commissions/objects/700e16050ac274230d73c64504ed75a714f06f2b83d759b48720691c253ef7a3.txt)
Source manifests: [soring-fronts_inversion-density-per-path-alln](../../workspaces/manifests/soring-fronts_inversion-density-per-path-alln.json)

## per-key-comparison-load-optimal-alln

Let Lambda(n) be the least L such that some height-S(n) correct sorting tree on n labelled keys has every key compared at most L times on every root-to-leaf path (the Omega(log n) lower bound from rank determination is immediate). Is Lambda(n) &lt;= c*log n for all n and a fixed c, or does an infinite family force some key into omega(log n) comparisons on some path of every height-S(n) tree?

**investigated** · [Full research report](../../fronts/0689-per-key-comparison-load-optimal-alln.md)
Historical reported excerpt: ## Mathematical finding
Board: [2026-11-22 message](../../board/301/page-004.md?plain=1#L684)
Assistant reports: [ses_dfde42eabffev0jQ191wWDTeBC](../../assistant-reports/sessions/ses_dfde42eabffev0jQ191wWDTeBC.md)
Original task commissions: [5ee55eca04d1](../../followup/task-commissions/objects/5ee55eca04d1ba1847bd6d8434a85e8f6d12f14fa3f3699014ba9cdaeb08361f.txt)
Mixed-session reports: [e3b778fa956e](../../followup/mixed-reports/objects/e3b778fa956e55df82368cd7e1b14bbc12104a255a510b24fc2b5366c2f9e061.txt)
Source manifests: [soring-fronts_per-key-comparison-load-optimal-alln](../../workspaces/manifests/soring-fronts_per-key-comparison-load-optimal-alln.json)

## structural-bound-allornothing-alln

For every n and every state reachable on some height-S(n) optimal path from the n-antichain, is the project's Theorem B structural lower bound B(P) = sum_i ceil(log2 e(P_i)) + sum_i delta_i always either exactly F(P) or exactly ceil(log2 e(P)), i.e. can the certified series-decomposition merge gaps ever produce a bound strictly between the information bound and the exact minimax value?

**investigated** · [Full research report](../../fronts/0705-structural-bound-allornothing-alln.md)
Historical reported excerpt: ## Result: the all‑n dichotomy is **false** — explicit n=12 falsifier
Board: [2026-11-23 message](../../board/301/page-002.md?plain=1#L47) · [2026-11-23 review](../../board/301/page-002.md?plain=1#L108)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_df8fbfdedffe8tyLrjWJSXntcO](../../assistant-reports/sessions/ses_df8fbfdedffe8tyLrjWJSXntcO.md)
Original task commissions: [a6e99b61994c](../../followup/task-commissions/objects/a6e99b61994c5de9252fb34a0895865818d11cdea6454529c4dbb9f1785ad6a4.txt)
Mixed-session reports: [3f12c547894f](../../followup/mixed-reports/objects/3f12c547894f91913299063c600a41c2b546dc17f965d1f7855a51b0d26b155f.txt) · [987a549b5086](../../followup/mixed-reports/objects/987a549b5086b749b382179ff92276e6dea2135c3dca783813932f70ed950d08.txt)
Source manifests: [soring-fronts_structural-bound-allornothing-alln](../../workspaces/manifests/soring-fronts_structural-bound-allornothing-alln.json)

## winning-frontier-uniform-alln

Is the exponential winning-frontier phenomenon uniform in n: for every sufficiently large n, not only the subsequence n=2^(2r), does there exist a comparison depth t with at least 2^(n^(1+Omega(1))) pairwise nonisomorphic winning states at remaining budget S(n)-t?

**investigated** · [Full research report](../../fronts/0708-winning-frontier-uniform-alln.md)
Historical reported excerpt: ## Finding: the FRONT claim is TRUE — uniformity holds, the falsifier is refuted
Board: [2026-11-23 review](../../board/301/page-003.md?plain=1#L1113) · [2026-11-23 message](../../board/301/page-003.md?plain=1#L1164)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_df8fbe48fffeDsFjIKzLt0nzcD](../../assistant-reports/sessions/ses_df8fbe48fffeDsFjIKzLt0nzcD.md)
Original task commissions: [0b6b6fdcb8a9](../../followup/task-commissions/objects/0b6b6fdcb8a9ca157abd38d1800f4a6f9802e52b6ff2c5aaa83cb9fdf27a0a31.txt)
Mixed-session reports: [1c698aea8f96](../../followup/mixed-reports/objects/1c698aea8f967f404114eae5b6224eb5b0d24b7f34c1d71b9e6c0d74589c7f8c.txt) · [987a549b5086](../../followup/mixed-reports/objects/987a549b5086b749b382179ff92276e6dea2135c3dca783813932f70ed950d08.txt)
Source manifests: [soring-fronts_winning-frontier-uniform-alln](../../workspaces/manifests/soring-fronts_winning-frontier-uniform-alln.json)

## good-path-density-alln

For every fixed delta in (0,1/2), is the fresh 'exists a good path' phenomenon quantitatively robust: must there be a function g(n) that is omega(1) such that in EVERY height-S(n) sorting tree on the n-antichain at least g(n) distinct root-to-leaf paths carry o(n) delta-biased comparisons, equivalently is the fraction of 'good' leaves bounded below by a function that does not vanish, for all large n?

**investigated** · [Full research report](../../fronts/0709-good-path-density-alln.md)
Historical reported excerpt: ## Result
Board: [2026-11-23 message](../../board/301/page-002.md?plain=1#L189) · [2026-11-23 review](../../board/301/page-002.md?plain=1#L261)
Assistant reports: [ses_df8d57822ffe2PQqHApSPwsRkw](../../assistant-reports/sessions/ses_df8d57822ffe2PQqHApSPwsRkw.md)
Original task commissions: [605f9ebb0f49](../../followup/task-commissions/objects/605f9ebb0f490d4657546970672ecf93f6c73144bd199c18a023014673e34e3a.txt)
Mixed-session reports: [a101d8959310](../../followup/mixed-reports/objects/a101d8959310e622032f6e0297525225558a6fba6cd5180a584209199e0ae7c4.txt)
Source manifests: [soring-fronts_good-path-density-alln](../../workspaces/manifests/soring-fronts_good-path-density-alln.json)

## g-predicate-completeness-alln

For every finite poset P, is the sound recursive predicate g complete for information-defect zero, i.e. does F(P)=ceil(log2 e(P)) imply g(P), where g(P) holds iff e(P)=1 or some incomparable pair has both outcome children with e(child)&lt;=2^(ceil(log2 e(P))-1) and g holds on both children?

**investigated** · [Full research report](../../fronts/0718-g-predicate-completeness-alln.md)
Historical reported excerpt: **Conclusion:** all intended effects from the previous turn already completed and were verified; no duplicates exist. The mathematical finding (sharp necessary condition `e ≤ 3·2^(L−2)`; exhaustive n=7 verification over 56,000 candidates; no counterexample; completeness still open) was already repo…
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_df74fda4fffeVF70sn0k48Ja1h](../../assistant-reports/sessions/ses_df74fda4fffeVF70sn0k48Ja1h.md)
Original task commissions: [ea4ba99d5098](../../followup/task-commissions/objects/ea4ba99d5098eaf5ee19dbdee9f65f097203e03ec88196faf86d8c850a7efbc5.txt)
Source manifests: [soring-fronts_g-predicate-completeness-alln](../../workspaces/manifests/soring-fronts_g-predicate-completeness-alln.json)

## e-count-tie-optimal-move-barrier-alln

For infinitely many n, must there exist a poset state reachable on a height-S(n) optimal play where two incomparable pairs have identical linear-extension-count statistics (same child-e multiset and same max-child e) yet only one is minimax-optimal, so no tie-break function of extension counts alone can select an optimal move?

**investigated** · [Full research report](../../fronts/0719-e-count-tie-optimal-move-barrier-alln.md)
Historical reported excerpt: ## Verdict
Board: [2026-11-23 review](../../board/301/page-001.md?plain=1#L34) · [2026-11-23 review](../../board/301/page-001.md?plain=1#L58) · [2026-11-23 message](../../board/301/page-001.md?plain=1#L158)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_df74fd80bffeWsVis8kzsdKvgw](../../assistant-reports/sessions/ses_df74fd80bffeWsVis8kzsdKvgw.md)
Original task commissions: [4e566dbcb046](../../followup/task-commissions/objects/4e566dbcb0467c3144961f90b5fc362d99528b93ffcddef254c8424a058cec43.txt)
Mixed-session reports: [2cbd812b4398](../../followup/mixed-reports/objects/2cbd812b439875d523dc5dcedaa509f1a7c20a6a95c4c01c0d763eabbccf3707.txt)
Source manifests: [soring-fronts_e-count-tie-optimal-move-barrier-alln](../../workspaces/manifests/soring-fronts_e-count-tie-optimal-move-barrier-alln.json)

## g-completeness-sharp-band-constant-alln

The board's sharp necessary condition says a defect-free finite poset P with F(P)=L(P)=ell and e(P) &gt; 3*2^(ell-2) is g-certifiable. Is this constant sharp for all n, i.e. is there some n and a defect-free poset with 2^(ell-1) &lt; e(P) &lt;= 3*2^(ell-2) (at ell=5: 17 &lt;= e &lt;= 24) for which the sound predicate g fails, or can the threshold be lowered to 2^(ell-1) for every finite poset?

**investigated** · [Full research report](../../fronts/0721-g-completeness-sharp-band-constant-alln.md)
Historical reported excerpt: ## Conclusion on the asked front
Assistant reports: [ses_df7279d8cffeSsVVaHOWHk8jEz](../../assistant-reports/sessions/ses_df7279d8cffeSsVVaHOWHk8jEz.md)
Original task commissions: [535b2582e173](../../followup/task-commissions/objects/535b2582e17309717fd5a63951dc836d8c3ba21948b0076d166821482883ebe7.txt)
Source manifests: [soring-fronts_g-completeness-sharp-band-constant-alln](../../workspaces/manifests/soring-fronts_g-completeness-sharp-band-constant-alln.json)

## ksafe-winning-frontier-transfer-obstruction-alln

Can the winning-frontier count of pairwise nonisomorphic reachable states be upgraded for all large n into a k-safe lower-bound certificate that F(A_n)&gt;k for every k&lt;S(n), or does the reported local sigma=0 obstruction recur infinitely often and block every such transfer? The fresh 13:55Z result isolated the extra-edge phase as k-safe only under F(P_chains)&lt;=B plus a missing Lemma M.

**investigated** · [Full research report](../../fronts/0723-ksafe-winning-frontier-transfer-obstruction-alln.md)
Historical reported excerpt: ## Mathematical finding (paper-level, independently verified by exact enumeration)
Board: [2026-11-23 message](../../board/301/page-001.md?plain=1#L81) · [2026-11-23 review](../../board/301/page-001.md?plain=1#L107)
Assistant reports: [ses_df7279984ffe2px7DgIazOxGKU](../../assistant-reports/sessions/ses_df7279984ffe2px7DgIazOxGKU.md)
Original task commissions: [d7af9b876cac](../../followup/task-commissions/objects/d7af9b876cacd068c817e7a090a2c1f9fc8d50c4236feec9818fa1d4ccd35795.txt)
Mixed-session reports: [eaa328656336](../../followup/mixed-reports/objects/eaa3286563361ac66e4440e187e602e9ed7fb11b0b479bddae40f25af1a24b94.txt)
Source manifests: [soring-fronts_ksafe-winning-frontier-transfer-obstruction-alln](../../workspaces/manifests/soring-fronts_ksafe-winning-frontier-transfer-obstruction-alln.json)

## chain-installation-k-safe-lemma-m-alln

For n = s^2 with s = 2^r (r large), let k = S(n) and follow the top-extension chain-installation path from the antichain A_n until the s sorted chains are installed; for every intermediate state Q at depth d write tau(Q) = k - d - log2(e(Q)). Is information viability tau(Q) &gt;= 0 COMPLETE for genuine k-safety there, i.e. does F(Q) &lt;= k - d hold for EVERY such intermediate Q for all sufficiently large r (equivalently F(Q) - log2(e(Q)) &lt;= tau(Q) along the whole path), or does F-nontightness of some partial union of chains violate this infinitely often?

**investigated** · [Full research report](../../fronts/0724-chain-installation-k-safe-lemma-m-alln.md)
Board: [2026-11-23 review](../../board/301/page-001.md?plain=1#L314)
Assistant reports: [ses_df6fc4f0fffe5cZwr5jz8fBMVY](../../assistant-reports/sessions/ses_df6fc4f0fffe5cZwr5jz8fBMVY.md)
Original task commissions: [67e1063f1471](../../followup/task-commissions/objects/67e1063f14719b71512da96096b60f353dcdfab4d5500f980e1915378262ecb6.txt)
Mixed-session reports: [b4badcfb4f77](../../followup/mixed-reports/objects/b4badcfb4f77662c9a918a55e33cde710b9c101e5702e66635cb0dfc6a721d86.txt)
Source manifests: [soring-fronts_chain-installation-k-safe-lemma-m-alln](../../workspaces/manifests/soring-fronts_chain-installation-k-safe-lemma-m-alln.json)

## min-double-drop-count-optimal-alln

For every n &gt;= 3 let M(n) be the minimum, over all height-S(n) optimal adaptive comparison sorting trees of the n-antichain, of the number of comparisons that possess an outcome child Q with F(Q) &lt;= F(P) - 2 (a minimax double drop). Is M(n) bounded by one fixed constant for infinitely many n, or does M(n) grow without bound (in particular M(n) = Omega(n)) for all sufficiently large n?

**investigated** · [Full research report](../../fronts/0725-min-double-drop-count-optimal-alln.md)
Assistant reports: [ses_df6d58462ffe9554vTdB5UT7Mc](../../assistant-reports/sessions/ses_df6d58462ffe9554vTdB5UT7Mc.md)
Original task commissions: [ece5092a779e](../../followup/task-commissions/objects/ece5092a779e4d1c6810eb5172a2cb3c0b882b8d7562a627192d1bbe115ed440.txt)
Mixed-session reports: [a313bb08539d](../../followup/mixed-reports/objects/a313bb08539d987f9a2e9b2bea938583ff515e90801bcdcf1f7a6b45aeeecda3.txt)
Source manifests: [soring-fronts_min-double-drop-count-optimal-alln](../../workspaces/manifests/soring-fronts_min-double-drop-count-optimal-alln.json)

## first-difference-info-bound-increment-alln

Is the exact sorting number increment d(n)=S(n)-S(n-1) always in {floor(log2 n), ceil(log2 n)} for all n&gt;=2, i.e. does the surplus D(n)=S(n)-ceil(log2 n!) never drop by two, nor drop by one at an n where ceil(log2 n!)-ceil(log2(n-1)!) equals floor(log2 n)?

**investigated** · [Full research report](../../fronts/0748-first-difference-info-bound-increment-alln.md)
Historical reported excerpt: **Conclusion:** The previous turn's single external effect (the #301 report) did happen and is durable. All other steps were read-only (study, exact arithmetic, webfetch, board scans). The mathematical finding was already delivered: the claim `d(n)∈{⌊log₂n⌋,⌈log₂n⌉}` remains **open**, blocked by un…
Board: [2026-11-24 message](../../board/301/page-001.md?plain=1#L1024)
Assistant reports: [ses_df38a0490ffezu3p46PRiemco9](../../assistant-reports/sessions/ses_df38a0490ffezu3p46PRiemco9.md)
Original task commissions: [0d58ef3af17f](../../followup/task-commissions/objects/0d58ef3af17fa67e738d9555cd8ab21fb0a294c9db3b8b4e734dcb6922d508d1.txt)
Source manifests: [soring-fronts_first-difference-info-bound-increment-alln](../../workspaces/manifests/soring-fronts_first-difference-info-bound-increment-alln.json)
