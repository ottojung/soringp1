# Profiles, decks and lookahead

[Catalogue home](../README.md) · [Evidence status guide](../../RESULTS.md)

Status is the original workflow label, not mathematical proof. Linked messages may contain corrections or rejected claims.

## linear-extension-sampling-lower-bound

Does approximate uniform sampling of linear extensions of states on any optimal sorting strategy require super-polynomial time for all-n, creating a barrier to certain randomized certificate approaches?

**investigated** · [Full research report](../../fronts/0052-linear-extension-sampling-lower-bound.md)
Source manifests: [soring-fronts_linear-extension-sampling-lower-bound](../../workspaces/manifests/soring-fronts_linear-extension-sampling-lower-bound.json)

## alln-ceiling-loss-invariant

For every all-n complete family of sound certificates for SORT-BOUND-U (framed or general join/intersection), let L(n) be the average ceiling rounding loss L(n)= (sum of per-stage ceil(log2 q_i)-log2 n!) / n over an optimal stage factorization; must liminf_{n-&gt;∞} L(n) &gt; 0, or can some family achieve L(n)=o(1)?

**investigated** · [Full research report](../../fronts/0071-alln-ceiling-loss-invariant.md)
Board: [2026-10-30 message](../../board/301/page-043.md?plain=1#L425)
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_alln-ceiling-loss-invariant](../../workspaces/manifests/soring-fronts_alln-ceiling-loss-invariant.json)

## antichain-root-invariant-separation

Does there exist an all-n invariant I(P) computable from a reachable poset P (with P reachable from antichain) that is strictly stronger than the information bound in the sense that for infinitely many optimal-decision paths from antichain, I forces &gt;= c*S(n) comparisons while log2(e(P)) is within o(n) of its maximum for P, for some fixed c&gt;1/ something or just strictly separating?

**investigated** · [Full research report](../../fronts/0083-antichain-root-invariant-separation.md)
Board: [2026-10-30 message](../../board/301/page-041.md?plain=1#L27)
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_antichain-root-invariant-separation](../../workspaces/manifests/soring-fronts_antichain-root-invariant-separation.json)

## coarser-sound-complete-invariant

Does there exist for all n a coarser equivalence relation on comparison histories (weaker than poset relabeling isomorphism) that is both sound for the minimax value F(P) and has only exp(O(n log n / log log n)) or polynomial classes per depth, or is every such all-n invariant exponentially large?

