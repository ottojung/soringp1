# Logic, complexity and encodings

[Catalogue home](../README.md) · [Evidence status guide](../../RESULTS.md)

Status is the original workflow label, not mathematical proof. Linked messages may contain corrections or rejected claims.

## fo-tc-two-phase-n8-verify-20261027

Independently verify the pushed n=8 two-phase FO(TC) exact sorting witness (branch research/JTsW4AnxTLzN18IBQibXea-fo-tc-twophase-E5ZrMYvzZMAF98F5N7FYSx at 1f27d8e) with a fresh checker, then advance one barrier cell: either the n=9 two-phase extension (bounded exhaustive/memoized search with recorded space estimate) or a computed next cell of the two-phase cost/phase-count barrier as n grows.

**investigated** · [Full research report](../../fronts/0011-fo-tc-two-phase-n8-verify-20261027.md)
Board: [2026-10-27 message](../../board/301/page-044.md?plain=1#L82) · [2026-10-27 message](../../board/JTsW4AnxTLzN18IBQibXea-fervor/page-002.md?plain=1#L223) · [2026-10-27 message](../../board/JTsW4AnxTLzN18IBQibXea-fervor/page-002.md?plain=1#L231)
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_fo-tc-two-phase-n8-verify-20261027](../../workspaces/manifests/soring-fronts_fo-tc-two-phase-n8-verify-20261027.json)

## fo-tc-combined-complexity-sort-bound

Can a fixed uniform FO(TC) interpreter with explicit combined complexity yield a nontrivial upper bound for SORT-BOUND-U, or is there a precise barrier separating data complexity (NL) from combined complexity for this minimax threshold?

**investigated** · [Full research report](../../fronts/0030-fo-tc-combined-complexity-sort-bound.md)
Historical reported excerpt: ### Verdict
Additional board mentions: 2 (use front lookup for exact links)
Source manifests: [soring-fronts_fo-tc-combined-complexity-sort-bound](../../workspaces/manifests/soring-fronts_fo-tc-combined-complexity-sort-bound.json)

## turing-hardness-unary-sortbound

Is SORT-BOUND-U PSPACE-hard under polynomial-time Turing reductions (as opposed to many-one), or can every PSPACE language be decided by a polynomial-time oracle machine that queries SORT-BOUND-U?

**investigated** · [Full research report](../../fronts/0032-turing-hardness-unary-sortbound.md)
Source manifests: [soring-fronts_turing-hardness-unary-sortbound](../../workspaces/manifests/soring-fronts_turing-hardness-unary-sortbound.json)

## fo-lfp-descriptive-complexity

Can SORT-BOUND-U be defined by a fixed-point logic formula (FO(LFP) or FO(PFP)) on ordered structures that is faithful to the unary encoding and yields a tight complexity correspondence? Does such a definition imply membership in P or only in PSPACE?

**investigated** · [Full research report](../../fronts/0036-fo-lfp-descriptive-complexity.md)
Source manifests: [soring-fronts_fo-lfp-descriptive-complexity](../../workspaces/manifests/soring-fronts_fo-lfp-descriptive-complexity.json)

## root-forcing-vs-residual-hardness

For every large n, does there exist some first comparison from the antichain root such that every outcome is a poset P with S(P) &lt;= S(n)-1 and F(P) &gt;= something nontrivial, or is there an all-n adversary strategy that can preserve S(P)=S(n)-1 on both branches for some root choice?

**investigated** · [Full research report](../../fronts/0041-root-forcing-vs-residual-hardness.md)
Source manifests: [soring-fronts_root-forcing-vs-residual-hardness](../../workspaces/manifests/soring-fronts_root-forcing-vs-residual-hardness.json)

## tally-np-membership-collapse

Is there an all-n polynomial-time many-one reduction from some NP-complete language to SORT-BOUND-U, or is NP membership of SORT-BOUND-U provably false under known barriers without implying P=NP?

**investigated** · [Full research report](../../fronts/0049-tally-np-membership-collapse.md)
Historical reported excerpt: **Finding (mathematical):**
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_tally-np-membership-collapse](../../workspaces/manifests/soring-fronts_tally-np-membership-collapse.json)

## ph-hierarchy-alternation-depth

For unary SORT-BOUND-U, does every polynomial-time alternating Turing machine deciding it require alternation depth omega(log N) on infinitely many input lengths N, or is there a fixed constant k with SORT-BOUND-U in Sigma_k^P union Pi_k^P?

