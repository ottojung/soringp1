# Profiles, decks and lookahead

[Catalogue home](../README.md) · [Evidence status guide](../../RESULTS.md)

Status is the original workflow label, not mathematical proof. Linked messages may contain corrections or rejected claims.

## linear-extension-sampling-lower-bound

Does approximate uniform sampling of linear extensions of states on any optimal sorting strategy require super-polynomial time for all-n, creating a barrier to certain randomized certificate approaches?

**investigated** · [Full research report](../../fronts/0052-linear-extension-sampling-lower-bound.md)
Intended test or falsifier: Give a polynomial-time approximate uniform sampler for all states reachable by some optimal strategy for all n, or prove it would imply collapse of counting classes.
Proposed implication: If sampling is hard, randomized polynomial-size certificates appear unlikely; this distinguishes counting complexity from decision complexity without claiming #P-hardness of S(n) directly.
Historical reported excerpt (unverified): The task says "on billy-dev ONLY" and to report to board #301 etc. But I need to follow the exact instructions - report a mathematical finding, concrete failed approach or exact obstruction; do not confuse process success with a proof. I should report honestly as above. The instructions say "Report…
Source manifests: [soring-fronts_linear-extension-sampling-lower-bound](../../workspaces/manifests/soring-fronts_linear-extension-sampling-lower-bound.json)

## alln-ceiling-loss-invariant

For every all-n complete family of sound certificates for SORT-BOUND-U (framed or general join/intersection), let L(n) be the average ceiling rounding loss L(n)= (sum of per-stage ceil(log2 q_i)-log2 n!) / n over an optimal stage factorization; must liminf_{n-&gt;∞} L(n) &gt; 0, or can some family achieve L(n)=o(1)?

**investigated** · [Full research report](../../fronts/0071-alln-ceiling-loss-invariant.md)
Intended test or falsifier: Give a constructive all-n certificate family with L(n)=o(1) (beating the known o(n) surplus asymptotics in the normalized loss) realizable by a sound polynomial-time verifier, or prove liminf L(n) &gt;= c&gt;0 from a model-in…
Proposed implication: A model-independent positive constant loss would rule out certain 'framed reset' routes regardless of branching details and connect directly to Sergeev's surplus; o(1) loss would be a strong structural fact about the ce…
Historical reported excerpt (unverified): **Concrete failed/obstructed route identified:** Trying to use arbitrary integer factorizations (like "one big factor") is not realizable by comparison-model splits; conversely, realizable comparison splits appear to force factors with persistent ceiling rounding loss, obstructing $L(n)=o(1)$ for c…
Board: [2026-10-30 message](../../board/301/page-043.md?plain=1#L425)
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_alln-ceiling-loss-invariant](../../workspaces/manifests/soring-fronts_alln-ceiling-loss-invariant.json)

## antichain-root-invariant-separation

Does there exist an all-n invariant I(P) computable from a reachable poset P (with P reachable from antichain) that is strictly stronger than the information bound in the sense that for infinitely many optimal-decision paths from antichain, I forces &gt;= c*S(n) comparisons while log2(e(P)) is within o(n) of its maximum for P, for some fixed c&gt;1/ something or just strictly separating?

**investigated** · [Full research report](../../fronts/0083-antichain-root-invariant-separation.md)
Intended test or falsifier: Show every polynomial-time (or just natural) invariant that is monotonic and adversary-sound is dominated by log2(e(P))+o(n) on all antichain-reachable winning states at budget S(n), or give a counterexample invariant a…
Proposed implication: A nontrivial root-quantified invariant would improve lower bounds on S(n) without attacking arbitrary posets; failure to separate would clarify why information-theoretic invariants have been insufficient.
Historical reported excerpt (unverified): Do not add new Lean/invariants. The falsifier is effectively true under standard asymptotics: no such strictly separating natural invariant exists for constant $c&gt;1$ in that regime. Focus instead on (1) better upper bounds/evaluators, (2) barriers that rule out whole invariant families with explici…
Board: [2026-10-30 message](../../board/301/page-041.md?plain=1#L27)
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_antichain-root-invariant-separation](../../workspaces/manifests/soring-fronts_antichain-root-invariant-separation.json)

## coarser-sound-complete-invariant

Does there exist for all n a coarser equivalence relation on comparison histories (weaker than poset relabeling isomorphism) that is both sound for the minimax value F(P) and has only exp(O(n log n / log log n)) or polynomial classes per depth, or is every such all-n invariant exponentially large?

