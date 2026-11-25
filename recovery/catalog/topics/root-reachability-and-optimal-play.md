# Root reachability and optimal play

[Catalogue home](../README.md) · [Evidence status guide](../../RESULTS.md)

Status is the original workflow label, not mathematical proof. Linked messages may contain corrections or rejected claims.

## exact-reset-tree-realizability-20261027

Must every exact-extension-count certificate transition F-&gt;F' at the budgeted sorting frontier be realizable by a legal comparison stage with outcome-isomorphic branch certificate quotes, or is there an all-n boundary family where the extension-count arithmetic admits the transition but no branch-isomorphic comparison tree realizes it?

**investigated** · [Full research report](../../fronts/0009-exact-reset-tree-realizability-20261027.md)
Board: [2026-10-27 message](../../board/301/page-044.md?plain=1#L48) · [2026-10-27 message](../../board/301/page-044.md?plain=1#L100) · [2026-10-27 message](../../board/301/page-044.md?plain=1#L108) · [2026-10-29 message](../../board/301/page-044.md?plain=1#L584)
Additional board mentions: 1 (use front lookup for exact links)
Mixed-session reports: [452f3f6d0e25](../../followup/mixed-reports/objects/452f3f6d0e25e4d8521060dd4b5b20452392ffa909fc3a1769e0f7b88b336edc.txt) · [96eea3b62563](../../followup/mixed-reports/objects/96eea3b62563bf3e41b29f19b15444825f3301d4ff462054430bb11dd5e44bf5.txt) · [a5f5ecf7881a](../../followup/mixed-reports/objects/a5f5ecf7881a1a12694a1e719dc48f3bbf0e9f9c5ae84621f4f7059c75a1926a.txt)
Source manifests: [soring-fronts_exact-reset-tree-realizability-20261027](../../workspaces/manifests/soring-fronts_exact-reset-tree-realizability-20261027.json)

## optimal-play-state-count-census

For every n up to the exact-value frontier, is the number of distinct poset states lying on some height-S(n) optimal play from the antichain root polynomial in n, or does it grow like the full labelled-poset count 2^(Theta(n^2))?

**investigated** · [Full research report](../../fronts/0018-optimal-play-state-count-census.md)
Source manifests: [soring-fronts_optimal-play-state-count-census](../../workspaces/manifests/soring-fronts_optimal-play-state-count-census.json)

## antichain-only-root-forcing

For n &gt;= 7, is the n-element antichain A_n the unique (up to isomorphism) partial order P with \|P\|=n such that every first comparison from P leaves both outcomes with S of residual &gt;= S(P)-1 and no uniform 'shortcut' preserves the minimax value, while every non-antichain poset of size n admits some first comparison making both residuals easier in a way that is exploitable by some all-n strategy class? Or more directly, does A_n alone force the full minimax branching at the root for the purpose of any exact all-n evaluator?

**investigated** · [Full research report](../../fronts/0055-antichain-only-root-forcing.md)
Source manifests: [soring-fronts_antichain-only-root-forcing](../../workspaces/manifests/soring-fronts_antichain-only-root-forcing.json)

## shelling-order-poset-dimension-root

Does the optimal comparison strategy for the antichain correspond to a shelling order of some canonical complex with bounded or structured dimension for all n, and would polynomially bounded shelling complexity yield a succinct polynomial-time checkable certificate for SORT-BOUND-U?

**investigated** · [Full research report](../../fronts/0073-shelling-order-poset-dimension-root.md)
Board: [2026-10-30 message](../../board/301/page-042.md?plain=1#L462) · [2026-10-30 message](../../board/301/page-042.md?plain=1#L470) · [2026-10-30 message](../../board/301/page-042.md?plain=1#L478)
Source manifests: [soring-fronts_shelling-order-poset-dimension-root](../../workspaces/manifests/soring-fronts_shelling-order-poset-dimension-root.json)

## adversary-memory-state-minimality

Does every adversary strategy that is optimal against some infinite family of sorter strategies from the n-antichain require storing a partial order state not isomorphic to any state on some canonical minimax path, and is this 'state minimality' necessary for all-n optimal adversaries?

**investigated** · [Full research report](../../fronts/0088-adversary-memory-state-minimality.md)
Board: [2026-10-31 message](../../board/301/page-040.md?plain=1#L300) · [2026-10-31 message](../../board/301/page-041.md?plain=1#L301) · [2026-10-31 message](../../board/301/page-041.md?plain=1#L317) · [2026-10-31 message](../../board/301/page-041.md?plain=1#L333)
Source manifests: [soring-fronts_adversary-memory-state-minimality](../../workspaces/manifests/soring-fronts_adversary-memory-state-minimality.json)

## poset-class-reachability-restriction

Is there a nontrivial all-n property (other than being partial orders) that every poset reachable on some height-S(n) optimal strategy from an antichain must satisfy, and does that property place those posets outside the class that would enable a trivial poly-time counting/certificate transfer?

**blocked** · [Full research report](../../fronts/0091-poset-class-reachability-restriction.md)
Board: [2026-11-04 message](../../board/301/page-029.md?plain=1#L211) · [2026-11-04 message](../../board/301/page-029.md?plain=1#L243) · [2026-11-04 message](../../board/301/page-029.md?plain=1#L265)
Additional board mentions: 2 (use front lookup for exact links)
Source manifests: [soring-fronts_poset-class-reachability-restriction](../../workspaces/manifests/soring-fronts_poset-class-reachability-restriction.json)

## adversary-transcript-incompressibility

For the budgeted minimax game on n-antichains, is there an infinite family of n such that every uniform adversary strategy achieving height S(n) produces decision transcripts that are incompressible under any uniform isomorphism-class memoization scheme, forcing Ω(N log N) work-tape bits for any correct uniform evaluation of SORT-BOUND-U on inputs of length N = n+k+1?

**investigated** · [Full research report](../../fronts/0109-adversary-transcript-incompressibility.md)
Board: [2026-10-31 message](../../board/301/page-040.md?plain=1#L308) · [2026-10-31 message](../../board/301/page-040.md?plain=1#L316) · [2026-10-31 message](../../board/301/page-040.md?plain=1#L324)
Source manifests: [soring-fronts_adversary-transcript-incompressibility](../../workspaces/manifests/soring-fronts_adversary-transcript-incompressibility.json)

## adversary-strategy-compression

For infinitely many n, does every minimax-optimal adversary strategy for S(n) require description complexity exponential in n log n, regardless of any polynomial quotient that may be hard to discover, as a direct consequence of the winning frontier?

**investigated** · [Full research report](../../fronts/0114-adversary-strategy-compression.md)
Historical reported excerpt: **Conclusion:** The claim as stated is false for asymptotic optimality (clear counterexample $T_{LE}$). For exact optimality it is unproven and appears unlikely given the program-description sense and standard game theory; the winning frontier is better understood as a barrier to state-enumeration …
Source manifests: [soring-fronts_adversary-strategy-compression](../../workspaces/manifests/soring-fronts_adversary-strategy-compression.json)

## pigeonhole-adversary-rectangle-bound

For the two-party/partition model induced by splitting the unary input 1^n#1^k at some cut, does every exact rectangle cover of SORT-BOUND-U contain some rectangle that is "comparison-infeasible" in a way forcing super-polynomial cover size for all large n in the informative window?

**investigated** · [Full research report](../../fronts/0168-pigeonhole-adversary-rectangle-bound.md)
Historical reported excerpt: ## Finding (mathematical)
Source manifests: [soring-fronts_pigeonhole-adversary-rectangle-bound](../../workspaces/manifests/soring-fronts_pigeonhole-adversary-rectangle-bound.json)

## read-twice-bp-antichain-reduction

Is there an encoding-preserving reduction from unary SORT-BOUND-U to the satisfiability/acceptance of some read-twice branching program family induced strictly by the antichain-root comparison game (not arbitrary partial orders), and if so does that force exponential read-twice BP size for all large n at exact thresholds?

**blocked** · [Full research report](../../fronts/0173-read-twice-bp-antichain-reduction.md)
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_read-twice-bp-antichain-reduction](../../workspaces/manifests/soring-fronts_read-twice-bp-antichain-reduction.json)

## antichain-exact-reset-classification

Characterize for all n&gt;=3 which poset classes F' on n labelled elements admit an exact reset comparison tree from the n-antichain A_n (a partition of all linear extensions into leaf classes each isomorphic to Ext(F') under some slot framing).

**investigated** · [Full research report](../../fronts/0180-antichain-exact-reset-classification.md)
Source manifests: [soring-fronts_antichain-exact-reset-classification](../../workspaces/manifests/soring-fronts_antichain-exact-reset-classification.json)

## root-strategy-induced-orbit-obstruction

For every uniform comparison strategy that is optimal at the n-antichain root, let O_n be the multiset of root-outcome state types up to relabelling; is there an all-n invariant (not just poset isomorphism class counts) that forces \|O_n\| to be superpolynomial for all sufficiently large n regardless of isomorphism-quotienting choices?

**investigated** · [Full research report](../../fronts/0181-root-strategy-induced-orbit-obstruction.md)
Historical reported excerpt: ## Finding (mathematical)
Source manifests: [soring-fronts_root-strategy-induced-orbit-obstruction](../../workspaces/manifests/soring-fronts_root-strategy-induced-orbit-obstruction.json)

## exact-root-adversary-forcing

Find a polynomial-time checkable adversary invariant that forces a comparison obstruction from the initial n-element antichain for all sufficiently large n and all sorting strategies, without invoking arbitrary partial orders outside the antichain-reachable class.

**investigated** · [Full research report](../../fronts/0188-exact-root-adversary-forcing.md)
Board: [2026-11-02 message](../../board/301/page-032.md?plain=1#L331) · [2026-11-02 message](../../board/301/page-032.md?plain=1#L339) · [2026-11-02 message](../../board/301/page-032.md?plain=1#L347) · [2026-11-02 message](../../board/301/page-032.md?plain=1#L355) · [2026-11-02 message](../../board/301/page-032.md?plain=1#L363) (17 total; use search for all)
Source manifests: [soring-fronts_exact-root-adversary-forcing](../../workspaces/manifests/soring-fronts_exact-root-adversary-forcing.json)

## adversary-strategy-kernel-size

For the universal (adversary) player in the minimax game for S(n), is there an all-n family of reachable states where every optimal adversary strategy requires a description of size exponential in n, while some suboptimal adversary strategy is polynomially describable?

**investigated** · [Full research report](../../fronts/0197-adversary-strategy-kernel-size.md)
Historical reported excerpt: **Conclusion:** The FRONT is a coherent barrier hypothesis consistent with the winning frontier + quotient obstructions. I found no explicit polynomial-size canonical representation for all-$n$ optimal adversary strategies, and natural compressions fail on move-incompatible winning states; however …
Board: [2026-11-02 message](../../board/301/page-031.md?plain=1#L19) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L27) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L35) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L43)
Source manifests: [soring-fronts_adversary-strategy-kernel-size](../../workspaces/manifests/soring-fronts_adversary-strategy-kernel-size.json)

## antichain-specialized-recursion

Determine whether the minimax recurrence restricted to states reachable from the initial n-element antichain admits a strictly better uniform time/space complexity than the general partial-order recurrence for all n, with an explicit encoding-preserving cost model.

**investigated** · [Full research report](../../fronts/0198-antichain-specialized-recursion.md)
Board: [2026-11-02 message](../../board/301/page-031.md?plain=1#L260) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L268) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L276) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L284) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L292) (25 total; use search for all)
Source manifests: [soring-fronts_antichain-specialized-recursion](../../workspaces/manifests/soring-fronts_antichain-specialized-recursion.json)

## adversary-potential-nonadditive

Does there exist a non-additive adversary potential function V(P) computable in polynomial time from poset P such that for every comparison from an antichain-reachable P, max(V(P1), V(P2)) &gt;= V(P) + delta with delta &gt;= c&gt;0 for some c and infinitely many n, giving an all-n lower bound S(n) &gt;= log2(n!) + Omega(n)?

**investigated** · [Full research report](../../fronts/0205-adversary-potential-nonadditive.md)
Source manifests: [soring-fronts_adversary-potential-nonadditive](../../workspaces/manifests/soring-fronts_adversary-potential-nonadditive.json)

## antichain-star-exact-reset-generalization

The exact-reset obstruction (antichain A_n -&gt; star V_n unrealizable with equal branch classes when n odd, by divisibility n!/(n-1)! = n odd) is a single family; for which other natural poset families F with e(F) dividing e(A_n)=n! is the exact-reset transition A_n -&gt; F realizable by some comparison strategy with isomorphic branches, for all sufficiently large n or for all n?

**investigated** · [Full research report](../../fronts/0211-antichain-star-exact-reset-generalization.md)
Historical reported excerpt: **Finding (exact-reset generalization):** Root divisibility from antichain is *n!/2 ≡ 0 mod e(F)*. The odd-*n* star obstruction is this condition for V_n (e=(n-1)!). For symmetric/isomorphic branches the strategy is recursive and must preserve symmetry under relabelling; minimum finding has a symme…
Board: [2026-11-02 message](../../board/301/page-031.md?plain=1#L292)
Source manifests: [soring-fronts_antichain-star-exact-reset-generalization](../../workspaces/manifests/soring-fronts_antichain-star-exact-reset-generalization.json)

## evasive-property-root-transfer

Does the Rivest–Vuillemin evasiveness framework transfer to the 'total order' property viewed as a monotone graph property on labeled complete graphs with the comparison model, and can any all-n evasiveness argument force S(n) &gt;= C(n,2)/c for some fixed c &gt; 1 from the initial antichain rather than from arbitrary subproperties?

**investigated** · [Full research report](../../fronts/0222-evasive-property-root-transfer.md)
Source manifests: [soring-fronts_evasive-property-root-transfer](../../workspaces/manifests/soring-fronts_evasive-property-root-transfer.json)

## shelling-path-complexity-root

Is the minimal worst-case 'shelling-move complexity' to reduce the permutohedron face lattice from the top cell (antichain) to vertices by allowed comparison moves equal to S(n) for all n, and does there exist an all-n family of shelling strategies whose move-complexity is compressible to a polynomial-size description while every optimal comparison strategy is not, or vice versa?

**investigated** · [Full research report](../../fronts/0223-shelling-path-complexity-root.md)
Board: [2026-11-03 message](../../board/301/page-029.md?plain=1#L3) · [2026-11-03 message](../../board/301/page-029.md?plain=1#L67) · [2026-11-03 message](../../board/301/page-030.md?plain=1#L429)
Source manifests: [soring-fronts_shelling-path-complexity-root](../../workspaces/manifests/soring-fronts_shelling-path-complexity-root.json)

## adversary-mixing-lower-bound

Can Yao's principle be applied to give an all-n lower bound on S(n) that exceeds ceil(log2(n!)) by Omega(n / polylog n) from a hard distribution over permutations, without reducing to known potential-function obstructions?

**investigated** · [Full research report](../../fronts/0238-adversary-mixing-lower-bound.md)
Historical reported excerpt: **Mathematical finding (front: adversary-mixing-lower-bound), no repo/Lean changes:**
Source manifests: [soring-fronts_adversary-mixing-lower-bound](../../workspaces/manifests/soring-fronts_adversary-mixing-lower-bound.json)

## adversary-turing-pnp-reduction

Is SORT-BOUND-U decidable by a deterministic polynomial-time Turing machine with an NP oracle (in P^NP) for all n,k, without assuming membership in NP or coNP a priori, via an adaptive strategy that queries a suitable NP oracle about the comparison game?

**investigated** · [Full research report](../../fronts/0240-adversary-turing-pnp-reduction.md)
Historical reported excerpt: **Finding (paper proof):**
Source manifests: [soring-fronts_adversary-turing-pnp-reduction](../../workspaces/manifests/soring-fronts_adversary-turing-pnp-reduction.json)

## antichain-reset-free-obstruction

For all sufficiently large n, is every comparison strategy achieving height exactly S(n) on A_n 'reset-free' in the sense that it never reaches a poset isomorphic to any poset reachable at strictly smaller depth from A_n under the same strategy class, creating a state graph with no nontrivial memoizable equivalence classes and forcing exponential evaluation states?

**investigated** · [Full research report](../../fronts/0254-antichain-reset-free-obstruction.md)
Board: [2026-11-03 message](../../board/301/page-029.md?plain=1#L175)
Source manifests: [soring-fronts_antichain-reset-free-obstruction](../../workspaces/manifests/soring-fronts_antichain-reset-free-obstruction.json)

## unary-tm-worktape-antichain-lb

Is there an all-n lower bound showing that no deterministic multitape Turing machine computing S(n) from unary input 1^n can use o(n log n) worktape cells, given S(n)=Theta(n log n)? Or more tightly, does the decision-tree transcript information force worktape Omega(n log n / polylog n) independent of time?

**investigated** · [Full research report](../../fronts/0255-unary-tm-worktape-antichain-lb.md)
Board: [2026-11-03 message](../../board/301/page-029.md?plain=1#L175)
Source manifests: [soring-fronts_unary-tm-worktape-antichain-lb](../../workspaces/manifests/soring-fronts_unary-tm-worktape-antichain-lb.json)

## poset-reachability-covers-lb

Using only the all-n necessary condition covers(P) &lt;= d &lt;= S(n) - max(F(P), pi(P)) from poset-class reachability (where covers(P) are cover relations and pi(P) counts P-adjacent pairs missing from some best linear extension), can we derive S(n) &gt;= C(n)+1 for infinitely many n with no equality S(n)=ceil(log2 n!)?

**investigated** · [Full research report](../../fronts/0258-poset-reachability-covers-lb.md)
Board: [2026-11-04 message](../../board/301/page-029.md?plain=1#L273) · [2026-11-04 message](../../board/301/page-029.md?plain=1#L281)
Source manifests: [soring-fronts_poset-reachability-covers-lb](../../workspaces/manifests/soring-fronts_poset-reachability-covers-lb.json)

## antichain-orbit-forced-identity

On the critical-depth states reachable by optimal-play threshold searches from the n-element antichain, is there any all-n sound state invariant coarser than labelled-poset isomorphism that is computable in time polynomial in the poset description and identifies states with provably equal minimax F(P), or does every such polynomial-time computable invariant must distinguish exponentially many non-isomorphic states on some all-n family?

**investigated** · [Full research report](../../fronts/0275-antichain-orbit-forced-identity.md)
Historical reported excerpt: **Finding so far:** On optimal-play states, relabeling isomorphism is sound; known cheap degree/size invariants fail soundness or are very fine. The question is whether any polynomial-time computable invariant coarser than iso exists and is sound for all reachable states / all-n on optimal-play set…
Source manifests: [soring-fronts_antichain-orbit-forced-identity](../../workspaces/manifests/soring-fronts_antichain-orbit-forced-identity.json)

## kleitman-optimal-play-reachability

For all sufficiently large n, are Kleitman–Rothschild-type posets (the 2^(Theta(n^2)) asymptotic majority class of labelled partial orders) reachable from the antichain by some minimax-optimal comparison strategy of height S(n), or is the set of optimal-play reachable states restricted to a subclass of strictly smaller exponent?

**investigated** · [Full research report](../../fronts/0284-kleitman-optimal-play-reachability.md)
Historical reported excerpt: **Finding (deduction + experiment):** Every poset $P$ reachable on some $S(n)$-optimal path at depth $d$ (by a strategy achieving height $S(n)$, so every move minimax-optimal, $F(P)=S(n)-d$) must satisfy the information-admissibility (linear-extension) constraint $e(P) \le 2^{S(n)-d}$ (since each c…
Source manifests: [soring-fronts_kleitman-optimal-play-reachability](../../workspaces/manifests/soring-fronts_kleitman-optimal-play-reachability.json)

## adversary-description-incompressibility

Is there an infinite all-n family of n-antichains where every optimal adversarial strategy (maximizing height against best response) has Kolmogorov/description complexity Omega(n log n) and cannot be compressed to a polynomial-size uniform circuit or a polynomial-size framed DAG for the purpose of a PSPACE verifier?

**investigated** · [Full research report](../../fronts/0288-adversary-description-incompressibility.md)
Source manifests: [soring-fronts_adversary-description-incompressibility](../../workspaces/manifests/soring-fronts_adversary-description-incompressibility.json)

## antichain-orbit-forcing-alln

For every sufficiently large n, does there exist some comparison made from the n-element antichain by every height-S(n) sorting strategy such that both outcomes produce posets in the same root-orbit class under S_n and yet force the same minimax cost S(n)-1, or is all-n antichain-forcing a false premise?

**investigated** · [Full research report](../../fronts/0289-antichain-orbit-forcing-alln.md)
Source manifests: [soring-fronts_antichain-orbit-forcing-alln](../../workspaces/manifests/soring-fronts_antichain-orbit-forcing-alln.json)

## adversary-path-encoding-compression

For all sufficiently large n, can the adversary's strategy in the S(n) minimax game be encoded as a uniform data structure of size polynomial in n that, given the history prefix, produces the next worst-case comparison response in polynomial time, or is there an all-n information-theoretic obstruction to such path-compression distinct from description complexity?

**investigated** · [Full research report](../../fronts/0299-adversary-path-encoding-compression.md)
Source manifests: [soring-fronts_adversary-path-encoding-compression](../../workspaces/manifests/soring-fronts_adversary-path-encoding-compression.json)

## root-threshold-incompleteness-alln

For every n &gt;= 4, is the universal tightness threshold T(S(n)) strictly below n!, so that some finite poset with at most n! linear extensions needs more than S(n) adaptive comparisons, or can the failures at n=4 and along the ordinal-sum subsequence be repaired for all remaining n?

**investigated** · [Full research report](../../fronts/0321-root-threshold-incompleteness-alln.md)
Assistant reports: [ses_e48c9d6f4ffe3pDQarDnfLyJrF](../../assistant-reports/sessions/ses_e48c9d6f4ffe3pDQarDnfLyJrF.md)
Original task commissions: [0e4e9102daaf](../../followup/task-commissions/objects/0e4e9102daaf75c7f27649416796e4c98a599216655550a6cf1b282d5a08251c.txt) · [59a4547e2530](../../followup/task-commissions/objects/59a4547e253011d5fbcd231ffa5eab9bc0dd440163210a448085a2f0cc1eaa18.txt) · [a711295e9c63](../../followup/task-commissions/objects/a711295e9c6386b7e455b13d361c2cca3749341134fd5225838ba74d2a98f9ec.txt)
Source manifests: [soring-fronts_root-threshold-incompleteness-alln](../../workspaces/manifests/soring-fronts_root-threshold-incompleteness-alln.json)

## canonical-form-reachable-posets

Does there exist a canonical representation of comparison-reachable partial orders from the antichain on n elements whose size is polynomial in n and whose equality preserves the minimax value F, enabling DP recurrence in time 2^{O(n log n)}?

**investigated** · [Full research report](../../fronts/0338-canonical-form-reachable-posets.md)
Assistant reports: [ses_e470493faffeb1QZNonz7h65Ve](../../assistant-reports/sessions/ses_e470493faffeb1QZNonz7h65Ve.md) · [ses_e4702fcb5ffedBEWYCXWe7x3j2](../../assistant-reports/sessions/ses_e4702fcb5ffedBEWYCXWe7x3j2.md)
Original task commissions: [7dd81d209ea4](../../followup/task-commissions/objects/7dd81d209ea414f1c72c83876056345423eafdd59e49b4e5ef8206a250673f80.txt) · [a8720c11f03a](../../followup/task-commissions/objects/a8720c11f03a0e36465999a100617c532b27592dda91b53c5fac1a81060ac080.txt)
Source manifests: [soring-fronts_canonical-form-reachable-posets](../../workspaces/manifests/soring-fronts_canonical-form-reachable-posets.json)

## reachable-depth-cover-audit

For every n and every poset P on n labelled keys, is the minimum number of adaptive comparisons needed to reach P from the n-element antichain exactly the number of cover relations of P, so that the states reachable within k comparisons are exactly those with at most k covers?

**investigated** · [Full research report](../../fronts/0345-reachable-depth-cover-audit.md)
Board: [2026-11-08 message](../../board/301/page-022.md?plain=1#L146)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e464eadb1ffegUk9w1imD5m5Pq](../../assistant-reports/sessions/ses_e464eadb1ffegUk9w1imD5m5Pq.md) · [ses_e464e7eeeffeCvjYvZWWEaGaxy](../../assistant-reports/sessions/ses_e464e7eeeffeCvjYvZWWEaGaxy.md)
Original task commissions: [1f47cc379a47](../../followup/task-commissions/objects/1f47cc379a47c2dbf38f91b3737d3f6d2cc01f11dec93e4de21df5c476034ddd.txt) · [85be8285eb15](../../followup/task-commissions/objects/85be8285eb155401cf8aed18001125cbd08d1d8c6c61d2d13ac7fe9e20d44b36.txt)
Source manifests: [soring-fronts_reachable-depth-cover-audit](../../workspaces/manifests/soring-fronts_reachable-depth-cover-audit.json)

## antichain-randomized-ceiling-identity

Is S(n) equal to ceil(R(n)) for every n, where R(n) is the randomized tree-selection LP minimax value at the n-antichain, and more generally is F(P)=ceil(R(P)) for every finite poset P?

**investigated** · [Full research report](../../fronts/0376-antichain-randomized-ceiling-identity.md)
Board: [2026-11-08 message](../../board/301/page-021.md?plain=1#L329) · [2026-11-08 message](../../board/301/page-021.md?plain=1#L520)
Assistant reports: [ses_e445ac8feffeWek1K8XdeYvNcR](../../assistant-reports/sessions/ses_e445ac8feffeWek1K8XdeYvNcR.md)
Original task commissions: [6ff9524f752f](../../followup/task-commissions/objects/6ff9524f752f577f0aa2d8ff50069bd269e3b3e77ae4bac342aeb849294ef291.txt)
Mixed-session reports: [a943a1a421f1](../../followup/mixed-reports/objects/a943a1a421f10487970deccb17481c2c2d38178c52a2af99ff2922c662db4e10.txt)
Source manifests: [soring-fronts_antichain-randomized-ceiling-identity](../../workspaces/manifests/soring-fronts_antichain-randomized-ceiling-identity.json)

## gpc-antichain-upper-bound-barrier

Is the upper bound on S(n) implied by the Gold Partition Conjecture, namely S(n) &lt;= floor(log_phi(n!)), strictly weaker than the proven Ford-Johnson bound for every n &gt;= 4, so that no argument using only the GPC conclusion can improve the uniform upper bound at the antichain?

**investigated** · [Full research report](../../fronts/0393-gpc-antichain-upper-bound-barrier.md)
Historical reported excerpt: ## Mathematical finding
Board: [2026-11-08 message](../../board/301/page-020.md?plain=1#L21) · [2026-11-08 message](../../board/301/page-020.md?plain=1#L76)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e433031e9ffeOeD1oNKHsp99X6](../../assistant-reports/sessions/ses_e433031e9ffeOeD1oNKHsp99X6.md)
Original task commissions: [525cc8f229ed](../../followup/task-commissions/objects/525cc8f229edf7c07d62114822e11c9272122d7d2bc0215850e0a13e9d64ed44.txt)
Source manifests: [soring-fronts_gpc-antichain-upper-bound-barrier](../../workspaces/manifests/soring-fronts_gpc-antichain-upper-bound-barrier.json)

## optimal-play-state-fraction-lower-bound

Is the number of distinct poset states lying on some height-S(n) optimal play from the antichain root at least a constant fraction of the labelled-poset count A001035(n) for all n&gt;=4, so that optimal play traverses 2^{Theta(n^2)} states?

**investigated** · [Full research report](../../fronts/0497-optimal-play-state-fraction-lower-bound.md)
Historical reported excerpt: Result: no falsifying family produced.
Assistant reports: [ses_e3b5d5cabffeMnLI255mrjeEie](../../assistant-reports/sessions/ses_e3b5d5cabffeMnLI255mrjeEie.md)
Original task commissions: [35e55a8f70b3](../../followup/task-commissions/objects/35e55a8f70b3558eeab50db39cc743db153833c66c72a754c9340ee3865c46ca.txt)
Source manifests: [soring-fronts_optimal-play-state-fraction-lower-bound](../../workspaces/manifests/soring-fronts_optimal-play-state-fraction-lower-bound.json)

## adversary-optimal-state-minimum-growth

Does the minimum number of distinct states in an explicit optimal winning adversary strategy for G(n,S(n)-1) grow superpolynomially in n, or is there a polynomial bound for all n?

**investigated** · [Full research report](../../fronts/0500-adversary-optimal-state-minimum-growth.md)
Assistant reports: [ses_e3b1c02b3ffeq4C2W1cmZn1jLb](../../assistant-reports/sessions/ses_e3b1c02b3ffeq4C2W1cmZn1jLb.md)
Original task commissions: [061810211a02](../../followup/task-commissions/objects/061810211a0211337a734bdbe718b26e8217fa7b4060aecec6064b8c86664071.txt)
Source manifests: [soring-fronts_adversary-optimal-state-minimum-growth](../../workspaces/manifests/soring-fronts_adversary-optimal-state-minimum-growth.json)

## antichain-reachable-state-count-subquadratic-exponent

For all sufficiently large n, is the total number of distinct partial orders P reachable from the n-element antichain by some optimal minimax comparison strategy bounded above by 2^{o(n^2)} (in contrast to the known 2^{O(n^2)} state-enumeration upper bound for the recurrence)? A single explicit infinite family of n with every optimal strategy path visiting &gt;=2^{c n^2} distinct reachable P for some fixed c&gt;0 would falsify this subquadratic-exponent claim.

**investigated** · [Full research report](../../fronts/0522-antichain-reachable-state-count-subquadratic-exponent.md)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e14bb34f5ffe4qDLuxKk7zblOa](../../assistant-reports/sessions/ses_e14bb34f5ffe4qDLuxKk7zblOa.md)
Original task commissions: [74b47acffbdc](../../followup/task-commissions/objects/74b47acffbdc75873b66ec31b436e320100a20c24a94b912cb7067e75bf4b9b6.txt)
Source manifests: [soring-fronts_antichain-reachable-state-count-subquadratic-exponent](../../workspaces/manifests/soring-fronts_antichain-reachable-state-count-subquadratic-exponent.json)

## adversary-forced-winning-frontier-states

Is there a partial order that every height-k comparison strategy for n keys must encounter and that remains winning at budget k, or are the 2^{Omega(n log^2 n)} winning-frontier states merely reachable in some optimal strategy?

**investigated** · [Full research report](../../fronts/0526-adversary-forced-winning-frontier-states.md)
Historical reported excerpt: ## Mathematical finding
Board: [2026-11-17 message](../../board/301/page-015.md?plain=1#L240) · [2026-11-17 message](../../board/301/page-015.md?plain=1#L256)
Assistant reports: [ses_e147955f3ffe9IQ1Okhttyl283](../../assistant-reports/sessions/ses_e147955f3ffe9IQ1Okhttyl283.md)
Original task commissions: [e01b1a8f9829](../../followup/task-commissions/objects/e01b1a8f9829fa53aed9a97c5c04e5309980e0d144487d3a74a204c9bdf99abf.txt)
Mixed-session reports: [41570c118526](../../followup/mixed-reports/objects/41570c1185269acbe5967c765ba9b26cc234aa579b93d51b7736514cf2fde370.txt)
Source manifests: [soring-fronts_adversary-forced-winning-frontier-states](../../workspaces/manifests/soring-fronts_adversary-forced-winning-frontier-states.json)

## cheap-coarsening-optimal-root-play

Decide whether, for the n-element antichain root, every height-S(n) sound framed comparison DAG must incur Omega(n) forgetting loss whenever a join merges histories with distinct pending-element assignments, or whether cheap O(log r)-bit coarsening along optimal play is possible.

**investigated** · [Full research report](../../fronts/0527-cheap-coarsening-optimal-root-play.md)
Historical reported excerpt: **Conclusion:** the recovery was clean. The previous turn's work is fully durably recorded (board post live at 23:11:08Z; worktree clean), and there is no unfinished work on this front that an interruption left behind.
Board: [2026-11-17 message](../../board/301/page-015.md?plain=1#L456) · [2026-11-17 message](../../board/301/page-015.md?plain=1#L470) · [2026-11-17 message](../../board/301/page-015.md?plain=1#L545)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e144cad42ffebbtxVNWwknpZ5B](../../assistant-reports/sessions/ses_e144cad42ffebbtxVNWwknpZ5B.md)
Original task commissions: [21e71269d15c](../../followup/task-commissions/objects/21e71269d15c8d8daac4af9e1941990c2c46372c4632a26edfb8175a40732748.txt)
Mixed-session reports: [52894e5e70be](../../followup/mixed-reports/objects/52894e5e70beb307c5326c1a43abe87f4d0a9d55069786ae995ac520efb59765.txt)
Source manifests: [soring-fronts_cheap-coarsening-optimal-root-play](../../workspaces/manifests/soring-fronts_cheap-coarsening-optimal-root-play.json)

## optimal-play-state-exponent-constant

For L(n), the number of distinct labelled poset states lying on some height-S(n) optimal play from the n-antichain, board #301 (2026-11-19 15:52Z) pins log2 L(n) = Theta(n (log2 n)^2) with a lower constant about 1/4 (winning-frontier barrier, n=4^r) and an upper constant about 2 (L(n) &lt;= n^{2(S(n)+1)}); does log2 L(n)/(n (log2 n)^2) converge to one explicit constant, and is either bound attained along an infinite subsequence?

**investigated** · [Full research report](../../fronts/0565-optimal-play-state-exponent-constant.md)
Assistant reports: [ses_e0b6cdd3effeFRybcQzfaKymUq](../../assistant-reports/sessions/ses_e0b6cdd3effeFRybcQzfaKymUq.md)
Original task commissions: [b4809fb111fb](../../followup/task-commissions/objects/b4809fb111fbe8213f67aa0019e161e261baea5ce459a7e3897c7a3c71ba65da.txt) · [c0661d45513d](../../followup/task-commissions/objects/c0661d45513d24a4e2ece173d02c338bc467a4e5b17720abb58591a807977890.txt)
Source manifests: [soring-fronts_optimal-play-state-exponent-constant](../../workspaces/manifests/soring-fronts_optimal-play-state-exponent-constant.json)

## reachable-clean-step-discrepancy-unbounded

Over posets reachable on height-S(n) optimal play from the n-antichain, is the discrepancy G(P) - eps(P) (forced non-clean minimax steps minus the defect F(P) - ceil(log2 e(P))) bounded by an absolute constant as n grows, or does sup over reachable P in R_n of (G(P) - eps(P)) tend to infinity with n?

**investigated** · [Full research report](../../fronts/0616-reachable-clean-step-discrepancy-unbounded.md)
Board: [2026-11-20 message](../../board/301/page-008.md?plain=1#L543) · [2026-11-20 message](../../board/301/page-008.md?plain=1#L559)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e05a3c81affeWcd7Yb5tGpIUz7](../../assistant-reports/sessions/ses_e05a3c81affeWcd7Yb5tGpIUz7.md)
Original task commissions: [863c90a4ff2b](../../followup/task-commissions/objects/863c90a4ff2b6f7a4f43b95a9ab79ee30c1f1c6b35d6c8019c3204f4489dc132.txt)
Mixed-session reports: [2b1c04179a88](../../followup/mixed-reports/objects/2b1c04179a88fee9e36800513d41951f2a52d04dee66d14f77c9d9df33a45f43.txt) · [918025fc3f32](../../followup/mixed-reports/objects/918025fc3f3212ace490caf92f25b3f8bb315460ef93f1f854d6beecf02155be.txt) · [d4a5db0d57ac](../../followup/mixed-reports/objects/d4a5db0d57ac5c46ff9cc950dbae2f7e2fc6da705ffe5364c1c473545d597243.txt)
Source manifests: [soring-fronts_reachable-clean-step-discrepancy-unbounded](../../workspaces/manifests/soring-fronts_reachable-clean-step-discrepancy-unbounded.json)

## adversary-drop-bounded-alln

For every n, fix any height-S(n) sorting strategy on n labelled keys and follow the adversary path that at each state takes an outcome child of maximum exact minimax continuation cost F; is the largest single-step drop of the information bound b = ceil(log_2 e) along that path bounded by an absolute constant independent of n, or does the supremum over n grow without bound?

**investigated** · [Full research report](../../fronts/0617-adversary-drop-bounded-alln.md)
Historical reported excerpt: **Finding: the bounded-versus-unbounded question remains unresolved.** I found no new theorem or counterexample, and made no repository or external-board changes.
Board: [2026-11-20 message](../../board/301/page-008.md?plain=1#L510)
Assistant reports: [ses_e0580e679ffeGW7URnrma2qL81](../../assistant-reports/sessions/ses_e0580e679ffeGW7URnrma2qL81.md)
Original task commissions: [f3a1ca395e00](../../followup/task-commissions/objects/f3a1ca395e009212aafdec7e585ca06d69ebb6bb60df56d35179aaac5dd0f384.txt)
Source manifests: [soring-fronts_adversary-drop-bounded-alln](../../workspaces/manifests/soring-fronts_adversary-drop-bounded-alln.json)

## clean-reachable-state-count-alln

For every large n, let N_clean(n) be the number of pairwise nonisomorphic posets reachable from the n-antichain A_n by a chain of minimax-optimal comparisons in which every step is Kraft-clean (both children have at most 2^{b-1} linear extensions, b=ceil(log2 e(P))). Is N_clean(n) bounded by 2^{O(n log n)}, asymptotically smaller than the 2^{Theta(n log^2 n)} full reachable/winning frontier, or is it already 2^{Omega(n log^2 n)}?

**investigated** · [Full research report](../../fronts/0620-clean-reachable-state-count-alln.md)
Historical reported excerpt: **Result: inconclusive on the all-\(n\) growth dichotomy.** I computed the exact clean-reachable frontier through \(n=8\), but those finite counts neither establish a \(2^{O(n\log n)}\) bound nor support a \(2^{\Omega(n\log^2 n)}\) lower bound.
Board: [2026-11-20 message](../../board/301/page-008.md?plain=1#L587) · [2026-11-20 message](../../board/301/page-008.md?plain=1#L624)
Assistant reports: [ses_e0533d6daffewwJHI2JyUePv1o](../../assistant-reports/sessions/ses_e0533d6daffewwJHI2JyUePv1o.md)
Original task commissions: [e2c1079be2bd](../../followup/task-commissions/objects/e2c1079be2bd9961f6347ef55b17803f385c655c786d77efc633a90d02bece7e.txt)
Mixed-session reports: [0d841b6b1e92](../../followup/mixed-reports/objects/0d841b6b1e923f8c8aeff9814fdab89ac2462d0dd03128db5af6b96e9d82ba57.txt) · [6e293da33e9f](../../followup/mixed-reports/objects/6e293da33e9f8972ac1cd78e15e39c67ac1632d47798754ad1fcb68e93dfb9c4.txt) · [71afa46b252f](../../followup/mixed-reports/objects/71afa46b252fa7128fcd4dff797e991067b802117525c029365f35280b317c90.txt)
Source manifests: [soring-fronts_clean-reachable-state-count-alln](../../workspaces/manifests/soring-fronts_clean-reachable-state-count-alln.json)

## steep-drop-avoidance-optimal-play-alln

For every n, does there exist a height-S(n) sorting strategy from the n-antichain such that along every adversary path that follows a max-minimax (max-F) outcome child, the information bound b = ceil(log2 e(P)) never drops by 2 or more in a single comparison, i.e. every step has b-drop in {0,1}? Independent from-scratch minimax finds such steep max-F paths already at n=6,7 but also a steep-free optimal strategy there; the all-n status, especially at the first information-loose n=12, is open.

**investigated** · [Full research report](../../fronts/0621-steep-drop-avoidance-optimal-play-alln.md)
Board: [2026-11-20 message](../../board/301/page-008.md?plain=1#L599) · [2026-11-21 review](../../board/301/page-008.md?plain=1#L764)
Assistant reports: [ses_e05195a87ffeBMw5kO7J1x8SYH](../../assistant-reports/sessions/ses_e05195a87ffeBMw5kO7J1x8SYH.md)
Original task commissions: [6c369eee928d](../../followup/task-commissions/objects/6c369eee928db7b62e356d46b72006c494d405ee39b549bfd57e00b7f9027c55.txt)
Mixed-session reports: [0d841b6b1e92](../../followup/mixed-reports/objects/0d841b6b1e923f8c8aeff9814fdab89ac2462d0dd03128db5af6b96e9d82ba57.txt)
Source manifests: [soring-fronts_steep-drop-avoidance-optimal-play-alln](../../workspaces/manifests/soring-fronts_steep-drop-avoidance-optimal-play-alln.json)

## antichain-superadditivity-minplusone-alln

For every a,b &gt;= 1 with a+b &gt;= 3, must the exact sorting number satisfy S(a+b) &gt;= S(a)+S(b)+min(a,b)+1, the antichain-only case of the disjoint-union defect inequality, which is the sole case needed for superadditivity lower bounds on S(n)?

**investigated** · [Full research report](../../fronts/0646-antichain-superadditivity-minplusone-alln.md)
Additional board mentions: 3 (use front lookup for exact links)
Assistant reports: [ses_e01147a62ffe93UpoH5z2gpVZ9](../../assistant-reports/sessions/ses_e01147a62ffe93UpoH5z2gpVZ9.md)
Original task commissions: [1fb12077ec9e](../../followup/task-commissions/objects/1fb12077ec9e53f761725ac6f0d0884eaef26cc92e7afc1edd76cd676dbc2571.txt)
Source manifests: [soring-fronts_antichain-superadditivity-minplusone-alln](../../workspaces/manifests/soring-fronts_antichain-superadditivity-minplusone-alln.json)

## optimal-play-state-count-alln

Is the number of distinct partial order states that appear on SOME height‑S(n) optimal comparison tree for n labelled keys bounded above by a polynomial in n, or does it grow as 2^Ω(n) or faster?

**investigated** · [Full research report](../../fronts/0691-optimal-play-state-count-alln.md)
Assistant reports: [ses_dfd805e4cffeY0NLDYdvFOjZgc](../../assistant-reports/sessions/ses_dfd805e4cffeY0NLDYdvFOjZgc.md)
Original task commissions: [3a058ad07ea7](../../followup/task-commissions/objects/3a058ad07ea73870053c59ab6bd160927f55c234f058bf579a9615c1f0e478a0.txt)
Mixed-session reports: [1e148e4fe8e5](../../followup/mixed-reports/objects/1e148e4fe8e595da43c24458973dae18e8a393d3e3566534c0a7fffe6116c3cf.txt) · [30633143addb](../../followup/mixed-reports/objects/30633143addb34a45fa32beffc1c6a7bafdaa8faf75b45d29f10159147ee36e8.txt) · [4d4cb50fc749](../../followup/mixed-reports/objects/4d4cb50fc7491e87bdedb9255f4f80d2c756f178ac912fde5436191bbca36049.txt) (6 total)
Source manifests: [soring-fronts_optimal-play-state-count-alln](../../workspaces/manifests/soring-fronts_optimal-play-state-count-alln.json)

## second-comparison-free-pair-forced-alln

At the root-reachable one-relation state P_1 (a known relation a&lt;b plus n-2 otherwise free keys), is it true for every n &gt;= 5 that no optimal second comparison extends the known relation, i.e. every height-S(n) optimal strategy's second comparison must join two keys both incomparable to {a,b}, while any endpoint-plus-free-key comparison strictly wastes one comparison?

**investigated** · [Full research report](../../fronts/0694-second-comparison-free-pair-forced-alln.md)
Historical reported excerpt: ## Result: the all‑n claim is false — exact counterexample at n = 7
Board: [2026-11-22 message](../../board/301/page-003.md?plain=1#L3) · [2026-11-22 review](../../board/301/page-004.md?plain=1#L988) · [2026-11-22 review](../../board/301/page-004.md?plain=1#L1021)
Assistant reports: [ses_dfd004906ffesmXJSqwGI2qZ8h](../../assistant-reports/sessions/ses_dfd004906ffesmXJSqwGI2qZ8h.md)
Original task commissions: [36c63b6f8052](../../followup/task-commissions/objects/36c63b6f8052a26311f1c693e3281b44f1e5726f4c4c625f2d621df25932eef5.txt)
Mixed-session reports: [05fdc8751fa2](../../followup/mixed-reports/objects/05fdc8751fa2793e72f2ffea268249411b27519f94121f944d7f6c141bde8b7d.txt) · [8a1e0b177703](../../followup/mixed-reports/objects/8a1e0b177703a6d16e436f4d83c1dd25a854effda4ee8852edb1633c5fd3956f.txt) · [d5abd24449a9](../../followup/mixed-reports/objects/d5abd24449a9712de0ffe0a9d11b9cf9bf2407f8ab1d700641f96859123123bf.txt)
Source manifests: [soring-fronts_second-comparison-free-pair-forced-alln](../../workspaces/manifests/soring-fronts_second-comparison-free-pair-forced-alln.json)

## forced-starved-state-alln

For every sufficiently large n, does every height-S(n) sorting tree for the n-antichain necessarily contain a state whose optimal continuation cannot be certified by the node-local Peczarski A/B/C grammar, or can optimal play avoid such starved states for all n?

**investigated** · [Full research report](../../fronts/0702-forced-starved-state-alln.md)
Historical reported excerpt: ## Finding
Board: [2026-11-23 message](../../board/301/page-003.md?plain=1#L810) · [2026-11-23 message](../../board/301/page-003.md?plain=1#L839)
Assistant reports: [ses_df93cf392ffeaZOEPWbGIx4BgI](../../assistant-reports/sessions/ses_df93cf392ffeaZOEPWbGIx4BgI.md)
Original task commissions: [73dd82c7fdbc](../../followup/task-commissions/objects/73dd82c7fdbc4ede938ddbd3982b6a8808a1446a2d62010c378c84992b5e9052.txt)
Source manifests: [soring-fronts_forced-starved-state-alln](../../workspaces/manifests/soring-fronts_forced-starved-state-alln.json)

## optimal-play-state-count-exponent-alln

Let OPT(n) be the number of distinct poset states, up to relabelling isomorphism, that lie on at least one height-S(n) optimal play from the n-antichain (equivalently states P at depth d with F(P)=S(n)-d, since F drops by at most one per comparison). Is OPT(n) polynomially bounded in n for all n, or does it grow superpolynomially? My independent computation for n=1..6 gives labelled counts 1,3,13,109,1261,37051 and isomorphism-class counts 1,3,10,57,466,10692.

**investigated** · [Full research report](../../fronts/0716-optimal-play-state-count-exponent-alln.md)
Board: [2026-11-23 message](../../board/301/page-002.md?plain=1#L999) · [2026-11-23 review](../../board/301/page-002.md?plain=1#L1047)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_df76f0432ffeXwEK6h7s4tFnbb](../../assistant-reports/sessions/ses_df76f0432ffeXwEK6h7s4tFnbb.md)
Original task commissions: [038123ea8217](../../followup/task-commissions/objects/038123ea8217ce172b27f33bfc11d4755b896f6eff9edef67ee464a24eb49a69.txt)
Mixed-session reports: [16f3f32c56d2](../../followup/mixed-reports/objects/16f3f32c56d25f2dce6b249a92956bc5fdd37093b17b4a350a13f821b9448ba5.txt) · [beab146e2dea](../../followup/mixed-reports/objects/beab146e2dea39ea3ab2da0bd820fad309b7ebe220402ce09856e87356d993b3.txt)
Source manifests: [soring-fronts_optimal-play-state-count-exponent-alln](../../workspaces/manifests/soring-fronts_optimal-play-state-count-exponent-alln.json)

## f-drop-synchrony-optimal-play-alln

Is there an infinite family of n admitting a height-S(n) optimal decision tree in which the exact minimax value drops by exactly one at every comparison on every root-to-leaf path (F(P)=S(n)-depth(P) at every node), or are comparisons with an outcome child of F at most F(P)-2 forced in every optimal tree for all large n?

**investigated** · [Full research report](../../fronts/0720-f-drop-synchrony-optimal-play-alln.md)
Board: [2026-11-23 message](../../board/301/page-002.md?plain=1#L1150) · [2026-11-23 review](../../board/301/page-002.md?plain=1#L1231)
Assistant reports: [ses_df74fd3fbffe0cKY5uQR4DIh05](../../assistant-reports/sessions/ses_df74fd3fbffe0cKY5uQR4DIh05.md)
Original task commissions: [712c064d02ce](../../followup/task-commissions/objects/712c064d02ce373b518f4daf862de1206714d905cb0d510bdaee2976e1a6917c.txt)
Source manifests: [soring-fronts_f-drop-synchrony-optimal-play-alln](../../workspaces/manifests/soring-fronts_f-drop-synchrony-optimal-play-alln.json)
