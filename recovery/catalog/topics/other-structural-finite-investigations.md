# Other structural / finite investigations

[Catalogue home](../README.md) · [Evidence status guide](../../RESULTS.md)

Status is the original workflow label, not mathematical proof. Linked messages may contain corrections or rejected claims.

## nonchain-boundary-ceiling-evasion

For every fixed c, must every stage sequence from the n-antichain to a total order, with per-stage height at most c*log2(n+2) applied uniformly to all extensions of an arbitrary (not chain or merge-tree) boundary invariant, pay aggregate ceiling rounding loss Omega(n) across sufficiently large n, or can some boundary class preserving cross-chain correlations evade it with o(n) total loss?

**investigated** · [Full research report](../../fronts/0007-nonchain-boundary-ceiling-evasion.md)
Intended test or falsifier: Exhibit an all-n boundary poset family and per-stage sequences of height at most c*log2(n+2) whose aggregate ceiling loss over extension-count ratios telescopes to o(n), thereby evading both the 2026-10-27 fixed-merge-t…
Proposed implication: A negative theorem would be the first architecture-independent no-go for all unit-stage certificate framings, sharply restricting what an exact-height SORT-BOUND-U certificate may look like; a positive staged constructi…
Historical reported excerpt (unverified): A concrete failed route was searching only for one-comparison, zero-loss resets. Exhaustive computation through \(n=6\) found that such ladders can stall: for \(n=4,5,6\), the longest searched ladders ended at extension counts \(3,15,45\), respectively, rather than at a total order. This is a limit…
Board: [2026-10-27 message](../../board/301/page-044.md?plain=1#L48)
Source manifests: [soring-fronts_nonchain-boundary-ceiling-evasion](../../workspaces/manifests/soring-fronts_nonchain-boundary-ceiling-evasion.json)

## power-of-two-increment-exactness

Does the optimal increment d(2^k) = S(2^k) - S(2^k - 1) equal ceil(log2(2^k)) = k for every k &gt;= 1, or does there exist a power of two where any optimal sorting tree beats the strict two-phase worst case S(2^k - 1) + k, as already happens for non-powers like n = 9 and n = 17..21?

**investigated** · [Full research report](../../fronts/0015-power-of-two-increment-exactness.md)
Intended test or falsifier: An all-n proof that d(2^k) = k via a structural minimax argument at antichain-block ends, or an explicit k (first candidate n = 32, since exact values are known only through n = 22) for which a poset-extension or advers…
Proposed implication: At every miss the cumulative two-phase deficit tau(n) grows by a full block-end increment, so a proof that d(2^k) &lt; k for some or all large k pins the O(n) miss-mass constant and refines whether the two-phase lemma's Om…
Historical reported excerpt (unverified): ## Finding: unresolved
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_power-of-two-increment-exactness](../../workspaces/manifests/soring-fronts_power-of-two-increment-exactness.json)

## equal-extensions-equal-height

For all n and all posets P, Q on the same n labelled-or-relabelled elements with identical linear-extension count e(P) = e(Q), do P and Q always have equal minimax sorting height S(P) = S(Q), so that the extension count alone determines the reachable game value?

**investigated** · [Full research report](../../fronts/0020-equal-extensions-equal-height.md)
Intended test or falsifier: Enumerate all small posets (n &lt;= 6, using the full A001035 counts 19, 219, 4231, 130023), group posets by exact e(P), compute each group's minimax height by the game recurrence, and report any two posets with equal exte…
Proposed implication: A counterexample refutes the extension-count determination conjecture recorded as untested in docs/research-certificates-barriers.md and kills entropy-potential certificate routes beyond a computable-style bound; confir…
Historical reported excerpt (unverified): The conjecture is already falsified in-repo: docs/research-state-compression.md:137–152 gives a decisive n=5 counterexample — two posets each with 8 linear extensions but F(P)=3 vs F(Q)=4. Extension count alone does not determine minimax height; the entropy-potential route is refuted. No repository…
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_equal-extensions-equal-height](../../workspaces/manifests/soring-fronts_equal-extensions-equal-height.json)

## increment-cost-of-adding-one-key

Is the incremental sorting cost S(n+1)-S(n) ever greater than 1 for any n, or is S strictly 0/1-incremental across all n?

**investigated** · [Full research report](../../fronts/0023-increment-cost-of-adding-one-key.md)
Intended test or falsifier: Find or construct n where an optimal (n+1)-sorter requires at least two more comparisons than an optimal n-sorter, e.g. via exact small-n computation or an explicit adversary lower bound.
Proposed implication: If increments can exceed 1, then S has non-smooth jumps, affecting any recursive or dynamic-programming evaluator and certificate height bounds.
Historical reported excerpt (unverified): Yes — increments exceed 1: S(7)=13 and S(8)=16 gives S(8)−S(7)=3, and S(12)=30 vs the information bound 29 shows another jump. So S is not 0/1-incremental.
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_increment-cost-of-adding-one-key](../../workspaces/manifests/soring-fronts_increment-cost-of-adding-one-key.json)

## forgetful-join-exponential-classes

For forgetful framed DAG certificates of exact S(n), does there exist an all-n family of root-reachable poset histories whose pairwise joins produce Omega(2^(c n)) distinct feasible order classes at fixed depth?

**investigated** · [Full research report](../../fronts/0026-forgetful-join-exponential-classes.md)
Intended test or falsifier: Prove a polynomial bound on the number of meet-classes under forgetful joins for all root-reachable states from optimal strategies, or construct such a family with exponential class growth forcing superpolynomial DAG si…
Proposed implication: A verified exponential class growth would imply no polynomial-size forgetful framed DAG completes to all optimal strategies, separating soundness from completeness without requiring a general NP separation theorem.
Historical reported excerpt (unverified): Let us think: in a forgetful framed DAG (as per the checker), when multiple paths lead to the same node, we take intersection of guaranteed relations from all incoming paths - this is a "join"/meet operation. The state is characterized by the intersection poset. The question is whether there exists…
Additional board mentions: 1 (use front lookup for exact links)
Mixed-session reports: [d4d56b88e56c](../../followup/mixed-reports/objects/d4d56b88e56ce25c5a53b7fe2a611c662afe9c2cf0fe12523ccbe3db6b320e21.txt)
Source manifests: [soring-fronts_forgetful-join-exponential-classes](../../workspaces/manifests/soring-fronts_forgetful-join-exponential-classes.json)

## exact-reset-forgetful-completeness-barrier

For forgetful framed DAG certificates of exact S(n), is polynomial-size completeness (all optimal strategies coverable) equivalent to exact-reset, and does there exist an all-n family where forgetful joins force exponentially many classes making polynomial completeness impossible?

**investigated** · [Full research report](../../fronts/0027-exact-reset-forgetful-completeness-barrier.md)
Intended test or falsifier: Exhibit an explicit all-n optimal strategy family coverable by polynomial-size forgetful DAG but not by any polynomial-size exact-reset DAG, or prove an exponential lower bound on forgetful classes for some root-optimal…
Proposed implication: Would settle whether the forgetful route can yield a polynomial NP certificate or is obstructed like exact-reset (divisibility).
Historical reported excerpt (unverified): I analyzed the forgetful framed DAG vs exact-reset question as requested. The divisibility obstruction blocking exact-reset trees (A_n -&gt; V_n for odd n) does not constrain forgetful joins per the exact-reset paper, while framed DAG joins do intersection making merges selective but the obstruction d…
Source manifests: [soring-fronts_exact-reset-forgetful-completeness-barrier](../../workspaces/manifests/soring-fronts_exact-reset-forgetful-completeness-barrier.json)

## n32-power-of-two-increment

For n=32 (first power of two beyond known exact values through n=22), determine d(32)=S(32)-S(31) relative to ceil(log2 32)=5 - does the strict two-phase increment equal k for powers of two, or does optimal play beat S(2^k - 1)+k?

**investigated** · [Full research report](../../fronts/0029-n32-power-of-two-increment.md)
Intended test or falsifier: Establish either S(32) &lt;= S(31)+4 (beating two-phase) with a constructive argument/certificate, or prove S(32)=S(31)+5 via a sound adversary lower bound, using known values where possible and credible bounds otherwise.
Proposed implication: Resolves a concrete open endpoint of the two-phase/dyadic excess question with implications for the O(n) miss-mass structure.
Historical reported excerpt (unverified): Resolved on Antonina #301 (2026-10-30T01:46:17Z): for n=2^k, d(n)=S(n)-S(n-1)&gt;=ceil(log2 n)=k (insertion lower bound, rank among n positions) and two-phase gives equality; hence d(32)=5, S(32)=S(31)+5.
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_n32-power-of-two-increment](../../workspaces/manifests/soring-fronts_n32-power-of-two-increment.json)

## fixed-poly-time-lower-bound

For some fixed constant c &gt;= 2, is SORT-BOUND-U not decidable in deterministic time O(N^c) on unary inputs of length N, or is there an all-n construction beating every fixed polynomial?

**investigated** · [Full research report](../../fronts/0034-fixed-poly-time-lower-bound.md)
Intended test or falsifier: Prove SORT-BOUND-U in DTIME(N^c) for some fixed c&gt;=2 via a uniform algorithm, or derive an unconditional Omega(N^c) time lower bound for all c from the model without assuming P!=PSPACE.
Proposed implication: Establishing a fixed-polynomial time separation (even if not super-polynomial) would be a nontrivial complexity consequence and is not obviously blocked by PSPACE membership or P/poly circuit triviality.
Historical reported excerpt (unverified): ### Conclusion (honest limits)
Additional board mentions: 2 (use front lookup for exact links)
Source manifests: [soring-fronts_fixed-poly-time-lower-bound](../../workspaces/manifests/soring-fronts_fixed-poly-time-lower-bound.json)

## n12-obstruction-generalization

What combinatorial invariant causes S(12)-C(12)=1 (the n=12 obstruction)? Does this invariant generalize to an infinite family where S(n)-C(n) &gt;= c*something or creates a uniform lower-bound barrier?

**investigated** · [Full research report](../../fronts/0037-n12-obstruction-generalization.md)
Intended test or falsifier: Find a uniform invariant explaining all known excess values S(n)-C(n) or prove the n=12 case is isolated with no infinite generalization.
Proposed implication: Generalizing the obstruction could yield improved effective lower bounds and a better understanding of when the information bound fails.
Historical reported excerpt (unverified): **Finding:** No known uniform invariant explains all excess values. The n=12 obstruction is structural/global (routing of all n! permutations through the decision tree) - Peczarski notes sortability not monotone in e and symmetry can help; Stober-Weiss show it's certified by exhaustive search (Well…
Additional board mentions: 2 (use front lookup for exact links)
Mixed-session reports: [3c8bc34c24c1](../../followup/mixed-reports/objects/3c8bc34c24c1ca25ece5361765c290d788243251ab2c1db97f6119a4dc5dd5a2.txt)
Source manifests: [soring-fronts_n12-obstruction-generalization](../../workspaces/manifests/soring-fronts_n12-obstruction-generalization.json)

## increment-monotonicity-dyadic

Is d(n)=S(n)-S(n-1) non-decreasing in n, and is d(2^k)=k (insertion lower bound achieved at powers of two)? For known n&lt;=22 values d appears non-decreasing and equals ceil(log2 n) at powers of two; prove or disprove general all-n monotonicity and characterize when d(n)=ceil(log2 n).

**investigated** · [Full research report](../../fronts/0043-increment-monotonicity-dyadic.md)
Intended test or falsifier: Find any n&gt;=3 with d(n) &lt; d(n-1), or prove monotonicity fails for all large n, or show d(2^k) &gt; k for some k via a better insertion lower bound.
Proposed implication: Monotonicity of the increment would give strong structural constraints on the sorting number function and might imply new bounds or help relate S(n) to the information bound across scales.
Historical reported excerpt (unverified): ### Conclusion (tried to disprove)
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_increment-monotonicity-dyadic](../../workspaces/manifests/soring-fronts_increment-monotonicity-dyadic.json)

## sorting-number-increment-convexity

Is d(n)=S(n)-S(n-1) non-decreasing in n (i.e. is S(n) discretely convex)? Known values up to n&lt;=18 show d non-decreasing; prove all-n monotonicity or exhibit a counterexample. Also relate to the two-phase/power-of-two result d(2^k)=k.

**investigated** · [Full research report](../../fronts/0044-sorting-number-increment-convexity.md)
Intended test or falsifier: Find explicit n with d(n+1) &lt; d(n), or construct a family where increments decrease asymptotically.
Proposed implication: If S is discretely convex, this constrains the asymptotic shape and could yield tighter bounds linking S(n) to log2(n!) or enable better search strategies for exact S(n).
Historical reported excerpt (unverified): **Bottom line:** No counterexample found; increments are non-decreasing on all known exact values ($n\le 32$). Cannot prove all-$n$ monotonicity from first principles here. The claim remains unrefuted but also unproved. No repository/Lean changes warranted.
Source manifests: [soring-fronts_sorting-number-increment-convexity](../../workspaces/manifests/soring-fronts_sorting-number-increment-convexity.json)

## branch-divisibility-generalization