**investigated** · [Full research report](../../fronts/0085-coarser-sound-complete-invariant.md)
Intended test or falsifier: Exhibit an explicit all-n coarser invariant computable uniformly with polynomial classes and prove F preservation, or prove that any invariant preserving F exactly on all reachable antichain histories requires Omega(n! …
Proposed implication: A polynomial class invariant would give a path to compact DP tables for exact S(n) computation; a super-polynomial all-n lower bound would formalize a state-complexity barrier beyond the winning frontier counting.
Historical reported excerpt (unverified): **Mathematical finding 1 — falsifier's lower-bound disjunct refuted (deduction).** The equivalence `P ~ Q ⇔ F(P) = F(Q)` on reachable states is sound for the minimax value by definition, strictly coarser than relabeling isomorphism (F is relabelling-invariant, already a deduction in `docs/research-…
Board: [2026-10-30 message](../../board/301/page-041.md?plain=1#L229) · [2026-10-31 message](../../board/301/page-041.md?plain=1#L301) · [2026-10-31 message](../../board/301/page-041.md?plain=1#L317) · [2026-10-31 message](../../board/301/page-041.md?plain=1#L333) · [2026-10-31 message](../../board/301/page-041.md?plain=1#L341)
Additional board mentions: 2 (use front lookup for exact links)
Mixed-session reports: [13ec1a6f6ef7](../../followup/mixed-reports/objects/13ec1a6f6ef728c8a70f9cc94053ae2bb7a46aff7a097756e7561b2b2d2d1c9d.txt) · [3c8bc34c24c1](../../followup/mixed-reports/objects/3c8bc34c24c1ca25ece5361765c290d788243251ab2c1db97f6119a4dc5dd5a2.txt) · [e70582fbe904](../../followup/mixed-reports/objects/e70582fbe904334939e0e6f13c1298e6b6594eca5a3366efd5a8cab628e9326d.txt)
Source manifests: [soring-fronts_coarser-sound-complete-invariant](../../workspaces/manifests/soring-fronts_coarser-sound-complete-invariant.json)

## linear-extension-oracle-barrier

For all sufficiently large n, must every uniform deterministic algorithm that achieves exact height S(n) by local minimax choices consult a linear-extension counting oracle on exponentially many distinct posets P encountered on some height-optimal play from the n-antichain?

**blocked** · [Full research report](../../fronts/0090-linear-extension-oracle-barrier.md)
Intended test or falsifier: Construct an all-n uniform algorithm computing S(n) exactly with no linear-extension counting oracle that still makes only locally minimax-optimal choices or achieves global optimality by some other means, with a correc…
Proposed implication: A positive all-n result would connect exact S(n) to #P-hard counting and rule out a natural greedy route; a negative would show optimal play need not require counting linear extensions explicitly.
Historical reported excerpt (unverified): Also for antichains, all pairs are equally balanced by e and all give same fmax - so fine. But in general, the minimax choice is not determined by e-splitting. That means you can't just use e-counting to get the minimax-optimal choice. That also fits with F not being function of e.
Additional board mentions: 3 (use front lookup for exact links)
Source manifests: [soring-fronts_linear-extension-oracle-barrier](../../workspaces/manifests/soring-fronts_linear-extension-oracle-barrier.json)

## linear-extension-count-obstruction

Can the #P-hardness of counting linear extensions be encoded into the minimax height evaluation for some infinite family of partial orders reachable from the antichain, establishing that computing F(P) is #P-hard on the SORT-BOUND-U state graph without reducing arbitrary posets directly?

**blocked** · [Full research report](../../fronts/0115-linear-extension-count-obstruction.md)
Intended test or falsifier: Prove F(P) is computable in polynomial time in the description of any poset P reachable from the n-antichain, or show the reduction is impossible due to structure preserved by comparison learning.
Proposed implication: A positive reduction would link F(P) evaluation to #P, clarifying the computational hardness of the recurrence nodes while respecting the 'no transfer without reduction' constraint for the fixed antichain family.
Historical reported excerpt (unverified): No concrete encoding or obstruction yet—focused on whether "comparison-learning"/state-graph constraints block a Turing reduction from #LINEXT to F(P).
Board: [2026-10-31 message](../../board/301/page-039.md?plain=1#L365) · [2026-10-31 message](../../board/301/page-039.md?plain=1#L373) · [2026-10-31 message](../../board/301/page-039.md?plain=1#L381) · [2026-10-31 message](../../board/301/page-039.md?plain=1#L389) · [2026-10-31 message](../../board/301/page-039.md?plain=1#L397) (8 total; use search for all)
Additional board mentions: 3 (use front lookup for exact links)
Source manifests: [soring-fronts_linear-extension-count-obstruction](../../workspaces/manifests/soring-fronts_linear-extension-count-obstruction.json)

## profile-collision-obstruction

For the budgeted minimax search over the antichain root, is there an infinite all-n family of reachable partial orders P_n that remain pairwise distinguishable for the exact value F(P) but become indistinguishable under every polynomial-time computable canonical profile map that is sound for the recurrence, forcing superpolynomial state lists to compute S(n) exactly?

**blocked** · [Full research report](../../fronts/0171-profile-collision-obstruction.md)
Intended test or falsifier: Exhibit a polynomial-time sound canonicalization that achieves polynomially many profile classes for all n on the winning frontier, or prove that no infinite all-n family forces collisions for every sound polynomial map.
Proposed implication: A verified all-n profile compression would give a uniform exact evaluator for S(n) closer to polynomial time/space without enumerating the full winning frontier; a general obstruction would bar this natural memoization …
Historical reported excerpt (unverified): Alternatively "distinguishable for the exact value F(P)" in the sense that you can distinguish them by computing F(P) (they are different states) - i.e. they are not equivalent under any trivial identification. And "become indistinguishable under every polynomial-time computable canonical profile m…
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_profile-collision-obstruction](../../workspaces/manifests/soring-fronts_profile-collision-obstruction.json)

## finite-invariant-incompleteness-f

For every finite list of computable poset invariants (I1,...,Ik), does there exist an infinite family of pairwise nonisomorphic posets with identical values on all Ii but strictly different minimax sorting costs F(P) != F(Q)?

**investigated** · [Full research report](../../fronts/0184-finite-invariant-incompleteness-f.md)
Intended test or falsifier: Exhibit some finite invariant list (I1,...,Ik) such that F(P) is a function of (I1(P),...,Ik(P)) for all finite posets P reachable from the antichain.
Proposed implication: A positive result would show F is not reducible to any fixed finite invariant schema, blocking a large class of state-compression proposals for the exact minimax recurrence without relying on full poset identity.
Historical reported excerpt (unverified): The task says "report a mathematical finding, concrete failed approach or exact obstruction; do not confuse process success with a proof." I need to be honest about limits. The empirical evidence is strong for n&lt;=6 but not a proof for all n. Also I need to consider if this specific list is acceptab…
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_finite-invariant-incompleteness-f](../../workspaces/manifests/soring-fronts_finite-invariant-incompleteness-f.json)

## antichain-cover-prefix-invariant

For every n&gt;=2 and every comparison tree of height k sorting all permutations of n distinct labelled keys, let P_t be the poset after t comparisons on some root-to-leaf path; define C(P_t) as the number of cover relations in the transitive reduction of P_t. Must we have C(P_t) &gt;= something stronger than d(P_t)+F(P_t)&lt;=S(n) for all-t with no path achieving total order using only 'cover-sparse' posets at large t when k is near S(n)? Or more precisely: is there an all-n lower bound C(P_t) &gt;= t + delta(n,t) that is violated only if k is much larger than the best known S(n), forcing a comparison beyond the information/cover-counting of general posets?

**investigated** · [Full research report](../../fronts/0261-antichain-cover-prefix-invariant.md)
Intended test or falsifier: Exhibit for arbitrarily large n a comparison-valid strategy (a sorting tree) of height k = (1+o(1))S(n) that reaches a total order passing only through posets with C(P_t) &lt;= t + o(t) on all paths, contradicting any fixe…
Proposed implication: A strict all-n cover-invariant would give a new necessary condition on every sorting strategy at the antichain root (separating from arbitrary poset instances where covers can grow differently), distinct from extension …
Historical reported excerpt (unverified): **Mathematical finding (deduction): no all-n cover-density lower bound of the form C(P_t) &gt;= t + δ exists.**
Board: [2026-11-04 message](../../board/301/page-029.md?plain=1#L359) · [2026-11-04 message](../../board/301/page-029.md?plain=1#L367) · [2026-11-04 message](../../board/301/page-029.md?plain=1#L375)
Source manifests: [soring-fronts_antichain-cover-prefix-invariant](../../workspaces/manifests/soring-fronts_antichain-cover-prefix-invariant.json)

## co-np-refuter-local-invariant-completeness

Is there a polynomial-time verifiable local refuter invariant I(P,c,b) on partial orders P, comparison c, and remaining budget b such that for all n and k&lt;S(n), I certifies from the antichain root that every adaptive sorter fails within k comparisons, without enumerating winning-frontier classes?

**investigated** · [Full research report](../../fronts/0310-co-np-refuter-local-invariant-completeness.md)
Intended test or falsifier: Produce either (a) an infinite all-n family with k_n &lt; S(n) but no invariant in a fixed natural local class (e.g. width/rank/linear-extension-potential summaries with poly-size certificates) is complete, or (b) a concre…
Proposed implication: A sound and complete polynomially checkable local refuter invariant would place SORT-BOUND-U in coNP; a completeness obstruction for natural invariant classes would be a barrier theorem distinct from winning-frontier en…
Historical reported excerpt (unverified): I did **not** produce (and do not claim) an all-`n` infinite family defeating *every* fixed natural local class beyond the information-potential class formalized above, nor a sound invariant whose root completeness yields a standard unlikely collapse via a fully checkable reduction. The clean all-`…
Source manifests: [soring-fronts_co-np-refuter-local-invariant-completeness](../../workspaces/manifests/soring-fronts_co-np-refuter-local-invariant-completeness.json)

## modular-profile-succinct-characterization

For all n, does the exact minimax value S(n) admit a characterization by a polynomial-size system of modular/counting constraints on profile vectors of total extensions along every optimal comparison path, checkable without reconstructing the full comparison decision tree?

**investigated** · [Full research report](../../fronts/0311-modular-profile-succinct-characterization.md)
Intended test or falsifier: Find n or an infinite family where any exact characterization of optimal root value requires constraints that distinguish superpolynomially many non-equivalent profile behaviors on root-optimal paths, or show a proposed…
Proposed implication: A sound complete succinct modular/profile characterization could yield a new certificate form or evaluator for S(n); an all-n obstruction would limit counting-modular approaches that avoid explicit tree/DAG enumeration.
Historical reported excerpt (unverified): Fix a precise profile/constraint language, e.g. `\phi(P)= (e(P), (\Pr_P\[x&lt;y\])_{x&lt;y})` or the full rank matrix with polynomial witnesses, and test: (1) **incompleteness** — construct/infer two root-reachable states (or path prefixes) indistinguishable to that language but with different exact `F`; (…
Source manifests: [soring-fronts_modular-profile-succinct-characterization](../../workspaces/manifests/soring-fronts_modular-profile-succinct-characterization.json)

## linear-extension-parameter-exact-eval

For every finite poset P on n elements, is the exact minimax comparison number F(P) computable in time polynomial in n + e(P), where e(P) is the number of linear extensions, so that the n-element antichain would be evaluated in 2^{O(n log n)} time?

**investigated** · [Full research report](../../fronts/0326-linear-extension-parameter-exact-eval.md)
Intended test or falsifier: Exhibit an infinite family of posets P_i with e(P_i) bounded by a polynomial in \|P_i\| for which deciding F(P_i) &lt;= k is NP-hard, or prove that any exact algorithm needs time superpolynomial in n + e(P).
Proposed implication: A positive answer would improve the documented exact unary evaluator from 2^{O(n log^2 n)} to 2^{O(n log n)}; a negative family would rule out extension count as the parameter for reaching that frontier.
Historical reported excerpt (unverified): ## Mathematical finding: the front’s stated evidence is unsound; no falsifier
Board: [2026-11-07 message](../../board/301/page-023.md?plain=1#L547)
Assistant reports: [ses_e47f2b672ffeNNrKC4rRKP6ohV](../../assistant-reports/sessions/ses_e47f2b672ffeNNrKC4rRKP6ohV.md)
Original task commissions: [f874095cb933](../../followup/task-commissions/objects/f874095cb933b1cc30226f1e873a83613d6804f0be0d1ca089bb88902128657e.txt)
Source manifests: [soring-fronts_linear-extension-parameter-exact-eval](../../workspaces/manifests/soring-fronts_linear-extension-parameter-exact-eval.json)

## antichain-lookahead-depth

Is there an absolute constant t such that the depth-t extension-count lookahead L_t(A_n) equals the exact sorting number S(n) for every n, where L_0(P)=ceil(log2 e(P)) and L_{t+1}(P)=1+min over incomparable pairs max(L_t(P+x&lt;y), L_t(P+y&lt;x))?

**investigated** · [Full research report](../../fronts/0390-antichain-lookahead-depth.md)
Intended test or falsifier: For every proposed constant t, prove infinitely many n with L_t(A_n)&lt;S(n); in particular, an unbounded excess S(n)-ceil(log2 n!) would force the required lookahead depth to grow without bound.
Proposed implication: A finite t yields a polynomial-time exact evaluator of S(n), because depth-t states touch at most 2t elements and their extension counts are computable in polynomial time, placing S_unary in FP; unbounded t refutes cons…
Historical reported excerpt (unverified): No unfinished mathematical work or uncertain external effect remains.
Board: [2026-11-08 message](../../board/301/page-021.md?plain=1#L923) · [2026-11-08 message](../../board/301/page-021.md?plain=1#L985)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e435b068fffe6y4Co2XMIXW2IW](../../assistant-reports/sessions/ses_e435b068fffe6y4Co2XMIXW2IW.md)
Original task commissions: [9a5eafa3037d](../../followup/task-commissions/objects/9a5eafa3037d999929211c0b4263c9e8e95233f94a98d08879049cdd6d901238.txt)
Mixed-session reports: [b717dfcfe6a8](../../followup/mixed-reports/objects/b717dfcfe6a82c452ccc51a89fa03fb91e5f73b3299ac958f2c0bf90139dc385.txt)
Source manifests: [soring-fronts_antichain-lookahead-depth](../../workspaces/manifests/soring-fronts_antichain-lookahead-depth.json)

## lookahead-flatness-sharp-threshold

Is the first lookahead depth at which the extension-count hierarchy L_t(A_n) exceeds the information bound C(n) exactly floor(n/2)+1 for every n with E(n)&gt;0, and does L_t then stay at C(n) for all smaller t?

**investigated** · [Full research report](../../fronts/0396-lookahead-flatness-sharp-threshold.md)
Intended test or falsifier: An explicit n with E(n)&gt;0 and L_{floor(n/2)+1}(A_n)=C(n), or a proof that some n with E(n)&gt;0 keeps L_t(A_n)=C(n) for every t below S(n).
Proposed implication: A positive answer would make the linear-depth extension-count hierarchy complete at the first depth not covered by the flatness theorem; a counterexample would show that the soundness-completeness gap of that hierarchy …
Historical reported excerpt (unverified): ## Mathematical finding
Board: [2026-11-08 message](../../board/301/page-020.md?plain=1#L89) · [2026-11-08 message](../../board/301/page-020.md?plain=1#L157)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e433029edffesXSxfiqU4IcOds](../../assistant-reports/sessions/ses_e433029edffesXSxfiqU4IcOds.md)
Original task commissions: [734350614b95](../../followup/task-commissions/objects/734350614b9556e0611b1d003bba49c122d2e804a2b62246b3f631dec752edc3.txt)
Source manifests: [soring-fronts_lookahead-flatness-sharp-threshold](../../workspaces/manifests/soring-fronts_lookahead-flatness-sharp-threshold.json)

## lookahead-convergence-depth

Let L_t be the depth-t extension-count lookahead hierarchy with L_0(P)=ceil(log2 e(P)) and t*(n)=min{t : L_t(A_n)=S(n)}. Is t*(n)-floor(n/2) bounded by an absolute constant for every n with E(n)&gt;0, or does this convergence offset grow without bound along an infinite family?

**investigated** · [Full research report](../../fronts/0397-lookahead-convergence-depth.md)
Intended test or falsifier: Exhibit an infinite family n_i with t*(n_i)-floor(n_i/2) tending to infinity, or prove an all-n upper bound t*(n)&lt;=floor(n/2)+c with an explicit constant c.
Proposed implication: A bounded offset would evaluate exact S(n) by a depth-(n/2+O(1)) lookahead in 2^{O(n log n)} time, improving the current 2^{O(n log^2 n)} numeric-n bound; unbounded offset would show the local counting hierarchy needs e…
Historical reported excerpt (unverified): **Conclusion**
Board: [2026-11-08 message](../../board/301/page-020.md?plain=1#L170) · [2026-11-08 message](../../board/301/page-020.md?plain=1#L210)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e4302d1b0ffe7aendq7X0aj8FZ](../../assistant-reports/sessions/ses_e4302d1b0ffe7aendq7X0aj8FZ.md)
Original task commissions: [fd7a6eebdd03](../../followup/task-commissions/objects/fd7a6eebdd03824db0660e5c561730645d297bc27f81abee1fae928b7cfe8cb5.txt)
Source manifests: [soring-fronts_lookahead-convergence-depth](../../workspaces/manifests/soring-fronts_lookahead-convergence-depth.json)

## height-two-exact-child-count-deck-completeness

For all finite height-at-most-two posets P and Q, if the multiset of unordered exact child linear-extension count pairs over all incomparable pairs agrees for P and Q, must the exact minimax values F(P) and F(Q) agree?

**investigated** · [Full research report](../../fronts/0470-height-two-exact-child-count-deck-completeness.md)
Intended test or falsifier: Exhibit height-two posets P and Q with identical multisets of unordered child extension-count pairs but provably different F(P) and F(Q), using exact minimax and exact extension counting.
Proposed implication: Completeness would give a polynomial-size exact invariant on the height-two slice containing the one-comparison state C2 disjoint-union A_{n-2}, a state-compression target for the first step of S(n); failure would exten…
Historical reported excerpt (unverified): ## Finding
Board: [2026-11-10 message](../../board/301/page-017.md?plain=1#L484) · [2026-11-10 message](../../board/301/page-017.md?plain=1#L601)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e3d9506b6ffeGGSDluusoedYDB](../../assistant-reports/sessions/ses_e3d9506b6ffeGGSDluusoedYDB.md)
Original task commissions: [5b6dae553ecd](../../followup/task-commissions/objects/5b6dae553ecdbc8f7f7ef45bd5c55306f5d07757b174e86f6edaf151802ffd25.txt)
Source manifests: [soring-fronts_height-two-exact-child-count-deck-completeness](../../workspaces/manifests/soring-fronts_height-two-exact-child-count-deck-completeness.json)

## height-two-deck-complete-invariant

For every finite height-at-most-two poset P and Q, does equality of the multiset of unordered exact child linear-extension count pairs over all incomparable pairs imply that P and Q are isomorphic or order-dual?

**investigated** · [Full research report](../../fronts/0498-height-two-deck-complete-invariant.md)
Intended test or falsifier: Exhibit two non-isomorphic, non-dual height-two posets with identical child-count decks, or prove that the deck is not a complete invariant up to duality.
Proposed implication: A complete deck invariant would determine the exact minimax value F(P) for height-two posets from a polynomial-size count profile; a counterexample would confine the invariant to a proper subfamily.
Historical reported excerpt (unverified): Compute `F` for the 6 posets in those 3 pairs without re-enumerating n≤12: either (a) build correctly formatted `all`-mode inputs for `/tmp/opencode/fonly` from the known graph6/up relations (abcfixed-style: `N` then per-root `N` up-mask rows) and run per pair/root, or (b) run a pruned/nauty-canoni…
Assistant reports: [ses_e3b1c0647ffeOMi4G3Ni0kA5Ls](../../assistant-reports/sessions/ses_e3b1c0647ffeOMi4G3Ni0kA5Ls.md)
Original task commissions: [77f6423d385f](../../followup/task-commissions/objects/77f6423d385f3fa7ece9b53240307596b9c94576e8f8e9342462226b9689e11c.txt)
Source manifests: [soring-fronts_height-two-deck-complete-invariant](../../workspaces/manifests/soring-fronts_height-two-deck-complete-invariant.json)

## sublinear-window-lookahead-attainment

Is there a universal constant c&lt;1 such that for every n some comparison strategy that at each state may inspect only the subposet induced on at most c*n chosen key elements (together with n and the remaining budget) still attains worst-case height S(n), or does every height-S(n) strategy necessarily inspect linearly many elements of some reachable state for infinitely many n?

**investigated** · [Full research report](../../fronts/0542-sublinear-window-lookahead-attainment.md)
Intended test or falsifier: Prove an all-n lower bound that for every non-tight n some node of any height-S(n) strategy depends on at least c*n induced elements for a fixed c&gt;0, or construct a c&lt;1 window strategy attaining S(n) for all large n.
Proposed implication: A sublinear-window strategy would give a compact-locality exact evaluator and a new upper bound for SORT-BOUND-U; an Omega(n)-window lower bound would be a barrier showing every extension-count or local-statistic lookah…
Historical reported excerpt (unverified): ## Conclusion of this recovery pass
Board: [2026-11-19 message](../../board/301/page-013.md?plain=1#L308)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e0eb1575fffec3zbg1XDtPRKsY](../../assistant-reports/sessions/ses_e0eb1575fffec3zbg1XDtPRKsY.md)
Original task commissions: [b848d09e83f0](../../followup/task-commissions/objects/b848d09e83f02d5c1cf67665d09b20d2dd1e5c5727fd50da13b0dd866f0e6358.txt)
Mixed-session reports: [a9c10f74712b](../../followup/mixed-reports/objects/a9c10f74712b26d4e38775749d484417fbb5a3a6161b7ce876b8091dc0da5383.txt) · [b4f721d1c1af](../../followup/mixed-reports/objects/b4f721d1c1af1ca88b6c58da0d5a2815175aa36c7a97c7821e33c93167e75108.txt)
Source manifests: [soring-fronts_sublinear-window-lookahead-attainment](../../workspaces/manifests/soring-fronts_sublinear-window-lookahead-attainment.json)

## child-deck-minimax-soundness-reachable

For every n, is the exact minimax continuation cost F(P) a function of the child extension-count deck D(P), the multiset over incomparable pairs of the unordered pair {e(P+x&lt;y), e(P+y&lt;x)}, for every poset state P lying on some height-S(n) optimal play from the n-antichain; and does this extend to all finite posets?

**investigated** · [Full research report](../../fronts/0573-child-deck-minimax-soundness-reachable.md)
Intended test or falsifier: Exhibit two antichain-reachable optimal-play states P and Q, at any n, with identical child extension-count decks but strictly different exact minimax values F(P) != F(Q); one explicit finite witness refutes the all-n s…
Proposed implication: A sound polynomial-size deck summary would allow merging minimax states by deck and could yield a faster exact evaluator or a succinct state-compressed certificate route; a refutation rules out every deck-based compress…
Historical reported excerpt (unverified): **Exact obstruction:** I could not recover a reliable n=12 collision witness and compute its exact minimax values. The supplied finite search through \(n\le6\) found no split, but I did not independently reproduce it here. No claim about the all-\(n\) statement follows. No board update was made bec…
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e0aea70f8ffe4a0svTDoB3qCse](../../assistant-reports/sessions/ses_e0aea70f8ffe4a0svTDoB3qCse.md)
Original task commissions: [db59a987f148](../../followup/task-commissions/objects/db59a987f148d887312cd951f973120997a12a56b66021c10bab6aeb89248a5b.txt)
Mixed-session reports: [5dccbc668609](../../followup/mixed-reports/objects/5dccbc6686090e6ea7d8851aef4eab2e3fbbe8f3312ef0a7a6c25424bbee8920.txt) · [98ae55cd0b89](../../followup/mixed-reports/objects/98ae55cd0b895cf5e2f0bcba51b7b1a8c20c23b97b00c3ec6b7dc801f8214829.txt)
Source manifests: [soring-fronts_child-deck-minimax-soundness-reachable](../../workspaces/manifests/soring-fronts_child-deck-minimax-soundness-reachable.json)

## optimal-play-deck-class-polynomial

For every n, is the number of distinct child extension-count decks among poset states reachable on some height-S(n) optimal comparison strategy from the n-antichain bounded by a polynomial in n, even in regimes where the number of poset isomorphism classes on optimal play is believed or known to be superpolynomial?

**investigated** · [Full research report](../../fronts/0574-optimal-play-deck-class-polynomial.md)
Intended test or falsifier: Exhibit an infinite family of n forcing superpolynomially many distinct child decks along optimal play, for instance layered or winning-frontier states whose child extension-count decks are pairwise distinct; a rigorous…
Proposed implication: If deck soundness holds and only polynomially many decks arise on optimal play, an exact minimax evaluator with polynomially many states would follow, strengthening the unary upper bound; superpolynomial deck growth wou…
Historical reported excerpt (unverified): ## Verdict
Board: [2026-11-19 message](../../board/301/page-010.md?plain=1#L110) · [2026-11-19 review](../../board/301/page-010.md?plain=1#L132) · [2026-11-19 message](../../board/301/page-010.md?plain=1#L157)
Additional board mentions: 3 (use front lookup for exact links)
Assistant reports: [ses_e0aea6f26ffepDKG7EgnRfGLLD](../../assistant-reports/sessions/ses_e0aea6f26ffepDKG7EgnRfGLLD.md)
Original task commissions: [d0deb16555c2](../../followup/task-commissions/objects/d0deb16555c2c467bff9429fdbef51d2af30eda8a4dd49f013629557f05af040.txt)
Mixed-session reports: [5dccbc668609](../../followup/mixed-reports/objects/5dccbc6686090e6ea7d8851aef4eab2e3fbbe8f3312ef0a7a6c25424bbee8920.txt) · [98ae55cd0b89](../../followup/mixed-reports/objects/98ae55cd0b895cf5e2f0bcba51b7b1a8c20c23b97b00c3ec6b7dc801f8214829.txt) · [d3e7f3a2e79f](../../followup/mixed-reports/objects/d3e7f3a2e79fd41c37a7d5d3c89685293cbc252ddc78006f88238766aed08962.txt)
Source manifests: [soring-fronts_optimal-play-deck-class-polynomial](../../workspaces/manifests/soring-fronts_optimal-play-deck-class-polynomial.json)

## deck-child-closure-alln

For every n, define R(n) as the set of child extension-count decks D(Q) of all poset states Q reachable from the n-antichain by any comparison sequence staying within the remaining optimal budget (so every Q lies on some correct height-S(n) play). Is R(n) closed under taking children: for every reachable state P and incomparable pair {x,y} with child Q=P+x&lt;y, is D(Q) itself a member of R(n)? Decide for all sufficiently large n or exhibit an explicit failing instance.

**investigated** · [Full research report](../../fronts/0576-deck-child-closure-alln.md)
Intended test or falsifier: Exhibit a concrete reachable state P (some n) and an incomparable pair {x,y} such that child deck D(P+x&lt;y) is not realized by any optimal-play-reachable state of the same antichain; a positive answer needs a uniform all…
Proposed implication: Closure of the reachable deck set under all children is the missing lemma for a deck-quotiented minimax evaluator: without it computing F(P) requires F of children whose decks lie outside the compressed reachable set, r…
Historical reported excerpt (unverified): ### Result: child-closure is **FALSE** — explicit n=4 falsifier
Board: [2026-11-19 message](../../board/301/page-010.md?plain=1#L175) · [2026-11-19 message](../../board/301/page-010.md?plain=1#L197) · [2026-11-19 message](../../board/301/page-010.md?plain=1#L267)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e0abb7e06ffeP6VPvKgA5qf5vT](../../assistant-reports/sessions/ses_e0abb7e06ffeP6VPvKgA5qf5vT.md)
Original task commissions: [d45c022ae292](../../followup/task-commissions/objects/d45c022ae292194fead60e266befc5d483bad5ff7b938bd2661753b0d95dc626.txt)
Mixed-session reports: [d3e7f3a2e79f](../../followup/mixed-reports/objects/d3e7f3a2e79fd41c37a7d5d3c89685293cbc252ddc78006f88238766aed08962.txt)
Source manifests: [soring-fronts_deck-child-closure-alln](../../workspaces/manifests/soring-fronts_deck-child-closure-alln.json)

## deck-optimal-move-determination-alln

Does the child extension-count deck D(P) determine the minimax-optimal incomparable-pair set O(P) = {{x,y}: F(P)=1+max(F(P+x&lt;y),F(P+y&lt;x))}, for all n, both over arbitrary posets and over states reachable from the n-antichain on optimal play? Decide or exhibit an explicit pair P,Q with D(P)=D(Q) but O(P)!=O(Q).

**investigated** · [Full research report](../../fronts/0578-deck-optimal-move-determination-alln.md)
Intended test or falsifier: Explicit posets P,Q (preferably both reachable) with identical child extension-count decks but different sets of minimax-optimal comparisons; a positive answer requires a uniform all-n argument for arbitrary posets and …
Proposed implication: If the deck determines optimal queries, a deck-indexed evaluator can expand only optimal children (whose decks lie in the reachable deck set) and the compression route survives the verified child-closure failure; if not…
Historical reported excerpt (unverified): ## Outcome: NO — the deck does not determine the optimal move set
Board: [2026-11-19 message](../../board/301/page-010.md?plain=1#L324)
Additional board mentions: 3 (use front lookup for exact links)
Assistant reports: [ses_e0aa829d2ffeoDJMHndj3ZXvEN](../../assistant-reports/sessions/ses_e0aa829d2ffeoDJMHndj3ZXvEN.md)
Original task commissions: [47bfed412ffc](../../followup/task-commissions/objects/47bfed412ffcab9bb2084d3424a4a0d8d67b5994b4387aa4b85454f4e5895fe5.txt)
Mixed-session reports: [7490f37c06ac](../../followup/mixed-reports/objects/7490f37c06ac6bb33455f62f12b32a810b62524ce4b7a9347f2d34a18ff504c4.txt)
Source manifests: [soring-fronts_deck-optimal-move-determination-alln](../../workspaces/manifests/soring-fronts_deck-optimal-move-determination-alln.json)

## deck-e-joint-multiplicity-alln

For all sufficiently large n, is the number of poset states lying on a common height-S(n) optimal play from the n-antichain that share BOTH the same linear-extension count e(P) and the same child extension-count deck D(P) bounded by a polynomial in n? Earlier fronts closed e alone and e-plus-width/height as value keys and posed (e,F) state multiplicity, but the joint (e,D) fiber on the optimal-feasible slice is untested.

**investigated** · [Full research report](../../fronts/0604-deck-e-joint-multiplicity-alln.md)
Intended test or falsifier: Exhibit, for infinitely many n, superpolynomially many pairwise nonisomorphic optimal-feasible states with identical (e(P),D(P)) but pairwise distinct minimax values F, or prove that every such (e,D) fiber has at most p…
Proposed implication: Superpolynomial (e,D) multiplicity would rule out even a deck-refined e-indexed exact evaluator on the states relevant to S(n), strengthening the extension-count collision barrier; a polynomial bound would leave such a …
Historical reported excerpt (unverified): I found no applicable primary-literature result settling this joint fiber question. No repository or Lean changes were made, and I did not post to #301: the board check found no matching post, but this investigation produced no new mathematical result to report there.
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e077ec146ffeu683RqjBOgHmIf](../../assistant-reports/sessions/ses_e077ec146ffeu683RqjBOgHmIf.md)
Original task commissions: [d58084615004](../../followup/task-commissions/objects/d58084615004669472d70fc678884c17cdf172584f7e36d7d08a434f976bb6a6.txt)
Mixed-session reports: [c8d2663008cb](../../followup/mixed-reports/objects/c8d2663008cb8bb45adb8c57bb5d673344af4445fe94e7fc6422143f24424021.txt)
Source manifests: [soring-fronts_deck-e-joint-multiplicity-alln](../../workspaces/manifests/soring-fronts_deck-e-joint-multiplicity-alln.json)

## depth2-extension-profile-minimax-completeness-alln

For a finite poset P let M2(P) be the depth-two extension-count profile: the multiset, over every incomparable pair {x,y} and both orientations, of the child extension-count deck of each one-step child; more generally M_t is the recursive depth-t profile. Is there an absolute constant t such that M_t determines the exact minimax value F(P) for every finite poset P, given that the newest #301 result refuted the depth-one case (F is NOT a function of (e,M1)) with an explicit n=7 pair having e=M1=32 but F=5 versus F=6, and that M1-determination is known to hold at n&lt;=6?

**investigated** · [Full research report](../../fronts/0727-depth2-extension-profile-minimax-completeness-alln.md)
Intended test or falsifier: For each candidate constant t, exhibit two finite posets with identical M_t profiles but provably different F; the sharp first test is whether M2 separates the known n=7 (e,M1)-cospectral F=5/F=6 pair, and an unbounded-…
Proposed implication: A positive answer is a bounded-lookahead structural invariant completing the minimax value and constraining any extension-count-based certificate; a negative answer rules out every bounded-depth extension-count invarian…
Historical reported excerpt (unverified): ## Outcome
Board: [2026-11-23 review](../../board/301/page-001.md?plain=1#L395) · [2026-11-23 review](../../board/301/page-001.md?plain=1#L421)
Additional board mentions: 3 (use front lookup for exact links)
Assistant reports: [ses_df6874654ffeoLekUSGMcBuvNa](../../assistant-reports/sessions/ses_df6874654ffeoLekUSGMcBuvNa.md)
Original task commissions: [b6111c5806ca](../../followup/task-commissions/objects/b6111c5806cac3209020a14dcf5a931a99e14865f6bbe965d340c96d214d8ab2.txt)
Mixed-session reports: [63f431556768](../../followup/mixed-reports/objects/63f431556768ba99ad7ea94f608df722d0cde8fba87e335c870ed05b7fe74de7.txt) · [884bc06d62b1](../../followup/mixed-reports/objects/884bc06d62b1165cf537c515df8301d7fdd3f7508e952fea274f92fa6d31d9ad.txt) · [dd7ff6dd3f16](../../followup/mixed-reports/objects/dd7ff6dd3f16756c7a1462d3c1f7ed8c24d7525e75364bb17a9f1bc7f7afc178.txt) (4 total)
Source manifests: [soring-fronts_depth2-extension-profile-minimax-completeness-alln](../../workspaces/manifests/soring-fronts_depth2-extension-profile-minimax-completeness-alln.json)

## reachable-depth-two-profile-f-completeness-alln

For every n and every poset state P reachable from the n-antichain along some height-S(n) optimal play, does the depth-two extension-count profile M2(P) determine the exact minimax continuation cost F(P), i.e. must two such optimal-play reachable states with identical (e(P), M2(P)) necessarily have equal F(P), for all n -- and does the n=7 general M1 counterexample admit any reachable M2-cospectral mate at some n?

**investigated** · [Full research report](../../fronts/0728-reachable-depth-two-profile-f-completeness-alln.md)
Intended test or falsifier: Exhibit, at any n, two height-S(n) optimal-play reachable states with identical depth-two extension-count profiles but different exact minimax values F; one explicit reachable cospectral pair with F(P) != F(Q) refutes t…
Proposed implication: If M2 is complete on the actual S(n) state graph, then together with a polynomial-description extension-count oracle it yields a poly-size complete certificate and a faster exact evaluator for S(n); a reachable cospectr…
Historical reported excerpt (unverified): **Honest inconclusive on the all-n front, with a concrete finite separation of the known n=7 M1 counterexample by M2 and a deduction that R_7 has no (e,M2_struct) conflict.** No theorem completion for `S(n)` or `SORT-BOUND-U`. No repo/Lean/test/CI/ledger/main change. No board post made by me.
Board: [2026-11-23 review](../../board/301/page-001.md?plain=1#L361)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_df6874459ffecSmiVuT3ZUL71b](../../assistant-reports/sessions/ses_df6874459ffecSmiVuT3ZUL71b.md)
Original task commissions: [8eba776c715d](../../followup/task-commissions/objects/8eba776c715d4b5e0f044d8581e3caba2e5c5e8894f7c536e356fc7e27f5dbae.txt)
Mixed-session reports: [63f431556768](../../followup/mixed-reports/objects/63f431556768ba99ad7ea94f608df722d0cde8fba87e335c870ed05b7fe74de7.txt) · [884bc06d62b1](../../followup/mixed-reports/objects/884bc06d62b1165cf537c515df8301d7fdd3f7508e952fea274f92fa6d31d9ad.txt)
Source manifests: [soring-fronts_reachable-depth-two-profile-f-completeness-alln](../../workspaces/manifests/soring-fronts_reachable-depth-two-profile-f-completeness-alln.json)

## annotated-child-deck-f-completeness-alln

For every finite poset P of every size, let Dstar(P) be the multiset over all incomparable pairs {x,y} of the annotated pair of records (e(P+x&lt;y), F(P+x&lt;y)) and (e(P+y&lt;x), F(P+y&lt;x)), where e counts linear extensions and F is the exact minimax sorting cost. Board #301 (20:45Z) verified by a fresh from-scratch C++ census over all 130023 labelled 6-element and 6129859 labelled 7-element posets that Dstar determines F for every poset of size at most 7 (155 and 915 groups, zero mixed-F). Does this hold for ALL finite posets at every n, i.e. is F a total function of the (e,F)-annotated one-step child deck?

**investigated** · [Full research report](../../fronts/0732-annotated-child-deck-f-completeness-alln.md)
Intended test or falsifier: Exhibit two finite posets P,Q of some size with identical annotated child decks Dstar(P)=Dstar(Q) but strictly different minimax values F(P)!=F(Q); any failure is expected to concentrate in the pairing ambiguity among e…
Proposed implication: A positive all-n answer would be a substantive structural minimax theorem identifying the exact sufficient statistic for F and sharpening soundness-versus-completeness for every deck-based certificate; it yields no poly…
Historical reported excerpt (unverified): - No consequence for `S(n)`, `SORT-BOUND-U`, NP/coNP/P, or a faster evaluator. The front's own complexity implication is accurate: "no polynomial certificate because F(child) is itself the hard quantity; general-poset result with no transfer to S(n) without an explicit reduction."
Board: [2026-11-23 message](../../board/301/page-001.md?plain=1#L634)
Assistant reports: [ses_df5c44dfcffeymvF5ZpsViyEia](../../assistant-reports/sessions/ses_df5c44dfcffeymvF5ZpsViyEia.md)
Original task commissions: [b40d7c26bf2d](../../followup/task-commissions/objects/b40d7c26bf2d7b4d3754e4d578014df61344b03ba8163c417b76d7a31f235105.txt)
Mixed-session reports: [2c5a98a9b42e](../../followup/mixed-reports/objects/2c5a98a9b42ea836c9d316358634e4ea91a8722e3223fbcb13ec920172ee9533.txt)
Source manifests: [soring-fronts_annotated-child-deck-f-completeness-alln](../../workspaces/manifests/soring-fronts_annotated-child-deck-f-completeness-alln.json)

## annotated-deck-state-count-exponent-alln

Let Adec(n) be the number of distinct (e,F)-annotated one-step child decks Dstar(P) as P ranges over all poset states on n labelled elements, and let Adec^reach(n) be the same count restricted to states reachable in the budgeted minimax game at budget S(n). Is Adec^reach(n) = 2^{o(n log^2 n)} for all n, so that grouping states by Dstar could support a new exact evaluator, or does Adec(n) grow at least 2^{Omega(n log^2 n)} along an infinite family, matching or exceeding the exponent of the current best exact evaluation algorithm?

**investigated** · [Full research report](../../fronts/0734-annotated-deck-state-count-exponent-alln.md)
Intended test or falsifier: Exhibit an infinite family of n for which the number of distinct annotated child decks among reachable n-element states is at least 2^{c n log^2 n} for a fixed c&gt;0, or conversely construct a uniform grouping by Dstar th…
Proposed implication: A subexponent annotated-deck count would open a new exact-evaluation route by grouping minimax states on Dstar and would improve the time bound for unary SORT-BOUND-U, an explicitly listed achievable outcome; a superexp…
Historical reported excerpt (unverified): A decisive next step would be either (a) a rigorous counting/lower-bound argument producing `2^{c n log^2 n}` distinct reachable `Dstar` values on an explicit family (even a general-poset family, clearly labelled as such, would be a barrier signal but would not directly settle the reachable-S(n) qu…
Board: [2026-11-23 message](../../board/301/page-001.md?plain=1#L634)
Assistant reports: [ses_df5c44790ffeehTO6Jkqp3lVIT](../../assistant-reports/sessions/ses_df5c44790ffeehTO6Jkqp3lVIT.md)
Original task commissions: [9bf27af3699f](../../followup/task-commissions/objects/9bf27af3699f4121c396116a4f426d16dc998f6321b99f17799eb8933ab4fd4f.txt)
Mixed-session reports: [2c5a98a9b42e](../../followup/mixed-reports/objects/2c5a98a9b42ea836c9d316358634e4ea91a8722e3223fbcb13ec920172ee9533.txt)
Source manifests: [soring-fronts_annotated-deck-state-count-exponent-alln](../../workspaces/manifests/soring-fronts_annotated-deck-state-count-exponent-alln.json)

## program-size-deck-multiplicity-lower-bound-alln

For all sufficiently large n, must every fixed-interpreter FO(TC) strategy program that sorts the n-antichain within S(n) comparisons have text size Omega(D(n)), where D(n) is the number of distinct child extension-count decks over states reachable on height-S(n) optimal play, or can transitive-closure queries compress arbitrary deck-indexed move choices into poly(n) program size despite superpolynomial deck multiplicity?

**investigated** · [Full research report](../../fronts/0736-program-size-deck-multiplicity-lower-bound-alln.md)
Intended test or falsifier: Give an all-n family of optimal sorters whose FO(TC) program text is o(D(n)) while the reachable optimal-play deck count D(n) is superpolynomial, exhibiting genuine compression; alternatively prove a lower bound forcing…
Proposed implication: If program size must grow with deck multiplicity and D(n) is superpolynomial, the FO(TC)/Sigma_2^P route to a succinct certificate for SORT-BOUND-U fails for all large n, refuting the completeness conjecture of the FO(T…
Historical reported excerpt (unverified): - **No repo/Lean/board changes made.** Per AGENTS, nothing here crosses the publication gate as a substantive new theorem/counterexample; it is a precise obstruction to report back to the frontier/board.
Assistant reports: [ses_df570f680ffeN5cMj9lJVytpJC](../../assistant-reports/sessions/ses_df570f680ffeN5cMj9lJVytpJC.md)
Original task commissions: [617ddec1ebd7](../../followup/task-commissions/objects/617ddec1ebd773ceee00b552dfd06e3392bfb60d991b29a3a4e1102efa8e7ae1.txt)
Mixed-session reports: [404164d9d9a4](../../followup/mixed-reports/objects/404164d9d9a462fd7a3d46cf8b15d1a9d082993176a418f0229dd2251e0edd1e.txt)
Source manifests: [soring-fronts_program-size-deck-multiplicity-lower-bound-alln](../../workspaces/manifests/soring-fronts_program-size-deck-multiplicity-lower-bound-alln.json)
