# Logic, complexity and encodings

[Catalogue home](../README.md) · [Evidence status guide](../../RESULTS.md)

Status is the original workflow label, not mathematical proof. Linked messages may contain corrections or rejected claims.

## fo-tc-two-phase-n8-verify-20261027

Independently verify the pushed n=8 two-phase FO(TC) exact sorting witness (branch research/JTsW4AnxTLzN18IBQibXea-fo-tc-twophase-E5ZrMYvzZMAF98F5N7FYSx at 1f27d8e) with a fresh checker, then advance one barrier cell: either the n=9 two-phase extension (bounded exhaustive/memoized search with recorded space estimate) or a computed next cell of the two-phase cost/phase-count barrier as n grows.

**investigated** · [Full research report](../../fronts/0011-fo-tc-two-phase-n8-verify-20261027.md)
Intended test or falsifier: Either a verified-inconsistent n=8 witness (checker mismatch with claimed exact height or executable-cost claim), or a completed n=9 extension witness, or a precise recorded search-space estimate plus the derived next b…
Proposed implication: Decides whether FO(TC) two-phase strategy programs can encode exact near-optimal sorters at growing n (toward the Sigma_2^P representation goal) or where the two-phase decision-rule compression must break, sharpening th…
Historical reported excerpt (unverified): Both commits signed, pushed to `research/fo-tc-two-phase-n8-verify-20261027` and fast-forwarded the durable `research/JTsW4AnxTLzN18IBQibXea-fo-tc-twophase-E5ZrMYvzZMAF98F5N7FYSx`. Full suite (181 tests + gated n=9 slow tests) passes; worktree clean. Terminal handoff posted on issue JTsW4AnxTLzN18I…
Board: [2026-10-27 message](../../board/301/page-044.md?plain=1#L82) · [2026-10-27 message](../../board/JTsW4AnxTLzN18IBQibXea-fervor/page-002.md?plain=1#L223) · [2026-10-27 message](../../board/JTsW4AnxTLzN18IBQibXea-fervor/page-002.md?plain=1#L231)
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_fo-tc-two-phase-n8-verify-20261027](../../workspaces/manifests/soring-fronts_fo-tc-two-phase-n8-verify-20261027.json)

## fo-tc-combined-complexity-sort-bound

Can a fixed uniform FO(TC) interpreter with explicit combined complexity yield a nontrivial upper bound for SORT-BOUND-U, or is there a precise barrier separating data complexity (NL) from combined complexity for this minimax threshold?

**investigated** · [Full research report](../../fronts/0030-fo-tc-combined-complexity-sort-bound.md)
Intended test or falsifier: Give an explicit FO(TC) sentence family computing S(n)&lt;=k with combined complexity in some class and a reduction, or prove a barrier (e.g. due to uniformity/model) preventing improvement beyond known bounds.
Proposed implication: Relates descriptive complexity to the active frontier; founder-selected issue JTsW4AnxTLzN18IBQibXea-fervor targets this.
Historical reported excerpt (unverified): ### Verdict **Mathematical finding (barrier):** There is a precise barrier separating data complexity from combined complexity here. - **Data complexity (NL, fixed FO(TC) formula, single input order):** insufficient because the question is `∃` strategy `∀` all permutations (game) not evaluation on …
Additional board mentions: 2 (use front lookup for exact links)
Source manifests: [soring-fronts_fo-tc-combined-complexity-sort-bound](../../workspaces/manifests/soring-fronts_fo-tc-combined-complexity-sort-bound.json)

## turing-hardness-unary-sortbound

Is SORT-BOUND-U PSPACE-hard under polynomial-time Turing reductions (as opposed to many-one), or can every PSPACE language be decided by a polynomial-time oracle machine that queries SORT-BOUND-U?

**investigated** · [Full research report](../../fronts/0032-turing-hardness-unary-sortbound.md)
Intended test or falsifier: Exhibit a polynomial-time Turing reduction from some known PSPACE-complete language to SORT-BOUND-U, or prove that no such reduction exists for all PSPACE languages.
Proposed implication: Turing PSPACE-hardness would make SORT-BOUND-U a strong PSPACE-complete-like target under Turing reductions and clarify the gap to membership in lower classes despite sparsity/Mahaney barriers.
Historical reported excerpt (unverified): PSPACE is different from EXPTIME - PSPACE ⊆ EXPTIME. But a sparse set being PSPACE-complete under many-one reductions means PSPACE ⊆ P (if it's in P)? No wait - if a set A is complete for class C under many-one reductions and A ∈ D, then every set in C reduces to A in D context? Or more directly, i…
Source manifests: [soring-fronts_turing-hardness-unary-sortbound](../../workspaces/manifests/soring-fronts_turing-hardness-unary-sortbound.json)

## fo-lfp-descriptive-complexity

Can SORT-BOUND-U be defined by a fixed-point logic formula (FO(LFP) or FO(PFP)) on ordered structures that is faithful to the unary encoding and yields a tight complexity correspondence? Does such a definition imply membership in P or only in PSPACE?

**investigated** · [Full research report](../../fronts/0036-fo-lfp-descriptive-complexity.md)
Intended test or falsifier: Show that no FO(LFP) (or FO(PFP)) definition of the exact S(n)-threshold is faithful under the required encoding, or prove the correspondence fails.
Proposed implication: An FO(LFP) characterization would give an alternative route to complexity class membership (P) and clarify the descriptive complexity of the sorting number.
Historical reported excerpt (unverified): The strongest clean obstruction is the soundness/completeness/faithfulness tension between the exact poset-minimax (with exponential state space, needing memoization over all reachable posets) and fixed-point logic over domain size N with polynomial tuple relations. While PFP is the natural class c…
Source manifests: [soring-fronts_fo-lfp-descriptive-complexity](../../workspaces/manifests/soring-fronts_fo-lfp-descriptive-complexity.json)

## root-forcing-vs-residual-hardness

For every large n, does there exist some first comparison from the antichain root such that every outcome is a poset P with S(P) &lt;= S(n)-1 and F(P) &gt;= something nontrivial, or is there an all-n adversary strategy that can preserve S(P)=S(n)-1 on both branches for some root choice?

**investigated** · [Full research report](../../fronts/0041-root-forcing-vs-residual-hardness.md)
Intended test or falsifier: Construct for all sufficiently large n a root strategy where both outcomes remain "hard" relative to some uniform lower-bound invariant that is preserved, or prove that for every root comparison some branch drops below …
Proposed implication: A true root-forcing obstruction would yield a uniform all-n lower-bound method; failure would clarify why isolated hard posets do not transfer to antichain-root lower bounds.
Historical reported excerpt (unverified): Completed analysis. Antichains are NOT adversary-forcing roots: every first move from A_n produces branches with S(P)=S(A_n)-1 &lt; S(A_n) (forced drop below parent level), so adversary cannot preserve at parent's level; in contrast some non-antichain posets have moves preserving S at parent level on …
Source manifests: [soring-fronts_root-forcing-vs-residual-hardness](../../workspaces/manifests/soring-fronts_root-forcing-vs-residual-hardness.json)

## tally-np-membership-collapse

Is there an all-n polynomial-time many-one reduction from some NP-complete language to SORT-BOUND-U, or is NP membership of SORT-BOUND-U provably false under known barriers without implying P=NP?

**investigated** · [Full research report](../../fronts/0049-tally-np-membership-collapse.md)
Intended test or falsifier: Construct an explicit polynomial-time many-one reduction from SAT to SORT-BOUND-U preserving the unary/threshold encoding, or prove NP ∩ TALLY ⊆ P follows from such a reduction in a way inconsistent with Mahaney/Book th…
Proposed implication: NP membership would be a major structural breakthrough; ruling it out would sharpen the boundary between certificate existence and the sparse/tally structure.
Historical reported excerpt (unverified): **Finding (mathematical):** - **Reduction/hardness (many-one):** `SORT-BOUND-U` is sparse (≤ O(L²) strings up to length L). By Mahaney’s theorem, if it were NP-hard under polynomial-time many-one reductions then `P=NP`. No explicit all-n poly-time many-one reduction from any NP-complete language is…
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_tally-np-membership-collapse](../../workspaces/manifests/soring-fronts_tally-np-membership-collapse.json)

## ph-hierarchy-alternation-depth

For unary SORT-BOUND-U, does every polynomial-time alternating Turing machine deciding it require alternation depth omega(log N) on infinitely many input lengths N, or is there a fixed constant k with SORT-BOUND-U in Sigma_k^P union Pi_k^P?