**investigated** · [Full research report](../../fronts/0085-coarser-sound-complete-invariant.md)
Historical reported excerpt: **Mathematical finding 1 — falsifier's lower-bound disjunct refuted (deduction).** The equivalence `P ~ Q ⇔ F(P) = F(Q)` on reachable states is sound for the minimax value by definition, strictly coarser than relabeling isomorphism (F is relabelling-invariant, already a deduction in `docs/research-…
Board: [2026-10-30 message](../../board/301/page-041.md?plain=1#L229) · [2026-10-31 message](../../board/301/page-041.md?plain=1#L301) · [2026-10-31 message](../../board/301/page-041.md?plain=1#L317) · [2026-10-31 message](../../board/301/page-041.md?plain=1#L333) · [2026-10-31 message](../../board/301/page-041.md?plain=1#L341)
Additional board mentions: 2 (use front lookup for exact links)
Mixed-session reports: [13ec1a6f6ef7](../../followup/mixed-reports/objects/13ec1a6f6ef728c8a70f9cc94053ae2bb7a46aff7a097756e7561b2b2d2d1c9d.txt) · [3c8bc34c24c1](../../followup/mixed-reports/objects/3c8bc34c24c1ca25ece5361765c290d788243251ab2c1db97f6119a4dc5dd5a2.txt) · [e70582fbe904](../../followup/mixed-reports/objects/e70582fbe904334939e0e6f13c1298e6b6594eca5a3366efd5a8cab628e9326d.txt)
Source manifests: [soring-fronts_coarser-sound-complete-invariant](../../workspaces/manifests/soring-fronts_coarser-sound-complete-invariant.json)

## linear-extension-oracle-barrier

For all sufficiently large n, must every uniform deterministic algorithm that achieves exact height S(n) by local minimax choices consult a linear-extension counting oracle on exponentially many distinct posets P encountered on some height-optimal play from the n-antichain?

**blocked** · [Full research report](../../fronts/0090-linear-extension-oracle-barrier.md)
Additional board mentions: 3 (use front lookup for exact links)
Source manifests: [soring-fronts_linear-extension-oracle-barrier](../../workspaces/manifests/soring-fronts_linear-extension-oracle-barrier.json)

## linear-extension-count-obstruction

Can the #P-hardness of counting linear extensions be encoded into the minimax height evaluation for some infinite family of partial orders reachable from the antichain, establishing that computing F(P) is #P-hard on the SORT-BOUND-U state graph without reducing arbitrary posets directly?

**blocked** · [Full research report](../../fronts/0115-linear-extension-count-obstruction.md)
Board: [2026-10-31 message](../../board/301/page-039.md?plain=1#L365) · [2026-10-31 message](../../board/301/page-039.md?plain=1#L373) · [2026-10-31 message](../../board/301/page-039.md?plain=1#L381) · [2026-10-31 message](../../board/301/page-039.md?plain=1#L389) · [2026-10-31 message](../../board/301/page-039.md?plain=1#L397) (8 total; use search for all)
Additional board mentions: 3 (use front lookup for exact links)
Source manifests: [soring-fronts_linear-extension-count-obstruction](../../workspaces/manifests/soring-fronts_linear-extension-count-obstruction.json)

## profile-collision-obstruction

For the budgeted minimax search over the antichain root, is there an infinite all-n family of reachable partial orders P_n that remain pairwise distinguishable for the exact value F(P) but become indistinguishable under every polynomial-time computable canonical profile map that is sound for the recurrence, forcing superpolynomial state lists to compute S(n) exactly?

**blocked** · [Full research report](../../fronts/0171-profile-collision-obstruction.md)
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_profile-collision-obstruction](../../workspaces/manifests/soring-fronts_profile-collision-obstruction.json)

## finite-invariant-incompleteness-f

For every finite list of computable poset invariants (I1,...,Ik), does there exist an infinite family of pairwise nonisomorphic posets with identical values on all Ii but strictly different minimax sorting costs F(P) != F(Q)?

**investigated** · [Full research report](../../fronts/0184-finite-invariant-incompleteness-f.md)
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_finite-invariant-incompleteness-f](../../workspaces/manifests/soring-fronts_finite-invariant-incompleteness-f.json)

## antichain-cover-prefix-invariant

For every n&gt;=2 and every comparison tree of height k sorting all permutations of n distinct labelled keys, let P_t be the poset after t comparisons on some root-to-leaf path; define C(P_t) as the number of cover relations in the transitive reduction of P_t. Must we have C(P_t) &gt;= something stronger than d(P_t)+F(P_t)&lt;=S(n) for all-t with no path achieving total order using only 'cover-sparse' posets at large t when k is near S(n)? Or more precisely: is there an all-n lower bound C(P_t) &gt;= t + delta(n,t) that is violated only if k is much larger than the best known S(n), forcing a comparison beyond the information/cover-counting of general posets?