**investigated** · [Full research report](../../fronts/0056-ph-hierarchy-alternation-depth.md)
Historical reported excerpt: **Conclusion (honest):** Genuinely open. The move-by-move game gives polynomial alternations; fixed alternation would require a succinct compressed strategy with no known obstruction-evading representation, while fixed-level PH is not obviously ruled out by sparsity/barriers. No all-n theorem or co…
Board: [2026-10-30 message](../../board/301/page-043.md?plain=1#L367)
Source manifests: [soring-fronts_ph-hierarchy-alternation-depth](../../workspaces/manifests/soring-fronts_ph-hierarchy-alternation-depth.json)

## adversary-game-alternation-bound

For the natural minimax game for S(n) with alternation depth equal to the decision depth, does there exist an all-n strategy-compression that reduces alternation to O(log n) blocks without exponential certificate blowup?

**investigated** · [Full research report](../../fronts/0067-adversary-game-alternation-bound.md)
Board: [2026-10-31 message](../../board/301/page-040.md?plain=1#L292) · [2026-10-30 message](../../board/301/page-043.md?plain=1#L425)
Source manifests: [soring-fronts_adversary-game-alternation-bound](../../workspaces/manifests/soring-fronts_adversary-game-alternation-bound.json)

## adversary-alternation-logn-blocks

For the minimax game underlying S(n) (unary SORT-BOUND-U), is there an all-n strategy-compression into O(log n) alternation blocks that preserves the exact value S(n) and admits a polynomial-size (in input length N) witness/checker, or must every exact strategy require omega(log N) alternation depth?

**investigated** · [Full research report](../../fronts/0069-adversary-alternation-logn-blocks.md)
Board: [2026-10-30 message](../../board/301/page-042.md?plain=1#L500) · [2026-10-30 message](../../board/301/page-042.md?plain=1#L508) · [2026-10-30 message](../../board/301/page-042.md?plain=1#L516) · [2026-10-30 message](../../board/301/page-042.md?plain=1#L524) · [2026-10-30 message](../../board/301/page-043.md?plain=1#L425) (8 total; use search for all)
Source manifests: [soring-fronts_adversary-alternation-logn-blocks](../../workspaces/manifests/soring-fronts_adversary-alternation-logn-blocks.json)

## downward-self-reducibility-sparse

Is SORT-BOUND-U downward self-reducible in a way compatible with polynomial-time reductions (or is every natural downward self-reduction blocked), and would such downward self-reducibility together with sparsity force consequences different from general sparse languages for this structured poset problem?

**investigated** · [Full research report](../../fronts/0070-downward-self-reducibility-sparse.md)
Historical reported excerpt: **Finding (mathematical):** No explicit polynomial-time downward self-reduction (DSR) from $SORT\!-\!BOUND\!-\!U = \{1^n\#1^k : S(n)\le k\}$ to strictly smaller instances of the same language is known, and the natural routes appear blocked.
Board: [2026-10-30 message](../../board/301/page-043.md?plain=1#L425)
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_downward-self-reducibility-sparse](../../workspaces/manifests/soring-fronts_downward-self-reducibility-sparse.json)

## comparison-test-np-hardness-antichain

Is computing S(n) (or deciding SORT-BOUND-U) NP-hard under the restriction to comparison tests only, for the antichain/root instance family S_n, or does the fixed comparison test set avoid Hyafil-Rivest/Laber-Nogueira transfers and place it below NP despite arbitrary-test NP-hardness?

**investigated** · [Full research report](../../fronts/0072-comparison-test-np-hardness-antichain.md)
Historical reported excerpt: **Finding:** No polynomial-time many-one reduction from NP-complete problems to `SORT-BOUND-U` is known, and there is a concrete obstruction tied to the fixed pairwise-comparison test set (plus the unary sparsity barrier). The Hyafil–Rivest/Laber–Nogueira results do **not** transfer.
Source manifests: [soring-fronts_comparison-test-np-hardness-antichain](../../workspaces/manifests/soring-fronts_comparison-test-np-hardness-antichain.json)

## bounded-alternation-sortbound

For SORT-BOUND-U modeled as the bounded-depth alternating game G(n,k), is there a fixed constant d&gt;=1 with SORT-BOUND-U in Σ_d^P union Π_d^P for the relevant encodings, or does the antichain-root game require unbounded alternation depth under any polynomial-time reduction?

**investigated** · [Full research report](../../fronts/0079-bounded-alternation-sortbound.md)
Board: [2026-10-30 message](../../board/301/page-041.md?plain=1#L27) · [2026-10-30 message](../../board/301/page-041.md?plain=1#L123) · [2026-10-30 message](../../board/301/page-042.md?plain=1#L508) · [2026-10-30 message](../../board/301/page-042.md?plain=1#L516) · [2026-10-30 message](../../board/301/page-042.md?plain=1#L524)
Source manifests: [soring-fronts_bounded-alternation-sortbound](../../workspaces/manifests/soring-fronts_bounded-alternation-sortbound.json)

## fixed-block-alternation-obstruction

For all sufficiently large n and k = S(n) + O(1), does every winning strategy for the sorter in game G(n,k) require Omega(log n) alternation blocks between sorter/adversary moves, or can a constant number of blocks suffice?

**blocked** · [Full research report](../../fronts/0084-fixed-block-alternation-obstruction.md)
Board: [2026-10-31 message](../../board/301/page-040.md?plain=1#L187) · [2026-10-30 message](../../board/301/page-041.md?plain=1#L229) · [2026-10-31 message](../../board/301/page-041.md?plain=1#L301) · [2026-10-31 message](../../board/301/page-041.md?plain=1#L317) · [2026-10-31 message](../../board/301/page-041.md?plain=1#L333) (18 total; use search for all)
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_fixed-block-alternation-obstruction](../../workspaces/manifests/soring-fronts_fixed-block-alternation-obstruction.json)

## unary-alternation-depth-lower-bound

For all sufficiently large n, must every alternating Turing machine deciding SORT-BOUND-U on inputs encoding (n,k) with k near S(n) use Omega(S(n)) alternation rounds in the worst case over all sorter/adversary lines, ruling out any simulation that compresses the O(n log n) natural game alternations by more than a constant factor?

**investigated** · [Full research report](../../fronts/0097-unary-alternation-depth-lower-bound.md)
Source manifests: [soring-fronts_unary-alternation-depth-lower-bound](../../workspaces/manifests/soring-fronts_unary-alternation-depth-lower-bound.json)

## alternation-depth-vs-blocks-separation

For the interleaved sorter/adversary game achieving S(n), does the alternation depth in standard quantifier blocks equal Theta(S(n)) for all large n, and can this be separated from any constant-block reformulation without increasing the number of moves or losing exactness?

**investigated** · [Full research report](../../fronts/0100-alternation-depth-vs-blocks-separation.md)
Historical reported excerpt: **Conclusion:** I cannot construct a concrete disproof (e.g. a proof that bounded blocks cannot simulate). The separation depends on polynomial strategy compressibility (NP membership), which is open with known obstructions but no settled all-$n$ obstruction theorem. No Lean/repo changes warranted;…
Source manifests: [soring-fronts_alternation-depth-vs-blocks-separation](../../workspaces/manifests/soring-fronts_alternation-depth-vs-blocks-separation.json)

## comparison-test-restriction-hardness

For the minimum-height comparison decision tree (only pairwise comparisons, adversarial outcomes forming a total order), is the exact construction NP-hard for the antichain root S(n), or does the pairwise-test restriction strictly separate it from the arbitrary-test case where Hyafil–Rivest shows NP-completeness?

**investigated** · [Full research report](../../fronts/0101-comparison-test-restriction-hardness.md)
Board: [2026-10-31 message](../../board/301/page-040.md?plain=1#L376) · [2026-10-31 message](../../board/301/page-040.md?plain=1#L384) · [2026-10-31 message](../../board/301/page-040.md?plain=1#L392) · [2026-10-31 message](../../board/301/page-040.md?plain=1#L400) · [2026-10-31 message](../../board/301/page-040.md?plain=1#L408) (24 total; use search for all)
Source manifests: [soring-fronts_comparison-test-restriction-hardness](../../workspaces/manifests/soring-fronts_comparison-test-restriction-hardness.json)

## fo-lfp-p-membership

Can SORT-BOUND-U be defined by a fixed-point logic formula (FO(LFP)) on ordered structures with polynomial-time data complexity, giving a new P-membership route distinct from explicit algorithmic recurrences?

**investigated** · [Full research report](../../fronts/0103-fo-lfp-p-membership.md)
Board: [2026-10-31 message](../../board/301/page-040.md?plain=1#L236) · [2026-10-31 message](../../board/301/page-040.md?plain=1#L244)
Source manifests: [soring-fronts_fo-lfp-p-membership](../../workspaces/manifests/soring-fronts_fo-lfp-p-membership.json)

## algebraic-invariants-sortbound-20261101

Can algebraic invariants of the weak order/permutohedron (e.g. Coxeter length classes, descent sets, or the "graph of linear extensions") yield a uniform polynomial-time certificate or a new all-n obstruction for exact S(n)? Focus on whether any known algebraic invariant is invariant under optimal comparison strategy branching or can rule out compression of winning states across all n.

**investigated** · [Full research report](../../fronts/0120-algebraic-invariants-sortbound-20261101.md)
Board: [2026-10-31 message](../../board/301/page-038.md?plain=1#L11) · [2026-11-01 message](../../board/301/page-038.md?plain=1#L123) · [2026-10-31 message](../../board/301/page-039.md?plain=1#L381) · [2026-10-31 message](../../board/301/page-039.md?plain=1#L389) · [2026-10-31 message](../../board/301/page-039.md?plain=1#L397)
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_algebraic-invariants-sortbound-20261101](../../workspaces/manifests/soring-fronts_algebraic-invariants-sortbound-20261101.json)

## fo-lfp-vs-sortbound-20261101

Does the uniform SORT-BOUND-U threshold admit an FO(LFP) (polynomial-time) definition on ordered structures, and if not what is the exact obstruction relative to known PSPACE bound? Distinguish descriptive complexity classes carefully against unary/binary encodings and against the special antichain case.

**investigated** · [Full research report](../../fronts/0122-fo-lfp-vs-sortbound-20261101.md)
Historical reported excerpt: **Mathematical finding (descriptive complexity / complexity of exact unary S(n)):**
Board: [2026-11-01 message](../../board/301/page-038.md?plain=1#L211) · [2026-11-01 message](../../board/301/page-038.md?plain=1#L219) · [2026-11-01 message](../../board/301/page-038.md?plain=1#L227) · [2026-11-01 message](../../board/301/page-038.md?plain=1#L235) · [2026-11-01 message](../../board/301/page-038.md?plain=1#L243) (10 total; use search for all)
Source manifests: [soring-fronts_fo-lfp-vs-sortbound-20261101](../../workspaces/manifests/soring-fronts_fo-lfp-vs-sortbound-20261101.json)

## folfp-explicit-sortbound

Can an explicit FO(LFP) formula over ordered finite structures define SORT-BOUND-U = {1^n # 1^k : S(n) &lt;= k} without encoding an exponential comparison tree?

**investigated** · [Full research report](../../fronts/0123-folfp-explicit-sortbound.md)
Board: [2026-11-01 message](../../board/301/page-038.md?plain=1#L363) · [2026-11-01 message](../../board/301/page-038.md?plain=1#L371) · [2026-11-01 message](../../board/301/page-038.md?plain=1#L379) · [2026-11-01 message](../../board/301/page-038.md?plain=1#L387) · [2026-11-01 message](../../board/301/page-038.md?plain=1#L395) (9 total; use search for all)
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_folfp-explicit-sortbound](../../workspaces/manifests/soring-fronts_folfp-explicit-sortbound.json)

## fo-lfp-exact-definition-sortbound

Is SORT-BOUND-U definable by an FO(LFP) formula (polynomial time, by Immerman–Vardi / Grädel) on the ordered structure encoding (1^n#1^k), given the known PSPACE/ATM characterization? If not directly obvious, find which precise game/recurrence is FO(LFP)-definable versus requiring PFP, and does a correct FO(LFP) definition yield a constructive polynomial-time evaluation method for the decision problem?

**investigated** · [Full research report](../../fronts/0134-fo-lfp-exact-definition-sortbound.md)
Board: [2026-11-01 message](../../board/301/page-035.md?plain=1#L219) · [2026-11-01 message](../../board/301/page-035.md?plain=1#L227) · [2026-11-01 message](../../board/301/page-035.md?plain=1#L291)
Source manifests: [soring-fronts_fo-lfp-exact-definition-sortbound](../../workspaces/manifests/soring-fronts_fo-lfp-exact-definition-sortbound.json)

## randomized-exact-sortbound

Can a uniform randomized algorithm compute S(n) exactly in time 2^(o(n log^2 n)) for all sufficiently large n, or is exact randomized evaluation subject to the same adversarial-state obstacles as deterministic search?

**investigated** · [Full research report](../../fronts/0138-randomized-exact-sortbound.md)
Source manifests: [soring-fronts_randomized-exact-sortbound](../../workspaces/manifests/soring-fronts_randomized-exact-sortbound.json)

## adversarial-width-sortbound

Is the pathwidth or the adversarial antichain width of the minimax game tree on n elements unbounded as Omega(n / log n) in the worst case over all optimal strategies, and does this force alternation of that depth?

**investigated** · [Full research report](../../fronts/0139-adversarial-width-sortbound.md)
Historical reported excerpt: **Finding (disproof): the premise is false by tree structure.**
Source manifests: [soring-fronts_adversarial-width-sortbound](../../workspaces/manifests/soring-fronts_adversarial-width-sortbound.json)

## antichain-fo-lfp-definability

Is SORT-BOUND-U definable in FO(LFP) on ordered structures representing the comparison game, or does the alternating minimax quantification over all incomparable pairs at each step create a strict alternation obstruction below PSPACE?

**investigated** · [Full research report](../../fronts/0143-antichain-fo-lfp-definability.md)
Board: [2026-11-01 message](../../board/301/page-034.md?plain=1#L195)
Mixed-session reports: [e70582fbe904](../../followup/mixed-reports/objects/e70582fbe904334939e0e6f13c1298e6b6594eca5a3366efd5a8cab628e9326d.txt)
Source manifests: [soring-fronts_antichain-fo-lfp-definability](../../workspaces/manifests/soring-fronts_antichain-fo-lfp-definability.json)

## comparison-restriction-hardness

For pairwise comparison tests (a restricted subclass of all possible tests), is the minimum-height decision tree problem NP-hard for the sorting function class, or does the total-order constraint make computing S(n) polynomial-time equivalent to easier problems despite arbitrary-test NP-hardness?

**investigated** · [Full research report](../../fronts/0147-comparison-restriction-hardness.md)
Historical reported excerpt: **Conclusion (honest):**
Source manifests: [soring-fronts_comparison-restriction-hardness](../../workspaces/manifests/soring-fronts_comparison-restriction-hardness.json)

## fo-lfp-explicit-formula-sorting-bound

Construct and validate an explicit FO(PFP) formula defining SORT-BOUND-U on ordered structures from the capture theorem, and determine whether an FO(LFP) or ESO formula is achievable for the unary language.

**investigated** · [Full research report](../../fronts/0153-fo-lfp-explicit-formula-sorting-bound.md)
Historical reported excerpt: **Mathematical finding (descriptive complexity):**
Source manifests: [soring-fronts_fo-lfp-explicit-formula-sorting-bound](../../workspaces/manifests/soring-fronts_fo-lfp-explicit-formula-sorting-bound.json)

## readonce-branching-program-sortbound

Is SORT-BOUND-U computable by polynomial-size uniform read-once branching programs (ROBP) over the unary input representation, and can the comparison-adversary structure of the antichain give an all-n exponential ROBP lower bound or a polynomial upper bound?

**investigated** · [Full research report](../../fronts/0166-readonce-branching-program-sortbound.md)
Source manifests: [soring-fronts_readonce-branching-program-sortbound](../../workspaces/manifests/soring-fronts_readonce-branching-program-sortbound.json)

## ordered-bp-polysize-unary-sortbound

Is SORT-BOUND-U decidable by polynomial-size uniform ordered branching programs (OBPs) under the canonical left-to-right unary encoding, for all n&gt;=1?

**investigated** · [Full research report](../../fronts/0167-ordered-bp-polysize-unary-sortbound.md)
Historical reported excerpt: **Finding (mathematical):** The question is genuinely open under standard complexity-theoretic interpretation of "ordered/oblivious branching programs" (fixed variable-access order, designer chooses best order) over the unary input 1^n # 1^k.
Source manifests: [soring-fronts_ordered-bp-polysize-unary-sortbound](../../workspaces/manifests/soring-fronts_ordered-bp-polysize-unary-sortbound.json)

## eso-descriptive-sortbound

For all n&gt;=1 with unary encoding of (n,k), does there exist an existential second-order sentence over finite ordered structures that is true iff S(n)&lt;=k and has size polynomial in (n+k), or is there an all-n inexpressibility obstruction forcing super-polynomial sentence size for any ESO definition of SORT-BOUND-U?

**blocked** · [Full research report](../../fronts/0174-eso-descriptive-sortbound.md)
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_eso-descriptive-sortbound](../../workspaces/manifests/soring-fronts_eso-descriptive-sortbound.json)

## uniform-ac0-tally-barrier

Is SORT-BOUND-U in DLOGTIME-uniform AC^0, or does the all-n nonperiodic growth of S(n) force every DLOGTIME-uniform constant-depth circuit family for its unary threshold to have super-polynomial size given the cutoff t_L depends on inverting S(n)?

**investigated** · [Full research report](../../fronts/0185-uniform-ac0-tally-barrier.md)
Historical reported excerpt: **FINDING (deduction):** SORT-BOUND-U ∉ DLOGTIME-uniform AC^0.
Source manifests: [soring-fronts_uniform-ac0-tally-barrier](../../workspaces/manifests/soring-fronts_uniform-ac0-tally-barrier.json)

## sparse-turing-np-hardness-collapse

Does polynomial-time Turing (Cook) reducibility of NP-complete languages to SORT-BOUND-U, despite its sparsity, force a collapse of the polynomial hierarchy beyond P=NP, and is such Turing-hardness compatible with known Mahaney obstructions?

**investigated** · [Full research report](../../fronts/0193-sparse-turing-np-hardness-collapse.md)
Board: [2026-11-02 message](../../board/301/page-032.md?plain=1#L347) · [2026-11-02 message](../../board/301/page-032.md?plain=1#L355)
Source manifests: [soring-fronts_sparse-turing-np-hardness-collapse](../../workspaces/manifests/soring-fronts_sparse-turing-np-hardness-collapse.json)

## antichain-fo-pfp-gap

Can the ATM alternation proof placing SORT-BOUND-U in PSPACE be translated into an explicit FO(PFP) formula on finite ordered structures for the antichain game, and does that translation create any uniform-size blowup that would obstruct effective reduction arguments?

**investigated** · [Full research report](../../fronts/0196-antichain-fo-pfp-gap.md)
Board: [2026-11-02 message](../../board/301/page-031.md?plain=1#L75) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L83) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L91) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L99) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L107) (12 total; use search for all)
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_antichain-fo-pfp-gap](../../workspaces/manifests/soring-fronts_antichain-fo-pfp-gap.json)

## fo-pfp-explicit-formula

Give an explicit FO(PFP) formula (on ordered structures encoding the poset/unary input) defining SORT-BOUND-U exactly, with a correctness argument mapping the alternation game to PFP and a complexity/size sketch; test on small n/k and show it does not collapse to FO(LFP).

**investigated** · [Full research report](../../fronts/0218-fo-pfp-explicit-formula.md)
Board: [2026-11-01 message](../../board/301/page-036.md?plain=1#L35) · [2026-11-01 message](../../board/301/page-036.md?plain=1#L51) · [2026-11-01 message](../../board/301/page-037.md?plain=1#L319) · [2026-11-01 message](../../board/301/page-037.md?plain=1#L343) · [2026-11-01 message](../../board/301/page-037.md?plain=1#L415) (9 total; use search for all)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e10956d47ffeMcCfEn7CJY7TWb](../../assistant-reports/sessions/ses_e10956d47ffeMcCfEn7CJY7TWb.md)
Original task commissions: [83b1d74913d7](../../followup/task-commissions/objects/83b1d74913d7edb7d2ee7ed491b6e188c0ebf4c6606edcd551d0467942d1b928.txt)
Mixed-session reports: [7337ad8fde3a](../../followup/mixed-reports/objects/7337ad8fde3ad2e2976de82c68af7c0d98afbebeffcec3135ed94b0cc8bdc9d6.txt)
Source manifests: [soring-fronts_fo-pfp-explicit-formula-20261101](../../workspaces/manifests/soring-fronts_fo-pfp-explicit-formula-20261101.json) · [soring-fronts_fo-pfp-explicit-formula-20261118exec](../../workspaces/manifests/soring-fronts_fo-pfp-explicit-formula-20261118exec.json) · [soring-fronts_fo-pfp-explicit-formula](../../workspaces/manifests/soring-fronts_fo-pfp-explicit-formula.json)

## alternation-depth-sorting-game

Model SORT-BOUND-U as an alternating game of depth exactly k with O(n^2) possible moves per round and quantify the alternation complexity: is the minimal alternation depth polynomial in input length for the unary threshold or is it linear in k?

**investigated** · [Full research report](../../fronts/0229-alternation-depth-sorting-game.md)
Historical reported excerpt: **Finding (deduction, game-theoretic):** Modeling SORT-BOUND-U as G(n,k) (sorter ∃ picks pair, adversary ∀ gives direction consistent with some linear extension, alternating, adversary must remain globally consistent), alternation depth cannot be collapsed below k because sorter moves must be adapt…
Source manifests: [soring-fronts_alternation-depth-sorting-game](../../workspaces/manifests/soring-fronts_alternation-depth-sorting-game.json)

## descriptive-folfp-sorting-bound

For all n,k, does there exist a fixed FO(LFP) sentence phi such that (N_n,k, &lt;) \|= phi iff S(n) &lt;= k, where N_n,k encodes 1^n # 1^k as an ordered structure (size Theta(n+k))? Equivalently, is SORT-BOUND-U in Datalog with least fixed point (P by Immerman–Vardi) via an explicit uniform formula over the game/poset states?

**investigated** · [Full research report](../../fronts/0239-descriptive-folfp-sorting-bound.md)
Historical reported excerpt: ## Conclusion
Source manifests: [soring-fronts_descriptive-folfp-sorting-bound](../../workspaces/manifests/soring-fronts_descriptive-folfp-sorting-bound.json)

## linear-extension-count-hardness-block

Show for all sufficiently large n that no polynomial-time (in n) uniform procedure can decide exact-reset feasibility from (P,Q) alone without simulating comparisons, because deciding partitionability by comparison splits reduces to counting linear extensions #P-hard instances embedded in reachable sorting posets.

**investigated** · [Full research report](../../fronts/0251-linear-extension-count-hardness-block.md)
Source manifests: [soring-fronts_linear-extension-count-hardness-block](../../workspaces/manifests/soring-fronts_linear-extension-count-hardness-block.json)

## atm-alternation-depth-bound

For the alternating Turing machine deciding SORT-BOUND-U via the minimax game G(n,k), is the polynomial alternation depth O(k)=O(n log n) necessary for all-n instances, or can a uniform ATM decide it with alternation depth O(log^c (n+k)) for some fixed c (bounded or polylog alternation)?

**blocked** · [Full research report](../../fronts/0291-atm-alternation-depth-bound.md)
Board: [2026-11-18 message](../../board/301/page-014.md?plain=1#L1161)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e105decefffezblM42p51WP44R](../../assistant-reports/sessions/ses_e105decefffezblM42p51WP44R.md)
Original task commissions: [eb66b7109658](../../followup/task-commissions/objects/eb66b7109658eae3bf12d8598d4c669e6c99ce5e1e732773095437a0701680a0.txt)
Mixed-session reports: [27ee65221e7e](../../followup/mixed-reports/objects/27ee65221e7eb263042318d26dd734e81aa31e632b8a1797488a03cfc0b5c518.txt) · [3f4f3b35bd60](../../followup/mixed-reports/objects/3f4f3b35bd60c6ae609978b0defad0175656dba30d24fc1d535e45018c3c99e6.txt)
Source manifests: [soring-fronts_atm-alternation-depth-bound](../../workspaces/manifests/soring-fronts_atm-alternation-depth-bound.json)

## turing-np-hardness-sparse

Is the unary threshold language SORT-BOUND-U NP-hard under polynomial-time Turing reductions, or can this be ruled out without collapsing P to NP?

**investigated** · [Full research report](../../fronts/0292-turing-np-hardness-sparse.md)
Source manifests: [soring-fronts_turing-np-hardness-sparse](../../workspaces/manifests/soring-fronts_turing-np-hardness-sparse.json)

## adaptive-tree-verification-hardness

For a succinctly described adaptive comparison tree (or framed DAG) that claims to sort n elements within k comparisons, is the validity+height verification problem complete for coNP or harder under the unary input encoding?

**investigated** · [Full research report](../../fronts/0294-adaptive-tree-verification-hardness.md)
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_adaptive-tree-verification-hardness](../../workspaces/manifests/soring-fronts_adaptive-tree-verification-hardness.json)

## winning-frontier-enumeration-hardness

For all sufficiently large n of the form n=2^(2r), does the exponential family of nonisomorphic winning states at fixed relative depth (the independent-edge/chain construction giving &gt;= 2^((1/4-o(1)) n (log n)^2) states) force any uniform DP algorithm that tracks all reachable winning classes by exact isomorphism to run in time &gt;= 2^((1/8-o(1)) n (log n)^2) on input 1^n, even if it does not enumerate a single-policy tree?

**investigated** · [Full research report](../../fronts/0300-winning-frontier-enumeration-hardness.md)
Source manifests: [soring-fronts_winning-frontier-enumeration-hardness](../../workspaces/manifests/soring-fronts_winning-frontier-enumeration-hardness.json)

## qbf-alternation-tightness

For the budgeted alternating/positional game characterizing SORT-BOUND-U, is the minimal all-n alternation depth Ω(n) or can it be shown O(n / polylog n) for some uniform ATM recognizing SORT-BOUND-U on unary input?

**investigated** · [Full research report](../../fronts/0306-qbf-alternation-tightness.md)
Historical reported excerpt: ## Mathematical finding / precise obstacle (honest limit)
Source manifests: [soring-fronts_qbf-alternation-tightness](../../workspaces/manifests/soring-fronts_qbf-alternation-tightness.json)

## factorial-extension-hardness-forcing

For every n &gt;= 12, must every finite poset P with e(P) = n! satisfy m(P) &gt;= S(n), or does some n admit a poset with n! linear extensions that is sortable in just ceil(log2(n!)) comparisons?

**investigated** · [Full research report](../../fronts/0333-factorial-extension-hardness-forcing.md)
Assistant reports: [ses_e4759458cffeCX3iqCfCZfW5Wi](../../assistant-reports/sessions/ses_e4759458cffeCX3iqCfCZfW5Wi.md) · [ses_e4758c007ffePpZdz6o8fJHnxG](../../assistant-reports/sessions/ses_e4758c007ffePpZdz6o8fJHnxG.md) · [ses_e47383d75ffeCJkOYm9BSMS058](../../assistant-reports/sessions/ses_e47383d75ffeCJkOYm9BSMS058.md)
Original task commissions: [8b1ea5ccf4a4](../../followup/task-commissions/objects/8b1ea5ccf4a444f47ab788f6089e0e3ea64c0a7ad5831e48bb10e0037248e1f5.txt) · [8b6eded51fcf](../../followup/task-commissions/objects/8b6eded51fcf49e21efa04dbcefc3a7dc1d64db87645de34a39483d6056eee18.txt) · [e284d19cd0e3](../../followup/task-commissions/objects/e284d19cd0e315af9127a7489d9241f0b1f28b120ff200ba9c6772f81dcf8c8e.txt)
Source manifests: [soring-fronts_factorial-extension-hardness-forcing](../../workspaces/manifests/soring-fronts_factorial-extension-hardness-forcing.json)

## shallow-state-fibonacci-hardness

Is the Fibonacci threshold predicate e(P) &lt;= T(b) still PP-hard under Las Vegas reductions when P is restricted to n-element posets lying at distance at most S(n) from the n-antichain, that is, the states actually reachable inside an exact unary evaluator?

**investigated** · [Full research report](../../fronts/0334-shallow-state-fibonacci-hardness.md)
Board: [2026-11-08 message](../../board/301/page-022.md?plain=1#L53)
Assistant reports: [ses_e47594105ffe8uRkSNvFMhap5B](../../assistant-reports/sessions/ses_e47594105ffe8uRkSNvFMhap5B.md) · [ses_e4758bca2ffeWZC1XVF6lgs01K](../../assistant-reports/sessions/ses_e4758bca2ffeWZC1XVF6lgs01K.md) · [ses_e47383ba8ffePddQX4d5lP8kjH](../../assistant-reports/sessions/ses_e47383ba8ffePddQX4d5lP8kjH.md)
Original task commissions: [23ae7b136128](../../followup/task-commissions/objects/23ae7b1361288ed8f248538b9fea9def897ef251559eec38dc08b90851683389.txt) · [3a418a1cb5d8](../../followup/task-commissions/objects/3a418a1cb5d8dbed75345472acf461ee97a8554c5cc68f426f4b0394f8c029cf.txt) · [a150b1d761a5](../../followup/task-commissions/objects/a150b1d761a5d08b81029e24f0d9658911b8c1848ce26dc7182438d4d843736f.txt)
Source manifests: [soring-fronts_shallow-state-fibonacci-hardness](../../workspaces/manifests/soring-fronts_shallow-state-fibonacci-hardness.json)

## sparse-hasse-extension-hardness

Is counting linear extensions #P-hard under Turing reductions for n-element posets whose Hasse diagram has at most C n log n cover relations, for some absolute constant C?

**investigated** · [Full research report](../../fronts/0344-sparse-hasse-extension-hardness.md)
Assistant reports: [ses_e46747f44ffeTbjs5WpgB9iZoA](../../assistant-reports/sessions/ses_e46747f44ffeTbjs5WpgB9iZoA.md) · [ses_e46736c09ffelmX1W6Qyurj4hb](../../assistant-reports/sessions/ses_e46736c09ffelmX1W6Qyurj4hb.md)
Original task commissions: [004c759b7dab](../../followup/task-commissions/objects/004c759b7dabe2c3addd5a87e6e613790aefc88ce59e0bd4ef8b7818e1e4439f.txt) · [31a499bcdc31](../../followup/task-commissions/objects/31a499bcdc31b6d0f2ba88f260c609f864660c57172ce68371aac49e9a910340.txt) · [b73e56a7164b](../../followup/task-commissions/objects/b73e56a7164bc103023a6aedbefafe40055f1b08dc54c7584930c9b8589ccaff.txt)
Source manifests: [soring-fronts_sparse-hasse-extension-hardness](../../workspaces/manifests/soring-fronts_sparse-hasse-extension-hardness.json)

## pp-hardness-transfer-antichain

Does the PP-hardness of the general-poset Fibonacci extension-threshold predicate transfer to the antichain language SORT-BOUND-U under polynomial-time reductions, or is there a provable non-transfer barrier?

**investigated** · [Full research report](../../fronts/0349-pp-hardness-transfer-antichain.md)
Historical reported excerpt: **Conclusion:** no unfinished mathematical work and no repeated side effects. The only review item is the stale ledger entry, which the keeper should mark `investigated` on agent exit.
Board: [2026-11-08 message](../../board/301/page-022.md?plain=1#L239)
Assistant reports: [ses_e461ce7baffe9VKQF1wTaXue8Q](../../assistant-reports/sessions/ses_e461ce7baffe9VKQF1wTaXue8Q.md)
Original task commissions: [66b34c59a996](../../followup/task-commissions/objects/66b34c59a996e13503af292f6d558d3adb007b8c77cbb5eee38b9a1143d924e3.txt)
Source manifests: [soring-fronts_pp-hardness-transfer-antichain](../../workspaces/manifests/soring-fronts_pp-hardness-transfer-antichain.json)

## counting-oracle-sortbound-complexity

Is SORT-BOUND-U decidable in deterministic polynomial time with an oracle for exact linear-extension counts, that is, in P^{#P}, and can the minimax height be recovered from polynomially many extension-count queries?

**investigated** · [Full research report](../../fronts/0353-counting-oracle-sortbound-complexity.md)
Historical reported excerpt: ## Finding: a proved unbounded lookahead-depth barrier for extension-count recovery
Board: [2026-11-08 message](../../board/301/page-022.md?plain=1#L358)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e45ac9b9cffevIzNrzH3W0V1y1](../../assistant-reports/sessions/ses_e45ac9b9cffevIzNrzH3W0V1y1.md)
Original task commissions: [966bdb037baf](../../followup/task-commissions/objects/966bdb037baf382b38e66992036496074e8edc1bc11f8c54a2194e8bb2234df4.txt)
Mixed-session reports: [87b5610cc743](../../followup/mixed-reports/objects/87b5610cc74393549864d862ab283c7e5bd3cb2983ddfed92110f5f7702ae245.txt)
Source manifests: [soring-fronts_counting-oracle-sortbound-complexity](../../workspaces/manifests/soring-fronts_counting-oracle-sortbound-complexity.json)

## constant-round-am-sortbound

Does SORT-BOUND-U admit a public-coin interactive proof with O(1) rounds and a polynomial-time verifier (membership in AM), or does every constant-round protocol fail on infinitely many unary inputs because the minimax game's alternation cannot be compressed?

**investigated** · [Full research report](../../fronts/0359-constant-round-am-sortbound.md)
Assistant reports: [ses_e455e57adffe0LMs0N5vWPY8Y0](../../assistant-reports/sessions/ses_e455e57adffe0LMs0N5vWPY8Y0.md)
Original task commissions: [c91a793269b5](../../followup/task-commissions/objects/c91a793269b540671cce4ca650e5dc8f9f1898a45ffaea63ee1636b901ab5e4a.txt)
Source manifests: [soring-fronts_constant-round-am-sortbound](../../workspaces/manifests/soring-fronts_constant-round-am-sortbound.json)

## optimal-play-membership-polynomial

For every n and every comparison history H reachable from the n-element antichain, decide whether H can be extended to a height-S(n) optimal sorting strategy; determine whether this decision problem is solvable in polynomial time in n and \|H\|, or whether an infinite family of histories makes it intractable.

**investigated** · [Full research report](../../fronts/0517-optimal-play-membership-polynomial.md)
Historical reported excerpt: **Outcome: concrete failed approach / exact obstruction (honest limit)**
Assistant reports: [ses_e186c55e4ffe4WZNfTduuwal0H](../../assistant-reports/sessions/ses_e186c55e4ffe4WZNfTduuwal0H.md)
Original task commissions: [ba02597b1659](../../followup/task-commissions/objects/ba02597b1659311a7146b8f003c7058d233ebb80827c5e1afaacb0f849caebfd.txt)
Mixed-session reports: [13ac6bdf6288](../../followup/mixed-reports/objects/13ac6bdf62887b40c8dc4a8e3f26c8e60e6d2050af7b37753b3f528d4fff7e1e.txt)
Source manifests: [soring-fronts_optimal-play-membership-polynomial](../../workspaces/manifests/soring-fronts_optimal-play-membership-polynomial.json)

## sortboundu-bqp-membership

Is the tally threshold language SORT-BOUND-U = {1^n # 1^k : S(n) &lt;= k} decidable by a uniform bounded-error quantum polynomial-time algorithm on unary input length N = n+k+1, i.e. is SORT-BOUND-U in BQP (which is contained in PSPACE, so this is a genuine upper-bound target)? Equivalently, can the exact minimax AND-OR game of depth k = O(n log n) and branching O(n^2) be evaluated by a quantum algorithm in time 2^{o(n log^2 n)} for all n, improving the classical transcript-DFS exponent by more than a constant factor?

**investigated** · [Full research report](../../fronts/0538-sortboundu-bqp-membership.md)
Historical reported excerpt: **Conclusion: nothing unfinished, nothing to repeat.** I did not re-post, re-commit, or re-execute anything. The interrupted-prompt template does not correspond to any new effect to perform; continuing it blindly would only cause duplication.
Board: [2026-11-18 message](../../board/301/page-014.md?plain=1#L1810) · [2026-11-18 message](../../board/301/page-014.md?plain=1#L1846) · [2026-11-18 message](../../board/301/page-014.md?plain=1#L1868)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e1021d8acffe6NbSSITdxBBgTw](../../assistant-reports/sessions/ses_e1021d8acffe6NbSSITdxBBgTw.md)
Original task commissions: [d48e072da2be](../../followup/task-commissions/objects/d48e072da2be80d6141419490b08cd854f5d55890a50e352d9f196e931f3f962.txt)
Mixed-session reports: [6c8b7f9d65b6](../../followup/mixed-reports/objects/6c8b7f9d65b62c6aee1c52ddd6b78e891233c2c9854ed662d668b413c39cd953.txt) · [874486592e62](../../followup/mixed-reports/objects/874486592e625afd2039417bf4beddc9f16a58d4f9e54d9f9925254b1ab4a157.txt) · [cdcdb0172472](../../followup/mixed-reports/objects/cdcdb01724722d467823ac87d9e5bbe5cb0cc016a9102ea36503efa1d19761b1.txt) (4 total)
Source manifests: [soring-fronts_sortboundu-bqp-membership](../../workspaces/manifests/soring-fronts_sortboundu-bqp-membership.json)

## uniform-tc0-sortbound-membership

For all n, is the unary threshold language SORT-BOUND-U decidable by a DLOGTIME-uniform TC0 (or ACC0) circuit family, given that the information bound ceil(log2 n!) is itself in uniform TC0 and only the o(n) information excess separates it from the exact sorting number S(n)?

**investigated** · [Full research report](../../fronts/0567-uniform-tc0-sortbound-membership.md)
Board: [2026-11-19 message](../../board/301/page-011.md?plain=1#L867) · [2026-11-19 message](../../board/301/page-011.md?plain=1#L929)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e0b2ec4dbffeb1lFKot4P8ELvv](../../assistant-reports/sessions/ses_e0b2ec4dbffeb1lFKot4P8ELvv.md)
Original task commissions: [578d3177af0d](../../followup/task-commissions/objects/578d3177af0d5c206212dbafe2d3640300a712a29a3c953951a4ed4028817db3.txt)
Mixed-session reports: [a3bf5ea80429](../../followup/mixed-reports/objects/a3bf5ea80429ee5a3edd96b6ee592b73c68392000a9a44eee74737ef6722a34b.txt) · [e70582fbe904](../../followup/mixed-reports/objects/e70582fbe904334939e0e6f13c1298e6b6594eca5a3366efd5a8cab628e9326d.txt)
Source manifests: [soring-fronts_uniform-tc0-sortbound-membership](../../workspaces/manifests/soring-fronts_uniform-tc0-sortbound-membership.json)

## sorter-refuter-duality-np-conp

Is there an all-n duality between succinct sound-and-complete sorter certificates for SORT-BOUND-U and succinct adversary refuter certificates for its complement, or can NP-style certificate soundness and coNP-style refutation be decoupled for this sparse tally language?

**investigated** · [Full research report](../../fronts/0569-sorter-refuter-duality-np-conp.md)
Board: [2026-11-19 message](../../board/301/page-011.md?plain=1#L929)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e0b2ec0e3ffetJnnK5AZDuq7N1](../../assistant-reports/sessions/ses_e0b2ec0e3ffetJnnK5AZDuq7N1.md)
Original task commissions: [4f56653d77f6](../../followup/task-commissions/objects/4f56653d77f65c830eec286b0ed5b9b9475ef9e159c47e55bc02b934df3cc1b8.txt)
Mixed-session reports: [a3bf5ea80429](../../followup/mixed-reports/objects/a3bf5ea80429ee5a3edd96b6ee592b73c68392000a9a44eee74737ef6722a34b.txt)
Source manifests: [soring-fronts_sorter-refuter-duality-np-conp](../../workspaces/manifests/soring-fronts_sorter-refuter-duality-np-conp.json)

## verif-adv-conp-hardness-barrier

The newest #301 sorter-refuter report places adversary-soundness VERIFY-ADV (does a given memoryless adversary circuit force more than k comparisons at the n-antichain?) in coNP while sorter-soundness VERIFY-SORT is in P. Is VERIFY-ADV actually coNP-hard, hence coNP-complete, for the exact game G(n, S(n)-1) on all large n, so that checking a refuter's soundness cannot be done in polynomial time unless P = coNP?

**investigated** · [Full research report](../../fronts/0570-verif-adv-conp-hardness-barrier.md)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e0b0f2c83ffeokr1R3Bxg22crs](../../assistant-reports/sessions/ses_e0b0f2c83ffeokr1R3Bxg22crs.md)
Original task commissions: [185c34e53aac](../../followup/task-commissions/objects/185c34e53aac3f9352bb6271d5ac1b9e7a63f95776ecd1d0c39dd08a5c79bee4.txt)
Mixed-session reports: [6be94586c29b](../../followup/mixed-reports/objects/6be94586c29b8b7ef1143246666b7e5e21058e9135b3a75acc7cbbd67a239b6d.txt)
Source manifests: [soring-fronts_verif-adv-conp-hardness-barrier](../../workspaces/manifests/soring-fronts_verif-adv-conp-hardness-barrier.json)

## minimal-v-fotc-optimal-program-fragment

Is there a fixed small variable bound v (for example v=3 with arity at most 2) such that for every n there is a polynomial-size FO(TC)_v strategy program achieving the optimal budget S(n) under the fixed-interpreter uniform model, or does exact optimality force the required v or the transitive-closure context width to grow with n?

**investigated** · [Full research report](../../fronts/0587-minimal-v-fotc-optimal-program-fragment.md)
Historical reported excerpt: **Conclusion:** the previous turn’s external side effect (the #301 post) completed successfully. There is **no unfinished work** and I will **not** repeat the post, commit, or other actions.
Board: [2026-11-20 message](../../board/301/page-010.md?plain=1#L506) · [2026-11-20 review](../../board/301/page-010.md?plain=1#L549)
Assistant reports: [ses_e08f7f662ffepVWnEoNal3WAfp](../../assistant-reports/sessions/ses_e08f7f662ffepVWnEoNal3WAfp.md)
Original task commissions: [198e821a6824](../../followup/task-commissions/objects/198e821a6824b395cdcb30b9f09031a48e4a1730077362a548a86b7c9bff1b5c.txt)
Mixed-session reports: [6e2dc0d6efae](../../followup/mixed-reports/objects/6e2dc0d6efaeaf44f60f64a4b13ee0ee6fc17444899a7f5a3344c4630c3cf72f.txt) · [be5d419b64c3](../../followup/mixed-reports/objects/be5d419b64c3d6017ddb73e48a4ff44d0d32482cbb0405f1d462c4d66b905d54.txt) · [c5c6f154984c](../../followup/mixed-reports/objects/c5c6f154984c733350270fa1f76ac9e9c2bce14956697065ca8d810e1cd7b448.txt) (4 total)
Source manifests: [soring-fronts_minimal-v-fotc-optimal-program-fragment](../../workspaces/manifests/soring-fronts_minimal-v-fotc-optimal-program-fragment.json)

## greedy-evalue-closed-form-sparse-exception-alln

Does there exist, for every n, a polynomial-time computable closed form f together with a sparse exception set E_n of at most poly(n) extension counts such that the greedy value V(P) of every greedy-reachable state P whose linear-extension count e(P) is outside E_n equals f(e(P))?

**investigated** · [Full research report](../../fronts/0595-greedy-evalue-closed-form-sparse-exception-alln.md)
Historical reported excerpt: ## Mathematical finding — the falsifier is proved
Board: [2026-11-20 message](../../board/301/page-010.md?plain=1#L902) · [2026-11-20 review](../../board/301/page-010.md?plain=1#L946)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e0866cc96ffeE92i9hPiiW19ag](../../assistant-reports/sessions/ses_e0866cc96ffeE92i9hPiiW19ag.md)
Original task commissions: [16566e3ea2cd](../../followup/task-commissions/objects/16566e3ea2cdcc9457c82a817e852c85c85d2ecc5dde529a32027ca9079d2cd8.txt)
Mixed-session reports: [fad44d0341a9](../../followup/mixed-reports/objects/fad44d0341a9053b44a8c8f3e99cfdaa9b94c987387822c972c2e5fc5c93c9cf.txt)
Source manifests: [soring-fronts_greedy-evalue-closed-form-sparse-exception-alln](../../workspaces/manifests/soring-fronts_greedy-evalue-closed-form-sparse-exception-alln.json)

## alternation-trading-fixed-poly-sortbound

Can the alternation-trading method — simulating alternating computation by deterministic time with a fixed, smaller alternation budget — yield an unconditional fixed-polynomial lower bound SORT-BOUND-U not in DTIME(N^c) for some specific constant c&gt;1 on unary input length N=n+k+1, or does the tally/sparse form of the language together with the absence of any class-completeness handle make alternation trading inherently incapable of yielding information about this single fixed language?

**investigated** · [Full research report](../../fronts/0657-alternation-trading-fixed-poly-sortbound.md)
Board: [2026-11-21 message](../../board/301/page-005.md?plain=1#L594) · [2026-11-21 review](../../board/301/page-005.md?plain=1#L618)
Assistant reports: [ses_e0021b30fffemioBIyl33r4g9Y](../../assistant-reports/sessions/ses_e0021b30fffemioBIyl33r4g9Y.md)
Original task commissions: [412169bcd20d](../../followup/task-commissions/objects/412169bcd20d9980c6726b665a3f5d554580bc7165f058d4379b30e505aa3591.txt)
Mixed-session reports: [5877b6da8f89](../../followup/mixed-reports/objects/5877b6da8f896707b050bee31995a48fc78a8fad4afe13a858f0cec0f858c4e8.txt)
Source manifests: [soring-fronts_alternation-trading-fixed-poly-sortbound](../../workspaces/manifests/soring-fronts_alternation-trading-fixed-poly-sortbound.json)

## sortboundu-conp-membership-alln

Is SORT-BOUND-U in coNP: for every n and k, is there a polynomial-size (in n+k) certificate, verifiable in polynomial time, that S(n) &gt; k?

**investigated** · [Full research report](../../fronts/0666-sortboundu-conp-membership-alln.md)
Historical reported excerpt: **Finding:** `SORT-BOUND-U ∈ coNP` remains open. No uniform polynomial-time verifier for no-instance certificates and no infinite family of `n,k` with a proved superpolynomial certificate lower bound was found.
Board: [2026-11-22 message](../../board/301/page-004.md?plain=1#L161) · [2026-11-22 review](../../board/301/page-004.md?plain=1#L288)
Assistant reports: [ses_dff45380affeRsXP6EX9SKz5nP](../../assistant-reports/sessions/ses_dff45380affeRsXP6EX9SKz5nP.md)
Original task commissions: [ddfdd51d8de4](../../followup/task-commissions/objects/ddfdd51d8de49cfc53f13b5fda3c2901c557a6978a9d7334522a2fbfbc659680.txt)
Mixed-session reports: [0e90e5d75777](../../followup/mixed-reports/objects/0e90e5d757776eb713f88bd5d784b8efa47bd90f5f58897533177385f71bce58.txt) · [18de4807e457](../../followup/mixed-reports/objects/18de4807e457779e15da84cb1940d8b24105d34d2a5a8c9648c5d194d2772075.txt) · [19fa271e8664](../../followup/mixed-reports/objects/19fa271e86647cbd472049691eea9618d0d3296e08fd7552240fd14ac51a612d.txt)
Source manifests: [soring-fronts_sortboundu-conp-membership-alln](../../workspaces/manifests/soring-fronts_sortboundu-conp-membership-alln.json)

## min-forced-inversions-tally-equivalence-alln

For each n let nu(n) be the minimum, over all height-S(n) sorting strategies on the n-antichain, of the worst-case number of sibling-extension-inverted optimal comparisons along any adversary path. For all n, is nu(n)=0 exactly on the information-tight sizes S(n)=ceil(log2 n!), and is computing nu(n) polynomial-time Turing-equivalent to computing the exact sorting number S(n)?

**investigated** · [Full research report](../../fronts/0687-min-forced-inversions-tally-equivalence-alln.md)
Historical reported excerpt: ### Mathematical finding — the EVIDENCE's "deduction" has a real gap
Board: [2026-11-22 message](../../board/301/page-004.md?plain=1#L632) · [2026-11-22 review](../../board/301/page-004.md?plain=1#L966)
Assistant reports: [ses_dfe0ef630ffeZzHVUJSwJhgkON](../../assistant-reports/sessions/ses_dfe0ef630ffeZzHVUJSwJhgkON.md)
Original task commissions: [b267f39bcd03](../../followup/task-commissions/objects/b267f39bcd03e1c5171837b1f9cf302d34dbf6c1dfb337930c372db65c6dfcbb.txt)
Mixed-session reports: [d1bc3569bc51](../../followup/mixed-reports/objects/d1bc3569bc5183e8d11f89f88024cbc5b06d90bbfaaa4da76fc4e2bfd83d99bf.txt)
Source manifests: [soring-fronts_min-forced-inversions-tally-equivalence-alln](../../workspaces/manifests/soring-fronts_min-forced-inversions-tally-equivalence-alln.json)

## sparse-optimal-comparison-graph-alln

In the fixed adaptive pairwise-comparison model of docs/problem.md, let g(n) be the minimum number of distinct key-pairs that any height-S(n) correct sorting tree on n labelled keys may compare anywhere over its whole leaf set. Is there a fixed constant c with g(n) &lt;= c*n*log n for all n (so some optimal strategy uses a sparse comparison graph), or does every height-S(n) tree compare Omega(n^2) distinct pairs for infinitely many n?

**investigated** · [Full research report](../../fronts/0688-sparse-optimal-comparison-graph-alln.md)
Board: [2026-11-22 message](../../board/301/page-004.md?plain=1#L654) · [2026-11-22 review](../../board/301/page-004.md?plain=1#L824)
Assistant reports: [ses_dfde43096ffe7sQf1cdX2wyYFA](../../assistant-reports/sessions/ses_dfde43096ffe7sQf1cdX2wyYFA.md)
Original task commissions: [5d7670d336d5](../../followup/task-commissions/objects/5d7670d336d584c966f626661ecf4f48c69f432c77c9843525ea5a4c82f96cc3.txt)
Mixed-session reports: [a5440dbe635f](../../followup/mixed-reports/objects/a5440dbe635fad57a80b086c15a65fb8934d352aca104e2cecc80290ec52d2c6.txt)
Source manifests: [soring-fronts_sparse-optimal-comparison-graph-alln](../../workspaces/manifests/soring-fronts_sparse-optimal-comparison-graph-alln.json)

## fotc-optimal-strategy-poly-size-alln

For all integers n&gt;=2, does every height-S(n) optimal adaptive comparison tree admit a fixed-interpreter FO(TC) strategy program of polynomial text size in n and polynomial per-input interpreter runtime on all permutations, enabling poly-time verification of that strategy’s worst-case depth S(n)?

**investigated** · [Full research report](../../fronts/0713-fotc-optimal-strategy-poly-size-alln.md)
Historical reported excerpt: **Conclusion: the previous turn performed no external side effects.** Everything was reads plus a local computation; the mathematical report was already delivered in full at the end of that turn. Host is `billy-dev` (confirmed via `hostname`), so the original mandate's location requirement was sati…
Assistant reports: [ses_df7b297feffejpBNcbwCccaRr5](../../assistant-reports/sessions/ses_df7b297feffejpBNcbwCccaRr5.md)
Original task commissions: [5325ebe8b287](../../followup/task-commissions/objects/5325ebe8b287769eb7fbf85d22dd576062cf1bc7d74c4b5cbb52ec9be81e72f5.txt)
Mixed-session reports: [0af85eea565d](../../followup/mixed-reports/objects/0af85eea565d2f5ff94f2f5df157c17f2a739f762f809023f545efe6472981cb.txt) · [20c902ccbdc2](../../followup/mixed-reports/objects/20c902ccbdc2ec642c7845d6d7f1c8b98044039e13a4c3fe776f885fb8b6f91e.txt) · [3331f2d81006](../../followup/mixed-reports/objects/3331f2d81006dfe00cf1029c6b03d37f2ad3f0e16e91dc221383f4c82db902fa.txt)
Source manifests: [soring-fronts_fotc-optimal-strategy-poly-size-alln](../../workspaces/manifests/soring-fronts_fotc-optimal-strategy-poly-size-alln.json)

## constant-alternation-ph-placement-alln

SORT-BOUND-U is decided by the sorter-versus-adversary game G(n,k) using k=Theta(N) alternating rounds, which yields PSPACE via APTIME=PSPACE. Does SORT-BOUND-U belong to a fixed level of the polynomial hierarchy, i.e. can G(n,k) be replaced for all n by an equivalent decision procedure using only O(1) alternations, giving a Sigma_i^p or Pi_i^p characterization for some constant i?

**investigated** · [Full research report](../../fronts/0717-constant-alternation-ph-placement-alln.md)
Board: [2026-11-23 message](../../board/301/page-002.md?plain=1#L904) · [2026-11-23 review](../../board/301/page-002.md?plain=1#L932)
Assistant reports: [ses_df76f00adffeb23CHgui6eWGkB](../../assistant-reports/sessions/ses_df76f00adffeb23CHgui6eWGkB.md)
Original task commissions: [82ba0a0a90eb](../../followup/task-commissions/objects/82ba0a0a90eb12451180375d214fa36ea3b7976e7826dfa24f22237311fd3f99.txt)
Mixed-session reports: [38c12353588b](../../followup/mixed-reports/objects/38c12353588b763d25d40e4ac1d2507c6e76c68bee0a80494ab391ce6843938c.txt) · [beab146e2dea](../../followup/mixed-reports/objects/beab146e2dea39ea3ab2da0bd820fad309b7ebe220402ce09856e87356d993b3.txt)
Source manifests: [soring-fronts_constant-alternation-ph-placement-alln](../../workspaces/manifests/soring-fronts_constant-alternation-ph-placement-alln.json)

## excess-sequence-regularity-unary-p-alln

For every n let D(n)=S(n)-ceil(log2(n!)) be the unary sorting excess. Is D k-regular for some integer base k&gt;=2, or P-recursive, or p-automatic for some prime p, for all n -- i.e. does the excess sequence admit any fixed finite linear digit representation or any polynomial-length linear recurrence, given that the repository's newest non-k-regularity and non-holonomy paper proofs rule these out for S(n) and for the information bound ceil(log2(n!)) but provably do NOT apply to their difference D(n)?

**investigated** · [Full research report](../../fronts/0726-excess-sequence-regularity-unary-p-alln.md)
Historical reported excerpt: ## Mathematical finding
Board: [2026-11-23 message](../../board/301/page-001.md?plain=1#L284) · [2026-11-23 review](../../board/301/page-001.md?plain=1#L336)
Assistant reports: [ses_df6adc281ffekqNQyn4M1ugLLO](../../assistant-reports/sessions/ses_df6adc281ffekqNQyn4M1ugLLO.md)
Original task commissions: [2992d220469c](../../followup/task-commissions/objects/2992d220469cb9d1aecc1e23517aaccce31ad115cfefbfdcf3364844c6fec729.txt)
Mixed-session reports: [884bc06d62b1](../../followup/mixed-reports/objects/884bc06d62b1165cf537c515df8301d7fdd3f7508e952fea274f92fa6d31d9ad.txt) · [d36747cda152](../../followup/mixed-reports/objects/d36747cda1524827ff4683923f6bdff9633e7eb6ae9517b14aefcda08b3d379e.txt)
Source manifests: [soring-fronts_excess-sequence-regularity-unary-p-alln](../../workspaces/manifests/soring-fronts_excess-sequence-regularity-unary-p-alln.json)

## succinct-adversary-copnp-sortboundu-alln

Does SORT-BOUND-U admit a polynomial-size succinct adversary certificate certifying S(n)&gt;k at the n-antichain against every sorter, thereby giving coNP membership without enumerating the exponentially many winning frontier states?

**investigated** · [Full research report](../../fronts/0746-succinct-adversary-copnp-sortboundu-alln.md)
Historical reported excerpt: ## Result
Board: [2026-11-24 message](../../board/301/page-001.md?plain=1#L998)
Assistant reports: [ses_df38a0d0cffey2bvY1EdrQNZy0](../../assistant-reports/sessions/ses_df38a0d0cffey2bvY1EdrQNZy0.md)
Original task commissions: [c8c48e00b776](../../followup/task-commissions/objects/c8c48e00b7767f78ebfb6624a3fc3006f733aa3fc458aef8047cdade77dc32dd.txt)
Source manifests: [soring-fronts_succinct-adversary-copnp-sortboundu-alln](../../workspaces/manifests/soring-fronts_succinct-adversary-copnp-sortboundu-alln.json)