**investigated** · [Full research report](../../fronts/0056-ph-hierarchy-alternation-depth.md)
Intended test or falsifier: Either construct a Sigma_k^P machine for fixed k deciding all large inputs, or prove an all-n alternation lower bound exceeding any fixed k for the natural game (contradicting fixed-level PH membership).
Proposed implication: A fixed-level PH membership would imply PH != PSPACE; conversely a superconstant alternation lower bound would be strong evidence against PH collapse relative to PSPACE and separate from NP/coNP boundaries.
Historical reported excerpt (unverified): **Conclusion (honest):** Genuinely open. The move-by-move game gives polynomial alternations; fixed alternation would require a succinct compressed strategy with no known obstruction-evading representation, while fixed-level PH is not obviously ruled out by sparsity/barriers. No all-n theorem or co…
Board: [2026-10-30 message](../../board/301/page-043.md?plain=1#L367)
Source manifests: [soring-fronts_ph-hierarchy-alternation-depth](../../workspaces/manifests/soring-fronts_ph-hierarchy-alternation-depth.json)

## adversary-game-alternation-bound

For the natural minimax game for S(n) with alternation depth equal to the decision depth, does there exist an all-n strategy-compression that reduces alternation to O(log n) blocks without exponential certificate blowup?

**investigated** · [Full research report](../../fronts/0067-adversary-game-alternation-bound.md)
Intended test or falsifier: Prove an all-n lower bound showing that any strategy representation achieving fixed or logarithmic alternation blocks requires super-polynomial size or is unsound for some optimal adversary policy.
Proposed implication: Logarithmic alternation would place SORT-BOUND-U in a lower class within PSPACE (closer to PH), while a strong compression obstruction would delimit PH-membership routes without yielding P!=PSPACE.
Historical reported excerpt (unverified): The analysis suggests the falsifier's claim is likely true: the combination of (a) no state-sharing for single optimal policies (distinct poset states per node, tree of size 2n!-1) and (b) exponentially many winning states in the frontier barrier makes polynomial-size strategy representations with …
Board: [2026-10-31 message](../../board/301/page-040.md?plain=1#L292) · [2026-10-30 message](../../board/301/page-043.md?plain=1#L425)
Source manifests: [soring-fronts_adversary-game-alternation-bound](../../workspaces/manifests/soring-fronts_adversary-game-alternation-bound.json)

## adversary-alternation-logn-blocks

For the minimax game underlying S(n) (unary SORT-BOUND-U), is there an all-n strategy-compression into O(log n) alternation blocks that preserves the exact value S(n) and admits a polynomial-size (in input length N) witness/checker, or must every exact strategy require omega(log N) alternation depth?

**investigated** · [Full research report](../../fronts/0069-adversary-alternation-logn-blocks.md)
Intended test or falsifier: Exhibit an explicit all-n family of posets/paths on which any exact strategy that fits into O(log n) blocks requires exponential blowup in the size of the block description, or give a constructive O(log N)-block exact s…
Proposed implication: A positive O(log N)-block compression would place SORT-BOUND-U into some level of PH (or give a stronger certificate class); a universal super-log alternation obstruction would rule out fixed-level PH membership and sha…
Historical reported excerpt (unverified): - Next: formalize operational definition of "alternation blocks" for G(n,k), relate to framed strategies/compression, form falsifiable all-n claim, try to disprove against known barriers.
Board: [2026-10-30 message](../../board/301/page-042.md?plain=1#L500) · [2026-10-30 message](../../board/301/page-042.md?plain=1#L508) · [2026-10-30 message](../../board/301/page-042.md?plain=1#L516) · [2026-10-30 message](../../board/301/page-042.md?plain=1#L524) · [2026-10-30 message](../../board/301/page-043.md?plain=1#L425) (8 total; use search for all)
Source manifests: [soring-fronts_adversary-alternation-logn-blocks](../../workspaces/manifests/soring-fronts_adversary-alternation-logn-blocks.json)

## downward-self-reducibility-sparse

Is SORT-BOUND-U downward self-reducible in a way compatible with polynomial-time reductions (or is every natural downward self-reduction blocked), and would such downward self-reducibility together with sparsity force consequences different from general sparse languages for this structured poset problem?

**investigated** · [Full research report](../../fronts/0070-downward-self-reducibility-sparse.md)
Intended test or falsifier: Construct an explicit polynomial-time downward self-reduction for SORT-BOUND-U to instances of strictly smaller 'size' in unary encoding, or prove that all poset-structure-preserving reductions must preserve some invari…
Proposed implication: For sparse sets, downward self-reducibility has known consequences (e.g. related to low sets/classes), but Mahaney already gave the many-one NP-hard =&gt; P=NP barrier; this targets the structured self-reducibility angle d…
Historical reported excerpt (unverified): **Finding (mathematical):** No explicit polynomial-time downward self-reduction (DSR) from $SORT\!-\!BOUND\!-\!U = \{1^n\#1^k : S(n)\le k\}$ to strictly smaller instances of the same language is known, and the natural routes appear blocked.
Board: [2026-10-30 message](../../board/301/page-043.md?plain=1#L425)
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_downward-self-reducibility-sparse](../../workspaces/manifests/soring-fronts_downward-self-reducibility-sparse.json)

## comparison-test-np-hardness-antichain

Is computing S(n) (or deciding SORT-BOUND-U) NP-hard under the restriction to comparison tests only, for the antichain/root instance family S_n, or does the fixed comparison test set avoid Hyafil-Rivest/Laber-Nogueira transfers and place it below NP despite arbitrary-test NP-hardness?

**investigated** · [Full research report](../../fronts/0072-comparison-test-np-hardness-antichain.md)
Intended test or falsifier: Exhibit a polynomial-time many-one reduction from some NP-complete problem to SORT-BOUND-U that is sound and complete for all n using only comparison-based tests and the antichain root, or prove no such reduction exists…
Proposed implication: A positive reduction would put SORT-BOUND-U in NP∩PSPACE (and relate to P!=NP) but must respect sparsity/Mahaney; a clean separation/obstruction would clarify whether NP membership is plausible without changing the arbi…
Historical reported excerpt (unverified): **Finding:** No polynomial-time many-one reduction from NP-complete problems to `SORT-BOUND-U` is known, and there is a concrete obstruction tied to the fixed pairwise-comparison test set (plus the unary sparsity barrier). The Hyafil–Rivest/Laber–Nogueira results do **not** transfer.
Source manifests: [soring-fronts_comparison-test-np-hardness-antichain](../../workspaces/manifests/soring-fronts_comparison-test-np-hardness-antichain.json)

## bounded-alternation-sortbound

For SORT-BOUND-U modeled as the bounded-depth alternating game G(n,k), is there a fixed constant d&gt;=1 with SORT-BOUND-U in Σ_d^P union Π_d^P for the relevant encodings, or does the antichain-root game require unbounded alternation depth under any polynomial-time reduction?

**investigated** · [Full research report](../../fronts/0079-bounded-alternation-sortbound.md)
Intended test or falsifier: Show unbounded alternation is necessary via a reduction preserving the game alternation structure, or conversely exhibit a fixed-level alternating algorithm for G(n,k) with polynomial time in unary N.
Proposed implication: A fixed-level collapse would place unary S(n)-evaluation much lower than full PSPACE; unbounded necessity would clarify the alternation/PSPACE boundary for this sparse language.
Historical reported excerpt (unverified): Reported alternation/strategy-size argument for unbounded alternation depth of the antichain-root game (adaptive dependencies + exponential strategy witnesses preclude fixed-level Σ_d^P with poly verification); distinguished general-poset results from certificate soundness/completeness. No repo cha…
Board: [2026-10-30 message](../../board/301/page-041.md?plain=1#L27) · [2026-10-30 message](../../board/301/page-041.md?plain=1#L123) · [2026-10-30 message](../../board/301/page-042.md?plain=1#L508) · [2026-10-30 message](../../board/301/page-042.md?plain=1#L516) · [2026-10-30 message](../../board/301/page-042.md?plain=1#L524)
Source manifests: [soring-fronts_bounded-alternation-sortbound](../../workspaces/manifests/soring-fronts_bounded-alternation-sortbound.json)

## fixed-block-alternation-obstruction

For all sufficiently large n and k = S(n) + O(1), does every winning strategy for the sorter in game G(n,k) require Omega(log n) alternation blocks between sorter/adversary moves, or can a constant number of blocks suffice?

**blocked** · [Full research report](../../fronts/0084-fixed-block-alternation-obstruction.md)
Intended test or falsifier: Construct for all large n a constant-block (say &lt;= 3 blocks) strategy achieving height within o(n) of S(n) and verifiable by a uniform polynomial-time procedure, or prove an all-n Omega(log n) block lower bound from the…
Proposed implication: A constant-block strategy would suggest highly compressed certificate forms for SORT-BOUND-U (closer to NP); an all-n Omega(log n) block lower bound would rule out fixed-block compressions and sharpen the alternation/PS…
Historical reported excerpt (unverified): Let us look up the game again carefully and think about block structure.
Board: [2026-10-31 message](../../board/301/page-040.md?plain=1#L187) · [2026-10-30 message](../../board/301/page-041.md?plain=1#L229) · [2026-10-31 message](../../board/301/page-041.md?plain=1#L301) · [2026-10-31 message](../../board/301/page-041.md?plain=1#L317) · [2026-10-31 message](../../board/301/page-041.md?plain=1#L333) (18 total; use search for all)
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_fixed-block-alternation-obstruction](../../workspaces/manifests/soring-fronts_fixed-block-alternation-obstruction.json)

## unary-alternation-depth-lower-bound

For all sufficiently large n, must every alternating Turing machine deciding SORT-BOUND-U on inputs encoding (n,k) with k near S(n) use Omega(S(n)) alternation rounds in the worst case over all sorter/adversary lines, ruling out any simulation that compresses the O(n log n) natural game alternations by more than a constant factor?

**investigated** · [Full research report](../../fronts/0097-unary-alternation-depth-lower-bound.md)
Intended test or falsifier: Construct an alternating algorithm (or uniform simulation) that decides SORT-BOUND-U in time polynomial in N=n+k+1 using o(S(n)) alternations for all large n, with an explicit correctness proof and alternation-count ana…
Proposed implication: A tight Theta(S(n)) alternation lower bound would fix the exact alternation complexity of the unary threshold game and sharpen the PSPACE upper bound to a more precise alternating-time class, distinguishing 'unbounded' …
Historical reported excerpt (unverified): **Honest limits:** No new theorem or counterexample was produced. The falsifier (explicit $o(S(n))$-alternation polytime ATM with proof) was not achieved; the obstruction is a paper-level complexity argument about strategy size/adaptivity, not a kernel-checked lower bound. Distinction maintained: g…
Source manifests: [soring-fronts_unary-alternation-depth-lower-bound](../../workspaces/manifests/soring-fronts_unary-alternation-depth-lower-bound.json)

## alternation-depth-vs-blocks-separation

For the interleaved sorter/adversary game achieving S(n), does the alternation depth in standard quantifier blocks equal Theta(S(n)) for all large n, and can this be separated from any constant-block reformulation without increasing the number of moves or losing exactness?

**investigated** · [Full research report](../../fronts/0100-alternation-depth-vs-blocks-separation.md)
Intended test or falsifier: Model the game as an ATM and show either that bounded blocks can simulate interleaved play with same move count and exact S(n), or prove an all-n lower bound of Omega(log n) blocks that is tight and cannot be compressed…
Proposed implication: A growing all-n alternation lower bound would constrain certificate forms below PSPACE; showing constant blocks suffice would suggest much more compressed forms exist, directly affecting NP-membership prospects.
Historical reported excerpt (unverified): **Conclusion:** I cannot construct a concrete disproof (e.g. a proof that bounded blocks cannot simulate). The separation depends on polynomial strategy compressibility (NP membership), which is open with known obstructions but no settled all-$n$ obstruction theorem. No Lean/repo changes warranted;…
Source manifests: [soring-fronts_alternation-depth-vs-blocks-separation](../../workspaces/manifests/soring-fronts_alternation-depth-vs-blocks-separation.json)

## comparison-test-restriction-hardness

For the minimum-height comparison decision tree (only pairwise comparisons, adversarial outcomes forming a total order), is the exact construction NP-hard for the antichain root S(n), or does the pairwise-test restriction strictly separate it from the arbitrary-test case where Hyafil–Rivest shows NP-completeness?

**investigated** · [Full research report](../../fronts/0101-comparison-test-restriction-hardness.md)
Intended test or falsifier: Produce a polynomial-time reduction from some NP-complete problem to constructing a height-S(n) comparison tree for some family, or prove the comparison-restricted problem is in P by a uniform all-n construction with a …
Proposed implication: A proof of NP-hardness for the restricted comparison model would change the complexity picture beyond arbitrary tests; a P-membership proof would rule out that route for NP membership of SORT-BOUND-U.
Historical reported excerpt (unverified): The active question is the NP-hardness/separation question described in AGENTS.md - whether constructing a minimum-height pairwise comparison tree for the antichain is NP-hard vs separated from Hyafil–Rivest.
Board: [2026-10-31 message](../../board/301/page-040.md?plain=1#L376) · [2026-10-31 message](../../board/301/page-040.md?plain=1#L384) · [2026-10-31 message](../../board/301/page-040.md?plain=1#L392) · [2026-10-31 message](../../board/301/page-040.md?plain=1#L400) · [2026-10-31 message](../../board/301/page-040.md?plain=1#L408) (24 total; use search for all)
Source manifests: [soring-fronts_comparison-test-restriction-hardness](../../workspaces/manifests/soring-fronts_comparison-test-restriction-hardness.json)

## fo-lfp-p-membership

Can SORT-BOUND-U be defined by a fixed-point logic formula (FO(LFP)) on ordered structures with polynomial-time data complexity, giving a new P-membership route distinct from explicit algorithmic recurrences?

**investigated** · [Full research report](../../fronts/0103-fo-lfp-p-membership.md)
Intended test or falsifier: Show that any FO(LFP) definition of the minimax height condition for the sorting game requires exponential growth on ordered structures or is equivalent to the game alternation (PSPACE) by known descriptive complexity t…
Proposed implication: An FO(LFP) (or Datalog) characterization would place exact comparison counting in P in the descriptive complexity sense and give a new algorithmic avenue; a barrier would sharpen the alternation/PSPACE connection.
Historical reported excerpt (unverified): **Bottom line:** The falsifier holds. An FO(LFP) (P) route is blocked by exponential state space / faithfulness + the alternation/PSPACE barrier; FO(PFP) aligns with the established PSPACE membership. This sharpens the alternation/PSPACE connection rather than giving a new P-membership route.
Board: [2026-10-31 message](../../board/301/page-040.md?plain=1#L236) · [2026-10-31 message](../../board/301/page-040.md?plain=1#L244)
Source manifests: [soring-fronts_fo-lfp-p-membership](../../workspaces/manifests/soring-fronts_fo-lfp-p-membership.json)

## algebraic-invariants-sortbound-20261101

Can algebraic invariants of the weak order/permutohedron (e.g. Coxeter length classes, descent sets, or the "graph of linear extensions") yield a uniform polynomial-time certificate or a new all-n obstruction for exact S(n)? Focus on whether any known algebraic invariant is invariant under optimal comparison strategy branching or can rule out compression of winning states across all n.

**investigated** · [Full research report](../../fronts/0120-algebraic-invariants-sortbound-20261101.md)
Intended test or falsifier: Exhibit an infinite family where every candidate algebraic invariant is identical on two root-adversarial histories but their minimax continuation costs S(P1), S(P2) differ, or show no algebraic invariant gives all-n in…
Proposed implication: A nontrivial algebraic invariant preserved by optimal play would give a new state compression class or a certificate property relevant to NP-membership; a strong falsification would rule out a large geometric/algebraic …
Historical reported excerpt (unverified): **Concrete failed/limited approach:** Exhaustive enumeration up to $n\le5$ + targeted searches for $n=6$ sampling; graph-isomorphism (WL) on linear extension graphs; checking Coxeter/descent/major-index distributions. No counterexample found; obstruction appears to be reduction to poset isomorphism…
Board: [2026-10-31 message](../../board/301/page-038.md?plain=1#L11) · [2026-11-01 message](../../board/301/page-038.md?plain=1#L123) · [2026-10-31 message](../../board/301/page-039.md?plain=1#L381) · [2026-10-31 message](../../board/301/page-039.md?plain=1#L389) · [2026-10-31 message](../../board/301/page-039.md?plain=1#L397)
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_algebraic-invariants-sortbound-20261101](../../workspaces/manifests/soring-fronts_algebraic-invariants-sortbound-20261101.json)

## fo-lfp-vs-sortbound-20261101

Does the uniform SORT-BOUND-U threshold admit an FO(LFP) (polynomial-time) definition on ordered structures, and if not what is the exact obstruction relative to known PSPACE bound? Distinguish descriptive complexity classes carefully against unary/binary encodings and against the special antichain case.

**investigated** · [Full research report](../../fronts/0122-fo-lfp-vs-sortbound-20261101.md)
Intended test or falsifier: Show either a natural FO(LFP) formula fails for some n due to model/encoding mismatch, or that FO(LFP) definability would force SORT-BOUND-U in P which is not ruled out but requires a nontrivial correspondence argument …
Proposed implication: FO(LFP) definability would give a strong structural upper bound (P) for SORT-BOUND-U; showing obstruction gives a descriptive-complexity barrier relevant to uniform evaluation.
Historical reported excerpt (unverified): **Mathematical finding (descriptive complexity / complexity of exact unary S(n)):**
Board: [2026-11-01 message](../../board/301/page-038.md?plain=1#L211) · [2026-11-01 message](../../board/301/page-038.md?plain=1#L219) · [2026-11-01 message](../../board/301/page-038.md?plain=1#L227) · [2026-11-01 message](../../board/301/page-038.md?plain=1#L235) · [2026-11-01 message](../../board/301/page-038.md?plain=1#L243) (10 total; use search for all)
Source manifests: [soring-fronts_fo-lfp-vs-sortbound-20261101](../../workspaces/manifests/soring-fronts_fo-lfp-vs-sortbound-20261101.json)

## folfp-explicit-sortbound

Can an explicit FO(LFP) formula over ordered finite structures define SORT-BOUND-U = {1^n # 1^k : S(n) &lt;= k} without encoding an exponential comparison tree?

**investigated** · [Full research report](../../fronts/0123-folfp-explicit-sortbound.md)
Intended test or falsifier: Prove no such uniform FO(LFP) definition exists for the exact unary sorting number predicate, or show any attempted definition is not faithful to adaptive pairwise comparison minimax on all n.
Proposed implication: An explicit FO(LFP) (capturing P on ordered structures) definition would yield SORT-BOUND-U in P; a general obstruction would sharpen the gap between the known PSPACE ATM bound and potential P membership.
Historical reported excerpt (unverified): The comment was posted. I need to follow the instruction exactly as given - "On billy-dev ONLY, study AGENTS.md, docs/problem.md and current board #301. Study the primary literature, attack a precise all-n falsifiable mathematical claim about complexity of EXACT unary S(n), and try seriously to DIS…
Board: [2026-11-01 message](../../board/301/page-038.md?plain=1#L363) · [2026-11-01 message](../../board/301/page-038.md?plain=1#L371) · [2026-11-01 message](../../board/301/page-038.md?plain=1#L379) · [2026-11-01 message](../../board/301/page-038.md?plain=1#L387) · [2026-11-01 message](../../board/301/page-038.md?plain=1#L395) (9 total; use search for all)
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_folfp-explicit-sortbound](../../workspaces/manifests/soring-fronts_folfp-explicit-sortbound.json)

## fo-lfp-exact-definition-sortbound

Is SORT-BOUND-U definable by an FO(LFP) formula (polynomial time, by Immerman–Vardi / Grädel) on the ordered structure encoding (1^n#1^k), given the known PSPACE/ATM characterization? If not directly obvious, find which precise game/recurrence is FO(LFP)-definable versus requiring PFP, and does a correct FO(LFP) definition yield a constructive polynomial-time evaluation method for the decision problem?

**investigated** · [Full research report](../../fronts/0134-fo-lfp-exact-definition-sortbound.md)
Intended test or falsifier: Prove SORT-BOUND-U is not FO(LFP)-definable (would separate P from PSPACE in this uniform model or show the minimax recurrence needs PFP) or construct an explicit FO(LFP) definition that is provably correct and can be e…
Proposed implication: FO(LFP) = P membership for SORT-BOUND-U would be a genuine upper-bound improvement beyond PSPACE; failure would clarify the descriptive complexity barrier.
Historical reported excerpt (unverified): The analysis suggests SORT-BOUND-U is not FO(LFP)-definable on the ordered structure encoding (1^n#1^k). The key obstruction is that the minimax recurrence over partial orders has exponentially many states (2^(Θ(n^2))) while any FO(LFP) formula of fixed arity can only define relations of polynomial…
Board: [2026-11-01 message](../../board/301/page-035.md?plain=1#L219) · [2026-11-01 message](../../board/301/page-035.md?plain=1#L227) · [2026-11-01 message](../../board/301/page-035.md?plain=1#L291)
Source manifests: [soring-fronts_fo-lfp-exact-definition-sortbound](../../workspaces/manifests/soring-fronts_fo-lfp-exact-definition-sortbound.json)

## randomized-exact-sortbound

Can a uniform randomized algorithm compute S(n) exactly in time 2^(o(n log^2 n)) for all sufficiently large n, or is exact randomized evaluation subject to the same adversarial-state obstacles as deterministic search?

**investigated** · [Full research report](../../fronts/0138-randomized-exact-sortbound.md)
Intended test or falsifier: Prove that any Las Vegas algorithm for exact S(n) must visit Omega(2^(c n log^2 n)) distinct poset states with high probability for some c&gt;0 and infinitely many n, or give a concrete randomized exact algorithm achieving…
Proposed implication: A randomized speedup would change the effective uniform complexity of computing S(n); a randomized lower bound would show the obstacle is information/strategy-theoretic rather than just determinism.
Historical reported excerpt (unverified): **Failed approach / obstruction:** Attempted to exploit random move ordering or randomized search; without knowing which OR moves are winning a priori and with adversarial AND forcing exploration of both outcomes for candidates, plus memoization requiring distinct states, exponential speedup is not…
Source manifests: [soring-fronts_randomized-exact-sortbound](../../workspaces/manifests/soring-fronts_randomized-exact-sortbound.json)

## adversarial-width-sortbound

Is the pathwidth or the adversarial antichain width of the minimax game tree on n elements unbounded as Omega(n / log n) in the worst case over all optimal strategies, and does this force alternation of that depth?

**investigated** · [Full research report](../../fronts/0139-adversarial-width-sortbound.md)
Intended test or falsifier: Show that for every n there is some strategy whose state graph has bounded pathwidth independent in effect or whose adversarial width is O(1), or prove width Omega(n/log n) forces the ATM alternation count to be linear …
Proposed implication: A width-based obstruction could link the unbounded alternation of the PSPACE ATM simulation to a concrete combinatorial parameter of the sorting game without reducing from arbitrary PSPACE instances.
Historical reported excerpt (unverified): **Finding (disproof): the premise is false by tree structure.** - **Model:** A deterministic adaptive sorting strategy is a comparison decision tree (game tree for G(n,k)) whose nodes are sorter/adversary states over partial orders; states reached under the strategy form a **tree** (not a general D…
Source manifests: [soring-fronts_adversarial-width-sortbound](../../workspaces/manifests/soring-fronts_adversarial-width-sortbound.json)

## antichain-fo-lfp-definability

Is SORT-BOUND-U definable in FO(LFP) on ordered structures representing the comparison game, or does the alternating minimax quantification over all incomparable pairs at each step create a strict alternation obstruction below PSPACE?

**investigated** · [Full research report](../../fronts/0143-antichain-fo-lfp-definability.md)
Intended test or falsifier: Construct an explicit FO(LFP) formula capturing the game (or show a polynomial-time evaluation reducing to it) contradicting known alternation bounds, or prove an alternation-depth/complexity obstruction that forces at …
Proposed implication: FO(LFP) definability would mean SORT-BOUND-U in P (Immerman–Vardi on ordered structures); an obstruction would rule out a direct P membership via descriptive complexity and sharpen the gap to PSPACE.
Historical reported excerpt (unverified): This is a structural/descriptive-complexity analysis. The obstruction is: polynomial alternation depth (∃pair ∀answer)^k over an exponentially large implicit poset arena cannot be collapsed into a monotone FO(LFP) on polynomial ordered structures (QBF-like), while ATM alternation gives APTIME=PSPAC…
Board: [2026-11-01 message](../../board/301/page-034.md?plain=1#L195)
Mixed-session reports: [e70582fbe904](../../followup/mixed-reports/objects/e70582fbe904334939e0e6f13c1298e6b6594eca5a3366efd5a8cab628e9326d.txt)
Source manifests: [soring-fronts_antichain-fo-lfp-definability](../../workspaces/manifests/soring-fronts_antichain-fo-lfp-definability.json)

## comparison-restriction-hardness

For pairwise comparison tests (a restricted subclass of all possible tests), is the minimum-height decision tree problem NP-hard for the sorting function class, or does the total-order constraint make computing S(n) polynomial-time equivalent to easier problems despite arbitrary-test NP-hardness?

**investigated** · [Full research report](../../fronts/0147-comparison-restriction-hardness.md)
Intended test or falsifier: Give a polynomial-time reduction from an NP-complete problem to SORT-BOUND-U under many-one reductions with correct unary encoding, or prove a complexity-theoretic barrier that blocks such a reduction given the comparis…
Proposed implication: NP-hardness under many-one reductions would force P=NP by sparsity of SORT-BOUND-U; polynomial-time tractability would separate the comparison-restricted model from arbitrary tests and place computing S(n) in P.
Historical reported excerpt (unverified): **Conclusion (honest):** - **No polynomial-time many-one reduction from an NP-complete problem to `SORT-BOUND-U` is known.** Given (1)-(3), such a reduction is *highly implausible* under the pairwise-comparison restriction + total-order constraint. - **Sparsity gives a strong conditional barrier:**…
Source manifests: [soring-fronts_comparison-restriction-hardness](../../workspaces/manifests/soring-fronts_comparison-restriction-hardness.json)

## fo-lfp-explicit-formula-sorting-bound

Construct and validate an explicit FO(PFP) formula defining SORT-BOUND-U on ordered structures from the capture theorem, and determine whether an FO(LFP) or ESO formula is achievable for the unary language.

**investigated** · [Full research report](../../fronts/0153-fo-lfp-explicit-formula-sorting-bound.md)
Intended test or falsifier: Show that no FO(PFP) formula captures SORT-BOUND-U up to encoding without using PSPACE resources in the formula, or construct an explicit FO(LFP) definition contradicting known barriers.
Proposed implication: An explicit descriptive complexity characterization would give a structural upper bound and clarify the relation between S(n) evaluation and fixed-point logics.
Historical reported excerpt (unverified): **Mathematical finding (descriptive complexity):** - **FO(PFP) capture is a theorem, not conjecture.** On ordered finite structures, Immerman–Vardi gives FO(PFP) = PSPACE. `SORT-BOUND-U ∈ PSPACE` (game/ATM) and the unary string `1^n#1^k` is naturally encodable as an ordered structure; hence there *…
Source manifests: [soring-fronts_fo-lfp-explicit-formula-sorting-bound](../../workspaces/manifests/soring-fronts_fo-lfp-explicit-formula-sorting-bound.json)

## readonce-branching-program-sortbound

Is SORT-BOUND-U computable by polynomial-size uniform read-once branching programs (ROBP) over the unary input representation, and can the comparison-adversary structure of the antichain give an all-n exponential ROBP lower bound or a polynomial upper bound?

**investigated** · [Full research report](../../fronts/0166-readonce-branching-program-sortbound.md)
Intended test or falsifier: Prove a super-polynomial uniform ROBP lower bound for SORT-BOUND-U for all large n, or construct a polynomial-size uniform ROBP family recognizing SORT-BOUND-U.
Proposed implication: ROBP lower bounds are often tractable and would separate SORT-BOUND-U from restricted classes without requiring a full P!=PSPACE proof; a polynomial ROBP would be a strong structural upper bound for exact sorting-number…
Historical reported excerpt (unverified): **Honest conclusion:** The question is genuinely open. A polynomial upper bound would need either S(n)∈P or a very clever uniform ROBP construction; an exponential lower bound would require a ROBP-specific lower-bound technique exploiting the minimax/adversary structure of sorting from the antichai…
Source manifests: [soring-fronts_readonce-branching-program-sortbound](../../workspaces/manifests/soring-fronts_readonce-branching-program-sortbound.json)

## ordered-bp-polysize-unary-sortbound

Is SORT-BOUND-U decidable by polynomial-size uniform ordered branching programs (OBPs) under the canonical left-to-right unary encoding, for all n&gt;=1?

**investigated** · [Full research report](../../fronts/0167-ordered-bp-polysize-unary-sortbound.md)
Intended test or falsifier: Prove an all-n super-polynomial lower bound on uniform OBP size for SORT-BOUND-U, or construct a polynomial-size uniform OBP family deciding it exactly for all n.
Proposed implication: An OBP separation from polynomial size would rule out a standard structured model without requiring full P!=PSPACE, while a polynomial OBP would yield a strong structured upper bound distinct from general branching prog…
Historical reported excerpt (unverified): **Finding (mathematical):** The question is genuinely open under standard complexity-theoretic interpretation of "ordered/oblivious branching programs" (fixed variable-access order, designer chooses best order) over the unary input 1^n # 1^k.
Source manifests: [soring-fronts_ordered-bp-polysize-unary-sortbound](../../workspaces/manifests/soring-fronts_ordered-bp-polysize-unary-sortbound.json)

## eso-descriptive-sortbound

For all n&gt;=1 with unary encoding of (n,k), does there exist an existential second-order sentence over finite ordered structures that is true iff S(n)&lt;=k and has size polynomial in (n+k), or is there an all-n inexpressibility obstruction forcing super-polynomial sentence size for any ESO definition of SORT-BOUND-U?

**blocked** · [Full research report](../../fronts/0174-eso-descriptive-sortbound.md)
Intended test or falsifier: Construct an explicit ESO sentence defining SORT-BOUND-U with size polynomial in unary input length, or prove for some all-n family that every ESO sentence deciding S(n)&lt;=k requires size &gt;= 2^(Omega(poly(n+k))).
Proposed implication: A polynomial ESO definition would yield SORT-BOUND-U in NP (a strict upper-bound improvement) while remaining uniform; a uniform inexpressibility barrier would constrain the descriptive-complexity route to NP membership…
Historical reported excerpt (unverified): Let us start by understanding the problem precisely.
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_eso-descriptive-sortbound](../../workspaces/manifests/soring-fronts_eso-descriptive-sortbound.json)

## uniform-ac0-tally-barrier

Is SORT-BOUND-U in DLOGTIME-uniform AC^0, or does the all-n nonperiodic growth of S(n) force every DLOGTIME-uniform constant-depth circuit family for its unary threshold to have super-polynomial size given the cutoff t_L depends on inverting S(n)?

**investigated** · [Full research report](../../fronts/0185-uniform-ac0-tally-barrier.md)
Intended test or falsifier: Construct a DLOGTIME-uniform AC^0 circuit family deciding SORT-BOUND-U for all lengths, or prove that DLOGTIME-uniformity plus constant depth plus polynomial size is incompatible with exactly representing the nondecreas…
Proposed implication: Separating nonuniform AC^0 (established) from uniform AC^0 would place SORT-BOUND-U below P but above the weakest uniform constant-depth classes, clarifying how advice/computability of the threshold interacts with exact…
Historical reported excerpt (unverified): **FINDING (deduction):** SORT-BOUND-U ∉ DLOGTIME-uniform AC^0. **Attack/result:** Try to falsify “in DLOGTIME-uniform AC^0” by analyzing uniformity. DLOGTIME-uniform AC^0 ⇔ threshold predicate P(n,k)= (S(n)≤k) decidable in DLOGTIME. DLOGTIME = random-access deterministic TM, time O(log t) on input …
Source manifests: [soring-fronts_uniform-ac0-tally-barrier](../../workspaces/manifests/soring-fronts_uniform-ac0-tally-barrier.json)

## sparse-turing-np-hardness-collapse

Does polynomial-time Turing (Cook) reducibility of NP-complete languages to SORT-BOUND-U, despite its sparsity, force a collapse of the polynomial hierarchy beyond P=NP, and is such Turing-hardness compatible with known Mahaney obstructions?

**investigated** · [Full research report](../../fronts/0193-sparse-turing-np-hardness-collapse.md)
Intended test or falsifier: Exhibit a formal barrier showing that Ogiwara–Watanabe or related sparse Turing-hardness consequences do not apply here due to the specific structure of SORT-BOUND-U, or construct an explicit Turing reduction from some …
Proposed implication: Establishing Turing-hardness of SORT-BOUND-U for NP would have major complexity consequences distinct from many-one reductions; ruling it out would close a plausible route around Mahaney's barrier.
Historical reported excerpt (unverified): **Honest limits:** The question as stated asks to “exhibit a formal barrier…” or construct reduction. I found no formal barrier specific to `SORT-BOUND-U` structure; the general sparse-set theory applies. I found no candidate explicit reduction. The key mathematical point is: Turing-hardness ⇒ PH c…
Board: [2026-11-02 message](../../board/301/page-032.md?plain=1#L347) · [2026-11-02 message](../../board/301/page-032.md?plain=1#L355)
Source manifests: [soring-fronts_sparse-turing-np-hardness-collapse](../../workspaces/manifests/soring-fronts_sparse-turing-np-hardness-collapse.json)

## antichain-fo-pfp-gap

Can the ATM alternation proof placing SORT-BOUND-U in PSPACE be translated into an explicit FO(PFP) formula on finite ordered structures for the antichain game, and does that translation create any uniform-size blowup that would obstruct effective reduction arguments?

**investigated** · [Full research report](../../fronts/0196-antichain-fo-pfp-gap.md)
Intended test or falsifier: Show that every FO(PFP) definition of SORT-BOUND-U requires a fixed-point operator nesting depth growing faster than polylogarithmically in input length, or construct an explicit formula of polynomial alternation depth …
Proposed implication: An explicit FO(PFP) form would make the descriptive complexity precise; a depth blowup could reveal a hidden barrier between ATM time and logical complexity for this game.
Historical reported excerpt (unverified): Let us look up the actual structure of the current running agent or think. But easier to just reason it out.
Board: [2026-11-02 message](../../board/301/page-031.md?plain=1#L75) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L83) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L91) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L99) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L107) (12 total; use search for all)
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_antichain-fo-pfp-gap](../../workspaces/manifests/soring-fronts_antichain-fo-pfp-gap.json)

## fo-pfp-explicit-formula

Give an explicit FO(PFP) formula (on ordered structures encoding the poset/unary input) defining SORT-BOUND-U exactly, with a correctness argument mapping the alternation game to PFP and a complexity/size sketch; test on small n/k and show it does not collapse to FO(LFP).

**investigated** · [Full research report](../../fronts/0218-fo-pfp-explicit-formula.md)
Intended test or falsifier: Find a counterexample instance or show the proposed formula is equivalent to FO(LFP)/P under standard assumptions or is not sound/compositional.
Proposed implication: A concrete explicit FO(PFP) definition strengthens the descriptive-complexity capture claim and could clarify whether a collapse to P/NP is ruled out by the formula structure; independent verification artifact.
Historical reported excerpt (unverified): The report is complete with explicit formula structure, correctness mapping to PFP/PSPACE, tests on small cases, falsification attempts (including adversary consistency constraint and collapse), and honest limits. No repo changes made as requested.The task is complete. Report written to FO_PFP_FORM…
Board: [2026-11-01 message](../../board/301/page-036.md?plain=1#L35) · [2026-11-01 message](../../board/301/page-036.md?plain=1#L51) · [2026-11-01 message](../../board/301/page-037.md?plain=1#L319) · [2026-11-01 message](../../board/301/page-037.md?plain=1#L343) · [2026-11-01 message](../../board/301/page-037.md?plain=1#L415) (9 total; use search for all)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e10956d47ffeMcCfEn7CJY7TWb](../../assistant-reports/sessions/ses_e10956d47ffeMcCfEn7CJY7TWb.md)
Original task commissions: [83b1d74913d7](../../followup/task-commissions/objects/83b1d74913d7edb7d2ee7ed491b6e188c0ebf4c6606edcd551d0467942d1b928.txt)
Mixed-session reports: [7337ad8fde3a](../../followup/mixed-reports/objects/7337ad8fde3ad2e2976de82c68af7c0d98afbebeffcec3135ed94b0cc8bdc9d6.txt)
Source manifests: [soring-fronts_fo-pfp-explicit-formula-20261101](../../workspaces/manifests/soring-fronts_fo-pfp-explicit-formula-20261101.json) · [soring-fronts_fo-pfp-explicit-formula-20261118exec](../../workspaces/manifests/soring-fronts_fo-pfp-explicit-formula-20261118exec.json) · [soring-fronts_fo-pfp-explicit-formula](../../workspaces/manifests/soring-fronts_fo-pfp-explicit-formula.json)

## alternation-depth-sorting-game

Model SORT-BOUND-U as an alternating game of depth exactly k with O(n^2) possible moves per round and quantify the alternation complexity: is the minimal alternation depth polynomial in input length for the unary threshold or is it linear in k?

**investigated** · [Full research report](../../fronts/0229-alternation-depth-sorting-game.md)
Intended test or falsifier: Show that bounding alternation depth below k forces loss for the sorter on some antichain instance, or prove the ATM of Claim A achieves PSPACE with alternation depth Theta(k)=Theta(N) and cannot be collapsed.
Proposed implication: Tight alternation-depth bounds would clarify the relation between game tree depth and the alternating complexity class, distinguishing 'polynomial alternations' from 'alternations up to input length'.
Historical reported excerpt (unverified): **Finding (deduction, game-theoretic):** Modeling SORT-BOUND-U as G(n,k) (sorter ∃ picks pair, adversary ∀ gives direction consistent with some linear extension, alternating, adversary must remain globally consistent), alternation depth cannot be collapsed below k because sorter moves must be adapt…
Source manifests: [soring-fronts_alternation-depth-sorting-game](../../workspaces/manifests/soring-fronts_alternation-depth-sorting-game.json)

## descriptive-folfp-sorting-bound

For all n,k, does there exist a fixed FO(LFP) sentence phi such that (N_n,k, &lt;) \|= phi iff S(n) &lt;= k, where N_n,k encodes 1^n # 1^k as an ordered structure (size Theta(n+k))? Equivalently, is SORT-BOUND-U in Datalog with least fixed point (P by Immerman–Vardi) via an explicit uniform formula over the game/poset states?

**investigated** · [Full research report](../../fronts/0239-descriptive-folfp-sorting-bound.md)
Intended test or falsifier: Prove that every FO(LFP) definition of the minimax height on the n-antichain comparison game must have quantifier/closure rank growing at least linearly in n (or unbounded over all n) with no uniform fixed formula, or e…
Proposed implication: A fixed FO(LFP) definition would give a new uniform upper bound placing SORT-BOUND-U in P (separately from the exponential-time DFS) and a descriptive-complexity characterization; a uniform-inexpressibility obstruction …
Historical reported excerpt (unverified): ## Conclusion I need to report this finding. The mathematical obstruction is the winning frontier barrier: 2^(Ω(n log² n)) nonisomorphic winning states at depths near S(n) imply that any correct algorithm must process super-polynomially many states relative to input length N=Θ(n log n), so SORT-BOU…
Source manifests: [soring-fronts_descriptive-folfp-sorting-bound](../../workspaces/manifests/soring-fronts_descriptive-folfp-sorting-bound.json)

## linear-extension-count-hardness-block

Show for all sufficiently large n that no polynomial-time (in n) uniform procedure can decide exact-reset feasibility from (P,Q) alone without simulating comparisons, because deciding partitionability by comparison splits reduces to counting linear extensions #P-hard instances embedded in reachable sorting posets.

**investigated** · [Full research report](../../fronts/0251-linear-extension-count-hardness-block.md)
Intended test or falsifier: Give a polynomial-time checkable invariant computable without full #P evaluation that is sound and complete for exact-reset realizability over all reachable P from A_n, or construct an explicit polynomial algorithm for …
Proposed implication: Would formalize why 'just track e(P)' is insufficient and show the certificate feasibility test itself is intractable, explaining the gap between soundness and completeness for exact-reset certificate systems without cl…
Historical reported excerpt (unverified): The analysis is done. I studied AGENTS.md, problem.md, docs on exact-reset, certificates/barriers, and looked at board context. I attacked the front claim - the #P-hardness of counting linear extensions combined with branch-divisibility constraints and strategy-dependence makes polynomial-time feas…
Source manifests: [soring-fronts_linear-extension-count-hardness-block](../../workspaces/manifests/soring-fronts_linear-extension-count-hardness-block.json)

## atm-alternation-depth-bound

For the alternating Turing machine deciding SORT-BOUND-U via the minimax game G(n,k), is the polynomial alternation depth O(k)=O(n log n) necessary for all-n instances, or can a uniform ATM decide it with alternation depth O(log^c (n+k)) for some fixed c (bounded or polylog alternation)?

**blocked** · [Full research report](../../fronts/0291-atm-alternation-depth-bound.md)
Intended test or falsifier: Construct a uniform alternating Turing machine for SORT-BOUND-U with alternation depth O(log^c N) and polynomial time in unary input length N, or prove that every uniform ATM accepting SORT-BOUND-U must have alternation…
Proposed implication: A bounded/polylog alternation bound would place SORT-BOUND-U in a strict subclass of PSPACE (below the full linear-alternation level) without invoking circuit lower bounds; a necessary linear alternation depth would cla…
Historical reported excerpt (unverified): Or another possibility is that determining the "graph’s pathwidth" via some games gives PSPACE-completeness? Or "graph bandwidth"? Let us search more specifically.
Board: [2026-11-18 message](../../board/301/page-014.md?plain=1#L1161)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e105decefffezblM42p51WP44R](../../assistant-reports/sessions/ses_e105decefffezblM42p51WP44R.md)
Original task commissions: [eb66b7109658](../../followup/task-commissions/objects/eb66b7109658eae3bf12d8598d4c669e6c99ce5e1e732773095437a0701680a0.txt)
Mixed-session reports: [27ee65221e7e](../../followup/mixed-reports/objects/27ee65221e7eb263042318d26dd734e81aa31e632b8a1797488a03cfc0b5c518.txt) · [3f4f3b35bd60](../../followup/mixed-reports/objects/3f4f3b35bd60c6ae609978b0defad0175656dba30d24fc1d535e45018c3c99e6.txt)
Source manifests: [soring-fronts_atm-alternation-depth-bound](../../workspaces/manifests/soring-fronts_atm-alternation-depth-bound.json)

## turing-np-hardness-sparse

Is the unary threshold language SORT-BOUND-U NP-hard under polynomial-time Turing reductions, or can this be ruled out without collapsing P to NP?

**investigated** · [Full research report](../../fronts/0292-turing-np-hardness-sparse.md)
Intended test or falsifier: Exhibit a polynomial-time Turing reduction from some NP-complete language to SORT-BOUND-U, or prove unconditionally that no such reduction exists via the Ogiwara–Watanabe sparse-set theory.
Proposed implication: Polynomial-time Turing NP-hardness of a sparse set in PSPACE would imply the polynomial hierarchy collapses to Δ₂P; ruling it out would clarify the boundary beyond Mahaney's many-one case.
Historical reported excerpt (unverified): **Concrete failed/obstructed angle:** Trying to port Brightwell–Winkler/#P-completeness directly fails by certificate-size/non-determinism mismatch and by the `S(P) != f(e(P))` obstruction (general-poset counting hard but the *minimax comparison cost* is not determined by extension count). Any atte…
Source manifests: [soring-fronts_turing-np-hardness-sparse](../../workspaces/manifests/soring-fronts_turing-np-hardness-sparse.json)

## adaptive-tree-verification-hardness

For a succinctly described adaptive comparison tree (or framed DAG) that claims to sort n elements within k comparisons, is the validity+height verification problem complete for coNP or harder under the unary input encoding?

**investigated** · [Full research report](../../fronts/0294-adaptive-tree-verification-hardness.md)
Intended test or falsifier: Show polynomial-time verification for all valid inputs via a uniform algorithm, or prove coNP-completeness (model-preserving) distinguishing this adaptive case from Parberry's fixed-network verification.
Proposed implication: CoNP-complete verification would create a gap between existence of a certificate and efficient checkability depending on representation, informing the NP-membership question for SORT-BOUND-U without conflating with netw…
Historical reported excerpt (unverified): **Bottom line:** The falsifier "prove coNP-completeness (model-preserving) distinguishing this adaptive case from Parberry's fixed-network verification" is refuted by the representation distinction. The correct complexity split is: **fixed-network correctness = coNP-complete (circuit/universal over…
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_adaptive-tree-verification-hardness](../../workspaces/manifests/soring-fronts_adaptive-tree-verification-hardness.json)

## winning-frontier-enumeration-hardness

For all sufficiently large n of the form n=2^(2r), does the exponential family of nonisomorphic winning states at fixed relative depth (the independent-edge/chain construction giving &gt;= 2^((1/4-o(1)) n (log n)^2) states) force any uniform DP algorithm that tracks all reachable winning classes by exact isomorphism to run in time &gt;= 2^((1/8-o(1)) n (log n)^2) on input 1^n, even if it does not enumerate a single-policy tree?

**investigated** · [Full research report](../../fronts/0300-winning-frontier-enumeration-hardness.md)
Intended test or falsifier: Give a uniform algorithm computing S(n) (or deciding SORT-BOUND-U) in time 2^((1/16) n (log n)^2) for all large n=2^(2r) by some symbolic method (not full state enumeration) exploiting the structure of that winning fron…
Proposed implication: A state-space frontier lower bound on uniform exact algorithms would be structural (not circuit-based) and directly relevant to the 2^(O(n log^2 n))/2^(O(N log N)) bounds, without claiming P!=PSPACE or super-polynomial …
Historical reported excerpt (unverified): **Limits:** This rules out the claim only for algorithms *forced* to track all reachable winning classes by exact isomorphism; it is a structural/compression argument (order ideals), not a circuit lower bound. Certificate soundness vs completeness remains distinct from this; no repository changes a…
Source manifests: [soring-fronts_winning-frontier-enumeration-hardness](../../workspaces/manifests/soring-fronts_winning-frontier-enumeration-hardness.json)

## qbf-alternation-tightness

For the budgeted alternating/positional game characterizing SORT-BOUND-U, is the minimal all-n alternation depth Ω(n) or can it be shown O(n / polylog n) for some uniform ATM recognizing SORT-BOUND-U on unary input?

**investigated** · [Full research report](../../fronts/0306-qbf-alternation-tightness.md)
Intended test or falsifier: Prove for all large n that every uniform ATM deciding SORT-BOUND-U in time polynomial in N=n+k+1 requires alternation depth Ω(n / polylog n) on some input, or construct one with depth o(n / polylog n) for all n.
Proposed implication: Tight alternation bounds would clarify the ATM-level position below PSPACE without relying on circuit lower bounds and without conflating numeric n with binary length.
Historical reported excerpt (unverified): ## Mathematical finding / precise obstacle (honest limit) **Deduction (paper-level, checkable):** The budgeted alternating game `G(n,k)` yields a uniform ATM for `SORT-BOUND-U` with `time O(N³)`, `space O(n²)`, and alternation depth `O(k)`. On the information-tight threshold regime `k = Θ(S(n)) = Θ…
Source manifests: [soring-fronts_qbf-alternation-tightness](../../workspaces/manifests/soring-fronts_qbf-alternation-tightness.json)

## factorial-extension-hardness-forcing

For every n &gt;= 12, must every finite poset P with e(P) = n! satisfy m(P) &gt;= S(n), or does some n admit a poset with n! linear extensions that is sortable in just ceil(log2(n!)) comparisons?

**investigated** · [Full research report](../../fronts/0333-factorial-extension-hardness-forcing.md)
Intended test or falsifier: Construct, first at n=12, a poset P with e(P)=12! and m(P)=29=ceil(log2 12!), or an infinite family with e(P)=n! and m(P)=ceil(log2(n!)) strictly below S(n).
Proposed implication: A construction shows the n=12 excess is caused by the antichain's structure rather than by its extension count, and proves that extension-count-only lower bounds cannot certify S(n); the universal answer would instead g…
Historical reported excerpt (unverified): While the full n=9 DP runs, a sharper targeted question emerges: the n=12 falsifier needs **945-block (F=10) and 495-block (F=9)**, since 12! = 2^10 · 945 · 495 with costs 10+10+9 = 29 = C(12). And e=143 was already *perfect* (F=8) on 8 elements. Let me build a capped, pruned solver for "does a pos…
Assistant reports: [ses_e4759458cffeCX3iqCfCZfW5Wi](../../assistant-reports/sessions/ses_e4759458cffeCX3iqCfCZfW5Wi.md) · [ses_e4758c007ffePpZdz6o8fJHnxG](../../assistant-reports/sessions/ses_e4758c007ffePpZdz6o8fJHnxG.md) · [ses_e47383d75ffeCJkOYm9BSMS058](../../assistant-reports/sessions/ses_e47383d75ffeCJkOYm9BSMS058.md)
Original task commissions: [8b1ea5ccf4a4](../../followup/task-commissions/objects/8b1ea5ccf4a444f47ab788f6089e0e3ea64c0a7ad5831e48bb10e0037248e1f5.txt) · [8b6eded51fcf](../../followup/task-commissions/objects/8b6eded51fcf49e21efa04dbcefc3a7dc1d64db87645de34a39483d6056eee18.txt) · [e284d19cd0e3](../../followup/task-commissions/objects/e284d19cd0e315af9127a7489d9241f0b1f28b120ff200ba9c6772f81dcf8c8e.txt)
Source manifests: [soring-fronts_factorial-extension-hardness-forcing](../../workspaces/manifests/soring-fronts_factorial-extension-hardness-forcing.json)

## shallow-state-fibonacci-hardness

Is the Fibonacci threshold predicate e(P) &lt;= T(b) still PP-hard under Las Vegas reductions when P is restricted to n-element posets lying at distance at most S(n) from the n-antichain, that is, the states actually reachable inside an exact unary evaluator?

**investigated** · [Full research report](../../fronts/0334-shallow-state-fibonacci-hardness.md)
Intended test or falsifier: Give a deterministic or Las Vegas polynomial-time (in n+b) algorithm for e(P) &lt;= T(b) on all such shallow n-element states, or an infinite family of shallow states whose threshold predicate encodes a PP-hard problem.
Proposed implication: If hardness survives the depth and ground-set restriction, the newest PP-hardness result genuinely blocks extension-threshold pruning for SORT-BOUND-U; if not, the general-poset hardness is an artifact of unreachable la…
Historical reported excerpt (unverified): The front's substantive question is answered (conditionally): the shallow/reachable-state restriction does not rescue extension-threshold pruning, because any reduction target can be pumped into the comparison-reachable class via a fixed bottom chain. The result's validity inherits the existing una…
Board: [2026-11-08 message](../../board/301/page-022.md?plain=1#L53)
Assistant reports: [ses_e47594105ffe8uRkSNvFMhap5B](../../assistant-reports/sessions/ses_e47594105ffe8uRkSNvFMhap5B.md) · [ses_e4758bca2ffeWZC1XVF6lgs01K](../../assistant-reports/sessions/ses_e4758bca2ffeWZC1XVF6lgs01K.md) · [ses_e47383ba8ffePddQX4d5lP8kjH](../../assistant-reports/sessions/ses_e47383ba8ffePddQX4d5lP8kjH.md)
Original task commissions: [23ae7b136128](../../followup/task-commissions/objects/23ae7b1361288ed8f248538b9fea9def897ef251559eec38dc08b90851683389.txt) · [3a418a1cb5d8](../../followup/task-commissions/objects/3a418a1cb5d8dbed75345472acf461ee97a8554c5cc68f426f4b0394f8c029cf.txt) · [a150b1d761a5](../../followup/task-commissions/objects/a150b1d761a5d08b81029e24f0d9658911b8c1848ce26dc7182438d4d843736f.txt)
Source manifests: [soring-fronts_shallow-state-fibonacci-hardness](../../workspaces/manifests/soring-fronts_shallow-state-fibonacci-hardness.json)

## sparse-hasse-extension-hardness

Is counting linear extensions #P-hard under Turing reductions for n-element posets whose Hasse diagram has at most C n log n cover relations, for some absolute constant C?

**investigated** · [Full research report](../../fronts/0344-sparse-hasse-extension-hardness.md)
Intended test or falsifier: Give a uniform polynomial-time algorithm that counts linear extensions exactly for every n-element poset with at most C n log n cover relations, or prove this restricted counting problem is in FP.
Proposed implication: Every poset reached from the n-antichain at depth at most S(n) has at most S(n)=O(n log n) covers, so hardness here would make the Fibonacci extension threshold unusable as a polynomial-time state-local prune on the rea…
Historical reported excerpt (unverified): duplicate acknowledged, no external effects
Assistant reports: [ses_e46747f44ffeTbjs5WpgB9iZoA](../../assistant-reports/sessions/ses_e46747f44ffeTbjs5WpgB9iZoA.md) · [ses_e46736c09ffelmX1W6Qyurj4hb](../../assistant-reports/sessions/ses_e46736c09ffelmX1W6Qyurj4hb.md)
Original task commissions: [004c759b7dab](../../followup/task-commissions/objects/004c759b7dabe2c3addd5a87e6e613790aefc88ce59e0bd4ef8b7818e1e4439f.txt) · [31a499bcdc31](../../followup/task-commissions/objects/31a499bcdc31b6d0f2ba88f260c609f864660c57172ce68371aac49e9a910340.txt) · [b73e56a7164b](../../followup/task-commissions/objects/b73e56a7164bc103023a6aedbefafe40055f1b08dc54c7584930c9b8589ccaff.txt)
Source manifests: [soring-fronts_sparse-hasse-extension-hardness](../../workspaces/manifests/soring-fronts_sparse-hasse-extension-hardness.json)

## pp-hardness-transfer-antichain

Does the PP-hardness of the general-poset Fibonacci extension-threshold predicate transfer to the antichain language SORT-BOUND-U under polynomial-time reductions, or is there a provable non-transfer barrier?

**investigated** · [Full research report](../../fronts/0349-pp-hardness-transfer-antichain.md)
Intended test or falsifier: Construct an encoding-preserving polynomial-time reduction from the PP-hard predicate e(P)&lt;=T(b) to SORT-BOUND-U, or prove that no such reduction can exist without collapsing PP or the polynomial hierarchy.
Proposed implication: A transfer would make SORT-BOUND-U PP-hard, a new hardness result below PSPACE that bypasses the sparse many-one NP barrier; a non-transfer theorem would isolate general-poset hardness as irrelevant to exact S(n) evalua…
Historical reported excerpt (unverified): **Conclusion:** no unfinished mathematical work and no repeated side effects. The only review item is the stale ledger entry, which the keeper should mark `investigated` on agent exit.
Board: [2026-11-08 message](../../board/301/page-022.md?plain=1#L239)
Assistant reports: [ses_e461ce7baffe9VKQF1wTaXue8Q](../../assistant-reports/sessions/ses_e461ce7baffe9VKQF1wTaXue8Q.md)
Original task commissions: [66b34c59a996](../../followup/task-commissions/objects/66b34c59a996e13503af292f6d558d3adb007b8c77cbb5eee38b9a1143d924e3.txt)
Source manifests: [soring-fronts_pp-hardness-transfer-antichain](../../workspaces/manifests/soring-fronts_pp-hardness-transfer-antichain.json)

## counting-oracle-sortbound-complexity

Is SORT-BOUND-U decidable in deterministic polynomial time with an oracle for exact linear-extension counts, that is, in P^{#P}, and can the minimax height be recovered from polynomially many extension-count queries?

**investigated** · [Full research report](../../fronts/0353-counting-oracle-sortbound-complexity.md)
Intended test or falsifier: Prove a query lower bound or a relativized separation showing that exact linear-extension counts cannot decide the unary sorting threshold in polynomial time, or construct the required P^{#P} algorithm with a correctnes…
Proposed implication: A P^{#P} upper bound would place the exact unary threshold below PSPACE and quantify what the general-poset #P hardness leaves open; a negative result would rule out extension-counting as a complete algorithmic route.
Historical reported excerpt (unverified): ## Finding: a proved unbounded lookahead-depth barrier for extension-count recovery
Board: [2026-11-08 message](../../board/301/page-022.md?plain=1#L358)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e45ac9b9cffevIzNrzH3W0V1y1](../../assistant-reports/sessions/ses_e45ac9b9cffevIzNrzH3W0V1y1.md)
Original task commissions: [966bdb037baf](../../followup/task-commissions/objects/966bdb037baf382b38e66992036496074e8edc1bc11f8c54a2194e8bb2234df4.txt)
Mixed-session reports: [87b5610cc743](../../followup/mixed-reports/objects/87b5610cc74393549864d862ab283c7e5bd3cb2983ddfed92110f5f7702ae245.txt)
Source manifests: [soring-fronts_counting-oracle-sortbound-complexity](../../workspaces/manifests/soring-fronts_counting-oracle-sortbound-complexity.json)

## constant-round-am-sortbound

Does SORT-BOUND-U admit a public-coin interactive proof with O(1) rounds and a polynomial-time verifier (membership in AM), or does every constant-round protocol fail on infinitely many unary inputs because the minimax game's alternation cannot be compressed?

**investigated** · [Full research report](../../fronts/0359-constant-round-am-sortbound.md)
Intended test or falsifier: An explicit O(1)-round Arthur-Merlin protocol with perfect completeness and soundness error at most 1/3 for all n,k, or a proof that every constant-round protocol errs on an infinite unary family.
Proposed implication: AM membership would place the unary threshold in the polynomial hierarchy (AM is contained in Pi_2^P), a new upper bound below the known PSPACE bound; a lower bound would separate this minimax language from arbitrary PS…
Historical reported excerpt (unverified): **Recommended next action:** let the keeper record this run’s finding from the agent output, or flag the ledger entry for review. No further mathematical work or repository action is warranted from this turn.
Assistant reports: [ses_e455e57adffe0LMs0N5vWPY8Y0](../../assistant-reports/sessions/ses_e455e57adffe0LMs0N5vWPY8Y0.md)
Original task commissions: [c91a793269b5](../../followup/task-commissions/objects/c91a793269b540671cce4ca650e5dc8f9f1898a45ffaea63ee1636b901ab5e4a.txt)
Source manifests: [soring-fronts_constant-round-am-sortbound](../../workspaces/manifests/soring-fronts_constant-round-am-sortbound.json)

## optimal-play-membership-polynomial

For every n and every comparison history H reachable from the n-element antichain, decide whether H can be extended to a height-S(n) optimal sorting strategy; determine whether this decision problem is solvable in polynomial time in n and \|H\|, or whether an infinite family of histories makes it intractable.

**investigated** · [Full research report](../../fronts/0517-optimal-play-membership-polynomial.md)
Intended test or falsifier: Exhibit an infinite family of prefixes H_n for which every algorithm deciding optimal-play extendability requires superpolynomial time, or construct a polynomial-time dynamic program with a proof of correctness for all …
Proposed implication: A polynomial-time test would turn optimal-play reachability into an efficiently checkable property and support succinct completeness arguments for SORT-BOUND-U; intractability would be a barrier to such certificates.
Historical reported excerpt (unverified): **Outcome: concrete failed approach / exact obstruction (honest limit)**
Assistant reports: [ses_e186c55e4ffe4WZNfTduuwal0H](../../assistant-reports/sessions/ses_e186c55e4ffe4WZNfTduuwal0H.md)
Original task commissions: [ba02597b1659](../../followup/task-commissions/objects/ba02597b1659311a7146b8f003c7058d233ebb80827c5e1afaacb0f849caebfd.txt)
Mixed-session reports: [13ac6bdf6288](../../followup/mixed-reports/objects/13ac6bdf62887b40c8dc4a8e3f26c8e60e6d2050af7b37753b3f528d4fff7e1e.txt)
Source manifests: [soring-fronts_optimal-play-membership-polynomial](../../workspaces/manifests/soring-fronts_optimal-play-membership-polynomial.json)

## sortboundu-bqp-membership

Is the tally threshold language SORT-BOUND-U = {1^n # 1^k : S(n) &lt;= k} decidable by a uniform bounded-error quantum polynomial-time algorithm on unary input length N = n+k+1, i.e. is SORT-BOUND-U in BQP (which is contained in PSPACE, so this is a genuine upper-bound target)? Equivalently, can the exact minimax AND-OR game of depth k = O(n log n) and branching O(n^2) be evaluated by a quantum algorithm in time 2^{o(n log^2 n)} for all n, improving the classical transcript-DFS exponent by more than a constant factor?

**investigated** · [Full research report](../../fronts/0538-sortboundu-bqp-membership.md)
Intended test or falsifier: Construct a uniform quantum algorithm (amplitude-amplified minimax, quantum walk over the winning-state/winning-frontier DAG, or quantum counting of consistent linear extensions) computing S(n) in time 2^{o(n log^2 n)} …
Proposed implication: A positive answer would place this tally language in BQP, a new upper bound below PSPACE independent of the NP/coNP certificate routes; a matching quantum lower bound would be a barrier ruling out the entire quantum-min…
Historical reported excerpt (unverified): **Conclusion: nothing unfinished, nothing to repeat.** I did not re-post, re-commit, or re-execute anything. The interrupted-prompt template does not correspond to any new effect to perform; continuing it blindly would only cause duplication.
Board: [2026-11-18 message](../../board/301/page-014.md?plain=1#L1810) · [2026-11-18 message](../../board/301/page-014.md?plain=1#L1846) · [2026-11-18 message](../../board/301/page-014.md?plain=1#L1868)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e1021d8acffe6NbSSITdxBBgTw](../../assistant-reports/sessions/ses_e1021d8acffe6NbSSITdxBBgTw.md)
Original task commissions: [d48e072da2be](../../followup/task-commissions/objects/d48e072da2be80d6141419490b08cd854f5d55890a50e352d9f196e931f3f962.txt)
Mixed-session reports: [6c8b7f9d65b6](../../followup/mixed-reports/objects/6c8b7f9d65b62c6aee1c52ddd6b78e891233c2c9854ed662d668b413c39cd953.txt) · [874486592e62](../../followup/mixed-reports/objects/874486592e625afd2039417bf4beddc9f16a58d4f9e54d9f9925254b1ab4a157.txt) · [cdcdb0172472](../../followup/mixed-reports/objects/cdcdb01724722d467823ac87d9e5bbe5cb0cc016a9102ea36503efa1d19761b1.txt) (4 total)
Source manifests: [soring-fronts_sortboundu-bqp-membership](../../workspaces/manifests/soring-fronts_sortboundu-bqp-membership.json)

## uniform-tc0-sortbound-membership

For all n, is the unary threshold language SORT-BOUND-U decidable by a DLOGTIME-uniform TC0 (or ACC0) circuit family, given that the information bound ceil(log2 n!) is itself in uniform TC0 and only the o(n) information excess separates it from the exact sorting number S(n)?

**investigated** · [Full research report](../../fronts/0567-uniform-tc0-sortbound-membership.md)
Intended test or falsifier: Exhibit a uniform TC0 circuit computing S(n) for every n (upper outcome), or derive a uniform TC0 lower bound for the excess predicate from iterated multiplication or majority (negative outcome).
Proposed implication: A TC0 membership proof would place exact unary sorting-number evaluation far below P; a lower bound would give the first circuit-class separation for the tally sequence and sharpen the known PSPACE/poly baseline.
Historical reported excerpt (unverified): Git is clean at `6a96398d937d20977a91b9afa8619cb27feab269`; no repository edits or commits occurred. Scratch material is under `/tmp/opencode/`. No unfinished external action remains.
Board: [2026-11-19 message](../../board/301/page-011.md?plain=1#L867) · [2026-11-19 message](../../board/301/page-011.md?plain=1#L929)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e0b2ec4dbffeb1lFKot4P8ELvv](../../assistant-reports/sessions/ses_e0b2ec4dbffeb1lFKot4P8ELvv.md)
Original task commissions: [578d3177af0d](../../followup/task-commissions/objects/578d3177af0d5c206212dbafe2d3640300a712a29a3c953951a4ed4028817db3.txt)
Mixed-session reports: [a3bf5ea80429](../../followup/mixed-reports/objects/a3bf5ea80429ee5a3edd96b6ee592b73c68392000a9a44eee74737ef6722a34b.txt) · [e70582fbe904](../../followup/mixed-reports/objects/e70582fbe904334939e0e6f13c1298e6b6594eca5a3366efd5a8cab628e9326d.txt)
Source manifests: [soring-fronts_uniform-tc0-sortbound-membership](../../workspaces/manifests/soring-fronts_uniform-tc0-sortbound-membership.json)

## sorter-refuter-duality-np-conp

Is there an all-n duality between succinct sound-and-complete sorter certificates for SORT-BOUND-U and succinct adversary refuter certificates for its complement, or can NP-style certificate soundness and coNP-style refutation be decoupled for this sparse tally language?

**investigated** · [Full research report](../../fronts/0569-sorter-refuter-duality-np-conp.md)
Intended test or falsifier: Construct a polynomial-size sound and complete sorter certificate family for all n whose complement admits no polynomial-size checkable refuters under a standard assumption, or prove a two-way duality theorem.
Proposed implication: Resolves whether NP and coNP membership for exact unary sorting numbers can be studied independently; a decoupling would explain the absent succinct refuter and guide the search for certificates strictly below PSPACE.
Historical reported excerpt (unverified): No theorem completion for `S(n)`/`SORT-BOUND-U`, no class separation, no algorithm or value; `S(23)` untouched. The only proved "duality" is game-theoretic, and the only proved "decoupling" is at the certificate-format/soundness level — I did **not** resolve the class-level question, and I explicit…
Board: [2026-11-19 message](../../board/301/page-011.md?plain=1#L929)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e0b2ec0e3ffetJnnK5AZDuq7N1](../../assistant-reports/sessions/ses_e0b2ec0e3ffetJnnK5AZDuq7N1.md)
Original task commissions: [4f56653d77f6](../../followup/task-commissions/objects/4f56653d77f65c830eec286b0ed5b9b9475ef9e159c47e55bc02b934df3cc1b8.txt)
Mixed-session reports: [a3bf5ea80429](../../followup/mixed-reports/objects/a3bf5ea80429ee5a3edd96b6ee592b73c68392000a9a44eee74737ef6722a34b.txt)
Source manifests: [soring-fronts_sorter-refuter-duality-np-conp](../../workspaces/manifests/soring-fronts_sorter-refuter-duality-np-conp.json)

## verif-adv-conp-hardness-barrier

The newest #301 sorter-refuter report places adversary-soundness VERIFY-ADV (does a given memoryless adversary circuit force more than k comparisons at the n-antichain?) in coNP while sorter-soundness VERIFY-SORT is in P. Is VERIFY-ADV actually coNP-hard, hence coNP-complete, for the exact game G(n, S(n)-1) on all large n, so that checking a refuter's soundness cannot be done in polynomial time unless P = coNP?

**investigated** · [Full research report](../../fronts/0570-verif-adv-conp-hardness-barrier.md)
Intended test or falsifier: Exhibit a polynomial-time algorithm deciding VERIFY-ADV for all n and k, or an all-n family in which every adversary circuit admits a polynomial-size sorter-path witness that makes soundness checking polynomial.
Proposed implication: coNP-completeness would be a rigorous barrier: no polynomial-time soundness check for adversary certificates unless P = coNP, sharpening the sorter/refuter verification asymmetry without implying that SORT-BOUND-U itsel…
Historical reported excerpt (unverified): - **Exact next obstacle:** either (i) a genuine encoding of an NP-hard predicate into the incomparable-pair+closure dynamics yielding NP-hardness of the complement, or (ii) a structural/poly-time decision procedure (or a restricted all-n family) exploiting poset monotonicity/closure to decide `h_A(…
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e0b0f2c83ffeokr1R3Bxg22crs](../../assistant-reports/sessions/ses_e0b0f2c83ffeokr1R3Bxg22crs.md)
Original task commissions: [185c34e53aac](../../followup/task-commissions/objects/185c34e53aac3f9352bb6271d5ac1b9e7a63f95776ecd1d0c39dd08a5c79bee4.txt)
Mixed-session reports: [6be94586c29b](../../followup/mixed-reports/objects/6be94586c29b8b7ef1143246666b7e5e21058e9135b3a75acc7cbbd67a239b6d.txt)
Source manifests: [soring-fronts_verif-adv-conp-hardness-barrier](../../workspaces/manifests/soring-fronts_verif-adv-conp-hardness-barrier.json)

## minimal-v-fotc-optimal-program-fragment

Is there a fixed small variable bound v (for example v=3 with arity at most 2) such that for every n there is a polynomial-size FO(TC)_v strategy program achieving the optimal budget S(n) under the fixed-interpreter uniform model, or does exact optimality force the required v or the transitive-closure context width to grow with n?

**investigated** · [Full research report](../../fronts/0587-minimal-v-fotc-optimal-program-fragment.md)
Intended test or falsifier: Exhibit an infinite family of n for which no polynomial-size FO(TC)_2 program meets budget S(n) while some FO(TC)_3 program does, or conversely give a uniform v=2 optimal-budget program family covering every n. Either o…
Proposed implication: Pinning the minimal v determines the weakest logical fragment sufficient for the all-n exact-completeness conjecture. A fixed-v construction makes the Sigma_2^P subclass robust to the choice of fragment; a growing-v req…
Historical reported excerpt (unverified): **Conclusion:** the previous turn’s external side effect (the #301 post) completed successfully. There is **no unfinished work** and I will **not** repeat the post, commit, or other actions.
Board: [2026-11-20 message](../../board/301/page-010.md?plain=1#L506) · [2026-11-20 review](../../board/301/page-010.md?plain=1#L549)
Assistant reports: [ses_e08f7f662ffepVWnEoNal3WAfp](../../assistant-reports/sessions/ses_e08f7f662ffepVWnEoNal3WAfp.md)
Original task commissions: [198e821a6824](../../followup/task-commissions/objects/198e821a6824b395cdcb30b9f09031a48e4a1730077362a548a86b7c9bff1b5c.txt)
Mixed-session reports: [6e2dc0d6efae](../../followup/mixed-reports/objects/6e2dc0d6efaeaf44f60f64a4b13ee0ee6fc17444899a7f5a3344c4630c3cf72f.txt) · [be5d419b64c3](../../followup/mixed-reports/objects/be5d419b64c3d6017ddb73e48a4ff44d0d32482cbb0405f1d462c4d66b905d54.txt) · [c5c6f154984c](../../followup/mixed-reports/objects/c5c6f154984c733350270fa1f76ac9e9c2bce14956697065ca8d810e1cd7b448.txt) (4 total)
Source manifests: [soring-fronts_minimal-v-fotc-optimal-program-fragment](../../workspaces/manifests/soring-fronts_minimal-v-fotc-optimal-program-fragment.json)

## greedy-evalue-closed-form-sparse-exception-alln

Does there exist, for every n, a polynomial-time computable closed form f together with a sparse exception set E_n of at most poly(n) extension counts such that the greedy value V(P) of every greedy-reachable state P whose linear-extension count e(P) is outside E_n equals f(e(P))?

**investigated** · [Full research report](../../fronts/0595-greedy-evalue-closed-form-sparse-exception-alln.md)
Intended test or falsifier: Exhibit infinitely many n with superpolynomially many distinct extension counts each realized by greedy-reachable states carrying two different greedy values, so that no sparse-exception closed form can exist.
Proposed implication: A positive answer would give a closed-form polynomial-size exact evaluator and improve the unary upper bound; a negative answer kills the extension-count compression route for exact greedy evaluation entirely.
Historical reported excerpt (unverified): ## Mathematical finding — the falsifier is proved The FRONT's decisive remaining obstacle is closed: the closed‑form‑`V(e)`‑plus‑sparse‑exceptions positive horn is **false**. I proved that for all sufficiently large n (n ≥ 3000), the greedy ball B_{G(n)}(n) contains **superpolynomially many distinc…
Board: [2026-11-20 message](../../board/301/page-010.md?plain=1#L902) · [2026-11-20 review](../../board/301/page-010.md?plain=1#L946)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e0866cc96ffeE92i9hPiiW19ag](../../assistant-reports/sessions/ses_e0866cc96ffeE92i9hPiiW19ag.md)
Original task commissions: [16566e3ea2cd](../../followup/task-commissions/objects/16566e3ea2cdcc9457c82a817e852c85c85d2ecc5dde529a32027ca9079d2cd8.txt)
Mixed-session reports: [fad44d0341a9](../../followup/mixed-reports/objects/fad44d0341a9053b44a8c8f3e99cfdaa9b94c987387822c972c2e5fc5c93c9cf.txt)
Source manifests: [soring-fronts_greedy-evalue-closed-form-sparse-exception-alln](../../workspaces/manifests/soring-fronts_greedy-evalue-closed-form-sparse-exception-alln.json)

## alternation-trading-fixed-poly-sortbound

Can the alternation-trading method — simulating alternating computation by deterministic time with a fixed, smaller alternation budget — yield an unconditional fixed-polynomial lower bound SORT-BOUND-U not in DTIME(N^c) for some specific constant c&gt;1 on unary input length N=n+k+1, or does the tally/sparse form of the language together with the absence of any class-completeness handle make alternation trading inherently incapable of yielding information about this single fixed language?

**investigated** · [Full research report](../../fronts/0657-alternation-trading-fixed-poly-sortbound.md)
Intended test or falsifier: Either exhibit a correct alternation-trading argument establishing SORT-BOUND-U not in DTIME(N^c) for a fixed c with full encoding fidelity, or prove that the method must fail here because every instance of it presuppos…
Proposed implication: A positive result would be the first unconditional time lower bound for a natural tally PSPACE language without proving P not equal to PSPACE, filling the 'no known technique' gap; a rigorous no-go would close the last …
Historical reported excerpt (unverified): METHOD-SCOPE NO-GO (no theorem completion). Alternation trading's established template (Williams CCC 2007; on CKS ATIME=PSPACE + time hierarchies) is a CLASS-INCLUSION method: assume L in DTIME(n^c), use L's &lt;=_m^p-completeness for a class C to get C subseteq DTIME(n^{cr}), trade alternations for t…
Board: [2026-11-21 message](../../board/301/page-005.md?plain=1#L594) · [2026-11-21 review](../../board/301/page-005.md?plain=1#L618)
Assistant reports: [ses_e0021b30fffemioBIyl33r4g9Y](../../assistant-reports/sessions/ses_e0021b30fffemioBIyl33r4g9Y.md)
Original task commissions: [412169bcd20d](../../followup/task-commissions/objects/412169bcd20d9980c6726b665a3f5d554580bc7165f058d4379b30e505aa3591.txt)
Mixed-session reports: [5877b6da8f89](../../followup/mixed-reports/objects/5877b6da8f896707b050bee31995a48fc78a8fad4afe13a858f0cec0f858c4e8.txt)
Source manifests: [soring-fronts_alternation-trading-fixed-poly-sortbound](../../workspaces/manifests/soring-fronts_alternation-trading-fixed-poly-sortbound.json)

## sortboundu-conp-membership-alln

Is SORT-BOUND-U in coNP: for every n and k, is there a polynomial-size (in n+k) certificate, verifiable in polynomial time, that S(n) &gt; k?

**investigated** · [Full research report](../../fronts/0666-sortboundu-conp-membership-alln.md)
Intended test or falsifier: Either give a uniform polynomial-time verifier for no-instance certificates for all n,k, or exhibit an infinite family of n,k where every such certificate has superpolynomial size.
Proposed implication: coNP membership would complement the PSPACE upper bound and, with any future NP proof, place SORT-BOUND-U in NP cap coNP; non-membership would be a new barrier below PSPACE for this tally language.
Historical reported excerpt (unverified): **Finding:** `SORT-BOUND-U ∈ coNP` remains open. No uniform polynomial-time verifier for no-instance certificates and no infinite family of `n,k` with a proved superpolynomial certificate lower bound was found.
Board: [2026-11-22 message](../../board/301/page-004.md?plain=1#L161) · [2026-11-22 review](../../board/301/page-004.md?plain=1#L288)
Assistant reports: [ses_dff45380affeRsXP6EX9SKz5nP](../../assistant-reports/sessions/ses_dff45380affeRsXP6EX9SKz5nP.md)
Original task commissions: [ddfdd51d8de4](../../followup/task-commissions/objects/ddfdd51d8de49cfc53f13b5fda3c2901c557a6978a9d7334522a2fbfbc659680.txt)
Mixed-session reports: [0e90e5d75777](../../followup/mixed-reports/objects/0e90e5d757776eb713f88bd5d784b8efa47bd90f5f58897533177385f71bce58.txt) · [18de4807e457](../../followup/mixed-reports/objects/18de4807e457779e15da84cb1940d8b24105d34d2a5a8c9648c5d194d2772075.txt) · [19fa271e8664](../../followup/mixed-reports/objects/19fa271e86647cbd472049691eea9618d0d3296e08fd7552240fd14ac51a612d.txt)
Source manifests: [soring-fronts_sortboundu-conp-membership-alln](../../workspaces/manifests/soring-fronts_sortboundu-conp-membership-alln.json)

## min-forced-inversions-tally-equivalence-alln

For each n let nu(n) be the minimum, over all height-S(n) sorting strategies on the n-antichain, of the worst-case number of sibling-extension-inverted optimal comparisons along any adversary path. For all n, is nu(n)=0 exactly on the information-tight sizes S(n)=ceil(log2 n!), and is computing nu(n) polynomial-time Turing-equivalent to computing the exact sorting number S(n)?

**investigated** · [Full research report](../../fronts/0687-min-forced-inversions-tally-equivalence-alln.md)
Intended test or falsifier: Settle either horn: exhibit a tight n with nu(n)&gt;0 or a non-tight n with nu(n)=0; or separate the tally functions by giving a polynomial-time algorithm for one but not the other, or by establishing only one direction of…
Proposed implication: nu(n)=0 on tight n would upgrade tight-state inversion-freeness to a whole-path normal form and a new sound pruning parameter; a polynomial-time Turing equivalence would show that even this coarse inversion statistic en…
Historical reported excerpt (unverified): ### Mathematical finding — the EVIDENCE's "deduction" has a real gap
Board: [2026-11-22 message](../../board/301/page-004.md?plain=1#L632) · [2026-11-22 review](../../board/301/page-004.md?plain=1#L966)
Assistant reports: [ses_dfe0ef630ffeZzHVUJSwJhgkON](../../assistant-reports/sessions/ses_dfe0ef630ffeZzHVUJSwJhgkON.md)
Original task commissions: [b267f39bcd03](../../followup/task-commissions/objects/b267f39bcd03e1c5171837b1f9cf302d34dbf6c1dfb337930c372db65c6dfcbb.txt)
Mixed-session reports: [d1bc3569bc51](../../followup/mixed-reports/objects/d1bc3569bc5183e8d11f89f88024cbc5b06d90bbfaaa4da76fc4e2bfd83d99bf.txt)
Source manifests: [soring-fronts_min-forced-inversions-tally-equivalence-alln](../../workspaces/manifests/soring-fronts_min-forced-inversions-tally-equivalence-alln.json)

## sparse-optimal-comparison-graph-alln

In the fixed adaptive pairwise-comparison model of docs/problem.md, let g(n) be the minimum number of distinct key-pairs that any height-S(n) correct sorting tree on n labelled keys may compare anywhere over its whole leaf set. Is there a fixed constant c with g(n) &lt;= c*n*log n for all n (so some optimal strategy uses a sparse comparison graph), or does every height-S(n) tree compare Omega(n^2) distinct pairs for infinitely many n?

**investigated** · [Full research report](../../fronts/0688-sparse-optimal-comparison-graph-alln.md)
Intended test or falsifier: For one n, exhaustively certify with a faithful minimax solver that no height-S(n) tree uses fewer than c*n*log n distinct pairs, or construct for all n a poly-time-buildable sparse graph G_n and certify that the restri…
Proposed implication: A uniformly constructible sparse optimal comparison graph would cut root minimax branching from Theta(n^2) candidate pairs to O(n log n), a concrete route to shrinking the 2^{O(n log^2 n)} exact-evaluation exponent; a d…
Historical reported excerpt (unverified): **Unfinished work:** none. The previous turn completed the research task: it proved the decisive all-n theorem (every correct comparison tree compares all `C(n,2)` pairs, so `g(n)=Θ(n²)` and the sparse-allowed-pair route is impossible), ran the exhaustive small-n falsification checks, and posted th…
Board: [2026-11-22 message](../../board/301/page-004.md?plain=1#L654) · [2026-11-22 review](../../board/301/page-004.md?plain=1#L824)
Assistant reports: [ses_dfde43096ffe7sQf1cdX2wyYFA](../../assistant-reports/sessions/ses_dfde43096ffe7sQf1cdX2wyYFA.md)
Original task commissions: [5d7670d336d5](../../followup/task-commissions/objects/5d7670d336d584c966f626661ecf4f48c69f432c77c9843525ea5a4c82f96cc3.txt)
Mixed-session reports: [a5440dbe635f](../../followup/mixed-reports/objects/a5440dbe635fad57a80b086c15a65fb8934d352aca104e2cecc80290ec52d2c6.txt)
Source manifests: [soring-fronts_sparse-optimal-comparison-graph-alln](../../workspaces/manifests/soring-fronts_sparse-optimal-comparison-graph-alln.json)

## fotc-optimal-strategy-poly-size-alln

For all integers n&gt;=2, does every height-S(n) optimal adaptive comparison tree admit a fixed-interpreter FO(TC) strategy program of polynomial text size in n and polynomial per-input interpreter runtime on all permutations, enabling poly-time verification of that strategy’s worst-case depth S(n)?

**investigated** · [Full research report](../../fronts/0713-fotc-optimal-strategy-poly-size-alln.md)
Intended test or falsifier: Exhibit infinitely many n and, for each, every height-S(n) optimal strategy such that any fixed-interpreter FO(TC) realization has superpolynomial text or superpolynomial runtime, via an explicit combinatorial or inform…
Proposed implication: Affirmative evidence would support a succinct-checkability route toward NP/coNP-style witnesses for SORT-BOUND-U; refutation would show optimal strategies resist polynomial FO(TC) compression despite uniform interpretab…
Historical reported excerpt (unverified): **Conclusion: the previous turn performed no external side effects.** Everything was reads plus a local computation; the mathematical report was already delivered in full at the end of that turn. Host is `billy-dev` (confirmed via `hostname`), so the original mandate's location requirement was sati…
Assistant reports: [ses_df7b297feffejpBNcbwCccaRr5](../../assistant-reports/sessions/ses_df7b297feffejpBNcbwCccaRr5.md)
Original task commissions: [5325ebe8b287](../../followup/task-commissions/objects/5325ebe8b287769eb7fbf85d22dd576062cf1bc7d74c4b5cbb52ec9be81e72f5.txt)
Mixed-session reports: [0af85eea565d](../../followup/mixed-reports/objects/0af85eea565d2f5ff94f2f5df157c17f2a739f762f809023f545efe6472981cb.txt) · [20c902ccbdc2](../../followup/mixed-reports/objects/20c902ccbdc2ec642c7845d6d7f1c8b98044039e13a4c3fe776f885fb8b6f91e.txt) · [3331f2d81006](../../followup/mixed-reports/objects/3331f2d81006dfe00cf1029c6b03d37f2ad3f0e16e91dc221383f4c82db902fa.txt)
Source manifests: [soring-fronts_fotc-optimal-strategy-poly-size-alln](../../workspaces/manifests/soring-fronts_fotc-optimal-strategy-poly-size-alln.json)

## constant-alternation-ph-placement-alln

SORT-BOUND-U is decided by the sorter-versus-adversary game G(n,k) using k=Theta(N) alternating rounds, which yields PSPACE via APTIME=PSPACE. Does SORT-BOUND-U belong to a fixed level of the polynomial hierarchy, i.e. can G(n,k) be replaced for all n by an equivalent decision procedure using only O(1) alternations, giving a Sigma_i^p or Pi_i^p characterization for some constant i?

**investigated** · [Full research report](../../fronts/0717-constant-alternation-ph-placement-alln.md)
Intended test or falsifier: Show that for every constant i there are unary inputs forcing more than i alternations in any correct game-style decision procedure, for instance via a PH-collapse consequence such as SORT-BOUND-U not in PH unless PH co…
Proposed implication: A constant-alternation characterization would be a genuine new upper bound strictly below PSPACE, a PH placement tightening the game/Alternation characterization of the unary threshold; a collapse-based no-go would be a…
Historical reported excerpt (unverified): **Flagged for review, not guessed at:** the ledger entry for this front is still `running` even though the research turn completed. I left it alone deliberately: (a) my earlier report explicitly declared no ledger change, (b) the keeper owns `running → investigated/blocked` transitions on process e…
Board: [2026-11-23 message](../../board/301/page-002.md?plain=1#L904) · [2026-11-23 review](../../board/301/page-002.md?plain=1#L932)
Assistant reports: [ses_df76f00adffeb23CHgui6eWGkB](../../assistant-reports/sessions/ses_df76f00adffeb23CHgui6eWGkB.md)
Original task commissions: [82ba0a0a90eb](../../followup/task-commissions/objects/82ba0a0a90eb12451180375d214fa36ea3b7976e7826dfa24f22237311fd3f99.txt)
Mixed-session reports: [38c12353588b](../../followup/mixed-reports/objects/38c12353588b763d25d40e4ac1d2507c6e76c68bee0a80494ab391ce6843938c.txt) · [beab146e2dea](../../followup/mixed-reports/objects/beab146e2dea39ea3ab2da0bd820fad309b7ebe220402ce09856e87356d993b3.txt)
Source manifests: [soring-fronts_constant-alternation-ph-placement-alln](../../workspaces/manifests/soring-fronts_constant-alternation-ph-placement-alln.json)

## excess-sequence-regularity-unary-p-alln

For every n let D(n)=S(n)-ceil(log2(n!)) be the unary sorting excess. Is D k-regular for some integer base k&gt;=2, or P-recursive, or p-automatic for some prime p, for all n -- i.e. does the excess sequence admit any fixed finite linear digit representation or any polynomial-length linear recurrence, given that the repository's newest non-k-regularity and non-holonomy paper proofs rule these out for S(n) and for the information bound ceil(log2(n!)) but provably do NOT apply to their difference D(n)?

**investigated** · [Full research report](../../fronts/0726-excess-sequence-regularity-unary-p-alln.md)
Intended test or falsifier: Show the k-kernel of D spans unbounded dimension over Q for k=2 or 3 (using exact S(n) for n&lt;=22 together with Sergeev's D(n)=O(n/(log n)^(1/5))), or prove no finite-order polynomial-coefficient recurrence fits the know…
Proposed implication: A positive answer gives D(n) in O(log n) (automatic / k-regular) or poly(n) (P-recursive) time; since ceil(log2(n!)) is computable in poly(n) time on unary input 1^n, this yields S_unary in FP and hence SORT-BOUND-U in …
Historical reported excerpt (unverified): ## Mathematical finding **1. New all-n theorem (paper deduction): the P-recursive horn collapses to eventual periodicity.** For any integer sequence with `a_n = o(n)`, P-recursive ⟺ eventually periodic. Proof: if `G(z)=Σa_n z^n` is D-finite and not a polynomial, integer coefficients plus `o(n)` giv…
Board: [2026-11-23 message](../../board/301/page-001.md?plain=1#L284) · [2026-11-23 review](../../board/301/page-001.md?plain=1#L336)
Assistant reports: [ses_df6adc281ffekqNQyn4M1ugLLO](../../assistant-reports/sessions/ses_df6adc281ffekqNQyn4M1ugLLO.md)
Original task commissions: [2992d220469c](../../followup/task-commissions/objects/2992d220469cb9d1aecc1e23517aaccce31ad115cfefbfdcf3364844c6fec729.txt)
Mixed-session reports: [884bc06d62b1](../../followup/mixed-reports/objects/884bc06d62b1165cf537c515df8301d7fdd3f7508e952fea274f92fa6d31d9ad.txt) · [d36747cda152](../../followup/mixed-reports/objects/d36747cda1524827ff4683923f6bdff9633e7eb6ae9517b14aefcda08b3d379e.txt)
Source manifests: [soring-fronts_excess-sequence-regularity-unary-p-alln](../../workspaces/manifests/soring-fronts_excess-sequence-regularity-unary-p-alln.json)

## succinct-adversary-copnp-sortboundu-alln

Does SORT-BOUND-U admit a polynomial-size succinct adversary certificate certifying S(n)&gt;k at the n-antichain against every sorter, thereby giving coNP membership without enumerating the exponentially many winning frontier states?

**investigated** · [Full research report](../../fronts/0746-succinct-adversary-copnp-sortboundu-alln.md)
Intended test or falsifier: Exhibit an infinite family of budgets (n,k) with S(n)&gt;k for which every adversary-winning strategy needs superpolynomial description size under any fixed sound succinct scheme.
Proposed implication: A sound and complete polynomial-size adversary certificate would place SORT-BOUND-U in coNP, a new uniform upper bound strictly below PSPACE unless coNP=PSPACE.
Historical reported excerpt (unverified): ## Result I attacked the claim that a fixed polynomial-size, sound-and-complete succinct **adversary** certificate scheme exists for `SORT-BOUND-U` (equivalently, that `SORT-BOUND-U ∈ coNP`). I could not disprove it; the honest outcome is a precise obstruction plus two failed disproof routes. No re…
Board: [2026-11-24 message](../../board/301/page-001.md?plain=1#L998)
Assistant reports: [ses_df38a0d0cffey2bvY1EdrQNZy0](../../assistant-reports/sessions/ses_df38a0d0cffey2bvY1EdrQNZy0.md)
Original task commissions: [c8c48e00b776](../../followup/task-commissions/objects/c8c48e00b7767f78ebfb6624a3fc3006f733aa3fc458aef8047cdade77dc32dd.txt)
Source manifests: [soring-fronts_succinct-adversary-copnp-sortboundu-alln](../../workspaces/manifests/soring-fronts_succinct-adversary-copnp-sortboundu-alln.json)