**investigated** · [Full research report](../../fronts/0261-antichain-cover-prefix-invariant.md)
Historical reported excerpt: **Mathematical finding (deduction): no all-n cover-density lower bound of the form C(P_t) &gt;= t + δ exists.**
Board: [2026-11-04 message](../../board/301/page-029.md?plain=1#L359) · [2026-11-04 message](../../board/301/page-029.md?plain=1#L367) · [2026-11-04 message](../../board/301/page-029.md?plain=1#L375)
Source manifests: [soring-fronts_antichain-cover-prefix-invariant](../../workspaces/manifests/soring-fronts_antichain-cover-prefix-invariant.json)

## co-np-refuter-local-invariant-completeness

Is there a polynomial-time verifiable local refuter invariant I(P,c,b) on partial orders P, comparison c, and remaining budget b such that for all n and k&lt;S(n), I certifies from the antichain root that every adaptive sorter fails within k comparisons, without enumerating winning-frontier classes?

**investigated** · [Full research report](../../fronts/0310-co-np-refuter-local-invariant-completeness.md)
Source manifests: [soring-fronts_co-np-refuter-local-invariant-completeness](../../workspaces/manifests/soring-fronts_co-np-refuter-local-invariant-completeness.json)

## modular-profile-succinct-characterization

For all n, does the exact minimax value S(n) admit a characterization by a polynomial-size system of modular/counting constraints on profile vectors of total extensions along every optimal comparison path, checkable without reconstructing the full comparison decision tree?

**investigated** · [Full research report](../../fronts/0311-modular-profile-succinct-characterization.md)
Source manifests: [soring-fronts_modular-profile-succinct-characterization](../../workspaces/manifests/soring-fronts_modular-profile-succinct-characterization.json)

## linear-extension-parameter-exact-eval

For every finite poset P on n elements, is the exact minimax comparison number F(P) computable in time polynomial in n + e(P), where e(P) is the number of linear extensions, so that the n-element antichain would be evaluated in 2^{O(n log n)} time?

**investigated** · [Full research report](../../fronts/0326-linear-extension-parameter-exact-eval.md)
Historical reported excerpt: ## Mathematical finding: the front’s stated evidence is unsound; no falsifier
Board: [2026-11-07 message](../../board/301/page-023.md?plain=1#L547)
Assistant reports: [ses_e47f2b672ffeNNrKC4rRKP6ohV](../../assistant-reports/sessions/ses_e47f2b672ffeNNrKC4rRKP6ohV.md)
Original task commissions: [f874095cb933](../../followup/task-commissions/objects/f874095cb933b1cc30226f1e873a83613d6804f0be0d1ca089bb88902128657e.txt)
Source manifests: [soring-fronts_linear-extension-parameter-exact-eval](../../workspaces/manifests/soring-fronts_linear-extension-parameter-exact-eval.json)

## antichain-lookahead-depth

Is there an absolute constant t such that the depth-t extension-count lookahead L_t(A_n) equals the exact sorting number S(n) for every n, where L_0(P)=ceil(log2 e(P)) and L_{t+1}(P)=1+min over incomparable pairs max(L_t(P+x&lt;y), L_t(P+y&lt;x))?

**investigated** · [Full research report](../../fronts/0390-antichain-lookahead-depth.md)
Board: [2026-11-08 message](../../board/301/page-021.md?plain=1#L923) · [2026-11-08 message](../../board/301/page-021.md?plain=1#L985)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e435b068fffe6y4Co2XMIXW2IW](../../assistant-reports/sessions/ses_e435b068fffe6y4Co2XMIXW2IW.md)
Original task commissions: [9a5eafa3037d](../../followup/task-commissions/objects/9a5eafa3037d999929211c0b4263c9e8e95233f94a98d08879049cdd6d901238.txt)
Mixed-session reports: [b717dfcfe6a8](../../followup/mixed-reports/objects/b717dfcfe6a82c452ccc51a89fa03fb91e5f73b3299ac958f2c0bf90139dc385.txt)
Source manifests: [soring-fronts_antichain-lookahead-depth](../../workspaces/manifests/soring-fronts_antichain-lookahead-depth.json)

## lookahead-flatness-sharp-threshold

Is the first lookahead depth at which the extension-count hierarchy L_t(A_n) exceeds the information bound C(n) exactly floor(n/2)+1 for every n with E(n)&gt;0, and does L_t then stay at C(n) for all smaller t?

**investigated** · [Full research report](../../fronts/0396-lookahead-flatness-sharp-threshold.md)
Historical reported excerpt: ## Mathematical finding
Board: [2026-11-08 message](../../board/301/page-020.md?plain=1#L89) · [2026-11-08 message](../../board/301/page-020.md?plain=1#L157)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e433029edffesXSxfiqU4IcOds](../../assistant-reports/sessions/ses_e433029edffesXSxfiqU4IcOds.md)
Original task commissions: [734350614b95](../../followup/task-commissions/objects/734350614b9556e0611b1d003bba49c122d2e804a2b62246b3f631dec752edc3.txt)
Source manifests: [soring-fronts_lookahead-flatness-sharp-threshold](../../workspaces/manifests/soring-fronts_lookahead-flatness-sharp-threshold.json)

## lookahead-convergence-depth

Let L_t be the depth-t extension-count lookahead hierarchy with L_0(P)=ceil(log2 e(P)) and t*(n)=min{t : L_t(A_n)=S(n)}. Is t*(n)-floor(n/2) bounded by an absolute constant for every n with E(n)&gt;0, or does this convergence offset grow without bound along an infinite family?

**investigated** · [Full research report](../../fronts/0397-lookahead-convergence-depth.md)
Historical reported excerpt: **Conclusion**
Board: [2026-11-08 message](../../board/301/page-020.md?plain=1#L170) · [2026-11-08 message](../../board/301/page-020.md?plain=1#L210)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e4302d1b0ffe7aendq7X0aj8FZ](../../assistant-reports/sessions/ses_e4302d1b0ffe7aendq7X0aj8FZ.md)
Original task commissions: [fd7a6eebdd03](../../followup/task-commissions/objects/fd7a6eebdd03824db0660e5c561730645d297bc27f81abee1fae928b7cfe8cb5.txt)
Source manifests: [soring-fronts_lookahead-convergence-depth](../../workspaces/manifests/soring-fronts_lookahead-convergence-depth.json)

## height-two-exact-child-count-deck-completeness

For all finite height-at-most-two posets P and Q, if the multiset of unordered exact child linear-extension count pairs over all incomparable pairs agrees for P and Q, must the exact minimax values F(P) and F(Q) agree?

**investigated** · [Full research report](../../fronts/0470-height-two-exact-child-count-deck-completeness.md)
Historical reported excerpt: ## Finding
Board: [2026-11-10 message](../../board/301/page-017.md?plain=1#L484) · [2026-11-10 message](../../board/301/page-017.md?plain=1#L601)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e3d9506b6ffeGGSDluusoedYDB](../../assistant-reports/sessions/ses_e3d9506b6ffeGGSDluusoedYDB.md)
Original task commissions: [5b6dae553ecd](../../followup/task-commissions/objects/5b6dae553ecdbc8f7f7ef45bd5c55306f5d07757b174e86f6edaf151802ffd25.txt)
Source manifests: [soring-fronts_height-two-exact-child-count-deck-completeness](../../workspaces/manifests/soring-fronts_height-two-exact-child-count-deck-completeness.json)

## height-two-deck-complete-invariant

For every finite height-at-most-two poset P and Q, does equality of the multiset of unordered exact child linear-extension count pairs over all incomparable pairs imply that P and Q are isomorphic or order-dual?

**investigated** · [Full research report](../../fronts/0498-height-two-deck-complete-invariant.md)
Assistant reports: [ses_e3b1c0647ffeOMi4G3Ni0kA5Ls](../../assistant-reports/sessions/ses_e3b1c0647ffeOMi4G3Ni0kA5Ls.md)
Original task commissions: [77f6423d385f](../../followup/task-commissions/objects/77f6423d385f3fa7ece9b53240307596b9c94576e8f8e9342462226b9689e11c.txt)
Source manifests: [soring-fronts_height-two-deck-complete-invariant](../../workspaces/manifests/soring-fronts_height-two-deck-complete-invariant.json)

## sublinear-window-lookahead-attainment

Is there a universal constant c&lt;1 such that for every n some comparison strategy that at each state may inspect only the subposet induced on at most c*n chosen key elements (together with n and the remaining budget) still attains worst-case height S(n), or does every height-S(n) strategy necessarily inspect linearly many elements of some reachable state for infinitely many n?

**investigated** · [Full research report](../../fronts/0542-sublinear-window-lookahead-attainment.md)
Historical reported excerpt: ## Conclusion of this recovery pass
Board: [2026-11-19 message](../../board/301/page-013.md?plain=1#L308)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e0eb1575fffec3zbg1XDtPRKsY](../../assistant-reports/sessions/ses_e0eb1575fffec3zbg1XDtPRKsY.md)
Original task commissions: [b848d09e83f0](../../followup/task-commissions/objects/b848d09e83f02d5c1cf67665d09b20d2dd1e5c5727fd50da13b0dd866f0e6358.txt)
Mixed-session reports: [a9c10f74712b](../../followup/mixed-reports/objects/a9c10f74712b26d4e38775749d484417fbb5a3a6161b7ce876b8091dc0da5383.txt) · [b4f721d1c1af](../../followup/mixed-reports/objects/b4f721d1c1af1ca88b6c58da0d5a2815175aa36c7a97c7821e33c93167e75108.txt)
Source manifests: [soring-fronts_sublinear-window-lookahead-attainment](../../workspaces/manifests/soring-fronts_sublinear-window-lookahead-attainment.json)

## child-deck-minimax-soundness-reachable

For every n, is the exact minimax continuation cost F(P) a function of the child extension-count deck D(P), the multiset over incomparable pairs of the unordered pair {e(P+x&lt;y), e(P+y&lt;x)}, for every poset state P lying on some height-S(n) optimal play from the n-antichain; and does this extend to all finite posets?

**investigated** · [Full research report](../../fronts/0573-child-deck-minimax-soundness-reachable.md)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e0aea70f8ffe4a0svTDoB3qCse](../../assistant-reports/sessions/ses_e0aea70f8ffe4a0svTDoB3qCse.md)
Original task commissions: [db59a987f148](../../followup/task-commissions/objects/db59a987f148d887312cd951f973120997a12a56b66021c10bab6aeb89248a5b.txt)
Mixed-session reports: [5dccbc668609](../../followup/mixed-reports/objects/5dccbc6686090e6ea7d8851aef4eab2e3fbbe8f3312ef0a7a6c25424bbee8920.txt) · [98ae55cd0b89](../../followup/mixed-reports/objects/98ae55cd0b895cf5e2f0bcba51b7b1a8c20c23b97b00c3ec6b7dc801f8214829.txt)
Source manifests: [soring-fronts_child-deck-minimax-soundness-reachable](../../workspaces/manifests/soring-fronts_child-deck-minimax-soundness-reachable.json)

## optimal-play-deck-class-polynomial

For every n, is the number of distinct child extension-count decks among poset states reachable on some height-S(n) optimal comparison strategy from the n-antichain bounded by a polynomial in n, even in regimes where the number of poset isomorphism classes on optimal play is believed or known to be superpolynomial?

**investigated** · [Full research report](../../fronts/0574-optimal-play-deck-class-polynomial.md)
Historical reported excerpt: ## Verdict
Board: [2026-11-19 message](../../board/301/page-010.md?plain=1#L110) · [2026-11-19 review](../../board/301/page-010.md?plain=1#L132) · [2026-11-19 message](../../board/301/page-010.md?plain=1#L157)
Additional board mentions: 3 (use front lookup for exact links)
Assistant reports: [ses_e0aea6f26ffepDKG7EgnRfGLLD](../../assistant-reports/sessions/ses_e0aea6f26ffepDKG7EgnRfGLLD.md)
Original task commissions: [d0deb16555c2](../../followup/task-commissions/objects/d0deb16555c2c467bff9429fdbef51d2af30eda8a4dd49f013629557f05af040.txt)
Mixed-session reports: [5dccbc668609](../../followup/mixed-reports/objects/5dccbc6686090e6ea7d8851aef4eab2e3fbbe8f3312ef0a7a6c25424bbee8920.txt) · [98ae55cd0b89](../../followup/mixed-reports/objects/98ae55cd0b895cf5e2f0bcba51b7b1a8c20c23b97b00c3ec6b7dc801f8214829.txt) · [d3e7f3a2e79f](../../followup/mixed-reports/objects/d3e7f3a2e79fd41c37a7d5d3c89685293cbc252ddc78006f88238766aed08962.txt)
Source manifests: [soring-fronts_optimal-play-deck-class-polynomial](../../workspaces/manifests/soring-fronts_optimal-play-deck-class-polynomial.json)

## deck-child-closure-alln

For every n, define R(n) as the set of child extension-count decks D(Q) of all poset states Q reachable from the n-antichain by any comparison sequence staying within the remaining optimal budget (so every Q lies on some correct height-S(n) play). Is R(n) closed under taking children: for every reachable state P and incomparable pair {x,y} with child Q=P+x&lt;y, is D(Q) itself a member of R(n)? Decide for all sufficiently large n or exhibit an explicit failing instance.

**investigated** · [Full research report](../../fronts/0576-deck-child-closure-alln.md)
Historical reported excerpt: ### Result: child-closure is **FALSE** — explicit n=4 falsifier
Board: [2026-11-19 message](../../board/301/page-010.md?plain=1#L175) · [2026-11-19 message](../../board/301/page-010.md?plain=1#L197) · [2026-11-19 message](../../board/301/page-010.md?plain=1#L267)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e0abb7e06ffeP6VPvKgA5qf5vT](../../assistant-reports/sessions/ses_e0abb7e06ffeP6VPvKgA5qf5vT.md)
Original task commissions: [d45c022ae292](../../followup/task-commissions/objects/d45c022ae292194fead60e266befc5d483bad5ff7b938bd2661753b0d95dc626.txt)
Mixed-session reports: [d3e7f3a2e79f](../../followup/mixed-reports/objects/d3e7f3a2e79fd41c37a7d5d3c89685293cbc252ddc78006f88238766aed08962.txt)
Source manifests: [soring-fronts_deck-child-closure-alln](../../workspaces/manifests/soring-fronts_deck-child-closure-alln.json)

## deck-optimal-move-determination-alln

Does the child extension-count deck D(P) determine the minimax-optimal incomparable-pair set O(P) = {{x,y}: F(P)=1+max(F(P+x&lt;y),F(P+y&lt;x))}, for all n, both over arbitrary posets and over states reachable from the n-antichain on optimal play? Decide or exhibit an explicit pair P,Q with D(P)=D(Q) but O(P)!=O(Q).

**investigated** · [Full research report](../../fronts/0578-deck-optimal-move-determination-alln.md)
Historical reported excerpt: ## Outcome: NO — the deck does not determine the optimal move set
Board: [2026-11-19 message](../../board/301/page-010.md?plain=1#L324)
Additional board mentions: 3 (use front lookup for exact links)
Assistant reports: [ses_e0aa829d2ffeoDJMHndj3ZXvEN](../../assistant-reports/sessions/ses_e0aa829d2ffeoDJMHndj3ZXvEN.md)
Original task commissions: [47bfed412ffc](../../followup/task-commissions/objects/47bfed412ffcab9bb2084d3424a4a0d8d67b5994b4387aa4b85454f4e5895fe5.txt)
Mixed-session reports: [7490f37c06ac](../../followup/mixed-reports/objects/7490f37c06ac6bb33455f62f12b32a810b62524ce4b7a9347f2d34a18ff504c4.txt)
Source manifests: [soring-fronts_deck-optimal-move-determination-alln](../../workspaces/manifests/soring-fronts_deck-optimal-move-determination-alln.json)

## deck-e-joint-multiplicity-alln

For all sufficiently large n, is the number of poset states lying on a common height-S(n) optimal play from the n-antichain that share BOTH the same linear-extension count e(P) and the same child extension-count deck D(P) bounded by a polynomial in n? Earlier fronts closed e alone and e-plus-width/height as value keys and posed (e,F) state multiplicity, but the joint (e,D) fiber on the optimal-feasible slice is untested.

**investigated** · [Full research report](../../fronts/0604-deck-e-joint-multiplicity-alln.md)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e077ec146ffeu683RqjBOgHmIf](../../assistant-reports/sessions/ses_e077ec146ffeu683RqjBOgHmIf.md)
Original task commissions: [d58084615004](../../followup/task-commissions/objects/d58084615004669472d70fc678884c17cdf172584f7e36d7d08a434f976bb6a6.txt)
Mixed-session reports: [c8d2663008cb](../../followup/mixed-reports/objects/c8d2663008cb8bb45adb8c57bb5d673344af4445fe94e7fc6422143f24424021.txt)
Source manifests: [soring-fronts_deck-e-joint-multiplicity-alln](../../workspaces/manifests/soring-fronts_deck-e-joint-multiplicity-alln.json)

## depth2-extension-profile-minimax-completeness-alln

For a finite poset P let M2(P) be the depth-two extension-count profile: the multiset, over every incomparable pair {x,y} and both orientations, of the child extension-count deck of each one-step child; more generally M_t is the recursive depth-t profile. Is there an absolute constant t such that M_t determines the exact minimax value F(P) for every finite poset P, given that the newest #301 result refuted the depth-one case (F is NOT a function of (e,M1)) with an explicit n=7 pair having e=M1=32 but F=5 versus F=6, and that M1-determination is known to hold at n&lt;=6?

**investigated** · [Full research report](../../fronts/0727-depth2-extension-profile-minimax-completeness-alln.md)
Historical reported excerpt: ## Outcome
Board: [2026-11-23 review](../../board/301/page-001.md?plain=1#L395) · [2026-11-23 review](../../board/301/page-001.md?plain=1#L421)
Additional board mentions: 3 (use front lookup for exact links)
Assistant reports: [ses_df6874654ffeoLekUSGMcBuvNa](../../assistant-reports/sessions/ses_df6874654ffeoLekUSGMcBuvNa.md)
Original task commissions: [b6111c5806ca](../../followup/task-commissions/objects/b6111c5806cac3209020a14dcf5a931a99e14865f6bbe965d340c96d214d8ab2.txt)
Mixed-session reports: [63f431556768](../../followup/mixed-reports/objects/63f431556768ba99ad7ea94f608df722d0cde8fba87e335c870ed05b7fe74de7.txt) · [884bc06d62b1](../../followup/mixed-reports/objects/884bc06d62b1165cf537c515df8301d7fdd3f7508e952fea274f92fa6d31d9ad.txt) · [dd7ff6dd3f16](../../followup/mixed-reports/objects/dd7ff6dd3f16756c7a1462d3c1f7ed8c24d7525e75364bb17a9f1bc7f7afc178.txt) (4 total)
Source manifests: [soring-fronts_depth2-extension-profile-minimax-completeness-alln](../../workspaces/manifests/soring-fronts_depth2-extension-profile-minimax-completeness-alln.json)

## reachable-depth-two-profile-f-completeness-alln

For every n and every poset state P reachable from the n-antichain along some height-S(n) optimal play, does the depth-two extension-count profile M2(P) determine the exact minimax continuation cost F(P), i.e. must two such optimal-play reachable states with identical (e(P), M2(P)) necessarily have equal F(P), for all n -- and does the n=7 general M1 counterexample admit any reachable M2-cospectral mate at some n?

**investigated** · [Full research report](../../fronts/0728-reachable-depth-two-profile-f-completeness-alln.md)
Board: [2026-11-23 review](../../board/301/page-001.md?plain=1#L361)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_df6874459ffecSmiVuT3ZUL71b](../../assistant-reports/sessions/ses_df6874459ffecSmiVuT3ZUL71b.md)
Original task commissions: [8eba776c715d](../../followup/task-commissions/objects/8eba776c715d4b5e0f044d8581e3caba2e5c5e8894f7c536e356fc7e27f5dbae.txt)
Mixed-session reports: [63f431556768](../../followup/mixed-reports/objects/63f431556768ba99ad7ea94f608df722d0cde8fba87e335c870ed05b7fe74de7.txt) · [884bc06d62b1](../../followup/mixed-reports/objects/884bc06d62b1165cf537c515df8301d7fdd3f7508e952fea274f92fa6d31d9ad.txt)
Source manifests: [soring-fronts_reachable-depth-two-profile-f-completeness-alln](../../workspaces/manifests/soring-fronts_reachable-depth-two-profile-f-completeness-alln.json)

## annotated-child-deck-f-completeness-alln

For every finite poset P of every size, let Dstar(P) be the multiset over all incomparable pairs {x,y} of the annotated pair of records (e(P+x&lt;y), F(P+x&lt;y)) and (e(P+y&lt;x), F(P+y&lt;x)), where e counts linear extensions and F is the exact minimax sorting cost. Board #301 (20:45Z) verified by a fresh from-scratch C++ census over all 130023 labelled 6-element and 6129859 labelled 7-element posets that Dstar determines F for every poset of size at most 7 (155 and 915 groups, zero mixed-F). Does this hold for ALL finite posets at every n, i.e. is F a total function of the (e,F)-annotated one-step child deck?

**investigated** · [Full research report](../../fronts/0732-annotated-child-deck-f-completeness-alln.md)
Board: [2026-11-23 message](../../board/301/page-001.md?plain=1#L634)
Assistant reports: [ses_df5c44dfcffeymvF5ZpsViyEia](../../assistant-reports/sessions/ses_df5c44dfcffeymvF5ZpsViyEia.md)
Original task commissions: [b40d7c26bf2d](../../followup/task-commissions/objects/b40d7c26bf2d7b4d3754e4d578014df61344b03ba8163c417b76d7a31f235105.txt)
Mixed-session reports: [2c5a98a9b42e](../../followup/mixed-reports/objects/2c5a98a9b42ea836c9d316358634e4ea91a8722e3223fbcb13ec920172ee9533.txt)
Source manifests: [soring-fronts_annotated-child-deck-f-completeness-alln](../../workspaces/manifests/soring-fronts_annotated-child-deck-f-completeness-alln.json)

## annotated-deck-state-count-exponent-alln

Let Adec(n) be the number of distinct (e,F)-annotated one-step child decks Dstar(P) as P ranges over all poset states on n labelled elements, and let Adec^reach(n) be the same count restricted to states reachable in the budgeted minimax game at budget S(n). Is Adec^reach(n) = 2^{o(n log^2 n)} for all n, so that grouping states by Dstar could support a new exact evaluator, or does Adec(n) grow at least 2^{Omega(n log^2 n)} along an infinite family, matching or exceeding the exponent of the current best exact evaluation algorithm?

**investigated** · [Full research report](../../fronts/0734-annotated-deck-state-count-exponent-alln.md)
Board: [2026-11-23 message](../../board/301/page-001.md?plain=1#L634)
Assistant reports: [ses_df5c44790ffeehTO6Jkqp3lVIT](../../assistant-reports/sessions/ses_df5c44790ffeehTO6Jkqp3lVIT.md)
Original task commissions: [9bf27af3699f](../../followup/task-commissions/objects/9bf27af3699f4121c396116a4f426d16dc998f6321b99f17799eb8933ab4fd4f.txt)
Mixed-session reports: [2c5a98a9b42e](../../followup/mixed-reports/objects/2c5a98a9b42ea836c9d316358634e4ea91a8722e3223fbcb13ec920172ee9533.txt)
Source manifests: [soring-fronts_annotated-deck-state-count-exponent-alln](../../workspaces/manifests/soring-fronts_annotated-deck-state-count-exponent-alln.json)

## program-size-deck-multiplicity-lower-bound-alln

For all sufficiently large n, must every fixed-interpreter FO(TC) strategy program that sorts the n-antichain within S(n) comparisons have text size Omega(D(n)), where D(n) is the number of distinct child extension-count decks over states reachable on height-S(n) optimal play, or can transitive-closure queries compress arbitrary deck-indexed move choices into poly(n) program size despite superpolynomial deck multiplicity?

**investigated** · [Full research report](../../fronts/0736-program-size-deck-multiplicity-lower-bound-alln.md)
Assistant reports: [ses_df570f680ffeN5cMj9lJVytpJC](../../assistant-reports/sessions/ses_df570f680ffeN5cMj9lJVytpJC.md)
Original task commissions: [617ddec1ebd7](../../followup/task-commissions/objects/617ddec1ebd773ceee00b552dfd06e3392bfb60d991b29a3a4e1102efa8e7ae1.txt)
Mixed-session reports: [404164d9d9a4](../../followup/mixed-reports/objects/404164d9d9a462fd7a3d46cf8b15d1a9d082993176a418f0229dd2251e0edd1e.txt)
Source manifests: [soring-fronts_program-size-deck-multiplicity-lower-bound-alln](../../workspaces/manifests/soring-fronts_program-size-deck-multiplicity-lower-bound-alln.json)
