# Space, search and exact algorithms

[Catalogue home](../README.md) · [Evidence status guide](../../RESULTS.md)

Status is the original workflow label, not mathematical proof. Linked messages may contain corrections or rejected claims.

## compress-exact-space-evaluator

Construct and rigorously analyze a uniform exact evaluation algorithm for S(n) with asymptotically smaller workspace than the existing recurrence, explicitly accounting for representation and branch recomputation.

**investigated** · [Full research report](../../fronts/0004-compress-exact-space-evaluator.md)
Intended test or falsifier: Give a concrete state family forcing the proposed compact representation to store superpolynomial independent decisions, or find a hidden recursive stack-space violation.
Proposed implication: A verified uniform smaller-space bound would strengthen the known upper bound for SORT-BOUND-U even without proving P or NP membership.
Historical reported excerpt (unverified): **Finding:** Canonical root-replay does not currently give a justified space improvement for the all-budget DFS. Storing a DFS-node rank has a straightforward worst-case cost of \(O(k\log n)\) bits, the same order as the path stack. Regenerating a target node from the root at each frame can repeate…
Board: [2026-11-17 message](../../board/301/page-016.md?plain=1#L1108) · [2026-10-30 message](../../board/301/page-042.md?plain=1#L3) · [2026-10-30 message](../../board/301/page-043.md?plain=1#L433)
Additional board mentions: 3 (use front lookup for exact links)
Mixed-session reports: [1693c66be111](../../followup/mixed-reports/objects/1693c66be11193b9a754e98df6e5017dab69616db6a66f33935217d33cbac083.txt) · [259ce2d13ee6](../../followup/mixed-reports/objects/259ce2d13ee60d5e524ec41580bd3b3b4933e52c3447f5f4400dd207caefe801.txt) · [2a669e7849b7](../../followup/mixed-reports/objects/2a669e7849b79109954ddb293592067e0940cfb701afdfb4d717837d55a945d1.txt) (10 total)
Source manifests: [soring-fronts_compress-exact-space-evaluator](../../workspaces/manifests/soring-fronts_compress-exact-space-evaluator.json)

## exact-evaluator-time-exponent

Can the exact numeric evaluator S_unary(1^n) be improved from the known 2^{O(n log^2 n)} time to 2^{O(n log n)} or 2^{O(n)} uniformly in n via a memoization or interface-summary tradeoff that provably recomputes or stores everything it needs, or is there an all-n state family forcing every such evaluator to keep an Omega(n^2)-bit seed table?

**investigated** · [Full research report](../../fronts/0014-exact-evaluator-time-exponent.md)
Intended test or falsifier: Either a fully specified algorithm with a correctness and cost paper argument reaching 2^{O(n log n)} or 2^{O(n)} on 1^n, or an explicit all-n family of reachable framed states such that any candidate interface summary …
Proposed implication: Any improvement directly lowers the known uniform time envelope for computing the exact function S(n), and a forced-state family would rule out an entire memoization-prune family of evaluators without touching the trans…
Historical reported excerpt (unverified): **Result (new, all-n, paper proof + experiments, commit `f9d444a`):**
Board: [2026-11-06 message](../../board/301/page-026.md?plain=1#L3) · [2026-10-27 message](../../board/301/page-044.md?plain=1#L74)
Additional board mentions: 4 (use front lookup for exact links)
Source manifests: [soring-fronts_exact-evaluator-time-exponent](../../workspaces/manifests/soring-fronts_exact-evaluator-time-exponent.json)

## sound-bisimulation-summary-evaluator

Is there a sound interface summary (a bisimulation-style congruence coarser than labelled-poset isomorphism) defined on the states reachable by a budget-critical threshold DFS, such that two congruent states provably share the same minimax budget, yet the induced quotient has only sub-exponentially many classes relative to the Theta(n log^2 n)-bit isomorphism-fine identity proven necessary?

**investigated** · [Full research report](../../fronts/0016-sound-bisimulation-summary-evaluator.md)
Intended test or falsifier: Exhibit two budget-critical reachable states that must be identified by every candidate coarse invariant (e.g., one proposing an explicit polynomial-size summary: usable-prefix chain counts, height profiles, or extensio…
Proposed implication: A verified sound-and-polynomial-bounded summary would let a canonical memoised evaluator evade the proven 2^{Theta(n log^2 n)} family barrier from board #301 and reopen uniform exact evaluation of S_unary at 2^{O(n log …
Historical reported excerpt (unverified): The precise unresolved point is whether a proposed summary—such as \(e(P)\)—merges budget-critical reachable states with different \(F(P)\), or whether some sound, coarser congruence can avoid the #301 isomorphism-fine state-count barrier. I did not verify a primary-literature result resolving that…
Additional board mentions: 1 (use front lookup for exact links)
Mixed-session reports: [13ec1a6f6ef7](../../followup/mixed-reports/objects/13ec1a6f6ef728c8a70f9cc94053ae2bb7a46aff7a097756e7561b2b2d2d1c9d.txt)
Source manifests: [soring-fronts_sound-bisimulation-summary-evaluator](../../workspaces/manifests/soring-fronts_sound-bisimulation-summary-evaluator.json)

## linear-space-unary-decision

Does SORT-BOUND-U admit a deterministic linear-space decision procedure, i.e. O(N) work-tape bits on unary input 1^n # 1^k of length N, improving the established O(N log(N+2))-space budgeted transcript DFS without any time blowup change?

**investigated** · [Full research report](../../fronts/0021-linear-space-unary-decision.md)
Intended test or falsifier: Attempt to replace every multi-bit component of the transcript DFS (the path stack, the pair cursors, and the counter bookkeeping) by an O(1)-bits-per-level encoding, and isolate a specific concrete state family at some…
Proposed implication: Proving the O(N) bound would tighten the PSPACE membership of the unary language to a linear-space bound, a strictly stronger uniform result; an authenticated forced-stack lower bound for the DFS family is a barrier the…
Historical reported excerpt (unverified): The transcript-DFS family cannot achieve O(N) bits: its path stack has depth k ≤ N levels, and each level must store a cursor over binom(n,2)=Ω(n²) candidate pairs, requiring Ω(log n)=Ω(log N) bits per level, giving Ω(N log N) bits total. The reachability workspace adds another Ω(N log N)-bit term.…
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_linear-space-unary-decision](../../workspaces/manifests/soring-fronts_linear-space-unary-decision.json)

## sort-bound-u-pspace-complete

Is SORT-BOUND-U PSPACE-complete under polynomial-time many-one reductions, or can the antichain symmetry of S(n) rule out PSPACE-hardness while preserving PSPACE membership?

**investigated** · [Full research report](../../fronts/0024-sort-bound-u-pspace-complete.md)
Intended test or falsifier: Exhibit either a polynomial-time many-one reduction from some PSPACE-complete problem to SORT-BOUND-U (proving PSPACE-hardness) or an unconditional proof that SORT-BOUND-U has structural properties incompatible with PSP…
Proposed implication: PSPACE-completeness would mean P!=PSPACE iff SORT-BOUND-U not in P (linking to a major separation), while a proof of PSPACE-membership without completeness would sharpen the gap and clarify the role of antichain structu…
Historical reported excerpt (unverified): **Finding (unconditional obstruction to PSPACE-completeness):** `SORT-BOUND-U` is sparse (\[deduction\], `research-certificates-barriers.md` Claim B / `research-hardness-boundaries.md` §4) and in `PSPACE` (\[deduction\], Claim A via `APTIME=PSPACE`). For classes that have self-reducible complete sets a…
Additional board mentions: 2 (use front lookup for exact links)
Mixed-session reports: [5877b6da8f89](../../followup/mixed-reports/objects/5877b6da8f896707b050bee31995a48fc78a8fad4afe13a858f0cec0f858c4e8.txt)
Source manifests: [soring-fronts_sort-bound-u-pspace-complete](../../workspaces/manifests/soring-fronts_sort-bound-u-pspace-complete.json)

## entropy-balance-deterministic-pruning

Can Sergeev's entropy-balance/o(n) surplus observation be turned into a sound deterministic worst-case pruning rule for root-optimal search that provably cuts the 2^{Theta(n log^2 n)} winning frontier without excluding any height-S(n) optimal strategy?

**investigated** · [Full research report](../../fronts/0028-entropy-balance-deterministic-pruning.md)
Intended test or falsifier: Show any proposed local entropy-balance potential is either unsound (prunes some optimal strategy) on a concrete family, or preserves an exponential class family equivalent to isomorphism classes.
Proposed implication: A verified sound pruning rule would give a practical path toward better exact evaluators and clarify barrier structure.
Historical reported excerpt (unverified): ### Verdict **No sound deterministic worst-case pruning rule based solely on a local entropy-balance potential is obvious, and there is a strong mathematical obstruction.** - **Against (b) (frontier cut):** Any potential invariant under isomorphism/Aut orbits preserves the 2^((1/4-o(1)) n log^2 n) …
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_entropy-balance-deterministic-pruning](../../workspaces/manifests/soring-fronts_entropy-balance-deterministic-pruning.json)

## universal-space-lower-bound

Does every correct uniform deterministic algorithm for deciding SORT-BOUND-U on unary input of length N use Omega(N log N) bits of work space, not just the transcript-DFS family?

**investigated** · [Full research report](../../fronts/0033-universal-space-lower-bound.md)
Intended test or falsifier: Construct a correct uniform algorithm deciding SORT-BOUND-U in o(N log N) work space with a rigorous cost analysis, or prove a general Omega(N log N) space lower bound for all uniform algorithms.
Proposed implication: A universal space lower bound would show the existing O(N log N) budgeted DFS space bound is asymptotically tight for all uniform methods and sharpen the space frontier beyond family-specific arguments.
Historical reported excerpt (unverified): Based on studying AGENTS.md, docs/problem.md, docs/research-budgeted-dfs.md, docs/research-plan.md, and the codebase: the control-stack/tree-evaluation argument suggests a universal Ω(N log N) lower bound is plausible (depth k with branching factor Θ(n^2) requires Θ(k log n) position/history bits, …
Source manifests: [soring-fronts_universal-space-lower-bound](../../workspaces/manifests/soring-fronts_universal-space-lower-bound.json)

## space-time-tradeoff-sorting-number

Can we achieve a better space-time tradeoff for exact computation of S(n) than current bounds, or is there a lower bound tradeoff that rules out subexponential time with polynomial space?

**investigated** · [Full research report](../../fronts/0038-space-time-tradeoff-sorting-number.md)
Intended test or falsifier: Construct a subexponential-time polynomial-space uniform algorithm for S(n), or prove a tradeoff lower bound showing it's impossible.
Proposed implication: Understanding space-time tradeoffs clarifies the complexity landscape and may reveal new barriers.
Historical reported excerpt (unverified): Conclusion: memoization gives a concrete better space-time tradeoff than the published no-memoization DFS; space can be traded for time. Whether subexponential time with polynomial space is achievable remains open (not ruled out by known barriers, not demonstrated). No repository changes made.
Source manifests: [soring-fronts_space-time-tradeoff-sorting-number](../../workspaces/manifests/soring-fronts_space-time-tradeoff-sorting-number.json)

## sergeev-effective-pruning-completeness

For all sufficiently large n, does there exist an explicit uniform polynomial-time (in n) procedure that certifies S(n) &gt;= C(n) + f(n) with f(n)=omega(log n) using only effectively computable constants from Sergeev's asymptotic, or is non-effectivity unavoidable for any such all-n certificate?

**investigated** · [Full research report](../../fronts/0039-sergeev-effective-pruning-completeness.md)
Intended test or falsifier: Prove that no Turing machine using only Sergeev's published O(·) parameters can produce an effective all-n lower certificate of the form above, or construct an explicit effective all-n procedure achieving f(n)=omega(log…
Proposed implication: An effective finite form would yield a uniform pruning test for SORT-BOUND-U and tighten the search window; a proven obstruction to effectivity would be a barrier limiting asymptotic bounds to non-constructive guidance.
Historical reported excerpt (unverified): **Honest limit:** this is a known blocker in the repo, not resolved by this analysis. No repository changes made. The question remains open; the cleanest falsifier is (b) a precise non-effectivity argument about the information content of “published $O(\cdot)$ parameters” vs extracting constructive…
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_sergeev-effective-pruning-completeness](../../workspaces/manifests/soring-fronts_sergeev-effective-pruning-completeness.json)

## uniform-space-lower-bound-sorting-number

For SORT-BOUND-U = {1^n # 1^k : S(n)&lt;=k} on multitape TMs with input length N=n+k+1, is there an all-n uniform space lower bound Ω(N log N / log log N) ruling out o(N log N / log log N) work tape for all large N, or does some uniform algorithm achieve strictly smaller space for all (n,k)?

**investigated** · [Full research report](../../fronts/0059-uniform-space-lower-bound-sorting-number.md)
Intended test or falsifier: Construct a deterministic uniform TM deciding SORT-BOUND-U for all (n,k) using S(N)=o(N log N / log log N) space for all sufficiently large N with an explicit correctness and space analysis.
Proposed implication: A uniform space lower bound would tighten the known O(N log N) bound below PSPACE in a nontrivial way; a constructive falsifier would show the transcript-only DFS bound is not asymptotically tight for space and suggest …
Historical reported excerpt (unverified): I examined the space complexity of deciding SORT-BOUND-U via the transcript DFS (with Savitch for reachability). No such lower bound appears in the repo's established results - only that poset-state size doesn't force Ω(n^2). The current worst-case O(N log N) is dominated by the stack of comparison…
Board: [2026-10-31 message](../../board/301/page-040.md?plain=1#L292)
Source manifests: [soring-fronts_uniform-space-lower-bound-sorting-number](../../workspaces/manifests/soring-fronts_uniform-space-lower-bound-sorting-number.json)

## sparse-pspace-completeness

Is SORT-BOUND-U PSPACE-complete under polynomial-time many-one reductions, or does its unary-sparse form and minimax structure place it strictly below PSPACE-complete problems relative to logspace/polynomial many-one reducibility?

**investigated** · [Full research report](../../fronts/0062-sparse-pspace-completeness.md)
Intended test or falsifier: Construct an explicit polynomial-time many-one reduction from some known PSPACE-complete language to SORT-BOUND-U, or prove SORT-BOUND-U is not PSPACE-hard under polynomial-time many-one reductions (e.g. via a density/s…
Proposed implication: PSPACE-completeness would mean exact S(n) evaluation is as hard as general PSPACE; a strict lower containment would reflect the combinatorial structure of sorting/minimax and could open paths to better bounds or to unde…
Historical reported excerpt (unverified): **Concrete failed approach:** trying to lift EXPTIME density argument to PSPACE failed because the standard padding/time-hierarchy step used for EXPTIME doesn't directly yield a contradiction for PSPACE-completeness of a sparse set under poly-time many-one reductions - the consequence is consistent…
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_sparse-pspace-completeness](../../workspaces/manifests/soring-fronts_sparse-pspace-completeness.json)

## sort-bound-pspace-completeness

Is the unary threshold language SORT-BOUND-U = {1^n # 1^k : S(n) &lt;= k} PSPACE-complete under polynomial-time many-one reductions, or does the comparison/antichain structure force it strictly below PSPACE?

**investigated** · [Full research report](../../fronts/0075-sort-bound-pspace-completeness.md)
Intended test or falsifier: Construct an explicit poly-time m-reduction from a known PSPACE-complete language to SORT-BOUND-U that preserves the antichain-root structure, or prove an invariant obstruction (beyond sparsity/barriers already known) t…
Proposed implication: PSPACE-completeness would show computing S(n) is PSPACE-hard (in the unary/decision sense), placing it among the hardest problems in PSPACE; a strict containment proof would reveal new structure limiting adversarial pow…
Historical reported excerpt (unverified): **Finding (mathematical):** SORT-BOUND-U cannot be PSPACE-complete under polynomial-time many-one reductions.
Source manifests: [soring-fronts_sort-bound-pspace-completeness](../../workspaces/manifests/soring-fronts_sort-bound-pspace-completeness.json)

## uniform-time-exponent-barrier

Is there an all-n lower bound showing that every uniform deterministic algorithm computing S(n) (or deciding SORT-BOUND-U) must run in time at least 2^(Omega(n log n)) on unary inputs, or can the budgeted DFS exponent be reduced below n log^2 n uniformly?

**investigated** · [Full research report](../../fronts/0086-uniform-time-exponent-barrier.md)
Intended test or falsifier: Give a uniform algorithm achieving time 2^(O(n log n / log log n)) for all large n with proof, or prove that the poset state graph of the minimax recurrence requires time 2^(Omega(n log n)) to evaluate by any uniform me…
Proposed implication: A tight uniform time lower bound would clarify the position of S(n)-evaluation relative to PSPACE and rule out near-linear-exponent improvements; a better algorithm would improve the known uniform upper bound.
Historical reported excerpt (unverified): No repository changes made (no substantive new theorem/counterexample found).
Board: [2026-10-31 message](../../board/301/page-040.md?plain=1#L292) · [2026-10-30 message](../../board/301/page-041.md?plain=1#L229) · [2026-10-31 message](../../board/301/page-041.md?plain=1#L301) · [2026-10-31 message](../../board/301/page-041.md?plain=1#L317) · [2026-10-31 message](../../board/301/page-041.md?plain=1#L333)
Source manifests: [soring-fronts_uniform-time-exponent-barrier](../../workspaces/manifests/soring-fronts_uniform-time-exponent-barrier.json)

## randomized-exact-evaluator-speedup

For the unary function S_unary(1^n), can a uniform randomized algorithm (with zero error, worst-case time bound over random coins) compute S(n) exactly in time 2^(o(n log^2 n)) for all large n, or is there an all-n lower bound ruling out subexponential-in-n log^2 n randomized exact computation?

**investigated** · [Full research report](../../fronts/0093-randomized-exact-evaluator-speedup.md)
Intended test or falsifier: Construct an explicit zero-error randomized uniform algorithm achieving 2^(o(n log^2 n)) time for all large n with a correctness/cost proof, or prove an unconditional 2^(Omega(n log^2 n)) time lower bound for zero-error…
Proposed implication: A verified randomized speedup would improve the known uniform upper bound for computing S(n) without changing the comparison model; a randomized lower bound would sharpen barriers to exact evaluation beyond deterministi…
Historical reported excerpt (unverified): Obstructions/failed approaches: randomized pair ordering unlikely to help against adversarial inputs where winning moves are sparse; randomized canonical labeling has exactness issues. No known construction achieves 2^(o(n log^2 n)), and a general lower bound would cross into discouraged territory …
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_randomized-exact-evaluator-speedup](../../workspaces/manifests/soring-fronts_randomized-exact-evaluator-speedup.json)

## and-or-tree-evaluation-class

Is the decision problem SORT-BOUND-U complete for some natural subclass of PSPACE (e.g. AC^0 reductions to AND-OR tree evaluation on poset games) or does the fixed antichain family place it strictly below the complexity of evaluating arbitrary AND-OR trees?

**investigated** · [Full research report](../../fronts/0094-and-or-tree-evaluation-class.md)
Intended test or falsifier: Give an all-n AC^0 (or logspace) reduction from some PSPACE-complete AND-OR tree evaluation instance to SORT-BOUND-U, or prove SORT-BOUND-U has a structural property (e.g. bounded alternation in some normalized form) in…
Proposed implication: A completeness result would classify S(n) evaluation relative to standard game-tree complexity; strict containment would explain why general AND-OR bounds don't apply and may suggest better algorithms.
Historical reported excerpt (unverified): The analysis above addresses both branches of the falsifier. Neither is satisfied by existing results - sparsity/collapse arguments obstruct reductions, bounded alternation remains unproven. No repo/Lean changes made; no new theorem/counterexample. This is the honest report.
Source manifests: [soring-fronts_and-or-tree-evaluation-class](../../workspaces/manifests/soring-fronts_and-or-tree-evaluation-class.json)

## unary-input-space-metric-barrier

For SORT-BOUND-U with actual input length N = n + S(n) + 1 (unary encoding of n and k), does every uniform deterministic algorithm deciding exact inequality S(n) &lt;= k require Ω(N / log N) working space for all sufficiently large n?

**investigated** · [Full research report](../../fronts/0096-unary-input-space-metric-barrier.md)
Intended test or falsifier: There exists a uniform deterministic algorithm deciding SORT-BOUND-U in o(N / log N) working space for all n &gt;= 1.
Proposed implication: Constrains exact evaluation in the problem's stated input metric without invoking unconditional super-polynomial lower bounds for the unary language or general-poset #P-hardness, potentially tightening the space side of…
Historical reported excerpt (unverified): The analysis identifies a concrete obstruction (path/transcript storage in DFS game-tree search) giving Ω(N log N) space, which is stronger than the claimed Ω(N/log N). I did not find a way to achieve o(N/log N) and no obvious algorithmic breakthrough to avoid transcript storage. This is an obstruc…
Source manifests: [soring-fronts_unary-input-space-metric-barrier](../../workspaces/manifests/soring-fronts_unary-input-space-metric-barrier.json)

## space-lower-bound-unary

Is there a nontrivial space lower bound (e.g. Omega(N log N) or better) for any uniform deterministic algorithm deciding SORT-BOUND-U on unary input of length N?

**investigated** · [Full research report](../../fronts/0104-space-lower-bound-unary.md)
Intended test or falsifier: Exhibit a uniform sublinear-space (in N) exact algorithm for SORT-BOUND-U, or prove the transcript-only bound is not improvable below Omega(n log n).
Proposed implication: A space lower bound would sharpen the upper/lower gap beyond time and inform whether the transcript-only O(N log N) is tight.
Historical reported excerpt (unverified): Mathematical finding: For SORT-BOUND-U with N = n+k+1 (input 1^n # 1^k) and k near S(n), information-theoretic bounds imply S(n)=Ω(n log n) and each backtrack frame needs Ω(log n) bits to identify a comparison; any uniform deterministic backtracking search over the minimax game tree requires Ω(n lo…
Board: [2026-10-31 message](../../board/301/page-040.md?plain=1#L236) · [2026-10-31 message](../../board/301/page-040.md?plain=1#L244) · [2026-10-31 message](../../board/301/page-040.md?plain=1#L252) · [2026-10-31 message](../../board/301/page-040.md?plain=1#L292)
Assistant reports: [ses_e18380ec5ffe3LlfIlEG5CmTjK](../../assistant-reports/sessions/ses_e18380ec5ffe3LlfIlEG5CmTjK.md)
Original task commissions: [782c3788713f](../../followup/task-commissions/objects/782c3788713f0b83e878e2d154944d5b7930d8c7adda1289996ce9b0b88cf8fc.txt)
Mixed-session reports: [82e2fa187327](../../followup/mixed-reports/objects/82e2fa18732785a2f988872d828b755b752761d4d3a97412d7906654b6a32a23.txt)
Source manifests: [soring-fronts_space-lower-bound-unary](../../workspaces/manifests/soring-fronts_space-lower-bound-unary.json)

## antichain-pspace-completeness

Is SORT-BOUND-U PSPACE-complete under polynomial-time many-one reductions for the exact adaptive comparison game on the antichain?

**investigated** · [Full research report](../../fronts/0124-antichain-pspace-completeness.md)
Intended test or falsifier: Show SORT-BOUND-U is not PSPACE-hard by exhibiting a complexity collapse obstruction for this sparse unary game, or place it in a strictly smaller class with a uniform algorithm for all n.
Proposed implication: PSPACE-completeness would fix SORT-BOUND-U's exact class (distinct from NP/EXPTIME by the barriers) and clarify the APTIME equivalence; non-hardness would show the antichain is easier than general poset games.
Historical reported excerpt (unverified): **Bottom line:** `SORT-BOUND-U ∈ PSPACE`. Under polynomial-time many-one reductions, PSPACE-hardness is obstructed by sparsity (=&gt; `PSPACE ⊆ P/poly`), which is a standard collapse obstruction with no known primary reduction for the antichain. No unconditional disproof, no known smaller class; the q…
Board: [2026-11-01 message](../../board/301/page-037.md?plain=1#L55) · [2026-11-01 message](../../board/301/page-037.md?plain=1#L63)
Source manifests: [soring-fronts_antichain-pspace-completeness](../../workspaces/manifests/soring-fronts_antichain-pspace-completeness.json)

## winning-frontier-space-tradeoff

Can the 2^{Θ(n log^2 n)} state space of the known memoized poset-DP be compressed below 2^{Ω(n log n)} for exact S(n) by exploiting the winning-frontier sparsity (the 2^{(1/4-o(1))n log^2 n} winning states at depth barrier) without losing exactness, and does any such compression yield a better uniform space bound for unary SORT-BOUND-U in PSPACE?

**blocked** · [Full research report](../../fronts/0133-winning-frontier-space-tradeoff.md)
Intended test or falsifier: Show the winning frontier is unavoidable for any exact recurrence preserving the minimax root (the sparsity is a lower bound on distinct states needed), or construct an exact method with smaller asymptotic state count d…
Proposed implication: A verified compression below the known barrier would tighten space/descriptional complexity of exact evaluation even if time bounds remain open.
Historical reported excerpt (unverified): **Next:** Disambiguate the target DP object, test the falsifier on rectangular states for distinguishability/compressibility, and assess implications for unary SORT-BOUND-U space.
Board: [2026-11-01 message](../../board/301/page-035.md?plain=1#L219) · [2026-11-01 message](../../board/301/page-035.md?plain=1#L227) · [2026-11-01 message](../../board/301/page-035.md?plain=1#L291)
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_winning-frontier-space-tradeoff](../../workspaces/manifests/soring-fronts_winning-frontier-space-tradeoff.json)

## sparse-pspace-ph-level

For the sparse unary language SORT-BOUND-U in PSPACE (by ATM alternation), is there a fixed level k of the polynomial hierarchy with SORT-BOUND-U in Sigma_k^P, or can it be shown to require arbitrarily high fixed alternation levels for all polynomial-time reductions from complete problems?

**investigated** · [Full research report](../../fronts/0135-sparse-pspace-ph-level.md)
Intended test or falsifier: Construct a polynomial-time reduction from some QBF_k-complete language to SORT-BOUND-U for all fixed k, or prove SORT-BOUND-U in Sigma_k^P for some fixed k using its sparsity and the minimax game structure.
Proposed implication: Pinning the PH level would clarify whether the alternating comparison game collapses below PSPACE or is a genuine sparse PSPACE instance, without relying on P/poly circuit lower bounds.
Historical reported excerpt (unverified): **Mathematical finding (attempt to disprove PH-hardness):** **Claim attacked:** SORT-BOUND-U is PH-hard (reduces QBF_k to it for all fixed k). **Structural obstruction (deduction):** The comparison game is ∃ (sorter picks incomparable pair) vs ∀ (adversary answers consistently with some total order…
Board: [2026-11-01 message](../../board/301/page-035.md?plain=1#L291)
Source manifests: [soring-fronts_sparse-pspace-ph-level](../../workspaces/manifests/soring-fronts_sparse-pspace-ph-level.json)

## pebbling-space-sortbound

For the partial-order minimax DAG of states reachable from the n-antichain, is its pebbling number polynomial in n for some optimal strategy ordering, or does every legal pebbling strategy require super-polynomial pebbles regardless of edge orientations?

**investigated** · [Full research report](../../fronts/0137-pebbling-space-sortbound.md)
Intended test or falsifier: Exhibit a family of poset states requiring Omega(n^c) pebbles for all c and all valid DAG pebblings, or construct a uniform ordering with pebbling number polynomial in the unary input length.
Proposed implication: A super-polynomial pebbling lower bound would give a space lower bound for uniform exact evaluation of S(n) without relying on circuit lower bounds, while a polynomial pebbling strategy could inform improved work-space …
Historical reported excerpt (unverified): **Pragmatic conclusion:** The question is well-posed, but as stated it conflates pebbling (memoization) with recomputation strategies. Given transcript DFS already achieves $O(n\log^2 n)$ space, a super-polynomial pebbling lower bound in the pure memoization sense would be interesting but the compl…
Source manifests: [soring-fronts_pebbling-space-sortbound](../../workspaces/manifests/soring-fronts_pebbling-space-sortbound.json)

## minimax-game-pspace-hardness-antichain

Can SORT-BOUND-U be shown PSPACE-hard under polynomial-time Turing reductions from QBF despite sparsity, or is sparsity an absolute obstruction to all polynomial reductions?

**investigated** · [Full research report](../../fronts/0142-minimax-game-pspace-hardness-antichain.md)
Intended test or falsifier: Give a formal proof that no polynomial-time Turing reduction from any PSPACE-complete language exists to SORT-BOUND-U, or construct an explicit Turing reduction and show it preserves encoding faithfully.
Proposed implication: Establishing Turing PSPACE-completeness would clarify whether the exact complexity is PSPACE-complete or strictly below; sparsity blocks many-one reductions but not necessarily Turing reductions in all settings.
Historical reported excerpt (unverified): **Notes on scope:** This is about Turing reductions (not many-one). Certificate soundness/completeness is orthogonal; the question is reduction class. No Lean/repo changes warranted. This matches AGENTS.md: sparsity blocks many-one NP-hardness → P=NP, but Turing case is different and the productive…
Source manifests: [soring-fronts_minimax-game-pspace-hardness-antichain](../../workspaces/manifests/soring-fronts_minimax-game-pspace-hardness-antichain.json)

## and-or-poset-pspace-completeness

Is SORT-BOUND-U PSPACE-complete under polynomial-time many-one reductions from QBF (or another PSPACE-complete language), or is the poset-lattice structure of the sorting game strictly less powerful than arbitrary AND-OR games despite membership in PSPACE?

**investigated** · [Full research report](../../fronts/0148-and-or-poset-pspace-completeness.md)
Intended test or falsifier: Construct an explicit polynomial-time many-one reduction from a PSPACE-complete language to SORT-BOUND-U preserving the unary encoding, or prove a structural invariant of the comparison game that cannot simulate arbitra…
Proposed implication: PSPACE-completeness would identify the exact class of SORT-BOUND-U and clarify the significance of any future upper/lower bounds; strict containment below PSPACE-complete would indicate exploitable structure in the sort…
Historical reported excerpt (unverified): I'll start by reading the current board state and the relevant front entries from the ledger.
Source manifests: [soring-fronts_and-or-poset-pspace-completeness](../../workspaces/manifests/soring-fronts_and-or-poset-pspace-completeness.json)

## gen-sort-pspace-reduction-antichain

Can GEN-SORT (sorting number for an arbitrary given poset) be reduced by a polynomial-time encoding-preserving reduction to SORT-BOUND-U (antichain case S(n)&lt;=k) for some function of n,k and poset size, or is such a transfer provably impossible for all all-n families while respecting the unary encoding and model restrictions?

**investigated** · [Full research report](../../fronts/0163-gen-sort-pspace-reduction-antichain.md)
Intended test or falsifier: Construct an explicit polynomial encoding from GEN-SORT instances to (n,k) in unary with correctness for all instances, or give a general theorem showing the fixed symmetric comparison set of the antichain blocks any su…
Proposed implication: A positive reduction would make SORT-BOUND-U PSPACE-hard (hence PSPACE-complete given known membership), linking P!=PSPACE to the antichain sorting number; a general obstruction would sharpen the 'hardness does not tran…
Historical reported excerpt (unverified): Do not try to construct such an encoding. The falsifier's "general theorem showing the fixed symmetric comparison set of the antichain blocks any such reduction" is satisfied by the parameter-dependence argument above. Any future attempt must first clarify whether $(n',k')$ are allowed to depend on…
Additional board mentions: 1 (use front lookup for exact links)
Mixed-session reports: [ff4c1855e691](../../followup/mixed-reports/objects/ff4c1855e691ee848b6b3ac7dbed8def5cc609426e36315764060ef6f8311f53.txt)
Source manifests: [soring-fronts_gen-sort-pspace-reduction-antichain](../../workspaces/manifests/soring-fronts_gen-sort-pspace-reduction-antichain.json)

## bottleneck-width-logspace-analogue

Is there an infinite all-n family where every strategy achieving S(n) forces a bottleneck of width &gt;= Omega(n^epsilon) in some path-decomposition of the state graph of optimal play, and does this obstruct uniform log-space evaluation of SORT-BOUND-U?

**investigated** · [Full research report](../../fronts/0169-bottleneck-width-logspace-analogue.md)
Intended test or falsifier: Prove that optimal-play state graphs have bounded pathwidth for all n (or admit a uniform log-space strategy evaluator), or exhibit a log-space uniform algorithm deciding SORT-BOUND-U exactly for all n.
Proposed implication: Linking pathwidth of the actual minimax optimal states to space complexity would connect combinatorial structure to uniform resources without assuming hardness of arbitrary partial orders or rediscovering known exact va…
Historical reported excerpt (unverified): **Verdict:** The front is coherent in principle, but not currently falsifiable/refutable from existing published facts because the “state graph of optimal play” is under-specified and the optimality restriction blocks direct general-poset arguments. No infinite all-n family forcing Ω(n^ε) pathwidth…
Mixed-session reports: [e03bbbb30466](../../followup/mixed-reports/objects/e03bbbb304661f2776172a43e970a1337c35468333d9414b2b800c27a59f2ae6.txt)
Source manifests: [soring-fronts_bottleneck-width-logspace-analogue](../../workspaces/manifests/soring-fronts_bottleneck-width-logspace-analogue.json)

## subexp-budgeted-dfs-barrier

For the unary threshold language SORT-BOUND-U with input length N = n+k+1, is there any all-n uniform deterministic algorithm deciding exact S(n) &lt;= k in time 2^(o(N log N)), or does the structure of budget-reachable poset states force a time lower bound of 2^(Omega(N log N))?

**investigated** · [Full research report](../../fronts/0179-subexp-budgeted-dfs-barrier.md)
Intended test or falsifier: Produce an explicit uniform algorithm achieving time 2^(o(N log N)) for all sufficiently large N with a rigorous correctness argument, or prove that the family of budget-reachable (P,d) states has size 2^(Omega(N log N)…
Proposed implication: A verified subexponential-in-N log N algorithm would strictly improve the known uniform upper bound for exact evaluation of S(n); a general barrier theorem would rule out that entire class of approaches and clarify the …
Historical reported excerpt (unverified): **Conclusion:** The decisive obstruction is real for *exhaustive/enumerative* approaches, but **not a general lower bound** ruling out all correct exact evaluators. No $2^{o(N\log N)}$ uniform algorithm is known. The question remains open; the tight exponent is not established. Any claim of a gener…
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_subexp-budgeted-dfs-barrier](../../workspaces/manifests/soring-fronts_subexp-budgeted-dfs-barrier.json)

## logspace-turing-sortbound-threshold

Is there any uniform deterministic log-space Turing machine that decides SORT-BOUND-U for all unary inputs 1^n # 1^k, given the established O(N log N) bit space bound from budgeted DFS and the fact that S(n)=Theta(n log n) is the threshold?

**investigated** · [Full research report](../../fronts/0187-logspace-turing-sortbound-threshold.md)
Intended test or falsifier: Show SORT-BOUND-U is not in L by a direct space lower bound argument exploiting the comparison constraints of the minimax game (not circuit size), or construct an explicit log-space algorithm achieving the decision via …
Proposed implication: Resolving L-membership (distinct from PSPACE/P) would pinpoint the exact small space class of the unary threshold; a log-space lower bound would rule out extremely space-efficient uniform evaluation even if time remains…
Historical reported excerpt (unverified): **Conclusion:** On the evidence, $\mathrm{SORT\!-\!BOUND\!-\!U} \notin \mathrm{L}$. The decisive obstruction is the $\Omega(n\log n)$ depth search stack over a large partial-order state space under comparison constraints (forcing $\\Omega(N\log N)$ space) combined with configuration-counting on the…
Source manifests: [soring-fronts_logspace-turing-sortbound-threshold](../../workspaces/manifests/soring-fronts_logspace-turing-sortbound-threshold.json)

## sortboundu-pspace-hardness

Is SORT-BOUND-U = {1^n # 1^k : S(n) &lt;= k} many-one polynomial-time hard for PSPACE (or complete), and if so can a direct reduction from a standard PSPACE-complete game be constructed without passing through general poset sorting?

**investigated** · [Full research report](../../fronts/0216-sortboundu-pspace-hardness.md)
Intended test or falsifier: Prove SORT-BOUND-U is in PH (or strictly below PSPACE) under some plausible assumption, or show that every reduction from a PSPACE-complete language produces an instance not realizable by any comparison-based sorting ga…
Proposed implication: PSPACE-completeness would make P != PSPACE equivalent to SORT-BOUND-U not in P and would rule out uniform subexponential exact algorithms for all practical purposes in a strong class sense.
Historical reported excerpt (unverified): **Mathematical finding (disproof attempt):** Under the standard assumption $\mathrm{PSPACE} \nsubseteq \mathrm{P/poly}$, $\mathrm{SORT\textrm{-}BOUND\textrm{-}U}$ is not $\le_m^p$-hard for $\mathrm{PSPACE}$ (hence not $\le_m^p$-complete), so PSPACE-completeness is false in that model. Argument: $\m…
Source manifests: [soring-fronts_sortboundu-pspace-hardness](../../workspaces/manifests/soring-fronts_sortboundu-pspace-hardness.json)

## space-o-n-reduction

Can the budgeted DFS for SORT-BOUND-U be implemented in O(N) work space (unary N=n+k+1) without increasing time beyond 2^(O(N log N)) asymptotically, or prove a space lower bound?

**investigated** · [Full research report](../../fronts/0220-space-o-n-reduction.md)
Intended test or falsifier: Prove space &gt;= omega(N) is necessary under some model, or construct O(N)-space algorithm.
Proposed implication: Tightens space complexity below current O(N log N); relevant to descriptive complexity (VAR hierarchy).
Historical reported excerpt (unverified): Thus falsify "O(N)" for budgeted DFS; complexity tightens to Ω(N log N). No Lean/repo changes made (no substantive new theorem/counterexample integrated). Concrete obstruction as above.
Board: [2026-11-03 message](../../board/301/page-030.md?plain=1#L233) · [2026-11-03 message](../../board/301/page-030.md?plain=1#L241) · [2026-11-03 message](../../board/301/page-030.md?plain=1#L249)
Source manifests: [soring-fronts_space-o-n-reduction](../../workspaces/manifests/soring-fronts_space-o-n-reduction.json)

## space-reduction-budgeted-dfs

Can the budgeted DFS for SORT-BOUND-U be implemented in O(N) working space (or polylog N) while preserving time bounds up to polynomial factors, without storing full exponential transcript lists?

**investigated** · [Full research report](../../fronts/0242-space-reduction-budgeted-dfs.md)
Intended test or falsifier: Prove any correct algorithm deciding SORT-BOUND-U in sublinear space relative to the number of states visited requires exponential time blowup, or show the poset DP/state graph forces O(N log N) space.
Proposed implication: Space reduction would clarify the L vs NL vs P boundary relative to this sparse PSPACE language.
Historical reported excerpt (unverified): **Limits:** No unconditional proof of a tight lower bound was derived here (just structural obstruction), no repo/Lean changes made, and this is consistent with SORT-BOUND-U's known PSPACE membership without implying PSPACE-completeness. Distinction between general-poset results and antichain-root …
Board: [2026-11-22 message](../../board/301/page-004.md?plain=1#L153) · [2026-11-22 review](../../board/301/page-004.md?plain=1#L307)
Assistant reports: [ses_e0386a991ffe6X6TLiELSfqYc0](../../assistant-reports/sessions/ses_e0386a991ffe6X6TLiELSfqYc0.md)
Original task commissions: [5b7ba3078d61](../../followup/task-commissions/objects/5b7ba3078d617f24c087e700294a6228c922288f251be7c8bbcff907c4c017ea.txt)
Mixed-session reports: [17528e456124](../../followup/mixed-reports/objects/17528e4561248b4f92df7f6615e4e99088b2c7e0d7867b55c99dc6ebf2206105.txt) · [19fa271e8664](../../followup/mixed-reports/objects/19fa271e86647cbd472049691eea9618d0d3296e08fd7552240fd14ac51a612d.txt)
Source manifests: [soring-fronts_space-reduction-budgeted-dfs-20261121](../../workspaces/manifests/soring-fronts_space-reduction-budgeted-dfs-20261121.json) · [soring-fronts_space-reduction-budgeted-dfs](../../workspaces/manifests/soring-fronts_space-reduction-budgeted-dfs.json)

## antichain-game-pspace-completeness

Can SORT-BOUND-U be shown many-one PSPACE-hard by reducing from QBF/alternating TQBF to the poset comparison game while respecting adversary total-order consistency and the unary antichain input?

**investigated** · [Full research report](../../fronts/0244-antichain-game-pspace-completeness.md)
Intended test or falsifier: Prove the adversary's global total-order consistency constraints create an insurmountable simulation gap that cannot be bridged for any polynomial-time reduction preserving yes-instances.
Proposed implication: PSPACE-completeness would be a strong complexity classification (separating from P/NP under standard assumptions). Ruling it out would bound hardness.
Historical reported excerpt (unverified): **Mathematical finding (obstruction):** - **Direction matters.** Claim A shows the game simulates an ATM (membership `SORT-BOUND-U ∈ PSPACE`). The converse fails. The adversary is *restricted*, not free. - **Strategy-space restriction.** In the comparison game, adversary must answer consistently wi…
Source manifests: [soring-fronts_antichain-game-pspace-completeness](../../workspaces/manifests/soring-fronts_antichain-game-pspace-completeness.json)

## sparse-manyone-pspace-hard-barrier

For SORT-BOUND-U (sparse unary threshold), is there an unconditional all-n barrier to many-one polynomial-time PSPACE-hardness stronger or different from EXPTIME-nonhardness, and would such hardness imply a specific collapse distinct from Mahaney's NP case?

**investigated** · [Full research report](../../fronts/0267-sparse-manyone-pspace-hard-barrier.md)
Intended test or falsifier: Exhibit a many-one polynomial-time reduction from some PSPACE-complete language to SORT-BOUND-U preserving the sparse/unary structure with an explicit all-n correctness argument, or derive an unconditional theorem showi…
Proposed implication: Clarifying PSPACE-hardness status would fix where SORT-BOUND-U sits relative to PH/PSPACE without relying on P!=PSPACE equivalences and would delimit alternation/certificate routes.
Historical reported excerpt (unverified): **Finding (\[deduction\]):** Unconditional barrier exists by density/preimage, same class as EXPTIME — not an open gap.
Board: [2026-11-04 message](../../board/301/page-029.md?plain=1#L511)
Source manifests: [soring-fronts_sparse-manyone-pspace-hard-barrier](../../workspaces/manifests/soring-fronts_sparse-manyone-pspace-hard-barrier.json)

## linear-extensions-count-pruning-barrier

For the winning-frontier family of layered posets (union of chains plus between-level edges) appearing at depths near S(n), is there an all-n obstruction showing that any exact uniform evaluator for S(n) that uses the information bound ceil(log2 e(P)) for pruning must compute e(P) exactly on exponentially many of these states and that exact linear-extension counting on this class is not uniform-polytime per state, forcing exponential total time regardless of other pruning?

**investigated** · [Full research report](../../fronts/0270-linear-extensions-count-pruning-barrier.md)
Intended test or falsifier: Exhibit a uniform polynomial-time algorithm to compute e(P) exactly for all posets in that layered winning-frontier family for large n, or show a sound pruning scheme avoiding exact e(P) that achieves subexponential tot…
Proposed implication: A verified all-n barrier would link #P-hardness of counting to the concrete complexity of evaluating S(n) via pruning, without requiring circuit lower bounds and while distinguishing general-poset counting from this str…
Historical reported excerpt (unverified): **Conclusion:** The obstruction argument is coherent and matches the repo’s evidence (frontier size + profile-DP exponential in width + pruning dependence on $e(P)$). However, I did not derive a new rigorous all-$n$ barrier theorem or a concrete counterexample/algorithm here — only a structural ana…
Source manifests: [soring-fronts_linear-extensions-count-pruning-barrier](../../workspaces/manifests/soring-fronts_linear-extensions-count-pruning-barrier.json)

## sortbound-u-pspace-completeness

Is SORT-BOUND-U PSPACE-complete under polynomial-time many-one reductions, or is there a polynomial-time reduction from some PSPACE-complete problem to it preserving the unary encoding?

**investigated** · [Full research report](../../fronts/0282-sortbound-u-pspace-completeness.md)
Intended test or falsifier: Exhibit a polynomial-time many-one reduction from a known PSPACE-complete language to SORT-BOUND-U, or prove an unconditional barrier showing no such reduction exists for all PSPACE-complete problems.
Proposed implication: PSPACE-completeness would tighten the equivalences in AGENTS.md (P!=PSPACE &lt;-&gt; SORT-BOUND-U not in P, NP!=PSPACE &lt;-&gt; not in NP); non-hardness would mean the sorting game is strictly easier than some PSPACE-complete prob…
Historical reported excerpt (unverified): **Conclusion:** SORT-BOUND-U is not PSPACE-hard under polynomial-time many-one reductions (no reduction from dense PSPACE-complete problems like TQBF). Hence not PSPACE-complete. The "preserving unary encoding" qualifier doesn't circumvent the barrier. This is an unconditional obstruction, not a pr…
Source manifests: [soring-fronts_sortbound-u-pspace-completeness](../../workspaces/manifests/soring-fronts_sortbound-u-pspace-completeness.json)

## path-stack-space-necessity

Is storing the full comparison transcript (the DFS path stack) necessary for any uniform algorithm deciding SORT-BOUND-U in the standard Turing model, or is there an all-n method that reuses workspace by canonicalizing states without expanding the alternation/game depth?

**investigated** · [Full research report](../../fronts/0283-path-stack-space-necessity.md)
Intended test or falsifier: Exhibit a uniform deterministic algorithm for SORT-BOUND-U using o(n log n) work-tape bits for all sufficiently large n (on the relevant input range) with a complete correctness proof and cost accounting in the unary in…
Proposed implication: A proven all-n space lower bound would sharpen the known polynomial-space upper bounds and constrain the transcript/DP family; a verified sublinear-in-n-log-n upper bound would improve the concrete space complexity for …
Historical reported excerpt (unverified): - No repository/Lean changes made. Posted findings to reasoning only as requested.
Source manifests: [soring-fronts_path-stack-space-necessity](../../workspaces/manifests/soring-fronts_path-stack-space-necessity.json)

## budgeted-dfs-algebraic-decision-lower-bound

In algebraic decision/comparison models that capture transcript-only budgeted DFS over extension-count and reachability predicates, must every exact SORT-BOUND-U decider perform 2^{Omega(n)} predicate evaluations on infinitely many unary inputs, even when allowed polynomial workspace?

**investigated** · [Full research report](../../fronts/0312-budgeted-dfs-algebraic-decision-lower-bound.md)
Intended test or falsifier: Give a uniform exact algorithm in that model family with 2^{o(n)} predicate evaluations for all sufficiently large n, or prove the model fails to capture a known exact method such as budgeted DFS/pruning variants releva…
Proposed implication: A model-specific exponential predicate lower bound would sharpen understanding of why current exact evaluators are costly without claiming a separation from P/PSPACE; a subexponential exact simulation would directly imp…
Historical reported excerpt (unverified): ## Conclusion (mathematical finding) **Literal claim C is refuted for the stated ExtGt-inclusive model on its easiest infinite subclass**: `ExtGt(A_n,2^k)` decides all `k &lt;= ⌈log₂ n!⌉-1` in 1 evaluation (`n&gt;=3`), so not `2^{Ω(n)}` on infinitely many inputs. The meaningful residue is: *on informatio…
Source manifests: [soring-fronts_budgeted-dfs-algebraic-decision-lower-bound](../../workspaces/manifests/soring-fronts_budgeted-dfs-algebraic-decision-lower-bound.json)

## threshold-pruning-state-count

In the budgeted exact minimax DFS for SORT-BOUND-U, does replacing the e&lt;=7 Hanamura-Iwata base by the exact extension-threshold base e(P) &lt;= T(b) imply accept reduce the worst-case number of expanded reachable states below the established 2^{O(n log^2 n)} frontier for all n?

**investigated** · [Full research report](../../fronts/0331-threshold-pruning-state-count.md)
Intended test or falsifier: An infinite all-n family of reachable states with e(P) &gt; T(b) that every correct threshold-pruned evaluator must expand, or a proof that the pruned state count remains 2^{Omega(n log^2 n)} at the antichain root.
Proposed implication: A yes answer would improve the exact unary time bound toward 2^{O(n log n)}; a no-go would show the Fibonacci threshold is structural only and sharpens the boundary of the current evaluator even though the pruning rule …
Historical reported excerpt (unverified): - This is a paper proof relying on the published Sergeev asymptotic; it is not Lean-checked and was not integrated into the repository.
Board: [2026-11-08 message](../../board/301/page-023.md?plain=1#L697) · [2026-11-08 message](../../board/301/page-023.md?plain=1#L719)
Assistant reports: [ses_e478c9bbbffeU0sTnTbXAGqvNE](../../assistant-reports/sessions/ses_e478c9bbbffeU0sTnTbXAGqvNE.md)
Original task commissions: [a008a6f6b6d1](../../followup/task-commissions/objects/a008a6f6b6d1b968871e7bcb433437b953d7bf0d2e1ebfe7db0c0c3931af4aa4.txt)
Source manifests: [soring-fronts_threshold-pruning-state-count](../../workspaces/manifests/soring-fronts_threshold-pruning-state-count.json)

## unary-evaluator-space-nlogn

Can S(n) be computed in O(n log n) space (or less) uniformly in n for the unary function S_unary(1^n), beating the current O(n log^2 n) work-tape bound?

**investigated** · [Full research report](../../fronts/0336-unary-evaluator-space-nlogn.md)
Intended test or falsifier: A lower bound showing any deterministic uniform evaluator of S(n) requires Omega(n log^2 n) space, or a construction achieving O(n log n) space with correctness proof.
Proposed implication: Improves the space complexity of exact S(n) evaluation below the established O(n log^2 n) bound, directly advancing the active frontier.
Historical reported excerpt (unverified): ## Finding (no repository change) **Claim attacked:** *S(n) can be computed in O(n log n) space uniformly, beating the established O(n log² n) work-tape bound.* **Result: not established; the natural reduction is obstructed, and no counterexample/lower bound is proved either.**
Assistant reports: [ses_e473cf102ffeVOhVB6azI3G2V6](../../assistant-reports/sessions/ses_e473cf102ffeVOhVB6azI3G2V6.md) · [ses_e473b3b1bffe9X3FYoxoVS9JpW](../../assistant-reports/sessions/ses_e473b3b1bffe9X3FYoxoVS9JpW.md)
Original task commissions: [3f65d416b003](../../followup/task-commissions/objects/3f65d416b00366d8edac642616d93e9f7d088a219dbb71888148d2f3e8279eb7.txt) · [d154dc457eec](../../followup/task-commissions/objects/d154dc457eec566dac8c3738dbe787a2f60e2f89d063dd464eae5bf8615d2c6c.txt)
Source manifests: [soring-fronts_unary-evaluator-space-nlogn](../../workspaces/manifests/soring-fronts_unary-evaluator-space-nlogn.json)

## adaptive-tree-minimax-recurrence-space

Is the partial-order minimax recurrence computable in polynomial space in n (as a function of numeric n) without exponential time, by exploiting structure of the antichain root?

**investigated** · [Full research report](../../fronts/0337-adaptive-tree-minimax-recurrence-space.md)
Intended test or falsifier: A proof that recurrence evaluation for the fixed antichain family requires 2^Omega(n^2) time for all algorithms, or an algorithm running in poly(n) space and subexponential time.
Proposed implication: Would either yield a faster exact evaluator or a barrier against recurrence-based methods for S(n).
Historical reported excerpt (unverified): **Next decisive obstacle:** find (or rule out) a canonical form for reachable partial orders under comparison transcripts with `poly(n)`-size description and `F`-invariant value.
Assistant reports: [ses_e473ced6affexYye5LV1cxcaRN](../../assistant-reports/sessions/ses_e473ced6affexYye5LV1cxcaRN.md) · [ses_e473b3708ffe6m5uVfXwfUHKP4](../../assistant-reports/sessions/ses_e473b3708ffe6m5uVfXwfUHKP4.md)
Original task commissions: [4e2cbc6c4ea6](../../followup/task-commissions/objects/4e2cbc6c4ea6adcb6c37f448930cad39f086df0b0a9b6bb2db4ba06682e66a30.txt) · [ad30fbc17b60](../../followup/task-commissions/objects/ad30fbc17b60e4b96317bcb653fa98c38c772dde23476956edab248a560f06d4.txt)
Source manifests: [soring-fronts_adaptive-tree-minimax-recurrence-space](../../workspaces/manifests/soring-fronts_adaptive-tree-minimax-recurrence-space.json)

## unary-space-transcript-encoding

Investigate whether the comparison transcript of an optimal sorting strategy can be encoded in o(n log n) bits while remaining uniformly decodable, as a path to improving the PSPACE space bound for S(n).

**investigated** · [Full research report](../../fronts/0341-unary-space-transcript-encoding.md)
Intended test or falsifier: Construct an infinite family of optimal strategies whose transcripts require at least n log n bits under every proposed uniform encoding, or show recomputation overhead breaks the bound.
Proposed implication: A sublinear-in-nlogn transcript encoding would improve the known uniform space bound for computing S(n) without changing time class.
Historical reported excerpt (unverified): ## Finding: transcript encoding cannot be o(n log n) bits (uniformly decodable)
Assistant reports: [ses_e46b0135fffeYzOr65LZu5iA3E](../../assistant-reports/sessions/ses_e46b0135fffeYzOr65LZu5iA3E.md) · [ses_e46ad3432ffeHeynyy0UhBKRbH](../../assistant-reports/sessions/ses_e46ad3432ffeHeynyy0UhBKRbH.md)
Original task commissions: [4351c066f984](../../followup/task-commissions/objects/4351c066f9845eb2a7f9e025b4f7eb06e0ec143c98e0db837d99cc6f626206ff.txt) · [b281d72f3efc](../../followup/task-commissions/objects/b281d72f3efcaeaa1b6215c8da3d9ce3388f5efcfd240ec355f8d0c2510ea6f6.txt)
Source manifests: [soring-fronts_unary-space-transcript-encoding](../../workspaces/manifests/soring-fronts_unary-space-transcript-encoding.json)

## bidirectional-backward-frontier-exponent

For the Stober-Weiss bidirectional exact search at budget k, is the pruned backward frontier of posets on n keys at distance at most k from a total order always of size 2^{O(n log n)}, giving a uniform 2^{O(n log n)} exact algorithm for SORT-BOUND-U, or is there an all-n family with backward frontier 2^{Omega(n^2)}?

**investigated** · [Full research report](../../fronts/0358-bidirectional-backward-frontier-exponent.md)
Intended test or falsifier: An explicit all-n family of budgets k_n, for example k_n=C(n)+1, whose pruned backward frontier provably contains 2^{Omega(n^2)} pairwise non-isomorphic posets; or a fully uniform implementation with a proved 2^{O(n log…
Proposed implication: A sub-2^{n log^2 n} uniform algorithm would improve the best known exact evaluator and tighten the unary upper bound; a super-polynomial backward-frontier theorem would show the practical bidirectional method cannot be …
Historical reported excerpt (unverified): Finally, even a complete pruned frontier of size `2^{Θ(n log² n)}` gives no uniform `2^{O(n log n)}` algorithm. Enumerating it cannot beat the existing `2^{O(n log² n)}` budgeted DFS. A sub-`n log² n` **selective** evaluator remains open. Soundness of absence-based advice (Stober–Weiss Lemma 4.2) i…
Board: [2026-11-08 message](../../board/301/page-022.md?plain=1#L465) · [2026-11-08 message](../../board/301/page-022.md?plain=1#L583)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e455e5e01ffehpaDvS6yacG7a5](../../assistant-reports/sessions/ses_e455e5e01ffehpaDvS6yacG7a5.md)
Original task commissions: [47697ca895b4](../../followup/task-commissions/objects/47697ca895b4355b6b8f48c5ac2bb0e871d653fa3180fe25136005817c9481a9.txt)
Mixed-session reports: [0ebafad113de](../../followup/mixed-reports/objects/0ebafad113dea9cce2eb4c1888f5c90997c949c4ffcabb0fe773b93fb3911bc2.txt) · [23157bf94e64](../../followup/mixed-reports/objects/23157bf94e6409968c979d9bab1afa7129ed22f8bf5a1d4bb42ca0e6341e932d.txt)
Source manifests: [soring-fronts_bidirectional-backward-frontier-exponent](../../workspaces/manifests/soring-fronts_bidirectional-backward-frontier-exponent.json)

## linear-time-logspace-sortnumber

Is S(n) computable uniformly in O(n) time and O(log n) work space on a multitape Turing machine with unary input 1^n, or does every exact evaluator require superlinear time or superlogarithmic space on infinitely many n?

**investigated** · [Full research report](../../fronts/0375-linear-time-logspace-sortnumber.md)
Intended test or falsifier: Give an explicit O(n)-time O(log n)-space algorithm with a correctness and machine-cost proof, or prove a time-space lower bound for an infinite family of n under a stated uniform model.
Proposed implication: Such an algorithm would be optimal in input length and place S_unary in FP with near-minimal resources, whereas a lower bound would show the current 2^{O(n log^2 n)}-time and O(n log^2 n)-space regime is not merely an a…
Historical reported excerpt (unverified): **Research status from the completed turn.** The front remains open: no `O(n)`-time/`O(log n)`-space evaluator and no superlinear-time/superlogarithmic-space lower bound. The substantive output is a barrier theorem: the class `DTIME(n) ∩ DSPACE(log n)` on unary inputs contains a monotone `Θ(n log n…
Board: [2026-11-08 message](../../board/301/page-021.md?plain=1#L92) · [2026-11-08 message](../../board/301/page-021.md?plain=1#L201)
Assistant reports: [ses_e44a964e9ffe0Vhc0pnP44xVeM](../../assistant-reports/sessions/ses_e44a964e9ffe0Vhc0pnP44xVeM.md)
Original task commissions: [29b95fba7d9d](../../followup/task-commissions/objects/29b95fba7d9d1b66225fd5d45df03bd5b3b9a050ade0ddbf3a04d7ea9f26c3df.txt)
Source manifests: [soring-fronts_linear-time-logspace-sortnumber](../../workspaces/manifests/soring-fronts_linear-time-logspace-sortnumber.json)

## matching-poset-evaluator-complexity

For the extreme matching poset M_n = floor(n/2)C2 disjoint-union A_{n mod 2} from the newest board reduction, is F(M_n) computable uniformly in time 2^{O(n)} (or polynomial in n), improving on the generic 2^{O(n log^2 n)} poset DP, and does the matching-prefix normal form S(n) = floor(n/2) + F(M_n) hold for every n?

**investigated** · [Full research report](../../fronts/0389-matching-poset-evaluator-complexity.md)
Intended test or falsifier: Exhibit an all-n lower bound showing that every exact algorithm for F(M_n) needs 2^{Omega(n log n)} time, or compute an n with F(M_n) != S(n) - floor(n/2).
Proposed implication: A 2^{O(n)} evaluator together with the matching-prefix normal form would give the first 2^{O(n)} algorithm for S(n); a lower bound would isolate this structured disjoint-union family as the obstruction and would also re…
Historical reported excerpt (unverified): None. The previous turn completed the investigation and posted its finding once: the front-loading lemma, the corrected `F(M_47) &lt;= 177` / `E_M(47) &lt;= 2` bound, the conclusion that the n=47 Ford–Johnson improvement is not a normal-form counterexample, and the precise open `n=23` failure cell `(F,S)…
Board: [2026-11-08 message](../../board/301/page-021.md?plain=1#L800) · [2026-11-08 message](../../board/301/page-021.md?plain=1#L823)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e4384d2e5ffe6kqSAtTfO3rK65](../../assistant-reports/sessions/ses_e4384d2e5ffe6kqSAtTfO3rK65.md)
Original task commissions: [95f372da578b](../../followup/task-commissions/objects/95f372da578bc59ebcb9542d6de56af50ec3042ebb61beaabbfec35f0d500fad.txt)
Mixed-session reports: [0db695414126](../../followup/mixed-reports/objects/0db695414126ee952baad00888924bb53669a678a07b9f736ad87b005fd3c0e1.txt)
Source manifests: [soring-fronts_matching-poset-evaluator-complexity](../../workspaces/manifests/soring-fronts_matching-poset-evaluator-complexity.json)

## excess-parameterized-exact-evaluator

Is there a uniform algorithm computing S(n) in time poly(n)*2^{O(E(n))}, where E(n)=S(n)-ceil(log2 n!) is the information excess, or does every exact evaluator require time 2^{omega(E(n))} on an infinite family?

**investigated** · [Full research report](../../fronts/0409-excess-parameterized-exact-evaluator.md)
Intended test or falsifier: Give the parameterized evaluator with a proved resource bound, or prove an infinite-family lower bound showing poly(n)*2^{o(E(n))} time is impossible under a stated uniform model.
Proposed implication: Such an FPT-in-excess algorithm would make every O(log n)-excess regime polynomial-time and give a new route to SORT-BOUND-U in P, while a lower bound would show excess is not the right algorithmic parameter.
Historical reported excerpt (unverified): None in the research task. No uncertain external effect remains.
Board: [2026-11-09 message](../../board/301/page-019.md?plain=1#L149) · [2026-11-08 message](../../board/301/page-020.md?plain=1#L423)
Assistant reports: [ses_e42809e24ffe6n1136M4I4uFO8](../../assistant-reports/sessions/ses_e42809e24ffe6n1136M4I4uFO8.md)
Original task commissions: [3d2e43123f17](../../followup/task-commissions/objects/3d2e43123f1750bbdcd688ceb865322dd69729e838d3799566a1f68e9ea08c13.txt)
Mixed-session reports: [1ac266a87a6f](../../followup/mixed-reports/objects/1ac266a87a6ff9c4d01a693b3b87d7fd7bbc50c0efab284fbb175c1ac0bb0b7b.txt) · [23157bf94e64](../../followup/mixed-reports/objects/23157bf94e6409968c979d9bab1afa7129ed22f8bf5a1d4bb42ca0e6341e932d.txt)
Source manifests: [soring-fronts_excess-parameterized-exact-evaluator](../../workspaces/manifests/soring-fronts_excess-parameterized-exact-evaluator.json)

## transcript-only-space-tightness

For the unary threshold language SORT-BOUND-U with input length N=n+k+1, does every transcript-only deterministic decider that replays only the comparison-outcome path (no poset-state memo) require Omega(N log N) work-tape bits on the infinite no-instance family k=ceil(log2(n!))-1, or is there a uniform o(N log N)-space transcript-only decider?

**investigated** · [Full research report](../../fronts/0510-transcript-only-space-tightness.md)
Intended test or falsifier: Either prove an Omega(N log N)-bit lower bound for transcript-only deciders on the stated no-instances, or exhibit a uniform transcript-only algorithm using o(N log N) bits with correctness and space accounting; isomorp…
Proposed implication: Tightness would be the first space-optimality barrier for the budgeted-DFS upper bound and would force any improved SORT-BOUND-U evaluator to leave the transcript-only family; a smaller-space transcript algorithm would …
Historical reported excerpt (unverified): - **Status:** exact all-`n` falsifiable resolution (proved general lower bound or a concrete smaller-space transcript algorithm) **not achieved** here; I report the obstruction and failed disproofs rather than claiming a theorem.
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e33def7dfffemT5o2Jt8R0v0N8](../../assistant-reports/sessions/ses_e33def7dfffemT5o2Jt8R0v0N8.md)
Original task commissions: [73262c679c25](../../followup/task-commissions/objects/73262c679c255d534212ce63dbdcfdc50bdbcee86bde11cb4ebe7972d47e42ad.txt)
Mixed-session reports: [6ed17f23db54](../../followup/mixed-reports/objects/6ed17f23db546407d61a08ee9cd3e24f156b8a13f30df13bcddae1937997508e.txt) · [bc4df4b4264c](../../followup/mixed-reports/objects/bc4df4b4264cb275d439c91f7a2cca5ccc8d01b7f027bb098f8c188cee96ed62.txt) · [cee2a0280acf](../../followup/mixed-reports/objects/cee2a0280acfb1c11a64d4134fa647d11c1d46780102ec49537a9fcaabad0afa.txt)
Source manifests: [soring-fronts_transcript-only-space-tightness](../../workspaces/manifests/soring-fronts_transcript-only-space-tightness.json)

## winning-frontier-space-lower-bound

For all sufficiently large n, does every deterministic RAM algorithm computing the exact S(n) from unary input 1^n require work-tape space Ω(n (log n)^2 / log log n)?

**investigated** · [Full research report](../../fronts/0511-winning-frontier-space-lower-bound.md)
Intended test or falsifier: Exhibit a deterministic uniform algorithm computing S(n) on 1^n in o(n (log n)^2 / log log n) work-tape space with a correctness proof and explicit cost accounting.
Proposed implication: A nontrivial space lower bound would tighten the known O(n log^2 n) upper bound and clarify whether transcript/state compression can beat the winning frontier.
Historical reported excerpt (unverified): - **Not established:** any new theorem, counterexample, improved bound, or class-separation implication. No Lean/repository changes are warranted. A decisive next step would be either (a) a genuine space-optimized exact evaluator with a full correctness/space proof, or (b) a new lower-bound method …
Assistant reports: [ses_e30a1d8f1ffedcyI2G06mAXbqS](../../assistant-reports/sessions/ses_e30a1d8f1ffedcyI2G06mAXbqS.md)
Original task commissions: [9abaaeb79e9c](../../followup/task-commissions/objects/9abaaeb79e9c226e3b8d306b1a68c7f8e06a5aa7b534e736599f34a21f3c0e20.txt)
Source manifests: [soring-fronts_winning-frontier-space-lower-bound](../../workspaces/manifests/soring-fronts_winning-frontier-space-lower-bound.json)

## sparse-manyone-pspace-completeness-barrier

Is SORT-BOUND-U unconditionally not many-one PSPACE-complete under polynomial-time reductions (by sparsity/isomorphism generalizations of Berman–Hartmanis/Mahaney)?

**investigated** · [Full research report](../../fronts/0512-sparse-manyone-pspace-completeness-barrier.md)
Intended test or falsifier: Give a polynomial-time many-one reduction from a known PSPACE-complete language to SORT-BOUND-U with a complete correctness proof and encoding analysis, or show the sparsity+isomorphism barrier fails in this model.
Proposed implication: Establishing or ruling out many-one PSPACE-completeness would fix the exact relation of the sparse unary threshold to PSPACE without relying only on P/poly circuit barriers.
Historical reported excerpt (unverified): The research remains unfinished mathematically: the report found neither a PSPACE-hardness reduction nor a verified unconditional sparse-PSPACE barrier. It records the EXPTIME exclusion and leaves PSPACE many-one completeness unresolved.
Assistant reports: [ses_e30a1d72affeoFqtT03rdIGdV0](../../assistant-reports/sessions/ses_e30a1d72affeoFqtT03rdIGdV0.md)
Original task commissions: [1e5cb884bfed](../../followup/task-commissions/objects/1e5cb884bfedf75b0e0d689dcbb044abaa2b7a20a911c2881450e9387d9418d5.txt)
Source manifests: [soring-fronts_sparse-manyone-pspace-completeness-barrier](../../workspaces/manifests/soring-fronts_sparse-manyone-pspace-completeness-barrier.json)

## catalytic-reversible-exact-evaluation-space

Can exact evaluation of S(n) or decision of SORT-BOUND-U be performed in o(n log^2 n) bits by a uniform deterministic algorithm using a catalytic or reversible work tape, or does every exact method still require Omega(n log^2 n) bits?

**investigated** · [Full research report](../../fronts/0524-catalytic-reversible-exact-evaluation-space.md)
Intended test or falsifier: An explicit uniform algorithm using o(n log^2 n) ordinary bits together with polynomial catalytic or reversible workspace and sub-2^{O(n^2)} time, or a proof that catalytic encodings cannot beat the state-storing barrie…
Proposed implication: A positive result would improve the unary space upper bound below n log^2 n; a negative result would extend the winning-frontier barrier from path- and state-storing paradigms to catalytic computation.
Historical reported excerpt (unverified): ## Outcome No substantive repository or Lean changes were made. I wrote a paper-level `exec-report.md` in the isolated worktree `/home/lubko/soring301-exec-catalytic-reversible-space-20261117` and attempted to report on board #301. ### Mathematical finding
Board: [2026-11-17 message](../../board/301/page-015.md?plain=1#L232) · [2026-11-17 message](../../board/301/page-015.md?plain=1#L256)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e147963e3ffec31P56HpreG0FD](../../assistant-reports/sessions/ses_e147963e3ffec31P56HpreG0FD.md)
Original task commissions: [60698742c9a2](../../followup/task-commissions/objects/60698742c9a2da3de90ae75704eaf48c85a0546886957038a005c133bc36e632.txt)
Source manifests: [soring-fronts_catalytic-reversible-exact-evaluation-space](../../workspaces/manifests/soring-fronts_catalytic-reversible-exact-evaluation-space.json)

## randomized-exact-evaluator-game-tree

Can a randomized Las Vegas algorithm compute S(n) exactly on input 1^n in expected time 2^{o(n log^2 n)} or expected workspace o(n log^2 n), using coin-flip-guided minimax/game-tree pruning to beat the deterministic transcript- and state-storing barriers?

**investigated** · [Full research report](../../fronts/0529-randomized-exact-evaluator-game-tree.md)
Intended test or falsifier: Establish a Yao-style average-case lower bound: exhibit a distribution on adversary states/paths on which every correct randomized evaluator explores at least 2^{Omega(n log^2 n)} nodes in expectation or retains Omega(n…
Proposed implication: A positive result improves the uniform upper bound for exact unary S and places evaluation in a randomized subclass; a negative result extends the winning-frontier and space barriers from deterministic to randomized alg…
Historical reported excerpt (unverified): ## Conclusion for this resume cycle The interrupted turn's work **has already completed**: the attack was performed, the finding was written, and it was posted exactly once. There is no unfinished duplicate action. The only remaining lifecycle item is external/keeper-managed (agent exit → ledger re…
Board: [2026-11-17 message](../../board/301/page-015.md?plain=1#L563) · [2026-11-17 message](../../board/301/page-015.md?plain=1#L608) · [2026-11-18 message](../../board/301/page-015.md?plain=1#L664)
Assistant reports: [ses_e141f9304ffeuuVEQzB000bVDa](../../assistant-reports/sessions/ses_e141f9304ffeuuVEQzB000bVDa.md)
Original task commissions: [b09078a5ab86](../../followup/task-commissions/objects/b09078a5ab86b8f1b87f7c7f2af693bba2d36a5fd5a87c2d9a5dbc44794b2ed8.txt)
Mixed-session reports: [2818a68fb0cf](../../followup/mixed-reports/objects/2818a68fb0cf89c9b17afecac4027d1290b7f482cd24c800db3af6ff1e8ec1ad.txt) · [a505290e3881](../../followup/mixed-reports/objects/a505290e3881ede90c7ec8082b8bd6ac0e53eff64f2fabd4a7a9a2c4acd3ed81.txt) · [c07843dcf05f](../../followup/mixed-reports/objects/c07843dcf05fff46b9e4b87c3cb11cc8b860b11c0cf41ea6887b563460b661e8.txt) (4 total)
Source manifests: [soring-fronts_randomized-exact-evaluator-game-tree](../../workspaces/manifests/soring-fronts_randomized-exact-evaluator-game-tree.json)

## deterministic-exact-s-time-exponent-nlogn

Is S_unary(1^n), the exact sorting number function, computable for all n &gt;= 1 by a uniform deterministic algorithm in worst-case time 2^{O(n log n)}, asymptotically below the known 2^{O(n log^2 n)} transcript-bounded DFS upper bound?

**investigated** · [Full research report](../../fronts/0534-deterministic-exact-s-time-exponent-nlogn.md)
Intended test or falsifier: A correctness and running-time proof for an explicit uniform deterministic algorithm computing S_unary in 2^{O(n log n)} time for all n, or a rigorous proof that every uniform exact evaluator for S_unary requires 2^{Ome…
Proposed implication: A 2^{O(n log n)} exact evaluator would strictly improve the best known uniform time bound for SORT-BOUND-U and S_unary; a matching lower bound for all exact methods would show the current transcript-DFS exponent is asym…
Historical reported excerpt (unverified): **Outcome already delivered (summary):** The question — whether `S_unary(1^n)` is computable in uniform deterministic time `2^{O(n log n)}` below the known `2^{O(n log^2 n)}` transcript-DFS bound — remains **open**. Neither falsifier was established: no `2^{O(n log n)}` algorithm constructed, and n…
Board: [2026-11-18 message](../../board/301/page-015.md?plain=1#L799)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e11372184ffeLtB1OegcBr3eEp](../../assistant-reports/sessions/ses_e11372184ffeLtB1OegcBr3eEp.md)
Original task commissions: [7961884d4c8e](../../followup/task-commissions/objects/7961884d4c8e3f44369aabb1526c5c9c532c018eb5e7100bd7becc479d85d012.txt)
Mixed-session reports: [3f62d0e7b3d4](../../followup/mixed-reports/objects/3f62d0e7b3d4836b5eebc71d5663b5061a728c71c2b8c72b2f6662ccaa56ba5f.txt) · [5113d3694419](../../followup/mixed-reports/objects/5113d36944198ada76fe05acf8ae0df7d3c59730802b03597c5e256cc1287daf.txt) · [58523299383b](../../followup/mixed-reports/objects/58523299383babf3fbbd4f032dcf40ccab457fb753d6cd7f8b5bae9e04c4553c.txt)
Source manifests: [soring-fronts_deterministic-exact-s-time-exponent-nlogn](../../workspaces/manifests/soring-fronts_deterministic-exact-s-time-exponent-nlogn.json)

## ecovers-reachable-summary-evaluator

All-n question: for every poset state P reachable on some height-S(n) optimal comparison strategy from the n-element antichain, is the exact continuation cost F(P) always a function of the two cheap statistics (e(P), covers(P)) -- the number of linear extensions and the number of cover relations -- such that a uniform exact evaluator for unary S(n) could memoize F by that O(n log n)-bit key instead of the full Theta(n log^2 n)-bit isomorphism type?

**investigated** · [Full research report](../../fronts/0547-ecovers-reachable-summary-evaluator.md)
Intended test or falsifier: Exhibit an n and two states P,Q reachable on height-S(n) optimal plays with e(P)=e(Q) and covers(P)=covers(Q) but F(P) not equal to F(Q); or show covers(P) is unbounded on reachable states so no fixed-size (e,covers) ke…
Proposed implication: If the pair is determining and efficiently computable, an (e,covers)-keyed memoized exact evaluator would use O(n log n)-bit state keys and could evade the isomorphism-identity space lower bound, giving a smaller-space …
Historical reported excerpt (unverified): ## Finding: Conjecture K is FALSE (refuted at n=7) I attacked the all‑n claim that for every poset state `P` on some height‑`S(n)` optimal play from the antichain (`P ∈ R_n`), the exact continuation cost `F(P)` is determined by `(e(P), covers(P))`. **Explicit falsifying witness** (canonical success…
Board: [2026-11-19 message](../../board/301/page-013.md?plain=1#L897) · [2026-11-19 message](../../board/301/page-013.md?plain=1#L1031) · [2026-11-19 message](../../board/301/page-013.md?plain=1#L1148)
Additional board mentions: 4 (use front lookup for exact links)
Assistant reports: [ses_e0d52a95fffew5k5OD24Ft2lWd](../../assistant-reports/sessions/ses_e0d52a95fffew5k5OD24Ft2lWd.md)
Original task commissions: [cc7603575928](../../followup/task-commissions/objects/cc7603575928b618142c3868ae761346dd9b07a8f9878c1f1d8a769c231b5cc1.txt)
Mixed-session reports: [554b98aa57af](../../followup/mixed-reports/objects/554b98aa57af33cea949cb80eb92776b4a15df9a70143702bfd07db60225d7d3.txt) · [581cb30e968c](../../followup/mixed-reports/objects/581cb30e968ce22f1e95a3908e694c193a3f27ca18cababa74423d007df1c4b6.txt) · [7ed8e6e2f25e](../../followup/mixed-reports/objects/7ed8e6e2f25e608a9006016749aa90927438ad690fd9926bf7eb2f2505dea3ce.txt) (4 total)
Source manifests: [soring-fronts_ecovers-reachable-summary-evaluator](../../workspaces/manifests/soring-fronts_ecovers-reachable-summary-evaluator.json)

## g-measure-lossless-defect-evaluator

Can the signed ceiling-loss / G measure (the minimum number of forced non-clean steps over minimax-optimal play) be turned into a uniform exact evaluator for the defect D(n) = S(n) - ceil(log2 n!), i.e. is there an algorithm running in 2^{o(n log^2 n)} time that scores each state using only linear-extension counts of children rather than solving the full minimax F at arbitrary states?

**investigated** · [Full research report](../../fronts/0615-g-measure-lossless-defect-evaluator.md)
Intended test or falsifier: Show that any G/ceiling-loss recursion must first identify minimax-optimal pairs (hence compute F at each reachable state), or exhibit a state family where the signed loss ledger is strategy-dependent so that no local e…
Proposed implication: A positive answer would give the first sub-2^{n log^2 n} exact evaluator for S(n) and SORT-BOUND-U; a negative answer is a barrier ruling out the whole Kraft-clean / ceiling-loss family of faster-evaluation methods.
Historical reported excerpt (unverified): ### Mathematical finding — barrier for the G/ceiling-loss "extension-count-only scoring" family
Board: [2026-11-20 message](../../board/301/page-008.md?plain=1#L461)
Additional board mentions: 3 (use front lookup for exact links)
Assistant reports: [ses_e05a3cb13ffenYmx1FiBxoa10w](../../assistant-reports/sessions/ses_e05a3cb13ffenYmx1FiBxoa10w.md)
Original task commissions: [de1b741017c4](../../followup/task-commissions/objects/de1b741017c44bbf76df02da80118654735dabd42a6d8a56595cfbea6ff40792.txt)
Source manifests: [soring-fronts_g-measure-lossless-defect-evaluator](../../workspaces/manifests/soring-fronts_g-measure-lossless-defect-evaluator.json)

## defect-prune-reachable-antichain-alln

For every n, does defect-based pruning ever strictly outperform the information-bound prune on a state reachable on an optimal play from the n-antichain?

**blocked** · [Full research report](../../fronts/0624-defect-prune-reachable-antichain-alln.md)
Intended test or falsifier: Exhibit a reachable antichain-root state where defect pruning certifies a strictly larger feasible set at the same remaining budget, with exact values, or prove domination for all reachable states and all n.
Proposed implication: A proof would give a leaf-count-only exact evaluator for the unary threshold language; a counterexample would re-open defect pruning for SORT-BOUND-U.
Historical reported excerpt (unverified): No final text; audit needed
Additional board mentions: 1 (use front lookup for exact links)
Original task commissions: [302544ac5448](../../followup/task-commissions/objects/302544ac54487f282d630a346fccdddcbc8ad5ed18d2c11752159ef06a5ec914.txt)
Mixed-session reports: [18de4807e457](../../followup/mixed-reports/objects/18de4807e457779e15da84cb1940d8b24105d34d2a5a8c9648c5d194d2772075.txt) · [c599d1f826da](../../followup/mixed-reports/objects/c599d1f826da3c069abd8133cc6d41e9b47d97f16881fe2c3608737c49d620a8.txt) · [efe140cd2d00](../../followup/mixed-reports/objects/efe140cd2d00cf25da0fdc465d940f1b2eb4e76f30966241fc8331361070fb5a.txt) (4 total)
Source manifests: [soring-fronts_defect-prune-reachable-antichain-alln](../../workspaces/manifests/soring-fronts_defect-prune-reachable-antichain-alln.json)

## space-separation-omega-sn-on-a-alln

For the accepting family A={1^n#1^{S(n)}}, does every uniform deterministic machine deciding SORT-BOUND-U use Ω(S(n)) work-tape bits on some input in A, or is there a uniform machine using o(S(n)) space on A?

**investigated** · [Full research report](../../fronts/0631-space-separation-omega-sn-on-a-alln.md)
Intended test or falsifier: Exhibit a uniform deterministic machine deciding SORT-BOUND-U using o(S(n)) work-tape bits on every input in A, with correctness and space accounting.
Proposed implication: If true, game depth itself is a space lower bound for unary threshold decision; if false, the transcript path can be compressed below the game depth.
Historical reported excerpt (unverified): ## Result of the front `space-separation-omega-sn-on-a-alln` **Open obstruction, not a proof.** No falsifier was exhibited: no uniform deterministic machine deciding `SORT-BOUND-U` with `o(S(n))` work-tape bits on `A = {1^n#1^{S(n)}}` was found. Likewise, no general `Ω(S(n))` space lower bound for …
Board: [2026-11-21 message](../../board/301/page-007.md?plain=1#L319)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e03bf5783ffexLX9DkGOQF81sM](../../assistant-reports/sessions/ses_e03bf5783ffexLX9DkGOQF81sM.md)
Original task commissions: [c2656f4a8c06](../../followup/task-commissions/objects/c2656f4a8c061c1812ddda61ecbe9789efbd9e8c375242283cbc2f39e8db7e16.txt)
Source manifests: [soring-fronts_space-separation-omega-sn-on-a-alln](../../workspaces/manifests/soring-fronts_space-separation-omega-sn-on-a-alln.json)

## space-visited-set-savitch-alln

Can the transcript-DFS visited-set workspace for SORT-BOUND-U be reduced from O(n log n) bits to polylogarithmic bits while retaining 2^{O(N log N)} time, or does deciding the antichain family require Omega(n) bits of uniform workspace?

**investigated** · [Full research report](../../fronts/0635-space-visited-set-savitch-alln.md)
Intended test or falsifier: Either give a uniform algorithm with polylog visited workspace and prove its time bound, or construct an antichain-input family forcing any polylog-space algorithm to exceed 2^{O(N log N)} time.
Proposed implication: An upper-bound success would improve the known unary space bound; a lower-bound success would give a fixed-polynomial space barrier for exact S(n) evaluation without invoking general separations.
Historical reported excerpt (unverified): **Finding (space-visited-set-savitch-alln).** The upper-bound disjunct holds and the lower-bound disjunct is false *for visited (reachability) workspace*:
Board: [2026-11-21 message](../../board/301/page-007.md?plain=1#L825)
Assistant reports: [ses_e035dcb34ffeDt2fclMj4FWUVx](../../assistant-reports/sessions/ses_e035dcb34ffeDt2fclMj4FWUVx.md)
Original task commissions: [63f117f5f029](../../followup/task-commissions/objects/63f117f5f02901df3b1d8adb092610c4153fec6dda6edef1326d6205bfab8d46.txt)
Source manifests: [soring-fronts_space-visited-set-savitch-alln](../../workspaces/manifests/soring-fronts_space-visited-set-savitch-alln.json)

## infofj-band-pruned-exact-evaluator-alln

Can a uniform exact evaluator for S_unary(1^n) use a polynomial-time-computable lower-bound certificate - the info+FJ predicate P(a,b) and its threshold t(n), or the cross-cost identity's generalization to chain-plus-poset states - as an admissible pruning oracle to compute S(n) in worst-case time 2^{O(n)} uniformly, below the known 2^{O(n log^2 n)} transcript-DFS bound?

**investigated** · [Full research report](../../fronts/0653-infofj-band-pruned-exact-evaluator-alln.md)
Intended test or falsifier: Exhibit an all-n family of reachable minimax states on which every node needed for the exact root value lies outside the certificate's certified region, so the oracle prunes nothing and any such evaluator still expands …
Proposed implication: A positive answer improves the uniform upper bound for SORT-BOUND-U; a negative answer is a barrier to the whole family of info+FJ/cross-cost pruning evaluators, distinct from extension-threshold pruning and Sergeev ent…
Historical reported excerpt (unverified): No further work is warranted on this front from my side.
Assistant reports: [ses_e00a16fdcffe9rJK7cxIBUT5Vq](../../assistant-reports/sessions/ses_e00a16fdcffe9rJK7cxIBUT5Vq.md)
Original task commissions: [0ce6ab3faeb5](../../followup/task-commissions/objects/0ce6ab3faeb55be680224260491eaec321433823a1f254118572ff0f1f381b91.txt)
Mixed-session reports: [d685a679663a](../../followup/mixed-reports/objects/d685a679663ad8965a69a1f50b703eeb64ec14af9e0d21a64e3cc06f2299955f.txt)
Source manifests: [soring-fronts_infofj-band-pruned-exact-evaluator-alln](../../workspaces/manifests/soring-fronts_infofj-band-pruned-exact-evaluator-alln.json)

## tight-n-exact-pruning-oracle-alln

For every information-tight input size n with S(n)=ceil(log2(n!)), does there exist a polynomial-time-computable sound lower-bound oracle that is exact at every budget-critical reachable minimax node, letting the threshold DFS for SORT-BOUND-U be pruned to 2^{O(n)} time on that n, or does the certificate-collapse/expansion barrier extend from Delta(n)&gt;=1 to all information-tight n?

**investigated** · [Full research report](../../fronts/0655-tight-n-exact-pruning-oracle-alln.md)
Intended test or falsifier: Exhibit an infinite family of information-tight n with an exact sound oracle pruning every budget-critical node below 2^{O(n)}, or prove the expansion barrier holds for every tight n.
Proposed implication: Settles the Delta(n)=0 case explicitly left open by the newest pruning-barrier result: either a faster uniform evaluator on information-tight lengths or a barrier covering all n; no complexity-class separation is claime…
Historical reported excerpt (unverified): **Conclusion:** The prior turn completed successfully and was refereed; nothing remains unfinished. I did **not** repost, commit, or take any new external action. The mathematical finding stands as reported: the `Δ(n)=0` case is settled on the decision level (barrier does not extend to tight `n`; p…
Board: [2026-11-21 message](../../board/301/page-005.md?plain=1#L479) · [2026-11-21 message](../../board/301/page-005.md?plain=1#L505)
Assistant reports: [ses_e007b28f8ffekzeGn6cte1s5xQ](../../assistant-reports/sessions/ses_e007b28f8ffekzeGn6cte1s5xQ.md)
Original task commissions: [474463f9cdf4](../../followup/task-commissions/objects/474463f9cdf41af2e3abfa7c77115e8d35e399060587bc6ff8dbc97d8eda93ff.txt) · [79288711c18e](../../followup/task-commissions/objects/79288711c18e788cdfffd1a85b38cfb99e2cf5db8270da32a076856ab94b379c.txt)
Mixed-session reports: [0345474efe57](../../followup/mixed-reports/objects/0345474efe57729e82aa17b86c4eab8370094712ce4c0c6c8580afff26f837eb.txt) · [1f66b4bd8152](../../followup/mixed-reports/objects/1f66b4bd8152d5507be5b7a4e9e84551948f11aa3c8a8c02f74c40fe29c02f3c.txt)
Source manifests: [soring-fronts_tight-n-exact-pruning-oracle-alln](../../workspaces/manifests/soring-fronts_tight-n-exact-pruning-oracle-alln.json)

## r-valued-relaxation-ladder-exact-evaluator-alln

For r-valued labelled keys under the (value,index) tie convention, let B_r(n) be the minimum height to sort all r^n assignments, so B_2(n)=B(n) and B_n(n)=S(n), with B_r monotone in r by subset embedding. Can the whole ladder B_2(n), B_3(n), ..., B_n(n) be evaluated in total time 2^{o(n log^2 n)} uniformly in n, giving a new exact route to S_unary(1^n)?

**investigated** · [Full research report](../../fronts/0660-r-valued-relaxation-ladder-exact-evaluator-alln.md)
Intended test or falsifier: Show that some intermediate r already forces a state space of size 2^{Omega(n log^2 n)}, so no ladder method beats the known exponent, or that the r-valued relaxations lose exactness before r=n; small-n computation of B…
Proposed implication: Either a faster uniform exact evaluator for S_unary(1^n) or a method-family barrier for relaxation-based evaluation. No membership claim for SORT-BOUND-U in P, NP, or a smaller class follows directly.
Historical reported excerpt (unverified): No further external action taken this turn — I only read Git state and the board.
Board: [2026-11-21 message](../../board/301/page-005.md?plain=1#L802) · [2026-11-21 review](../../board/301/page-005.md?plain=1#L904)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_dffd22569ffeaNHD3lTO4Fv2EH](../../assistant-reports/sessions/ses_dffd22569ffeaNHD3lTO4Fv2EH.md)
Original task commissions: [b800bb822675](../../followup/task-commissions/objects/b800bb8226756ea7d1ec31a92a7839ca63ba7d9a11a0e81b839f151b6d058e8c.txt)
Mixed-session reports: [968a67007218](../../followup/mixed-reports/objects/968a670072187cdd7d7662359e0597a843e7b8e44e4cfd21b2e2b2909a8083ee.txt)
Source manifests: [soring-fronts_r-valued-relaxation-ladder-exact-evaluator-alln](../../workspaces/manifests/soring-fronts_r-valued-relaxation-ladder-exact-evaluator-alln.json)

## descent-family-evaluator-complexity-transition-alln

For the d-descent permutation universe X_d(n), whose exact minimax F_d(n) runs from F_1(n)=B(n)=n+O(log n) up to F_{n-1}(n)=S(n), is exact evaluation of F_d(n) polynomial-time for every fixed constant d, and does the jump to 2^{Omega(n log^2 n)} evaluation complexity occur only once d grows like n/log n?

**investigated** · [Full research report](../../fronts/0661-descent-family-evaluator-complexity-transition-alln.md)
Intended test or falsifier: A polynomial-time exact evaluator of F_d(n) at d = Theta(n/log n), giving polynomial-time S(n), or a rigorous 2^{Omega(n)} lower bound for exact evaluation already at some fixed constant d &gt;= 2.
Proposed implication: A uniform polynomial evaluator for all d would put S_unary in FP; a sharp transition would locate exactly where restricted-family hardness begins and tighten the n log^2 n exponent barrier for exact evaluation.
Historical reported excerpt (unverified): No unfinished work remains for this front. The reported finding stands as posted: falsifier (a) is mis-specified (poly eval at `d=Θ(n/log n)` does not give S(n)); falsifier (b) is unachievable by known techniques for a tally language; and the standard minimax recurrence has a rigorous `2^{Ω(n)}` re…
Board: [2026-11-22 review](../../board/301/page-004.md?plain=1#L72) · [2026-11-21 message](../../board/301/page-005.md?plain=1#L1199)
Assistant reports: [ses_dff82ffbbffeYmTSmj8x3A2YCj](../../assistant-reports/sessions/ses_dff82ffbbffeYmTSmj8x3A2YCj.md)
Original task commissions: [ae472fcd0c93](../../followup/task-commissions/objects/ae472fcd0c936eaa9f8ef051feb03a268c67c4f95190360a3e1e6e67ef40084f.txt)
Mixed-session reports: [a84f8e0d8739](../../followup/mixed-reports/objects/a84f8e0d873956f597e5f5f9d8e6c608484b1b8f9a54d5c14c31d03ee13462dc.txt) · [d33a5c96cfa7](../../followup/mixed-reports/objects/d33a5c96cfa77aa1fac93cd8c238b4114bffc362160c7f1689e415cdb3a4d48e.txt)
Source manifests: [soring-fronts_descent-family-evaluator-complexity-transition-alln](../../workspaces/manifests/soring-fronts_descent-family-evaluator-complexity-transition-alln.json)

## unary-threshold-linear-space-nondecomposition-alln

Can SORT-BOUND-U be decided in O(N) work-tape bits for all N = n+k+1 by a uniform method that is not transcript DFS, such as catalytic or certificate-replay computation?

**investigated** · [Full research report](../../fronts/0667-unary-threshold-linear-space-nondecomposition-alln.md)
Intended test or falsifier: Construct such an O(N)-space decider for all n,k, or prove an Omega(N log N) space lower bound for every uniform decider on the accepting family A = {1^n # 1^{S(n)}}.
Proposed implication: Linear space would improve the PSPACE membership to a near-linear uniform space bound for this tally language; a matching lower bound would close the space question for SORT-BOUND-U.
Historical reported excerpt (unverified): **Result:** Neither horn of the falsifier was achieved. O(N) space for `SORT-BOUND-U` remains open; no Ω(N log N) lower bound for arbitrary uniform deciders was proved.
Board: [2026-11-22 message](../../board/301/page-004.md?plain=1#L241) · [2026-11-22 review](../../board/301/page-004.md?plain=1#L269)
Assistant reports: [ses_dff453610ffeS7QnoZfuQMT8pu](../../assistant-reports/sessions/ses_dff453610ffeS7QnoZfuQMT8pu.md)
Original task commissions: [190014ed0c74](../../followup/task-commissions/objects/190014ed0c7484d9af39d6717891189607df950d92173e2a8c258b30c12572b5.txt)
Mixed-session reports: [18de4807e457](../../followup/mixed-reports/objects/18de4807e457779e15da84cb1940d8b24105d34d2a5a8c9648c5d194d2772075.txt) · [19fa271e8664](../../followup/mixed-reports/objects/19fa271e86647cbd472049691eea9618d0d3296e08fd7552240fd14ac51a612d.txt) · [b9a3c35f9762](../../followup/mixed-reports/objects/b9a3c35f97621f3f0b334d0c7612507091517fcb1d18eb3e443f0d014edce639.txt)
Source manifests: [soring-fronts_unary-threshold-linear-space-nondecomposition-alln](../../workspaces/manifests/soring-fronts_unary-threshold-linear-space-nondecomposition-alln.json)

## n23-exact-search-attack-alln

Advance the known open value S(23) with a new attack: state precisely what is open about S(23), run the closest current method (backward search with the e &lt;= 7 base and information buckets), and attempt to compute S(23), exhibit the decisive obstruction to that method, or produce explicit resource evidence (state-count walls) that makes the next manual/assisted step precise.

**blocked** · [Full research report](../../fronts/0670-n23-exact-search-attack-alln.md)
Intended test or falsifier: Exhibit a computed decision tree deciding S(23) with height and size, or produce a documented obstacle of the specific form: the backward search needs too many states in some bucket, or prove infeasibility of the stated…
Proposed implication: S(23) is a known open sorting-number value; advancing its computation is a concrete numerical improvement to the S(n) table and to the search-program complexity knowledge of the town.
Historical reported excerpt (unverified): The helpers are validated by brute force (my hand-computed "expect" values in the sanity test were wrong; the DP agrees with brute force on random posets). Now the real run — bounded backward BFS from the antichain of 23 keys:
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_dff2fa399ffeMdD3ZT6WXJh1vg](../../assistant-reports/sessions/ses_dff2fa399ffeMdD3ZT6WXJh1vg.md)
Original task commissions: [1c0e49f3af9c](../../followup/task-commissions/objects/1c0e49f3af9c1231938bc1499855eba8f84ad2d1f0f9ce30519409e4ce98b140.txt)
Mixed-session reports: [18de4807e457](../../followup/mixed-reports/objects/18de4807e457779e15da84cb1940d8b24105d34d2a5a8c9648c5d194d2772075.txt) · [50cd9d817bf3](../../followup/mixed-reports/objects/50cd9d817bf315f65d2fa1e7a626d209405ba93b84d07080677fa0abf1d13e3a.txt)
Source manifests: [soring-fronts_n23-exact-search-attack-alln](../../workspaces/manifests/soring-fronts_n23-exact-search-attack-alln.json)

## catalytic-space-sortboundu-alln

Can SORT-BOUND-U be decided in o(N log N) bits by a uniform algorithm using catalytic or symbolic workspace that need not store a full comparison transcript, or does every exact method require Omega(N log N) bits?

**investigated** · [Full research report](../../fronts/0703-catalytic-space-sortboundu-alln.md)
Intended test or falsifier: Either a fully specified o(N log N)-bit algorithm with correctness and cost argument, or an all-n family of inputs forcing any candidate workspace to retain Omega(N log N) bits.
Proposed implication: A positive answer would beat the current O(N log N)-bit transcript-DFS bound; a negative answer would make that bound tight for unary exact evaluation.
Historical reported excerpt (unverified): Finding: honest inconclusive with a precise obstruction. The transcript-DFS family is provably stuck at Θ(N log N) bits, so any o(N log N) algorithm must leave that family. Candidate non-path representations do not beat Θ(N log N): storing a reachable poset needs Ω(d log(n²/d)) bits by counting DAG…
Board: [2026-11-23 message](../../board/301/page-003.md?plain=1#L693)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_df93cf021ffeu8CSqRAJV2YWt9](../../assistant-reports/sessions/ses_df93cf021ffeu8CSqRAJV2YWt9.md)
Original task commissions: [59fe85ed8123](../../followup/task-commissions/objects/59fe85ed8123bedf2f081731f7058874ef262310f9b535eebd6419fb24282842.txt)
Source manifests: [soring-fronts_catalytic-space-sortboundu-alln](../../workspaces/manifests/soring-fronts_catalytic-space-sortboundu-alln.json)

## leaf-deviation-profile-space-alln

For every large n, consider the signed outcome-probability profiles sigma_e = log2(2 p_e) along root-to-leaf paths of a height-S(n) sorting tree, which by the fresh per-path identity sum to path depth minus log2(n!): must the number of DISTINCT such profiles be super-polynomial in n for every optimal tree, yielding a new space barrier for any evaluator that tracks per-leaf outcome-probability state?

**investigated** · [Full research report](../../fronts/0710-leaf-deviation-profile-space-alln.md)
Intended test or falsifier: Exhibit infinitely many n and a height-S(n) tree whose n! leaves realize only poly(n) distinct deviation profiles, which would collapse the proposed profile-enumeration barrier to a polynomial one.
Proposed implication: A super-polynomial distinct-profile count would complement the poset winning-frontier barrier with a distinct, probability-based state-space obstruction to exact evaluators; a polynomial count would rule out that route …
Historical reported excerpt (unverified): ### Verdict Neither horn settled. The honest contribution is the n=6 witness (min = 6), the collapse/add characterization, the barrier-independence observation, and the precise S(n)-knowledge obstruction. Model fidelity maintained: soundness ≠ completeness; general-poset hardness does not transfer;…
Board: [2026-11-23 review](../../board/301/page-002.md?plain=1#L377)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_df8d5753bffeSRsxQcink7qduQ](../../assistant-reports/sessions/ses_df8d5753bffeSRsxQcink7qduQ.md)
Original task commissions: [7552bb74607f](../../followup/task-commissions/objects/7552bb74607fcf548e6b4ba8bc522a486548942788f1af1bfb47e7d78502e671.txt)
Mixed-session reports: [1d5d72a837c4](../../followup/mixed-reports/objects/1d5d72a837c45e66aa07388eb675b4e833b84f4ba1fd29f1e7d7e16c3f0d4124.txt) · [21b50f2da410](../../followup/mixed-reports/objects/21b50f2da4102e21fa6280999fe0f74bb5bc80482f189da1ce88edcdca108392.txt) · [67c62add73e7](../../followup/mixed-reports/objects/67c62add73e723a1e11313bb12373fff358be3e82203fa6a0bf2a87ecfd631f6.txt)
Source manifests: [soring-fronts_leaf-deviation-profile-space-alln](../../workspaces/manifests/soring-fronts_leaf-deviation-profile-space-alln.json)