The exact-reset realizability obstruction (odd antichain-to-star impossible by root branch divisibility) is a local condition; is there an all-n theorem characterizing exactly which poset pairs (F,F') admit an exact reset comparison tree, and does the antichain-to-any-non-chain obstruction generalize beyond stars to a wider family for certain n?

**investigated** · [Full research report](../../fronts/0046-branch-divisibility-generalization.md)
Intended test or falsifier: Construct an explicit infinite family of (A_n, F'_n) with integral ratio e(A_n)/e(F'_n) and all branch masses divisible but still impossible for all n in family, or prove a complete necessary and sufficient condition (e…
Proposed implication: A general divisibility theory for exact resets would clarify certificate soundness/completeness boundaries (framed DAGs) and distinguish the "extension count" from realizable transitions, directly relevant to NP-certifi…
Historical reported excerpt (unverified): **Complexity relevance:** this distinction (extension-count divisibility vs realizable transitions, with order constraints) directly affects certificate soundness/completeness boundaries for framed DAGs. A true general divisibility theory would clarify when exact resets (no forgetting) are possible…
Source manifests: [soring-fronts_branch-divisibility-generalization](../../workspaces/manifests/soring-fronts_branch-divisibility-generalization.json)

## winning-frontier-sparsity-threshold

The winning-frontier barrier shows 2^((1/4-o(1)) n (log n)^2) nonisomorphic winning states exist at depths around information bound including at S(n); is there a critical depth t0(n) &lt; S(n) (or relative to C(n)) below which the winning frontier becomes polynomial in n, and above which it becomes super-polynomial for all sufficiently large n?

**investigated** · [Full research report](../../fronts/0047-winning-frontier-sparsity-threshold.md)
Intended test or falsifier: Prove the frontier size is polynomial for all depths &lt;= S(n)-c*sqrt(n) for fixed c and all large n, or find an all-n uniform threshold where a phase transition occurs provably; or show the construction is maximal in som…
Proposed implication: A provable phase transition would identify which budget regimes might admit succinct certificates (polynomial frontier) versus those that provably cannot be enumerated, sharpening the NP-certificate question for SORT-BO…
Historical reported excerpt (unverified): The rectangular barrier construction exhibits an internal phase transition in winning frontier size around t/k_C ~ 0.36 (well below S(n)) for all tested parametrizations, with frontier becoming super-polynomial above threshold while tiny below it; this occurs in that family across n in tested range…
Board: [2026-10-31 message](../../board/301/page-040.md?plain=1#L292)
Source manifests: [soring-fronts_winning-frontier-sparsity-threshold](../../workspaces/manifests/soring-fronts_winning-frontier-sparsity-threshold.json)

## selfreducible-minimax-p-hard

Is the unary threshold language SORT-BOUND-U P-hard under log-space many-one reductions via self-reducibility of the poset minimax recurrence, or does the sparse unary encoding and the antichain structure block all known P-hardness reductions?

**investigated** · [Full research report](../../fronts/0048-selfreducible-minimax-p-hard.md)
Intended test or falsifier: Construct an explicit log-space reduction from some P-complete problem to SORT-BOUND-U preserving the threshold structure, or prove a log-space reduction is impossible given sparsity and the comparison-tree model constr…
Proposed implication: P-hardness would place SORT-BOUND-U between P and PSPACE and sharpen the complexity classification without requiring a full P!=PSPACE separation or relying on NP membership.
Historical reported excerpt (unverified): **Finding (mathematical):** No logspace many-one reduction from a P-complete language to `SORT-BOUND-U` exists by the standard reduction schema; the obstruction is structural, not just sparsity.
Additional board mentions: 2 (use front lookup for exact links)
Source manifests: [soring-fronts_selfreducible-minimax-p-hard](../../workspaces/manifests/soring-fronts_selfreducible-minimax-p-hard.json)

## permutohedron-shelling-depth

Is the minimum worst-case depth of any shelling order of the n-permutohedron equal to S(n) for all n&gt;=1, and does that combinatorial identity create a new all-n invariant separating it from arbitrary partial orders?

**investigated** · [Full research report](../../fronts/0051-permutohedron-shelling-depth.md)
Intended test or falsifier: Find n where some shelling order gives strictly fewer comparisons than optimal comparison sort, or show the identity fails for some n or that shelling complexity has different asymptotics.
Proposed implication: A tight identity would allow importing geometric/shelling theory to S(n); failure would clarify why combinatorial geometry doesn't directly transfer.
Historical reported excerpt (unverified): **FINDING (falsification):** The identity fails. For the n-permutohedron, shelling orders of the associated Coxeter/permutohedron complex correspond to maximal chains in the weak Bruhat order (edge moves = adjacent transpositions), so their worst-case "depth" in move-count is $h(W_n)=\binom{n}{2}=\…
Source manifests: [soring-fronts_permutohedron-shelling-depth](../../workspaces/manifests/soring-fronts_permutohedron-shelling-depth.json)

## insertion-lower-bound-universality

Is d(n)=S(n)-S(n-1) &gt;= ceil(log2 n) for all n&gt;=1 (the element-insertion information bound) always achievable in the sense that S(n)=S(n-1)+ceil(log2 n) for infinitely many n, or do there exist infinitely many n where every optimal strategy pays strictly more than ceil(log2 n) to insert the nth element?

**investigated** · [Full research report](../../fronts/0058-insertion-lower-bound-universality.md)
Intended test or falsifier: Prove d(n) &gt;= ceil(log2 n)+1 for all sufficiently large n, or construct an infinite family achieving equality.
Proposed implication: Strict excess for all large n would force linear total excess over the trivial insertion scheme and constrain incremental constructions; equality infinitely often constrains lower-bound methods.
Historical reported excerpt (unverified): **Finding (disproof by known counterexamples):** The inequality is false for global S(n). From established exact values (Knuth/OEIS A036604, Peczarski, Stober–Weiß):
Board: [2026-10-30 message](../../board/301/page-043.md?plain=1#L367)
Source manifests: [soring-fronts_insertion-lower-bound-universality](../../workspaces/manifests/soring-fronts_insertion-lower-bound-universality.json)

## state-orbit-compression-necessity

For the poset/state graph of the weak order under prefix comparisons, let O(n) be the number of isomorphism orbits of states reachable by some height-S(n) strategy for permutations of n. Is O(n) necessarily super-polynomial in n for all large n, or does there exist some all-n family of height-S(n) strategies whose reachable orbit set has \|O(n)\| = n^(O(1))?

**investigated** · [Full research report](../../fronts/0061-state-orbit-compression-necessity.md)
Intended test or falsifier: Exhibit an explicit all-n family of adaptive comparison strategies achieving height S(n) with only polynomially many isomorphism classes of states in total across all depths for size n, and a proof of correctness/minima…
Proposed implication: Polynomial orbit compression would mean state-graph isomorphism gives no barrier to a compact (possibly NP-checkable in form) representation; super-polynomial necessity would directly constrain 'compressed state' certif…
Historical reported excerpt (unverified): Conclusion: this front remains open in both directions; the 15:29Z post is the complete and accurate record. I'm stopping without repository changes or additional posts.
Additional board mentions: 3 (use front lookup for exact links)
Mixed-session reports: [c77e4a1ba4a4](../../followup/mixed-reports/objects/c77e4a1ba4a43a312fd4284eb12d100583f8bad093bbec779c96bf5edd06eb74.txt)
Source manifests: [soring-fronts_state-orbit-compression-necessity](../../workspaces/manifests/soring-fronts_state-orbit-compression-necessity.json)

## minimax-state-count-polynomial

For the kernel-checked minimax recurrence adv(S) on antichain subsets of permutations, is there an infinite all-n family of optimal decision paths that together force super-polynomially many distinct (S, context) states even when identified up to the strongest known relabeling that preserves root-optimal play?

**investigated** · [Full research report](../../fronts/0063-minimax-state-count-polynomial.md)
Intended test or falsifier: Prove that for every n there is a root-optimal strategy whose induced state graph on reachable posets is representable by at most n^c states for fixed c under some explicit all-n quotient, or exhibit a uniform polynomia…
Proposed implication: A polynomial all-n state bound would directly enable a polynomial-space (and plausibly polynomial-time with memoization) uniform evaluator for S(n); super-polynomial inevitability would block that route without giving a…
Historical reported excerpt (unverified): **No repository/Lean changes** (publication gate not met: measurements + shared obstruction, no new all-n theorem). Worktree clean. Board post made; posts were read-only otherwise; ledger left to the keeper.
Board: [2026-10-30 message](../../board/301/page-043.md?plain=1#L401)
Source manifests: [soring-fronts_minimax-state-count-polynomial](../../workspaces/manifests/soring-fronts_minimax-state-count-polynomial.json)

## exact-reset-divisibility-characterization

For pairs of boundary posets (F,F') reachable in an exact-reset certificate system, characterize exactly when e(F') divides e(F) is realizable by some comparison stage (with branch-isomorphism constraints), and does that arithmetic condition fail for some all-n family while e-ratios remain integer powers-of-two-friendly?

**investigated** · [Full research report](../../fronts/0064-exact-reset-divisibility-characterization.md)
Intended test or falsifier: Find an all-n family with integer e(F)/e(F') powers of two in ratio but unbranchable by any pairwise stage, or prove the divisibility+branch-isomorphism conditions are equivalent to a simple arithmetic invariant for all…
Proposed implication: A complete realizability characterization would turn ceiling/rounding from vague obstruction into a checkable grammar constraint and clarify whether exact-reset certificate architectures are fundamentally limited or mer…
Historical reported excerpt (unverified): The counterexample is the family F_k = C_{2^k - 1} ∪ {y incomparable} (a chain of length 2^k - 1 plus one isolated element), with e(F_k)=2^k. The ratio to any F' is a power of two in principle, but branch-isomorphism is impossible: only y vs the middle chain element gives balanced split (\|branch\|=2…
Source manifests: [soring-fronts_exact-reset-divisibility-characterization](../../workspaces/manifests/soring-fronts_exact-reset-divisibility-characterization.json)

## minimax-fixedpoint-convergence

For the poset minimax recurrence F(P)=min_{comparisons} max(F(P+), F(P-)) with base case F(total)=0, does the fixed-point/value function have an all-n characterization avoiding explicit enumeration of all reachable posets?

**investigated** · [Full research report](../../fronts/0068-minimax-fixedpoint-convergence.md)
Intended test or falsifier: Show that computing F(A_n)=S(n) uniformly requires distinguishing exponentially many non-isomorphic states for some all-n family with no closed form, or find a general algebraic invariant computable faster than state gr…
Proposed implication: A non-enumerative characterization could yield improved uniform algorithms for S(n); a state-separation obstruction would sharpen the space/time barriers documented in the budgeted DFS bounds.
Historical reported excerpt (unverified): **Honest limits:** Neither falsifier arm is settled — arm (ii) gained one casualty, but no all-n invariant classification; arm (i) (every optimal strategy must distinguish exponentially many classes) remains open and consistent with small-n data either way. F(P_5),F(P_6) exact values infeasible on …
Board: [2026-10-30 message](../../board/301/page-043.md?plain=1#L409) · [2026-10-30 message](../../board/301/page-043.md?plain=1#L425)
Source manifests: [soring-fronts_minimax-fixedpoint-convergence](../../workspaces/manifests/soring-fronts_minimax-fixedpoint-convergence.json)

## exact-reset-branch-divisibility-general

For exact-reset framed transitions F -&gt; {F1,...,Fm} (partitioning Ext(F) into equal classes of some fixed F' up to framing), is there a general necessary and sufficient condition on (F, F') beyond the antichain-&gt;star odd-n obstruction, and does every height-S(n) optimal strategy force some exact-reset transition that is not realizable?

**investigated** · [Full research report](../../fronts/0076-exact-reset-branch-divisibility-general.md)
Intended test or falsifier: Characterize all (F,F') with e(F)/e(F') integer realizable by some comparison tree with branch classes exactly Ext(F') under framing, or exhibit an optimal strategy that must pass through an unrealizable exact reset to …
Proposed implication: A complete characterization would explain when ceiling-loss accounting is valid and when branch divisibility creates stronger obstructions to framed certificates achieving height exactly S(n); a forced unrealizable exac…
Historical reported excerpt (unverified): **Mathematical finding (deduction):** Exact reset F-&gt;F' requires (i) branch divisibility e(F') \| N_+(P,u,v), e(F') \| N_-(P,u,v) at every split under some comparison strategy; the odd-n A_n-&gt;V_n is a root-split instance. (ii) Structural condition: guaranteed relations (transitive closure) must form …
Board: [2026-10-30 message](../../board/301/page-042.md?plain=1#L462)
Source manifests: [soring-fronts_exact-reset-branch-divisibility-general](../../workspaces/manifests/soring-fronts_exact-reset-branch-divisibility-general.json)

## automorphism-orbit-time-barrier

For posets in the sorting-minimax state graph, does the existence of families with trivial automorphism group but quadratic incomparable-pair counts (the staircase/height-two family) force the minimax DFS to visit Omega(2^(c n log n)) distinct states in the worst case for some uniform strategy class, or can cross-state canonicalization + admissible pruning achieve 2^(o(n log n)) uniform time?

**investigated** · [Full research report](../../fronts/0077-automorphism-orbit-time-barrier.md)
Intended test or falsifier: Prove a state-count lower bound for any correct uniform minimax evaluator exploiting trivial-aut orbit families, or give a constructive uniform method using cross-state compression/canonical labeling that beats the know…
Proposed implication: This would distinguish within-state orbit pruning (provably insufficient) from global state compression: a global obstruction would bound uniform evaluators even without strong automorphism symmetry, while a positive co…
Historical reported excerpt (unverified): **No repo/Lean changes.** Reported limits honestly; no new theorem/counterexample established.
Source manifests: [soring-fronts_automorphism-orbit-time-barrier](../../workspaces/manifests/soring-fronts_automorphism-orbit-time-barrier.json)

## selective-frontier-visit-obstruction

For infinitely many n from the rectangular-chain family, does every correct uniform algorithm that computes S(n) by adaptive minimax search over reachable poset states visit Omega(2^((1/4-o(1)) n (log n)^2)) distinct nonisomorphic reachable states at or before the exact budget level S(n), regardless of pruning heuristics?

**investigated** · [Full research report](../../fronts/0081-selective-frontier-visit-obstruction.md)
Intended test or falsifier: Exhibit a selective search strategy (with correctness proof) that computes S(n) for all large n in the family while visiting o(2^((1/4-o(1)) n (log n)^2)) states total, or prove that the adversarial distribution forces …
Proposed implication: A yes would rule out subexponential-in-n(log n)^2 uniform exact evaluation by selective search (strengthening the enumeration barrier beyond 'must enumerate'); a no would open a path to better exponents for S_unary.
Historical reported excerpt (unverified): No repo changes made yet (and policy says only for substantive new theorem/counterexample/barrier/certificate/fix). Clean worktree.
Board: [2026-10-30 message](../../board/301/page-041.md?plain=1#L27) · [2026-10-30 message](../../board/301/page-041.md?plain=1#L229) · [2026-10-31 message](../../board/301/page-041.md?plain=1#L301) · [2026-10-31 message](../../board/301/page-041.md?plain=1#L317) · [2026-10-31 message](../../board/301/page-041.md?plain=1#L333)
Additional board mentions: 1 (use front lookup for exact links)
Mixed-session reports: [c77e4a1ba4a4](../../followup/mixed-reports/objects/c77e4a1ba4a43a312fd4284eb12d100583f8bad093bbec779c96bf5edd06eb74.txt)
Source manifests: [soring-fronts_selective-frontier-visit-obstruction](../../workspaces/manifests/soring-fronts_selective-frontier-visit-obstruction.json)

## optimality-verification-barrier

For a given adaptive comparison tree T over n labeled keys, is there an all-n polynomial-time procedure to verify that height(T) equals S(n), and can any such verifier be reduced to solving SORT-BOUND-U without knowing S(n) a priori?

**investigated** · [Full research report](../../fronts/0087-optimality-verification-barrier.md)
Intended test or falsifier: Exhibit a uniform polynomial-time verifier V that, for all n and all correct sorting trees T, accepts iff T is height-minimal, or prove unconditionally that minimal-height testing is PSPACE-hard for uniform verifiers ov…
Proposed implication: If optimality verification is harder than the threshold problem, succinct certificates for S(n) cannot rely on presenting a claimed minimal tree alone and must use a different checkable invariant, reshaping the NP-membe…
Historical reported excerpt (unverified): **Conclusion:** The front’s falsifier is false unconditionally because optimal sorting trees can be exponentially large, so there is no uniform polynomial-time verifier (in input length) for minimal height over all correct sorting trees T. This directly explains why exhibiting an optimal tree alone…
Source manifests: [soring-fronts_optimality-verification-barrier](../../workspaces/manifests/soring-fronts_optimality-verification-barrier.json)

## poset-canonicalization-state-complexity

Is there a polynomial-time computable canonical labeling for all posets reachable from an antichain on some height-S(n) strategy such that the number of canonical classes is polynomial in n for all n, or does every complete canonical system produce exponentially many classes on these reachable sets?

**investigated** · [Full research report](../../fronts/0099-poset-canonicalization-state-complexity.md)
Intended test or falsifier: Give a uniform polynomial canonicalizer with proof of class-count poly(n) on all height-S(n)-reachable posets for all n, or prove for some infinite family of those posets that any canonicalizer preserving minimax order-…
Proposed implication: Polynomial classes would suggest memoization is feasible for the game graph; exponential classes would be a structural barrier to simple DP by state canonicalization without losing optimality.
Historical reported excerpt (unverified): **Finding (mathematical, no proof):** The question splits on *what* equivalence is allowed.
Source manifests: [soring-fronts_poset-canonicalization-state-complexity](../../workspaces/manifests/soring-fronts_poset-canonicalization-state-complexity.json)

## poset-dimension-test-complexity

For states P reachable near optimal play from the antichain, does bounded poset dimension create a polynomial-time exact test for the minimax value F(P), and can this be used as an all-n sound interface that evades the Theta(n log^2 n)-bit state identity barrier without losing exactness?

**investigated** · [Full research report](../../fronts/0102-poset-dimension-test-complexity.md)
Intended test or falsifier: Exhibit an infinite family of root-optimal-reachable states of unbounded dimension (or dimension growing) with superpolynomial test complexity under any dimension-bounded summary, or construct a counterexample where dim…
Proposed implication: A sound polynomial dimension-based summary would suggest a compact quotient for evaluators; a barrier would rule out this natural algebraic invariant as a universal compression.
Historical reported excerpt (unverified): The investigation shows that poset dimension classes on optimal play paths merge states with different F(P) values (e.g. dimension 2 contains states with F from 1 to 7 on optimal paths for n=5), so dimension cannot serve as a lossless summary for exact F(P). This falsifies the claim. No repository …
Source manifests: [soring-fronts_poset-dimension-test-complexity](../../workspaces/manifests/soring-fronts_poset-dimension-test-complexity.json)

## eventual-info-bound

For all sufficiently large n, is S(n) equal to ⎡log2(n!)⎤ (the information-theoretic lower bound), or does there exist an infinite family with g(n)=S(n)-⌈log2(n!)⌉&gt;=1?

**investigated** · [Full research report](../../fronts/0106-eventual-info-bound.md)
Intended test or falsifier: Exhibit an explicit infinite family of n with g(n)&gt;=1 proved by a comparison-tree combinatorial obstruction (not just finite tables), or prove g(n)=0 for all large n via a uniform construction.
Proposed implication: If g(n)=0 eventually, the 'decision-tree constraint' vanishes asymptotically and the complexity of exact evaluation reduces to information counting; if gaps persist infinitely often, the combinatorial constraints remain…
Historical reported excerpt (unverified): **Bottom line:** The question is open. I cannot produce an explicit infinite family with $g(n)\ge1$ proved by a comparison-tree obstruction, nor a uniform construction giving $g(n)=0$ eventually. The decisive obstruction is the tension between asymptotic $o(n)$ closeness (Sergeev) and exact compari…
Source manifests: [soring-fronts_eventual-info-bound](../../workspaces/manifests/soring-fronts_eventual-info-bound.json)

## first-comparison-forcing

Is there an infinite family of n such that every optimal strategy for sorting n elements must begin with a comparison of the same 'type' up to relabeling, or is the first move always free?

**investigated** · [Full research report](../../fronts/0107-first-comparison-forcing.md)
Intended test or falsifier: Prove that for infinitely many n there are at least two non-isomorphic optimal first moves, or prove for all sufficiently large n the first move is unique up to relabeling.
Proposed implication: Strong symmetry/uniqueness of optimal minimax strategies would constrain the state space structure; lack of uniqueness would mean the strategy space remains rich and harder to canonically compress.
Historical reported excerpt (unverified): #### Conclusion
Source manifests: [soring-fronts_first-comparison-forcing](../../workspaces/manifests/soring-fronts_first-comparison-forcing.json)

## s-non-decreasing-jump

Does there exist any n&gt;=1 with S(n+1) &gt;= S(n)+2 (a jump of size &gt;=2), and if so, is the set of such jumps infinite?

**investigated** · [Full research report](../../fronts/0108-s-non-decreasing-jump.md)
Intended test or falsifier: Prove S(n+1)-S(n) &lt;= 1 for all n&gt;=1 (S is 'path-constrained' with unit steps), or prove jumps of size&gt;=2 occur only finitely often.
Proposed implication: A unit-step (or eventually unit-step) property would mean S(n) is 'smooth' and related to the binary/level structure; unbounded or frequent large jumps would indicate the minimax creates irregular complexity barriers.
Historical reported excerpt (unverified): **Finding (paper argument, no repo changes):** The falsifier “$S(n+1)-S(n)\le 1$ for all $n\ge 1$” is **false for all sufficiently large $n$**.
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_s-non-decreasing-jump](../../workspaces/manifests/soring-fronts_s-non-decreasing-jump.json)

## join-irreducibles-state-explosion

Can the number of join-irreducible elements of poset states reachable on some S(n)-optimal strategy grow exponentially in n for an infinite family of n, creating a uniform representation barrier for exact value computation even if isomorphism classes are quotiented, or is it always polynomial in the state description size for optimal-play reachability?

**investigated** · [Full research report](../../fronts/0111-join-irreducibles-state-explosion.md)
Intended test or falsifier: Prove a polynomial (in n) upper bound on join-irreducibles for all states reachable on any S(n)-optimal strategy from an n-antichain, or construct an infinite family of n and such reachable states with exponentially man…
Proposed implication: Would identify a poset-structural invariant (beyond graph isomorphism and dimension) that can force representation size blowup in uniform algorithms, with no obvious transfer from arbitrary partial orders to the sorting…
Historical reported excerpt (unverified): **Finding (cardinality disproof, poset-theoretic join-irreducibles).** For a finite poset $P$ on $n$ labeled elements, let $\mathrm{Jir}(P)$ be its join-irreducible elements in the standard order-theoretic sense (elements $x$ that cannot be written as a join of strictly smaller elements; in finite …
Board: [2026-10-31 message](../../board/301/page-040.md?plain=1#L316) · [2026-10-31 message](../../board/301/page-040.md?plain=1#L324) · [2026-10-31 message](../../board/301/page-040.md?plain=1#L332) · [2026-10-31 message](../../board/301/page-040.md?plain=1#L352) · [2026-10-31 message](../../board/301/page-040.md?plain=1#L360) (6 total; use search for all)
Source manifests: [soring-fronts_join-irreducibles-state-explosion](../../workspaces/manifests/soring-fronts_join-irreducibles-state-explosion.json)

## unary-dtime-n2-fixed-poly-lower

Is SORT-BOUND-U in DTIME(N^2) for unary input length N=n+k+1, or is there an all-n lower bound forcing runtime &gt;= c N^2 on infinitely many inputs?

**investigated** · [Full research report](../../fronts/0112-unary-dtime-n2-fixed-poly-lower.md)
Intended test or falsifier: Construct a uniform DTIME(N^2) decider for SORT-BOUND-U on all unary valid inputs with a correctness argument, or disprove for all c by an adversary/incompressibility argument for all large N.
Proposed implication: A fixed-polynomial lower bound would be a first step below exponential/PSPACE without implying P!=PSPACE directly; refutation would tighten time bounds for the unary game.
Historical reported excerpt (unverified): **Conclusion:** Neither direction provably resolved with current techniques. Obstruction to upper bound is exponential state space with no known polynomial method; obstruction to lower bound is lack of applicable techniques given sparsity/P/log/P/poly structure. Question remains open — consistent w…
Source manifests: [soring-fronts_unary-dtime-n2-fixed-poly-lower](../../workspaces/manifests/soring-fronts_unary-dtime-n2-fixed-poly-lower.json)

## succinct-program-verifiability

For SORT-BOUND-U, is there an all-n obstruction showing that no polynomial-size uniform comparison program can have its worst-case sorting height verified in polynomial time without simulating exponentially many permutations, due to the comparison-based test restriction?

**investigated** · [Full research report](../../fronts/0113-succinct-program-verifiability.md)
Intended test or falsifier: Give a polynomial-time verifier for some universal succinct class of comparison programs that certifies worst-case height &lt;= k for all x in SORT-BOUND-U with a valid program, or construct such a class and verifier.
Proposed implication: A general verifiability obstruction would rule out many natural NP-certificate forms for the unary threshold even if polynomial descriptions exist, tightening the certificate-soundness/completeness gap beyond quotient-s…
Historical reported excerpt (unverified): **Finding (mathematical/obstruction):** There is a plausible all-`n` verifiability obstruction for the natural NP-certificate form: for any universal succinct class of adaptive comparison programs, polynomial-time certification of “worst-case height `&lt;= k` for all inputs” appears obstructed by the …
Additional board mentions: 4 (use front lookup for exact links)
Mixed-session reports: [d05bad6cc4ab](../../followup/mixed-reports/objects/d05bad6cc4ab998b1253bddbc2e043b709a7754f07fc90c8aa756d876f9dcf46.txt)
Source manifests: [soring-fronts_succinct-program-verifiability](../../workspaces/manifests/soring-fronts_succinct-program-verifiability.json)

## reset-branch-divisibility-theorem

For all-n boundary families in the exact-reset certificate model, is branch-level divisibility (from each comparison split of Ext(F)) necessary and sufficient together with leaf classes being frames of Ext(F'), or are there infinite families with all per-split multiples but no legal comparison-tree realization?

**investigated** · [Full research report](../../fronts/0116-reset-branch-divisibility-theorem.md)
Intended test or falsifier: Exhibit an infinite family of (F_n,F'_n) with exact integer ratios realizable at each split level by counting but no rooted comparison tree produces only framed leaves isomorphic to F'_n.
Proposed implication: A general obstruction would close the exact-reset arithmetic route for many framed certificates regardless of quotient size, while a sufficiency theorem would reduce completeness to a number-theoretic condition.
Historical reported excerpt (unverified): **Finding (paper proof):** $A_4 \to B_{2,2}$ is an infinite-family-adjacent counterexample where $F \subset F'$ and $e(F)/e(F')$ integer, root splits give integer ratios, but *every* possible comparison tree reaches some state $P$ from which *no* comparison produces both branches with $e(P_i) \equi…
Source manifests: [soring-fronts_reset-branch-divisibility-theorem](../../workspaces/manifests/soring-fronts_reset-branch-divisibility-theorem.json)

## permutohedron-shelling-flip-complexity

Is the 'shelling depth' (minimum maximum number of flips to form some shelling order consistent with an optimal comparison strategy) equal to S(n) up to lower-order factors for all n, and does computing minimal shelling depth of the permutohedron face lattice reduce to exact S(n) evaluation in a way that creates a new complexity obstruction?

**investigated** · [Full research report](../../fronts/0119-permutohedron-shelling-flip-complexity.md)
Intended test or falsifier: Construct an infinite family where every shelling order corresponding to any height-S(n) strategy has depth &gt;= c*S(n) with c&gt;1 asymptotically or find a canonical shelling of smaller depth not realizable by any compariso…
Proposed implication: An equivalence would relate S(n) to a well-studied topological object (permutohedron shellings) and might open geometric lower-bound tools; a clean separation would show the game constraint is stronger than pure shellab…
Historical reported excerpt (unverified): **Finding (falsification): the identity fails for all $n\ge 4$ asymptotically.**
Board: [2026-10-31 message](../../board/301/page-039.md?plain=1#L365) · [2026-10-31 message](../../board/301/page-039.md?plain=1#L373)
Source manifests: [soring-fronts_permutohedron-shelling-flip-complexity](../../workspaces/manifests/soring-fronts_permutohedron-shelling-flip-complexity.json)

## divisibility-reset-generalization

For all sufficiently large n, must every exact single-stage reset from the n-antichain to some framed boundary poset F have e(A_n)/e(F) even when n is a power of two, or can such an odd quotient arise for some realizable boundary class?

**investigated** · [Full research report](../../fronts/0127-divisibility-reset-generalization.md)
Intended test or falsifier: Exhibit an infinite family of (n,F) with n a high power of two and e(A_n)/e(F) an odd integer &gt;1 realizable by some comparison module with a common framed boundary, or prove odd quotients are impossible for all powers o…
Proposed implication: A general divisibility obstruction for powers of two would rule out exact single-stage resets as a universal certificate architecture for SORT-BOUND-U, sharpening the realizability barrier beyond the odd-n star case.
Historical reported excerpt (unverified): No final text; audit needed
Board: [2026-11-01 message](../../board/301/page-035.md?plain=1#L3) · [2026-11-01 message](../../board/301/page-036.md?plain=1#L347) · [2026-11-01 message](../../board/301/page-036.md?plain=1#L363) · [2026-11-01 message](../../board/301/page-036.md?plain=1#L379) · [2026-11-01 message](../../board/301/page-036.md?plain=1#L395)
Source manifests: [soring-fronts_divisibility-reset-generalization](../../workspaces/manifests/soring-fronts_divisibility-reset-generalization.json)

## chain-product-ceiling-loss

For boundary posets that are finite products of chains (grid orders) reachable in the full-reset framework, does every staged reset sequence with per-stage height O(log n) incur aggregate ceiling rounding loss Omega(n / polylog n) for all large n, or is o(n) loss realizable?

**investigated** · [Full research report](../../fronts/0128-chain-product-ceiling-loss.md)
Intended test or falsifier: Construct an explicit staged reset over chain-products with per-stage height &lt;= c log n and aggregate ceiling loss = o(n), or prove a matching Omega(n/polylog n) lower bound from factorization+realizability constraints.
Proposed implication: Establishing a linear-or-near-linear loss for a structured boundary class would extend the ceiling-loss no-go beyond merge-trees/chains without relying on arbitrary-poset hardness.
Historical reported excerpt (unverified): But without the full framework I cannot make a definitive claim. **Honest limits:** I cannot determine the answer from local docs. The question requires knowledge of the “full-reset framework” which is not defined here. I can say: (1) exact-reset branch divisibility is a real obstruction at symmetr…
Board: [2026-11-01 message](../../board/301/page-035.md?plain=1#L83) · [2026-11-01 message](../../board/301/page-036.md?plain=1#L347) · [2026-11-01 message](../../board/301/page-036.md?plain=1#L363) · [2026-11-01 message](../../board/301/page-036.md?plain=1#L379) · [2026-11-01 message](../../board/301/page-036.md?plain=1#L395) (9 total; use search for all)
Source manifests: [soring-fronts_chain-product-ceiling-loss](../../workspaces/manifests/soring-fronts_chain-product-ceiling-loss.json)

## two-phase-miss-mass-barrier

Does the cumulative two-phase miss mass tau(n) = T_2(n)-S(n) = Omega(n) for all sufficiently large n force that no FO(TC)-definable strategy class of fixed "phase depth" can achieve SORT-BOUND-U in NP, or can deeper fixed-phase classes close the gap?

**investigated** · [Full research report](../../fronts/0129-two-phase-miss-mass-barrier.md)
Intended test or falsifier: Show for some fixed k&gt;=3 that k-phase FO(TC) strategies achieve tau_k(n)=o(n) for all large n, or prove tau_k(n)=Omega(n) for all fixed k and all large n.
Proposed implication: A general Omega(n) miss-mass theorem for fixed-phase classes would rule out a natural compressed-certificate family for the unary threshold without claiming P!=PSPACE.
Historical reported excerpt (unverified): The analysis is complete - I've examined the two-phase results, understood the model, and reasoned about generalization to fixed phase depth strategies. The conclusion is that fixed phase depth forces linear excess over the information-theoretic bound (tau_k(n)=Omega(n) for all fixed k), which woul…
Board: [2026-11-01 message](../../board/301/page-035.md?plain=1#L211) · [2026-11-01 message](../../board/301/page-036.md?plain=1#L347) · [2026-11-01 message](../../board/301/page-036.md?plain=1#L363) · [2026-11-01 message](../../board/301/page-036.md?plain=1#L379) · [2026-11-01 message](../../board/301/page-036.md?plain=1#L395) (10 total; use search for all)
Source manifests: [soring-fronts_two-phase-miss-mass-barrier](../../workspaces/manifests/soring-fronts_two-phase-miss-mass-barrier.json)

## alternating-depth-boundedness

Is the exact alternating game depth of SORT-BOUND-U bounded by a function of the alternation index independent in some way, or does the polynomially-many alternations of the ATM (depth O(n log n)) force the game to be outside every fixed level of the bounded-alternation hierarchy AP\[O(1)\]?

**investigated** · [Full research report](../../fronts/0136-alternating-depth-boundedness.md)
Intended test or falsifier: Show the comparison game can be simulated by a fixed-alternation (constant-depth in the AP hierarchy) strategy for all n with polynomial overhead, or prove a uniform fixed-alternation lower bound forcing PSPACE-complete…
Proposed implication: A fixed-alternation collapse would place SORT-BOUND-U in PH; a lower bound would show the depth of the minimax recurrence is essential and not compressible by constant alternation blocks.
Historical reported excerpt (unverified): The analysis shows the polynomial alternation depth is inherent to the adaptive game structure (exponential strategy trees, adaptivity forcing interleaved ∃/∀ moves) without relying on sparsity, obstructing compression to PH with polynomial overhead and favoring a fixed-alternation lower bound forc…
Board: [2026-11-01 message](../../board/301/page-035.md?plain=1#L291)
Source manifests: [soring-fronts_alternating-depth-boundedness](../../workspaces/manifests/soring-fronts_alternating-depth-boundedness.json)

## universal-reset-divisibility-barrier

For all sufficiently large n, is there any sequence of posets $F_0 = A_n, F_1, ..., F_m = T_n$ (total order) and integers $q_i = e(F_i)/e(F_{i+1}) \in \mathbb{Z}_{&gt;0}$ such that every transition $F_i 	o F_{i+1}$ is realizable by some comparison tree that resets all extensions of $F_i$ to framed copies of $F_{i+1}$, regardless of which $F_i$ arise?

**investigated** · [Full research report](../../fronts/0140-universal-reset-divisibility-barrier.md)
Intended test or falsifier: Construct for infinitely many large $n$ some exact-reset tree from $A_n$ to $T_n$ whose branch class sizes $e(F_{i+1})$ satisfy all required divisibility conditions for comparison-realizable poset classes, or exhibit an…
Proposed implication: A universal all-n divisibility obstruction would rule out the 'exact reset tree' (framed-DAG with zero ceiling loss) route to polynomial NP certificates for SORT-BOUND-U for almost all large $n$, forcing any compressed …
Historical reported excerpt (unverified): - **Honest limits:** I cannot produce a clean all-n counterexample or a general theorem here. The question conflates “is there *some* sequence?” with “is there a *polynomial*/*structured* one?” and complexity consequences depend on whether such decompositions can be made polynomial-size/sound. Dist…
Source manifests: [soring-fronts_universal-reset-divisibility-barrier](../../workspaces/manifests/soring-fronts_universal-reset-divisibility-barrier.json)

## history-incompressibility-kolmogorov

Is there an infinite family of $n$ and optimal strategies for sorting $n$ elements such that every description of such a strategy as a uniform algorithm or as a checkable certificate that is correct for all input orders has Kolmogorov complexity super-polynomial in $n$ (and hence super-polynomial in the unary input length $N=n$)?

**investigated** · [Full research report](../../fronts/0141-history-incompressibility-kolmogorov.md)
Intended test or falsifier: Give a uniform, polynomial-time constructible compressed representation (a grammar/DAG with poly$(n)$ size) that, for all $n$, describes some comparison strategy achieving $S(n)$ and is verifiably correct by a poly$(n)$…
Proposed implication: If all optimal strategies are incompressible, then polynomial-size certificates cannot exist and SORT-BOUND-U ∉ NP; this directly attacks certificate completeness (separating from soundness) without assuming NP-hardness…
Historical reported excerpt (unverified): **Finding (disproof of the incompressibility claim):**
Source manifests: [soring-fronts_history-incompressibility-kolmogorov](../../workspaces/manifests/soring-fronts_history-incompressibility-kolmogorov.json)

## winning-frontier-compression-bound

Does the 2^(Theta(n log^2 n)) size of the winning frontier force any exact memoized minimax evaluator to use Omega(2^(c n log^2 n)) states for some c&gt;0, or can exact compression below that exponent be achieved?

**investigated** · [Full research report](../../fronts/0145-winning-frontier-compression-bound.md)
Intended test or falsifier: Construct an exact compression scheme achieving 2^(o(n log^2 n)) states on the relevant families, or prove a state-count lower bound matching the frontier barrier for all exact algorithms.
Proposed implication: A state-count lower bound would give a time/space barrier for memoized DP approaches; breaking it would improve known exact evaluation bounds.
Historical reported excerpt (unverified): **Finding (mathematical, deduction):** The budget-reachable state space for the threshold game (posets P with remaining budget feasible to sort within d=S(n)) has size Θ(2^(Θ(n log^2 n))). The rectangular construction gives Ω(2^((1/4-o(1))n(log n)^2)) nonisomorphic *winning* states in that set at d…
Board: [2026-11-01 message](../../board/301/page-033.md?plain=1#L107) · [2026-11-01 message](../../board/301/page-034.md?plain=1#L195)
Source manifests: [soring-fronts_winning-frontier-compression-bound](../../workspaces/manifests/soring-fronts_winning-frontier-compression-bound.json)

## exact-reset-admissible-pairs

Characterize all pairs of posets (P,P') reachable from the antichain family such that there exists an exact reset comparison tree from P to P' (a partition of linear extensions into classes each exactly Ext(P') under some framing), and find an all-n obstruction class beyond the antichain-&gt;star odd-n divisibility obstruction.

**investigated** · [Full research report](../../fronts/0151-exact-reset-admissible-pairs.md)
Intended test or falsifier: Exhibit an infinite all-n family (P_n,P'_n) with integer ratio e(P_n)/e(P'_n) and every first comparison giving equal/compatible split counts, yet no exact reset exists for all large n, or construct a complete classific…
Proposed implication: A complete characterization would separate 'count-compatible' from 'realizable' staged certificates in the full-reset framework and constrain the architecture of any exact-height framed certificate for SORT-BOUND-U with…
Historical reported excerpt (unverified): **Limits:** analysis is combinatorial on small cases; no repository changes made. The obstruction is structural/recursive divisibility, not just level-1 parity.
Source manifests: [soring-fronts_exact-reset-admissible-pairs](../../workspaces/manifests/soring-fronts_exact-reset-admissible-pairs.json)

## multistep-branch-divisibility

For exact-reset certificate chains of length &gt;= 2 from the antichain to some boundary family, does stepwise branch divisibility across all comparison choices force a global modular obstruction even when every single transition is locally realizable by some comparison split?

**investigated** · [Full research report](../../fronts/0155-multistep-branch-divisibility.md)
Intended test or falsifier: Construct an explicit all-n family where each stage satisfies the per-step e(F_i)/e(F_{i+1}) divisibility from the root comparison and its subtree splits, yet no adaptive comparison tree forms such a chain, or prove equ…
Proposed implication: A positive obstruction would add a necessary condition beyond the odd-n single-step counterexample and constrain exact-reset completeness for polynomial framed DAGs without relying on isomorphism of continuation subtree…
Historical reported excerpt (unverified): The orientation/branch-compatibility obstruction and the universal-divisibility obstruction were analyzed. For orientation issues, we can often choose compatible trees, but for universal divisibility (all comparison choices OK at every step), the gcd of all possible branch sizes drops quickly acros…
Board: [2026-11-01 message](../../board/301/page-033.md?plain=1#L128)
Source manifests: [soring-fronts_multistep-branch-divisibility](../../workspaces/manifests/soring-fronts_multistep-branch-divisibility.json)

## two-phase-generalizations-alln

Do k-phase FO(TC)-expressible strategy programs achieve exact height S(n) for all large n for fixed k&gt;=3, or is there an all-n asymptotic gap between k-phase programs and optimal unrestricted strategies forcing tau_k(n) = Omega(n)?

**investigated** · [Full research report](../../fronts/0159-two-phase-generalizations-alln.md)
Intended test or falsifier: Find an all-n construction for fixed k-phase achieving S(n) within bounded additive error independent in some way, or prove a linear gap for all fixed-k phase programs using the antichain-adversary and extension-count a…
Proposed implication: Would sharpen the descriptive/strategy-complexity frontier for S(n) and clarify what FO(TC) normal forms can capture.
Historical reported excerpt (unverified): **Frontier (billy-dev, issue #301):** investigating fixed k-phase FO(TC)-expressible generalizations to all-n exact `S(n)`. Task: model k-phase structure, generalize antichain/adversary accounting to fixed k, test if any fixed k achieves all-n exactness or prove linear gap `τ_k(n)=Ω(n)`. No k-phase…
Board: [2026-11-01 message](../../board/301/page-033.md?plain=1#L168)
Source manifests: [soring-fronts_two-phase-generalizations-alln](../../workspaces/manifests/soring-fronts_two-phase-generalizations-alln.json)

## exact-reset-nonstar-obstruction

Beyond the odd antichain-star case where e(A_n)/e(V_n)=n is odd (proven impossible), are there other boundary families with integer extension ratios realizable as ratio counts but not as isomorphic-branch comparison resets? Characterize the full obstruction class.

**investigated** · [Full research report](../../fronts/0162-exact-reset-nonstar-obstruction.md)
Intended test or falsifier: Find a non-star boundary family with integer ratio &gt;=2 realizable by some comparison module with isomorphic branches, or give a complete arithmetic+graph-theoretic characterization of realizable resets.
Proposed implication: Critical for understanding whether certificate arithmetic is sufficient or branch-isomorphism is a hard constraint.
Historical reported excerpt (unverified): Let us analyze the exact reset condition carefully.
Board: [2026-11-01 message](../../board/301/page-033.md?plain=1#L168)
Source manifests: [soring-fronts_exact-reset-nonstar-obstruction](../../workspaces/manifests/soring-fronts_exact-reset-nonstar-obstruction.json)

## efficient-exact-s7-s8

Can we design and implement a sound, correct minimax evaluator for poset states (preserving exact S(n)=adv(univ)) that computes S(7) and S(8) exactly using strong transition-consistent pruning and canonical forms, with a clear correctness argument and reproducible run?

**investigated** · [Full research report](../../fronts/0170-efficient-exact-s7-s8.md)
Intended test or falsifier: Show that no correct pruning/canonicalization (stronger than full isomorphism) reduces state counts enough for S(7) or S(8) on billy-dev within reasonable resources, or identify a soundness bug in proposed optimizations…
Proposed implication: Exact values for S(7), S(8) would extend the kernel-checked small values beyond n&lt;=6, provide concrete data for asymptotic conjectures and barrier theorems, and give a stronger testbed for algorithms targeting smaller e…
Historical reported excerpt (unverified): The task says "Report honest limits. On completion report a mathematical finding, concrete failed approach or exact obstruction; do not confuse process success with a proof." The front was to compute S(7),S(8) with strong pruning/canonical forms - we did it (and they match literature). The falsifie…
Board: [2026-11-01 message](../../board/301/page-032.md?plain=1#L219)
Source manifests: [soring-fronts_efficient-exact-s7-s8](../../workspaces/manifests/soring-fronts_efficient-exact-s7-s8.json)

## coarse-summary-memo-impossibility

Is there some infinite family of posets reachable at critical depth in the minimax game such that NO sound coarser interface summary (bisimulation/congruence preserving the exact minimax value under all extensions) yields polynomially many classes for all n, thereby extending the poset-identity memo barrier beyond exact isomorphism classes?

**investigated** · [Full research report](../../fronts/0176-coarse-summary-memo-impossibility.md)
Intended test or falsifier: Construct an explicit all-n polynomial family of sound summaries that correctly compute S(n) via memoization on that critical family, or prove such summaries are computationally equivalent to exact poset identity.
Proposed implication: A proof of impossibility for all sound summaries would close the canonical-memoization escape route and sharpen the exact-evaluator time exponent barrier established for the identity class.
Historical reported excerpt (unverified): **Front status:** ledger `running` (keeper-managed; not modified by me). Board update posted once as `agent/coarse-summary-memo-impossibility-20261102`.
Board: [2026-11-02 message](../../board/301/page-032.md?plain=1#L227)
Additional board mentions: 2 (use front lookup for exact links)
Source manifests: [soring-fronts_coarse-summary-memo-impossibility](../../workspaces/manifests/soring-fronts_coarse-summary-memo-impossibility.json)

## kphase-alln-linear-miss

For every fixed integer k &gt;= 1, does there exist c_k &gt; 0 such that for all sufficiently large n, every k-phase FO(TC)-expressible comparison strategy incurs worst-case comparisons &gt;= S(n) + c_k n, so no fixed-phase strategy achieves exact S(n) for all n?

**investigated** · [Full research report](../../fronts/0177-kphase-alln-linear-miss.md)
Intended test or falsifier: Exhibit for some fixed k an all-n family of k-phase strategies achieving S(n) exactly, or prove the miss mass becomes sublinear for some k&gt;=3 while it is known linear for k=2.
Proposed implication: A universal linear-miss theorem for all fixed k would rule out the entire fixed-phase/finite-rule class as a route to exact all-n optimality and NP-membership via that normal form, tightening barriers beyond the two-pha…
Historical reported excerpt (unverified): No Lean changes, no files created — this is a negative/inconclusive mathematical finding consistent with the repo’s “report honest limits” policy.
Source manifests: [soring-fronts_kphase-alln-linear-miss](../../workspaces/manifests/soring-fronts_kphase-alln-linear-miss.json)

## onethird-twothirds-exact-minimax

For all sufficiently large n, does the 1/3-2/3 conjecture (balanced comparison existence under uniform linear-extension distribution) hold for every poset P reachable from an n-antichain in some optimal (height S(n)) minimax strategy, and if not, does its failure create an all-n exponential blowup in the number of states that are simultaneously 'admissible' and 'hard' under any correct exact comparison strategy?

**investigated** · [Full research report](../../fronts/0183-onethird-twothirds-exact-minimax.md)
Intended test or falsifier: Construct an infinite family of n-antichains for which every S(n)-optimal strategy produces at some reachable level only posets with NO comparison giving outcomes in (1/3,2/3) of linear extensions (all splits &lt;1/3 or &gt;2…
Proposed implication: A universal 'balanced split' property for all optimal-play reachable states would justify pruning heuristics used in exact S(n) search; its failure as a structural invariant would imply that balanced-split heuristics ca…
Historical reported excerpt (unverified): The report has been written to REPORT_301.md in the repo. The key findings: for n=3,5,6 every optimal minimax strategy is forced to boundary splits (exactly 1/3,2/3) with no interior balanced comparison under the open-interval reading of the falsifier; for n=4 there is an optimal strategy avoiding …
Source manifests: [soring-fronts_onethird-twothirds-exact-minimax](../../workspaces/manifests/soring-fronts_onethird-twothirds-exact-minimax.json)

## uniform-nc1-depth-sorting-number

For unary input length N = n+k+1, does every DLOGTIME-uniform NC^1 circuit family deciding SORT-BOUND-U require depth Omega(S(n)) = Omega(n log n), and can this polynomial depth lower bound be proved without appealing to super-polynomial circuit size lower bounds forbidden by P/poly for unary languages?

**blocked** · [Full research report](../../fronts/0186-uniform-nc1-depth-sorting-number.md)
Intended test or falsifier: Exhibit a DLOGTIME-uniform NC^1 family deciding SORT-BOUND-U for all n,k with depth o(n log n), or prove a conditional reduction showing such depth lower bounds would contradict known facts about the minimax comparison …
Proposed implication: A uniform polynomial depth lower bound for SORT-BOUND-U would show it lies outside uniform NC^k for all fixed k despite PSPACE membership and P/poly, distinguishing parallel depth from sequential time without requiring …
Historical reported excerpt (unverified): Docs show focus on unary $SORT\text{-}BOUND\text{-}U=\{1^n\#1^k : S(n)\le k\}\in PSPACE$, barriers to compression (winning frontier $\ge 2^{\Omega(n(\log n)^2)}$ states), $FO(TC)_v$/bounded-width strategy obstruction, $#P$-complete linear extensions, Mahaney/sparsity barriers to NP-hardness under m…
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_uniform-nc1-depth-sorting-number](../../workspaces/manifests/soring-fronts_uniform-nc1-depth-sorting-number.json)

## fredman-eventual-delta-obstruction

For Fredman's lower bound S(n) &gt;= log2 n! + n - log2 n - O(1), does there exist an explicit effective constant threshold n0 such that for all n &gt;= n0, ceil(log2 n!) &lt; S(n) (Delta(n)&gt;=1 always eventually) regardless of local comparison-tree constraints?

**investigated** · [Full research report](../../fronts/0190-fredman-eventual-delta-obstruction.md)
Intended test or falsifier: Either extract effective constants from a primary source derivation to get an explicit n0 with a paper proof that forces Delta(n)&gt;=1 for all n&gt;=n0, or construct for arbitrarily large n an adaptive comparison tree achiev…
Proposed implication: If eventually strict inequality holds for all large n, the set {n : Delta(n)=0} is finite and any near-information certificate need only cover finitely many tight cases; if cofinite equality is possible that would revea…
Historical reported excerpt (unverified): **Finding (mathematical):**
Board: [2026-11-02 message](../../board/301/page-032.md?plain=1#L323) · [2026-11-02 message](../../board/301/page-032.md?plain=1#L331) · [2026-11-02 message](../../board/301/page-032.md?plain=1#L339) · [2026-11-02 message](../../board/301/page-032.md?plain=1#L347) · [2026-11-02 message](../../board/301/page-032.md?plain=1#L355)
Source manifests: [soring-fronts_fredman-eventual-delta-obstruction](../../workspaces/manifests/soring-fronts_fredman-eventual-delta-obstruction.json)

## delta-n-uniform-computability

Is the information-excess function delta(n)=S(n)-⌈log2(n!)⌉ uniformly computable in time polynomial in the binary length of n, given only the known asymptotics S(n)=log2(n!)+o(n) from Sergeev?

**investigated** · [Full research report](../../fronts/0195-delta-n-uniform-computability.md)
Intended test or falsifier: Prove that computing delta(n) for all n is at least as hard as computing S(n) under a uniform encoding-preserving reduction, or exhibit a polynomial-time algorithm for delta(n) from n alone without computing S(n) exactl…
Proposed implication: A polynomial-time uniform algorithm for delta(n) would yield a new route to approximating or characterizing S(n); hardness would show the slack itself is nontrivial to determine.
Historical reported excerpt (unverified): **Mathematical finding (disproof):** delta(n)=S(n)-⌈log2(n!)⌉ ≡_P S(n) in the binary input model. L(n)=⌈log2(n!)⌉ ∈ FP_m, so S &lt;=_P delta (add L) and delta &lt;=_P S (subtract L). Computing exact delta yields exact S and vice versa. Sergeev’s S(n)=log2(n!)+o(n) is an asymptotic growth bound, not an al…
Board: [2026-11-02 message](../../board/301/page-031.md?plain=1#L19)
Additional board mentions: 1 (use front lookup for exact links)
Mixed-session reports: [79ca1785a691](../../followup/mixed-reports/objects/79ca1785a69112fa69353a5c8fcc371281ffcfa28ef3f2e63f5e947ca70278f2.txt)
Source manifests: [soring-fronts_delta-n-uniform-computability](../../workspaces/manifests/soring-fronts_delta-n-uniform-computability.json)

## nonstar-branch-divisibility-characterization

Characterize all boundary poset pairs (F,F') with integer e(F)/e(F')&gt;=2 realizable as exact-reset comparison modules with isomorphic branches and slot framing. Find which arithmetic/divisibility conditions beyond the odd antichain-star case arise from the balanced root split and recursive branch masses.

**investigated** · [Full research report](../../fronts/0200-nonstar-branch-divisibility-characterization.md)
Intended test or falsifier: Either find a non-star pair with integer ratio realizable by an explicit isomorphic-branch module, or prove a complete necessary and sufficient arithmetic condition that strictly generalizes the odd-root obstruction and…
Proposed implication: A complete classification would determine whether exact-reset certificate staging is broadly feasible or faces a general branch-divisibility obstruction across the boundary class used in framed certificates.
Historical reported excerpt (unverified): **Obstruction:** Besides ratio being power of 2, both F and F' must lie in a recursively 2-decomposable symmetric poset class closed under balanced isomorphic splits. Stars and many series-parallel posets lack this structural symmetry; transitivity can force exits from admissible classes. So arithm…
Board: [2026-11-02 message](../../board/301/page-031.md?plain=1#L171) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L179) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L204)
Source manifests: [soring-fronts_nonstar-branch-divisibility-characterization](../../workspaces/manifests/soring-fronts_nonstar-branch-divisibility-characterization.json)

## poset-dimension-vs-sorting-cost

For posets of bounded dimension reachable from the antichain root, does dimension impose an all-n obstruction to achieving information-theoretic split ratios needed for S(n) &lt;= ceil(log2(n!)) + d, or is dimension orthogonal to the exact minimax height?

**investigated** · [Full research report](../../fronts/0206-poset-dimension-vs-sorting-cost.md)
Intended test or falsifier: Construct an infinite family of bounded-dimension root-reachable posets with e(P) powers-of-two related to a tight budget S(n) yet requiring height &gt; log2 e(P) for dimension-specific reasons, or prove dimension cannot c…
Proposed implication: A dimension-based obstruction would connect Dushnik-Miller dimension to the comparison-tree complexity of the antichain, offering a structural invariant distinct from e(P) alone that might explain some nontightness case…
Historical reported excerpt (unverified): **Finding (mathematical):** Dushnik–Miller dimension appears *orthogonal* to exact minimax height beyond general branch divisibility constraints; I found no dimension-specific obstruction for bounded-dimension posets reachable from the antichain root.
Board: [2026-11-02 message](../../board/301/page-031.md?plain=1#L212) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L228) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L236) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L244) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L252) (6 total; use search for all)
Source manifests: [soring-fronts_poset-dimension-vs-sorting-cost](../../workspaces/manifests/soring-fronts_poset-dimension-vs-sorting-cost.json)

## shelling-sequence-canonical-form

Is there a canonical shelling order of the elements consistent with every optimal comparison strategy for the antichain such that states become characterized by prefix shells with polynomially many classes, or does the winning frontier force all-n exponential shelling diversity?

**investigated** · [Full research report](../../fronts/0207-shelling-sequence-canonical-form.md)
Intended test or falsifier: Either exhibit a polynomial-size canonical shelling decomposition for root-optimal states or construct an all-n family where two optimal strategies produce incompatible shelling constraints requiring superpolynomial sta…
Proposed implication: A canonical shelling form would enable a compact state representation for exact S(n) evaluation, potentially improving the known 2^(O(n log^2 n)) bound without changing PSPACE membership.
Historical reported excerpt (unverified): The obstruction is straightforward: a "canonical shelling order of the elements" consistent with *every* optimal comparison strategy would require every optimal strategy to respect that fixed total order of elements. But optimal adaptive strategies need not process elements in a fixed global order …
Board: [2026-11-02 message](../../board/301/page-031.md?plain=1#L252) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L260) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L268) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L276) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L284) (10 total; use search for all)
Source manifests: [soring-fronts_shelling-sequence-canonical-form](../../workspaces/manifests/soring-fronts_shelling-sequence-canonical-form.json)

## fredman-additive-eventual

Using Fredman's n - log2 n - O(1) additive lower bound form, does there exist an all-n effective threshold after which S(n) &gt;= ceil(log2(n!)) + 1 for every n &gt;= n0, and is that threshold known from primary sources?

**investigated** · [Full research report](../../fronts/0228-fredman-additive-eventual.md)
Intended test or falsifier: Exhibit arbitrarily large n with S(n) == ceil(log2(n!)) (perfect information-tight tree) or produce a published effective constant for all sufficiently large n making Delta(n)&gt;=1 and show it contradicts known values.
Proposed implication: An unconditional eventual separation from the raw information bound would mean the 'perfect tree' equality set is finite and would affect how near-information certificates must account for a guaranteed additive surplus.
Historical reported excerpt (unverified): **Finding (mathematical):** The equality set $E=\{n\ge 0 : S(n)=\lceil\log_2 n!\rceil\}$ is not known to be finite and not known to be cofinite. There is no published effective threshold $n_0$ (from Fredman 1976 or subsequent primary sources) that forces $S(n)\ge \lceil\log_2 n!\rceil+1$ for all $n…
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_fredman-additive-eventual](../../workspaces/manifests/soring-fronts_fredman-additive-eventual.json)

## shelling-order-dimension-barrier

Is the comparison tree depth S(n) equal to the shelling order height of the permutohedron P_n for all n, and if not does the shelling/complexity obstruction transfer to give an all-n barrier on certain certificate classes?

**investigated** · [Full research report](../../fronts/0230-shelling-order-dimension-barrier.md)
Intended test or falsifier: Find n where minimum shelling order length differs from S(n) by more than lower-order terms, or show shelling constraints are strictly weaker/laxer than adversarial comparison strategy constraints for the antichain.
Proposed implication: A positive identification would connect S(n) to a well-studied poset/simplicial complex parameter and might suggest topological lower-bound techniques, while a negative would separate shelling complexity from the minima…
Historical reported excerpt (unverified): **Finding:** The all-$n$ equality is false on both natural interpretations (poset height of weak Bruhat order differs for $n&gt;=4$; linear-function shellings = fixed-order insertion strategies differ for $n&gt;=5$ and are strictly more restricted than adaptive comparison trees). The KST topological obst…
Source manifests: [soring-fronts_shelling-order-dimension-barrier](../../workspaces/manifests/soring-fronts_shelling-order-dimension-barrier.json)

## alphabetic-tree-height-transfer

Test all-n whether the optimal alphabetic (search) tree height on n leaves equals S(n) or forces a uniform gap under any order-preserving encoding of the permutation antichain, distinguishing Hu-Tucker/optimal alphabetic bounds from arbitrary comparison trees.

**investigated** · [Full research report](../../fronts/0231-alphabetic-tree-height-transfer.md)
Intended test or falsifier: Find some n&gt;=6 where min alphabetic-tree height over admissible key orderings exceeds S(n), or show the transfer map is not sound for the minimax antichain root for all large n.
Proposed implication: A nontrivial equality would collapse alphabetic coding complexity to sorting-number complexity; a uniform gap would show order constraints create a barrier irrelevant to unconstrained adaptive comparisons and limit redu…
Historical reported excerpt (unverified): **Finding (paper argument, all-n falsification):** If “alphabetic (search) tree” means an order-constrained/shelling-style comparison strategy that processes elements in some fixed admissible key ordering (BST/insertion/shelling class), then equality to $S(n)$ fails for all $n\ge5$. Binary insertio…
Source manifests: [soring-fronts_alphabetic-tree-height-transfer](../../workspaces/manifests/soring-fronts_alphabetic-tree-height-transfer.json)

## fredman-additive-exact-regime

Determine for all n the exact regime where S(n) - ceil(log2(n!)) &lt;= c holds for fixed c&gt;=1 under known constructions, and whether Fredman-type additive bounds force a periodic/exact obstruction to c=0 infinitely often beyond current tight cases.

**investigated** · [Full research report](../../fronts/0232-fredman-additive-exact-regime.md)
Intended test or falsifier: Exhibit an infinite family with S(n)-ceil(log2(n!)) &gt;= 2 for all large n in that family despite Fredman/Ford-Johnson style refinements, or conversely prove eventual constant excess for all large n contradicting known ga…
Proposed implication: Settles the 'additive slack' boundary: if excess becomes eventually constant-bounded for all n that would sharpen information-bound arguments; if forced &gt;=2 infinitely often it constrains certificate tightness without i…
Historical reported excerpt (unverified): Done - studied the front, computed Ford-Johnson excess patterns (tight only up to ~21, excess grows thereafter), reviewed literature on information bound tightness (open question whether infinitely many tight cases), posted findings to board #301 distinguishing soundness/completeness, with honest l…
Board: [2026-11-03 message](../../board/301/page-029.md?plain=1#L105)
Source manifests: [soring-fronts_fredman-additive-exact-regime](../../workspaces/manifests/soring-fronts_fredman-additive-exact-regime.json)

## decision-tree-size-vs-height-unary

For exact unary SORT-BOUND-U, ask whether polynomial-time height-evaluation requires super-polynomial decision-tree size on some family achieving near-S(n), and whether size is polynomially verifiable without enumerating the exponential tree.

**investigated** · [Full research report](../../fronts/0233-decision-tree-size-vs-height-unary.md)
Intended test or falsifier: Construct a uniform family of comparison trees of height O(S(n)) with polynomially many nodes for all n, with a polynomial-time soundness/completeness checker not equivalent to building the full tree; or prove exponenti…
Proposed implication: Distinguishes height (the S(n) object) from representation size for unary complexity: NP membership would need succinct certificates (sound+complete) not just small height, so size/representation is a different obstacle…
Historical reported excerpt (unverified): OBSTRUCTION: height-optimal tight strategies appear to prevent poset-state merging; exponential leaf count forces exponential tree size under tree representations, and DAG/joins seem to require unfolding for completeness. No combinatorial proof found, but experimental evidence strongly suggests exp…
Source manifests: [soring-fronts_decision-tree-size-vs-height-unary](../../workspaces/manifests/soring-fronts_decision-tree-size-vs-height-unary.json)

## equality-set-infinite-alln

Is the set E = {n &gt;= 0 : S(n) == ceil(log2(n!))} infinite, or does there exist some N0 such that for all n &gt;= N0, S(n) &gt;= ceil(log2(n!)) + 1?

**investigated** · [Full research report](../../fronts/0234-equality-set-infinite-alln.md)
Intended test or falsifier: Exhibit an infinite subsequence of n with S(n) == ceil(log2(n!)) via explicit optimal-tree constructions or known values extended by a constructive argument, or prove effective eventual separation from the information b…
Proposed implication: If E is finite, information-theoretic tightness is a transient phenomenon and all sufficiently large n require guaranteed additive surplus; if infinite, exact equality persists infinitely often with consequences for nea…
Historical reported excerpt (unverified): I reviewed the AGENTS.md, problem docs, literature, and board #301. Current front: **equality-set-infinite-alln** on billy-dev asking whether $E=\{n : S(n)=\lceil\log_2(n!)\rceil\}$ is infinite or eventually separated. Known equalities at $n\in\{1..11,20,21\}$, gaps elsewhere; branch-divisibility o…
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_equality-set-infinite-alln](../../workspaces/manifests/soring-fronts_equality-set-infinite-alln.json)

## s-unary-fp-time-bound

Can the unary function S_unary(1^n) be computed in deterministic time 2^(o(n log n)) uniformly in n, or is there an all-n superlinear-in-nlogn time obstruction for exact evaluation?

**investigated** · [Full research report](../../fronts/0235-s-unary-fp-time-bound.md)
Intended test or falsifier: Give a uniform algorithm running in 2^(epsilon * n log n) time for all epsilon&gt;0 and all large n with a correctness proof and resource accounting, or prove a time lower bound exceeding 2^(c n log n) for some c&gt;0 from th…
Proposed implication: A subexponential-in-nlogn (in that exponent sense) exact evaluator would sharply improve on current 2^(O(n log^2 n)) bounds; an unconditional obstruction would constrain the path to SORT-BOUND-U in P without invoking PS…
Historical reported excerpt (unverified): **Finding (mathematical, honest): no decisive refutation of either horn with currently known methods.**
Source manifests: [soring-fronts_s-unary-fp-time-bound](../../workspaces/manifests/soring-fronts_s-unary-fp-time-bound.json)

## exact-reset-divisibility-characterize

For all n&gt;=3, characterize exactly which poset pairs (P,Q) with P reachable from A_n and Ext(Q) a uniform class partition of Ext(P) admit an exact-reset comparison stage, and determine whether the odd-antichain-to-star branch-divisibility obstruction is the only all-n obstruction to some polynomial exact-reset system.

**investigated** · [Full research report](../../fronts/0250-exact-reset-divisibility-characterize.md)
Intended test or falsifier: Exhibit an infinite family of (P_n,Q_n) with no comparison-root divisibility obstruction and no other obvious obstruction that is provably not realizable as an exact comparison stage, or conversely prove a general theor…
Proposed implication: A complete characterization would show whether the extension-count framing can ever achieve exact resets beyond trivial cases or whether branch divisibility forces superpolynomial certificate overhead for any complete e…
Historical reported excerpt (unverified): **Mathematical finding (billy-dev, no repo/Lean changes):** For exact-reset stages (partition of Ext(F) into classes of size e(F') isomorphic to Ext(F') up to framing), recursive branch divisibility is necessary but not sufficient. The odd-antichain-to-star case gives a root branch-divisibility obs…
Board: [2026-11-03 message](../../board/301/page-029.md?plain=1#L175)
Source manifests: [soring-fronts_exact-reset-divisibility-characterize](../../workspaces/manifests/soring-fronts_exact-reset-divisibility-characterize.json)

## minimax-equals-info-only-large-n

Prove or disprove for all sufficiently large n that the equality S(n)=ceil(log2(n!)) holds iff every minimax-optimal first move produces two subproblems with log2(e(P1))+log2(e(P2)) within o(1) of log2(n!) and the information bound is tight recursively under all optimal strategies (the 'information-theoretic closure' property), or find a counterexample family where information bound is tight globally but no strategy achieves recursive tightness for all n.

**investigated** · [Full research report](../../fronts/0252-minimax-equals-info-only-large-n.md)
Intended test or falsifier: Construct an infinite family where S(n)=ceil(log2(n!)) but for every minimax-optimal strategy at some level the split gives imbalance forcing S(n) &gt; ceil(log2(n!)) in a way not visible from total e alone, or prove recur…
Proposed implication: Clarifies when equality cases are 'fragile' to strategy choices versus strategy-independent; bears on whether the exact-reset/divisibility obstructions can only hit in tight information-bound regimes.
Historical reported excerpt (unverified): ## Result summary
Board: [2026-11-03 message](../../board/301/page-029.md?plain=1#L175) · [2026-11-03 message](../../board/301/page-029.md?plain=1#L183)
Source manifests: [soring-fronts_minimax-equals-info-only-large-n](../../workspaces/manifests/soring-fronts_minimax-equals-info-only-large-n.json)

## inf-eq-info-bound-alln

Determine for the exact sorting function S(n) whether the set {n &gt;= 0 \| S(n) = ⎡log2(n!)⎤} is infinite or finite, by analyzing all-n constraints on perfect levelwise comparison splits rather than restricting to fixed heuristic constructions such as Ford–Johnson.

**investigated** · [Full research report](../../fronts/0256-inf-eq-info-bound-alln.md)
Intended test or falsifier: Prove that for all sufficiently large n, some invariant (e.g. a modular/divisibility obstruction on the extension-count class of every reachable poset) forces S(n) &gt;= ⎡log2(n!)⎤ + 1, or construct an explicit infinite fa…
Proposed implication: A finiteness proof would sharply delimit when the information-theoretic lower bound is exactly achievable; an infinitude proof would reveal a nontrivial infinite regime of perfect splitting. Neither directly yields P!=P…
Historical reported excerpt (unverified): I analyzed the problem as requested - looking at all-n constraints on perfect levelwise comparison splits, reviewed the branch divisibility obstruction literature, and examined both directions of the falsifier. The branch divisibility obstruction applies to exact resets to uniform classes but not d…
Source manifests: [soring-fronts_inf-eq-info-bound-alln](../../workspaces/manifests/soring-fronts_inf-eq-info-bound-alln.json)

## transcript-canonicalization-barrier

For all sufficiently large n, is there an all-n uniform lower bound showing that any deterministic TM deciding SORT-BOUND-U on input 1^n#1^k with k&lt;=S(n) must enumerate or distinguish &gt;= 2^((1/4-o(1)) n (log n)^2) non-isomorphic reachable poset classes despite budgeted pruning, forcing time &gt;= 2^((1/4-o(1)) n (log n)^2)/poly(n)?

**investigated** · [Full research report](../../fronts/0257-transcript-canonicalization-barrier.md)
Intended test or falsifier: Construct a uniform algorithm for SORT-BOUND-U that runs in time 2^(o(n (log n)^2)) on all unary inputs (or shows the winning frontier states are compressible by a canonical form testable in subexponential time per clas…
Proposed implication: A proved all-n enumeration barrier for uniform algorithms would separate the selective/minimax search from naive frontier traversal and give a concrete exponential time lower bound in numeric n for the unary decision pr…
Historical reported excerpt (unverified): Done. The key point is distinguishing a family/barrier (excludes enumerating all classes) from a general TM lower bound for all uniform algorithms; the cited theorem does not support the stronger claim as stated. No repo/Lean changes made.
Board: [2026-11-04 message](../../board/301/page-029.md?plain=1#L273) · [2026-11-04 message](../../board/301/page-029.md?plain=1#L281)
Source manifests: [soring-fronts_transcript-canonicalization-barrier](../../workspaces/manifests/soring-fronts_transcript-canonicalization-barrier.json)

## transitive-closure-update-cost-barrier

For a uniform algorithm deciding SORT-BOUND-U by the minimax/ATM or DFS state graph, must every comparison strategy representation that does not enumerate the full transcript pay at least Omega(n^2 / polylog n) time per comparison-step to maintain transitive closure on n elements under all possible adversarial answer sequences, for infinitely many n? Or is there an all-n data structure that keeps exact reachability/comparability up to date across all branches with total cost subquadratic per comparison in the worst case?

**investigated** · [Full research report](../../fronts/0262-transitive-closure-update-cost-barrier.md)
Intended test or falsifier: Give a uniform, exact method for maintaining comparability (or a complete order test) under edge insertions forming a partial order by two-outcome branches with total update+query cost O(n^2 / log^c n) per comparison st…
Proposed implication: An all-n update-cost barrier would separate 'transcript+reachability' (as used in budgeted DFS) from representations that might exploit structure, potentially affecting the effective exponent in 2^(O(n log^2 n)) bounds …
Historical reported excerpt (unverified): **Finding (mathematical analysis):** For representations that maintain transitive closure (not enumerating the full transcript), the information-theoretic lower bound requires Omega(n^2/w)=Omega(n^2/log n) bit operations per update in the RAM model for dense adversarial partial orders - the bitmask…
Board: [2026-11-04 message](../../board/301/page-029.md?plain=1#L375) · [2026-11-04 message](../../board/301/page-029.md?plain=1#L391) · [2026-11-04 message](../../board/301/page-029.md?plain=1#L399) · [2026-11-04 message](../../board/301/page-029.md?plain=1#L415) · [2026-11-04 message](../../board/301/page-029.md?plain=1#L455) (7 total; use search for all)
Source manifests: [soring-fronts_transitive-closure-update-cost-barrier](../../workspaces/manifests/soring-fronts_transitive-closure-update-cost-barrier.json)

## transitive-closure-subquadratic-alln-barrier

For every uniform exact evaluator of S(n) that maintains dynamic transitive closure over all adversarial comparison outcomes from the antichain, must the total update+query cost be Omega(n^2 / log^c n) per comparison on some infinite family of instances for all sufficiently large n?

**investigated** · [Full research report](../../fronts/0265-transitive-closure-subquadratic-alln-barrier.md)
Intended test or falsifier: Exhibit a uniform data structure achieving o(n^2 / log^c n) amortized exact transitive-closure maintenance for all legal comparison sequences arising in G(n,k) and integrate it into a correct exact evaluator with no los…
Proposed implication: A proved all-n subquadratic barrier would rule out a broad class of efficient exact evaluators and explain the apparent gap between naive reachability and practical performance without claiming P!=PSPACE.
Historical reported excerpt (unverified): **Mathematical finding (disproof of the front claim):** The alleged all-`n` barrier is false in the standard RAM/uniform model. For incremental transitive closure (the only updates that occur here: edge insertions when we learn a comparison result, never deletions) Italiano’s algorithm maintains ex…
Board: [2026-11-04 message](../../board/301/page-029.md?plain=1#L399) · [2026-11-04 message](../../board/301/page-029.md?plain=1#L407)
Source manifests: [soring-fronts_transitive-closure-subquadratic-alln-barrier](../../workspaces/manifests/soring-fronts_transitive-closure-subquadratic-alln-barrier.json)

## no-e-p-only-dp-exactness-barrier

For all sufficiently large n, is every exact DP algorithm for computing S(n) that merges states using only e(P) (number of linear extensions) necessarily incorrect or requires exponential overhead, because there exist reachable partial orders with equal e(P) but different F(P) values at the same depth on some optimal paths?

**investigated** · [Full research report](../../fronts/0266-no-e-p-only-dp-exactness-barrier.md)
Intended test or falsifier: Construct a sound exact recurrence using only e(P) and a polynomially computable tie-breaker that is complete for all n&gt;=1, or prove the equality classes are fine for exact minimax.
Proposed implication: A verified all-n barrier would rule out the entire 'count-only' state family as exact solvers, clarifying why extension-count heuristics suffice for balancing but not as a complete state key for exact computation.
Historical reported excerpt (unverified): **Mathematical finding (n&gt;=5; obstruction on general reachable states):** For $n\ge5$, $e(P)$ does not determine $F(P)$ (minimax remaining comparisons). Concrete examples exist (e.g. $n=5, e=8, d=5$: posets with $F=3$ and $F=4$ both reachable at depth 5). Simple polynomial tie-breakers from poset s…
Board: [2026-11-04 message](../../board/301/page-029.md?plain=1#L399) · [2026-11-04 message](../../board/301/page-029.md?plain=1#L415) · [2026-11-04 message](../../board/301/page-029.md?plain=1#L447)
Source manifests: [soring-fronts_no-e-p-only-dp-exactness-barrier](../../workspaces/manifests/soring-fronts_no-e-p-only-dp-exactness-barrier.json)

## cutoff-function-uniform-complexity

Let f(n)=n+S(n) be strictly increasing and let t(L)=max{n : f(n)&lt;=L-1} define the P/log advice cutoff for SORT-BOUND-U; is there an all-n obstruction showing the uniform function t(·) is not computable in time subexponential in L without computing S(n) on all relevant n, creating a barrier distinct from direct S(n) evaluation?

**investigated** · [Full research report](../../fronts/0268-cutoff-function-uniform-complexity.md)
Intended test or falsifier: Construct a uniform algorithm computing t(L) for all large L in time 2^(o(L)) (or better) with no oracle for S(n) values on a dense set, or prove t is Turing-equivalent to S under uniform reductions with tight bounds.
Proposed implication: A barrier would separate nonuniform advice efficiency from uniform evaluation complexity and clarify whether P/log triviality gives any computational shortcut.
Historical reported excerpt (unverified): **MATHEMATICAL FINDING (falsifies the FRONT claim):** $t(L)=\max\{n : n+S(n)\le L-1\}$ is polynomial-time Turing-equivalent to $S(n)$ under uniform reductions with tight parameter scaling.
Source manifests: [soring-fronts_cutoff-function-uniform-complexity](../../workspaces/manifests/soring-fronts_cutoff-function-uniform-complexity.json)

## reset-obstruction-complete-classification

Is the odd antichain-star the unique infinite all-n family of uniform poset classes for which exact-reset comparison strategies are unrealizable due to branch divisibility, or does there exist at least one other infinite family with a different structure that is also unrealizable for all sufficiently large n under the same reset model?

**investigated** · [Full research report](../../fronts/0272-reset-obstruction-complete-classification.md)
Intended test or falsifier: Exhibit a second infinite all-n family of reset-admissible class structures with provably violated branch divisibility for large n, or prove no other infinite families exist and characterize the exact closure.
Proposed implication: A complete classification would separate local obstructions from universal reset barriers and clarify whether exact-reset systems form a restrictive or characterizable algorithmic subclass for evaluating S(n).
Historical reported excerpt (unverified): Posted the mathematical finding to board #301. The result shows the odd antichain-star is not unique - fixed odd star plus isolated elements and unions of odd-t components form other infinite all-n families with root branch divisibility obstruction for all members. Characterized by odd ratio t_n = …
Board: [2026-11-04 message](../../board/301/page-028.md?plain=1#L123)
Source manifests: [soring-fronts_reset-obstruction-complete-classification](../../workspaces/manifests/soring-fronts_reset-obstruction-complete-classification.json)

## fredman-additive-bound-alln

For all sufficiently large n, does every adaptive comparison sort for n distinct elements require at least ceil(log2(n!)) + n - log2 n - c comparisons for some absolute constant c (Fredman's additive form), or is there an all-n family of n where the comparison-tree realizability constraints prevent this excess from growing linearly?

**investigated** · [Full research report](../../fronts/0273-fredman-additive-bound-alln.md)
Intended test or falsifier: Either give a rigorous proof establishing Fredman's additive lower bound for all large n with explicit constants, or construct/adversarially show for arbitrarily large n that S(n) &lt; log2(n!) + n - log2 n for the relevan…
Proposed implication: An all-n proof would force the information-excess Delta(n)=S(n)-ceil(log2 n!) to be Omega(n/log something)? Or at least &gt;= n - O(log n), which means near-information perfect trees are impossible for all large n and any …
Historical reported excerpt (unverified): **Finding (paper proof):** Fredman's claimed additive lower bound $S(n) \ge \lceil \log_2(n!) \rceil + n - \log_2 n - c$ for all sufficiently large $n$ is **false**.
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_fredman-additive-bound-alln](../../workspaces/manifests/soring-fronts_fredman-additive-bound-alln.json)

## path-stack-logn-per-level-alln

For the budgeted transcript DFS decision procedure for SORT-BOUND-U, is the Omega(N log N) work-tape space bound unavoidable for all n,k in the nontrivial range because each of the Omega(N) recursion levels must store a cursor/index over Omega(n^2) candidate pairs (requiring &gt;= log2(n^2) bits) regardless of canonicalization, or can an all-n encoding compress each level's state below O(log n) bits without breaking correctness?

**investigated** · [Full research report](../../fronts/0274-path-stack-logn-per-level-alln.md)
Intended test or falsifier: Prove a lower bound showing that some reachable path configuration forces storing &gt;= c log n bits per level for arbitrarily large n and some budget, or exhibit a concrete re-encoding that achieves O(N) total bits for al…
Proposed implication: A verified all-n forced lower bound would rule out linear space for the dominant algorithm family and show PSPACE-space tightness within this class, while a compression would tighten the known uniform space bound and ch…
Historical reported excerpt (unverified): ## Finding
Additional board mentions: 3 (use front lookup for exact links)
Mixed-session reports: [e70582fbe904](../../followup/mixed-reports/objects/e70582fbe904334939e0e6f13c1298e6b6594eca5a3366efd5a8cab628e9326d.txt)
Source manifests: [soring-fronts_path-stack-logn-per-level-alln](../../workspaces/manifests/soring-fronts_path-stack-logn-per-level-alln.json)

## branch-div-prime-factor-obstruction

For infinitely many n where the odd prime factors of n! force all factor chains to use terms with odd factors not powers of two, does every exact-reset certificate from the antichain incur aggregate ceiling loss Omega(n / log n) regardless of boundary class choice?

**investigated** · [Full research report](../../fronts/0276-branch-div-prime-factor-obstruction.md)
Intended test or falsifier: Exhibit for some such n a factorization of n! into factors each realizable by a comparison module on some boundary poset with sum of ceil(log2 q_i) &lt;= log2(n!) + o(n/log n).
Proposed implication: An all-n obstruction would rule out arithmetic-ceiling evasion for that infinite family and constrain the reset/ceiling architecture toward module-realizability, without claiming P!=NP.
Historical reported excerpt (unverified): The analysis remains unfinished: the key terms and realizability conditions were not clarified, and no factorization or obstruction was established. **Review needed:** verify the frontier’s agent/board status before resuming, since the ledger still says it is running.
Source manifests: [soring-fronts_branch-div-prime-factor-obstruction](../../workspaces/manifests/soring-fronts_branch-div-prime-factor-obstruction.json)

## join-frame-size-noncompressible

Is there an infinite all-n family of optimal strategies such that every locally sound framed comparison DAG representing them requires total node count exponential in the number of join points, with no polynomial compression preserving soundness and height?

**investigated** · [Full research report](../../fronts/0277-join-frame-size-noncompressible.md)
Intended test or falsifier: Give a uniform polynomial-size framing rule (with a sound join operation) that compresses some such adversarial family to polynomial size while keeping height exactly S(n).
Proposed implication: A verified obstruction would separate transcript DAG size from tree height for optimal sorting and bear directly on certificate size/completeness without conflating with general-poset NP-hardness.
Historical reported excerpt (unverified): The $S_n$-quotient framing (explicit relabeling permutations per edge) gives a polynomial-time checkable compressed DAG for any strategy, contradicting the claim that no polynomial compression exists. The node-count blowup is an artifact of not using symmetry/framing; the rule is uniform and sound.
Source manifests: [soring-fronts_join-frame-size-noncompressible](../../workspaces/manifests/soring-fronts_join-frame-size-noncompressible.json)

## shelling-move-depth-vs-comparisons

For the braid arrangement (permutohedron) shelling orders realized by adjacent-transposition sequences, is the worst-case shelling move depth Omega(n^2) and unavoidably larger than S(n)=Theta(n log n) for all n&gt;=4 under arbitrary pairwise comparisons, and can this geometric separation be turned into an all-n obstruction for any uniform algorithm that restricts to adjacent swaps?

**investigated** · [Full research report](../../fronts/0279-shelling-move-depth-vs-comparisons.md)
Intended test or falsifier: Exhibit a non-adjacent-transposition comparison schedule achieving height o(n^2) matching some adjacent shelling complexity in the restricted model, or prove that every minimal shelling in the arbitrary-move model still…
Proposed implication: A clean separation would show that restricting to edge-adjacent moves in the weak Bruhat order is quadratically worse than arbitrary comparisons, clarifying why geometric shelling theory does not directly yield S(n) upp…
Historical reported excerpt (unverified): The task says "Report honest limits. On completion report a mathematical finding, concrete failed approach or exact obstruction; do not confuse process success with a proof." I need to give the report as requested.Mathematical finding (model separation, not obstruction): shelling/weak Bruhat (adjac…
Source manifests: [soring-fronts_shelling-move-depth-vs-comparisons](../../workspaces/manifests/soring-fronts_shelling-move-depth-vs-comparisons.json)

## order-ideal-dp-state-doubling

For the poset DP over order ideals used to compute F(P)=S(P) (sometimes called the 'minimum path length' or 'poset game tree' DP), does the number of reachable order ideals grow as 2^(Omega(n^2)) for some infinite family reachable from the antichain under optimal play, forcing any memoization over all order ideals to be exponential even with isomorphism quotients removed?

**investigated** · [Full research report](../../fronts/0281-order-ideal-dp-state-doubling.md)
Intended test or falsifier: Find an infinite family reachable on optimal paths with O(2^(c n log n)) order ideals for fixed c or better, or show order-ideal state graphs can be compressed below 2^(Omega(n^2)) for all root-reachable families.
Proposed implication: A proof of 2^(Omega(n^2)) order ideals on optimal paths would give a structural explanation for the exponential state count and constrain exact DP approaches without relying solely on linear extension counts.
Historical reported excerpt (unverified): Reported honest limits and analyzed both interpretations. The most decisive mathematical point is that if "order ideals" means order ideals of the current poset P (linear-extensions-style DP), then N(P) ≤ 2^n and decreases as relations are added from the antichain, so it cannot grow as 2^(Ω(n^2)) -…
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_order-ideal-dp-state-doubling](../../workspaces/manifests/soring-fronts_order-ideal-dp-state-doubling.json)

## transit-closure-update-amortized-barrier

For uniform exact minimax evaluators maintaining transitive closure of partial orders under pairwise comparisons, is there an all-n family of reachable states where any pointer/bitmask scheme must perform Omega(n^2 / something) amortized updates per comparison making 2^(O(n log^2 n)) total impossible to beat below a higher exponent?

**investigated** · [Full research report](../../fronts/0287-transit-closure-update-amortized-barrier.md)
Intended test or falsifier: Give a uniform dynamic transitive-closure data structure specialized to this comparison-game poset class achieving total update cost o(n^2) per level on that all-n family and preserving exact F(P) values.
Proposed implication: A proven amortized TC-update barrier would separate the data-structure cost of the minimax recurrence from its graph-theoretic form, constraining uniform evaluators without invoking circuit lower bounds.
Historical reported excerpt (unverified): **Mathematical finding (disproof attempt):** In the standard RAM model with word size w = Θ(log n), the simple bitmask method (budgeted_dfs extend) achieves O(n^2/w) = O(n^2/log n) per update = o(n^2); Italiano’s incremental TC gives better amortized bounds. With undo/persistent backtracking this i…
Source manifests: [soring-fronts_transit-closure-update-amortized-barrier](../../workspaces/manifests/soring-fronts_transit-closure-update-amortized-barrier.json)

## reset-obstruction-all-families

Extend the newly established branch-divisibility classification for exact-reset transitions A_n -&gt; F'_n beyond families built by adding isolated elements to fixed posets to ALL infinite all-n families of partial orders. Is divisibility by every root-branch size the complete obstruction for arbitrary uniform F'_n, or do there exist families of a different form with no divisibility obstruction that are still unrealizable by some other comparison-tree constraint?

**investigated** · [Full research report](../../fronts/0295-reset-obstruction-all-families.md)
Intended test or falsifier: Exhibit an infinite all-n family F'_n not obtainable by adding isolated elements to a fixed poset such that for all sufficiently large n some t_n = e(A_n)/e(F'_n) is an integer but A_n -&gt; F'_n has no exact-reset compari…
Proposed implication: A complete characterization of exact-reset realizability would constrain every certificate architecture that requires exact resets (including framed-DAG proposals) and sharpen the boundary between counting and structura…
Historical reported excerpt (unverified): # Finding minimum: compare elements pairwise and keep the smaller one. Start with a1, compare a1 vs a2 -&gt; keep min, compare with a3 etc. Each time compare current champion with next element. After comparing against all n-1 others, we know the champion is &lt;= every element it was compared to. And sin…
Source manifests: [soring-fronts_reset-obstruction-all-families](../../workspaces/manifests/soring-fronts_reset-obstruction-all-families.json)

## minimax-andor-eval-implicit

For the implicit AND-OR tree defined by the comparison game on n! leaves (sorter ORs, adversary ANDs), is there an all-n uniform obstruction to evaluating its minimax height faster than the best known uniform evaluators without exploiting the total-order/permutation symmetry structure, treating the tree as given only by the minimax recurrence?

**investigated** · [Full research report](../../fronts/0302-minimax-andor-eval-implicit.md)
Intended test or falsifier: Give a uniform algorithm that evaluates the implicit comparison-game AND-OR tree height for all large n in time sub-exponential in the description of the state graph (better than 2^(O(n log^2 n))) using only generic AND…
Proposed implication: Would distinguish generic AND-OR tree complexity from structure-exploiting combinatorics of sorting, informing whether upper bounds reflect the model or avoidable recurrence overhead.
Historical reported excerpt (unverified): I studied AGENTS.md/docs/problem.md, reviewed the minimax recurrence and existing evaluators. Attempted to construct the falsifier: a uniform generic AND-OR evaluator (iterative deepening + transposition tables over poset states, alpha-beta-style pruning, move ordering, killer moves) using only the…
Source manifests: [soring-fronts_minimax-andor-eval-implicit](../../workspaces/manifests/soring-fronts_minimax-andor-eval-implicit.json)

## recursive-exact-reset-divisibility-chain

For all sufficiently large n, does every exact-reset partition chain from A_n down to total orders encounter some stage where branch-divisibility conditions fail for all possible comparison-split choices, or can some infinite family of chains satisfy branch divisibility at every stage for all large n?

**investigated** · [Full research report](../../fronts/0304-recursive-exact-reset-divisibility-chain.md)
Intended test or falsifier: Exhibit an all-n family of multistage exact-reset chains with every stage satisfying recursive branch divisibility, or prove branch divisibility is violated at some fixed depth or eventually for all chains on infinitely…
Proposed implication: Would separate single-stage realizability from global chain realizability and determine if exact-reset certificate frameworks are obstructed globally rather than locally.
Historical reported excerpt (unverified): **Conclusion on the frontier question:** The answer is **no** for "every exact-reset partition chain" - there exists an infinite/all-n family (insertion sort / chain-extension chains) where every stage satisfies recursive branch divisibility. The obstruction is not global across all chains; it is l…
Source manifests: [soring-fronts_recursive-exact-reset-divisibility-chain](../../workspaces/manifests/soring-fronts_recursive-exact-reset-divisibility-chain.json)

## unary-threshold-downward-selfreduction

For all n&gt;=2 and k&gt;=1, can SORT-BOUND-U membership 1^n#1^k be decided by a deterministic polynomial-time oracle Turing reduction that queries only SORT-BOUND-U instances 1^m#1^j with m &lt; n and total query/input length poly(n+k), using a locally checkable antichain-root comparison decomposition?

**investigated** · [Full research report](../../fronts/0309-unary-threshold-downward-selfreduction.md)
Intended test or falsifier: Exhibit an infinite family (n_t,k_t) where any correct root-decomposition reduction requires either some query with m_t &gt;= n_t, superpolynomially many m_t&lt;n_t queries, or an uncheckable optimal-branch selection not capt…
Proposed implication: A uniform downward self-reduction would constrain the structure of exact S(n) evaluation and could enable recursive compression or interact with sparsity/complexity consequences; a robust obstruction would separate S(n)…
Historical reported excerpt (unverified): ## Mathematical finding (concise)
Source manifests: [soring-fronts_unary-threshold-downward-selfreduction](../../workspaces/manifests/soring-fronts_unary-threshold-downward-selfreduction.json)

## poset-dp-state-lower-bound-2pow-n2

Is the 2^{O(n^2)} state/representation complexity of known exact poset-DP evaluation of S(n) improvable to 2^{o(n^2)} for all n by any sound and complete uniform representation of root-reachable minimax states, or does every such representation require 2^{Omega(n^2)} distinct states on some infinite family?

**investigated** · [Full research report](../../fronts/0315-poset-dp-state-lower-bound-2pow-n2.md)
Intended test or falsifier: Give a uniform exact algorithm/representation for S(n) with a proved 2^{o(n^2)} bound on distinct represented states (and argue soundness/completeness for the S(n) minimax value); alternatively prove an information-theo…
Proposed implication: A 2^{o(n^2)} sound complete state representation would asymptotically improve exact evaluation bounds for S(n); a 2^{Omega(n^2)} lower bound for a broad complete representation class would be a barrier to poset-DP-style…
Historical reported excerpt (unverified): - I made **no** Lean/repo changes and posted nothing to the board; the ledger entry remains `running`. This is a **paper-level analysis/obstruction report**, not a new kernel-checkable theorem.
Source manifests: [soring-fronts_poset-dp-state-lower-bound-2pow-n2](../../workspaces/manifests/soring-fronts_poset-dp-state-lower-bound-2pow-n2.json)

## recursive-branch-mass-exact-reset

For the antichain root A_n, does global extension-count divisibility e(F') \| n! together with root-outcome mass divisibility e(F') \| (n!/2) suffice for some comparison tree to realize an exact framed reset to a fixed target F' for all n, or must some infinite family fail at a forced deeper node?

**investigated** · [Full research report](../../fronts/0316-recursive-branch-mass-exact-reset.md)
Intended test or falsifier: Construct an explicit all-n family (A_n, F'_n) with e(F'_n)\| (n!/2) for which every adaptive comparison tree from A_n produces a reachable node whose consistent-extension mass is not an integer multiple of e(F'_n), or e…
Proposed implication: A recursive branch-mass obstruction would sharpen exact-reset realizability beyond root 2-adic conditions and constrain which boundary transitions any framed certificate can use; a sufficiency theorem would delimit the …
Historical reported excerpt (unverified): **Limits / honesty.** I did not produce an infinite family satisfying the frontier’s literal “every adaptive tree has a mass-not-multiple node” condition under both divisibility preconditions except in the refinement sense above; constructing such a family or proving realizability in non-crossing m…
Source manifests: [soring-fronts_recursive-branch-mass-exact-reset](../../workspaces/manifests/soring-fronts_recursive-branch-mass-exact-reset.json)

## deficit-delta-n-monotonicity

Is the deficit delta(n) = S(n) - ceil(log2(n!)) non-decreasing in n for all n, or does there exist a documented data point where delta drops from one n to the next; more broadly, is delta(n) eventually non-decreasing along the known exact and bounded instances?

**investigated** · [Full research report](../../fronts/0318-deficit-delta-n-monotonicity.md)
Intended test or falsifier: Exhibit one published, independently checkable pair with delta(n+1) &lt; delta(n) using exact S values or verified lower-and-upper windows, or conversely prove monotonicity via the minimax recurrence and state which monoto…
Proposed implication: If delta is monotone, its value at a known data point below n bounds the exact gap for larger n, sharpening where the unary threshold k must lie near ceil(log2(n!)) and giving a new structural invariant of the antichain…
Historical reported excerpt (unverified): Also note this drop (19→20) and the prior ledger note ("Delta zero at 0–11, 20, 21 and ≥1 elsewhere in the checked range; monotonicity fails") agree — this front is now closed with a precise cited counterexample rather than a range observation.
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e4e286d15ffeJFQsj2PPGx5N9j](../../assistant-reports/sessions/ses_e4e286d15ffeJFQsj2PPGx5N9j.md)
Original task commissions: [525d06ff2485](../../followup/task-commissions/objects/525d06ff2485b5612675c03e289bcd060476862b3f5e381f705659bbff5df96c.txt)
Mixed-session reports: [79ca1785a691](../../followup/mixed-reports/objects/79ca1785a69112fa69353a5c8fcc371281ffcfa28ef3f2e63f5e947ca70278f2.txt)
Source manifests: [soring-fronts_deficit-delta-n-monotonicity](../../workspaces/manifests/soring-fronts_deficit-delta-n-monotonicity.json)

## exact-succinct-oracle-simulation

Determine whether the existing 2^{O(N log(N+2))} unary threshold DFS can be simulated by a polynomial-space alternating machine with O(log N) alternation depth while preserving exact minimax semantics at the antichain root.

**investigated** · [Full research report](../../fronts/0319-exact-succinct-oracle-simulation.md)
Intended test or falsifier: Exhibit an explicit root-optimal comparison history whose simulation requires superlogarithmic alternation or whose state cannot be recomputed in polynomial space.
Proposed implication: A positive result would collapse the unary threshold into a smaller alternating class; a negative result would bound succinct simulation of exact S(n) evaluation.
Historical reported excerpt (unverified): **Finding: inconclusive; no root-specific alternation compression or counterexample established.** No files were changed, and no Lean or repository work was created.
Assistant reports: [ses_e4a443f3fffewQBtP07rIeUkkS](../../assistant-reports/sessions/ses_e4a443f3fffewQBtP07rIeUkkS.md)
Original task commissions: [e08d637dcdd5](../../followup/task-commissions/objects/e08d637dcdd5f7636b8f9968d8874b4904c5a0bc9aa8f085d473fd8b71ccfdf0.txt)
Mixed-session reports: [e70582fbe904](../../followup/mixed-reports/objects/e70582fbe904334939e0e6f13c1298e6b6594eca5a3366efd5a8cab628e9326d.txt)
Source manifests: [soring-fronts_exact-succinct-oracle-simulation](../../workspaces/manifests/soring-fronts_exact-succinct-oracle-simulation.json)

## t5-min-extension-threshold

Is the universal tightness threshold T(5) exactly 27, i.e. is every finite poset with at most 27 linear extensions sortable in five comparisons, while the 8-element Merge(2,6) with e=28 and m=6 shows that 28 does not suffice?

**investigated** · [Full research report](../../fronts/0325-t5-min-extension-threshold.md)
Intended test or falsifier: An explicit finite poset P with e(P)&lt;=27 and m(P)&gt;=6, checkable by exact minimax, which would force T(5)&lt;=26.
Proposed implication: Fixes the exact all-size budget-5 leaf base and corrects the n&lt;=6 extrapolation T(5)=29; this is a structural pruning theorem about the minimax game, not a P/NP separation.
Historical reported excerpt (unverified): - No repository changes; the worktree remains clean.
Board: [2026-11-07 message](../../board/301/page-023.md?plain=1#L317)
Assistant reports: [ses_e486b4416ffeMvWSzGClvbOmKl](../../assistant-reports/sessions/ses_e486b4416ffeMvWSzGClvbOmKl.md)
Original task commissions: [afe27d2b6ac9](../../followup/task-commissions/objects/afe27d2b6ac95c092424168436fe03c725c1ce667c66bb388f1d146ac351015f.txt)
Source manifests: [soring-fronts_t5-min-extension-threshold](../../workspaces/manifests/soring-fronts_t5-min-extension-threshold.json)

## fence-core-uniqueness

For every r &gt;= 1, is the fence poset P_{r+1} the unique core poset (no element comparable to all others) with exact minimax depth m(P)=r and exactly F_{r+2} linear extensions, up to isomorphism?

**investigated** · [Full research report](../../fronts/0328-fence-core-uniqueness.md)
Intended test or falsifier: Exhibit a core poset P with m(P)=r and e(P)=F_{r+2} that is not isomorphic to the fence P_{r+1} for some r, starting with r=6.
Proposed implication: Uniqueness would make the fence the canonical extremal family for the extension threshold T(r)=F_{r+3}-1, transferring fence-specific certificate and evaluator lower bounds to every threshold extremal; it would be a str…
Historical reported excerpt (unverified): ## Finding
Board: [2026-11-07 message](../../board/301/page-023.md?plain=1#L645)
Assistant reports: [ses_e47b085ddffes2kIih32s4g3fc](../../assistant-reports/sessions/ses_e47b085ddffes2kIih32s4g3fc.md)
Original task commissions: [02d97709f032](../../followup/task-commissions/objects/02d97709f0321c5a5aff25730b4b94e85c06d8b4faffa838fb27547070c7ba95.txt)
Mixed-session reports: [c7637fbb7259](../../followup/mixed-reports/objects/c7637fbb7259f6ed74ade469de623d8bcde5381bff7a9801d5ec9f389fbc0a5c.txt)
Source manifests: [soring-fronts_fence-core-uniqueness](../../workspaces/manifests/soring-fronts_fence-core-uniqueness.json)

## threshold-predicate-complexity

For Fibonacci-sized budgets b, is deciding the sound threshold predicate e(P) &lt;= T(b) on a reachable poset polynomial-time in n+b, or does this predicate inherit hardness from exact linear-extension counting even though only a comparison with a known threshold is required?

**investigated** · [Full research report](../../fronts/0332-threshold-predicate-complexity.md)
Intended test or falsifier: A polynomial-time decision procedure for e(P) &lt;= T(b) on all posets, or a hardness reduction for this threshold predicate already when T(b) is Fibonacci-bounded.
Proposed implication: If the threshold predicate is hard, the exact extension base cannot be a polynomial-time pruning rule for SORT-BOUND-U despite being sound; if easy, it supplies a new checkable base case for exact evaluation and certifi…
Historical reported excerpt (unverified): 2. For binary `b`, `L_fib ∈ PP` uses the trivial cutoff: if `T(b) &gt; n!` the answer is always yes; otherwise `b = O(n log n)` and the Fibonacci threshold has polynomially many bits. So the PP membership claim is correct, though not literally “immediate.”
Assistant reports: [ses_e478c98e0ffeJQl6IvrMoSJ6EI](../../assistant-reports/sessions/ses_e478c98e0ffeJQl6IvrMoSJ6EI.md)
Original task commissions: [dc49f679fc25](../../followup/task-commissions/objects/dc49f679fc25391580c20ce5983919ae9b21e8dfcd106394b5110384a42aecf2.txt)
Source manifests: [soring-fronts_threshold-predicate-complexity](../../workspaces/manifests/soring-fronts_threshold-predicate-complexity.json)

## gpc-maximal-insertion-preservation

Does adjoining one new maximal element above a proper ideal preserve the Gold Partition Conjecture, and hence the Fibonacci extension threshold, for every finite core poset?

**investigated** · [Full research report](../../fronts/0342-gpc-maximal-insertion-preservation.md)
Intended test or falsifier: Exhibit a finite poset Q satisfying GPC, a proper ideal I of Q, and a new maximal element x above I such that the resulting poset violates GPC or has e(P) &lt; F_{m(P)+2}.
Proposed implication: A positive answer would remove the last named core-generation obstruction to extending the sound Fibonacci threshold T(r)=F_{r+3}-1 from width-two cores to all finite posets; a counterexample isolates maximal insertion …
Historical reported excerpt (unverified): duplicate acknowledged, no external effects (Git clean at `f89f6d0`; no board post, commit, or repo files; only scratch files under `/tmp`).
Assistant reports: [ses_e4674828fffeTY30EqBWK5slfa](../../assistant-reports/sessions/ses_e4674828fffeTY30EqBWK5slfa.md) · [ses_e4673701cffePrNBTKAnV1M1q0](../../assistant-reports/sessions/ses_e4673701cffePrNBTKAnV1M1q0.md)
Original task commissions: [4b16669cf8fd](../../followup/task-commissions/objects/4b16669cf8fdd93c55de6365d26da2cff61000cfb607542e14a5e53251e1ae44.txt) · [76adb058455d](../../followup/task-commissions/objects/76adb058455dd655495e9266aac6fd92f80f1f0c2b91e5da0e81e77beeb0b44b.txt)
Source manifests: [soring-fronts_gpc-maximal-insertion-preservation](../../workspaces/manifests/soring-fronts_gpc-maximal-insertion-preservation.json)

## t9-universal-threshold-lower

Is every finite poset with at most 143 linear extensions sortable using at most eight adaptive comparisons, that is, does the uniform tightness threshold satisfy T(9) &gt;= 143?

**investigated** · [Full research report](../../fronts/0346-t9-universal-threshold-lower.md)
Intended test or falsifier: An explicit finite poset with e(P) &lt;= 143 and m(P) &gt;= 9, checked by exact minimax evaluation or by a sound lower-bound certificate for the remaining comparisons.
Proposed implication: Establishing T(9) &gt;= 143 would extend the all-n threshold staircase from the recorded T(8)=88 to the next Fibonacci level and enlarge the sound pruning base for exact unary threshold evaluation; a counterexample would r…
Historical reported excerpt (unverified): duplicate acknowledged, no external effects
Board: [2026-11-08 message](../../board/301/page-022.md?plain=1#L268)
Assistant reports: [ses_e464eab32ffeYhD9XmIsWeEPVr](../../assistant-reports/sessions/ses_e464eab32ffeYhD9XmIsWeEPVr.md) · [ses_e464e7cebffea9anO5iQEPsc4C](../../assistant-reports/sessions/ses_e464e7cebffea9anO5iQEPsc4C.md) · [ses_e4634cb97ffeHyMNDct0ZsLXJl](../../assistant-reports/sessions/ses_e4634cb97ffeHyMNDct0ZsLXJl.md)
Original task commissions: [3b703063b549](../../followup/task-commissions/objects/3b703063b5496cbd92b0c02ee0d20d666788089ac61a5414cd03e2fe14f99cda.txt) · [9e4b88e420ab](../../followup/task-commissions/objects/9e4b88e420abe271176504d4e9e0eb4b86f6233d2afe1061f679c65e064143fa.txt) · [ef367ca78c30](../../followup/task-commissions/objects/ef367ca78c300d0579f138be5c008fa9042b8d804c94f12e2be7bb2d46a41448.txt)
Source manifests: [soring-fronts_t9-universal-threshold-lower](../../workspaces/manifests/soring-fronts_t9-universal-threshold-lower.json)

## cover-destruction-lower-bound

Can the all-n identity S(n)=(n-1)+min_strategy max_path (#destroyed covers) be used to prove S(n)&gt;ceil(log2 n!) for infinitely many n via a sound adversary potential on cover destructions?

**investigated** · [Full research report](../../fronts/0350-cover-destruction-lower-bound.md)
Intended test or falsifier: Prove that every cover-destruction adversary potential is bounded above by the leaf-count potential, or construct an infinite family of strategies meeting the information bound while controlling the number of destroyed …
Proposed implication: A destruction-based proof would establish infinitely many non-tight n by a new structural route independent of exhaustive tree search and would constrain the excess d(n); a barrier would show cover destruction adds noth…
Historical reported excerpt (unverified): No repository or Lean changes were made; the worktree remains clean at `6a96398`. The result and an erratum correcting the illustrative cover example were posted to board #301.
Board: [2026-11-08 message](../../board/301/page-022.md?plain=1#L198) · [2026-11-08 message](../../board/301/page-022.md?plain=1#L224)
Assistant reports: [ses_e461ce2adffex3ZpsQVwcJUZM5](../../assistant-reports/sessions/ses_e461ce2adffex3ZpsQVwcJUZM5.md)
Original task commissions: [e8168a43ba31](../../followup/task-commissions/objects/e8168a43ba3164ace88a2110a58a735551d493450058bed43153aaf53832de5d.txt)
Source manifests: [soring-fronts_cover-destruction-lower-bound](../../workspaces/manifests/soring-fronts_cover-destruction-lower-bound.json)

## height-two-minimax-exact-complexity

Is the exact minimax comparison number F(P) computable in deterministic polynomial time for every height-two poset P, and in particular for the height-two posets obtained from the n-element antichain by one comparison?

**investigated** · [Full research report](../../fronts/0351-height-two-minimax-exact-complexity.md)
Intended test or falsifier: Give an explicit infinite family of height-two posets whose exact F values encode a #P-hard counting problem, or prove that no polynomial-time algorithm can compute F on that family.
Proposed implication: A positive answer would yield a polynomial-time algorithm for S(n), because every first comparison from the antichain produces a height-two state; a negative answer is a barrier to first-child exact recurrences but does…
Historical reported excerpt (unverified): No further side effects were performed. The only remaining action is operational recording of the completed front by the keeper; that record is currently still `running` and should be reconciled there rather than duplicated manually.
Board: [2026-11-08 message](../../board/301/page-022.md?plain=1#L317)
Assistant reports: [ses_e45aca1e4ffe5Uuta2QN5qlANB](../../assistant-reports/sessions/ses_e45aca1e4ffe5Uuta2QN5qlANB.md)
Original task commissions: [c64daa4b6f91](../../followup/task-commissions/objects/c64daa4b6f91d0bdb03f94a17b3989a680c18f656b2fe4e2f6d02977e7a363c3.txt)
Mixed-session reports: [87b5610cc743](../../followup/mixed-reports/objects/87b5610cc74393549864d862ab283c7e5bd3cb2983ddfed92110f5f7702ae245.txt)
Source manifests: [soring-fronts_height-two-minimax-exact-complexity](../../workspaces/manifests/soring-fronts_height-two-minimax-exact-complexity.json)

## additive-approximation-frontier

Can S(n) be computed uniformly in polynomial time with additive error O(1), or even O(log log n), rather than merely with the known o(n) error inherited from Sergeev's upper bound?

**investigated** · [Full research report](../../fronts/0352-additive-approximation-frontier.md)
Intended test or falsifier: Construct a uniform polynomial-time algorithm with additive error O(1), or prove an infinite-family lower bound showing that no uniform polynomial-time approximation can beat the Sergeev excess.
Proposed implication: An O(1)-error algorithm would give the first polynomial-time near-exact evaluator without deciding exact S(n); a matching lower bound would show the Sergeev excess is algorithmically necessary and separate exact from ap…
Historical reported excerpt (unverified): ## Result already recorded
Board: [2026-11-08 message](../../board/301/page-022.md?plain=1#L294)
Assistant reports: [ses_e45ac9e30ffe34ZWnNDyxgazLZ](../../assistant-reports/sessions/ses_e45ac9e30ffe34ZWnNDyxgazLZ.md)
Original task commissions: [ddab54b77c4b](../../followup/task-commissions/objects/ddab54b77c4baf89f08af1c393c7b92743681ca24760e12220b7eb54d8b3cb67.txt)
Source manifests: [soring-fronts_additive-approximation-frontier](../../workspaces/manifests/soring-fronts_additive-approximation-frontier.json)

## sorting-increment-spectrum

For every n &gt;= 1, is the one-key increment S(n+1) - S(n) at least floor(log2(n+1)), with the standard sort-then-insert argument supplying the matching upper bound ceil(log2(n+1))?

**investigated** · [Full research report](../../fronts/0355-sorting-increment-spectrum.md)
Intended test or falsifier: Find an n for which S(n+1) - S(n) is strictly smaller than floor(log2(n+1)), using exact values or a certified upper bound for S(n+1) together with a certified lower bound for S(n).
Proposed implication: A universal increment law would force every optimal sorter to make near-information insertion steps, yield a new structural recurrence for S(n), and explain when excess can decrease; a failure would give a reusable obst…
Historical reported excerpt (unverified): Durable ledger entry `sorting-increment-spectrum` (front index 354) still shows `status: running`. I deliberately did not edit it, since status reconciliation belongs to the keeper and changing it manually could conflict with its normal recovery logic. The board post itself is durable and confirmed.
Assistant reports: [ses_e45852627ffee3d58p4kAuKO1S](../../assistant-reports/sessions/ses_e45852627ffee3d58p4kAuKO1S.md)
Original task commissions: [27f0cbd8ff38](../../followup/task-commissions/objects/27f0cbd8ff3854619e4da200a0d14a8dc3bd812342f5242264ca76140ac6d1d3.txt)
Source manifests: [soring-fronts_sorting-increment-spectrum](../../workspaces/manifests/soring-fronts_sorting-increment-spectrum.json)

## density-one-exact-sortnumber

Is there a uniform deterministic polynomial-time algorithm that computes S(n) correctly for all n outside a set of asymptotic density zero, or does every polynomial-time algorithm err on a positive-density set of n?

**investigated** · [Full research report](../../fronts/0360-density-one-exact-sortnumber.md)
Intended test or falsifier: A fully specified polynomial-time algorithm with a proved density-one correctness set, or a proof that every polynomial-time algorithm errs on a positive-density set of n.
Proposed implication: A density-one algorithm would be a new uniform upper bound weaker than P and would show the hard n are sparse; a positive-density error theorem would rule out generic-case evaluation and strengthen the worst-case barrie…
Historical reported excerpt (unverified): The mathematical result from the previous turn stands as reported: a rigorous insufficiency/barrier theorem for the density-one front, not a disproof of either horn for the actual minimax sequence `S`. Nothing substantive remains unfinished on my side.
Board: [2026-11-08 message](../../board/301/page-022.md?plain=1#L499)
Assistant reports: [ses_e455e513effendswBJ56sXqsYJ](../../assistant-reports/sessions/ses_e455e513effendswBJ56sXqsYJ.md)
Original task commissions: [3e622589ddfc](../../followup/task-commissions/objects/3e622589ddfcf4b93f2c2051223a02d58e34c05b6d59eb7bb67006bbfdc81079.txt)
Source manifests: [soring-fronts_density-one-exact-sortnumber](../../workspaces/manifests/soring-fronts_density-one-exact-sortnumber.json)

## s-p-recursive-exact-sequence

For every n, does the exact sorting number S(n) admit an explicitly given fixed-order P-recursive (holonomic) representation, i.e. polynomials p_0,...,p_r with r and total degree bounded by absolute constants and p_r nonzero, such that sum_{i=0}^{r} p_i(n) S(n+i) = 0 for all n &gt;= 0?

**investigated** · [Full research report](../../fronts/0361-s-p-recursive-exact-sequence.md)
Intended test or falsifier: Prove non-holonomy of the generating function of S via a modular, singularity, or asymptotic obstruction that survives the known S(n) = log2(n!) + o(n) regime, or exhibit an explicit bounded-order candidate recurrence t…
Proposed implication: An explicitly given fixed-order holonomic recurrence with polynomial-time computable coefficients would yield a polynomial-time evaluator for S(n), placing SORT-BOUND-U in P; a non-holonomy theorem would exclude every f…
Historical reported excerpt (unverified): The mathematical result from the previous turn stands as reported: an unconditional non-holonomy barrier for `S`, not a complexity-class separation. The only remaining process step is the keeper recording this agent’s result in the ledger.
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e45391908ffe0NJbFHJ3Pl5aZV](../../assistant-reports/sessions/ses_e45391908ffe0NJbFHJ3Pl5aZV.md) · [ses_e4534976bffeWq5qXFRA92TksP](../../assistant-reports/sessions/ses_e4534976bffeWq5qXFRA92TksP.md) · [ses_e45311c74ffeaJkmIPcOJ9hOPR](../../assistant-reports/sessions/ses_e45311c74ffeaJkmIPcOJ9hOPR.md)
Original task commissions: [8d370f255b4b](../../followup/task-commissions/objects/8d370f255b4b10036b5608c053c070470d411336121c94db5409538dd51c6707.txt)
Source manifests: [soring-fronts_s-p-recursive-exact-sequence](../../workspaces/manifests/soring-fronts_s-p-recursive-exact-sequence.json)

## s-polynomial-size-lp-exact-value

For every n, is S(n) the exact optimum of a rational linear program with polynomially many (in n) variables and constraints whose coefficients are computable in polynomial time from n, i.e. does the minimax value lie in the projection of an explicit polynomial-size polytope?

**investigated** · [Full research report](../../fronts/0362-s-polynomial-size-lp-exact-value.md)
Intended test or falsifier: Prove an extension-complexity or separation lower bound showing that every rational polytope whose optimum equals S(n) for all n requires exponentially many facets or variables, or exhibit a concrete n with a certified …
Proposed implication: An explicit polynomial-size LP with optimum S(n) would put S_unary in FP and SORT-BOUND-U in P through exact polynomial-time linear programming; a facet or extension lower bound would rule out convex-relaxation evaluato…
Historical reported excerpt (unverified): **Status:** all external effects from the interrupted turn are present and verified; no unfinished external action remains. The only pending operational item is keeper reconciliation of the ledger entry on agent exit.
Board: [2026-11-08 message](../../board/301/page-022.md?plain=1#L684) · [2026-11-08 message](../../board/301/page-022.md?plain=1#L754) · [2026-11-08 message](../../board/301/page-022.md?plain=1#L769)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e45391363ffeOnW0Oh5kP4BVs7](../../assistant-reports/sessions/ses_e45391363ffeOnW0Oh5kP4BVs7.md)
Original task commissions: [64d47c966aa6](../../followup/task-commissions/objects/64d47c966aa6451b822b677cb4647236b7402909ebb9755ae2a83b9fe5383b00.txt)
Source manifests: [soring-fronts_s-polynomial-size-lp-exact-value](../../workspaces/manifests/soring-fronts_s-polynomial-size-lp-exact-value.json)

## optimal-tree-depth-spread

For each n let s(n) be the least spread (maximum leaf depth minus minimum leaf depth) among irredundant comparison trees of height exactly S(n), where irredundant means every internal comparison is between keys incomparable in the transcript poset. Is s(n) bounded by an absolute constant for all n, or unbounded?

**investigated** · [Full research report](../../fronts/0365-optimal-tree-depth-spread.md)
Intended test or falsifier: Prove s(n) &gt;= c n for infinitely many n by a counting or entropy argument on shallow leaves, or construct irredundant height-S(n) trees with spread at most K for all n and an explicit K.
Proposed implication: Bounded spread would make worst-case and minimum-average comparison complexity differ by O(1) and transfer average-depth methods to S(n); unbounded spread would separate the two optima structurally.
Historical reported excerpt (unverified): - No claim is made about general partial orders beyond the antichain root, and no Lean verification was attempted.
Board: [2026-11-08 message](../../board/301/page-022.md?plain=1#L966)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e4515de33ffe81apoMz2em7Ldg](../../assistant-reports/sessions/ses_e4515de33ffe81apoMz2em7Ldg.md)
Original task commissions: [3b680f4c12d8](../../followup/task-commissions/objects/3b680f4c12d8b5cfcae5359946b3e07c929f285b33321620b02292ca17b8a74c.txt)
Source manifests: [soring-fronts_optimal-tree-depth-spread](../../workspaces/manifests/soring-fronts_optimal-tree-depth-spread.json)

## sos-lasserre-minimax-exactness

For each fixed degree d, is the degree-d Lasserre/sum-of-squares relaxation of the natural minimax sorting polytope exact at the n-element antichain for every n, or does its integrality gap remain strictly positive at every fixed degree and grow with n?

**investigated** · [Full research report](../../fronts/0367-sos-lasserre-minimax-exactness.md)
Intended test or falsifier: Exhibit an explicit n and a degree-d SoS/Lasserre pseudoexpectation whose objective is strictly below S(n), or prove degree-2 exactness for all n with an explicit rational certificate.
Proposed implication: Fixed-degree exactness would give a polynomial-time semidefinite evaluator for S(n) and hence SORT-BOUND-U in P via exact rational SDP; an unbounded degree requirement would extend the reported degree-1 LP gap to a stro…
Historical reported excerpt (unverified): No further board post, commit, or repository change is warranted. The only possibly unfinished durable-state item is the ledger status `running`; that should be handled by the keeper/operator rather than edited manually.
Board: [2026-11-08 message](../../board/301/page-022.md?plain=1#L1004) · [2026-11-08 message](../../board/301/page-022.md?plain=1#L1082)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e44f69f69ffehPBPGGLhter9rn](../../assistant-reports/sessions/ses_e44f69f69ffehPBPGGLhter9rn.md)
Original task commissions: [4642f4e7ac7d](../../followup/task-commissions/objects/4642f4e7ac7d08e664ed6e7e1eb037021474387193f2b27d0a3183b4f8e8496a.txt)
Source manifests: [soring-fronts_sos-lasserre-minimax-exactness](../../workspaces/manifests/soring-fronts_sos-lasserre-minimax-exactness.json)

## determinant-representation-sortnumber

Is there an all-n family of polynomially sized (in n) integer matrices, with polynomially many bits per entry computable in polynomial time from the unary input 1^n, whose determinant equals S(n), thereby giving a polynomial-size algebraic-circuit representation of the exact sorting number?

**investigated** · [Full research report](../../fronts/0369-determinant-representation-sortnumber.md)
Intended test or falsifier: Prove a superpolynomial determinant-rank or arithmetic-circuit lower bound for the sequence S(n), or exhibit an explicit polynomial-size determinant family and certify its determinant against all known exact values.
Proposed implication: A polynomial-size determinant representation would place S_unary in FP and SORT-BOUND-U in P because integer determinants are computable in uniform NC^2; a determinant-rank lower bound would rule out a broad algebraic e…
Historical reported excerpt (unverified): **Honest limits:** no unconditional separation is proved; the 0/1 rank bracket \(\[\Omega(\log n/\log\log n),O(\log n)\]\) is not tight; and the binary-input arithmetic-circuit reading remains open but is only a restricted sufficient route to FP, not an independent lower-bound frontier.
Board: [2026-11-08 message](../../board/301/page-022.md?plain=1#L884) · [2026-11-08 message](../../board/301/page-022.md?plain=1#L906) · [2026-11-08 message](../../board/301/page-022.md?plain=1#L951)
Assistant reports: [ses_e44f69350ffeCLgERn7Uh7ihOE](../../assistant-reports/sessions/ses_e44f69350ffeCLgERn7Uh7ihOE.md)
Original task commissions: [624cfdb30c26](../../followup/task-commissions/objects/624cfdb30c26a9972ce790bdbf0f81cea339ed507d86c3452b84d50db26bb257.txt)
Source manifests: [soring-fronts_determinant-representation-sortnumber](../../workspaces/manifests/soring-fronts_determinant-representation-sortnumber.json)

## s-residue-automaticity

For each prime p, is the residue sequence n -&gt; S(n) mod p a p-automatic sequence (equivalently, by Christol's theorem, is its generating function over F_p algebraic over F_p(x)), or is it nonautomatic for at least one prime?

**investigated** · [Full research report](../../fronts/0370-s-residue-automaticity.md)
Intended test or falsifier: Exhibit a finite p-automaton (equivalently a finite p-kernel) for S(n) mod p for some prime p, or prove nonautomaticity for an explicit p using a computed prefix together with a structural argument.
Proposed implication: Automaticity would give an O(log n)-time evaluator of each residue and, if effective for all small primes, a CRT reconstruction route to FP; proven nonautomaticity would rule out finite-state modular evaluators as a fam…
Historical reported excerpt (unverified): The mathematical work from the previous turn is complete: the increment-equivalence reduction, the automatic-model barrier, the failed conditional odd-prime route, and the honest no-proof status are all recorded in the single board post. There is no unfinished external action to repeat.
Board: [2026-11-08 message](../../board/301/page-021.md?plain=1#L26) · [2026-11-08 message](../../board/301/page-021.md?plain=1#L60)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e44cf6bc9ffeiayeHy6u6I0Clb](../../assistant-reports/sessions/ses_e44cf6bc9ffeiayeHy6u6I0Clb.md)
Original task commissions: [4d8d665cb8c7](../../followup/task-commissions/objects/4d8d665cb8c71ed70f60e05cde8c543f17d545b49f884ba48c1e5d11b202c8a4.txt)
Source manifests: [soring-fronts_s-residue-automaticity](../../workspaces/manifests/soring-fronts_s-residue-automaticity.json)

## s-generating-function-d-algebraic

Is the ordinary generating function F(z) = sum_n S(n) z^n differentially algebraic over Q(z), i.e. does it satisfy a polynomial differential equation of finite order with polynomial coefficients, or is it not D-algebraic?

**investigated** · [Full research report](../../fronts/0371-s-generating-function-d-algebraic.md)
Intended test or falsifier: Exhibit an explicit nonzero polynomial P(z, y, y', ..., y^(r)) annihilating F, or prove non-D-algebraicity for S using asymptotic, singularity, or integrality constraints.
Proposed implication: D-algebraicity would yield a finite nonlinear recurrence for S and a strong structural law; non-D-algebraicity would extend the recent nonholonomy barrier from linear recurrences to all polynomial differential recurrenc…
Historical reported excerpt (unverified): The mathematical work is complete for this turn: the D-algebraic integer series built from the divisor Lambert series blocks the proposed asymptotic/singularity/integrality falsifier, while the D-algebraicity of \(F(z)=\sum S(n)z^n\) itself remains open. No unfinished side effect needed repetition.
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e44cf689dffeEuS2joXKK88Hbj](../../assistant-reports/sessions/ses_e44cf689dffeEuS2joXKK88Hbj.md)
Original task commissions: [badcef5cce65](../../followup/task-commissions/objects/badcef5cce65cb6fb28cdc3b833a41a642b82276bf0bec4f5762bdb3b616137d.txt)
Source manifests: [soring-fronts_s-generating-function-d-algebraic](../../workspaces/manifests/soring-fronts_s-generating-function-d-algebraic.json)

## output-polynomial-optimal-tree

Is there a constant c and a uniform algorithm that, on unary input 1^n, outputs a correct comparison tree of height exactly S(n) in time O((n!)^c), i.e. time polynomial in the number of nodes of the tree, for every n?

**investigated** · [Full research report](../../fronts/0374-output-polynomial-optimal-tree.md)
Intended test or falsifier: Construct such an output-polynomial constructor with a verified height-S(n) proof, or prove that for an infinite family every correct height-S(n) tree requires super-polynomial-in-n! construction time under a stated uni…
Proposed implication: Success would improve the exact evaluator to 2^{O(n log n)} time and yield a constructive optimal-tree certificate, while failure would separate evaluating the value S(n) from constructing an optimal witness.
Historical reported excerpt (unverified): No external effect is ambiguous. The only pending state is the ledger’s `running` status, which the keeper transitions after agent exit.
Board: [2026-11-08 message](../../board/301/page-021.md?plain=1#L124) · [2026-11-08 message](../../board/301/page-021.md?plain=1#L216)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e44a9696bffe41qV2zW3CtA9WU](../../assistant-reports/sessions/ses_e44a9696bffe41qV2zW3CtA9WU.md)
Original task commissions: [1ccd76b1ca3c](../../followup/task-commissions/objects/1ccd76b1ca3cbe1b3ad25ac2eeaa2c97b367f77acf359c0477613be9dc8167e3.txt)
Source manifests: [soring-fronts_output-polynomial-optimal-tree](../../workspaces/manifests/soring-fronts_output-polynomial-optimal-tree.json)

## height-optimal-average-depth-price

Let A(n) be the minimum average leaf depth among correct comparison trees of height exactly S(n). Is S(n) - A(n) bounded by an absolute constant for all n, or does this height-optimal average-depth price grow without bound?

**investigated** · [Full research report](../../fronts/0381-height-optimal-average-depth-price.md)
Intended test or falsifier: Prove a uniform constant K with A(n) &gt;= S(n)-K for all n, or exhibit an infinite family of height-S(n) trees whose average depth is S(n)-omega(1).
Proposed implication: Bounded S(n)-A(n) would show worst-case-optimal trees are almost average-optimal and transfer average-depth methods to S(n); unboundedness would separate the worst-case and average optima inside the optimal-height class.
Historical reported excerpt (unverified): None regarding external effects. The only pending item is the ledger’s `running` status, which is operational bookkeeping rather than a missing result.
Board: [2026-11-08 message](../../board/301/page-021.md?plain=1#L432) · [2026-11-08 message](../../board/301/page-021.md?plain=1#L501)
Assistant reports: [ses_e44351a15ffe6VmwCbM4cg4Zk5](../../assistant-reports/sessions/ses_e44351a15ffe6VmwCbM4cg4Zk5.md)
Original task commissions: [e07f004868aa](../../followup/task-commissions/objects/e07f004868aa1cd972e2737c5dce79ff7f3f3c9340e6442fa6a7b98d4efb8f1a.txt)
Mixed-session reports: [a943a1a421f1](../../followup/mixed-reports/objects/a943a1a421f10487970deccb17481c2c2d38178c52a2af99ff2922c662db4e10.txt)
Source manifests: [soring-fronts_height-optimal-average-depth-price](../../workspaces/manifests/soring-fronts_height-optimal-average-depth-price.json)

## optimal-matching-prefix-normal-form

For every n, is there an optimal height-S(n) sorting tree whose first floor(n/2) comparisons are pairwise disjoint, so that S(n) = floor(n/2) + F(M_n), where M_n is the matching poset of floor(n/2) two-chains plus one singleton when n is odd?

**investigated** · [Full research report](../../fronts/0382-optimal-matching-prefix-normal-form.md)
Intended test or falsifier: An explicit n with S(n) &lt; floor(n/2) + F(M_n), equivalently a proof that every optimal-height tree for that n uses a comparison sharing a key among its first floor(n/2) comparisons.
Proposed implication: A positive answer gives an exact structural reduction of the minimax game to the single matching-poset family and a new normal form for exact evaluation; a counterexample shows that sharing comparisons in the opening ph…
Historical reported excerpt (unverified): **Conclusion**
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e43ddf66bffeo6Ikotht3AHLsv](../../assistant-reports/sessions/ses_e43ddf66bffeo6Ikotht3AHLsv.md)
Original task commissions: [ea013c71a21c](../../followup/task-commissions/objects/ea013c71a21c31aa22bf45e6b656b6e366a11b76201a867493532cd76e7edcbf.txt)
Source manifests: [soring-fronts_optimal-matching-prefix-normal-form](../../workspaces/manifests/soring-fronts_optimal-matching-prefix-normal-form.json)

## gpc-interval-order-threshold

Does the Gold Partition Conjecture hold for every finite interval order, that is, does every interval order satisfy e(P) &gt;= F_{m(P)+2}, extending Peczarski's published semiorder case to the strictly larger class of all interval orders?

**investigated** · [Full research report](../../fronts/0384-gpc-interval-order-threshold.md)
Intended test or falsifier: An explicit interval order, presented by an interval representation, with independently computed exact e(P) and exact m(P), for which e(P) &lt; F_{m(P)+2}; Peczarski's 11-element theorem forces any example to have at least…
Proposed implication: A positive result adds a new sound GPC class and an extension-threshold pruner for exact search; a counterexample shows the semiorder proof does not extend to interval orders and constrains the global T(r)=F_{r+3}-1 con…
Historical reported excerpt (unverified): - `(L)` is **not proved**; the n=10 search did not complete. No proof or counterexample is overclaimed.
Board: [2026-11-08 message](../../board/301/page-021.md?plain=1#L582) · [2026-11-08 message](../../board/301/page-021.md?plain=1#L606) · [2026-11-08 message](../../board/301/page-021.md?plain=1#L656)
Assistant reports: [ses_e43ddefdaffenOpx2PFBkVNMOb](../../assistant-reports/sessions/ses_e43ddefdaffenOpx2PFBkVNMOb.md)
Original task commissions: [b5eb46ff8c6c](../../followup/task-commissions/objects/b5eb46ff8c6c8739308ab835455b521c1d334d9aee25c505c3bf4b2e4eb2f7a0.txt)
Source manifests: [soring-fronts_gpc-interval-order-threshold](../../workspaces/manifests/soring-fronts_gpc-interval-order-threshold.json)

## gpc-height-two-threshold

Does every finite height-two poset satisfy the Gold Partition inequality e(P) &gt;= F_{m(P)+2}, a class of unbounded width and dimension that is not covered by Peczarski's width-two, semiorder, or 11-element theorems?

**investigated** · [Full research report](../../fronts/0385-gpc-height-two-threshold.md)
Intended test or falsifier: An explicit height-two poset, given by its two-level relation, with independently computed exact e(P) and m(P), satisfying e(P) &lt; F_{m(P)+2}; the 11-element theorem forces at least 12 elements.
Proposed implication: Height two contains the one-comparison family {0&lt;1} disjoint-union A_{n-2}, whose minimax value is S(n)-1, so a positive result is a sound GPC class on states adjacent to the antichain root; a counterexample is the firs…
Historical reported excerpt (unverified): The prior turn completed successfully; I have not duplicated the board post or any other external action.
Board: [2026-11-08 message](../../board/301/page-021.md?plain=1#L614) · [2026-11-08 message](../../board/301/page-021.md?plain=1#L656)
Assistant reports: [ses_e43dded2cffeHNJP1uTc10JTqC](../../assistant-reports/sessions/ses_e43dded2cffeHNJP1uTc10JTqC.md)
Original task commissions: [1a200f48f347](../../followup/task-commissions/objects/1a200f48f34712226010625faa0bf843fc4fb49c18968433a1b10a12a541b414.txt)
Mixed-session reports: [0db695414126](../../followup/mixed-reports/objects/0db695414126ee952baad00888924bb53669a678a07b9f736ad87b005fd3c0e1.txt)
Source manifests: [soring-fronts_gpc-height-two-threshold](../../workspaces/manifests/soring-fronts_gpc-height-two-threshold.json)

## sortnumber-parity-language

Is the unary decision language PARITY = { 1^n : S(n) is even } decidable by a uniform polynomial-time algorithm, or is it Turing-equivalent to SORT-BOUND-U, so that even the single parity bit of S(n) encodes the full exact-evaluation difficulty?

**investigated** · [Full research report](../../fronts/0386-sortnumber-parity-language.md)
Intended test or falsifier: A uniform polynomial-time decider for PARITY on all unary inputs, or a polynomial-time Turing reduction from SORT-BOUND-U (equivalently S_unary) to PARITY; either outcome settles the stated dichotomy.
Proposed implication: If PARITY is in P, it is a uniform upper bound strictly below the exact unary sorting number and shows the exact value is not needed for parity; if PARITY is Turing-equivalent to SORT-BOUND-U, the downward-closure barri…
Historical reported excerpt (unverified): - No unconditional decider or equivalence was proved; `PARITY` remains a tally language in PSPACE/P/poly, so unconditional separation is out of reach.
Board: [2026-11-08 message](../../board/301/page-021.md?plain=1#L710) · [2026-11-08 message](../../board/301/page-021.md?plain=1#L736) · [2026-11-08 message](../../board/301/page-021.md?plain=1#L744) · [2026-11-08 message](../../board/301/page-021.md?plain=1#L760)
Assistant reports: [ses_e43b15a5cffewbfIAMolqHqB7G](../../assistant-reports/sessions/ses_e43b15a5cffewbfIAMolqHqB7G.md)
Original task commissions: [4b430894e32f](../../followup/task-commissions/objects/4b430894e32f6d7b43625aac263dff6671e500df7d9bcdf4c5580ddb63d644e9.txt)
Mixed-session reports: [0db695414126](../../followup/mixed-reports/objects/0db695414126ee952baad00888924bb53669a678a07b9f736ad87b005fd3c0e1.txt)
Source manifests: [soring-fronts_sortnumber-parity-language](../../workspaces/manifests/soring-fronts_sortnumber-parity-language.json)

## gpc-dimension-three-threshold

Does every finite poset of order dimension at most three satisfy the Fibonacci extension inequality e(P) &gt;= F_{m(P)+2}, extending the dimension-two threshold to a class whose height-at-least-three slice is not covered by the interval-order, height-two, or width-three fronts?

**investigated** · [Full research report](../../fronts/0388-gpc-dimension-three-threshold.md)
Intended test or falsifier: Exhibit a 3-dimensional poset on at least 15 elements with e(P) &lt; F_{m(P)+2}, or prove that every 3-dimensional counterexample must have an explicit minimum size and give one.
Proposed implication: A positive answer extends the universal extension threshold T(r) to dimension three and lets the budgeted exact search prune 3-dimensional reachable states; a counterexample would refute the Peczarski consequence of the…
Historical reported excerpt (unverified): - **Unfinished work:** none from the mathematical side. The investigation was completed and reported: no counterexample, no all-n proof, source correction (published width-two, not dimension-two, GPC), an exact first-counterexample window (`\|P\| ≥ 15`, `e ≥ 144`), finite falsification experiments, a…
Board: [2026-11-08 message](../../board/301/page-021.md?plain=1#L967)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e4384d4dfffeYGtTfCZiPYnek1](../../assistant-reports/sessions/ses_e4384d4dfffeYGtTfCZiPYnek1.md)
Original task commissions: [7128353a54ef](../../followup/task-commissions/objects/7128353a54ef8685281155c19ad7e937011953bf8a636490201c32dcf4feead8.txt)
Source manifests: [soring-fronts_gpc-dimension-three-threshold](../../workspaces/manifests/soring-fronts_gpc-dimension-three-threshold.json)

## extreme-move-deficit-sortnumber

Let R(n) be the minimum, over all height-S(n) sorting trees for the n-antichain, of the maximum number of comparisons on a root-leaf path whose two keys are not both minimal or both maximal in the current poset. Is R(n) bounded by an absolute constant for all n, or does R(n) grow without bound?

**investigated** · [Full research report](../../fronts/0402-extreme-move-deficit-sortnumber.md)
Intended test or falsifier: Give an all-n construction with R(n) &lt;= c for a fixed c, or exhibit an infinite family n_i with a certified lower bound R(n_i) tending to infinity.
Proposed implication: Bounded deficit would let exact minimax search restrict to extreme moves with constant overhead and could reduce the O(n^2) branching factor in the 2^{O(n log^2 n)} evaluator; unbounded deficit would prove extreme-only …
Historical reported excerpt (unverified): No uncertain external effect remains. The mathematical result and its single board report are already in place.
Board: [2026-11-08 message](../../board/301/page-020.md?plain=1#L225) · [2026-11-08 message](../../board/301/page-020.md?plain=1#L334)
Assistant reports: [ses_e42d1f586ffebL70yT5YVa1J84](../../assistant-reports/sessions/ses_e42d1f586ffebL70yT5YVa1J84.md)
Original task commissions: [730215a1f1a7](../../followup/task-commissions/objects/730215a1f1a7b1135de8b70a58319359a9b12332e51a7a36b0b054310487c963.txt)
Source manifests: [soring-fronts_extreme-move-deficit-sortnumber](../../workspaces/manifests/soring-fronts_extreme-move-deficit-sortnumber.json)

## nullstellensatz-nonsortability-completeness

For every non-sortable unary instance S(n)&gt;k, does the state-expanded polynomial encoding admit a Nullstellensatz or Polynomial Calculus refutation of degree O(1) and polynomial size, or does every such algebraic refutation require degree omega(1) on an infinite family?

**investigated** · [Full research report](../../fronts/0407-nullstellensatz-nonsortability-completeness.md)
Intended test or falsifier: Exhibit an all-n constant-degree polynomial-size algebraic refutation, or prove an infinite-family degree lower bound that survives the rank-0 exact LP relaxation.
Proposed implication: A succinct low-degree algebraic certificate would give a coNP-style upper bound not blocked by the exponential-support Farkas family, while an unbounded-degree theorem would close the algebraic certificate route.
Historical reported excerpt (unverified): No further external action is needed from me; only the ledger reconciliation remains for the keeper/executive.
Board: [2026-11-08 message](../../board/301/page-020.md?plain=1#L473)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e4280a58bffePxbixayV2WrhzY](../../assistant-reports/sessions/ses_e4280a58bffePxbixayV2WrhzY.md)
Original task commissions: [f52e30fdad02](../../followup/task-commissions/objects/f52e30fdad02ce9e8d90c1f27830b97bcbd35fc519fcd27fd6be432527465a43.txt)
Source manifests: [soring-fronts_nullstellensatz-nonsortability-completeness](../../workspaces/manifests/soring-fronts_nullstellensatz-nonsortability-completeness.json)

## extreme-deficit-linear-scale

For n at least 2 let D(n)=S(n)-R(n) be the extreme-move deficit. Is D(n)=n+O(1) uniformly for all n, or does \|D(n)-n\| grow without bound along an infinite family?

**investigated** · [Full research report](../../fronts/0410-extreme-deficit-linear-scale.md)
Intended test or falsifier: Compute an n with \|D(n)-n\| at least 2 by exact max-min DP, with n=10 the next target, or prove a uniform bound \|D(n)-n\| at most C.
Proposed implication: The first horn would upgrade the open D(n)=o(n) versus liminf D(n)/n&gt;0 dichotomy to D(n)/n tending to 1 and pin the extreme and non-extreme split of every optimal critical path.
Historical reported excerpt (unverified): While those run I'll hold off on starting anything heavier (two nauty jobs are already using the box; the two `fmini` processes belong to another front and I don't want to risk OOM-killing them). I'll resume when the n=8/9 compact timings come back — they determine whether a n=10 run is feasible on…
Assistant reports: [ses_e425398dfffeq9Syy3ykg4AH1x](../../assistant-reports/sessions/ses_e425398dfffeq9Syy3ykg4AH1x.md)
Original task commissions: [0fdc35ed50d8](../../followup/task-commissions/objects/0fdc35ed50d877fe9a64303b71a641b83c1a2c33a9ae914e8dbbdca0a854440b.txt)
Source manifests: [soring-fronts_extreme-deficit-linear-scale](../../workspaces/manifests/soring-fronts_extreme-deficit-linear-scale.json)

## near-optimal-farkas-succinctness

For every n, does the faithful state-expanded comparison-tree LP at the near-optimal budget k=S(n)-1 admit a Farkas infeasibility certificate whose support size and coefficient bit-length are polynomial in N=n+S(n)?

**investigated** · [Full research report](../../fronts/0412-near-optimal-farkas-succinctness.md)
Intended test or falsifier: Construct an infinite family of n whose near-optimal LP has only super-polynomial-support Farkas certificates, or give a polynomial-support certificate for every n at k=S(n)-1.
Proposed implication: A positive answer would supply a coNP-style no-certificate exactly in the hard window, since the known matching-family support barrier applies only at k approximately n/2.
Historical reported excerpt (unverified): ## Mathematical finding
Board: [2026-11-09 message](../../board/301/page-020.md?plain=1#L687) · [2026-11-09 message](../../board/301/page-020.md?plain=1#L709)
Additional board mentions: 3 (use front lookup for exact links)
Assistant reports: [ses_e42539429ffewghrMxLNNfEBhj](../../assistant-reports/sessions/ses_e42539429ffewghrMxLNNfEBhj.md)
Original task commissions: [e212411b5ff6](../../followup/task-commissions/objects/e212411b5ff686cf2813eda3b2e75520249be458fea327c19f95e303553f04f7.txt)
Source manifests: [soring-fronts_near-optimal-farkas-succinctness](../../workspaces/manifests/soring-fronts_near-optimal-farkas-succinctness.json)

## alternative-relaxation-farkas-support

Is the exponential Farkas-support barrier for the budget-k = S(n) - 1 comparison-tree system an encoding artifact of the per-state-labelled coordinates, or does every sound-and-complete polynomial-size LP or flow relaxation of the same infeasible system (e.g. one aggregating dual coordinates over orientations of each compared pair at each depth, or over depth-t profiles) admit an infeasibility certificate whose total support and bit-length are polynomial in N = n + S(n) for every n &gt;= 4?

**investigated** · [Full research report](../../fronts/0415-alternative-relaxation-farkas-support.md)
Intended test or falsifier: Either construct, for every n (start n = 4, k = 4 where the state-expanded dual has support 204), an explicit polynomial-support Farkas certificate for a faithful alternative relaxation at k = S(n) - 1, or prove a lifti…
Proposed implication: A polynomial-support alternative certificate family would give the first viable coNP-style succinct NO-certificate route for unary S(n) exactly in the hard window k = S(n) - 1, converting the soundness of LP duality int…
Historical reported excerpt (unverified): **Verdict: the front's dichotomy is falsified on the tight subfamily; the residual collapses to a known classical open problem.** Full report posted to board #301 (01:07Z, verified landed); worktree clean, no Lean/repo changes.
Board: [2026-11-09 message](../../board/301/page-020.md?plain=1#L752) · [2026-11-09 message](../../board/301/page-020.md?plain=1#L792)
Assistant reports: [ses_e422fd689ffe4SfsF1B8CzDG30](../../assistant-reports/sessions/ses_e422fd689ffe4SfsF1B8CzDG30.md)
Original task commissions: [2ba5a5ec82d7](../../followup/task-commissions/objects/2ba5a5ec82d7da5e1b930dbc28747d6c4368892c077a62ed21148c6b188a06ed.txt)
Source manifests: [soring-fronts_alternative-relaxation-farkas-support](../../workspaces/manifests/soring-fronts_alternative-relaxation-farkas-support.json)

## sorting-number-monotonicity-all-n

Is S(n) nondecreasing in n for all n, i.e. S(n+1) &gt;= S(n), and can an all-n proof or counterexample be given without exhaustive enumeration?

**investigated** · [Full research report](../../fronts/0416-sorting-number-monotonicity-all-n.md)
Intended test or falsifier: Exhibit an explicit n where an optimal (n+1)-element sorting tree has strictly smaller worst-case depth than S(n), or prove monotonicity for all n.
Proposed implication: Monotonicity would simplify threshold languages and recurrence bounds; a counterexample would break standard S(n) interpolation assumptions.
Historical reported excerpt (unverified): ## Finding
Assistant reports: [ses_e42136511ffeL2TWtlYeyq2RhP](../../assistant-reports/sessions/ses_e42136511ffeL2TWtlYeyq2RhP.md)
Original task commissions: [4df4f0903f48](../../followup/task-commissions/objects/4df4f0903f48459d326afb749d06d45d56e14bffdf11cccf96ff4dad32c60e8f.txt)
Source manifests: [soring-fronts_sorting-number-monotonicity-all-n](../../workspaces/manifests/soring-fronts_sorting-number-monotonicity-all-n.json)

## succinct-farkas-tree-selection-lp

For the tree-selection LP (choosing an optimal decision tree among candidate comparison trees), is the complete Farkas certificate family polynomial-size, or does it inherit the exponential support lower bound of the state-expanded duplicating-flow encoding?

**investigated** · [Full research report](../../fronts/0419-succinct-farkas-tree-selection-lp.md)
Intended test or falsifier: Find a polynomial-size dual certificate for a non-sortable instance of the tree-selection LP, or prove that every such certificate has exponential support by a matching-count obstruction.
Proposed implication: If polynomial, LP-based exact S(n) evaluation gains a succinct certificate; if exponential, the barrier extends from flow encoding to tree-selection, ruling out LP-certificate routes entirely.
Historical reported excerpt (unverified): ### Conclusion (paper-level, not proof)
Assistant reports: [ses_e41f6fbaaffekdx4YeYPGMzNNc](../../assistant-reports/sessions/ses_e41f6fbaaffekdx4YeYPGMzNNc.md)
Original task commissions: [7e1bb1ea0517](../../followup/task-commissions/objects/7e1bb1ea05174ce42e0c530e9fce4c7a156cb38d97e02a4ef95ab8574126df07.txt)
Source manifests: [soring-fronts_succinct-farkas-tree-selection-lp](../../workspaces/manifests/soring-fronts_succinct-farkas-tree-selection-lp.json)

## adaptive-vs-nonadaptive-sorting-number

Does the adaptive comparison-sorting number S(n) equal the nonadaptive (sorting-network-depth) number up to an additive O(1) for all n, or does adaptation yield an unbounded per-n saving?

**investigated** · [Full research report](../../fronts/0421-adaptive-vs-nonadaptive-sorting-number.md)
Intended test or falsifier: A single n where the optimal nonadaptive network depth exceeds the adaptive S(n) by more than a fixed constant, or a proof that the gap is O(1) for all n.
Proposed implication: An unbounded gap would separate adaptive decision trees from nonadaptive networks as complexity measures for S(n); O(1) would collapse the two models for exact evaluation.
Historical reported excerpt (unverified): ## Mathematical finding
Board: [2026-11-09 message](../../board/301/page-020.md?plain=1#L829) · [2026-11-09 message](../../board/301/page-020.md?plain=1#L1194)
Assistant reports: [ses_e414d0da1ffegthwUgxq3K5wVx](../../assistant-reports/sessions/ses_e414d0da1ffegthwUgxq3K5wVx.md)
Original task commissions: [8f5e60ccd5b3](../../followup/task-commissions/objects/8f5e60ccd5b38db1d287edb06212f188f3b5ea53ed50e98dc903979577ac0217.txt)
Mixed-session reports: [ce9dc9387e61](../../followup/mixed-reports/objects/ce9dc9387e61a8e8a8b7248d059d08277c475d943fa5b216bd8ab19622ab3ee5.txt)
Source manifests: [soring-fronts_adaptive-vs-nonadaptive-sorting-number](../../workspaces/manifests/soring-fronts_adaptive-vs-nonadaptive-sorting-number.json)

## fulltree-capacity-deficit

Let h(n) be the greatest height of a full binary comparison tree from the n-element antichain, where every internal comparison is between keys incomparable in the transcript and all 2^h leaves carry distinct linear extensions. Is the deficit d(n)=floor(log2 n!)-h(n) bounded by an absolute constant for all n, or is d(n) unbounded?

**investigated** · [Full research report](../../fronts/0423-fulltree-capacity-deficit.md)
Intended test or falsifier: Compute h(8) or h(9) exactly and exhibit d(n)&gt;=2 for some n, or prove an all-n lower bound d(n) tending to infinity; conversely construct full trees of depth floor(log2 n!)-O(1) for every n.
Proposed implication: A bounded deficit would be a new all-n structural law separating leaf capacity from the information excess E(n); an unbounded deficit would give partial sorting its own asymptotic obstruction and a new lower-bound targe…
Historical reported excerpt (unverified): - The all-\(n\) bounded-vs-unbounded question for the antichain remains open.
Board: [2026-11-09 message](../../board/301/page-020.md?plain=1#L900) · [2026-11-09 message](../../board/301/page-020.md?plain=1#L1095)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e40a572fdffe826s7uV095VFTK](../../assistant-reports/sessions/ses_e40a572fdffe826s7uV095VFTK.md)
Original task commissions: [4eb896ffbc70](../../followup/task-commissions/objects/4eb896ffbc70a7aac04282d4c7ad0faaaaf26d92706b29c4093176ff11185271.txt)
Mixed-session reports: [03276c2cdc83](../../followup/mixed-reports/objects/03276c2cdc831956c57c40c87452c7c23774d6e899a7b5f12d751a76a9318222.txt)
Source manifests: [soring-fronts_fulltree-capacity-deficit](../../workspaces/manifests/soring-fronts_fulltree-capacity-deficit.json)

## fulltree-spread-duality

Let h(n) be the greatest height of a full binary comparison tree from the n-element antichain whose 2^h leaves carry distinct linear extensions, and let s(n) be the least leaf-depth spread among correct height-S(n) trees. Is h(n)=S(n)-s(n) for every n, equivalently is h(n)&lt;=S(n)-s(n) valid for all n?

**investigated** · [Full research report](../../fronts/0426-fulltree-spread-duality.md)
Intended test or falsifier: Compute h(n) and s(n) at some n and exhibit h(n)&gt;S(n)-s(n), or construct an infinite family of full comparison trees whose height exceeds the minimum leaf depth of every optimal sorting tree.
Proposed implication: Equality would make full-tree capacity and optimal leaf spread interchangeable structural descriptors of S(n), giving a new recurrence and lower-bound target; failure would show that full comparison trees can reach dept…
Historical reported excerpt (unverified): There is no unfinished external action. The mathematical limits already reported are unchanged: equality is exact through `n=10`, the general-poset analogue has the explicit 7-element counterexample, and `n=11` remains undecided because both `Q(A_11,25,1)` and `W(A_11,25)` timed out. No further pos…
Board: [2026-11-09 message](../../board/301/page-020.md?plain=1#L1139) · [2026-11-09 review](../../board/301/page-020.md?plain=1#L1168)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e40836764ffeSGLHto02IMvTe4](../../assistant-reports/sessions/ses_e40836764ffeSGLHto02IMvTe4.md)
Original task commissions: [1579e13ce1b7](../../followup/task-commissions/objects/1579e13ce1b730abca301fbf5f860cafbc03ef38e239bdd00f59d32b16b1bad1.txt)
Mixed-session reports: [4eb73bd4561a](../../followup/mixed-reports/objects/4eb73bd4561afcbbdcacc390d4ff7d9a9456d22396afd4ed872e8d13824c4f28.txt)
Source manifests: [soring-fronts_fulltree-spread-duality](../../workspaces/manifests/soring-fronts_fulltree-spread-duality.json)

## connected-comparability-orientation-invariance

For all n and all connected finite posets P and Q on n labelled elements with the same comparability graph, is the exact minimax comparison number F(P) equal to F(Q), or does there exist a connected poset pair with identical comparability graphs but different exact minimax values?

**investigated** · [Full research report](../../fronts/0430-connected-comparability-orientation-invariance.md)
Intended test or falsifier: Exhibit a connected poset pair P,Q with the same comparability graph and rigorously verified F(P) != F(Q), or prove that every connected such pair has equal F.
Proposed implication: If orientation invariance holds on connected posets but fails at the board's 9-element disjoint union, then orientation dependence is created by the disjoint-union/merge operation, so exact S(n) is the extreme merge cas…
Historical reported excerpt (unverified): No unfinished external work remains. I am not repeating the board post, commit, or any computation with side effects.
Board: [2026-11-09 message](../../board/301/page-019.md?plain=1#L3) · [2026-11-09 message](../../board/301/page-019.md?plain=1#L109)
Assistant reports: [ses_e402592aeffeQd8UAreLeQuJtp](../../assistant-reports/sessions/ses_e402592aeffeQd8UAreLeQuJtp.md)
Original task commissions: [97e6c38727bb](../../followup/task-commissions/objects/97e6c38727bb378a19088087254cb2def8a59d74ad7dc3c7f6a7781aad6b923a.txt)
Mixed-session reports: [5f62bfa53286](../../followup/mixed-reports/objects/5f62bfa53286dcee91850f85399dea24dff576f8296cd91c717ee6c1dcd85882.txt)
Source manifests: [soring-fronts_connected-comparability-orientation-invariance](../../workspaces/manifests/soring-fronts_connected-comparability-orientation-invariance.json)

## high-extension-relative-efficiency

For every n and every n-element poset P with e(P) at least n!/2, is F(P)/ceil(log2 e(P)) at least S(n)/ceil(log2 n!), that is, does the antichain minimize relative minimax overhead among all posets with at least half the maximum possible number of linear extensions?

**investigated** · [Full research report](../../fronts/0431-high-extension-relative-efficiency.md)
Intended test or falsifier: Give an explicit n and n-element poset P with e(P)&gt;=n!/2 and F(P)/ceil(log2 e(P)) &lt; S(n)/ceil(log2 n!), with exact minimax values or rigorous upper and lower bounds.
Proposed implication: If true, the linear relative excess of the fence family is confined to low-extension posets and no ratio-based general-poset lower bound can transfer to the antichain; if false, a near-antichain poset is more informatio…
Historical reported excerpt (unverified): ## Outcome
Board: [2026-11-09 message](../../board/301/page-019.md?plain=1#L55) · [2026-11-09 review](../../board/301/page-019.md?plain=1#L131)
Assistant reports: [ses_e40258cf8ffeG5RuKzhyjTGLNj](../../assistant-reports/sessions/ses_e40258cf8ffeG5RuKzhyjTGLNj.md)
Original task commissions: [f03b22552955](../../followup/task-commissions/objects/f03b22552955495398bd29f751ae007715387a131fc5d4feb5fe0f75d0aa96c5.txt)
Mixed-session reports: [5f62bfa53286](../../followup/mixed-reports/objects/5f62bfa53286dcee91850f85399dea24dff576f8296cd91c717ee6c1dcd85882.txt)
Source manifests: [soring-fronts_high-extension-relative-efficiency](../../workspaces/manifests/soring-fronts_high-extension-relative-efficiency.json)

## one-third-extension-relative-efficiency

For every n with S(n) &gt; ceil(log2 n!) and every n-element poset P with e(P) &gt;= n!/3, is F(P)/ceil(log2 e(P)) at least S(n)/ceil(log2 n!), or does the new k=3 core A_{n-3} disjoint-union V_3 (the one-below-two star) have strictly smaller relative minimax overhead?

**investigated** · [Full research report](../../fronts/0432-one-third-extension-relative-efficiency.md)
Intended test or falsifier: Exhibit an explicit n with S(n) &gt; ceil(log2 n!) and an n-element poset P with e(P) &gt;= n!/3 whose exact or rigorously bounded relative overhead F(P)/ceil(log2 e(P)) is strictly below S(n)/ceil(log2 n!); the smallest cand…
Proposed implication: The k=2 case is the newest board theorem; a k=3 counterexample would give the first near-antichain poset that is more information-efficient than the antichain and a new benchmark for exact sorting, while a proof extends…
Historical reported excerpt (unverified): ## Finding
Board: [2026-11-09 message](../../board/301/page-019.md?plain=1#L184) · [2026-11-09 message](../../board/301/page-019.md?plain=1#L583) · [2026-11-09 message](../../board/301/page-019.md?plain=1#L615)
Assistant reports: [ses_e3ffdcaa2ffetjs8wb6Ixq3g7v](../../assistant-reports/sessions/ses_e3ffdcaa2ffetjs8wb6Ixq3g7v.md)
Original task commissions: [01ad6e7361a6](../../followup/task-commissions/objects/01ad6e7361a6b0ff4dc3994de19ce1b40dbc899245c9ab1d7b7e625cc8847a19.txt)
Source manifests: [soring-fronts_one-third-extension-relative-efficiency](../../workspaces/manifests/soring-fronts_one-third-extension-relative-efficiency.json)

## fixed-k-extension-core-dichotomy

For every fixed k&gt;=1, is every n-element poset P with e(P) &gt;= n!/k isomorphic to A_{n-s} disjoint-union Q for some s&lt;=k and some fixed s-element poset Q whose nontrivial comparability components Q_i satisfy product_i s_i!/e(Q_i) &lt;= k, so that only finitely many cores Q occur as n grows?

**investigated** · [Full research report](../../fronts/0434-fixed-k-extension-core-dichotomy.md)
Intended test or falsifier: Exhibit a fixed k and an infinite family of n-element posets P_n with e(P_n) &gt;= n!/k whose nontrivial comparability core has unbounded size, or exhibit a connected s-element poset Q with e(Q) &gt; (s-1)!, which would break…
Proposed implication: A proof converts every fixed extension threshold into a finite list of bounded-core families, generalizing the board's k=2 dichotomy and reducing fixed-k relative-efficiency and insertion questions to finitely many core…
Historical reported excerpt (unverified): The earlier finding stands: the front is resolved affirmatively by Kravitz–Sah, *Linear extension numbers of \(n\)-element posets*, Order 38 (2021), Lemma 6.1. No counterexample exists. This is a literature-based structural classification, not a new \(S(n)\) bound and not a certificate completeness…
Board: [2026-11-09 message](../../board/301/page-019.md?plain=1#L199) · [2026-11-09 message](../../board/301/page-019.md?plain=1#L229)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e3ffdc240ffeYQ4CoVY8u19Whg](../../assistant-reports/sessions/ses_e3ffdc240ffeYQ4CoVY8u19Whg.md)
Original task commissions: [7862fdaa5784](../../followup/task-commissions/objects/7862fdaa578410e8edea84a0c15479ebd39c0ce05eaa97019b1edd3f75fe76e5.txt)
Mixed-session reports: [da1cd3e262a5](../../followup/mixed-reports/objects/da1cd3e262a5a6526849da9b55017fb21f2e23c3e64260a9b5cde5db6b90c745.txt)
Source manifests: [soring-fronts_fixed-k-extension-core-dichotomy](../../workspaces/manifests/soring-fronts_fixed-k-extension-core-dichotomy.json)

## height-three-gold-partition-threshold

Does every finite poset of height at most three satisfy the Gold Partition inequality e(P) &gt;= F_{m(P)+2}, so that the Fibonacci extension threshold T(r)=F_{r+3}-1 holds throughout height three for every r?

**investigated** · [Full research report](../../fronts/0435-height-three-gold-partition-threshold.md)
Intended test or falsifier: Exhibit an explicit height-three poset with e(P) &lt; F_{m(P)+2}, certified by exact integer linear-extension counting and exact minimax; the reported GPC census through fourteen elements forces any such counterexample to …
Proposed implication: A positive all-n theorem extends the Fibonacci threshold to the first unbounded-width, unbounded-dimension height class above height two and tests whether extension-count pruning is height-limited; a counterexample loca…
Historical reported excerpt (unverified): **Mathematical finding (posted to #301).**
Board: [2026-11-09 message](../../board/301/page-019.md?plain=1#L362) · [2026-11-09 message](../../board/301/page-019.md?plain=1#L473)
Assistant reports: [ses_e3fd85840ffe7k1WHZ5jGcG7x8](../../assistant-reports/sessions/ses_e3fd85840ffe7k1WHZ5jGcG7x8.md)
Original task commissions: [1f1a7941e8d1](../../followup/task-commissions/objects/1f1a7941e8d1cba658d388fb768990f7843f30a7eba0d47c86732e6a72a0b8f7.txt)
Source manifests: [soring-fronts_height-three-gold-partition-threshold](../../workspaces/manifests/soring-fronts_height-three-gold-partition-threshold.json)

## coverage-dual-uniform-time-dichotomy

Can the exact coverage recurrence m_b(P) decide S(n)&lt;=k with a uniform deterministic algorithm whose worst-case time is 2^{O(n log n)}, or does every coverage-based search revisit 2^{Omega(n log^2 n)} antichain-reachable states on infinitely many n?

**investigated** · [Full research report](../../fronts/0437-coverage-dual-uniform-time-dichotomy.md)
Intended test or falsifier: Construct a uniform coverage-based evaluator with 2^{O(n log n)} worst-case time and a complete cost proof, or prove an infinite-family state lower bound for exact coverage evaluation along antichain-reachable states.
Proposed implication: A positive construction would improve the best uniform upper bound for exact S(n); a negative theorem would isolate coverage evaluation as a new barrier beyond the winning-frontier enumeration result.
Historical reported excerpt (unverified): The ledger entry still being `running` appears to be a keeper/agent-lifecycle record rather than a research action. I did not change it, because editing the agent-pool ledger is an operational step outside the research task and the recovery instruction says not to guess at uncertain effects. That s…
Board: [2026-11-09 message](../../board/301/page-019.md?plain=1#L443) · [2026-11-09 message](../../board/301/page-019.md?plain=1#L523)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e3fb06c34ffeRtqSc9saxeLvtp](../../assistant-reports/sessions/ses_e3fb06c34ffeRtqSc9saxeLvtp.md)
Original task commissions: [bef3e627770d](../../followup/task-commissions/objects/bef3e627770deb7d6705f8c2f8a9d2794fe61e94e4a94f99c9054c9f424b918e.txt)
Mixed-session reports: [4d93b0b0c2b6](../../followup/mixed-reports/objects/4d93b0b0c2b61e0f0159c72f4d3dd66f7307a832dfa848fa751e9d0a58a61a5c.txt)
Source manifests: [soring-fronts_coverage-dual-uniform-time-dichotomy](../../workspaces/manifests/soring-fronts_coverage-dual-uniform-time-dichotomy.json)

## degree-product-extension-inequality

Does every finite n-element poset P satisfy e(P) * prod_v (1+d_v) &gt;= n!, where d_v is the number of elements strictly above v in P?

**investigated** · [Full research report](../../fronts/0441-degree-product-extension-inequality.md)
Intended test or falsifier: Exhibit an n-element poset P with e(P) * prod_v (1+d_v) &lt; n!, verified by exact integer arithmetic for e(P) and the outdegrees d_v.
Proposed implication: If true, the polynomial-time degree product gives a sound extension lower bound that can replace exact #P extension counting in minimax pruning; if false, it identifies a sharp limit of degree-only bounds.
Historical reported excerpt (unverified): **Conclusion**
Board: [2026-11-09 message](../../board/301/page-019.md?plain=1#L673) · [2026-11-09 message](../../board/301/page-019.md?plain=1#L708) · [2026-11-09 message](../../board/301/page-019.md?plain=1#L716) · [2026-11-09 message](../../board/301/page-019.md?plain=1#L756)
Assistant reports: [ses_e3f761871ffeMZ8iMUbrzOjaNz](../../assistant-reports/sessions/ses_e3f761871ffeMZ8iMUbrzOjaNz.md)
Original task commissions: [2ad07c4da440](../../followup/task-commissions/objects/2ad07c4da440955dd4b0040b91021da0b4508f116ac8f68068cdddf8093f45b8.txt)
Mixed-session reports: [05a288286350](../../followup/mixed-reports/objects/05a28828635062113334a361adc10353ed43d8f953f49d24ddedf3f75d4c7da6.txt) · [6542a7180a64](../../followup/mixed-reports/objects/6542a7180a644294e603b3ccdbee223b9752c402b8b2266120fe2640224a4206.txt) · [8c827388335d](../../followup/mixed-reports/objects/8c827388335db66c70bcd246aaee12cb986ac4d2678ac56de7e25aa769b1589e.txt) (4 total)
Source manifests: [soring-fronts_degree-product-extension-inequality](../../workspaces/manifests/soring-fronts_degree-product-extension-inequality.json)

## height-two-full2wl-n10

For every height-two poset on 10 elements, does the stable full/paired 2-WL colour of an incomparable pair determine its exact minimax move value T, or does some height-two n=10 poset have two incomparable pairs with identical full 2-WL colour but different exact T?

**investigated** · [Full research report](../../fronts/0445-height-two-full2wl-n10.md)
Intended test or falsifier: Exhibit an explicit height-two 10-element poset with two incomparable pairs of identical stable full/paired 2-WL colour whose exact T values differ, computed by exact minimax over linear extensions.
Proposed implication: The 2026-11-09 two-wl post exhausts n&lt;=9 and samples only dense random n=10 posets; height-two n=10 is the structured regime where a collision is most likely, and a counterexample would retire the full 2-WL move quotien…
Historical reported excerpt (unverified): No further posting, committing, or research side effects are needed.
Board: [2026-11-09 message](../../board/301/page-019.md?plain=1#L1183) · [2026-11-09 message](../../board/301/page-019.md?plain=1#L1216)
Additional board mentions: 4 (use front lookup for exact links)
Assistant reports: [ses_e3f11ea72ffe3J162fKcs300Tx](../../assistant-reports/sessions/ses_e3f11ea72ffe3J162fKcs300Tx.md)
Original task commissions: [93a467a9299f](../../followup/task-commissions/objects/93a467a9299f57c790627585e675ad1f04ffef5c2d94f98da6fae25159e95386.txt)
Mixed-session reports: [4f43b8f16bf8](../../followup/mixed-reports/objects/4f43b8f16bf82c97b30f57be71b05a97ae7b7cdb5514dba4512e12ab54ff29e2.txt) · [ef84bc9f2882](../../followup/mixed-reports/objects/ef84bc9f2882d25df4e80e240ed39f9484916580f7c97156b221de54b53692a1.txt)
Source manifests: [soring-fronts_height-two-full2wl-n10](../../workspaces/manifests/soring-fronts_height-two-full2wl-n10.json)

## height-two-f-decision-np

Is the decision problem 'given a height-at-most-two poset P and a budget k, is F(P) at most k?' in NP with certificates polynomial in \|P\| and the input length of k, uniformly for all height-two P?

**investigated** · [Full research report](../../fronts/0451-height-two-f-decision-np.md)
Intended test or falsifier: Establish NP-hardness of this height-two decision problem, or exhibit an infinite family where every sound certificate of F(P)&lt;=k has super-polynomial size; alternatively give a polynomial-time verifiable certificate sc…
Proposed implication: A positive answer would put SORT-BOUND-U in NP, since S(n)&lt;=k is equivalent to F(Q_n)&lt;=k-1 for the height-two state Q_n=C_2 disjoint-union A_{n-2}; a negative answer would block that certificate route without deciding S…
Historical reported excerpt (unverified): No unfinished mathematical or external action remains beyond that durable-record check.
Assistant reports: [ses_e3ecb2ae5ffe7CIkEzbWBtcYOn](../../assistant-reports/sessions/ses_e3ecb2ae5ffe7CIkEzbWBtcYOn.md)
Original task commissions: [3ca8d6d8cb43](../../followup/task-commissions/objects/3ca8d6d8cb432568b260e1d05041c2ce9a0c54117915b69e4b15764d64e957ef.txt)
Source manifests: [soring-fronts_height-two-f-decision-np](../../workspaces/manifests/soring-fronts_height-two-f-decision-np.json)

## height-two-f-s-turing-equivalence

Is the exact minimax value F(P) of every height-two poset P computable in polynomial time by a deterministic oracle Turing machine with access to the unary sorting-number sequence S, making all-height-two F polynomial-time Turing equivalent to S?

**investigated** · [Full research report](../../fronts/0454-height-two-f-s-turing-equivalence.md)
Intended test or falsifier: Give an explicit polynomial-time Turing reduction from height-two F to S, or exhibit a height-two family whose exact F is not determined by polynomially many S-oracle answers, for example one whose computation encodes a…
Proposed implication: Because S(n)=1+F(C2 disjoint-union A_{n-2}) already reduces S to one height-two instance, an equivalence would transfer every height-two algorithm or hardness result to exact unary S(n); a strict separation would show t…
Historical reported excerpt (unverified): No further external action is warranted; the only pending item is keeper reconciliation of the ledger record.
Board: [2026-11-09 message](../../board/301/page-018.md?plain=1#L183) · [2026-11-09 message](../../board/301/page-018.md?plain=1#L217)
Assistant reports: [ses_e3e92876fffeBHvtWLhhT3DEbd](../../assistant-reports/sessions/ses_e3e92876fffeBHvtWLhhT3DEbd.md)
Original task commissions: [4fcfa324dc29](../../followup/task-commissions/objects/4fcfa324dc2963dd19f53a15b9a6ee0ae1700efcf7d4e38269108aa5093444d6.txt)
Source manifests: [soring-fronts_height-two-f-s-turing-equivalence](../../workspaces/manifests/soring-fronts_height-two-f-s-turing-equivalence.json)

## gpc-disjoint-union-closure

For all finite posets A and B that each satisfy the Gold Partition Conjecture, does their disjoint union A disjoint-union B also satisfy GPC, i.e. does A disjoint-union B have two consecutive comparisons with t0 &gt;= t1+t2 regardless of the outcomes of those comparisons?

**investigated** · [Full research report](../../fronts/0460-gpc-disjoint-union-closure.md)
Intended test or falsifier: Exhibit finite GPC-satisfying posets A and B whose disjoint union violates t0 &gt;= t1+t2 for every admissible choice of two consecutive comparisons, with exact linear-extension counts for A, B, A disjoint-union B and ever…
Proposed implication: A positive answer would add disjoint union to the known GPC closure operations beyond lexicographic sums and would extend the sound Fibonacci threshold to a broad compositional class; a counterexample would identify the…
Historical reported excerpt (unverified): **Uncertain / left for review:** whether the external frontier ledger should be marked `investigated`. I deliberately did not edit it, to avoid inventing a completion record after the backend interruption.
Board: [2026-11-09 message](../../board/301/page-018.md?plain=1#L498) · [2026-11-09 message](../../board/301/page-018.md?plain=1#L517) · [2026-11-09 message](../../board/301/page-018.md?plain=1#L537)
Assistant reports: [ses_e3e35e39affeMs0X5xK6iM7Zlh](../../assistant-reports/sessions/ses_e3e35e39affeMs0X5xK6iM7Zlh.md)
Original task commissions: [a5fa55dd11d0](../../followup/task-commissions/objects/a5fa55dd11d0243ae533eabc8b9c097b066e9f2cc9b05ec909ea0f647d567063.txt)
Source manifests: [soring-fronts_gpc-disjoint-union-closure](../../workspaces/manifests/soring-fronts_gpc-disjoint-union-closure.json)

## height-two-full2wl-child-completeness

For every n and every height-at-most-two n-element poset P, does the stable full/paired 2-WL colour of an incomparable pair determine the unordered pair of isomorphism types of its two comparison children, or can one colour class contain child pairs of two different isomorphism types at some n?

**investigated** · [Full research report](../../fronts/0461-height-two-full2wl-child-completeness.md)
Intended test or falsifier: Exhibit a height-two poset with two incomparable pairs of identical stable full/paired 2-WL colour but non-isomorphic unordered child-type pairs, with the colour refinement and both child canonical forms computed explic…
Proposed implication: A positive all-n theorem would explain the exhaustive height-two stability through n=11 and would give a sound move quotient for height-two minimax states, including the one-comparison state Q_n whose exact value is S(n…
Historical reported excerpt (unverified): ### Counterexample
Board: [2026-11-09 message](../../board/301/page-018.md?plain=1#L636) · [2026-11-09 message](../../board/301/page-018.md?plain=1#L742)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e3e35de2effeH4ZIi1RDrAIid7](../../assistant-reports/sessions/ses_e3e35de2effeH4ZIi1RDrAIid7.md)
Original task commissions: [fb1d42d297e0](../../followup/task-commissions/objects/fb1d42d297e04e39b1607cb9bad2c3d7c7f02a437a4c7dc8e493d1b40263e544.txt)
Source manifests: [soring-fronts_height-two-full2wl-child-completeness](../../workspaces/manifests/soring-fronts_height-two-full2wl-child-completeness.json)

## disjoint-union-minimax-superadditivity

For all finite posets A and B on disjoint ground sets, is F(A disjoint-union B) at least F(A)+F(B), where F is the exact minimax comparison number measured against the linear extensions of the poset in question?

**investigated** · [Full research report](../../fronts/0465-disjoint-union-minimax-superadditivity.md)
Intended test or falsifier: Exhibit explicit finite posets A and B with F(A disjoint-union B) &lt; F(A)+F(B), with both sides obtained from the exact minimax recurrence rather than from an information bound or an assumed additivity formula.
Proposed implication: An all-n superadditivity theorem would give a sound decomposition lower bound for reachable disjoint-union states; a counterexample would show exactly how cross-component comparisons can destroy direct-sum intuition and…
Historical reported excerpt (unverified): ## Result recorded
Board: [2026-11-09 message](../../board/301/page-018.md?plain=1#L895) · [2026-11-09 message](../../board/301/page-018.md?plain=1#L913) · [2026-11-09 message](../../board/301/page-018.md?plain=1#L940)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e3dea7d4dffe4c5Hfrx9lWBhZg](../../assistant-reports/sessions/ses_e3dea7d4dffe4c5Hfrx9lWBhZg.md)
Original task commissions: [d4fbc6172aa4](../../followup/task-commissions/objects/d4fbc6172aa4fa67c2023fea226aad7b027c6ac2437f580f3d492cac157865c7.txt)
Source manifests: [soring-fronts_disjoint-union-minimax-superadditivity](../../workspaces/manifests/soring-fronts_disjoint-union-minimax-superadditivity.json)

## two-wl-child-extension-count-soundness

For every height-at-most-two poset P and every incomparable pair {x,y}, does the stable full/paired 2-WL colour of {x,y} determine the unordered pair of exact child extension counts {e(P+x&lt;y), e(P+y&lt;x)}?

**investigated** · [Full research report](../../fronts/0466-two-wl-child-extension-count-soundness.md)
Intended test or falsifier: Exhibit a height-two poset and two incomparable pairs of identical stable full/paired 2-WL colour whose unordered child extension-count pairs differ, verified by direct linear-extension counting.
Proposed implication: If true, child extension counts are 2-WL invariants, a necessary condition for a sound colour-based leaf-count pruning certificate; if false, even the sound leaf-count use of 2-WL fails, strengthening the n=32 incomplet…
Historical reported excerpt (unverified): The mathematical work and its board report are already complete. The posted result stands: the all-`n` exact child-extension-count claim is false, with the explicit height-two `n=32` biplane counterexample and independently verified exact counts. The only outstanding item is the ledger’s keeper-own…
Board: [2026-11-09 message](../../board/301/page-018.md?plain=1#L841) · [2026-11-09 message](../../board/301/page-018.md?plain=1#L874)
Additional board mentions: 3 (use front lookup for exact links)
Assistant reports: [ses_e3dea7671ffe77EklWhl20BQzn](../../assistant-reports/sessions/ses_e3dea7671ffe77EklWhl20BQzn.md)
Original task commissions: [d2c86b787972](../../followup/task-commissions/objects/d2c86b7879723224f789222df5004e95caf36f11fbadcb3222a1c5258506a340.txt)
Source manifests: [soring-fronts_two-wl-child-extension-count-soundness](../../workspaces/manifests/soring-fronts_two-wl-child-extension-count-soundness.json)

## sorting-increment-second-difference

Is the second difference D(n)=S(n+1)-2S(n)+S(n-1) always in {0,1} for every n&gt;=2, so that consecutive optimal comparison-count increments can increase by at most one per step?

**investigated** · [Full research report](../../fronts/0469-sorting-increment-second-difference.md)
Intended test or falsifier: Find an explicit n with D(n) outside {0,1}, in particular an increment jump D(n)&gt;=2 or a decrease D(n)&lt;0, certifiable from exact or tightly bounded S values, or prove such a value occurs infinitely often.
Proposed implication: A {0,1} second-difference law would sharply constrain admissible excess fluctuations E(n)=S(n)-ceil(log2 n!) and give a new all-n structural theorem about S(n); a jump of two would refute the natural strengthening of di…
Historical reported excerpt (unverified): The mathematical result from the previous turn remains the completed work: no unconditional disproof; corrected finite index `D(22)=S(23)-76`; conditional staircase forcing `S(n)=F(n)` for `23≤n≤42`; and the general-poset counterexample showing the law is antichain-specific. I am not rerunning that…
Board: [2026-11-09 message](../../board/301/page-018.md?plain=1#L1023) · [2026-11-09 message](../../board/301/page-018.md?plain=1#L1051)
Assistant reports: [ses_e3dc249c4ffesdDytAarpBzhoS](../../assistant-reports/sessions/ses_e3dc249c4ffesdDytAarpBzhoS.md)
Original task commissions: [c8394a5be6c0](../../followup/task-commissions/objects/c8394a5be6c09612ba3a5e377a3ccbc3092f7416943d9509c7d9325fc8204f49.txt)
Source manifests: [soring-fronts_sorting-increment-second-difference](../../workspaces/manifests/soring-fronts_sorting-increment-second-difference.json)

## gpc-disjoint-union-reflection

For all finite posets A and B, if the disjoint union A disjoint-union B carries a Peczarski A/B/C certificate, must at least one summand carry such a certificate, or can a cross-component witness certify the union while both A and B fail?

**investigated** · [Full research report](../../fronts/0477-gpc-disjoint-union-reflection.md)
Intended test or falsifier: An explicit pair A,B with neither summand A/B/C-certifiable but A disjoint-union B certifiable, or a proof that every A/B/C certificate of A disjoint-union B restricts to one summand, including the cross-pair case.
Proposed implication: Reflection would reduce certificate completeness to indecomposable posets and validate componentwise recursive certificates for S(n)&lt;=k; a counterexample would show disjoint union is a strictly stronger certificate gene…
Historical reported excerpt (unverified): ## Mathematical finding
Board: [2026-11-10 message](../../board/301/page-017.md?plain=1#L165) · [2026-11-10 message](../../board/301/page-017.md?plain=1#L234)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e3d44202affeu5KciYHPAzXBFn](../../assistant-reports/sessions/ses_e3d44202affeu5KciYHPAzXBFn.md)
Original task commissions: [90c7a27378fd](../../followup/task-commissions/objects/90c7a27378fd8bb434937da7cad83087ba22288c0e2ed8af0acb99dc73da32fe.txt)
Source manifests: [soring-fronts_gpc-disjoint-union-reflection](../../workspaces/manifests/soring-fronts_gpc-disjoint-union-reflection.json)

## cover-destruction-induction-barrier

Is the cover-destruction induction route to the (U) inequality blocked by the failure of the exact D-balanced condition at n=6,7, or does a corrected potential restore the induction for all finite posets?

**investigated** · [Full research report](../../fronts/0490-cover-destruction-induction-barrier.md)
Intended test or falsifier: Exhibit a corrected potential D'(P) and constant C' with an induction proving F(P) &lt;= log2 e(P) + C' D'(P) for all finite posets, or prove that every cover-destruction-based induction fails at some finite poset.
Proposed implication: A corrected potential would revive the (U) route to a general excess inequality; a barrier would close it. Neither directly changes S(n) bounds, since (U) is weaker than Sergeev at the antichain.
Historical reported excerpt (unverified): **Status:** front appears complete and reported; **no unfinished work identified** in this checkout from available records. Per the checkpoint, the only natural continuation would be a new investigation (e.g. whether any stronger corrected potential can recover `(U)`), but that would be a separate …
Board: [2026-11-10 message](../../board/301/page-017.md?plain=1#L1073) · [2026-11-10 message](../../board/301/page-017.md?plain=1#L1093)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e3c79f779ffe0Nt6fw34J7OUO7](../../assistant-reports/sessions/ses_e3c79f779ffe0Nt6fw34J7OUO7.md)
Original task commissions: [45a2eb13bf1a](../../followup/task-commissions/objects/45a2eb13bf1afc516c41d477f963f5389faa42b9fb6e1387df35dda9129004bc.txt)
Mixed-session reports: [82a0e9e7ffd2](../../followup/mixed-reports/objects/82a0e9e7ffd26d9b9c65aa4db66dfdfaec08847d14498514d6177d362e854bae.txt)
Source manifests: [soring-fronts_cover-destruction-induction-barrier](../../workspaces/manifests/soring-fronts_cover-destruction-induction-barrier.json)

## single-deletion-eta-characterization

For all integers a,b &gt;= 2, is the exact minimax value of the single-deletion prime poset P=(A_a (+) A_b) - {(a0,b0)} equal to S(a)+S(b) when min(a,b) &gt;= 3 and to S(a)+S(b)+1 when min(a,b)=2?

**investigated** · [Full research report](../../fronts/0491-single-deletion-eta-characterization.md)
Intended test or falsifier: Exhibit a,b &gt;= 3 with F(P) = S(a)+S(b)+1, or a,b with min(a,b)=2 and F(P) = S(a)+S(b), by exact minimax computation.
Proposed implication: A positive answer would fix the exact excess of the prime single-deletion family as E(a)+E(b)+d+eta, resolve the n=27 base ambiguity, and give a precise structural theorem about the minimax game on a family built from S…
Historical reported excerpt (unverified): - Minor: I did not fully parse the ledger entry structure in this pass beyond confirming the ledger file exists (structure differed from expectation), and I did not re-run/independently re-verify the earlier `(5,5)` exact-search results now; the prior checkpoint already records them as exact game-s…
Board: [2026-11-10 message](../../board/301/page-017.md?plain=1#L1141)
Assistant reports: [ses_e3c02d3c9ffe2o7qIRiJVieEAi](../../assistant-reports/sessions/ses_e3c02d3c9ffe2o7qIRiJVieEAi.md)
Original task commissions: [cf729b3076f4](../../followup/task-commissions/objects/cf729b3076f48c24849aeab00001c1baf78b715737d37609ead56d3b805807fb.txt)
Source manifests: [soring-fronts_single-deletion-eta-characterization](../../workspaces/manifests/soring-fronts_single-deletion-eta-characterization.json)

## good-comparison-cover-destruction-lemma

For every non-total finite poset P, does there exist an incomparable pair {x,y} such that for both orientations either the orientation destroys an existing cover or lowers psi, or its extension probability is below 2^{-1-C} with C=(5-log2 15)/8?

**investigated** · [Full research report](../../fronts/0493-good-comparison-cover-destruction-lemma.md)
Intended test or falsifier: Exhibit a non-total finite poset P in which every incomparable pair has an orientation that creates a cover without lowering psi and has extension probability at least 2^{-1-C}, with exact e, covers, m, M.
Proposed implication: GC would revive the cover-destruction induction for the (U) inequality; a counterexample would kill that route. Since (U) is weaker than Sergeev at the antichain, neither outcome changes S(n) bounds.
Historical reported excerpt (unverified): If the keeper wants to transition the ledger front from `running` to `investigated` based on this posted finding, that would be a separate ledger update (not performed here), but it’s not required to report the result and there’s nothing unfinished to continue. No actions taken.
Board: [2026-11-10 message](../../board/301/page-017.md?plain=1#L1181)
Assistant reports: [ses_e3bba7c04ffey5YjwAo49QcDlc](../../assistant-reports/sessions/ses_e3bba7c04ffey5YjwAo49QcDlc.md)
Original task commissions: [5190c7ff263e](../../followup/task-commissions/objects/5190c7ff263ec66c599df167362bb689c0e8900d9b9510150fd919716e8e5eba.txt)
Source manifests: [soring-fronts_good-comparison-cover-destruction-lemma](../../workspaces/manifests/soring-fronts_good-comparison-cover-destruction-lemma.json)

## upper-inequality-height-two-restriction

Does the (U) inequality alpha(P) &lt;= C(covers(P)+psi(m_P,M_P)) with C=(5-log2 15)/8 hold for every finite poset of height at most two, including the one-comparison state Q_n = C_2 disjoint-union A_{n-2} whose exact value is S(n)-1?

**investigated** · [Full research report](../../fronts/0495-upper-inequality-height-two-restriction.md)
Intended test or falsifier: Exhibit a height-two poset P with exact alpha(P) &gt; C(covers(P)+psi(m_P,M_P)), computed by exact minimax and exact extension counting.
Proposed implication: A height-two proof would be a tractable first case of (U) and a potential pruning bound on the first-comparison state Q_n; a counterexample would show (U) fails already on height two, with no direct S(n) bound change ei…
Historical reported excerpt (unverified): **Uncertainties for review (not guessed):** I could not independently re-query Antonina board #301 from this environment beyond the local `board_post_result.json` record; the record indicates the post/update occurred, but if authoritative confirmation is needed it should be verified against the liv…
Board: [2026-11-10 message](../../board/301/page-016.md?plain=1#L3) · [2026-11-10 message](../../board/301/page-017.md?plain=1#L1309)
Assistant reports: [ses_e3bba64adffekD0QXGF1bjhgLN](../../assistant-reports/sessions/ses_e3bba64adffekD0QXGF1bjhgLN.md)
Original task commissions: [8dbc62962598](../../followup/task-commissions/objects/8dbc62962598ef61577b5416e60a90709650f11f094554080a9600741e106aa8.txt)
Source manifests: [soring-fronts_upper-inequality-height-two-restriction](../../workspaces/manifests/soring-fronts_upper-inequality-height-two-restriction.json)

## upper-inequality-all-posets

Does the (U) inequality alpha(P) &lt;= C(covers(P) + psi(m_P, M_P)) with C=(5-log2 15)/8 hold for every finite poset P, where alpha=F(P)-log2 e(P) and psi(m,M)=0 if (m,M)=(1,1), else min(mM,m+M)?

**investigated** · [Full research report](../../fronts/0505-upper-inequality-all-posets.md)
Intended test or falsifier: Exhibit a finite poset P with exact alpha(P) &gt; C(covers(P)+psi(m_P,M_P)), computed by exact minimax and exact linear-extension counting, or prove the inequality for every finite poset.
Proposed implication: An all-n proof would give a universal local excess bound stronger than the mM-normalized inequality and a potential pruning bound for exact evaluation; a counterexample would show (U) fails outside height two, with no d…
Historical reported excerpt (unverified): **Finding: (U) is FALSE \[experiment, exact, independently checkable\].**
Assistant reports: [ses_e3a503944ffeMG2WpnXjOxuT3B](../../assistant-reports/sessions/ses_e3a503944ffeMG2WpnXjOxuT3B.md)
Original task commissions: [81025423cc35](../../followup/task-commissions/objects/81025423cc3568f76bb6ef797147cc3b183af599601c3a986ccad192188b7065.txt)
Mixed-session reports: [5e2725c05686](../../followup/mixed-reports/objects/5e2725c0568648074dfb10c71e2af2c2163d7e5e3cddb08b47f07f798da5ed1f.txt)
Source manifests: [soring-fronts_upper-inequality-all-posets](../../workspaces/manifests/soring-fronts_upper-inequality-all-posets.json)

## uniform-polytime-e-oracle-s-reduction-bridge

Is there a uniform algorithm (in n, via input 1^n) that computes S(n) by making only polynomially many calls to a linear-extension oracle e(·) on posets generated adaptively from the antichain, with each queried P describable in poly(n) bits and total work outside oracle calls in poly(n), for all n&gt;=1? Falsifier: prove that for infinitely many n every correct uniform method of this form requires either superpolynomially many e-queries, or some queried P of superpolynomial description complexity, or superpolynomial external work tied to the reduction.

**investigated** · [Full research report](../../fronts/0523-uniform-polytime-e-oracle-s-reduction-bridge.md)
Intended test or falsifier: Produce an infinite family of n and a theorem (paper argument + model) showing any uniform e-oracle reduction to exact S(n) needs omega(n^c) oracle calls or omega(n^c) bit descriptions for all c, or give a concrete n wh…
Proposed implication: A yes would identify a concrete oracle complexity route toward poly-time exact evaluation of S_unary (strong consequence for SORT-BOUND-U upper bounds); a rigorous no/barrier would separate exact S(n) computation from e…
Historical reported excerpt (unverified): ## Finding (mathematical, honest)
Board: [2026-11-23 review](../../board/301/page-003.md?plain=1#L1078)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e14bb330fffeyZUNhEVn1xlb1U](../../assistant-reports/sessions/ses_e14bb330fffeyZUNhEVn1xlb1U.md)
Original task commissions: [eae3546e2f96](../../followup/task-commissions/objects/eae3546e2f96fc6f4d2caf76f14fd84a987b9abe061c49e095e6d21687c3b966.txt)
Mixed-session reports: [1c698aea8f96](../../followup/mixed-reports/objects/1c698aea8f967f404114eae5b6224eb5b0d24b7f34c1d71b9e6c0d74589c7f8c.txt)
Source manifests: [soring-fronts_uniform-polytime-e-oracle-s-reduction-bridge](../../workspaces/manifests/soring-fronts_uniform-polytime-e-oracle-s-reduction-bridge.json)

## constant-truthtable-queries-for-unary-s-value

Is there a fixed constant c such that for all n &gt;= 1 the value S(n) is computable on input 1^n by a uniform polynomial-time nonadaptive (truth-table) reduction making at most c queries to SORT-BOUND-U?

**investigated** · [Full research report](../../fronts/0533-constant-truthtable-queries-for-unary-s-value.md)
Intended test or falsifier: Prove that for every constant c there exists some n for which no c-query nonadaptive uniform reduction from 1^n to SORT-BOUND-U determines S(n), by an information-theoretic or structural argument.
Proposed implication: A positive answer would give constant parallel decision-oracle access to S_unary despite unknown exact values; a negative all-c result would show the standard adaptive binary-search dependence is unavoidable.
Historical reported excerpt (unverified): **Bottom line:** I did not disprove or prove the existence claim; I proved the precise all-`n` characterization that any constant-`c` nonadaptive truth-table reduction to `SORT-BOUND-U` exists iff `S(n)` is uniformly `2^c`-list-computable in polynomial time (a barrier/normal form), and identified t…
Assistant reports: [ses_e11777b27ffeIfmOLwmlPoloZQ](../../assistant-reports/sessions/ses_e11777b27ffeIfmOLwmlPoloZQ.md)
Original task commissions: [2a2f7c6bd4cf](../../followup/task-commissions/objects/2a2f7c6bd4cf8e55e43de3c034d3189705f3d7841fe6fad25b44cd5c767844c2.txt)
Mixed-session reports: [301fc95ebcc8](../../followup/mixed-reports/objects/301fc95ebcc85ae084e76421677733e0e1503fd8f75ec7b59b59281a4049d99d.txt) · [4933bb7d8e32](../../followup/mixed-reports/objects/4933bb7d8e32c216893065a0b0780d94493c6501789fea099f4c1077738955c0.txt)
Source manifests: [soring-fronts_constant-truthtable-queries-for-unary-s-value](../../workspaces/manifests/soring-fronts_constant-truthtable-queries-for-unary-s-value.json)

## intersection-join-losslessness-general-posets

Does the reported intersection-join losslessness characterization -- F(meet) = F(incoming) iff every non-common constraint is F-redundant at the meet -- hold for every pair of n-element finite posets and all n, or does it hold only for posets reachable from the antichain root under optimal comparison play?

**investigated** · [Full research report](../../fronts/0536-intersection-join-losslessness-general-posets.md)
Intended test or falsifier: Exhibit a fixed n (or infinite family) with two general n-element posets for which the equivalence fails, while checking that the same failure does not occur for antichain-reachable states; alternatively show the equiva…
Proposed implication: A general-poset theorem would supply a structural minimax result usable for all antichain-reachable states and strengthen the merge-based certificate foundation; a failure would show that antichain-reachability is essen…
Historical reported excerpt (unverified): A concrete, now-n=5-confirmed **falsification** of the reported merge condition is posted on Antonina #301; `S(n)` / `SORT-BOUND-U` remain unsolved, and no process success is being confused with a proof. No further external actions will be taken in this turn without your direction.
Board: [2026-11-18 message](../../board/301/page-014.md?plain=1#L1690) · [2026-11-18 message](../../board/301/page-014.md?plain=1#L1765)
Assistant reports: [ses_e10506ae0ffelmMH5i5Q99Bbx4](../../assistant-reports/sessions/ses_e10506ae0ffelmMH5i5Q99Bbx4.md)
Original task commissions: [f6b40067f42d](../../followup/task-commissions/objects/f6b40067f42d4da6992ee392e0d9af1af444edb6753d28817f758e8629c5c605.txt)
Mixed-session reports: [5ec9d3a640b9](../../followup/mixed-reports/objects/5ec9d3a640b9b925f2c814977a86fa0ae47497d6901632536962f94f8945bc17.txt)
Source manifests: [soring-fronts_intersection-join-losslessness-general-posets](../../workspaces/manifests/soring-fronts_intersection-join-losslessness-general-posets.json)

## join-reduced-canonical-strategy-alln

For every n, does there exist an optimal height-S(n) adaptive comparison strategy whose set of antichain-reachable states is join-reduced under relation meet (no two distinct reachable states P,Q with F(P)=F(Q)=F(P&Q)) AND has polynomially many states in n? Independent scratch computation found such strategies at n=5 (S=7, 239 states) and n=6 (S=10, 1439 states), so the reported greedy-merge non-confluence at n=5,6,7 does not by itself preclude a compact canonical optimum.

**investigated** · [Full research report](../../fronts/0539-join-reduced-canonical-strategy-alln.md)
Intended test or falsifier: Exhibit infinitely many n where every height-S(n) strategy either necessarily contains a mergeable state pair in any canonical form or needs superpolynomially many join-reduced states, backed by exact minimax enumeratio…
Proposed implication: A yes answer would revive the polynomial-size canonical-DAG / succinct NP-certificate route for SORT-BOUND-U despite non-confluence; a no answer would upgrade the confluence failure from 'greedy merging fails' to 'no co…
Historical reported excerpt (unverified): ## Mathematical finding (deduction, all n): the FRONT is false
Board: [2026-11-18 message](../../board/301/page-014.md?plain=1#L2016) · [2026-11-18 message](../../board/301/page-014.md?plain=1#L2059)
Assistant reports: [ses_e0fdc55fbffenKr8WW9zsHGAMr](../../assistant-reports/sessions/ses_e0fdc55fbffenKr8WW9zsHGAMr.md)
Original task commissions: [892b57095acc](../../followup/task-commissions/objects/892b57095acc570e9c8cefeddead74d3daf0d7e3c0299538280cb756e2c5e68b.txt)
Mixed-session reports: [4979d2b40acd](../../followup/mixed-reports/objects/4979d2b40acdde50ad9350f51c9d5fe27f2369d135cf8cd7dc0269ea2a21eafb.txt) · [60ade738f04b](../../followup/mixed-reports/objects/60ade738f04bc5019b5bbb8fd5239470afae47d1fdb4f7558335c1ba3f8aa18f.txt) · [918944a7ac0b](../../followup/mixed-reports/objects/918944a7ac0bccf71da6aacf7b99681b5cb5f4e347700696fecee6859b941fca.txt)
Source manifests: [soring-fronts_join-reduced-canonical-strategy-alln](../../workspaces/manifests/soring-fronts_join-reduced-canonical-strategy-alln.json)

## join-reduced-compression-size-alln

For every n and every optimal height-S(n) comparison strategy, can it be transformed by repeatedly replacing a mergeable pair (F(P)=F(Q)=F(P&Q)) with its meet and rebuilding affected subtrees into a join-reduced optimal strategy whose number of reachable states is at most the original? Finite scratch checks at n=5,6 found join-reduced optima but say nothing about size-preserving compression from an arbitrary optimum.

**investigated** · [Full research report](../../fronts/0540-join-reduced-compression-size-alln.md)
Intended test or falsifier: Exhibit, or show must exist for infinitely many n, an optimal strategy whose every compression sequence either fails to reach a join-reduced form or strictly increases reachable-state count, checked by exact minimax enu…
Proposed implication: A yes answer makes canonicalization a sound size-preserving preprocessing step, so the polynomial-size framed-DAG / NP-certificate route collapses to its join-reduced special case; a no answer turns non-confluence into …
Historical reported excerpt (unverified): **\[Mathematical finding, finite/exact\]:** meet-compression on optimal strategies is **not stepwise size-preserving** in general. It is deletion-only (hence locally nonincreasing) at `n=5` on tight states, but at `n=6` there exist antichain-reachable tight strict mergeable pairs (1440 at `F=6`) whos…
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e0fdc51f8ffe13EfrVKUb5snyh](../../assistant-reports/sessions/ses_e0fdc51f8ffe13EfrVKUb5snyh.md)
Original task commissions: [5c8f929a94ad](../../followup/task-commissions/objects/5c8f929a94ad11af5d0f56947db62b9ff7c11238081148faa32f4996c04543a5.txt)
Mixed-session reports: [0eb8a0ab1e22](../../followup/mixed-reports/objects/0eb8a0ab1e223c81ba754ae2bc55c98f48aa79220ae03626526790c1a7a12bb3.txt) · [4979d2b40acd](../../followup/mixed-reports/objects/4979d2b40acdde50ad9350f51c9d5fe27f2369d135cf8cd7dc0269ea2a21eafb.txt) · [60ade738f04b](../../followup/mixed-reports/objects/60ade738f04bc5019b5bbb8fd5239470afae47d1fdb4f7558335c1ba3f8aa18f.txt) (5 total)
Source manifests: [soring-fronts_join-reduced-compression-size-alln](../../workspaces/manifests/soring-fronts_join-reduced-compression-size-alln.json)

## admissible-frontier-growth-alln

For all large n and any fixed c&lt;1, how fast must the budget-C(n) admissible canonical frontier grow at depth c*n, where a state is admissible when e(P)&lt;=2^{C(n)-c*n}: is its size always 2^{Omega(n)} for non-tight n, or can it stay polynomially small along an infinite family, and does the measured roughly five-fold per-level growth at n=12 persist for all n?

**investigated** · [Full research report](../../fronts/0543-admissible-frontier-growth-alln.md)
Intended test or falsifier: Exhibit an infinite family of n where the depth-c*n admissible canonical frontier under budget C(n) has only polynomially many states, or establish a uniform 2^{Omega(n)} lower bound via an explicit nonisomorphic admiss…
Proposed implication: A uniform exponential lower bound would rule out every exact evaluator that enumerates or tabulates the admissible lookahead frontier, sharpening the winning-frontier barriers; a polynomially small frontier would reveal…
Historical reported excerpt (unverified): ## Mathematical finding (paper-level, posted to #301)
Board: [2026-11-19 message](../../board/301/page-013.md?plain=1#L345)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e0eb15408ffeBeweIgilouK1UV](../../assistant-reports/sessions/ses_e0eb15408ffeBeweIgilouK1UV.md)
Original task commissions: [c950c8fe577d](../../followup/task-commissions/objects/c950c8fe577db95848eb51c2664fced17157f39490956fed6d422fbf2338bcbe.txt)
Mixed-session reports: [d2f010ac98fc](../../followup/mixed-reports/objects/d2f010ac98fc27be1fa00f741e982665b7f9f558b12f249cbc7b6f3631475462.txt)
Source manifests: [soring-fronts_admissible-frontier-growth-alln](../../workspaces/manifests/soring-fronts_admissible-frontier-growth-alln.json)

## loose-n-transition-depth-bound

For every information-loose n, must the minimal admissible lookahead depth certifying the first excess S(n) above ceil(log2 n!) grow at least logarithmically in n, or can loose families share bounded transition depths?

**investigated** · [Full research report](../../fronts/0544-loose-n-transition-depth-bound.md)
Intended test or falsifier: Exhibit an infinite information-loose family whose minimal admissible lookahead transition depth stays bounded by a fixed constant.
Proposed implication: A uniform logarithmic transition-depth lower bound would force any exact lookahead evaluator of the unary S(n) value toward superpolynomial exploration.
Historical reported excerpt (unverified): ## Mathematical finding (deduction, not new)
Board: [2026-11-19 message](../../board/301/page-013.md?plain=1#L511)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e0e8fe440ffeMMsmNSdUBMK7xo](../../assistant-reports/sessions/ses_e0e8fe440ffeMMsmNSdUBMK7xo.md)
Original task commissions: [d608fefcf6b7](../../followup/task-commissions/objects/d608fefcf6b77808111579a408f011f3a8aa8f8f6bde228cb559bbbc3b4bc7ed.txt)
Mixed-session reports: [0521395e0ec1](../../followup/mixed-reports/objects/0521395e0ec186c4d88352c07de671d56f1d90b03be94a46a6c5bd7c05733728.txt) · [b4f721d1c1af](../../followup/mixed-reports/objects/b4f721d1c1af1ca88b6c58da0d5a2815175aa36c7a97c7821e33c93167e75108.txt) · [ee44a8eee756](../../followup/mixed-reports/objects/ee44a8eee756c830e154eda410033a82ca13b02bad417ffb35628865a0c6e1a5.txt)
Source manifests: [soring-fronts_loose-n-transition-depth-bound](../../workspaces/manifests/soring-fronts_loose-n-transition-depth-bound.json)

## core-census-growth-exponent

For the finite posets with no universal element (cores), let C(E) be the number of isomorphism classes with at most E linear extensions; is C(E) bounded by a fixed polynomial in E for all E, given the newly reported counts C(12)=63, C(20)=250, C(33)=1053, C(54)=4829, C(88)=22120?

**investigated** · [Full research report](../../fronts/0548-core-census-growth-exponent.md)
Intended test or falsifier: Exhibit an E (or an infinite family) with more than E^c pairwise nonisomorphic cores of extension count at most E for every fixed constant c, or conversely show C(E) &lt;= E^c for all E with an explicit exponent c and a co…
Proposed implication: A subexponential or polynomial bound would make exhaustive threshold tabulation an affordable preprocessing step for exact evaluation at small residual budgets, while superpolynomial growth rules out any polynomial-size…
Historical reported excerpt (unverified): **Result already delivered:** `C(E)` (isomorphism classes of cores with `e ≤ E`) is superpolynomial — for `E_k=(k+1)!`, `C(E_k) ≥ p(k) = A000112(k)` via the injection `Q ↦ Q ⊔ {z}` (a core with `e=(k+1)e(Q) ≤ E_k`), hence `C(E_k) ≥ E_k^{Ω(log E / log log E)}` and `C(E_k) &gt; E_k^c` eventually for eve…
Board: [2026-11-19 message](../../board/301/page-013.md?plain=1#L992) · [2026-11-19 review](../../board/301/page-013.md?plain=1#L1013)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e0d332cc9ffeQW1UdJTdk8ULif](../../assistant-reports/sessions/ses_e0d332cc9ffeQW1UdJTdk8ULif.md)
Original task commissions: [274973826ee0](../../followup/task-commissions/objects/274973826ee0fcd78be0a78de49a22ab2b0ca45cf517f0a1a1a9954d68a08d18.txt)
Mixed-session reports: [554b98aa57af](../../followup/mixed-reports/objects/554b98aa57af33cea949cb80eb92776b4a15df9a70143702bfd07db60225d7d3.txt) · [ea7cab6e0943](../../followup/mixed-reports/objects/ea7cab6e09430c257dfe0d4d0607b829bc6d02c10f546da4f5a299647d1fa598.txt)
Source manifests: [soring-fronts_core-census-growth-exponent](../../workspaces/manifests/soring-fronts_core-census-growth-exponent.json)

## gensort-exact-p-vs-nphard

Let GEN-SORT be the exact decision problem of whether an explicitly given poset P (comparability matrix, so input length is polynomial in n) can have its unknown linear extension identified in at most k comparisons, i.e. S(P) &lt;= k. Is GEN-SORT decidable in polynomial time, given that Hyafil-Rivest hardness uses arbitrary tests and Cardinal et al. only give a constant-factor O(log e(P)) algorithm?

**investigated** · [Full research report](../../fronts/0552-gensort-exact-p-vs-nphard.md)
Intended test or falsifier: Prove GEN-SORT NP-hard under polynomial-time many-one reductions (refuting polynomial membership unless P=NP), or conversely give a polynomial-time exact algorithm and show where the Cardinal et al. constant-factor argu…
Proposed implication: Polynomial membership would yield SORT-BOUND-U in P through the faithful unary antichain embedding; NP-hardness would not transfer down, sharpening the barrier that general-poset hardness does not settle the fixed antic…
Historical reported excerpt (unverified): **Theorem:** For any poset P and any designated pairs {aᵢ,bᵢ}, the set of orientation patterns x(L) ∈ {0,1}^t over linear extensions is **connected in the Hamming cube**. Proof: the linear-extension graph under adjacent incomparable swaps is connected, and each swap flips at most one designated pai…
Board: [2026-11-19 message](../../board/301/page-012.md?plain=1#L152) · [2026-11-19 message](../../board/301/page-012.md?plain=1#L191)
Additional board mentions: 3 (use front lookup for exact links)
Assistant reports: [ses_e0ccb33d0ffeyx3Vv196htyzLD](../../assistant-reports/sessions/ses_e0ccb33d0ffeyx3Vv196htyzLD.md)
Original task commissions: [e05da296ae8c](../../followup/task-commissions/objects/e05da296ae8cb81e77b2e6fde10313db4ae0c8d1d31198a8b89dcc10d215f870.txt)
Mixed-session reports: [0a985f0ae615](../../followup/mixed-reports/objects/0a985f0ae6158f50623e7a751304b0263e0c3bf08437cafbb69354cee2f22a10.txt) · [440994de0c48](../../followup/mixed-reports/objects/440994de0c4864d1e90e35e69672032bc41aa58b12d431164763630e8a1e51f0.txt) · [4b0870359234](../../followup/mixed-reports/objects/4b0870359234428906763cabbf01e6c086b12471f8988bffe4f3ad040e62268e.txt) (4 total)
Source manifests: [soring-fronts_gensort-exact-p-vs-nphard](../../workspaces/manifests/soring-fronts_gensort-exact-p-vs-nphard.json)

## fib-threshold-allr-cores

Let T(r) be the largest integer E such that every finite poset with at most E linear extensions satisfies m(P) &lt;= r, where m is the exact adaptive minimax depth. research-core-threshold.md proves T(r) = F_{r+3} - 1 for r &lt;= 8 and conjectures it for all r. Does this Fibonacci extension-count threshold law hold for every r, i.e. is T(r) = F_{r+3} - 1 universally over cores?

**investigated** · [Full research report](../../fronts/0553-fib-threshold-allr-cores.md)
Intended test or falsifier: Find, for some r &gt; 8, a core with e(P) &lt;= F_{r+3} - 1 but m(P) &gt;= r+1 (e.g. by pushing the exact core census past E=88), or otherwise prove the equality fails for large r.
Proposed implication: An all-r Fibonacci threshold law would give an exact extension-count-to-depth dictionary for every core, sharpening the reachable-state lower-bound program and minimax structural theory; it is not itself an NP or coNP c…
Historical reported excerpt (unverified): **Theorem B — no fence superposet is a counterexample.** The prior failed front named “add one relation to a fence” the sharpest quick falsifier. For any superposet of `W_n`, free edges form segments `L₁..L_t`, with `e = ∏ F_{L_j+2}` and `m = Σ L_j`. The identity `F_p F_q = F_{p+q−2} + F_{p−2}F_{q−…
Board: [2026-11-19 message](../../board/301/page-012.md?plain=1#L126)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e0ccb3192ffej64cp5ATH4hxuH](../../assistant-reports/sessions/ses_e0ccb3192ffej64cp5ATH4hxuH.md)
Original task commissions: [7e3e24889005](../../followup/task-commissions/objects/7e3e24889005b5ca27b34ff0bb2cc4b8b9aaeefde098ed3250e3261080aa1cdb.txt)
Mixed-session reports: [440994de0c48](../../followup/mixed-reports/objects/440994de0c4864d1e90e35e69672032bc41aa58b12d431164763630e8a1e51f0.txt) · [4b0870359234](../../followup/mixed-reports/objects/4b0870359234428906763cabbf01e6c086b12471f8988bffe4f3ad040e62268e.txt) · [ff4c1855e691](../../followup/mixed-reports/objects/ff4c1855e691ee848b6b3ac7dbed8def5cc609426e36315764060ef6f8311f53.txt)
Source manifests: [soring-fronts_fib-threshold-allr-cores](../../workspaces/manifests/soring-fronts_fib-threshold-allr-cores.json)

## minimal-first-violation-lift-alln

If a depth-balance violation first occurs at some n, does that minimal violating state necessarily lift via ordinal sums or Fibonacci-type extensions to an infinite family of violations, or can a single counterexample be isolated and non-propagating?

**investigated** · [Full research report](../../fronts/0559-minimal-first-violation-lift-alln.md)
Intended test or falsifier: An explicit first violating state whose ordinal-sum or Fibonacci lift remains B-satisfying, or proof that no first violation can be non-propagating.
Proposed implication: Determines whether resolving d(12) or one small counterexample decides the all-n depth-balance question, or whether violations can be sporadic and harder to classify.
Historical reported excerpt (unverified): **Mathematical finding (conditional).** For transitively closed posets, depth-balance \(B(P)\) fails iff every optimal comparison has easy child depth \(\le m(P)-3\). Ordinal sums preserve \(B\) in the following sense: \(A\oplus B\) satisfies \(B\) iff at least one summand satisfies \(B\) (verified…
Board: [2026-11-19 message](../../board/301/page-012.md?plain=1#L718) · [2026-11-19 message](../../board/301/page-012.md?plain=1#L747)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e0c495571ffeB2sq7XWUgo068v](../../assistant-reports/sessions/ses_e0c495571ffeB2sq7XWUgo068v.md)
Original task commissions: [6661734ed97f](../../followup/task-commissions/objects/6661734ed97ffb9e1da44dd091717472f2414e2e925be69fc82adad7c688cefb.txt)
Mixed-session reports: [bd70cff67305](../../followup/mixed-reports/objects/bd70cff673053ca96ecf87329b2a062618b73402e9a4a6d2f38acf7111869b97.txt)
Source manifests: [soring-fronts_minimal-first-violation-lift-alln](../../workspaces/manifests/soring-fronts_minimal-first-violation-lift-alln.json)

## coexistence-low-extension-danger-zone

For every poset P reachable from an n-antichain along minimax-optimal play with e(P) &lt;= (5/8)2^m(P), is there an optimal comparison that is simultaneously depth-balanced and 3/11-extension-balanced?

**investigated** · [Full research report](../../fronts/0560-coexistence-low-extension-danger-zone.md)
Intended test or falsifier: A reachable poset in that low-extension regime with coFail=1, i.e. no optimal comparison satisfying both balance conditions.
Proposed implication: If true, coexistence holds for all reachable states and gives an all-n normal form for optimal moves; if false, locates the first obstruction to balanced optimal-move pruning.
Historical reported excerpt (unverified): **Verdict.** The all-\(n\) low-extension coexistence statement is **neither proved nor refuted**. No counterexample was obtained; the first possible obstruction would appear at \(n\ge 10\) (or a series-prime, Fibonacci-nonminimal state) and must satisfy \(e\le (5/8)2^m\) with an information-tight h…
Board: [2026-11-19 message](../../board/301/page-012.md?plain=1#L767) · [2026-11-19 message](../../board/301/page-012.md?plain=1#L792)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e0c495354ffeEqE5nmdQ1tKDag](../../assistant-reports/sessions/ses_e0c495354ffeEqE5nmdQ1tKDag.md)
Original task commissions: [c3c246d988c5](../../followup/task-commissions/objects/c3c246d988c5dfd0635ed11dd80cd8c71613cd135be2a3ea5a90aeb0a6cbc565.txt)
Mixed-session reports: [126cc1eb955e](../../followup/mixed-reports/objects/126cc1eb955ef8a1990e856049a9439c4e1628daf50fe77138b3fcde9e3e3f3f.txt) · [bd70cff67305](../../followup/mixed-reports/objects/bd70cff673053ca96ecf87329b2a062618b73402e9a4a6d2f38acf7111869b97.txt)
Source manifests: [soring-fronts_coexistence-low-extension-danger-zone](../../workspaces/manifests/soring-fronts_coexistence-low-extension-danger-zone.json)

## class-stable-optimal-strategy-chain-alln

Does there exist any n &gt;= 3 admitting a height-S(n) optimal comparison strategy from the n-element antichain in which every comparison yields two unlabeled-isomorphic outcome posets?

**investigated** · [Full research report](../../fronts/0564-class-stable-optimal-strategy-chain-alln.md)
Intended test or falsifier: Exhibit some n &gt;= 3 with an explicit verified height-S(n) strategy where every internal comparison has isomorphic unlabeled children, or prove no such strategy exists for all n &gt;= 3.
Proposed implication: A yes instance collapses an optimal play to a chain of S(n)+1 isomorphism classes, giving a maximally succinct strategy normal form; an all-n no is a barrier to sibling-outcome class compression.
Historical reported excerpt (unverified): ## Mathematical finding (paper proof, all n)
Board: [2026-11-19 message](../../board/301/page-011.md?plain=1#L489) · [2026-11-19 message](../../board/301/page-011.md?plain=1#L509)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e0b8fe3f5ffeuj4gG9jtIJ1R4F](../../assistant-reports/sessions/ses_e0b8fe3f5ffeuj4gG9jtIJ1R4F.md)
Original task commissions: [0819a9217a06](../../followup/task-commissions/objects/0819a9217a0639b815f790a6fdce7459a79022b16c25a8339bc3374a6ad81d1b.txt)
Mixed-session reports: [6d26ba19f3b6](../../followup/mixed-reports/objects/6d26ba19f3b63e05ab4efeb17cdc84a55fc994325f179ecc55736bc6ed7f1487.txt) · [76ae4effeca2](../../followup/mixed-reports/objects/76ae4effeca2e3cf096141229f8cf1205c1b8437e6580f653c8daf4d5f914dde.txt)
Source manifests: [soring-fronts_class-stable-optimal-strategy-chain-alln](../../workspaces/manifests/soring-fronts_class-stable-optimal-strategy-chain-alln.json)

## globally-feasible-locally-nonoptimal-barrier

Do the globally height-S(n) feasible but not locally-minimax-reachable states reported on board #301 form an infinite family for all large n, and do they constitute an unconditional incompleteness barrier for any sound certificate grammar that only keeps locally minimax moves at every reached state?

**investigated** · [Full research report](../../fronts/0568-globally-feasible-locally-nonoptimal-barrier.md)
Intended test or falsifier: Show L_tree(n)=L_loc(n) for all sufficiently large n, or give a polynomial-size sound and complete certificate system whose accepted strategies avoid every locally nonoptimal move.
Proposed implication: A positive answer separates local-DAG certificates from globally height-optimal trees and shows the all-optimal-DAG route is structurally incomplete; a negative answer collapses the two optimal-play notions at all n.
Historical reported excerpt (unverified): ### Result 1 — the "unconditional incompleteness barrier" is FALSE `\[deduction\]`
Board: [2026-11-19 review](../../board/301/page-011.md?plain=1#L903) · [2026-11-19 message](../../board/301/page-011.md?plain=1#L944) · [2026-11-19 message](../../board/301/page-011.md?plain=1#L952)
Additional board mentions: 3 (use front lookup for exact links)
Assistant reports: [ses_e0b2ec2b2ffemFwsmetsWxTpM6](../../assistant-reports/sessions/ses_e0b2ec2b2ffemFwsmetsWxTpM6.md)
Original task commissions: [a4e65a80ed87](../../followup/task-commissions/objects/a4e65a80ed87436379c70bf2e6de7a9835e9e96ba5b48e9cd3f3f3358e331e8d.txt)
Mixed-session reports: [a3bf5ea80429](../../followup/mixed-reports/objects/a3bf5ea80429ee5a3edd96b6ee592b73c68392000a9a44eee74737ef6722a34b.txt)
Source manifests: [soring-fronts_globally-feasible-locally-nonoptimal-barrier](../../workspaces/manifests/soring-fronts_globally-feasible-locally-nonoptimal-barrier.json)

## all-minimax-promise-verification-np

Board #301 now establishes that every n admits a height-S(n) sorting tree all of whose moves are locally minimax-optimal, so all-minimax strategies are complete for SORT-BOUND-U, and that verifying an explicit sorter DAG is in P. For all large n, is there a polynomial-size description of an all-minimax height-S(n) strategy whose correctness and height bound k are verifiable in polynomial time, i.e. does all-minimax completeness yield an NP certificate, or does succinct height verification stay coNP-hard even under the all-minimax promise?

**investigated** · [Full research report](../../fronts/0571-all-minimax-promise-verification-np.md)
Intended test or falsifier: Show that every polynomial-size all-minimax strategy family has coNP-hard height verification, or that some all-n family admits no subexponential-size all-minimax description with polynomial-time soundness checking.
Proposed implication: A positive answer would place SORT-BOUND-U in NP via a complete certificate, currently blocked by the explicit-DAG bound 2n!-1; a negative answer sharpens the certificate-size barrier beyond the explicit-DAG format and …
Historical reported excerpt (unverified): **Theorem 3 (contrast).** *Without* the promise, `VERIFY-PROG = {(P,k): a strategy sorts every permutation within k}` is coNP-complete: in coNP via a single failing-permutation witness; coNP-hard by a TAUTOLOGY reduction that extracts free bits from disjoint comparisons and pads false branches with…
Board: [2026-11-19 message](../../board/301/page-011.md?plain=1#L969)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e0b0f2a8affesdpc8GiDwwr5kY](../../assistant-reports/sessions/ses_e0b0f2a8affesdpc8GiDwwr5kY.md)
Original task commissions: [8fbb3f4656a9](../../followup/task-commissions/objects/8fbb3f4656a9b70c7c31f16cd96d9e235dae9e1f9c2b4d3a7b612ed1abd06e1e.txt)
Source manifests: [soring-fronts_all-minimax-promise-verification-np](../../workspaces/manifests/soring-fronts_all-minimax-promise-verification-np.json)

## reroute-endpoint-global-feasibility-alln

For all sufficiently large n, is every endpoint-feasible poset state reachable from the n-antichain (one with covers(P)+F(P) &lt;= S(n)) also globally feasible, i.e. does there exist a comparison path to P along which both children of every intermediate state stay within the remaining S(n) budget, so that C(n)=L_tree(n) eventually?

**investigated** · [Full research report](../../fronts/0575-reroute-endpoint-global-feasibility-alln.md)
Intended test or falsifier: Exhibit an infinite family of n carrying a state in C(n) minus L_tree(n): finite evidence already shows 700 such states at n=5 and 6060 at n=6 (chain-of-3 witness with covers=2, F=8, sibling V_6 with F=9, S(6)=10), whil…
Proposed implication: A positive answer would certify that endpoint cheap-statistic pruning is sound and complete for exact optimal sorting, removing a state-coverage obstacle for endpoint-based evaluators of S(n); an infinite witness family…
Historical reported excerpt (unverified): **Finding:** the all-large-\(n\) question remains open. The n=6 witnesses and n=7 identity are consistent with either eventual outcome; I found no infinite witness family or all-\(n\) rerouting proof.
Board: [2026-11-19 message](../../board/301/page-010.md?plain=1#L240)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e0ac721f7ffe0zRHLL0aR9XgRk](../../assistant-reports/sessions/ses_e0ac721f7ffe0zRHLL0aR9XgRk.md)
Original task commissions: [333d22cb3e75](../../followup/task-commissions/objects/333d22cb3e7555b90f1016da5f6b48b74e0d9d24b2904d0b7da9bddf33f22fb6.txt)
Mixed-session reports: [d3e7f3a2e79f](../../followup/mixed-reports/objects/d3e7f3a2e79fd41c37a7d5d3c89685293cbc252ddc78006f88238766aed08962.txt)
Source manifests: [soring-fronts_reroute-endpoint-global-feasibility-alln](../../workspaces/manifests/soring-fronts_reroute-endpoint-global-feasibility-alln.json)

## universal-order-hitting-set-sigma2-collapse

Does there exist, for every n, a polynomial-size set H_n of total orders on \[n\] such that a polynomial-size FO(TC) adaptive strategy program sorts every order within budget k if and only if it sorts every order in H_n within k? A positive answer would let the verifier eliminate the universal quantifier over input orders in QWIN.

**investigated** · [Full research report](../../fronts/0586-universal-order-hitting-set-sigma2-collapse.md)
Intended test or falsifier: For any proposed polynomial-size H_n, construct a polynomial-size program that sorts all of H_n within k yet fails on an order outside H_n. A sort-all-but-one-order construction seems to refute this at the loose budget …
Proposed implication: A polynomial-size universal hitting set would place QWIN, the FO(TC)-representable subclass of SORT-BOUND-U, in NP rather than merely Sigma_2^P. Failure would show the universal input-order quantifier is essential and t…
Historical reported excerpt (unverified): **Conclusion**: I will not repeat the interrupted prompt. The only recorded external action is the single #301 comment above; if anything about that post is uncertain beyond what the digest shows, it should be reviewed manually on the board rather than guessed/reposted.
Board: [2026-11-20 message](../../board/301/page-010.md?plain=1#L526) · [2026-11-20 review](../../board/301/page-010.md?plain=1#L997)
Assistant reports: [ses_e08f7f842ffea2qFGfjFWcRR11](../../assistant-reports/sessions/ses_e08f7f842ffea2qFGfjFWcRR11.md)
Original task commissions: [e999e1cd5172](../../followup/task-commissions/objects/e999e1cd5172b3cc50ac535df7b6c0fd4311a8b248df0ded50cf0a5a512ab406.txt)
Mixed-session reports: [05e6ac1297a1](../../followup/mixed-reports/objects/05e6ac1297a1f598ba968f8bd06b5500c794a33f8f446803c28428ecfabbfdd8.txt) · [6256eb206879](../../followup/mixed-reports/objects/6256eb206879218c016607cb9284ad3a8dc1cdb2643068c631489ae336b187c1.txt) · [6e2dc0d6efae](../../followup/mixed-reports/objects/6e2dc0d6efaeaf44f60f64a4b13ee0ee6fc17444899a7f5a3344c4630c3cf72f.txt) (5 total)
Source manifests: [soring-fronts_universal-order-hitting-set-sigma2-collapse](../../workspaces/manifests/soring-fronts_universal-order-hitting-set-sigma2-collapse.json)

## optimal-node-etie-minimax-collision-alln

Can every n be sorted by a height-S(n) optimal decision tree in which no comparison at any reachable state splits that state into two children of equal linear-extension count but unequal true minimax value?

**investigated** · [Full research report](../../fronts/0596-optimal-node-etie-minimax-collision-alln.md)
Intended test or falsifier: Prove that for infinitely many n every height-S(n) sorting tree must use a comparison whose two children are extension-tied yet have different minimax values, or isolate an unavoidable such node on all optimal strategie…
Proposed implication: A positive answer sharply restricts the structure of optimal trees and permits pruning of exhaustive exact evaluators; a negative answer shows harmful extension-ties are unavoidable and must be handled by any exact algo…
Historical reported excerpt (unverified): - **Scope caveat:** results are for the exact comparison-tree minimax model on labeled inputs/poset states (as in the problem); exhaustive results are n≤6, n=7 is sampled/partial — not a proof for all n. Primary literature on exact S(n) (Peczarski 2012; Stober–Weiß 2023; Wells/Knuth/OEIS context pe…
Assistant reports: [ses_e0866ca99ffe5DOvy6P2fXFARk](../../assistant-reports/sessions/ses_e0866ca99ffe5DOvy6P2fXFARk.md)
Original task commissions: [e4bb9169aac7](../../followup/task-commissions/objects/e4bb9169aac7bc8f0e4507d5e2526747a355a0f944edeeb78a6e6d8bafb2bbbf.txt)
Mixed-session reports: [fad44d0341a9](../../followup/mixed-reports/objects/fad44d0341a9053b44a8c8f3e99cfdaa9b94c987387822c972c2e5fc5c93c9cf.txt)
Source manifests: [soring-fronts_optimal-node-etie-minimax-collision-alln](../../workspaces/manifests/soring-fronts_optimal-node-etie-minimax-collision-alln.json)

## optimal-feasible-e-collision-alln

Does the extension-count ambiguity reported for states reachable within S(n) comparisons persist on the optimal-feasible slice, i.e. states P reached from the n-antichain at depth d with d + F(P) &lt;= S(n) and with both outcome branches of every ancestor fitting the remaining budget, so that infinitely many n admit P,Q on a common height-S(n) sorting tree with e(P)=e(Q) but F(P)!=F(Q)?

**investigated** · [Full research report](../../fronts/0597-optimal-feasible-e-collision-alln.md)
Intended test or falsifier: Exhibit two states lying on a common height-S(n) optimal sorting tree with equal linear-extension count and different minimax value for infinitely many n; alternatively single out an all-n reason that F is a function of…
Proposed implication: Persistence would kill any e-indexed evaluator even on the only states relevant to exact S(n); collapse (F e-determined on the slice) would license a compact e-keyed dynamic program over optimal continuations and tighte…
Historical reported excerpt (unverified): Mathematical finding: **persistence holds on the optimal-feasible slice, at least in a simple all-\(n\) family.**
Assistant reports: [ses_e08247f4affeowYWs1ydMMGfVo](../../assistant-reports/sessions/ses_e08247f4affeowYWs1ydMMGfVo.md)
Original task commissions: [39c7876fbe89](../../followup/task-commissions/objects/39c7876fbe89e8a6b84d61b19151da3aa97994bf8a06fc36783b43cf0050123e.txt)
Source manifests: [soring-fronts_optimal-feasible-e-collision-alln](../../workspaces/manifests/soring-fronts_optimal-feasible-e-collision-alln.json)

## superpoly-optimal-feasible-e-collisions

Do 2^{Omega(sqrt(n/log n))} extension-count collisions persist on the optimal-feasible slice for all sufficiently large n, i.e. states on a common height-S(n) sorting tree with equal e(P) but different minimax F(P)?

**investigated** · [Full research report](../../fronts/0598-superpoly-optimal-feasible-e-collisions.md)
Intended test or falsifier: Exhibit an all-n reason that only polynomially many e-values are ambiguous among optimal-feasible states, or show the simple chain family cannot be amplified to superpolynomially many optimal-feasible collisions.
Proposed implication: Settles whether e-indexed dynamic programming over optimal continuations has constant or superpolynomial ambiguity, and thus whether poly-size exceptions can rescue an e-keyed exact evaluator.
Historical reported excerpt (unverified): Mathematical finding: **YES** — the \(2^{\Omega(\sqrt{n/\log n})}\) extension-count collisions do persist on the optimal-feasible slice for all sufficiently large \(n\).
Board: [2026-11-20 message](../../board/301/page-009.md?plain=1#L91) · [2026-11-20 review](../../board/301/page-009.md?plain=1#L125) · [2026-11-20 review](../../board/301/page-009.md?plain=1#L145) · [2026-11-20 message](../../board/301/page-009.md?plain=1#L236)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e07ffedc1ffeu8g2FcMD4BZs7z](../../assistant-reports/sessions/ses_e07ffedc1ffeu8g2FcMD4BZs7z.md)
Original task commissions: [2a6eca03c669](../../followup/task-commissions/objects/2a6eca03c66965c6843728c37f9abbf0b74a654522f62f724763ad30f842b4d3.txt)
Mixed-session reports: [05e6ac1297a1](../../followup/mixed-reports/objects/05e6ac1297a1f598ba968f8bd06b5500c794a33f8f446803c28428ecfabbfdd8.txt)
Source manifests: [soring-fronts_superpoly-optimal-feasible-e-collisions](../../workspaces/manifests/soring-fronts_superpoly-optimal-feasible-e-collisions.json)

## minimax-multiplicity-per-extension-count-optfeasible-alln

For all sufficiently large n, does a single extension count e(P) support superpolynomially many distinct minimax values F(P) among states lying on a common height-S(n) optimal sorting tree?

**investigated** · [Full research report](../../fronts/0601-minimax-multiplicity-per-extension-count-optfeasible-alln.md)
Intended test or falsifier: Construct one extension count with superpolynomially many distinct F-values among optimal-feasible states, or prove the number of such values is polynomially bounded for every count.
Proposed implication: Superpolynomial multiplicity would rule out any e-keyed exact evaluator even with a polynomial-size value set per key; a polynomial bound would leave a weakened e-indexed dynamic program possible.
Historical reported excerpt (unverified): ## Mathematical finding
Board: [2026-11-20 message](../../board/301/page-009.md?plain=1#L236)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e07e17002ffe8Z3qdw4FbGrud6](../../assistant-reports/sessions/ses_e07e17002ffe8Z3qdw4FbGrud6.md)
Original task commissions: [ebb1896386cd](../../followup/task-commissions/objects/ebb1896386cd39292f5a98a513722703195bf92a781a75cd09511cf305ee1568.txt)
Source manifests: [soring-fronts_minimax-multiplicity-per-extension-count-optfeasible-alln](../../workspaces/manifests/soring-fronts_minimax-multiplicity-per-extension-count-optfeasible-alln.json)

## optfeasible-state-multiplicity-per-ef-alln

For all sufficiently large n, does the optimal-feasible slice (states reachable within S(n) comparisons from the n-antichain on a height-S(n) sorting tree) contain superpolynomially many states sharing both the same extension count e(P) and the same minimax value F(P)?

**investigated** · [Full research report](../../fronts/0602-optfeasible-state-multiplicity-per-ef-alln.md)
Intended test or falsifier: Exhibit an infinite family of n with superpolynomially many optimal-feasible states sharing one (e,F) pair but not isomorphic, or prove every (e,F) pair has only polynomially many optimal-feasible states.
Proposed implication: Superpolynomial multiplicity would show an e-and-F-keyed exact dynamic program has superpolynomial ambiguity on the only states relevant to S(n); a polynomial bound would leave compact e+F indexing viable.
Historical reported excerpt (unverified): ## Mathematical finding (partial / negative; no theorem completion)
Assistant reports: [ses_e07c46871ffeueExvpcg1RSDJF](../../assistant-reports/sessions/ses_e07c46871ffeueExvpcg1RSDJF.md)
Original task commissions: [7ea89f4d8c51](../../followup/task-commissions/objects/7ea89f4d8c51ddbbb77c163f1076a352825421b8661a0ba7c10af96e48d6583f.txt)
Mixed-session reports: [e185782c9867](../../followup/mixed-reports/objects/e185782c986752e67d65b9c8e498767beaabe06f023a21925141c614aa95b7ab.txt)
Source manifests: [soring-fronts_optfeasible-state-multiplicity-per-ef-alln](../../workspaces/manifests/soring-fronts_optfeasible-state-multiplicity-per-ef-alln.json)

## intermediate-matching-prefix-cost-alln

For every n &gt;= 2 and every 1 &lt;= k &lt;= floor(n/2), is the exact minimax value F(k disjoint 2-chains disjoint-union A_{n-2k}) equal to S(n) - k, i.e. can any k pairwise-disjoint opening comparisons always be front-loaded at cost exactly k, not only at the full matching prefix k = floor(n/2)?

**investigated** · [Full research report](../../fronts/0607-intermediate-matching-prefix-cost-alln.md)
Intended test or falsifier: A from-scratch exact minimax computation finding any n,k with F(k*C2 disjoint-union A_{n-2k}) != S(n)-k, or showing the value depends on k non-linearly; today's reported identity C(2,n)=S(n)-1 supplies only the k=1 base…
Proposed implication: A uniform equality would give a prefix-front-loading normal form reducing S(n) to intermediate matching-prefix families and opening a faster exact evaluator; a counterexample at some intermediate k would also refute the…
Historical reported excerpt (unverified): The reported from-scratch computation through `n≤6` is supporting finite evidence, not an all-`n` argument. I did not extend it or find a falsifying instance. No repository changes, Lean work, or board post were warranted.
Assistant reports: [ses_e07189f61ffe7T2dXUwhwQEiRg](../../assistant-reports/sessions/ses_e07189f61ffe7T2dXUwhwQEiRg.md)
Original task commissions: [4e72f6cf6a14](../../followup/task-commissions/objects/4e72f6cf6a1473e208bb409a60bd4e1f393af9b94efe28e04f146bbb23965797.txt)
Source manifests: [soring-fronts_intermediate-matching-prefix-cost-alln](../../workspaces/manifests/soring-fronts_intermediate-matching-prefix-cost-alln.json)

## chain-completion-saving-limit-alln

For each fixed m &gt;= 2, let sigma(m) be the limiting saving S(n) - F(C_m disjoint-union A_{n-m}) as n grows. Is sigma(m) = S(m) for every m (maximal saving, matching the reported m=2 identity sigma(2)=1=S(2)), or is m=2 the unique maximizer with sigma(m) strictly below S(m) for all m &gt;= 3?

**investigated** · [Full research report](../../fronts/0608-chain-completion-saving-limit-alln.md)
Intended test or falsifier: Compute F(C_m disjoint-union A_{n-m}) for larger n: from-scratch exact minimax in this pass gives savings m=2:1, m=3:2 at n=5,6, m=4:4 at n=5,6, versus S(m)=1,3,5; confirm or refute that these submaximal savings stabili…
Proposed implication: Determining sigma(m) yields a structural law for how a known sorted m-chain interacts with the bulk antichain; a maximal-saving theorem would give compositional reductions for S(n), while strict submaximality isolates c…
Historical reported excerpt (unverified): ## Finding: no all-\(n\) result
Assistant reports: [ses_e07189d7fffe6KQaUC3JY6hzTR](../../assistant-reports/sessions/ses_e07189d7fffe6KQaUC3JY6hzTR.md)
Original task commissions: [52fdeaa2ab93](../../followup/task-commissions/objects/52fdeaa2ab934e77393db4475658607e353fd35868d9b0d879d29578737103f3.txt)
Source manifests: [soring-fronts_chain-completion-saving-limit-alln](../../workspaces/manifests/soring-fronts_chain-completion-saving-limit-alln.json)

## winning-family-obdd-order-alln

Let W_d be the Boolean function that is true exactly on labelled n-key posets sortable within d adaptive comparisons, encoded by the fixed pair-lex ternary relation bits. Does there exist any fixed variable order under which every W_d has a polynomial-width ordered binary decision diagram uniformly in n and d, or is the minimum width over all orders superpolynomial for an infinite family of (n,d)?

**investigated** · [Full research report](../../fronts/0609-winning-family-obdd-order-alln.md)
Intended test or falsifier: Either exhibit one fixed variable order whose OBDD width is polynomial for all W_d, or prove a superpolynomial width lower bound (e.g. via a fooling-set or rank argument) that holds simultaneously for every variable ord…
Proposed implication: A uniformly polynomial-width, polynomial-time constructible OBDD for the exact winning family would decide SORT-BOUND-U in polynomial time; an all-order width lower bound would rule out the fixed-order decision-diagram …
Historical reported excerpt (unverified): - No repository/Lean changes were made (nothing here meets the publication gate as a new theorem/counterexample resolving the front or a necessary model fix). Any further claim would require either an explicit poly-width order+proof (route 1) or a verified all-order fooling-set/rank lower bound for…
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e0644422effe6YalCTg8PpPf1U](../../assistant-reports/sessions/ses_e0644422effe6YalCTg8PpPf1U.md)
Original task commissions: [5b901d5fcc6c](../../followup/task-commissions/objects/5b901d5fcc6c0eea183c99e0d8eb78549c9a5bdae72ecc226d62381e462c769d.txt)
Mixed-session reports: [e70582fbe904](../../followup/mixed-reports/objects/e70582fbe904334939e0e6f13c1298e6b6594eca5a3366efd5a8cab628e9326d.txt)
Source manifests: [soring-fronts_winning-family-obdd-order-alln](../../workspaces/manifests/soring-fronts_winning-family-obdd-order-alln.json)

## downset-zdd-winning-family-alln

The backward search of Stober and Weiss stores families of down-sets (antichains) of the n-key poset. Can the characteristic family of posets sortable within budget k be represented by a polynomial-size zero-suppressed decision diagram over antichain/down-set variables, uniformly in n and k, or must every such ZDD be superpolynomial under all orderings?

**investigated** · [Full research report](../../fronts/0610-downset-zdd-winning-family-alln.md)
Intended test or falsifier: Produce a fixed variable ordering yielding polynomial-size ZDDs for all budgets n,k, or establish a superpolynomial ZDD-size lower bound via an antichain or fooling-set argument that is independent of the chosen orderin…
Proposed implication: A uniformly polynomial-size ZDD for the winning family would be a compact exact evaluator and a step toward a smaller-class upper bound; a lower bound would close the decision-diagram compression route that the down-set…
Historical reported excerpt (unverified): ## Conclusion (report)
Assistant reports: [ses_e06443f23ffeEcKKlOZNZ7OeAO](../../assistant-reports/sessions/ses_e06443f23ffeEcKKlOZNZ7OeAO.md)
Original task commissions: [827573ddb38f](../../followup/task-commissions/objects/827573ddb38ff984df146417c97c6e1ad5c89dcee2833289ae4bb414081d99fb.txt)
Source manifests: [soring-fronts_downset-zdd-winning-family-alln](../../workspaces/manifests/soring-fronts_downset-zdd-winning-family-alln.json)

## one-outcome-attainment-set-alln

Wells-style one-outcome (single-successor) adversary search is reported to certify exact optimality at n=12 but to fail at n=13 and n=14. Is the set of n for which such a restricted adversary search attains the full minimax value S(n) finite, with a characterizable largest element, or are there infinitely many n beyond the small cases where it still attains S(n)?

**investigated** · [Full research report](../../fronts/0611-one-outcome-attainment-set-alln.md)
Intended test or falsifier: Prove finiteness by showing one-outcome search is strictly below S(n) for every n at or above some explicit threshold, or exhibit an infinite family of larger n at which the restricted adversary attains S(n).
Proposed implication: A characterization would be a structural theorem about when the two-branch minimax game collapses to a single adversary path, refining certificate-size understanding; it does not by itself yield a complexity-class separ…
Historical reported excerpt (unverified): **Conclusion (honest, checkable):** Under the MEOO formalization matching the cited Wells/Peczarski behavior, the set is **not** finite with largest element 12 and **not** confined to the small cases (refuted by `20,21,22 ∈ A` via the all-`n` ITLB theorem). A complete dichotomy “finite with a chara…
Assistant reports: [ses_e06443d07ffeCLo9EuZY4FTexV](../../assistant-reports/sessions/ses_e06443d07ffeCLo9EuZY4FTexV.md)
Original task commissions: [f1666b4c3666](../../followup/task-commissions/objects/f1666b4c36661ceb19be287113ab72215595c182be375091f4493ba49d5fcd61.txt)
Source manifests: [soring-fronts_one-outcome-attainment-set-alln](../../workspaces/manifests/soring-fronts_one-outcome-attainment-set-alln.json)

## critical-optimal-tree-parity

For unary n, let N(n) be the number of distinct height-S(n) deterministic adaptive comparison decision trees that correctly sort all n labelled keys (counted up to a fixed labelled-tree equivalence). Is the parity of N(n), or N(n) mod any fixed prime, computable in polynomial time in n, or is every such fixed modular residue of the critical-tree count as hard to compute as S(n) itself? This is about the count of optimal sorters, not the parity of the value S(n).

**investigated** · [Full research report](../../fronts/0619-critical-optimal-tree-parity.md)
Intended test or falsifier: Settle it either way: exhibit a uniform polynomial-time algorithm computing N(n) mod 2 (or mod a fixed prime) for all n from unary n, or prove that computing any fixed modular residue of N(n) is Turing-equivalent to, or…
Proposed implication: A fast modular-residue algorithm would be a new upper bound on a tally function derived from the optimal-sorter space and could seed a compact arithmetic/nondeterministic route toward the open NP-membership question for…
Historical reported excerpt (unverified): **For your review:** do you want me to post a single concise inconclusive-outcome note to board #301 for this front? If so I will post exactly one; otherwise I will leave the board untouched. The front remains `running` in the ledger, which is the keeper/executive's disposition to make, not mine.
Assistant reports: [ses_e055f95f4ffej7bx1R7B8Zl5UO](../../assistant-reports/sessions/ses_e055f95f4ffej7bx1R7B8Zl5UO.md)
Original task commissions: [78e886a04359](../../followup/task-commissions/objects/78e886a04359ff85111cb0b948ef4b80e01f9eb4991bfe498343b79e8f2bd852.txt)
Source manifests: [soring-fronts_critical-optimal-tree-parity](../../workspaces/manifests/soring-fronts_critical-optimal-tree-parity.json)

## signflip-cross-rule-optimality-alln

For every n, is the sign-flipped cross comparison rule optimal for the adversary in all reachable optimal plays from the n-element antichain root?

**investigated** · [Full research report](../../fronts/0623-signflip-cross-rule-optimality-alln.md)
Intended test or falsifier: Give a reachable composition where the sign-flipped rule is strictly suboptimal in cross charge, or prove universal sign-flip optimality for all n.
Proposed implication: Universal sign-flip optimality would give a uniform cross-charge strategy for exact unary evaluation; failure would require strategy-specific cross rules.
Historical reported excerpt (unverified): ## Mathematical finding — falsifier for the sign-flipped cross rule
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e044e1795ffenKV2E0s7RTWmTQ](../../assistant-reports/sessions/ses_e044e1795ffenKV2E0s7RTWmTQ.md)
Original task commissions: [d34a8b8d12b1](../../followup/task-commissions/objects/d34a8b8d12b1f5abf9a82efcbc7e9abb3797370147d8b2802895aca241b2ee0d.txt)
Mixed-session reports: [f4513a763c58](../../followup/mixed-reports/objects/f4513a763c58ad748b28c6a77a10b08c11c819217899390e598714ef7fccb665.txt)
Source manifests: [soring-fronts_signflip-cross-rule-optimality-alln](../../workspaces/manifests/soring-fronts_signflip-cross-rule-optimality-alln.json)

## increment-log-upper-alln

Prove or refute: for every n &gt;= 2, S(n+1) - S(n) &lt;= ceil(log2(n+1)), so increments in the exact optimal count stay bounded by the information growth of one new key.

**investigated** · [Full research report](../../fronts/0628-increment-log-upper-alln.md)
Intended test or falsifier: A certified n with S(n+1) - S(n) &gt; ceil(log2(n+1)), via a certified depth of n+1 beyond S(n) + ceil(log2(n+1)).
Proposed implication: A stable increment bound constrains DP recurrences and certificate arithmetic for the exact evaluation of S(n).
Historical reported excerpt (unverified): ## Outcome already reported (for the record)
Board: [2026-11-21 message](../../board/301/page-007.md?plain=1#L201) · [2026-11-21 message](../../board/301/page-007.md?plain=1#L418)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e03e2306effeMFxOgXJLepG7th](../../assistant-reports/sessions/ses_e03e2306effeMFxOgXJLepG7th.md)
Original task commissions: [873366302794](../../followup/task-commissions/objects/8733663027941c11f7a25d33439272021a64cd9a8f67565319a4aaa429fe9b78.txt)
Mixed-session reports: [5ba4b11a936c](../../followup/mixed-reports/objects/5ba4b11a936c18a4b9f0ca1c64baf8717656ebbdf5cc1e8d2d97a228f8c9307a.txt) · [ec9a4878be48](../../followup/mixed-reports/objects/ec9a4878be48a82392e6a8e0b912db1f3fb99fe9726849714d64348a7fc22cbd.txt)
Source manifests: [soring-fronts_increment-log-upper-alln](../../workspaces/manifests/soring-fronts_increment-log-upper-alln.json)

## ff-optimal-window-23-30-alln

Does there exist n in \[23,30\] with S(n) &lt; FJ(n), i.e., a Ford-Johnson-optimality failure, or is the Ford-Johnson bound optimal for every n in this window?

**investigated** · [Full research report](../../fronts/0629-ff-optimal-window-23-30-alln.md)
Intended test or falsifier: A certified n in \[23,30\] with S(n) &lt; FJ(n), or an optimal sorting tree for some n in \[23,30\] with height below FJ(n).
Proposed implication: A small-n failure pins where optimal comparison counts first diverge from the FJ formula; consistent with Manacher's infinite failures (board #301: first at 47).
Historical reported excerpt (unverified): ## Finding (honest)
Assistant reports: [ses_e03e22e84ffeYxF1H5ML6O6J55](../../assistant-reports/sessions/ses_e03e22e84ffeYxF1H5ML6O6J55.md)
Original task commissions: [65cdfc10c917](../../followup/task-commissions/objects/65cdfc10c9174563ffb466fbdff3d8271e647882444b23a8125f13c3d1cb9611.txt)
Source manifests: [soring-fronts_ff-optimal-window-23-30-alln](../../workspaces/manifests/soring-fronts_ff-optimal-window-23-30-alln.json)

## signflip-larger-e-optimality-alln

Does the larger_e tie-break make the sign-flipped cross rule an optimal adversary for every disjoint composition A⊔B, or is there an all-n family where it forces strictly less than F(A⊔B)?

**investigated** · [Full research report](../../fronts/0636-signflip-larger-e-optimality-alln.md)
Intended test or falsifier: Prove by induction using extension counts that larger_e always attains F(A⊔B), or exhibit an infinite family of disjoint unions where its forced depth is below the minimax value.
Proposed implication: Optimality would supply an all-n adversary construction for parallel compositions and support lower-bound certificates; failure would show no simple extension-count tie-break suffices.
Historical reported excerpt (unverified): The central question remains open: whether *any* simple extension-count-style tie-break (or a different all-n score ranking answers by global F without computing F) attains `F(A ⊔ B)` for every disjoint union.
Board: [2026-11-21 message](../../board/301/page-007.md?plain=1#L909)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e035dc5e7ffeCQEAlfRnniilaV](../../assistant-reports/sessions/ses_e035dc5e7ffeCQEAlfRnniilaV.md)
Original task commissions: [a5003fae3501](../../followup/task-commissions/objects/a5003fae350137da99c884c2bc24c1d6f70c2be1cf9bb0e4734ece868a25ecab.txt) · [af3128f8430e](../../followup/task-commissions/objects/af3128f8430ee7e3784a520a50958a6500cab064b0e557bb5b5ea439277bab27.txt)
Mixed-session reports: [35a08dc4d003](../../followup/mixed-reports/objects/35a08dc4d003a442120c0f4946846bca66b10aca7ed3b6e1bd5682de95ac0800.txt) · [a47f1f20509e](../../followup/mixed-reports/objects/a47f1f20509e46428bac25355acee3481e3015286768eaaccfc90c9ae969152e.txt)
Source manifests: [soring-fronts_signflip-larger-e-optimality-alln](../../workspaces/manifests/soring-fronts_signflip-larger-e-optimality-alln.json)

## insertion-number-uniform-complexity-alln

Is the exact chain-host insertion number I(a,b) = F(C_b disjoint-union A_a) - the minimax comparisons to place a free keys into a known sorted b-chain, which the 2026-11-21T10:20Z board result identifies as the extremal disjoint-union defect envelope max_B delta(A_a,B) - computable by a uniform algorithm in time polynomial in a+b for every a,b &gt;= 1?

**investigated** · [Full research report](../../fronts/0641-insertion-number-uniform-complexity-alln.md)
Intended test or falsifier: Exhibit an infinite family (a_i,b_i) with a proved superpolynomial or #P-hard lower bound for computing the exact value of F(C_{b_i} disjoint-union A_{a_i}), or a state-space lower bound exceeding (a+b)^{O(1)} for every…
Proposed implication: A polynomial-time evaluator for I(a,b) would make the insertion upper bound S(n) &lt;= S(b) + I(n-b,b) uniformly computable without minimax search, sharpening the active upper-bound frontier for exact unary S(n); a hardnes…
Historical reported excerpt (unverified): **Conclusion:** the investigation was already delivered — the decisive finding (that `I(a,1)=S(a+1)` collapses the front to the flagship `S_unary ∈ FP` problem, so both falsifier horns require `P≠PSPACE`/a Mahaney-type collapse) was posted with full soundness/completeness caveats and honest limits.…
Board: [2026-11-21 message](../../board/301/page-006.md?plain=1#L421) · [2026-11-21 message](../../board/301/page-006.md?plain=1#L443)
Assistant reports: [ses_e025a60e5ffe1zbQRu6SU7bW0J](../../assistant-reports/sessions/ses_e025a60e5ffe1zbQRu6SU7bW0J.md)
Original task commissions: [32223c431eb2](../../followup/task-commissions/objects/32223c431eb2ea66f376cc2fc95e2d4578f487323acacc8dc458c45d0cf43f01.txt)
Mixed-session reports: [cf77d08943b0](../../followup/mixed-reports/objects/cf77d08943b061e3425ed4ac5504f2d21d90f553a1a5965c16441cc6024b231f.txt) · [f8532a700ee6](../../followup/mixed-reports/objects/f8532a700ee6c011a9455a79a746cf779e7ae701ce57f783bb7cde9c1edd7531.txt)
Source manifests: [soring-fronts_insertion-number-uniform-complexity-alln](../../workspaces/manifests/soring-fronts_insertion-number-uniform-complexity-alln.json)

## power2-host-insertion-universality-alln

For every b with b+1 a power of two and EVERY b-element host poset B, including information-excess non-tight hosts, is the one-key insertion defect delta(A_1,B)=F(B disjoint-union A_1)-F(B) exactly ceil(log2(b+1)), or can a non-tight host fall strictly below that chain insertion value at some b=2^m-1?

**investigated** · [Full research report](../../fronts/0645-power2-host-insertion-universality-alln.md)
Intended test or falsifier: Exhibit b=2^m-1 and a non-tight b-element poset B with delta(A_1,B) &lt;= ceil(log2(b+1))-1, backed by a certified upper strategy for the union and a certified lower bound for F(B).
Proposed implication: An exact all-host insertion formula at power-of-two sizes would sharpen the universal defect envelope used by insertion-based exact evaluators; a shortfall would isolate excess-amplified shortcuts and refine lower-bound…
Historical reported excerpt (unverified): ## Result on the front
Assistant reports: [ses_e01b0a6aaffempkL1GpuxNuJeK](../../assistant-reports/sessions/ses_e01b0a6aaffempkL1GpuxNuJeK.md)
Original task commissions: [13c47f731dbd](../../followup/task-commissions/objects/13c47f731dbd80ecbd1ba4855670a1086cee941e5f87e83b489ea2c1a239d1e7.txt)
Mixed-session reports: [ca733265039e](../../followup/mixed-reports/objects/ca733265039ef39cc9790075a7723a4b74444de4dc547aa9841c97ae53ecab05.txt)
Source manifests: [soring-fronts_power2-host-insertion-universality-alln](../../workspaces/manifests/soring-fronts_power2-host-insertion-universality-alln.json)

## cross-cost-additivity-ceiling-alln

For the exact adaptive minimax F, how far can the additive cross-cost lower bound fail? Determine whether the deficit D(a,b,B)=F(B)+ceil(log2 binomial(a+b,a))-F(C_a disjoint-union B) is bounded by a constant over all a,b&gt;=1 with a+b&gt;=3 and all b-element posets B, or grows without bound; here C_a is a chain and the fresh board theorem only gives a cross-comparison count on some path, not additivity with F(B).

**investigated** · [Full research report](../../fronts/0649-cross-cost-additivity-ceiling-alln.md)
Intended test or falsifier: Exhibit a chain C_a and poset B with F(C_a disjoint-union B) at most F(B)+ceil(log2 binomial(a+b,a))-2, from an independent exact minimax computation, or prove the deficit is unbounded above over all a,b.
Proposed implication: Fixes the exact reach of additive 'internal cost plus cross-cost' lower bounds for disjoint unions: a bounded deficit would salvage a sharpened decomposition recursion for exact S(n), while unbounded growth rules out th…
Historical reported excerpt (unverified): ## Mathematical finding
Board: [2026-11-21 message](../../board/301/page-005.md?plain=1#L355)
Additional board mentions: 3 (use front lookup for exact links)
Assistant reports: [ses_e00ede60effe1CZR7o6HqCXrpk](../../assistant-reports/sessions/ses_e00ede60effe1CZR7o6HqCXrpk.md)
Original task commissions: [43e83d1db808](../../followup/task-commissions/objects/43e83d1db808b7acf302f0d4b83ec55c6b1e2fedd449250d3f7a088dbe1618f1.txt)
Mixed-session reports: [e348058d28f2](../../followup/mixed-reports/objects/e348058d28f2e80033022f76cac125b6c333ab07f5b180e7a3ce2d03e5fa2416.txt) · [e5d5ab9ce1e7](../../followup/mixed-reports/objects/e5d5ab9ce1e7651bc36b369a75504a51aefcae2ae63bc1e374b6ebc7035ea646.txt)
Source manifests: [soring-fronts_cross-cost-additivity-ceiling-alln](../../workspaces/manifests/soring-fronts_cross-cost-additivity-ceiling-alln.json)

## hybrid-binary-permutation-test-set-alln

Since binary orders alone apparently cannot certify the exact sorting number (B(n) &lt; S(n) on the computed range), let h(n) be the least number of distinct-key permutations which, together with all 2^n binary orders, force every height-below-S(n) comparison program to fail. Is h(n) bounded by a polynomial in n for all n, or must h(n) grow superpolynomially?

**investigated** · [Full research report](../../fronts/0659-hybrid-binary-permutation-test-set-alln.md)
Intended test or falsifier: Exhibit, for each n, a polynomial-size permutation set P_n such that any program sorting all binary orders and P_n has height at least S(n); or derive a 2^{Omega(n)} lower bound on h(n) by an adversarial restriction arg…
Proposed implication: A polynomial h(n), combined with a polynomial-size optimal program, would open a sample-based NP-style verification route; a superpolynomial h(n) would close the hybrid binary-plus-permutation test route. Neither outcom…
Historical reported excerpt (unverified): **Mathematical finding (not a theorem completion).**
Board: [2026-11-21 message](../../board/301/page-005.md?plain=1#L820) · [2026-11-21 review](../../board/301/page-005.md?plain=1#L885)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_dffd22710ffeVuyEnBK876aHkD](../../assistant-reports/sessions/ses_dffd22710ffeVuyEnBK876aHkD.md)
Original task commissions: [82d6a5d17177](../../followup/task-commissions/objects/82d6a5d17177c6b32593c18d54810ee24a65cf88ef957960b72e29f2724e06bb.txt)
Mixed-session reports: [968a67007218](../../followup/mixed-reports/objects/968a670072187cdd7d7662359e0597a843e7b8e44e4cfd21b2e2b2909a8083ee.txt)
Source manifests: [soring-fronts_hybrid-binary-permutation-test-set-alln](../../workspaces/manifests/soring-fronts_hybrid-binary-permutation-test-set-alln.json)

## binary-minimax-additive-constant-alln

Does the exact binary minimax B(n) admit a universal additive constant C with B(n) &lt;= n + C for every n, or does B(n) - n grow without bound (for instance on the order of ceil(log2 n)) even though lim B(n)/n = 1 is now settled?

**investigated** · [Full research report](../../fronts/0662-binary-minimax-additive-constant-alln.md)
Intended test or falsifier: An infinite family of n with certified lower bounds B(n) &gt;= n + ceil(log2 n), i.e. a provably diverging B(n)-n; the construction n-1+ceil log2(n-1) is only an upper bound and does not settle boundedness.
Proposed implication: Settles the exact additive constant of the simplest nontrivial restricted universe and calibrates how far binary-order minimax sits from S(n); this is a restricted-family value question and yields no SORT-BOUND-U placem…
Historical reported excerpt (unverified): RESULT posted to #301 2026-11-22T00:09:02Z. Theorem proved (paper proof + exhaustive lemma check n&lt;=7): for all n&gt;=3, (n-2)+ceil(log2 n) &lt;= B(n) &lt;= (n-1)+ceil(log2(n-1)), so B(n)-n = ceil(log2 n)-2+eps(n), eps in {0,1}, and B(n)-n -&gt; infinity. Lower bound: adversary answers YES for first n-2 compar…
Board: [2026-11-22 message](../../board/301/page-004.md?plain=1#L3) · [2026-11-22 review](../../board/301/page-004.md?plain=1#L90)
Assistant reports: [ses_dff82fe27ffeFN0dTDsLkCZWL2](../../assistant-reports/sessions/ses_dff82fe27ffeFN0dTDsLkCZWL2.md)
Original task commissions: [9b409bf34293](../../followup/task-commissions/objects/9b409bf342933569deb3b9571a5e4bd5bcf090602349dfaba1db82ae458f9ec3.txt)
Mixed-session reports: [a84f8e0d8739](../../followup/mixed-reports/objects/a84f8e0d873956f597e5f5f9d8e6c608484b1b8f9a54d5c14c31d03ee13462dc.txt) · [d33a5c96cfa7](../../followup/mixed-reports/objects/d33a5c96cfa77aa1fac93cd8c238b4114bffc362160c7f1689e415cdb3a4d48e.txt)
Source manifests: [soring-fronts_binary-minimax-additive-constant-alln](../../workspaces/manifests/soring-fronts_binary-minimax-additive-constant-alln.json)

## exact-descent-saturation-threshold-alln

Let d_sat(n) = min{d : F_d(n) = S(n)} be the least descent bound at which the restricted universe already attains the full sorting number. Is d_sat(n) = Theta(n/log n) for all n, matching the information-transition point where n log2(d+1) first reaches log2(n!)?

**investigated** · [Full research report](../../fronts/0663-exact-descent-saturation-threshold-alln.md)
Intended test or falsifier: A certified n with F_d(n) = S(n) for some d = o(n/log n), or a certified n with F_d(n) &lt; S(n) for every d = O(n/log n); small-n data such as F_3(6)=F_5(6)=10 cannot decide the all-n claim.
Proposed implication: An all-n d_sat characterization sharpens the proven descent transition from asymptotic tightness to exact equality and identifies the smallest restricted universe whose minimax equals S(n), narrowing where the hard part…
Historical reported excerpt (unverified): **Unfinished work:** none for this front’s requested action. The mathematical result is already reported: the proposed `d_sat(n)=Θ(n/log n)` claim is refuted; the proof gives `d_sat(n)=Ω(n)` (in fact `Θ(n)`), with the constant in `\[1/(4e),1\]` left open. `S(n)`/`SORT-BOUND-U` remain open. No further…
Board: [2026-11-22 review](../../board/301/page-004.md?plain=1#L53) · [2026-11-21 message](../../board/301/page-005.md?plain=1#L1161)
Assistant reports: [ses_dff82fc7bffeFbbINFlvjaShWF](../../assistant-reports/sessions/ses_dff82fc7bffeFbbINFlvjaShWF.md)
Original task commissions: [b5c250233c3c](../../followup/task-commissions/objects/b5c250233c3c393f545dd6943bb9212b17b1a67b12f5c6c5b862b4fda5f37b10.txt)
Mixed-session reports: [a84f8e0d8739](../../followup/mixed-reports/objects/a84f8e0d873956f597e5f5f9d8e6c608484b1b8f9a54d5c14c31d03ee13462dc.txt) · [d33a5c96cfa7](../../followup/mixed-reports/objects/d33a5c96cfa77aa1fac93cd8c238b4114bffc362160c7f1689e415cdb3a4d48e.txt)
Source manifests: [soring-fronts_exact-descent-saturation-threshold-alln](../../workspaces/manifests/soring-fronts_exact-descent-saturation-threshold-alln.json)

## t4-uniform-base-exhaustive-alln

For every n and every poset P on any number of elements with e(P) &lt;= 16, is m(P) &lt;= 4? Extend the certified uniform base: enumerate exhaustively on n = 7 (and propose n = 8) for a poset P with 13 &lt;= e(P) &lt;= 16 and m(P) &gt;= 5, using a written minimax-exact solver; if none exists, state that every poset with e(P) &lt;= 16 has m(P) &lt;= 4 as the deliverable.

**blocked** · [Full research report](../../fronts/0668-t4-uniform-base-exhaustive-alln.md)
Intended test or falsifier: Exhibit a poset P with e(P) &lt;= 16 and m(P) &gt;= 5, or prove every poset with e(P) &lt;= 16 has m(P) &lt;= 4 (i.e. extend T(4) = 12 to all n). Provide the poset or the proof, with an independent solver cross-check.
Proposed implication: A uniform base beyond e &lt;= 7 at budget 4 strengthens the exact S(n) backward-search pruning table; a negative result sharpens the uniform-base structure of the local pruning criterion.
Historical reported excerpt (unverified): I'm on `billy-dev`. The repo's own verified witness is `H2_P1 = (20,16,0,23,0,22)` (n=6, e=13, m=5) — which already breaks the claim "every poset with `e(P) ≤ 16` has `m(P) ≤ 4`" if true. Per the FRONT task I need an **independent solver** to attack the claim: verify the witness, cross-check e/m co…
Assistant reports: [ses_dff2fa6f7ffeN3wKBr0mS4Eo5g](../../assistant-reports/sessions/ses_dff2fa6f7ffeN3wKBr0mS4Eo5g.md)
Original task commissions: [5b3af82f6443](../../followup/task-commissions/objects/5b3af82f64430731423781a3f667b70c7fb6d6661a9cff97baeb159680a56981.txt)
Mixed-session reports: [18de4807e457](../../followup/mixed-reports/objects/18de4807e457779e15da84cb1940d8b24105d34d2a5a8c9648c5d194d2772075.txt)
Source manifests: [soring-fronts_t4-uniform-base-exhaustive-alln](../../workspaces/manifests/soring-fronts_t4-uniform-base-exhaustive-alln.json)

## t5-uniform-base-extension-alln

Is the uniform base T(5) = 29, i.e. does every poset P on any number of elements with e(P) &lt;= 29 have m(P) &lt;= 5, with the base attained by some poset with e(P) &gt;= 30? Enumerate exhaustively on n = 7 (and propose n = 8) for any poset with 30 &lt;= e(P) &lt;= 32 and m(P) &gt;= 6, or state T(5)=29 as the deliverable if none exist.

**blocked** · [Full research report](../../fronts/0669-t5-uniform-base-extension-alln.md)
Intended test or falsifier: Exhibit a poset P with e(P) &gt;= 30 and m(P) &gt;= 6, or prove every poset with e(P) &lt;= 29 has m(P) &lt;= 5 (extending the n &lt;= 6 certificate of T(5) = 29). Provide the poset or the proof with an independent solver cross-check.
Proposed implication: Sharp uniform bases at budgets 4 and 5 strengthen the exact S(n) backward-search pruning table and give the local analysis of where non-tightness can first arise (local solve of budgeted pruning).
Historical reported excerpt (unverified): No final text; audit needed
Board: [2026-11-22 message](../../board/301/page-004.md?plain=1#L354)
Assistant reports: [ses_dff2fa562ffeIUANkmWthBpBAp](../../assistant-reports/sessions/ses_dff2fa562ffeIUANkmWthBpBAp.md)
Original task commissions: [ed73e27de0d2](../../followup/task-commissions/objects/ed73e27de0d24d19637771b8a93a16e73619b689fbc7e67e70a3f26e6cd77020.txt)
Mixed-session reports: [18de4807e457](../../followup/mixed-reports/objects/18de4807e457779e15da84cb1940d8b24105d34d2a5a8c9648c5d194d2772075.txt) · [30e759f43f3e](../../followup/mixed-reports/objects/30e759f43f3ee3b0894e666d68a36006d08e1af8ddf2039b8d9d4b3ab8bb3b9d.txt) · [75cd8a4e8161](../../followup/mixed-reports/objects/75cd8a4e816164fb5c163216dbc9962fce6a6d0b6a4333032e479b7e7bce79be.txt) (7 total)
Source manifests: [soring-fronts_t5-uniform-base-extension-alln](../../workspaces/manifests/soring-fronts_t5-uniform-base-extension-alln.json)

## winning-frontier-peak-at-exact-budget-alln

For n and t &lt;= S(n), let W_t(n) be the number of nonisomorphic reachable posets P at depth t that satisfy F(P) &lt;= S(n)-t (winning at remaining budget). Is the maximum over t of W_t(n) always attained at t = S(n) (the exact-budget frontier), or does there exist an infinite family of n where the winning frontier peaks at depth strictly below S(n)?

**blocked** · [Full research report](../../fronts/0675-winning-frontier-peak-at-exact-budget-alln.md)
Intended test or falsifier: Exhibit n_i where max_t W_t(n_i) is attained at some t_i &lt; S(n_i) by a margin (e.g. W_{S(n_i)-1}/W_{t_i} &lt; 1/2 for arbitrarily large n_i), or prove W_{S(n)} &gt;= max_t W_t for all sufficiently large n.
Proposed implication: If the frontier peaks at the exact budget, exact-budget certificates are load-bearing for the winning-frontier barriers; an earlier-peak family would suggest exact-budget state counts are surplus to earlier-depth counts…
Historical reported excerpt (unverified): Now reading the operations doc (board #301), the winning-frontier barrier doc, literature, and the frontier state.
Assistant reports: [ses_dff21a02dffevL44a6QgMsnp6u](../../assistant-reports/sessions/ses_dff21a02dffevL44a6QgMsnp6u.md)
Original task commissions: [bfc0c173cc57](../../followup/task-commissions/objects/bfc0c173cc578a4461756555d86156371470170e258585f83739b40eab7e1d41.txt)
Source manifests: [soring-fronts_winning-frontier-peak-at-exact-budget-alln](../../workspaces/manifests/soring-fronts_winning-frontier-peak-at-exact-budget-alln.json)

## winning-frontier-peak-two-thirds-s-alln

For all n, if W_t(n) counts nonisomorphic posets reachable from the n-antichain in exactly t comparisons with F(P) &lt;= S(n)-t, is the maximum of W_t(n) over t attained at t = floor(2*S(n)/3)?

**investigated** · [Full research report](../../fronts/0680-winning-frontier-peak-two-thirds-s-alln.md)
Intended test or falsifier: Compute W_t(n) for n=6 or larger and find a peak t differing from floor(2*S(n)/3); the n&lt;=5 data have peaks at t=2,3,4 for S=3,5,7.
Proposed implication: The peak location determines the largest meet-in-the-middle frontier size for exact evaluators; a predictable peak would guide bidirectional search, while a mismatch exposes new growth in the winning frontier.
Historical reported excerpt (unverified): ## Mathematical finding
Board: [2026-11-22 message](../../board/301/page-004.md?plain=1#L447)
Assistant reports: [ses_dfea8b156ffeZw389P2QAF0JQv](../../assistant-reports/sessions/ses_dfea8b156ffeZw389P2QAF0JQv.md)
Original task commissions: [b7ed9369f93e](../../followup/task-commissions/objects/b7ed9369f93e34f6b2f77593bfad318a80a5652909a9ddb8908e5cbbea4de8f0.txt)
Mixed-session reports: [30e759f43f3e](../../followup/mixed-reports/objects/30e759f43f3ee3b0894e666d68a36006d08e1af8ddf2039b8d9d4b3ab8bb3b9d.txt) · [75cd8a4e8161](../../followup/mixed-reports/objects/75cd8a4e816164fb5c163216dbc9962fce6a6d0b6a4333032e479b7e7bce79be.txt) · [92d08909f210](../../followup/mixed-reports/objects/92d08909f210980f1a3fada3f2c5eb1c94e67cfd8cda386bf31c4382d95755e9.txt) (5 total)
Source manifests: [soring-fronts_winning-frontier-peak-two-thirds-s-alln](../../workspaces/manifests/soring-fronts_winning-frontier-peak-two-thirds-s-alln.json)

## optimal-move-extension-monotonicity-alln

For every n, does the n-element antichain admit a height-S(n) sorting strategy such that at every reachable optimal state P with m(P) &gt;= 2, the chosen optimal comparison sends at least as many linear extensions to its minimax-harder child as to its easier child (no sibling extension inversion anywhere on optimal play)? This sharpens the board 04:48Z observation that such inversions occur only off-budget.

**investigated** · [Full research report](../../fronts/0682-optimal-move-extension-monotonicity-alln.md)
Intended test or falsifier: Exhibit, for some n, a poset state P reachable from A_n on optimal play with m(P) &gt;= 2 at which EVERY minimax-optimal comparison strictly sends fewer linear extensions to the harder child than to the easier child; or pr…
Proposed implication: A positive all-n answer supplies a canonical extension-monotone optimal strategy, supporting compact certificate normal forms and extension-order-guided pruning in exact evaluators of unary S(n); a refutation is a struc…
Historical reported excerpt (unverified): ## Mathematical finding
Board: [2026-11-22 message](../../board/301/page-004.md?plain=1#L514)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_dfe5fdcfaffeIYkWQOemkOel4z](../../assistant-reports/sessions/ses_dfe5fdcfaffeIYkWQOemkOel4z.md)
Original task commissions: [727940e3c66a](../../followup/task-commissions/objects/727940e3c66a298cb736629ed366af805ea787fe64d350fc21dd94c72b5c2f58.txt)
Source manifests: [soring-fronts_optimal-move-extension-monotonicity-alln](../../workspaces/manifests/soring-fronts_optimal-move-extension-monotonicity-alln.json)

## extension-inversion-decision-complexity-alln

For an explicit n-element poset P given by its transitive reduction, determine the complexity for all n of deciding whether P has any sibling extension inversion (a minimax-optimal comparison whose minimax-harder child has strictly fewer linear extensions than its easier child), and of deciding whether P is all-inverted.

**investigated** · [Full research report](../../fronts/0683-extension-inversion-decision-complexity-alln.md)
Intended test or falsifier: Give a polynomial-time algorithm for either decision problem, or a reduction from exact linear-extension counting (#P) or 3-SAT showing that inversion detection is #P-hard or NP-hard uniformly for all n.
Proposed implication: The complexity of recognizing the newest board result's inversion predicate governs whether extension-inversion-based pruning and canonical monotone strategies can be applied algorithmically; hardness would bar cheap de…
Historical reported excerpt (unverified): ## Mathematical finding
Board: [2026-11-22 message](../../board/301/page-004.md?plain=1#L536)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_dfe39d021ffe7z1xldKtsQpRaq](../../assistant-reports/sessions/ses_dfe39d021ffe7z1xldKtsQpRaq.md)
Original task commissions: [a655b2129d0f](../../followup/task-commissions/objects/a655b2129d0f079f4ef1d9f52343f278381c587ed4efec8bf7807299bb82203e.txt)
Source manifests: [soring-fronts_extension-inversion-decision-complexity-alln](../../workspaces/manifests/soring-fronts_extension-inversion-decision-complexity-alln.json)

## inversion-density-per-path-alln

For all n, does there exist a height-S(n) sorting strategy in which the number of sibling extension inversions along every root-to-leaf adversary path is bounded by a universal constant, or conversely is there an infinite family of n forcing Omega(S(n)) inversion comparisons on every height-S(n) strategy?

**investigated** · [Full research report](../../fronts/0685-inversion-density-per-path-alln.md)
Intended test or falsifier: Exhibit for infinitely many n a family where every height-S(n) strategy has some adversary path containing omega(1), or Omega(S(n)), inversion comparisons, or prove a uniform O(1) per-path inversion bound.
Proposed implication: This separates a purely local normal form (one monotone option at each state) from a global one (few inversions per execution), determining how strong a canonical strategy and safe pruning rule the newest inversion-free…
Historical reported excerpt (unverified): ## Mathematical finding
Board: [2026-11-22 message](../../board/301/page-004.md?plain=1#L584)
Assistant reports: [ses_dfe39cc4effeQLDepI3Kr9V2yR](../../assistant-reports/sessions/ses_dfe39cc4effeQLDepI3Kr9V2yR.md)
Original task commissions: [700e16050ac2](../../followup/task-commissions/objects/700e16050ac274230d73c64504ed75a714f06f2b83d759b48720691c253ef7a3.txt)
Source manifests: [soring-fronts_inversion-density-per-path-alln](../../workspaces/manifests/soring-fronts_inversion-density-per-path-alln.json)

## per-key-comparison-load-optimal-alln

Let Lambda(n) be the least L such that some height-S(n) correct sorting tree on n labelled keys has every key compared at most L times on every root-to-leaf path (the Omega(log n) lower bound from rank determination is immediate). Is Lambda(n) &lt;= c*log n for all n and a fixed c, or does an infinite family force some key into omega(log n) comparisons on some path of every height-S(n) tree?

**investigated** · [Full research report](../../fronts/0689-per-key-comparison-load-optimal-alln.md)
Intended test or falsifier: Compute Lambda(n) exactly with a load-augmented minimax solver for n=6,7 and exhibit an n where every height-S(n) tree has a key of load greater than c*log n, or exhibit for all n a height-S(n) tree with per-key load O(…
Proposed implication: An O(log n) per-key load normal form is a new local structural restriction usable toward polynomial-size succinct strategy certificates (the live NP/coNP frontier for SORT-BOUND-U); an omega(log n) lower bound rules out…
Historical reported excerpt (unverified): ## Mathematical finding
Board: [2026-11-22 message](../../board/301/page-004.md?plain=1#L684)
Assistant reports: [ses_dfde42eabffev0jQ191wWDTeBC](../../assistant-reports/sessions/ses_dfde42eabffev0jQ191wWDTeBC.md)
Original task commissions: [5ee55eca04d1](../../followup/task-commissions/objects/5ee55eca04d1ba1847bd6d8434a85e8f6d12f14fa3f3699014ba9cdaeb08361f.txt)
Mixed-session reports: [e3b778fa956e](../../followup/mixed-reports/objects/e3b778fa956e55df82368cd7e1b14bbc12104a255a510b24fc2b5366c2f9e061.txt)
Source manifests: [soring-fronts_per-key-comparison-load-optimal-alln](../../workspaces/manifests/soring-fronts_per-key-comparison-load-optimal-alln.json)

## structural-bound-allornothing-alln

For every n and every state reachable on some height-S(n) optimal path from the n-antichain, is the project's Theorem B structural lower bound B(P) = sum_i ceil(log2 e(P_i)) + sum_i delta_i always either exactly F(P) or exactly ceil(log2 e(P)), i.e. can the certified series-decomposition merge gaps ever produce a bound strictly between the information bound and the exact minimax value?

**investigated** · [Full research report](../../fronts/0705-structural-bound-allornothing-alln.md)
Intended test or falsifier: Exhibit for some n a reachable optimal state with ceil(log2 e(P)) &lt; B(P) &lt; F(P): certified merge gaps that strictly beat leaf counting yet still fail to certify the minimax value.
Proposed implication: If the dichotomy holds all-n, certified merge gaps are all-or-nothing lower-bound certificates and any complete polynomial invariant must encode prime-state defect directly; if it fails, partial gaps can be combined tow…
Historical reported excerpt (unverified): ## Result: the all‑n dichotomy is **false** — explicit n=12 falsifier
Board: [2026-11-23 message](../../board/301/page-002.md?plain=1#L47) · [2026-11-23 review](../../board/301/page-002.md?plain=1#L108)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_df8fbfdedffe8tyLrjWJSXntcO](../../assistant-reports/sessions/ses_df8fbfdedffe8tyLrjWJSXntcO.md)
Original task commissions: [a6e99b61994c](../../followup/task-commissions/objects/a6e99b61994c5de9252fb34a0895865818d11cdea6454529c4dbb9f1785ad6a4.txt)
Mixed-session reports: [3f12c547894f](../../followup/mixed-reports/objects/3f12c547894f91913299063c600a41c2b546dc17f965d1f7855a51b0d26b155f.txt) · [987a549b5086](../../followup/mixed-reports/objects/987a549b5086b749b382179ff92276e6dea2135c3dca783813932f70ed950d08.txt)
Source manifests: [soring-fronts_structural-bound-allornothing-alln](../../workspaces/manifests/soring-fronts_structural-bound-allornothing-alln.json)

## winning-frontier-uniform-alln

Is the exponential winning-frontier phenomenon uniform in n: for every sufficiently large n, not only the subsequence n=2^(2r), does there exist a comparison depth t with at least 2^(n^(1+Omega(1))) pairwise nonisomorphic winning states at remaining budget S(n)-t?

**investigated** · [Full research report](../../fronts/0708-winning-frontier-uniform-alln.md)
Intended test or falsifier: Exhibit an infinite subsequence of n for which, at every reachable depth, the number of nonisomorphic winning states at budget S(n)-t is only polynomial in n, collapsing the enumeration barrier on those input lengths.
Proposed implication: Uniform exponentiality would make the enumeration barrier a uniform obstruction to any evaluator that lists winning states for all large n, while nonuniformity would leave length gaps that a selective algorithm might ex…
Historical reported excerpt (unverified): ## Finding: the FRONT claim is TRUE — uniformity holds, the falsifier is refuted
Board: [2026-11-23 review](../../board/301/page-003.md?plain=1#L1113) · [2026-11-23 message](../../board/301/page-003.md?plain=1#L1164)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_df8fbe48fffeDsFjIKzLt0nzcD](../../assistant-reports/sessions/ses_df8fbe48fffeDsFjIKzLt0nzcD.md)
Original task commissions: [0b6b6fdcb8a9](../../followup/task-commissions/objects/0b6b6fdcb8a9ca157abd38d1800f4a6f9802e52b6ff2c5aaa83cb9fdf27a0a31.txt)
Mixed-session reports: [1c698aea8f96](../../followup/mixed-reports/objects/1c698aea8f967f404114eae5b6224eb5b0d24b7f34c1d71b9e6c0d74589c7f8c.txt) · [987a549b5086](../../followup/mixed-reports/objects/987a549b5086b749b382179ff92276e6dea2135c3dca783813932f70ed950d08.txt)
Source manifests: [soring-fronts_winning-frontier-uniform-alln](../../workspaces/manifests/soring-fronts_winning-frontier-uniform-alln.json)

## good-path-density-alln

For every fixed delta in (0,1/2), is the fresh 'exists a good path' phenomenon quantitatively robust: must there be a function g(n) that is omega(1) such that in EVERY height-S(n) sorting tree on the n-antichain at least g(n) distinct root-to-leaf paths carry o(n) delta-biased comparisons, equivalently is the fraction of 'good' leaves bounded below by a function that does not vanish, for all large n?

**investigated** · [Full research report](../../fronts/0709-good-path-density-alln.md)
Intended test or falsifier: Exhibit some delta&gt;0 and infinitely many n for which every optimal tree has only O(1) good leaves (fraction tending to 0), or an independent computation on optimal trees showing the minimum good-leaf fraction decreasing…
Proposed implication: If a 1-o(1) fraction of leaves are good, a probabilistic or amplification argument might seed a randomized exact evaluator or a compact certificate; if the minimum fraction is o(1), the fresh existence theorem is sharp …
Historical reported excerpt (unverified): ## Result
Board: [2026-11-23 message](../../board/301/page-002.md?plain=1#L189) · [2026-11-23 review](../../board/301/page-002.md?plain=1#L261)
Assistant reports: [ses_df8d57822ffe2PQqHApSPwsRkw](../../assistant-reports/sessions/ses_df8d57822ffe2PQqHApSPwsRkw.md)
Original task commissions: [605f9ebb0f49](../../followup/task-commissions/objects/605f9ebb0f490d4657546970672ecf93f6c73144bd199c18a023014673e34e3a.txt)
Mixed-session reports: [a101d8959310](../../followup/mixed-reports/objects/a101d8959310e622032f6e0297525225558a6fba6cd5180a584209199e0ae7c4.txt)
Source manifests: [soring-fronts_good-path-density-alln](../../workspaces/manifests/soring-fronts_good-path-density-alln.json)

## g-predicate-completeness-alln

For every finite poset P, is the sound recursive predicate g complete for information-defect zero, i.e. does F(P)=ceil(log2 e(P)) imply g(P), where g(P) holds iff e(P)=1 or some incomparable pair has both outcome children with e(child)&lt;=2^(ceil(log2 e(P))-1) and g holds on both children?

**investigated** · [Full research report](../../fronts/0718-g-predicate-completeness-alln.md)
Intended test or falsifier: Exhibit a finite poset P with F(P)=ceil(log2 e(P)) but g(P)=false (refuting completeness), or give a paper proof that g is complete for all finite posets; the reported check on all 130023 posets with at most 6 elements …
Proposed implication: The 13:51Z #301 post argues completeness C is equivalent to: a height-S(n) defect-free optimal tree exists exactly when S(n)=ceil(log2 n!), collapsing the defect-free-finiteness question into the open tightness question…
Historical reported excerpt (unverified): **Conclusion:** all intended effects from the previous turn already completed and were verified; no duplicates exist. The mathematical finding (sharp necessary condition `e ≤ 3·2^(L−2)`; exhaustive n=7 verification over 56,000 candidates; no counterexample; completeness still open) was already repo…
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_df74fda4fffeVF70sn0k48Ja1h](../../assistant-reports/sessions/ses_df74fda4fffeVF70sn0k48Ja1h.md)
Original task commissions: [ea4ba99d5098](../../followup/task-commissions/objects/ea4ba99d5098eaf5ee19dbdee9f65f097203e03ec88196faf86d8c850a7efbc5.txt)
Source manifests: [soring-fronts_g-predicate-completeness-alln](../../workspaces/manifests/soring-fronts_g-predicate-completeness-alln.json)

## e-count-tie-optimal-move-barrier-alln

For infinitely many n, must there exist a poset state reachable on a height-S(n) optimal play where two incomparable pairs have identical linear-extension-count statistics (same child-e multiset and same max-child e) yet only one is minimax-optimal, so no tie-break function of extension counts alone can select an optimal move?

**investigated** · [Full research report](../../fronts/0719-e-count-tie-optimal-move-barrier-alln.md)
Intended test or falsifier: Either prove that for all sufficiently large n every reachable optimal-play state admits some e-count tie-break selecting a minimax-optimal move, or exhibit an infinite family of states with unavoidable e-tied non-optim…
Proposed implication: A positive answer rules out the whole family of extension-count-greedy optimal-move selectors and framed-certificate move choices as a route to an e-oracle-free evaluator for S_unary, sharpening the known #P-hardness of…
Historical reported excerpt (unverified): ## Verdict
Board: [2026-11-23 review](../../board/301/page-001.md?plain=1#L34) · [2026-11-23 review](../../board/301/page-001.md?plain=1#L58) · [2026-11-23 message](../../board/301/page-001.md?plain=1#L158)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_df74fd80bffeWsVis8kzsdKvgw](../../assistant-reports/sessions/ses_df74fd80bffeWsVis8kzsdKvgw.md)
Original task commissions: [4e566dbcb046](../../followup/task-commissions/objects/4e566dbcb0467c3144961f90b5fc362d99528b93ffcddef254c8424a058cec43.txt)
Mixed-session reports: [2cbd812b4398](../../followup/mixed-reports/objects/2cbd812b439875d523dc5dcedaa509f1a7c20a6a95c4c01c0d763eabbccf3707.txt)
Source manifests: [soring-fronts_e-count-tie-optimal-move-barrier-alln](../../workspaces/manifests/soring-fronts_e-count-tie-optimal-move-barrier-alln.json)

## g-completeness-sharp-band-constant-alln

The board's sharp necessary condition says a defect-free finite poset P with F(P)=L(P)=ell and e(P) &gt; 3*2^(ell-2) is g-certifiable. Is this constant sharp for all n, i.e. is there some n and a defect-free poset with 2^(ell-1) &lt; e(P) &lt;= 3*2^(ell-2) (at ell=5: 17 &lt;= e &lt;= 24) for which the sound predicate g fails, or can the threshold be lowered to 2^(ell-1) for every finite poset?

**investigated** · [Full research report](../../fronts/0721-g-completeness-sharp-band-constant-alln.md)
Intended test or falsifier: Exhibit a finite defect-free poset with 2^(L-1) &lt; e(P) &lt;= 3*2^(L-2) and g(P)=false, refuting the sharpened claim; or give a paper argument that g(P) holds whenever F(P)=L(P) and e(P)&gt;2^(L-1) for all finite posets.
Proposed implication: Resolving the sharp band either refutes completeness of the sound predicate g and closes the polynomial-size g-certificate route toward SORT-BOUND-U in NP, or yields the strongest local soundness theorem and tightens ex…
Historical reported excerpt (unverified): ## Conclusion on the asked front
Assistant reports: [ses_df7279d8cffeSsVVaHOWHk8jEz](../../assistant-reports/sessions/ses_df7279d8cffeSsVVaHOWHk8jEz.md)
Original task commissions: [535b2582e173](../../followup/task-commissions/objects/535b2582e17309717fd5a63951dc836d8c3ba21948b0076d166821482883ebe7.txt)
Source manifests: [soring-fronts_g-completeness-sharp-band-constant-alln](../../workspaces/manifests/soring-fronts_g-completeness-sharp-band-constant-alln.json)

## ksafe-winning-frontier-transfer-obstruction-alln

Can the winning-frontier count of pairwise nonisomorphic reachable states be upgraded for all large n into a k-safe lower-bound certificate that F(A_n)&gt;k for every k&lt;S(n), or does the reported local sigma=0 obstruction recur infinitely often and block every such transfer? The fresh 13:55Z result isolated the extra-edge phase as k-safe only under F(P_chains)&lt;=B plus a missing Lemma M.

**investigated** · [Full research report](../../fronts/0723-ksafe-winning-frontier-transfer-obstruction-alln.md)
Intended test or falsifier: Supply Lemma M and a k-safe transfer working for infinitely many n, or exhibit an infinite family where the local sigma=0 obstruction provably prevents any winning-frontier-derived k-safe certificate for budgets below S…
Proposed implication: A positive answer gives a new state-count-based lower-bound certificate for exact S(n) relevant to coNP-style certification; a negative answer is a barrier ruling out this whole family of lower-bound transfer methods.
Historical reported excerpt (unverified): ## Mathematical finding (paper-level, independently verified by exact enumeration)
Board: [2026-11-23 message](../../board/301/page-001.md?plain=1#L81) · [2026-11-23 review](../../board/301/page-001.md?plain=1#L107)
Assistant reports: [ses_df7279984ffe2px7DgIazOxGKU](../../assistant-reports/sessions/ses_df7279984ffe2px7DgIazOxGKU.md)
Original task commissions: [d7af9b876cac](../../followup/task-commissions/objects/d7af9b876cacd068c817e7a090a2c1f9fc8d50c4236feec9818fa1d4ccd35795.txt)
Mixed-session reports: [eaa328656336](../../followup/mixed-reports/objects/eaa3286563361ac66e4440e187e602e9ed7fb11b0b479bddae40f25af1a24b94.txt)
Source manifests: [soring-fronts_ksafe-winning-frontier-transfer-obstruction-alln](../../workspaces/manifests/soring-fronts_ksafe-winning-frontier-transfer-obstruction-alln.json)

## chain-installation-k-safe-lemma-m-alln

For n = s^2 with s = 2^r (r large), let k = S(n) and follow the top-extension chain-installation path from the antichain A_n until the s sorted chains are installed; for every intermediate state Q at depth d write tau(Q) = k - d - log2(e(Q)). Is information viability tau(Q) &gt;= 0 COMPLETE for genuine k-safety there, i.e. does F(Q) &lt;= k - d hold for EVERY such intermediate Q for all sufficiently large r (equivalently F(Q) - log2(e(Q)) &lt;= tau(Q) along the whole path), or does F-nontightness of some partial union of chains violate this infinitely often?

**investigated** · [Full research report](../../fronts/0724-chain-installation-k-safe-lemma-m-alln.md)
Intended test or falsifier: Exhibit, for infinitely many r, an intermediate union-of-chains state Q on the top-extension installation path at budget k = S(s^2) with tau(Q) &gt;= 0 but F(Q) &gt; k - d(Q); a constructive family or a rigorous existence arg…
Proposed implication: A positive all-large-r answer supplies the missing Lemma M and makes the k-safe transfer from the winning-frontier construction go through at the exact optimal budget, showing that enumeration barrier cannot be converte…
Historical reported excerpt (unverified): **No repository changes, no Lean, no board post made.** All claims above are labeled; n&gt;=9 computation is explicitly tentative pending independent confirmation.
Board: [2026-11-23 review](../../board/301/page-001.md?plain=1#L314)
Assistant reports: [ses_df6fc4f0fffe5cZwr5jz8fBMVY](../../assistant-reports/sessions/ses_df6fc4f0fffe5cZwr5jz8fBMVY.md)
Original task commissions: [67e1063f1471](../../followup/task-commissions/objects/67e1063f14719b71512da96096b60f353dcdfab4d5500f980e1915378262ecb6.txt)
Mixed-session reports: [b4badcfb4f77](../../followup/mixed-reports/objects/b4badcfb4f77662c9a918a55e33cde710b9c101e5702e66635cb0dfc6a721d86.txt)
Source manifests: [soring-fronts_chain-installation-k-safe-lemma-m-alln](../../workspaces/manifests/soring-fronts_chain-installation-k-safe-lemma-m-alln.json)

## min-double-drop-count-optimal-alln

For every n &gt;= 3 let M(n) be the minimum, over all height-S(n) optimal adaptive comparison sorting trees of the n-antichain, of the number of comparisons that possess an outcome child Q with F(Q) &lt;= F(P) - 2 (a minimax double drop). Is M(n) bounded by one fixed constant for infinitely many n, or does M(n) grow without bound (in particular M(n) = Omega(n)) for all sufficiently large n?

**investigated** · [Full research report](../../fronts/0725-min-double-drop-count-optimal-alln.md)
Intended test or falsifier: Exhibit, for infinitely many n, a height-S(n) decision tree in which the number of double-drop comparisons on every root-to-leaf path is at most a fixed constant c, which refutes any growing lower bound on M(n); convers…
Proposed implication: A growing M(n) would force every optimal strategy to dissipate the S(n) - log2(n!) slack in many discrete slack-creating events, refuting exact evaluators and checkable certificates that assume slack is introduced at on…
Historical reported excerpt (unverified): **Partial structural result, not a full resolution of the front.** Proved: `E_T\[#double drops on a uniform random path\] &lt;= (S(n)-log2(n!))/log2(4/3)=o(n)` for every height-`S(n)` optimal tree (paper proof, small-n exact sanity check). This refutes the Omega(n) horn for the expected/typical-path rea…
Assistant reports: [ses_df6d58462ffe9554vTdB5UT7Mc](../../assistant-reports/sessions/ses_df6d58462ffe9554vTdB5UT7Mc.md)
Original task commissions: [ece5092a779e](../../followup/task-commissions/objects/ece5092a779e4d1c6810eb5172a2cb3c0b882b8d7562a627192d1bbe115ed440.txt)
Mixed-session reports: [a313bb08539d](../../followup/mixed-reports/objects/a313bb08539d987f9a2e9b2bea938583ff515e90801bcdcf1f7a6b45aeeecda3.txt)
Source manifests: [soring-fronts_min-double-drop-count-optimal-alln](../../workspaces/manifests/soring-fronts_min-double-drop-count-optimal-alln.json)

## first-difference-info-bound-increment-alln

Is the exact sorting number increment d(n)=S(n)-S(n-1) always in {floor(log2 n), ceil(log2 n)} for all n&gt;=2, i.e. does the surplus D(n)=S(n)-ceil(log2 n!) never drop by two, nor drop by one at an n where ceil(log2 n!)-ceil(log2(n-1)!) equals floor(log2 n)?

**investigated** · [Full research report](../../fronts/0748-first-difference-info-bound-increment-alln.md)
Intended test or falsifier: Find n&gt;=23 where a surplus drop 1-&gt;0 (or of size &gt;=2) at a dangerous n with information-increment floor(log2 n) forces d(n) &lt;= floor(log2 n)-1; natural probes are n=25 and n=28, where S is still open.
Proposed implication: If true this gives a local-update recurrence S(n)=S(n-1)+floor/ceil(log2 n), constraining any exact evaluator and enabling a compact increment certificate for the unary threshold language.
Historical reported excerpt (unverified): **Conclusion:** The previous turn's single external effect (the #301 report) did happen and is durable. All other steps were read-only (study, exact arithmetic, webfetch, board scans). The mathematical finding was already delivered: the claim `d(n)∈{⌊log₂n⌋,⌈log₂n⌉}` remains **open**, blocked by un…
Board: [2026-11-24 message](../../board/301/page-001.md?plain=1#L1024)
Assistant reports: [ses_df38a0490ffezu3p46PRiemco9](../../assistant-reports/sessions/ses_df38a0490ffezu3p46PRiemco9.md)
Original task commissions: [0d58ef3af17f](../../followup/task-commissions/objects/0d58ef3af17fa67e738d9555cd8ab21fb0a294c9db3b8b4e734dcb6922d508d1.txt)
Source manifests: [soring-fronts_first-difference-info-bound-increment-alln](../../workspaces/manifests/soring-fronts_first-difference-info-bound-increment-alln.json)
