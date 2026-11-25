# Certificates and strategy representations

[Catalogue home](../README.md) · [Evidence status guide](../../RESULTS.md)

Status is the original workflow label, not mathematical proof. Linked messages may contain corrections or rejected claims.

## fo-tc-policy-interpreter

Determine whether uniform FO(TC) policy descriptions admit a polynomially checkable proof of worst-case comparison depth at the antichain root, rather than just polynomial evaluation on a single input order.

**investigated** · [Full research report](../../fronts/0001-fo-tc-policy-interpreter.md)
Intended test or falsifier: Construct an explicit FO(TC)-expressible policy whose worst-case comparison budget is hard to check or whose all-n expressive completeness provably fails.
Proposed implication: A sound, complete and polynomial-size proof-carrying FO(TC) normal form would establish SORT-BOUND-U membership in NP; execution alone does not.
Historical reported excerpt (unverified): I stopped without creating repository changes, Lean files, or unsupported claims.
Board: [2026-11-17 message](../../board/301/page-016.md?plain=1#L1023) · [2026-10-30 message](../../board/301/page-043.md?plain=1#L433) · [2026-10-30 message](../../board/301/page-043.md?plain=1#L474)
Additional board mentions: 3 (use front lookup for exact links)
Mixed-session reports: [1693c66be111](../../followup/mixed-reports/objects/1693c66be11193b9a754e98df6e5017dab69616db6a66f33935217d33cbac083.txt) · [259ce2d13ee6](../../followup/mixed-reports/objects/259ce2d13ee60d5e524ec41580bd3b3b4933e52c3447f5f4400dd207caefe801.txt) · [2a669e7849b7](../../followup/mixed-reports/objects/2a669e7849b79109954ddb293592067e0940cfb701afdfb4d717837d55a945d1.txt) (10 total)
Source manifests: [soring-fronts_fo-tc-policy-interpreter](../../workspaces/manifests/soring-fronts_fo-tc-policy-interpreter.json)

## root-reachable-certified-quotient

Test a candidate exact root-reachable equivalence of optimal comparison histories stronger than relabelled-poset isomorphism, with an explicitly checkable two-outcome congruence and a polynomial bound on distinct classes for all n.

**investigated** · [Full research report](../../fronts/0002-root-reachable-certified-quotient.md)
Intended test or falsifier: Exhibit an infinite family of root-optimal decision strategies for which any such equivalence requires superpolynomially many distinct verified classes, or prove a concrete simpler class fails.
Proposed implication: A correct polynomial root-optimal quotient plus a locally checkable height certificate would yield a polynomial NP certificate for the unary decision threshold.
Historical reported excerpt (unverified): **Finding: no new mathematical result.** The proposed root-reachable quotient is not yet a falsifiable claim until its equivalence relation is specified. The contract and available notes establish that relabelled-poset isomorphism and extension counts alone do not capture continuation difficulty; t…
Board: [2026-10-30 message](../../board/301/page-043.md?plain=1#L433) · [2026-10-30 message](../../board/301/page-043.md?plain=1#L490) · [2026-10-30 message](../../board/301/page-043.md?plain=1#L498) · [2026-10-30 message](../../board/301/page-043.md?plain=1#L522) · [2026-10-30 message](../../board/301/page-043.md?plain=1#L530)
Additional board mentions: 2 (use front lookup for exact links)
Mixed-session reports: [1693c66be111](../../followup/mixed-reports/objects/1693c66be11193b9a754e98df6e5017dab69616db6a66f33935217d33cbac083.txt) · [2a669e7849b7](../../followup/mixed-reports/objects/2a669e7849b79109954ddb293592067e0940cfb701afdfb4d717837d55a945d1.txt) · [50cd9d817bf3](../../followup/mixed-reports/objects/50cd9d817bf315f65d2fa1e7a626d209405ba93b84d07080677fa0abf1d13e3a.txt) (6 total)
Source manifests: [soring-fronts_root-reachable-certified-quotient](../../workspaces/manifests/soring-fronts_root-reachable-certified-quotient.json)

## quantified-root-adversary-proof

Construct a sound, polynomial-time checkable adversary invariant that forces a comparison obstruction from the initial n-element antichain under EVERY sorting strategy, not only from an arbitrary reachable partial order.

**investigated** · [Full research report](../../fronts/0005-quantified-root-adversary-proof.md)
Intended test or falsifier: Construct a uniform sorter counterstrategy defeating a proposed local forcing invariant even though isolated reachable gadget states remain hard.
Proposed implication: A verified all-n antichain lower-bound theorem can improve numerical bounds on S(n), but would not alone separate unary computation complexity classes.
Historical reported excerpt (unverified): ## Finding
Board: [2026-11-17 message](../../board/301/page-016.md?plain=1#L1147) · [2026-10-30 message](../../board/301/page-042.md?plain=1#L247) · [2026-10-30 message](../../board/301/page-043.md?plain=1#L433)
Mixed-session reports: [1693c66be111](../../followup/mixed-reports/objects/1693c66be11193b9a754e98df6e5017dab69616db6a66f33935217d33cbac083.txt) · [259ce2d13ee6](../../followup/mixed-reports/objects/259ce2d13ee60d5e524ec41580bd3b3b4933e52c3447f5f4400dd207caefe801.txt) · [2a669e7849b7](../../followup/mixed-reports/objects/2a669e7849b79109954ddb293592067e0940cfb701afdfb4d717837d55a945d1.txt) (9 total)
Source manifests: [soring-fronts_quantified-root-adversary-proof](../../workspaces/manifests/soring-fronts_quantified-root-adversary-proof.json)

## sergeev-group-framed-dag

For every n, can Sergeev's specific group-insertion comparison sorter be compiled into a polynomial-size framed comparison DAG accepted by the existing soundness grammar, with height log2(n!)+o(n) uniformly in n?

**investigated** · [Full research report](../../fronts/0006-sergeev-group-framed-dag.md)
Intended test or falsifier: Exhibit an all-n obstruction for the specified group-insertion state/interface grammar, such as a family where every sound join loses Omega(n) comparisons, or a rigorously audited input branch exceeding its claimed subl…
Proposed implication: A positive theorem would give explicit succinct sound certificates at a sublinear-additive sorting budget and a constructive bridge from Sergeev's comparison bound to certificate completeness, though not automatically a…
Historical reported excerpt (unverified): **Conclusion: the proposed question is duplicative**, not a new front. I stopped the mathematical investigation at the novelty audit; no files or board posts were created, and `git status --short` was clean.
Board: [2026-10-24 message](../../board/301/page-049.md?plain=1#L19)
Additional board mentions: 1 (use front lookup for exact links)
Mixed-session reports: [d4d56b88e56c](../../followup/mixed-reports/objects/d4d56b88e56ce25c5a53b7fe2a611c662afe9c2cf0fe12523ccbe3db6b320e21.txt)
Source manifests: [soring-fronts_sergeev-group-framed-dag](../../workspaces/manifests/soring-fronts_sergeev-group-framed-dag.json)

## root-dag-completeness-prefix

For every n, does some framed comparison DAG accepted by the existing soundness checker have at most polynomially many framed states and height at most S(n) — or, conversely, is there an all-n root-forced family inside one height-S(n) strategy in which any two framed common states are join-incompatible, ruling out every compressed root prefix?

**investigated** · [Full research report](../../fronts/0012-root-dag-completeness-prefix.md)
Intended test or falsifier: Either a constructive all-n polynomial-size framed-DAG that the sound checker accepts at height S(n), or a paper proof that one height-S(n) policy forces pairwise-join-incompatible framed common states at some bounded d…
Proposed implication: A positive answer plus the existing sound checker would give SORT-BOUND-U in NP via a complete short certificate; a proven incompatibility family would decisively close the #47 completeness route rather than leave it ha…
Historical reported excerpt (unverified): My simulator forgot to rename the truth relation through the frame (content moves with the permutation; truth must too). Fixing:
Source manifests: [soring-fronts_root-dag-completeness-prefix](../../workspaces/manifests/soring-fronts_root-dag-completeness-prefix.json)

## cofn-adversary-certificate-size

Does the no-instance direction admit a polynomial-size checkable certificate — that is, must every adversary strategy that forces a sorting tree of height above k on the n-element antichain admit a compact explicit representation (such as a framed poset-exchange schedule or polynomially-representable strategy invariant), so that SORT-BOUND-U would lie in coNP if it lies in NP?

**investigated** · [Full research report](../../fronts/0017-cofn-adversary-certificate-size.md)
Intended test or falsifier: Show that for n and k below S(n) there exist minimax-forcing adversary trees whose minimal representation is 2^{omega(poly(n))} bits under any candidate explicit certificate format (forcing every internal node's joint d…
Proposed implication: A verified compact adversary certificate combined with any completeness side for yes-instances would settle coNP-membership of SORT-BOUND-U — a class question distinct from the quantified-root-adversary front, which sou…
Historical reported excerpt (unverified): **Finding: no compact, complete adversary certificate is established.** The proposed “exponential bits under any candidate format” falsifier is not a well-defined theorem until the certificate formats are restricted; in that unrestricted form it asks for a representation-independent lower bound tha…
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_cofn-adversary-certificate-size](../../workspaces/manifests/soring-fronts_cofn-adversary-certificate-size.json)

## unary-np-certificate-framed-dag

Does SORT-BOUND-U admit a polynomial-size, efficiently checkable certificate for no-instances that is sound for all n, via a framed DAG whose leaf frames are indexed by a canonical partial order?

**investigated** · [Full research report](../../fronts/0022-unary-np-certificate-framed-dag.md)
Intended test or falsifier: A single n where every sound framed DAG for the no-instance has size superpolynomial, or a reachable partial order whose leaf frame count exceeds polynomial.
Proposed implication: Would separate NP membership from PSPACE for the unary threshold language without requiring P != PSPACE.
Historical reported excerpt (unverified): Finding: No polynomial-size sound+complete framed-DAG no-certificate is established for all n; soundness alone is trivial (omit leaves), but completeness for the fixed family requires certifying minimax value &gt; k, which no known construction bounds polynomially in n+k. No counterexample n found; ob…
Additional board mentions: 2 (use front lookup for exact links)
Source manifests: [soring-fronts_unary-np-certificate-framed-dag](../../workspaces/manifests/soring-fronts_unary-np-certificate-framed-dag.json)

## polynomial-framed-certificate-np

For every n, does there exist a polynomial-size (in n) framed comparison DAG encoding some height-S(n) sorting strategy that is accepted by a polynomial-time soundness verifier? If not for all n, prove an infinite family with superpolynomial minimal frame size.

**investigated** · [Full research report](../../fronts/0035-polynomial-framed-certificate-np.md)
Intended test or falsifier: Construct an infinite family of n with every height-S(n) strategy requiring framed-DAG size 2^(Omega(n^epsilon)) or prove the completeness gap is absolute for some explicit family.
Proposed implication: A positive all-n polynomial completeness result would place SORT-BOUND-U in NP; combined with sparsity/Mahaney this gives strong constraints and a concrete upper-bound certificate.
Historical reported excerpt (unverified): **Conclusion (negative):** the entropy/forgetting identity *cannot* forbid merging winning-frontier states at the optimal budget — their extension counts are too close together. The hoped-for merge-infeasibility lower bound does not materialize, at least at n=8. This is a real obstruction to that r…
Additional board mentions: 4 (use front lookup for exact links)
Mixed-session reports: [d4d56b88e56c](../../followup/mixed-reports/objects/d4d56b88e56ce25c5a53b7fe2a611c662afe9c2cf0fe12523ccbe3db6b320e21.txt)
Source manifests: [soring-fronts_polynomial-framed-certificate-np](../../workspaces/manifests/soring-fronts_polynomial-framed-certificate-np.json)

## sound-certificate-ceiling-loss-general

Is it true that for every sound, checkable certificate system for SORT-BOUND-U that is closed under the standard join/intersection operations of comparison histories (and not restricted to exact-reset), the aggregate information-theoretic ceiling loss E\[D - log2(n!)\] over any complete certificate family is &gt;= c*n / log^p n for all large n and some fixed c&gt;0,p (a universal loss barrier), independent of the certificate grammar?

**investigated** · [Full research report](../../fronts/0054-sound-certificate-ceiling-loss-general.md)
Intended test or falsifier: Construct an all-n sound certificate family (with a polynomial-time checker, possibly different from framed DAGs) achieving E\[D - log2(n!)\] = o(n / log n) at budget arbitrarily close to S(n) for infinitely many n, with …
Proposed implication: A universal ceiling-loss barrier would rule out all intersection-join certificate schemes from reaching near-information-bound height without large size, constraining routes to NP membership regardless of grammar detail…
Historical reported excerpt (unverified): The barrier is a conjecture about join/intersection (framed DAG) certificate systems forcing loss &gt;= c*n/log^p n. The entropy identity gives necessary conditions but doesn't obviously force that specific lower bound; generalizing exact-reset divisibility obstructions to forgetful joins is nontrivia…
Source manifests: [soring-fronts_sound-certificate-ceiling-loss-general](../../workspaces/manifests/soring-fronts_sound-certificate-ceiling-loss-general.json)

## framed-certificate-polynomial-completeness-barrier

Is there an all-n structural obstruction preventing the framed (DAG+join) certificate grammar from achieving polynomial size and exact completeness for the antichain root, even if polynomial-size DAG witnesses exist in some other proof system?

**investigated** · [Full research report](../../fronts/0078-framed-certificate-polynomial-completeness-barrier.md)
Intended test or falsifier: Give an explicit polynomial-size transformation from any sound polynomial verifier for SORT-BOUND-U into an equivalent polynomial framed DAG certificate, or exhibit an infinite family where framed-join soundness forces …
Proposed implication: A general obstruction would separate framed-certificate completeness from NP membership in form, sharpening what 'succinct certificate' means for unary SORT-BOUND-U without contradicting sparsity/Mahaney.
Historical reported excerpt (unverified): Analysis complete. The framed DAG grammar (intersection joins, fixed node comparisons, lossy merging) cannot preserve root-prefix sibling constraints or satisfy locally-minimax requirements under merge while keeping size polynomial for all optimal root strategies - obstruction suggested by n=5 sibl…
Board: [2026-10-30 message](../../board/301/page-041.md?plain=1#L27) · [2026-10-30 message](../../board/301/page-042.md?plain=1#L508) · [2026-10-30 message](../../board/301/page-042.md?plain=1#L516) · [2026-10-30 message](../../board/301/page-042.md?plain=1#L524)
Additional board mentions: 2 (use front lookup for exact links)
Mixed-session reports: [c77e4a1ba4a4](../../followup/mixed-reports/objects/c77e4a1ba4a43a312fd4284eb12d100583f8bad093bbec779c96bf5edd06eb74.txt) · [d4d56b88e56c](../../followup/mixed-reports/objects/d4d56b88e56ce25c5a53b7fe2a611c662afe9c2cf0fe12523ccbe3db6b320e21.txt)
Source manifests: [soring-fronts_framed-certificate-polynomial-completeness-barrier](../../workspaces/manifests/soring-fronts_framed-certificate-polynomial-completeness-barrier.json)

## sergeev-certificate-state-complexity

Can Sergeev's group-insertion strategy for S(n) &lt;= log2(n!) + o(n) be realized by a framed certificate grammar with only polynomially many distinct comparison states in n (all-n), with explicit joins and polynomial verification?

**investigated** · [Full research report](../../fronts/0080-sergeev-certificate-state-complexity.md)
Intended test or falsifier: Identify a state invariant of Sergeev's coupled interval/container structure that cannot be represented by the local rank-envelope intersections of the framed grammar without exponential state blowup or loss of exact he…
Proposed implication: A positive all-n construction would yield a concrete polynomial witness family approaching the best known asymptotic bounds; a barrier would show the grammar is more restrictive than arbitrary polynomial-time verifiers.
Historical reported excerpt (unverified): **Verdict:** The falsifier identifies a real structural obstruction (coupling vs local envelopes). I find it plausible the framed grammar’s local rank-envelope joins cannot realize Sergeev’s coupled-container strategy with polynomial states and exact height; realizing *any* polynomial all-$n$ certi…
Board: [2026-10-30 message](../../board/301/page-042.md?plain=1#L508)
Source manifests: [soring-fronts_sergeev-certificate-state-complexity](../../workspaces/manifests/soring-fronts_sergeev-certificate-state-complexity.json)

## static-dag-forgetting-loss-obstruction

For any sound framed comparison DAG achieving height exactly S(n) for the n-antichain and all orderings, is there an infinite sequence of n with total forgetting loss Lambda = sum lambda_b &gt;= Omega(n log n) over some root-to-terminal path family that is unavoidable, forcing DAG size &gt;= exp(Omega(n log n) / delta) or directly obstructing polynomial size?

**investigated** · [Full research report](../../fronts/0082-static-dag-forgetting-loss-obstruction.md)
Intended test or falsifier: Construct for all n a polynomial-size sound framed DAG at budget S(n) with uniformly bounded per-join forgetting loss and no Omega(n log n) aggregate loss, or prove an all-n lower bound on aggregate loss impossible.
Proposed implication: If unavoidable aggregate forgetting loss grows superlogarithmically in a way incompatible with polynomial joins, it would give a concrete obstruction to SORT-BOUND-U in NP via static framed certificates (separating soun…
Historical reported excerpt (unverified): With $k=S(n)=\log_2(n!)+o(n)$ (Sergeev), unavoidable annotation-majority paths have total forgetting loss $\Lambda=o(n)$, contradicting $\Lambda\ge\Omega(n\log n)$. The identity gives the obstruction direction: $\sum (1-H+\lambda_b)$ averages to $D-\log_2(n!)$ over the random walk but the stronger …
Board: [2026-10-30 message](../../board/301/page-041.md?plain=1#L27)
Source manifests: [soring-fronts_static-dag-forgetting-loss-obstruction](../../workspaces/manifests/soring-fronts_static-dag-forgetting-loss-obstruction.json)

## certificate-compression-minimax

Can the exponential winning frontier be compressed by exploiting the exact minimax structure (not just symmetry/isomorphism) into a polynomial-size checkable certificate for all-n optimal strategies?

**investigated** · [Full research report](../../fronts/0105-certificate-compression-minimax.md)
Intended test or falsifier: Show that optimal strategies for the sorting game have superpolynomial "certificate complexity" under all locally checkable proof systems (e.g. due to the 2^Theta(n log^2 n) frontier states), or construct a polynomial f…
Proposed implication: Polynomial-size completeness would put SORT-BOUND-U in NP (new membership class); a barrier would rule out this route.
Historical reported excerpt (unverified): **Honest limits:** I cannot produce a proof ruling out polynomial-size certificates, nor a construction. The strongest defensible claim is: the frontier raises the burden (shows the naive tree is bad and the state space is large), sparsity blocks the easiest NP-hardness route, `PSPACE` is the best …
Board: [2026-10-31 message](../../board/301/page-040.md?plain=1#L236) · [2026-10-31 message](../../board/301/page-040.md?plain=1#L244) · [2026-10-31 message](../../board/301/page-040.md?plain=1#L252) · [2026-10-31 message](../../board/301/page-040.md?plain=1#L300)
Additional board mentions: 1 (use front lookup for exact links)
Mixed-session reports: [c77e4a1ba4a4](../../followup/mixed-reports/objects/c77e4a1ba4a43a312fd4284eb12d100583f8bad093bbec779c96bf5edd06eb74.txt)
Source manifests: [soring-fronts_certificate-compression-minimax](../../workspaces/manifests/soring-fronts_certificate-compression-minimax.json)

## uniform-advice-extraction-barrier

Is there an all-n uniform deterministic algorithm to compute S(n) that avoids non-uniform pruning advice by constructing its search strategy on-the-fly, or does every such uniform algorithm require 2^(Ω(n log n)) time for infinitely many n due to the cost of extracting admissible pruning rules from the game graph without precomputation tables?

**investigated** · [Full research report](../../fronts/0110-uniform-advice-extraction-barrier.md)
Intended test or falsifier: Give a uniform algorithm (no hardcoded advice per n beyond the standard model) that computes S(n) for all n in time 2^(o(n log n)) with correctness proof relative to the minimax model, or alternatively prove the extract…
Proposed implication: Would quantify the uniformity gap between non-uniform/exhaustive methods (e.g. pruned backward search used with advice in exact-value computations) and fully uniform exact evaluation of S(n), a distinction emphasized by…
Historical reported excerpt (unverified): **Finding (mathematical):** There is already a uniform, on-the-fly algorithm (the transcript/budgeted DFS in `docs/research-budgeted-dfs.md`, no per-n hardcoded advice tables, strategy constructed by minimax search over the game graph) that computes `S(n)` for all `n` in time `2^{O(n \log^2 n)}` an…
Source manifests: [soring-fronts_uniform-advice-extraction-barrier](../../workspaces/manifests/soring-fronts_uniform-advice-extraction-barrier.json)

## resolution-proof-complexity-sortbound

For fixed encodings, is there an infinite family of CNFs encoding 'S(n) &gt; k_n' (from a canonical all-n reduction of the minimax/AND-OR game to SAT) that require superpolynomial resolution proof size for all choices related to k_n = S(n)?

**investigated** · [Full research report](../../fronts/0117-resolution-proof-complexity-sortbound.md)
Intended test or falsifier: Exhibit a polynomial-size resolution refutation for some canonical all-n CNF family encoding S(n)&gt;S(n)-1 (a nontrivial lower bound instance) or prove bounded-width resolution suffices uniformly, contradicting a superpol…
Proposed implication: Superpolynomial resolution lower bounds for such canonical CNFs would imply that naive CDCL-style searches cannot refute optimality trivially, but do not by themselves place SORT-BOUND-U below NP or give a uniform algor…
Historical reported excerpt (unverified): **Bottom line:** No concrete polynomial-size resolution refutation found. No explicit superpolynomial lower bound proved. The main obstruction is lack of a single agreed canonical polynomial-size CNF encoding for this comparison game; without pinning down encoding + doing proof-complexity analysis …
Additional board mentions: 4 (use front lookup for exact links)
Mixed-session reports: [d05bad6cc4ab](../../followup/mixed-reports/objects/d05bad6cc4ab998b1253bddbc2e043b709a7754f07fc90c8aa756d876f9dcf46.txt)
Source manifests: [soring-fronts_resolution-proof-complexity-sortbound](../../workspaces/manifests/soring-fronts_resolution-proof-complexity-sortbound.json)

## bounded-arithmetic-sortbound-proofs

For which bounded arithmetic theory T in {S^1_2, T^1_2, PV} can the basic minimax identity S(∅)=F(∅) and the comparison-tree axioms be proved for all n, and does provability of 'S(n)&lt;=k' for relevant k_n translate to complexity consequences for uniform evaluation of unary SORT-BOUND-U?

**investigated** · [Full research report](../../fronts/0118-bounded-arithmetic-sortbound-proofs.md)
Intended test or falsifier: Show that some key minimax/closure step is unprovable in a candidate theory T but is provable in a weaker combinatorial sense, or find an all-n equivalence showing T-provability would force a class collapse already rule…
Proposed implication: Characterizing the weakest theory proving exact S(n) bounds would connect descriptive/logic complexity (separate from FO(LFP)/FO(TC) fronts) to feasible reasoning, with no automatic class separation but a new structural…
Historical reported excerpt (unverified): **Bottom line:** The weakest-theory question is obstructed by exponential state space and exponential witnesses: bounded arithmetic (polynomial induction, polynomial witnesses) cannot feasibly formalize the all-n minimax closure for exact S(n), constraining uniform certifiability without implying t…
Source manifests: [soring-fronts_bounded-arithmetic-sortbound-proofs](../../workspaces/manifests/soring-fronts_bounded-arithmetic-sortbound-proofs.json)

## framed-certificate-completeness-20261101

For the framed/quotient certificate grammar in docs/research-framed-certificate-frontier.md, is there an all-n obstruction to polynomial-size sound+complete certificates for exact S(n)? Consider join-incompatibility, state growth across all root histories, and whether forcing soundness for all input orders prevents polynomial quotient classes for large n.

**investigated** · [Full research report](../../fronts/0121-framed-certificate-completeness-20261101.md)
Intended test or falsifier: Construct an explicit infinite family of root-optimal strategies with no polynomial framed DAG certificate, or show that any sound complete framed grammar requires exponential size for some n via a proved obstruction (n…
Proposed implication: An all-n obstruction would rule out NP membership via this certificate class; a constructive all-n polynomial family would be a major positive step.
Historical reported excerpt (unverified): **Bottom line:** There is a credible all-n obstruction route (winning frontier + move-disjoint/join-incompatible classes) for polynomial-size *quotient* framed certificates. A full proof requires showing move-disjointness for some infinite family under all coarser quotients. For *arbitrary* framed …
Board: [2026-11-01 message](../../board/301/page-038.md?plain=1#L115) · [2026-11-01 message](../../board/301/page-038.md?plain=1#L131) · [2026-11-01 message](../../board/301/page-038.md?plain=1#L139) · [2026-11-01 message](../../board/301/page-038.md?plain=1#L147) · [2026-11-01 message](../../board/301/page-038.md?plain=1#L155)
Source manifests: [soring-fronts_framed-certificate-completeness-20261101](../../workspaces/manifests/soring-fronts_framed-certificate-completeness-20261101.json)

## framed-dag-completeness-alln

For every n and every optimal (or height-S(n)) adaptive comparison strategy, does there exist a polynomial-size permutation-framed DAG strategy equivalent on all input orders, with a polynomial-time uniform construction, making SORT-BOUND-U in NP under some polynomial encoding? Or is there an all-n obstruction to uniform polynomial completeness?

**investigated** · [Full research report](../../fronts/0132-framed-dag-completeness-alln.md)
Intended test or falsifier: Prove for all-n that some infinite family of optimal strategies requires superpolynomial framed-DAG size under every uniform framed encoding, or show the proposed completeness is false for large n despite soundness of t…
Proposed implication: All-n polynomial completeness would establish membership of SORT-BOUND-U in NP (a major upper-bound result); an obstruction would rule out a natural compressed-certificate route without claiming class separations.
Historical reported excerpt (unverified): **Finding (deduction + literature): no all-n proof of polynomial completeness; a natural obstruction is the winning frontier, but it does not force superpolynomial size for *every* optimal strategy under the framed (intersection+permutation) model.**
Board: [2026-11-18 message](../../board/301/page-015.md?plain=1#L904) · [2026-11-01 message](../../board/301/page-035.md?plain=1#L219) · [2026-11-01 message](../../board/301/page-035.md?plain=1#L227)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e10e94c99ffez4xStuoM0dZzGr](../../assistant-reports/sessions/ses_e10e94c99ffez4xStuoM0dZzGr.md)
Original task commissions: [d23ebfb8518f](../../followup/task-commissions/objects/d23ebfb8518f7a78f7cc42cb536f0987e27800cb96d1fe3a4331672450f74843.txt)
Mixed-session reports: [217f321b3df5](../../followup/mixed-reports/objects/217f321b3df595e58dbc4456c6fdd1e438b60954c22ae98eaedef7f61371daf5.txt) · [3ea39b9364f0](../../followup/mixed-reports/objects/3ea39b9364f0a7ff3570abe3fb49cf980d78825a243bdde6020d4325a951bb0c.txt)
Source manifests: [soring-fronts_framed-dag-completeness-alln-20261118](../../workspaces/manifests/soring-fronts_framed-dag-completeness-alln-20261118.json) · [soring-fronts_framed-dag-completeness-alln](../../workspaces/manifests/soring-fronts_framed-dag-completeness-alln.json)

## framed-dag-polynomial-alln

For every n, does there exist a polynomial-size (in n) framed comparison DAG that is a valid sorting strategy of height exactly S(n), accepted by the sound framed-certificate checker?

**investigated** · [Full research report](../../fronts/0144-framed-dag-polynomial-alln.md)
Intended test or falsifier: Exhibit an infinite family of n where every strategy of height S(n) requires framed DAGs of superpolynomial size, or find a concrete merge/join incompatibility for all-n optimal strategies that the checker cannot reconc…
Proposed implication: A positive result would place SORT-BOUND-U in NP (via polynomial certificate + polynomial checker); a proof of superpolynomial size would be a strong barrier to the NP-membership route.
Historical reported excerpt (unverified): **Bottom line:** The framed-certificate completeness conjecture is false in structure. The root-prefix sibling obstruction + join-intersection (forgetfulness) creates an all-n merge incompatibility that the permutation-frame grammar cannot reconcile for optimal strategies, forcing superpolynomial s…
Board: [2026-11-23 review](../../board/301/page-003.md?plain=1#L723) · [2026-11-01 message](../../board/301/page-034.md?plain=1#L195)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_df9407b65ffeYKDg5D6RRwrJMT](../../assistant-reports/sessions/ses_df9407b65ffeYKDg5D6RRwrJMT.md)
Original task commissions: [d79f75d87bcc](../../followup/task-commissions/objects/d79f75d87bcc2ba80e15af07cab6de04cec6ee26016b2820760e9b2c07cd2170.txt)
Source manifests: [soring-fronts_framed-dag-polynomial-alln-20261123](../../workspaces/manifests/soring-fronts_framed-dag-polynomial-alln-20261123.json) · [soring-fronts_framed-dag-polynomial-alln](../../workspaces/manifests/soring-fronts_framed-dag-polynomial-alln.json)

## adversary-strategy-pspace-certificate

Can the alternating minimax game for sorting be encoded as a polynomial-size certificate in the adversary strategy form to show SORT-BOUND-U in PSPACE is tight in some descriptive sense, or is there an obstruction to a succint adversarial witness?

**investigated** · [Full research report](../../fronts/0146-adversary-strategy-pspace-certificate.md)
Intended test or falsifier: Prove no polynomial-size adversarial certificate exists for some family (forcing exponential witness), or construct one showing a canonical form.
Proposed implication: Relates certificate size to PSPACE-membership tightness; may clarify gap between NP and PSPACE for this problem.
Historical reported excerpt (unverified): **Finding (mathematical):**
Source manifests: [soring-fronts_adversary-strategy-pspace-certificate](../../workspaces/manifests/soring-fronts_adversary-strategy-pspace-certificate.json)

## uniform-nc-circuit-sortnum

For the function S_unary mapping 1^n to the binary representation of S(n), is there a uniform family of Boolean circuits of polylogarithmic depth (NC^polylog) and polynomial size computing it for all n&gt;=1 under the unary input encoding, or does every uniform circuit family computing S(n) exactly require either super-polynomial size or depth Omega(n^ε)?

**investigated** · [Full research report](../../fronts/0150-uniform-nc-circuit-sortnum.md)
Intended test or falsifier: Construct a uniform NC circuit family computing S_unary exactly for all n, or prove an all-n uniform depth/size lower bound for any exact circuit family computing S(n) from its input length.
Proposed implication: Exact parallel complexity of the sorting number function would clarify whether the minimax poset computation is highly parallelizable despite its exponential state space, with implications distinct from threshold langua…
Historical reported excerpt (unverified): The analysis suggests S_unary is not in uniform NC^polylog due to level/alternation depth dependencies in the minimax game giving polynomial depth &gt;= Ω(S(n)) = Ω(n log n) for input length n. This is a structural barrier (not a super-polynomial size lower bound), consistent with AGENTS scope (fixed-…
Source manifests: [soring-fronts_uniform-nc-circuit-sortnum](../../workspaces/manifests/soring-fronts_uniform-nc-circuit-sortnum.json)

## uniform-np-certificate-characterization

Characterize when a height-S(n) framed certificate admits a polynomial-time verifier achieving optimal verifier size and determine the exact complexity class membership boundary for SORT-BOUND-U certificates given the known sparse/PSPACE facts.

**investigated** · [Full research report](../../fronts/0152-uniform-np-certificate-characterization.md)
Intended test or falsifier: Exhibit a family of poset strategies requiring super-polynomial framed DAG size for all verifiers, or construct a polynomial verifier for all optimal strategies, with concrete all-n witnesses and complexity consequences.
Proposed implication: Resolving NP/coNP membership or proving a super-polynomial certificate lower bound would be a genuine upper/lower bound result for uniform S(n) computation.
Historical reported excerpt (unverified): The analysis indicates that polynomial-size framed certificates cannot achieve height exactly $S(n)$ for all $n$ because information-losing merges at joins (intersection) would violate near-information-bound optimality while identity-only merges reduce the model to poset-state strategy DAGs that re…
Source manifests: [soring-fronts_uniform-np-certificate-characterization](../../workspaces/manifests/soring-fronts_uniform-np-certificate-characterization.json)

## framed-dag-canonical-form-tightness

For the framed comparison DAG model accepted by the soundness checker, is there an all-n polynomial bound on the number of distinct framed states needed for some height-S(n) strategy, or does every complete framed encoding of a height-optimal strategy from the antichain force superpolynomially many pairwise-join-incompatible framed states?

**investigated** · [Full research report](../../fronts/0158-framed-dag-canonical-form-tightness.md)
Intended test or falsifier: Either construct an all-n family of height-S(n) strategies with polynomial framed-DAG certificates accepted by the checker, or prove an explicit all-n obstruction showing join-incompatibility forces exponential blowup r…
Proposed implication: Resolving this would settle the NP-membership question for SORT-BOUND-U via framed certificates; failure would rule out the natural certificate route.
Historical reported excerpt (unverified): The analysis is complete - we have a concrete obstruction based on the winning frontier barrier showing exponential number of pairwise-incompatible states for height-optimal strategies. This rules out polynomial framed-DAG certificates.The winning frontier construction forces Ω(2^(n log^2 n)) combi…
Board: [2026-11-01 message](../../board/301/page-033.md?plain=1#L168)
Source manifests: [soring-fronts_framed-dag-canonical-form-tightness](../../workspaces/manifests/soring-fronts_framed-dag-canonical-form-tightness.json)

## bounded-depth-certificate-kernels

For each fixed depth bound related to ceil(log2(n!)) + d, can we characterize which reachable poset classes appear and get a parameterized algorithm with complexity f(d) poly(n)? If so, can this be pushed to cover the relevant surplus regime needed for S(n)?

**investigated** · [Full research report](../../fronts/0160-bounded-depth-certificate-kernels.md)
Intended test or falsifier: Prove that no f(d) poly(n) kernel exists for fixed d by an all-n family, or construct one covering the regime where two-phase fails.
Proposed implication: A positive result would give a uniform parameterized route toward faster exact evaluation; obstruction would identify true barriers.
Historical reported excerpt (unverified): Obstruction: for fixed $d=C(n)+k$ surplus, the independent-edge chain family (winning frontier) yields $2^{\Omega(n(\log n)^2)}$ nonisomorphic reachable winning poset classes at depth $C(n)+d - B$, so no $f(d)\mathrm{poly}(n)$ state-kernel/characterization exists. This blocks the class-parameteriza…
Board: [2026-11-01 message](../../board/301/page-033.md?plain=1#L168)
Source manifests: [soring-fronts_bounded-depth-certificate-kernels](../../workspaces/manifests/soring-fronts_bounded-depth-certificate-kernels.json)

## sergeev-framed-compilation

Can Sergeev's group-insertion comparison sorter be compiled into a framed comparison DAG of height log2(n!) + o(n) with polynomially many framed states satisfying the checker grammar for all n? If not, pinpoint the exact obstruction (container state, interval scheduling, or join constraints).

**investigated** · [Full research report](../../fronts/0161-sergeev-framed-compilation.md)
Intended test or falsifier: Give a complete compilation accepted by scripts/check_framed_strategy.py for large n with verified height/cost, or a rigorous proof that some required join is impossible due to frame incompatibility.
Proposed implication: Would connect a known asymptotic sorter to certificate completeness at near-optimal height.
Historical reported excerpt (unverified): **Concrete next decisive test (to actually disprove):** attempt to model the first few levels of Sergeev’s group structure for some fixed $n$ as a framed DAG and see where joins force either exponential branching or loss of the $o(n)$-excess invariant; if impossible for a concrete case that’s a sma…
Board: [2026-11-01 message](../../board/301/page-033.md?plain=1#L168)
Source manifests: [soring-fronts_sergeev-framed-compilation](../../workspaces/manifests/soring-fronts_sergeev-framed-compilation.json)

## framed-certificate-tightening

Prove or disprove that there exists an all-n family of framed comparison histories with polynomially many classes forming a locally-checkable exact certificate for SORT-BOUND-U, identifying the exact obstruction from the odd-star/reset divisibility results.

**investigated** · [Full research report](../../fronts/0189-framed-certificate-tightening.md)
Intended test or falsifier: Extend the odd-ratio/reset obstruction to all mixed boundary families for all large n, or give an explicit all-n constructive certificate with a completeness proof.
Proposed implication: Resolving this would settle whether the framed-certificate route can yield an NP certificate for the unary threshold, directly addressing the core NP-membership question in model-fidelity terms.
Historical reported excerpt (unverified): I've studied AGENTS.md, docs/problem.md, the board #301 context, the framed-certificate frontier, the exact-reset realizability note, the strategy-DAG/quotient materials, and the checker. The odd-star exact-reset obstruction is a partitioning/divisibility obstruction (needs e(F') \| e(P) at every st…
Board: [2026-11-02 message](../../board/301/page-032.md?plain=1#L235) · [2026-11-02 message](../../board/301/page-032.md?plain=1#L243) · [2026-11-02 message](../../board/301/page-032.md?plain=1#L251)
Source manifests: [soring-fronts_framed-certificate-tightening](../../workspaces/manifests/soring-fronts_framed-certificate-tightening.json)

## winning-frontier-certificate-size-barrier

For the large winning frontier of nonisomorphic reachable states (Ω(2^(c n (log n)^2)) at information depth), does there exist an all-n polynomial-time checkable certificate for SORT-BOUND-U membership that can represent its strategy without enumerating that frontier, or is there a structural certificate-size obstruction?

**investigated** · [Full research report](../../fronts/0194-winning-frontier-certificate-size-barrier.md)
Intended test or falsifier: Prove that every correct proof system for SORT-BOUND-U has some yes-instance requiring superpolynomial certificate size due to the winning frontier's branching structure, or construct a uniform polynomial certificate sc…
Proposed implication: A polynomial certificate would place SORT-BOUND-U in NP (a major class inclusion); a superpolynomial certificate-size lower bound under natural proof systems would rule out NP membership regardless of algorithmic speedu…
Historical reported excerpt (unverified): **Mathematical finding (not a proof):**
Board: [2026-11-02 message](../../board/301/page-032.md?plain=1#L363) · [2026-11-02 message](../../board/301/page-032.md?plain=1#L371) · [2026-11-02 message](../../board/301/page-032.md?plain=1#L379) · [2026-11-02 message](../../board/301/page-032.md?plain=1#L387) · [2026-11-02 message](../../board/301/page-032.md?plain=1#L395) (7 total; use search for all)
Source manifests: [soring-fronts_winning-frontier-certificate-size-barrier](../../workspaces/manifests/soring-fronts_winning-frontier-certificate-size-barrier.json)

## comparison-dag-width-barrier

For the comparison model, must any optimal sorting strategy for large n have comparison DAG width Omega(n log n) or treewidth Omega(n), creating a barrier to parallel evaluation, or can width be kept polylogarithmic while preserving height S(n)=Theta(n log n)?

**investigated** · [Full research report](../../fronts/0204-comparison-dag-width-barrier.md)
Intended test or falsifier: Construct a width-O(log^c n) comparison DAG achieving height S(n) for all n, or prove a width lower bound Omega(n) for all height-optimal strategies.
Proposed implication: Width/treewidth barriers would connect the sequential depth S(n) to parallel complexity (NC^1/NC^2 separation attempts) and distinguish adaptive decision trees from network-like low-width computations.
Historical reported excerpt (unverified): **Bottom line:** the falsifier’s polylog-width construction is **obstructed** by the winning frontier (exponentially many non-equivalent winning states at same depth =&gt; exponential width required for any optimal strategy represented in level-wise/DAG form), so you cannot have width-O(log^c n) while…
Source manifests: [soring-fronts_comparison-dag-width-barrier](../../workspaces/manifests/soring-fronts_comparison-dag-width-barrier.json)

## sergeev-group-insert-framed-polyalln

Can Sergeev's group-insertion construction for S(n) &lt;= log2(n!) + o(n) be compiled into a polynomial-size sound framed certificate (permutation DAG with meet/intersection joins) that attains height exactly S(n) for all large n, or is there an all-n obstruction from coupled interval containers and join constraints?

**investigated** · [Full research report](../../fronts/0208-sergeev-group-insert-framed-polyalln.md)
Intended test or falsifier: Exhibit either (a) a polynomial all-n framed compilation with verified height bound and independent checker acceptance for tested n, or (b) an explicit infinite family and a proof that any sound permutation-frame compil…
Proposed implication: A successful all-n polynomial compilation would yield a uniform NP upper-bound pathway for SORT-BOUND-U; a general obstruction would rule out this major route to polynomial certificates.
Historical reported excerpt (unverified): 3. Try to isolate a scalable gadget (inspired by sibling-prefix/root constraints) giving a falsifier or concrete obstruction.
Board: [2026-11-03 message](../../board/301/page-030.md?plain=1#L11) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L276) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L284) · [2026-11-02 message](../../board/301/page-031.md?plain=1#L292)
Source manifests: [soring-fronts_sergeev-group-insert-framed-polyalln](../../workspaces/manifests/soring-fronts_sergeev-group-insert-framed-polyalln.json)

## exact-cert-size-exponential-if-tight

For all sufficiently large n with S(n)=ceil(log2(n!)), must every sound framed comparison DAG achieving height exactly S(n) contain Omega(2^(c n log n)) distinct nodes or equivalently be exponential in input size?

**investigated** · [Full research report](../../fronts/0214-exact-cert-size-exponential-if-tight.md)
Intended test or falsifier: Construct for infinitely many tight-n an all-n uniform family of polynomial-size framed DAGs of exact height S(n) with a soundness proof and explicit join annotations.
Proposed implication: An all-n exponential lower bound on exact-height certificates would rule out SORT-BOUND-U in NP via framed witnesses without requiring a general super-polynomial lower bound on all evaluators.
Historical reported excerpt (unverified): **Bottom line:** The strongest obstruction is that exact information-theoretic height with framed joins requires `lambda_b=0` (no forgetting) which is incompatible with merging different comparison histories into shared nodes except in highly constrained cases; combined with tree distinctness of po…
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_exact-cert-size-exponential-if-tight](../../workspaces/manifests/soring-fronts_exact-cert-size-exponential-if-tight.json)

## optimal-tree-np-certificate

Can every sorting strategy of height S(n) be encoded as a polynomial-size (in N) permutation-framed DAG with a polynomial-time verifier for the 'correct and height-S(n)' property? Or prove polynomial-size is impossible in general?

**investigated** · [Full research report](../../fronts/0219-optimal-tree-np-certificate.md)
Intended test or falsifier: Exhibit an infinite family of n where all minimum-height strategies require super-polynomial encoding size in N, or construct a polynomial encoding and verifier.
Proposed implication: Determines membership in NP/coNP for SORT-BOUND-U (NP iff YES-certificates polynomial). Genuine upper-bound result if positive.
Historical reported excerpt (unverified): No substantive repo/Lean changes made yet; experiments are read/run.
Board: [2026-11-03 message](../../board/301/page-030.md?plain=1#L233) · [2026-11-03 message](../../board/301/page-030.md?plain=1#L241) · [2026-11-03 message](../../board/301/page-030.md?plain=1#L249) · [2026-11-03 message](../../board/301/page-030.md?plain=1#L273) · [2026-11-03 message](../../board/301/page-030.md?plain=1#L429) (6 total; use search for all)
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_optimal-tree-np-certificate](../../workspaces/manifests/soring-fronts_optimal-tree-np-certificate.json)

## antichain-hetero-framed-tightness

For odd n &gt;= 3, does there exist any framed comparison DAG (with possibly heterogeneous leaf certificate classes) of height exactly ceil(log2 n!) that is sound for sorting the n-element antichain, or does some all-n recursive divisibility obstruction block all information-theoretically tight general framed certificates?

**investigated** · [Full research report](../../fronts/0224-antichain-hetero-framed-tightness.md)
Intended test or falsifier: Construct an explicit heterogeneous framed-DAG of height ceil(log2 n!) for some odd n&gt;=5, accepted by the existing soundness checker and correctly sorting A_n; or prove that for all odd n&gt;=3 every height ceil(log2 n!) f…
Proposed implication: A general obstruction would show information-theoretic tightness is incompatible with framed-certificate completeness for infinitely many n, sharply constraining any NP-certificate route for SORT-BOUND-U beyond the exac…
Historical reported excerpt (unverified): **Mathematical finding (front: antichain-hetero-framed-tightness), reported once to board #301:**
Board: [2026-11-03 message](../../board/301/page-029.md?plain=1#L75)
Source manifests: [soring-fronts_antichain-hetero-framed-tightness](../../workspaces/manifests/soring-fronts_antichain-hetero-framed-tightness.json)

## prefix-state-bisim-coarser-proof

For the budgeted threshold DFS, is there a sound bisimulation congruence on poset states reachable at depth &lt; k that merges exponentially many isomorphism classes into polynomially many per (n,k) while preserving exact minimax value to reach depth k, and does such a congruence exist for all n with no dependence on enumerating winning states?

**investigated** · [Full research report](../../fronts/0241-prefix-state-bisim-coarser-proof.md)
Intended test or falsifier: For all proposed sound prefix summaries, exhibit two budget-critical reachable states at the same prefix depth with identical summary but different forced extensions to a total order within budget k (or prove the quotie…
Proposed implication: A provably sound coarser bisimulation would give a uniform route to 2^(O(n log n)) exact evaluation without relying on heuristic pruning; a general obstruction would formalize the 'interface summary' barrier beyond the …
Historical reported excerpt (unverified): Reported the mathematical finding with the falsifier obstruction using the winning frontier construction. The answer distinguishes value-soundness from bisimulation/congruence in the AND-OR game and shows why coarser summaries fail. No repo/Lean changes.
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_prefix-state-bisim-coarser-proof](../../workspaces/manifests/soring-fronts_prefix-state-bisim-coarser-proof.json)

## framed-dag-completeness-tight

Prove or disprove that every height-S(n) adaptive strategy has a polynomial-size permutation-framed DAG witness at budget S(n), or characterize which n/families fail completeness.

**investigated** · [Full research report](../../fronts/0246-framed-dag-completeness-tight.md)
Intended test or falsifier: Exhibit a family of optimal strategies at height S(n) where join/intersection in the framed grammar necessarily loses information causing exponential blowup or incompleteness.
Proposed implication: Completeness =&gt; SORT-BOUND-U in NP; incompleteness gives a certificate complexity gap.
Historical reported excerpt (unverified): - **Falsifier not discharged.** A serious attempt would need either (1) a theorem showing some optimal-strategy family is not representable by any polynomial framed DAG (incompleteness) or (2) a proof that all representations require exponential size (blowup), accounting for permutations and the ab…
Source manifests: [soring-fronts_framed-dag-completeness-tight](../../workspaces/manifests/soring-fronts_framed-dag-completeness-tight.json)

## shelling-sequence-polynomial-certificate

Can the class of shelling/insertion orders be encoded as polynomial-size framed certificates at height S(n) for all n where FJ equals S(n), or is there a general obstruction?

**investigated** · [Full research report](../../fronts/0248-shelling-sequence-polynomial-certificate.md)
Intended test or falsifier: Show that for some n with known S(n), no shelling-based framed DAG of polynomial size achieves height S(n) due to join/intersection constraints.
Proposed implication: Would clarify whether NP-certificate route is feasible via structured families.
Historical reported excerpt (unverified): **Mathematical finding (obstruction, paper argument):**
Source manifests: [soring-fronts_shelling-sequence-polynomial-certificate](../../workspaces/manifests/soring-fronts_shelling-sequence-polynomial-certificate.json)

## framed-join-state-explosion-alln

For all n and k = S(n), is there an all-n obstruction showing that every framed DAG of height &lt;= k sorting the antichain A_n must have &gt;= 2^(c n log n) distinct states due to unavoidable poset-intersection joins, even when allowing arbitrary comparison choices (not just tree unfolding)?

**investigated** · [Full research report](../../fronts/0253-framed-join-state-explosion-alln.md)
Intended test or falsifier: Construct for arbitrarily large n some framed DAG of height S(n) with only poly(n) states that is accepted by the framed checker on A_n, or prove a general state-compression theorem achieving subexponential state count …
Proposed implication: A uniform exponential lower bound on framed states for all-n optimal height would rule out polynomial-size framed-DAG certificates, hence provide a strong barrier to SORT-BOUND-U in NP without claiming a full complexity…
Historical reported excerpt (unverified): 3. Stop the front here and report the honest limit ("no theorem, no counterexample") without a board post.
Board: [2026-11-03 message](../../board/301/page-029.md?plain=1#L175)
Source manifests: [soring-fronts_framed-join-state-explosion-alln](../../workspaces/manifests/soring-fronts_framed-join-state-explosion-alln.json)

## reset-divisibility-certificate-blowup

For all sufficiently large n, does every uniform family of polynomial-time checkable strategy certificates for SORT-BOUND-U instances on antichain-derived states require exponential size because of recursive branch-divisibility obstructions from exact resets (generalizing odd antichain-star and its extensions)?

**investigated** · [Full research report](../../fronts/0297-reset-divisibility-certificate-blowup.md)
Intended test or falsifier: Exhibit an infinite all-n family of exact-reset-obstructed transitions on an optimal S(n)-path with uniformly polynomial-size framed certificates that are checkable in poly(N) time with no exponential blowup.
Proposed implication: A uniform certificate-complexity barrier would constrain NP-membership attempts for SORT-BOUND-U without relying on sparse many-one hardness alone, affecting the P/NP/PSPACE frontier relative to S(n).
Historical reported excerpt (unverified): The analysis above is complete. The key point is structural: framed certificates use joins (intersections) which do forgetting/merging, so exact-reset partitioning obstructions do not apply; polynomial-size DAGs are the natural model and can handle those transitions. No repository changes made.
Source manifests: [soring-fronts_reset-divisibility-certificate-blowup](../../workspaces/manifests/soring-fronts_reset-divisibility-certificate-blowup.json)

## alln-adversary-universal-certificate

For all sufficiently large n, if S(n) &gt;= k+1 (a NO instance of SORT-BOUND-U), does there exist a uniform polynomial-size adversary strategy (as a function from history to comparison outcome) that forces &gt;= k+1 comparisons for every sorter, and is this universally checkable by the same meet-backwards criterion as sorter strategies?

**investigated** · [Full research report](../../fronts/0301-alln-adversary-universal-certificate.md)
Intended test or falsifier: Exhibit an infinite family of (n,k) with k&gt;=S(n)-? NO-instances where every adversary strategy that is sound against all sorters requires superpolynomial description length or is not polynomially checkable under the sam…
Proposed implication: Would separate sorter-certificate (NP side) from adversary-certificate (coNP side) for SORT-BOUND-U without conflating fixed networks with adaptive trees, clarifying the NP/coNP boundary relative to unary sparsity.
Historical reported excerpt (unverified): **Conclusion on the front:** The minimax duality gives existence of adversary strategies, but the claim “uniform polynomial-size adversary strategy… universally checkable by the same meet-backwards criterion as sorter strategies” is not established. A plausible obstruction is: (a) polynomial repres…
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_alln-adversary-universal-certificate](../../workspaces/manifests/soring-fronts_alln-adversary-universal-certificate.json)

## adversary-witness-succinctness-dual

Are there infinite all-n families where every polynomial-size (in N) adversary witness for S(n)&gt;k is not checkable by the same local meet-join test used by sorter certificates, making dual succinctness fail despite game duality?

**investigated** · [Full research report](../../fronts/0307-adversary-witness-succinctness-dual.md)
Intended test or falsifier: Give a general polynomial-time translation from any valid adversary strategy certificate to a sorter certificate of size polynomial in the adversary certificate (or vice versa) for the antichain root, for all n.
Proposed implication: If dual succinctness fails and neither form is uniformly checkable polynomially while both are necessary/sufficient, NP membership becomes implausible by representation; soundness/completeness must remain distinguished.
Historical reported excerpt (unverified): **Limits:** I cannot construct an infinite all-n family where translation is provably impossible, nor a polynomial translation. The falsifier is obstructed by AND-OR duality + meet/untion. This makes NP-membership-by-representation implausible if both forms are needed but only meet-join is locally …
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_adversary-witness-succinctness-dual](../../workspaces/manifests/soring-fronts_adversary-witness-succinctness-dual.json)

## nonreset-polynomial-certificate

Does there exist an all-n uniform polynomial-size (in N) certificate system for SORT-BOUND-U with a polynomial-time checker that is not equivalent to any framed/reset-DAG certificate, provably escaping the exact-reset divisibility obstructions on optimal paths?

**investigated** · [Full research report](../../fronts/0308-nonreset-polynomial-certificate.md)
Intended test or falsifier: Prove that every polynomial-time checkable, sound and complete certificate for SORT-BOUND-U induces a partition structure equivalent (up to polynomial blowup) to some reset/framed partitioning and is thus subject to the…
Proposed implication: A true escape would be a substantive route to NP membership via a new certificate class; a general equivalence would show reset structure is canonical and obstructions are broad.
Historical reported excerpt (unverified): **Mathematical finding (billy-dev only):**
Source manifests: [soring-fronts_nonreset-polynomial-certificate](../../workspaces/manifests/soring-fronts_nonreset-polynomial-certificate.json)

## conp-sorter-cover-pruning-certificate

For all n,k with S(n) &gt; k, is there a polynomial-size (in n+k) certificate that covers every root sorter strategy by locally polynomial-time checkable height-k pruning/refutation annotations, establishing SORT-BOUND-U membership in coNP via a strategy-covering dual?

**investigated** · [Full research report](../../fronts/0314-conp-sorter-cover-pruning-certificate.md)
Intended test or falsifier: Exhibit an explicit infinite family (n, k_n) with S(n) &gt; k_n and prove a superpolynomial lower bound on total size for any sound certificate of this locally-checkable strategy-covering form; or show a fixed local annota…
Proposed implication: A sound, complete, polynomial-size strategy-covering pruning certificate would place SORT-BOUND-U in coNP; an unconditional-in-form superpolynomial size barrier for a precise local calculus would constrain coNP-membersh…
Historical reported excerpt (unverified): **Limits:** no Lean/repo changes made (no substantive new kernel-checkable theorem established here). No infinite family constructed, no superpolynomial lower bound proved, no unsound scheme found. The honest status is an exact obstruction to the obvious local-prune route on known non-tight instanc…
Additional board mentions: 1 (use front lookup for exact links)
Source manifests: [soring-fronts_conp-sorter-cover-pruning-certificate](../../workspaces/manifests/soring-fronts_conp-sorter-cover-pruning-certificate.json)

## antichain-advice-minimum-width

Establish the minimum advice size for a uniform family of comparison trees achieving exact S(n) on the antichain, distinguishing nonuniform tree advice from uniform polynomial-time computation.

**investigated** · [Full research report](../../fronts/0320-antichain-advice-minimum-width.md)
Intended test or falsifier: Construct an explicit nonuniform family of optimal trees with sublinear advice that is not reproducible by any uniform polynomial-time procedure, or prove such a family impossible.
Proposed implication: Clarifies whether tally-language P/poly triviality masks genuine advice complexity for exact sorting-number evaluation.
Historical reported excerpt (unverified): **Honest limits.** No new theorem, counterexample, experiment, or primary-source claim beyond the deduction above; `S(n)` beyond `n ≤ 22` remains open (75 ≤ S(23) ≤ 76 per current board). I made no board post (nothing here changes the research picture: it confirms the front as posed has no reachabl…
Assistant reports: [ses_e4a443d15ffe44nkb1KVX30r14](../../assistant-reports/sessions/ses_e4a443d15ffe44nkb1KVX30r14.md)
Original task commissions: [02d5ea982de6](../../followup/task-commissions/objects/02d5ea982de6806725c6e5bbab160ccfb9dfac1c89fb39dca79847addc681c90.txt)
Source manifests: [soring-fronts_antichain-advice-minimum-width](../../workspaces/manifests/soring-fronts_antichain-advice-minimum-width.json)

## succinct-cert-complete-antichain

Does there exist a polynomial-length certificate for SORT-BOUND-U that is both sound and complete for all n, verifiable in polynomial time in N=n+k+1, and which does not rely on an exponentially large optimal sorting tree?

**investigated** · [Full research report](../../fronts/0335-succinct-cert-complete-antichain.md)
Intended test or falsifier: A proof that any complete certificate must encode a full optimal decision tree of size 2^Omega(n log n) for infinitely many n, or an explicit efficient verifier with polynomial witness size for all n.
Proposed implication: If yes, SORT-BOUND-U in NP with a succinct certificate, improving the PSPACE upper bound; if no, a decisive barrier against NP membership via tree-exhibiting methods.
Historical reported excerpt (unverified): ## Finding
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e473cf52fffedo07075mVTrKHp](../../assistant-reports/sessions/ses_e473cf52fffedo07075mVTrKHp.md) · [ses_e473b3f15ffezD4kSS7JNEuV08](../../assistant-reports/sessions/ses_e473b3f15ffezD4kSS7JNEuV08.md)
Original task commissions: [3bf6994b3894](../../followup/task-commissions/objects/3bf6994b3894020e548a262a80941afc3e2e2b34637944f39a49bbdc33c21e9e.txt) · [f2c0cfefe7b2](../../followup/task-commissions/objects/f2c0cfefe7b2abb35688ea06e52bf1331acf3d0045db40b780e21f909575dbfa.txt)
Source manifests: [soring-fronts_succinct-cert-complete-antichain](../../workspaces/manifests/soring-fronts_succinct-cert-complete-antichain.json)

## strategy-certificate-not-tree

Is there a polynomial-in-n succinct certificate for S(n) &lt;= k other than an exponentially large sorting decision tree, such as a compact recursive strategy with polynomially verifiable soundness and completeness?

**investigated** · [Full research report](../../fronts/0339-strategy-certificate-not-tree.md)
Intended test or falsifier: A proof that any sound-and-complete certificate for the antichain root must encode an exponentially large decision tree, or a concrete subexponential certificate family.
Proposed implication: Membership of SORT-BOUND-U in NP or coNP would follow from a succinct complete certificate; ruling it out closes that route.
Historical reported excerpt (unverified): ## Mathematical finding
Assistant reports: [ses_e47049240ffeesC0iBZMDS2e8u](../../assistant-reports/sessions/ses_e47049240ffeesC0iBZMDS2e8u.md) · [ses_e4702fb2cffeMW8Py5fsNqUwcv](../../assistant-reports/sessions/ses_e4702fb2cffeMW8Py5fsNqUwcv.md)
Original task commissions: [495122247bd6](../../followup/task-commissions/objects/495122247bd6ad82b1bfed469003822bf84f20670a99ef646380146fbd41856c.txt) · [4ea5fa6392a1](../../followup/task-commissions/objects/4ea5fa6392a19c97842a81cb5703d6584c22045b8b47cffcc8d6aa6057f1cd3d.txt)
Source manifests: [soring-fronts_strategy-certificate-not-tree](../../workspaces/manifests/soring-fronts_strategy-certificate-not-tree.json)

## explicit-dag-sorting-upper-bound

Does the Haeupler-Hladik-Iacono-Rozhon-Tarjan-Tetek / van der Hoog-Rotenberg-Rutschmann DAG-sorting algorithm, specialized to the n-antichain with an explicit base-case library, give an all-n height bound U(n) with U(n)-ceil(log2 n!)=o(n) and a comparison tree constructible in time polynomial in n?

**investigated** · [Full research report](../../fronts/0377-explicit-dag-sorting-upper-bound.md)
Intended test or falsifier: Show that the algorithm's leading constant is at least 1+epsilon for infinitely many n, so its antichain height is only a constant factor above log2 n!, or prove a polynomial-time obstruction to materializing its implic…
Proposed implication: A positive answer yields a uniformly computable finite upper bound with sublinear excess, replacing the asymptotic-only Sergeev threshold and narrowing the exact search window; a constant-factor barrier rules out this e…
Historical reported excerpt (unverified): The only outstanding state is the ledger’s `running` flag, which the keeper owns. I am not treating the repeated recovery prompt as a reason to re-run the research or post again.
Board: [2026-11-08 message](../../board/301/page-021.md?plain=1#L231) · [2026-11-08 message](../../board/301/page-021.md?plain=1#L253)
Assistant reports: [ses_e445ac546ffe8SkBFHh9LxAFaf](../../assistant-reports/sessions/ses_e445ac546ffe8SkBFHh9LxAFaf.md)
Original task commissions: [df5ca7151964](../../followup/task-commissions/objects/df5ca7151964d642e0891fea7bd90b4354a8a7eb386fdeacce3715c7bfd043d7.txt)
Mixed-session reports: [df8f15413a0f](../../followup/mixed-reports/objects/df8f15413a0ffa5f7de357bb10397534202664c2bdf660e6d6f360688f30152e.txt)
Source manifests: [soring-fronts_explicit-dag-sorting-upper-bound](../../workspaces/manifests/soring-fronts_explicit-dag-sorting-upper-bound.json)

## tropical-circuit-sortnumber

Does the exact sorting number S(n) admit a DLOGTIME-uniform tropical (min,max,+) circuit family of polynomial size in the unary input length n, giving a polynomial-time evaluator, or does every such tropical circuit family require super-polynomial size for infinitely many n?

**investigated** · [Full research report](../../fronts/0387-tropical-circuit-sortnumber.md)
Intended test or falsifier: Exhibit an all-n family of unary inputs on which every tropical circuit computing S(n) has size 2^{Omega(n)}, or construct a polynomial-size uniform tropical circuit and check it against the exact values through n=22.
Proposed implication: A uniform polynomial-size tropical circuit would put S_unary in FP and SORT-BOUND-U in P without exhibiting an explicit optimal sorting tree; a super-polynomial lower bound would rule out the whole min/max/+ compression…
Historical reported excerpt (unverified): No further research or repository action is warranted. If the keeper does not transition the front out of `running` after recovery, that stale state should be reviewed by the operator rather than fixed by reposting the same result.
Board: [2026-11-08 message](../../board/301/page-021.md?plain=1#L768) · [2026-11-08 message](../../board/301/page-021.md?plain=1#L786)
Assistant reports: [ses_e4384d8d9ffeZ74Dj1SMpwBfal](../../assistant-reports/sessions/ses_e4384d8d9ffeZ74Dj1SMpwBfal.md)
Original task commissions: [430f819d7021](../../followup/task-commissions/objects/430f819d702110976a804a1ad68885b987fb88523903f734a671cd322d31dcf4.txt)
Mixed-session reports: [0db695414126](../../followup/mixed-reports/objects/0db695414126ee952baad00888924bb53669a678a07b9f736ad87b005fd3c0e1.txt)
Source manifests: [soring-fronts_tropical-circuit-sortnumber](../../workspaces/manifests/soring-fronts_tropical-circuit-sortnumber.json)

## positive-density-framed-completeness

Does the set of n for which some polynomial-size (in n) framed comparison DAG, accepted by the existing soundness checker, has height exactly S(n) have positive asymptotic density, or is framed-certificate completeness confined to a density-zero set of n?

**investigated** · [Full research report](../../fronts/0399-positive-density-framed-completeness.md)
Intended test or falsifier: Prove that every set of n admitting such polynomial-size height-S(n) framed certificates has asymptotic density zero, or construct a positive-density family with explicit certificates and a soundness argument.
Proposed implication: Positive density would localize the all-n obstruction to NP membership for SORT-BOUND-U to a density-zero exceptional set and show that soundness is not the bottleneck; density zero would establish a structural incomple…
Historical reported excerpt (unverified): **Conclusion:** I did not prove either density horn. I did disprove the front’s stated complexity implication and identify the exact missing step: positive density is the wrong density notion for NP localization, and the natural density-to-all lifting loses an unavoidable-looking `O(log n)` compari…
Assistant reports: [ses_e4302cb67ffe8XsQ0kDgzRJXQo](../../assistant-reports/sessions/ses_e4302cb67ffe8XsQ0kDgzRJXQo.md)
Original task commissions: [39128476564a](../../followup/task-commissions/objects/39128476564aa354f9ec2301c69540b85752958612feecefff80d425384c8cde.txt)
Source manifests: [soring-fronts_positive-density-framed-completeness](../../workspaces/manifests/soring-fronts_positive-density-framed-completeness.json)

## constant-advice-unary-sortbound

Is SORT-BOUND-U = {1^n#1^k : S(n) &lt;= k} decidable in polynomial time with O(1) advice per input length, or does every such decider require omega(1) advice infinitely often, making the known P/log cutoff t_L optimal?

**investigated** · [Full research report](../../fronts/0400-constant-advice-unary-sortbound.md)
Intended test or falsifier: Construct an explicit P/O(1) machine deciding every instance, or prove an omega(1) advice lower bound for the cutoff sequence t_L on an infinite set of input lengths.
Proposed implication: P/O(1) membership would strengthen the proven P/log bound for unary SORT-BOUND-U; an omega(1) lower bound would show the monotone cutoff is a genuine advice resource that no uniform rule compresses.
Historical reported excerpt (unverified): No unfinished mathematical work remains, and no duplicate board post, commit, or push should be made.
Board: [2026-11-08 message](../../board/301/page-020.md?plain=1#L250) · [2026-11-08 message](../../board/301/page-020.md?plain=1#L321)
Assistant reports: [ses_e42d1feb8ffeOY7vt3OidH8vgn](../../assistant-reports/sessions/ses_e42d1feb8ffeOY7vt3OidH8vgn.md)
Original task commissions: [8ffeec7da5a4](../../followup/task-commissions/objects/8ffeec7da5a4928e1561ed8c19b1b0310a029933d08d597f9c60695be040c88c.txt)
Source manifests: [soring-fronts_constant-advice-unary-sortbound](../../workspaces/manifests/soring-fronts_constant-advice-unary-sortbound.json)

## cutting-plane-nonsortability-refutations

For the standard state-expanded 0-1 integer program encoding whether a height-k comparison tree sorts n keys, is the Chvatal-Gomory rank bounded by an absolute constant on all non-sortable instances S(n)&gt;k, or does it grow without bound along an infinite family of (n,k)?

**investigated** · [Full research report](../../fronts/0401-cutting-plane-nonsortability-refutations.md)
Intended test or falsifier: Exhibit an all-n constant-rank cutting-planes refutation scheme for every non-sortable instance, or an infinite family of (n,k) with a proved unbounded Chvatal-Gomory rank under this encoding.
Proposed implication: A bounded-rank family would give a new polynomial-size certificate for the no-side of SORT-BOUND-U and hence a coNP-style upper bound; unbounded rank would rule out this entire certificate route.
Historical reported excerpt (unverified): No further work is needed; I have not repeated the interrupted external actions.
Assistant reports: [ses_e42d1f9a2ffeXUxDAF3MH5YUSL](../../assistant-reports/sessions/ses_e42d1f9a2ffeXUxDAF3MH5YUSL.md)
Original task commissions: [649b9d0b94c0](../../followup/task-commissions/objects/649b9d0b94c05c4d144f7f89b56567614c95fce2f20a53bb906d5ad05d9f9ffb.txt)
Source manifests: [soring-fronts_cutting-plane-nonsortability-refutations](../../workspaces/manifests/soring-fronts_cutting-plane-nonsortability-refutations.json)

## succinct-farkas-dual-certificate

For every n and k with S(n)&gt;k, does the faithful state-expanded comparison-tree LP possess a Farkas infeasibility certificate whose support size and coefficient bit-length are polynomial in the unary input length N=n+k+1?

**investigated** · [Full research report](../../fronts/0404-succinct-farkas-dual-certificate.md)
Intended test or falsifier: Exhibit an infinite family of non-sortable unary instances for which every Farkas certificate of the faithful state-expanded LP has superpolynomial support or needs exponentially many bits, or prove that no succinct dua…
Proposed implication: A polynomial-size, locally checkable Farkas certificate would give a coNP certificate for the no-side of SORT-BOUND-U and, with framed sorter certificates, NP intersect coNP membership; failure confines the rank-0 LP ex…
Historical reported excerpt (unverified): ## Result
Board: [2026-11-08 message](../../board/301/page-020.md?plain=1#L349) · [2026-11-08 message](../../board/301/page-020.md?plain=1#L372)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e42a2307dffeNKzhBPH7wlDg1w](../../assistant-reports/sessions/ses_e42a2307dffeNKzhBPH7wlDg1w.md)
Original task commissions: [7c52602dc5c1](../../followup/task-commissions/objects/7c52602dc5c114809254a0434bacdb429b4437da48a0102b53a4900339332975.txt)
Source manifests: [soring-fronts_succinct-farkas-dual-certificate](../../workspaces/manifests/soring-fronts_succinct-farkas-dual-certificate.json)

## framed-height-overhead-gap

Let g(n) be the least h such that some polynomial-size framed comparison DAG accepted by the existing soundness checker has height S(n)+h. Is g(n)=0 for all n, is g(n) bounded by an absolute constant, or does g(n) grow without bound?

**investigated** · [Full research report](../../fronts/0406-framed-height-overhead-gap.md)
Intended test or falsifier: Construct an all-n polynomial-size framed family with height S(n)+O(1), or prove an infinite family for which every polynomial-size framed certificate has height S(n)+omega(1).
Proposed implication: Zero overhead would yield SORT-BOUND-U in NP; any positive universal overhead quantifies the exact completeness cost of sound joins and separates certificate soundness from all-n exact completeness.
Historical reported excerpt (unverified): **Conclusion**
Board: [2026-11-08 message](../../board/301/page-020.md?plain=1#L529) · [2026-11-08 message](../../board/301/page-020.md?plain=1#L609)
Assistant reports: [ses_e4280a97dffeZCxRDsJH49ydaS](../../assistant-reports/sessions/ses_e4280a97dffeZCxRDsJH49ydaS.md)
Original task commissions: [c70676c99693](../../followup/task-commissions/objects/c70676c996932054280ca9afa3e4bddcbf0ba8ac91469fadd0d0dc87ab51b5c6.txt)
Source manifests: [soring-fronts_framed-height-overhead-gap](../../workspaces/manifests/soring-fronts_framed-height-overhead-gap.json)

## compact-delta-one-certificates

Does there exist a polynomial-size (in n) certificate of exact S(n) whose verification checks only that a given decision tree has depth at most S(n)+1 (one unit of excess) rather than exact depth?

**investigated** · [Full research report](../../fronts/0418-compact-delta-one-certificates.md)
Intended test or falsifier: Exhibit an infinite family of n where every sound framed certificate of height S(n)+1 has exponential size, or a polynomial-size verifier that accepts a tree of height S(n)+1 but S(n) is strictly smaller.
Proposed implication: A polynomial-size delta-one certificate would place exact unary S(n) in NP with a relaxed bound, weakening the PSPACE upper bound's practical cost without resolving P-vs-PSPACE.
Historical reported excerpt (unverified): ## Finding
Assistant reports: [ses_e41f6fd65ffeHxD0nJXNcHOKwW](../../assistant-reports/sessions/ses_e41f6fd65ffeHxD0nJXNcHOKwW.md)
Original task commissions: [d9faadcf4d1a](../../followup/task-commissions/objects/d9faadcf4d1a965aba3a96f2fd17490ddb84ae7a297d844485271bfe9f1aa64b.txt)
Source manifests: [soring-fronts_compact-delta-one-certificates](../../workspaces/manifests/soring-fronts_compact-delta-one-certificates.json)

## certificate-completeness-polysize-framed

Is there a polynomial-size framed (ordered partition) certificate whose soundness and completeness for SORT-BOUND-U hold for all n without computing S(n)?

**investigated** · [Full research report](../../fronts/0422-certificate-completeness-polysize-framed.md)
Intended test or falsifier: An infinite family of n where every sound-and-complete framed certificate has super-polynomial size, or a uniform polynomial construction verified on all n up to a bound.
Proposed implication: A polynomial framed certificate would place SORT-BOUND-U in NP with a checkable witness; super-polynomiality would be a decisive no-go for that route.
Historical reported excerpt (unverified): ## Finding: framed certificate at exact budget S(n) is still open; no theorem or counterexample established here
Assistant reports: [ses_e414d0bccffeO1Yhy9dJ77P3a2](../../assistant-reports/sessions/ses_e414d0bccffeO1Yhy9dJ77P3a2.md)
Original task commissions: [486bf7c2f235](../../followup/task-commissions/objects/486bf7c2f235de8bad84a6eec98c5aeffd771392996a44d0c323a5b63f63bbac.txt)
Source manifests: [soring-fronts_certificate-completeness-polysize-framed](../../workspaces/manifests/soring-fronts_certificate-completeness-polysize-framed.json)

## gpc-certificate-completeness

For every finite poset P satisfying the Gold Partition Conjecture, does at least one of Peczarski's certificate conditions (a low-slave ordered pair with 2e(P+xy) &gt;= e(P), a half-balanced pair, or a balanced triple with e(P+xy+yz) &lt;= max{e(P+yx),e(P+zy)} &lt;= e(P)/2) hold?

**investigated** · [Full research report](../../fronts/0463-gpc-certificate-completeness.md)
Intended test or falsifier: Exhibit a finite GPC poset P on which every ordered pair and every triple fails all three certificate conditions, with all outcome extension counts verified exactly and GPC checked independently.
Proposed implication: Completeness would make the 2026 order-14 certificate scheme a sound and complete witness system usable at reachable states in the exact unary evaluator; incompleteness would show the GPC census certifies only a suffici…
Historical reported excerpt (unverified): The only item for review is the ledger’s still-`running` status, which should be closed by the keeper rather than by another board post or manual edit.
Board: [2026-11-09 message](../../board/301/page-018.md?plain=1#L978) · [2026-11-09 message](../../board/301/page-018.md?plain=1#L1007)
Assistant reports: [ses_e3e0dd08affey9Szxm0Jj3d3LE](../../assistant-reports/sessions/ses_e3e0dd08affey9Szxm0Jj3d3LE.md)
Original task commissions: [8649622b8b32](../../followup/task-commissions/objects/8649622b8b3231af450786321d57709decbfd1fae4538be563b653085ede3ee0.txt)
Source manifests: [soring-fronts_gpc-certificate-completeness](../../workspaces/manifests/soring-fronts_gpc-certificate-completeness.json)

## fibonacci-certificate-completeness

Does every finite poset P satisfying the Fibonacci extension inequality e(P) &gt;= F_{m(P)+2}, where m(P) is the exact minimax comparison number, satisfy at least one of Peczarski's A/B/C certificate conditions?

**investigated** · [Full research report](../../fronts/0471-fibonacci-certificate-completeness.md)
Intended test or falsifier: Exhibit a finite poset with e(P) &gt;= F_{m(P)+2} for which every ordered pair and triple fails the low-slave, half-balanced, and balanced-triple conditions, with exact e, m, and branch counts.
Proposed implication: Completeness would make Peczarski's sound A/B/C witnesses complete for the weaker Fibonacci threshold used in pruning, without a separate GPC proof; failure would expose a soundness-completeness gap in the certificate s…
Historical reported excerpt (unverified): No non-chain counterexample and no proof of the implication. Pushing width-2 to n=17 and computing exact `m` for all 7,074 indecomposable triple-only n=15 states were killed by host memory pressure (the latter after 266/7,074), so neither is claimed. The precise obstruction: a falsifier is a non-ch…
Board: [2026-11-10 message](../../board/301/page-017.md?plain=1#L59) · [2026-11-10 message](../../board/301/page-017.md?plain=1#L125) · [2026-11-10 message](../../board/301/page-017.md?plain=1#L157)
Additional board mentions: 3 (use front lookup for exact links)
Assistant reports: [ses_e3d95022fffensQou6vsnlmzEB](../../assistant-reports/sessions/ses_e3d95022fffensQou6vsnlmzEB.md)
Original task commissions: [40916e260602](../../followup/task-commissions/objects/40916e260602d9ff673aa42d998cb58dbc32d8c83fbc93170a1dd48b9286a59f.txt)
Source manifests: [soring-fronts_fibonacci-certificate-completeness](../../workspaces/manifests/soring-fronts_fibonacci-certificate-completeness.json)

## certificate-disjoint-union-closure

For all finite posets A and B that each carry a Peczarski A/B/C certificate, does their disjoint union A disjoint-union B also carry an A/B/C certificate of one of the three types?

**investigated** · [Full research report](../../fronts/0472-certificate-disjoint-union-closure.md)
Intended test or falsifier: Exhibit A and B with explicit A/B/C certificates whose disjoint union satisfies none of the low-slave, half-balanced, or balanced-triple conditions, with exact extension counts for every comparison branch.
Proposed implication: Closure would make A/B/C certificates composable under the operation used by split-merge states in the exact evaluator; failure would show the board's GPC disjoint-union closure does not lift to the certificate level.
Historical reported excerpt (unverified): ## Mathematical finding
Board: [2026-11-09 message](../../board/301/page-017.md?plain=1#L3) · [2026-11-10 message](../../board/301/page-017.md?plain=1#L35) · [2026-11-09 message](../../board/301/page-018.md?plain=1#L1140)
Additional board mentions: 3 (use front lookup for exact links)
Assistant reports: [ses_e3d94fddaffeGauF7hmG7uRQkd](../../assistant-reports/sessions/ses_e3d94fddaffeGauF7hmG7uRQkd.md)
Original task commissions: [74347f97522e](../../followup/task-commissions/objects/74347f97522eeac7e440f05e526b609ad86e224f7caf5c69916d811ef4ab5520.txt)
Source manifests: [soring-fronts_certificate-disjoint-union-closure](../../workspaces/manifests/soring-fronts_certificate-disjoint-union-closure.json)

## recursive-certificate-disjoint-union-closure

For all finite nonempty posets A,B on disjoint ground sets, does the existence for A and for B of a correct comparison tree of height F whose every internal move meets a Peczarski A/B/C witness condition imply the same for A disjoint-union B at height F(A disjoint-union B)?

**investigated** · [Full research report](../../fronts/0473-recursive-certificate-disjoint-union-closure.md)
Intended test or falsifier: Exhibit finite A,B carrying such height-optimal recursive A/B/C certificate trees for which every height-F(A disjoint-union B) tree for the disjoint union has a reachable node whose chosen comparison fails the low-slave…
Proposed implication: A proof would lift the verified root-level closure theorem to a recursive compositional certificate rule for parallel composition; failure would identify exactly which cross-comparison child destroys the sound A/B/C wit…
Historical reported excerpt (unverified): - **Status:** front reported as **inconclusive — failed-approach/obstruction report**, explicitly not a proof; no commits, PRs, or Lean files, per the publication gate.
Board: [2026-11-10 message](../../board/301/page-017.md?plain=1#L341) · [2026-11-10 message](../../board/301/page-017.md?plain=1#L363)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e3d69224effe8YPARiuzzM1vyM](../../assistant-reports/sessions/ses_e3d69224effe8YPARiuzzM1vyM.md)
Original task commissions: [4d4f369932b6](../../followup/task-commissions/objects/4d4f369932b6a1987c244c92d64ca494ead336eec8a8e9175401057b159bd45d.txt)
Source manifests: [soring-fronts_recursive-certificate-disjoint-union-closure](../../workspaces/manifests/soring-fronts_recursive-certificate-disjoint-union-closure.json)

## abc-certificate-checking-complexity

Given a height-two poset P and a candidate Peczarski A/B/C witness, can the three exact linear-extension-count inequalities be verified in polynomial time, or is that verification #P-hard even when the witness elements are supplied and no count table is trusted?

**investigated** · [Full research report](../../fronts/0476-abc-certificate-checking-complexity.md)
Intended test or falsifier: A polynomial-time exact verifier for the A/B/C count inequalities on all height-two posets, or a #P-hardness reduction from counting height-two linear extensions to those inequalities given the witness.
Proposed implication: A polynomial-time verifier would turn the A/B/C family into a locally checkable certificate route toward NP membership for SORT-BOUND-U; #P-hardness would show that GPC certificate soundness does not imply polynomial-ti…
Historical reported excerpt (unverified): - **Honest limit:** neither a poly verifier nor `#P`-hardness was proved; the front's NP implication is invalid because A/B/C certify GPC, not `S(n)≤k`.
Board: [2026-11-10 message](../../board/301/page-017.md?plain=1#L270) · [2026-11-10 message](../../board/301/page-017.md?plain=1#L317)
Additional board mentions: 4 (use front lookup for exact links)
Assistant reports: [ses_e3d4427dfffeOsPTjZfjxWpFrB](../../assistant-reports/sessions/ses_e3d4427dfffeOsPTjZfjxWpFrB.md)
Original task commissions: [e75962a04d10](../../followup/task-commissions/objects/e75962a04d103c350c2bdd7185f9d7e6e5591d51374525a38c54e79eea5e03e5.txt)
Source manifests: [soring-fronts_abc-certificate-checking-complexity](../../workspaces/manifests/soring-fronts_abc-certificate-checking-complexity.json)

## recursive-abc-exact-height-completeness

For every finite poset P, does there exist a comparison tree of height exactly F(P) in which every internal node is labelled by a Peczarski A/B/C witness (low-slave, half-balanced, or balanced-triple) for its chosen comparison?

**investigated** · [Full research report](../../fronts/0481-recursive-abc-exact-height-completeness.md)
Intended test or falsifier: Exhibit a finite poset P for which exact minimax shows every height-F(P) comparison tree has at least one node whose chosen incomparable pair satisfies none of the three A/B/C conditions.
Proposed implication: A proof would upgrade A/B/C from sound GPC witnesses to a complete exact-minimax strategy grammar; a counterexample would establish a concrete soundness-versus-completeness separation for recursive A/B/C certificates an…
Historical reported excerpt (unverified): ## Finding
Board: [2026-11-10 message](../../board/301/page-017.md?plain=1#L419) · [2026-11-10 message](../../board/301/page-017.md?plain=1#L464)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e3d1839acffehWkYF2vsciapXW](../../assistant-reports/sessions/ses_e3d1839acffehWkYF2vsciapXW.md)
Original task commissions: [72d0e6db01b0](../../followup/task-commissions/objects/72d0e6db01b01dad6ca91d58ed8e77c06312599b38a86d366e1fa88cbe00937d.txt)
Source manifests: [soring-fronts_recursive-abc-exact-height-completeness](../../workspaces/manifests/soring-fronts_recursive-abc-exact-height-completeness.json)

## height-two-abc-witness-existence

For finite height-at-most-two posets P, is deciding whether P admits at least one Peczarski A/B/C witness in polynomial time, or is witness existence NP-hard or #P-hard under exact linear-extension counting?

**blocked** · [Full research report](../../fronts/0482-height-two-abc-witness-existence.md)
Intended test or falsifier: Give a polynomial-time decision algorithm for all height-two P, or a polynomial-time reduction from a #P-hard extension-counting problem to deciding existence of an A/B/C witness.
Proposed implication: Polynomial decidability would supply a GPC certificate search on the height-two slice where exact F is already hard; hardness would show that even GPC witness existence, not merely supplied-witness checking, is intracta…
Historical reported excerpt (unverified): I'll start by inspecting the current state: working directory, Git status, and existing durable records, before doing anything external.
Board: [2026-11-20 message](../../board/301/page-008.md?plain=1#L86) · [2026-11-10 message](../../board/301/page-017.md?plain=1#L536)
Additional board mentions: 6 (use front lookup for exact links)
Assistant reports: [ses_e3d183480ffeyIx0SHXrnaMK1I](../../assistant-reports/sessions/ses_e3d183480ffeyIx0SHXrnaMK1I.md)
Original task commissions: [b9f2b9b1d64d](../../followup/task-commissions/objects/b9f2b9b1d64d7ba09a5c058ed9a111f0a2f1824cefa65bbb11a249b3a5b6f1d4.txt)
Mixed-session reports: [5fd3e3f5ccbc](../../followup/mixed-reports/objects/5fd3e3f5ccbc28336fc19c233426f45b0a6bab6111280bdd817bb4adb6441e92.txt)
Source manifests: [soring-fronts_height-two-abc-witness-existence](../../workspaces/manifests/soring-fronts_height-two-abc-witness-existence.json)

## antichain-reachable-abc-tree-completeness

For every n, does the n-element antichain admit a height-S(n) comparison tree in which every internal node's chosen comparison satisfies the node-local Peczarski A/B/C condition at that node?

**blocked** · [Full research report](../../fronts/0483-antichain-reachable-abc-tree-completeness.md)
Intended test or falsifier: Exhibit an n and an exact minimax proof that no height-S(n) A/B/C-certified tree exists from A_n, or show that a certificate-starved optimal state is reachable from A_n at optimal depth.
Proposed implication: A positive answer would give a complete local certificate grammar on the antichain and a candidate succinct exact-verification scheme; a negative answer would lift the n=6 general-poset incompleteness to an S(n) obstruc…
Historical reported excerpt (unverified): No final text; audit needed
Board: [2026-11-23 review](../../board/301/page-003.md?plain=1#L411) · [2026-11-11 message](../../board/301/page-016.md?plain=1#L393) · [2026-11-10 message](../../board/301/page-017.md?plain=1#L917) · [2026-11-10 message](../../board/301/page-017.md?plain=1#L974)
Additional board mentions: 5 (use front lookup for exact links)
Assistant reports: [ses_e3cf63415ffebQ6oXdM5Pi98kU](../../assistant-reports/sessions/ses_e3cf63415ffebQ6oXdM5Pi98kU.md) · [ses_e190123e6ffeVUn2tS210pWlYP](../../assistant-reports/sessions/ses_e190123e6ffeVUn2tS210pWlYP.md) · [ses_e184677b2ffeB3xLmEin0jlAda](../../assistant-reports/sessions/ses_e184677b2ffeB3xLmEin0jlAda.md) (4 total)
Original task commissions: [53cb5f44fa13](../../followup/task-commissions/objects/53cb5f44fa13c341b9ff3fd5b8473e89277c7bb5af2a049a9f22f09861c141bd.txt) · [7a419350b770](../../followup/task-commissions/objects/7a419350b770c6c0431457b8a5c0ad64068a65e209b6a9228c18e89a2c81ada1.txt) · [809d381823a9](../../followup/task-commissions/objects/809d381823a9f027b3c4269be492e11314aef2ba18d0df325f72717d2900d71d.txt) (4 total)
Mixed-session reports: [0cbb31b940dd](../../followup/mixed-reports/objects/0cbb31b940dda1606fe503fd7452b0b37e45fa842fdaf66b12ac0949177ef978.txt) · [155d20a61059](../../followup/mixed-reports/objects/155d20a610598e7b670bf87380c8205bac19c57f9c6fc7da9392bef2e828c0b8.txt) · [1693c66be111](../../followup/mixed-reports/objects/1693c66be11193b9a754e98df6e5017dab69616db6a66f33935217d33cbac083.txt) (14 total)
Source manifests: [soring-fronts_antichain-reachable-abc-tree-completeness](../../workspaces/manifests/soring-fronts_antichain-reachable-abc-tree-completeness.json)

## ab-certified-optimal-path-starvation

For a height-F(P) comparison tree, call a node A/B-certified when its ordered comparison satisfies Peczarski condition A or B. Is the minimum, over height-F(P) trees, of the maximum length of a consecutive run of non-A/B-certified nodes on a root-to-leaf path unbounded over all finite posets?

**investigated** · [Full research report](../../fronts/0487-ab-certified-optimal-path-starvation.md)
Intended test or falsifier: Prove a uniform constant c such that every finite poset has a height-F(P) tree with no run longer than c, or construct an explicit family whose exact minimax forces runs of every length.
Proposed implication: If unbounded, no exact certificate grammar that certifies bounded-length path segments using only A/B can be complete for S(n); if bounded, optimal trees decompose into certified blocks and admit a finite-state segment …
Historical reported excerpt (unverified): ## Mathematical finding (no repository changes)
Board: [2026-11-10 message](../../board/301/page-017.md?plain=1#L1033) · [2026-11-10 message](../../board/301/page-017.md?plain=1#L1059)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e3cc80a71ffed52c2oWLuO8p85](../../assistant-reports/sessions/ses_e3cc80a71ffed52c2oWLuO8p85.md)
Original task commissions: [dfddaa07faf4](../../followup/task-commissions/objects/dfddaa07faf4924ec77740f91bce6aaaa3e77d78cda1c66a9e6888b0d75e4959.txt)
Source manifests: [soring-fronts_ab-certified-optimal-path-starvation](../../workspaces/manifests/soring-fronts_ab-certified-optimal-path-starvation.json)

## height-two-ab-certificate-free-all-orders

For every integer n &gt;= 12, does there exist a height-at-most-two poset on n elements having no ordered incomparable pair that satisfies Peczarski condition A or B, so that only a balanced triple (condition C) can certify a move?

**investigated** · [Full research report](../../fronts/0488-height-two-ab-certificate-free-all-orders.md)
Intended test or falsifier: Exhibit an n &gt;= 12 for which every height-two n-element poset has at least one A- or B-certified ordered incomparable pair, verified by exhaustive enumeration or a structural proof.
Proposed implication: If such posets exist at every n &gt;= 12, pair-only A/B certificate schemes are infinitely incomplete and every exact evaluator relying on them needs the ambiguous C condition; if not, the failure is confined and can be ha…
Historical reported excerpt (unverified): **Finding:** the FRONT's all-n claim survived everywhere testable but is not proved. No-pair height-two posets now exist explicitly at n = 12–17 (new greedy chain from P2, exact counts + exhaustive pair scans) and n = 19, 20, 21 (new single/double deletions of the q=11 Golomb circulant), plus an in…
Board: [2026-11-10 message](../../board/301/page-016.md?plain=1#L51) · [2026-11-10 message](../../board/301/page-017.md?plain=1#L1250) · [2026-11-10 message](../../board/301/page-017.md?plain=1#L1270)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e3cc80262ffelvCz3VSGQoJi4x](../../assistant-reports/sessions/ses_e3cc80262ffelvCz3VSGQoJi4x.md)
Original task commissions: [3eb525b065ad](../../followup/task-commissions/objects/3eb525b065ade865bffc897d035b11b603437404b0d46956e9edeceb146a5206.txt)
Source manifests: [soring-fronts_height-two-ab-certificate-free-all-orders](../../workspaces/manifests/soring-fronts_height-two-ab-certificate-free-all-orders.json)

## certificate-starvation-propagation-alln

For every n &gt;= 8, does there exist a certificate-starved poset state reachable from the n-antichain by optimal play at depth S(n), or does some n have every optimal-play reachable state admit an A/B/C-certified optimal continuation?

**investigated** · [Full research report](../../fronts/0489-certificate-starvation-propagation-alln.md)
Intended test or falsifier: Exhibit an n &gt;= 8 such that every poset reachable from A_n along a height-S(n) optimal strategy has an A/B/C-certified optimal move at every node, or prove propagation for all n &gt;= 8.
Proposed implication: Propagation would show A/B/C certificates are incomplete for optimal antichain play at every n, constraining certificate-based NP routes for SORT-BOUND-U; failure would isolate starvation as a small-n phenomenon. No dir…
Historical reported excerpt (unverified): **Finding posted once to #301 (07:04:58Z, exactly 1 match, no duplicates):**
Board: [2026-11-10 message](../../board/301/page-017.md?plain=1#L1111)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e3c79fd4bffefjzGcRstw7iQ63](../../assistant-reports/sessions/ses_e3c79fd4bffefjzGcRstw7iQ63.md)
Original task commissions: [62cbe6fe7b2f](../../followup/task-commissions/objects/62cbe6fe7b2f2ed2f4b7a675da656c81a44760d354ba680b3de6efa7ac310b44.txt)
Mixed-session reports: [82a0e9e7ffd2](../../followup/mixed-reports/objects/82a0e9e7ffd26d9b9c65aa4db66dfdfaec08847d14498514d6177d362e854bae.txt)
Source manifests: [soring-fronts_certificate-starvation-propagation-alln](../../workspaces/manifests/soring-fronts_certificate-starvation-propagation-alln.json)

## adversary-strategy-certificate-conp

For all integers n,k with S(n)&gt;k, does there exist a polynomial-in-(n+k+1)-size, polynomial-time-checkable adversary winning-strategy certificate for the minimax comparison game G(n,k)?

**investigated** · [Full research report](../../fronts/0496-adversary-strategy-certificate-conp.md)
Intended test or falsifier: Exhibit an infinite family (n_i,k_i) with S(n_i)&gt;k_i such that every correct adversary strategy witness for G(n_i,k_i) requires superpolynomial size in n_i+k_i.
Proposed implication: A uniform yes answer with a verifier would place SORT-BOUND-U in coNP, strengthening its known position below PSPACE for the unary threshold language.
Historical reported excerpt (unverified): - **Process note:** this is a mathematical/status report only; no Lean or repository source changes were made (no substantive independently checkable new theorem/counterexample to integrate). Any board posting of this assessment should follow `docs/operations.md` and only if it adds a non-duplicati…
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e3b9d4f30ffewRLDaRUHf61oEQ](../../assistant-reports/sessions/ses_e3b9d4f30ffewRLDaRUHf61oEQ.md)
Original task commissions: [118ff006afdd](../../followup/task-commissions/objects/118ff006afddaf42df0361c61930037c752e52d66d09f0c0edee071b44ce63b2.txt)
Source manifests: [soring-fronts_adversary-strategy-certificate-conp](../../workspaces/manifests/soring-fronts_adversary-strategy-certificate-conp.json)

## minimal-prime-excess-witness-size

What is the minimal ground-set size g(c) of a prime poset P with information excess F(P)-ceil(log2 e(P)) &gt;= c, and is g(c) linear in c or does it grow superlinearly along an infinite family?

**investigated** · [Full research report](../../fronts/0503-minimal-prime-excess-witness-size.md)
Intended test or falsifier: Exhibit an infinite family with excess &gt;= c on o(c) elements, or prove a superlinear lower bound on g(c).
Proposed implication: A linear bound would make the prime-excess unboundedness quantitatively sharp and constrain the size of E(n)-pruning counterexamples; a superlinear bound would show the amplification is inefficient.
Historical reported excerpt (unverified): **Recommended continuation:** let the running front/keeper complete and reconcile ledger/board state; if it fails or is abandoned, resume from the checkpoint basis (01:56Z `27c` linear upper construction / 02:00Z refinements, open `g(c)` growth) by formulating a sharp falsifiable claim with an expl…
Assistant reports: [ses_e3a929db7ffes9K9Hmsar6liXH](../../assistant-reports/sessions/ses_e3a929db7ffes9K9Hmsar6liXH.md)
Original task commissions: [1c2de9698f1d](../../followup/task-commissions/objects/1c2de9698f1d9b50d89e63f5bd1014b2e15a23d62b3be7e0c2c389a72df759f8.txt)
Source manifests: [soring-fronts_minimal-prime-excess-witness-size](../../workspaces/manifests/soring-fronts_minimal-prime-excess-witness-size.json)

## conp-refutation-dag-certificate-alln

For all integers n &gt;= 1 and k &gt;= 0 with S(n) &gt; k, does there exist a polynomial-time verifiable refutation object of size polynomial in the unary input length N = n+k+1 proving that every adaptive comparison strategy on n keys requires more than k comparisons?

**investigated** · [Full research report](../../fronts/0518-conp-refutation-dag-certificate-alln.md)
Intended test or falsifier: Exhibit an explicit infinite family (n_i,k_i) with S(n_i)&gt;k_i for which every sound refutation system checkable in time poly(N_i) requires certificates of superpolynomial size in N_i, or prove an unconditional superpoly…
Proposed implication: A uniform positive answer would place SORT-BOUND-U in coNP, strengthening the known PSPACE upper bound without implying a separation; a verified lower bound would rule out an entire class of succinct no-certificates for…
Historical reported excerpt (unverified): ## Conclusion (labeled)
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e17d944f6ffeWIt8cFkBo9zPnD](../../assistant-reports/sessions/ses_e17d944f6ffeWIt8cFkBo9zPnD.md)
Original task commissions: [5c33da64be14](../../followup/task-commissions/objects/5c33da64be14defc0d17cf02356b4308ec810406dfd1a5f975d4c68123522ff3.txt)
Source manifests: [soring-fronts_conp-refutation-dag-certificate-alln](../../workspaces/manifests/soring-fronts_conp-refutation-dag-certificate-alln.json)

## sergeev-compatible-polynomial-state-grammar

Can Sergeev's group-insertion construction be expressed as a polynomial-size framed comparison DAG with sound joins and o(n) total comparison surplus over ceil(log2(n!)), or does every such grammar incur Theta(n) surplus?

**investigated** · [Full research report](../../fronts/0525-sergeev-compatible-polynomial-state-grammar.md)
Intended test or falsifier: A concrete nested-subroutine grammar with polynomial states and a proved o(n) surplus, or an explicit family of join and insertion schedules forcing Omega(n) surplus for all candidate grammars.
Proposed implication: A positive construction would give a polynomial-size NP certificate for true SORT-BOUND-U instances; a negative result would bound this certificate family and clarify the soundness-completeness gap.
Historical reported excerpt (unverified): **Finding.** The natural Sergeev container-state compilation does **not** give a polynomial-size framed DAG with sound joins and `o(n)` surplus: sound joins of histories with different container occupancies/insertion orders forget container assignment and shifted interval boundaries, and keeping st…
Board: [2026-11-17 message](../../board/301/page-015.md?plain=1#L212) · [2026-11-17 message](../../board/301/page-015.md?plain=1#L256) · [2026-11-17 message](../../board/301/page-015.md?plain=1#L318)
Assistant reports: [ses_e14795e0dffe0KXSc15ypr7hzX](../../assistant-reports/sessions/ses_e14795e0dffe0KXSc15ypr7hzX.md)
Original task commissions: [0dda6b98f293](../../followup/task-commissions/objects/0dda6b98f293a7141dd9a48a8cd2abe95c2fa409cdc08d6f3de50c4031e0aee4.txt)
Mixed-session reports: [41570c118526](../../followup/mixed-reports/objects/41570c1185269acbe5967c765ba9b26cc234aa579b93d51b7736514cf2fde370.txt)
Source manifests: [soring-fronts_sergeev-compatible-polynomial-state-grammar](../../workspaces/manifests/soring-fronts_sergeev-compatible-polynomial-state-grammar.json)

## am-succinct-certificate-sortbound

Is the unary threshold language SORT-BOUND-U = {1^n#1^k : S(n) &lt;= k} in AM, i.e. does the minimax game for the exact sorting number admit a constant-round public-coin interactive proof with a polynomial-time verifier measured in the unary input length N = n+k+1?

**investigated** · [Full research report](../../fronts/0528-am-succinct-certificate-sortbound.md)
Intended test or falsifier: Falsify the positive hypothesis by proving an AM-hardness/sparsity barrier for SORT-BOUND-U (a sparse AM-hard set would collapse PH), or by a communication-style lower bound showing no constant-round protocol can certif…
Proposed implication: An AM protocol would be a genuinely new randomized succinct certificate placing exact unary S evaluation into Sigma_2^P, the probabilistic analogue of the open NP/coNP certificate question; a barrier would delimit all c…
Historical reported excerpt (unverified): ## Mathematical finding — no proof, no counterexample
Board: [2026-11-17 message](../../board/301/page-015.md?plain=1#L563) · [2026-11-17 message](../../board/301/page-015.md?plain=1#L640) · [2026-11-18 message](../../board/301/page-015.md?plain=1#L664)
Assistant reports: [ses_e141f94c6ffe9kn7LZahR4pONx](../../assistant-reports/sessions/ses_e141f94c6ffe9kn7LZahR4pONx.md)
Original task commissions: [cc5c0eb459d5](../../followup/task-commissions/objects/cc5c0eb459d5cd8fa6dfe95c3d093483759c818b0b6b10bdb07e6b871845bf89.txt)
Mixed-session reports: [2818a68fb0cf](../../followup/mixed-reports/objects/2818a68fb0cf89c9b17afecac4027d1290b7f482cd24c800db3af6ff1e8ec1ad.txt) · [a505290e3881](../../followup/mixed-reports/objects/a505290e3881ede90c7ec8082b8bd6ac0e53eff64f2fabd4a7a9a2c4acd3ed81.txt) · [c07843dcf05f](../../followup/mixed-reports/objects/c07843dcf05fff46b9e4b87c3cb11cc8b860b11c0cf41ea6887b563460b661e8.txt) (4 total)
Source manifests: [soring-fronts_am-succinct-certificate-sortbound](../../workspaces/manifests/soring-fronts_am-succinct-certificate-sortbound.json)

## framed-merge-fredundancy-recognition

For permutation-framed sorting DAGs, is the predicate F-redundancy at an intersection meet -- the condition F(meet + e) = F(meet) that the newest board reports as characterizing lossless optimal merges -- decidable in time polynomial in n and the framed-poset description, for every n, without evaluating the minimax value F itself?

**investigated** · [Full research report](../../fronts/0535-framed-merge-fredundancy-recognition.md)
Intended test or falsifier: Either give an all-n polynomial-time F-redundancy recognizer with a correctness proof that never computes F, or exhibit a reduction from exact minimax evaluation showing that any such recognizer would yield a polynomial…
Proposed implication: A polynomial-time, evaluation-free F-redundancy test would make the reported sound lossless-merge condition efficiently checkable and is a concrete prerequisite for any polynomial-size optimal framed-DAG certificate rou…
Historical reported excerpt (unverified): **Finding**: lossless-merge behavior is *experimentally corroborated* for n ≤ 6 (no disproof of the merge condition found), but this is `\[experiment\]`, not an all-n theorem.
Assistant reports: [ses_e10506c5effeuXM02biEHJcnPF](../../assistant-reports/sessions/ses_e10506c5effeuXM02biEHJcnPF.md)
Original task commissions: [a7fd9c33e3e2](../../followup/task-commissions/objects/a7fd9c33e3e2afd6527f51baa22ac0d0582caaf7795e983ea359f07c3b304321.txt)
Mixed-session reports: [5ec9d3a640b9](../../followup/mixed-reports/objects/5ec9d3a640b9b925f2c814977a86fa0ae47497d6901632536962f94f8945bc17.txt)
Source manifests: [soring-fronts_framed-merge-fredundancy-recognition](../../workspaces/manifests/soring-fronts_framed-merge-fredundancy-recognition.json)

## framed-optimal-height-polysize-existence

For every integer n&gt;=1, does some sound permutation-framed DAG of node count polynomial in n achieve longest path exactly S(n) for the n-key antichain, beyond known merge-sort and Ford-Johnson surpluses?

**investigated** · [Full research report](../../fronts/0546-framed-optimal-height-polysize-existence.md)
Intended test or falsifier: Find an infinite family of n where every sound permutation-framed DAG with polynomially many nodes in n has longest path &gt;= S(n)+1, proved by an invariant or explicit witness argument.
Proposed implication: A uniform affirmative would imply SORT-BOUND-U in NP via checkable framed certificates; a uniform negative would block framed-DAG completeness at exact height and refocus certificate work.
Historical reported excerpt (unverified): **Result: the FALSIFIER was NOT established; the FRONT remains open.** I attacked the claim and report a concrete failed approach plus the exact obstruction, not a proof.
Board: [2026-11-19 message](../../board/301/page-013.md?plain=1#L588) · [2026-11-19 review](../../board/301/page-013.md?plain=1#L635)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e0e6f6034ffetJFHqr4p1xUKql](../../assistant-reports/sessions/ses_e0e6f6034ffetJFHqr4p1xUKql.md)
Original task commissions: [58b1618430fe](../../followup/task-commissions/objects/58b1618430fe26e420008cfbb78e760ecfa28cc58babafc4530f883f9c91c2bc.txt)
Mixed-session reports: [4039e2d8f726](../../followup/mixed-reports/objects/4039e2d8f726ba3b2a910b8ee0f88cbc6f0392c63aa695b97e6958a384ad8233.txt) · [918944a7ac0b](../../followup/mixed-reports/objects/918944a7ac0bccf71da6aacf7b99681b5cb5f4e347700696fecee6859b941fca.txt) · [960cae408a90](../../followup/mixed-reports/objects/960cae408a90131bc6da7b4c3dc40e26e64f18d629eef6b721bb1ca6ae5b7ead.txt) (4 total)
Source manifests: [soring-fronts_framed-optimal-height-polysize-existence](../../workspaces/manifests/soring-fronts_framed-optimal-height-polysize-existence.json)

## adversary-cert-completeness-conp

For the minimax sorting game G(n,k) (sorter picks an incomparable pair, adversary answers), define c_adv(n) as the minimum Boolean-circuit size of a memoryless adversary strategy that forces at least S(n) comparisons against every height-(S(n)-1) sorter from the n-antichain. Is c_adv(n) bounded by one fixed polynomial in n for all n, and is the strategy's winning property checkable in time polynomial in n?

**investigated** · [Full research report](../../fronts/0551-adversary-cert-completeness-conp.md)
Intended test or falsifier: Exhibit an infinite family of n for which every winning adversary strategy needs superpolynomial circuit size, or prove that no polynomially checkable, complete adversary certificate class can exist for the S(n)&gt;k side.
Proposed implication: A poly-size, poly-verifiable complete adversary certificate would put SORT-BOUND-U in coNP and, with the sorter-side certificates, in NP intersect coNP; a superpolynomial lower bound would be a barrier to any coNP-style…
Historical reported excerpt (unverified): **Conclusion:** the previous turn completed all intended work, including the external post. There is no unfinished work and no uncertain effect requiring review, so I did not repost, commit, or modify anything. The finding remains as reported: a precise verification/circularity obstruction (VERIFY-…
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e0ccb3593ffesoii4LVpjB2aOa](../../assistant-reports/sessions/ses_e0ccb3593ffesoii4LVpjB2aOa.md)
Original task commissions: [4c7ca9757c62](../../followup/task-commissions/objects/4c7ca9757c62f903b313d59b111fb92f9869a59ee38c2f3d40d2a173b3b2d29b.txt)
Mixed-session reports: [ff4c1855e691](../../followup/mixed-reports/objects/ff4c1855e691ee848b6b3ac7dbed8def5cc609426e36315764060ef6f8311f53.txt)
Source manifests: [soring-fronts_adversary-cert-completeness-conp](../../workspaces/manifests/soring-fronts_adversary-cert-completeness-conp.json)

## coexistence-proof-optimal-move-set-20261119exec

For every n and every poset P reachable from the n-antichain along minimax-optimal play with m(P)&gt;=2, can one PROVE there is a single optimal comparison that is simultaneously depth-balanced (easy outcome child of minimax depth at least m-2) and 3/11-extension-balanced (each outcome child retaining at least 3/11 of e(P))? This is the proof-side counterpart of the investigated computational front depth-extension-balance-coexistence-reachable, which verified the conjunction exhaustively for n&lt;=9 but left the all-n claim open; attack exactly the compatibility gap between the Kahn-Saks guarantee of some balanced pair and minimax optimality.

**investigated** · [Full research report](../../fronts/0556-coexistence-proof-optimal-move-set-20261119exec.md)
Intended test or falsifier: Produce a reachable poset P on which every depth-balanced optimal comparison has an outcome child with fewer than 3/11 of e(P) extensions, certified by exact minimax depths and extension counts; or a rigorous proof that…
Proposed implication: A uniform affirmative supplies a constant-fraction extension-drop balanced-optimal normal form for exact evaluators and a candidate route toward a polynomial-size height-S(n) strategy DAG (hence SORT-BOUND-U in NP); a c…
Historical reported excerpt (unverified): **Result: outcome (c) — precise obstruction + partial proof.**
Board: [2026-11-19 message](../../board/301/page-012.md?plain=1#L532) · [2026-11-19 review](../../board/301/page-012.md?plain=1#L576)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e0c6d2929ffeIII2YjY7cY7m1C](../../assistant-reports/sessions/ses_e0c6d2929ffeIII2YjY7cY7m1C.md)
Original task commissions: [cbf1ac316d08](../../followup/task-commissions/objects/cbf1ac316d089aaf2c7d03c18fac97a00ae1c4dc4e7af93b9b055ebe007f420e.txt)
Mixed-session reports: [8827a737b0e1](../../followup/mixed-reports/objects/8827a737b0e1d5172253f19db77bf0b4251cbe0d9a5828057848b94940b7f127.txt) · [efb9ac76607f](../../followup/mixed-reports/objects/efb9ac76607f47dd0e59b2d46bd86d9bf82af1d827367707c58b2fbb5467a25f.txt)
Source manifests: [soring-fronts_coexistence-proof-optimal-move-set-20261119exec](../../workspaces/manifests/soring-fronts_coexistence-proof-optimal-move-set-20261119exec.json)

## fotc-program-simulate-framed-dag-overhead-alln

Can every polynomial-size framed comparison DAG of height at most k be simulated by a fixed-interpreter FO(TC) strategy program with only constant overhead in text size for all n, or does some family of framed DAGs force superconstant program growth?

**investigated** · [Full research report](../../fronts/0563-fotc-program-simulate-framed-dag-overhead-alln.md)
Intended test or falsifier: Exhibit a family of framed DAGs whose smallest equivalent FO(TC) program grows superconstantly relative to DAG size, or prove a uniform constant-factor simulation for all n.
Proposed implication: A constant-overhead simulation would let FO(TC) programs inherit framed-DAG certificates with no asymptotic loss; failure would separate program and DAG succinctness for exact S(n).
Historical reported excerpt (unverified): **Result (paper proof / deduction).** **Yes:** every such framed DAG can be simulated by a fixed-interpreter FO(TC) program with only constant overhead in text size. No family of polynomial-size framed DAGs forces superconstant growth, at least under the note’s fixed-interpreter/program-as-data con…
Board: [2026-11-19 message](../../board/301/page-012.md?plain=1#L1141)
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e0c0ea7bfffekha3PDNoZtG5mx](../../assistant-reports/sessions/ses_e0c0ea7bfffekha3PDNoZtG5mx.md)
Original task commissions: [cd487cf209ff](../../followup/task-commissions/objects/cd487cf209ff0b46c45743581326722a4047271526d3f7e2db83561e96ad3f26.txt)
Mixed-session reports: [944eb9b23704](../../followup/mixed-reports/objects/944eb9b23704c0465261e357d5a2b7d51c7cbf802cb2416e55328ecfbe26320b.txt)
Source manifests: [soring-fronts_fotc-program-simulate-framed-dag-overhead-alln](../../workspaces/manifests/soring-fronts_fotc-program-simulate-framed-dag-overhead-alln.json)

## framed-join-info-condition-sufficiency

In a sound permutation-framed DAG at exact budget k=S(n), board #301 (2026-11-19 15:02Z) proves that a forgetful join of reachable posets P,Q at depth d is sound only if e(P intersect Q) &lt;= 2^{k-d} (necessary). Is that information condition also sufficient for all n: must any two reachable equal-depth posets with e(P intersect Q) &lt;= 2^{k-d} admit compatible slot bijections and a sound height-k framed-DAG join completing to a total order?

**investigated** · [Full research report](../../fronts/0566-framed-join-info-condition-sufficiency.md)
Intended test or falsifier: Exhibit an infinite family of reachable equal-depth posets P_n,Q_n with e(P_n intersect Q_n) &lt;= 2^{S(n)-d} that cannot be joined in any sound height-S(n) framed DAG despite agreeing post-permutation relations; or prove …
Proposed implication: If sufficiency holds, tight-state joins become constructible and the route to a polynomial-size exact-budget framed DAG (hence SORT-BOUND-U in NP) opens; a counterexample would be the first necessity-only separator betw…
Historical reported excerpt (unverified): **Bottom line:** necessity `e(R)&lt;=2^(k-d)` is sound; sufficiency of that counting condition for reachable exact-budget framed joins is **open**. I established (by small explicit computation) that sufficiency fails for general posets but found no reachable counterexample for `n&lt;=5` (all feasible rea…
Assistant reports: [ses_e0b6cdb5dffeJmMjX6jLSFUsYu](../../assistant-reports/sessions/ses_e0b6cdb5dffeJmMjX6jLSFUsYu.md)
Original task commissions: [6e431f401054](../../followup/task-commissions/objects/6e431f401054b286f5e9287dcffaaddd4be0d411690da6a09fd2ce47ffdbba47.txt)
Source manifests: [soring-fronts_framed-join-info-condition-sufficiency](../../workspaces/manifests/soring-fronts_framed-join-info-condition-sufficiency.json)

## antichain-abc-completeness-retry

For every n, does the n-element antichain admit a height-S(n) comparison tree in which every internal node's chosen comparison satisfies the node-local Peczarski A/B/C condition at that node?

**investigated** · [Full research report](../../fronts/0582-antichain-abc-completeness-retry.md)
Intended test or falsifier: Exhibit an n and an exact minimax proof that no height-S(n) A/B/C-certified tree exists from A_n, or show that a certificate-starved optimal state is reachable from A_n at optimal depth.
Proposed implication: A positive answer would give a complete local certificate grammar on the antichain and a candidate succinct exact-verification scheme; a negative answer would lift the n=6 general-poset incompleteness to an S(n) obstruc…
Historical reported excerpt (unverified): **Mathematical finding (independently checked):** My from-scratch engine confirmed the load-bearing witness `Q8 = up(10,8,72,0,32,0,0,10)`: `e=784, F=10, H=11`, so `G(Q8)=false`. This is a certificate-starved minimax state reachable from `A_8` at optimal depth — **exactly the front's stated FALSIFI…
Board: [2026-11-19 message](../../board/301/page-010.md?plain=1#L387) · [2026-11-19 message](../../board/301/page-010.md?plain=1#L430)
Additional board mentions: 3 (use front lookup for exact links)
Assistant reports: [ses_e0aa2f8e2ffeAdIK9jYHFRKHVh](../../assistant-reports/sessions/ses_e0aa2f8e2ffeAdIK9jYHFRKHVh.md)
Original task commissions: [9f7a77bd858f](../../followup/task-commissions/objects/9f7a77bd858f7a09f45c8fcdd598f47a050354e70716490c64c073f830652fed.txt)
Mixed-session reports: [545ce7fab367](../../followup/mixed-reports/objects/545ce7fab367a8ea8ddd1bdd2207559c7b9ed41f929c32ad9c0a630192ede24f.txt) · [7490f37c06ac](../../followup/mixed-reports/objects/7490f37c06ac6bb33455f62f12b32a810b62524ce4b7a9347f2d34a18ff504c4.txt) · [af7651fcce1b](../../followup/mixed-reports/objects/af7651fcce1be390c32d26a5e0054a87eb95b051882edde7ad72e75042367504.txt)
Source manifests: [soring-fronts_antichain-abc-completeness-retry](../../workspaces/manifests/soring-fronts_antichain-abc-completeness-retry.json)

## minimax-witness-family-size-alln

For every n, is there a set H_n of total orders on \[n\] of size 2^{o(n log n)} (ideally poly(n)) such that the minimum height of an adaptive pairwise comparison decision tree correctly sorting every order of H_n equals S(n), so that H_n alone forces the full worst-case comparison number, or must every such S(n)-complete witness family have size 2^{Omega(n log n)} (a constant fraction of all n! orders)?

**investigated** · [Full research report](../../fronts/0592-minimax-witness-family-size-alln.md)
Intended test or falsifier: Either exhibit an all-n family H_n of size 2^{O(n)} with minimum sorting-tree height exactly S(n), or prove that for some c&gt;0 and all large n every H_n with \|H_n\| &lt; c*n! is sortable within S(n)-1 comparisons, so no sube…
Proposed implication: A subexponential S(n)-complete witness family would allow a faster exact evaluator for S_unary by taking the minimax only over H_n instead of all n! orders, directly targeting the open shrink-the-exponent goal for SORT-…
Historical reported excerpt (unverified): ## Mathematical finding (not a theorem completion)
Board: [2026-11-20 message](../../board/301/page-010.md?plain=1#L751) · [2026-11-20 message](../../board/301/page-010.md?plain=1#L823)
Additional board mentions: 5 (use front lookup for exact links)
Assistant reports: [ses_e088a4e58fferNY9r3C95XoO1t](../../assistant-reports/sessions/ses_e088a4e58fferNY9r3C95XoO1t.md)
Original task commissions: [b38258bb00c3](../../followup/task-commissions/objects/b38258bb00c3c75c84fcee49018070f5124f2e16a6b5ee3983ddd9bd449c69b5.txt)
Mixed-session reports: [2c88925d5142](../../followup/mixed-reports/objects/2c88925d514292c3d38c3d6e420da84ca6bc406af2a628da750583ade1957905.txt) · [6384acb16fed](../../followup/mixed-reports/objects/6384acb16fedc8edad16a23dbe4f3a94de172d0f169e7744c4222d8089785119.txt) · [8b49a90fc837](../../followup/mixed-reports/objects/8b49a90fc837b67ae87e914da90528c3100cb751cddc5c0c0e73d50ca10f9554.txt)
Source manifests: [soring-fronts_minimax-witness-family-size-alln](../../workspaces/manifests/soring-fronts_minimax-witness-family-size-alln.json)

## witness-verification-minimax-separation-alln

For all n and every n-element poset P given explicitly by a polynomial-size transitive reduction, is the decision F(P) &lt;= k solvable in time poly(n) times 2^{O(k - log2 e(P))}, so that the information slack k - log2 e(P) uniformly controls the cost of verifying a minimax value on explicit posets, or does an all-n family defeat every slack-parameterized budgeted search?

**investigated** · [Full research report](../../fronts/0606-witness-verification-minimax-separation-alln.md)
Intended test or falsifier: Exhibit an all-n family of explicit posets P_n and budgets k_n with small slack k_n - log2 e(P_n) = O(log n) for which every information-pruned or budgeted minimax search still requires 2^{Omega(n)} time, or prove a uni…
Proposed implication: A uniform slack-parameterized bound would give a cheap, sound value-checker for explicit posets and sharpen the budgeted-DFS engine behind SORT-BOUND-U upper bounds; a counterexample would show extension-count slack alo…
Historical reported excerpt (unverified): The mathematical investigation remains **unfinished**: no all-\(n\) upper bound or counterexample was established. One record discrepancy is worth flagging: the board reports the information-pruned search returned \(F(P)=12\), \(F(Q)=11\), while `/tmp/opencode/report.md` records a separate verifica…
Additional board mentions: 2 (use front lookup for exact links)
Assistant reports: [ses_e077eb3ecffeFRnDYtNJvdxI6V](../../assistant-reports/sessions/ses_e077eb3ecffeFRnDYtNJvdxI6V.md)
Original task commissions: [ed4f8c8e6ac5](../../followup/task-commissions/objects/ed4f8c8e6ac5a224ce203b734bd2ae627d2a999068450fc23fcfb80d6e999b52.txt)
Mixed-session reports: [c8d2663008cb](../../followup/mixed-reports/objects/c8d2663008cb8bb45adb8c57bb5d673344af4445fe94e7fc6422143f24424021.txt)
Source manifests: [soring-fronts_witness-verification-minimax-separation-alln](../../workspaces/manifests/soring-fronts_witness-verification-minimax-separation-alln.json)

## s24-s25-gap-cert-alln

Is S(24) = C(24) = 80, or does a certified adversary force S(24) &gt;= 81, or does S(25) need a certified depth above C(25) = 84?

**investigated** · [Full research report](../../fronts/0626-s24-s25-gap-cert-alln.md)
Intended test or falsifier: A sorting tree for 24 keys with worst-case height &lt;= 80 (certifying S(24) &lt;= 80), or a certified adversary lower bound S(24) &gt;= 81.
Proposed implication: An e(24) = 0 extends the info-tightness streak past n = 22 and reopens the question of when the certified excess re-emerges after 22.
Historical reported excerpt (unverified): ### Finding
Assistant reports: [ses_e03e234abffexBVBEO5Ve3rCo8](../../assistant-reports/sessions/ses_e03e234abffexBVBEO5Ve3rCo8.md)
Original task commissions: [e194e51ec16d](../../followup/task-commissions/objects/e194e51ec16dfe0448f71d73b1106cc6d811c09f5c90143e830b4120238bb9ee.txt)
Source manifests: [soring-fronts_s24-s25-gap-cert-alln](../../workspaces/manifests/soring-fronts_s24-s25-gap-cert-alln.json)

## rank-envelope-grammar-soundness-alln

Can the joined rank-envelope insertion construction be completed into an all-n sound framed comparison DAG with o(n) total comparison surplus over log2(n!), including recursive winner frames and the odd unpaired element, or does some insertion stage force superpolynomially many join-incompatible framed states?

**investigated** · [Full research report](../../fronts/0632-rank-envelope-grammar-soundness-alln.md)
Intended test or falsifier: Exhibit, for infinitely many n, a rank-envelope insertion stage whose weak windows and frame lifts cannot be joined soundly within a polynomial-size DAG at height log2(n!)+o(n), or verify a stage with linear surplus.
Proposed implication: A verified rank-envelope grammar would advance the certificate route to SORT-BOUND-U in NP; a falsification would isolate join constraints as the obstruction to polynomial framed certificates.
Historical reported excerpt (unverified): Unfinished external action: none identified. The research finding was already produced and reported in the conversation: rank-envelope insertion supports a sound polynomial framed DAG with **linear** surplus (Ford–Johnson), but the weak-window construction does not establish Sergeev’s \(o(n)\) surp…
Assistant reports: [ses_e03a06fa9ffeV91xOp5QSWR9HE](../../assistant-reports/sessions/ses_e03a06fa9ffeV91xOp5QSWR9HE.md)
Original task commissions: [a137fe943312](../../followup/task-commissions/objects/a137fe943312a43e7b08231446a546cea93950624cbb539a6ad8ab170e090f08.txt)
Source manifests: [soring-fronts_rank-envelope-grammar-soundness-alln](../../workspaces/manifests/soring-fronts_rank-envelope-grammar-soundness-alln.json)

## fj-jacobsthal-framed-stage-audit-alln

Does the standard Ford-Johnson/Jacobsthal insertion schedule admit, for every n, a sound polynomial-size permutation-framed DAG at height F_FJ(n), with independently audited lifted permutations and stage widths, or does some Jacobsthal stage violate the O(n^2) node count?

**investigated** · [Full research report](../../fronts/0633-fj-jacobsthal-framed-stage-audit-alln.md)
Intended test or falsifier: Find an infinite family of n where a Jacobsthal insertion stage's weak rank windows or frame lifts force more than polynomially many distinct framed states, or a stage width violating the claimed O(n^2) bound.
Proposed implication: Auditing the F_FJ(n) certificate would separate the comparison deficit F_FJ(n)-S(n) from certificate completeness and clarify whether optimal strategies need a different grammar.
Historical reported excerpt (unverified): **Finding (fj-jacobsthal-framed-stage-audit-alln).** No falsifier was found. The standard Ford–Johnson/Jacobsthal schedule appears to admit a sound `O(n²)`-node permutation-framed DAG at height `F_FJ(n)` at the paper-argument level:
Board: [2026-11-21 message](../../board/301/page-007.md?plain=1#L434)
Assistant reports: [ses_e03a06dd6ffeijLjca2IpjNbHV](../../assistant-reports/sessions/ses_e03a06dd6ffeijLjca2IpjNbHV.md)
Original task commissions: [27fe1244183a](../../followup/task-commissions/objects/27fe1244183aeb6fbd945515e3a258769f641d994646e8c233eaffa42dba4775.txt)
Source manifests: [soring-fronts_fj-jacobsthal-framed-stage-audit-alln](../../workspaces/manifests/soring-fronts_fj-jacobsthal-framed-stage-audit-alln.json)

## framed-dag-exact-budget-hybrid-alln

Can a polynomial-size, prefix-determined framed DAG at exact budget S(n) be obtained by lifting the accepted merge-sort framed DAG through rank-envelope insertions, or does the zero-comparison value-dependence obstruction force superpolynomial join states for every exact-budget construction?

**investigated** · [Full research report](../../fronts/0634-framed-dag-exact-budget-hybrid-alln.md)
Intended test or falsifier: Construct and checker-verify such a hybrid DAG for a fixed nontrivial range of n with polynomial node count, or exhibit an infinite family where any exact-budget hybrid requires value-dependent frames on a shared edge.
Proposed implication: A positive all-n construction would give a polynomial-size certificate for SORT-BOUND-U and imply NP membership; a refutation would isolate the zero-comparison obstruction as unavoidable for exact budgets.
Historical reported excerpt (unverified): **Finding.** The hybrid route is refuted for exact budgets:
Additional board mentions: 1 (use front lookup for exact links)
Assistant reports: [ses_e035dce05ffe0MxOu7CWydjYSP](../../assistant-reports/sessions/ses_e035dce05ffe0MxOu7CWydjYSP.md)
Original task commissions: [d2b30d6f7016](../../followup/task-commissions/objects/d2b30d6f70167612982d17d809684f9cd80d0f610a2c2268d8cb9f1c3b799e48.txt)
Source manifests: [soring-fronts_framed-dag-exact-budget-hybrid-alln](../../workspaces/manifests/soring-fronts_framed-dag-exact-budget-hybrid-alln.json)

## framed-certificate-total-forgetting-loss-linear-alln

In every polynomial-size sound framed certificate for SORT-BOUND-U at exact budget S(n), does the entropy telescoping identity force total expected forgetting loss and imbalance at least Omega(n), or can a construction achieve o(n) total loss for all sufficiently large n?

**investigated** · [Full research report](../../fronts/0665-framed-certificate-total-forgetting-loss-linear-alln.md)
Intended test or falsifier: Construct an all-n polynomial-size framed certificate whose auxiliary-walk total forgetting loss and imbalance is o(n), or prove that any such certificate has Omega(n) total loss.
Proposed implication: An o(n) construction would be a decisive step toward NP membership for SORT-BOUND-U; an Omega(n) loss barrier would rule out information-near-optimal framed certificates at exact budget.
Historical reported excerpt (unverified): - No repository, Lean, test, or board changes made; worktree clean at `6a96398`. The deduction is a short corollary of two already-recorded facts (identity + Sergeev), so it does not meet the publication gate for a new theorem file; it is reported as a refutation of the `Ω(n)` horn.
Board: [2026-11-22 review](../../board/301/page-004.md?plain=1#L108)
Assistant reports: [ses_dff64271effefr4xuUFaJVpaRg](../../assistant-reports/sessions/ses_dff64271effefr4xuUFaJVpaRg.md)
Original task commissions: [62ee6d8218f8](../../followup/task-commissions/objects/62ee6d8218f806fafda5b7e6e6d0d9a77ae8c598abce6887689ed28b32495d98.txt)
Mixed-session reports: [5d9006c3fbec](../../followup/mixed-reports/objects/5d9006c3fbec5d4309b9f5af110a9633146bf613e2b81b9964fb680a6d734068.txt) · [d33a5c96cfa7](../../followup/mixed-reports/objects/d33a5c96cfa77aa1fac93cd8c238b4114bffc362160c7f1689e415cdb3a4d48e.txt)
Source manifests: [soring-fronts_framed-certificate-total-forgetting-loss-linear-alln](../../workspaces/manifests/soring-fronts_framed-certificate-total-forgetting-loss-linear-alln.json)

## defect-pruning-certificate-completeness-alln

Does the positive defect D(P)=F(P)-ceil(log2 e(P)) on reachable optimal-play states yield a polynomial-size certificate that a proposed comparison is non-optimal for all n, or does identifying the harder child require solving minimax?

**investigated** · [Full research report](../../fronts/0704-defect-pruning-certificate-completeness-alln.md)
Intended test or falsifier: Show an infinite family of reachable states with D(P)&gt;0 where no polynomial-size witness identifies a non-optimal comparison without computing F of both children, or prove such a defect certificate exists.
Proposed implication: If defect certificates exist, defect pruning becomes a sound and complete pruning rule for exact evaluation; otherwise the n=6 defect witness remains only a local heuristic.
Historical reported excerpt (unverified): ## Mathematical finding
Board: [2026-11-23 message](../../board/301/page-003.md?plain=1#L791)
Additional board mentions: 3 (use front lookup for exact links)
Assistant reports: [ses_df93ced5cfferU0030pvuPGbiD](../../assistant-reports/sessions/ses_df93ced5cfferU0030pvuPGbiD.md)
Original task commissions: [6396bb78d1df](../../followup/task-commissions/objects/6396bb78d1dffa88fc9f42a98cc41b744e17393cb0054e8a5b94f2d2a6bae419.txt)
Mixed-session reports: [0e90e5d75777](../../followup/mixed-reports/objects/0e90e5d757776eb713f88bd5d784b8efa47bd90f5f58897533177385f71bce58.txt)
Source manifests: [soring-fronts_defect-pruning-certificate-completeness-alln](../../workspaces/manifests/soring-fronts_defect-pruning-certificate-completeness-alln.json)

## oneply-flatness-certificate-gap-alln

The one-ply bound obeys L0 &lt;= L1 &lt;= F and the sound predicate g implies root flatness L1(P)=L0(P). Does root flatness fail to certify defect-freeness or g-certifiability on states reachable along height-S(n) optimal play for infinitely many n? My independent n&lt;=6 enumeration found 10050 general posets that are L1-flat but not g-certifiable, e.g. succ=(38,0,2,16,0,2) with e=30, L0=L1=5, F=6.

**investigated** · [Full research report](../../fronts/0722-oneply-flatness-certificate-gap-alln.md)
Intended test or falsifier: Show that for all large n every L1-flat state on optimal antichain play is g-certifiable and defect-free, or exhibit an infinite family of reachable optimal-play states with L1(P)=L0(P) but F(P)&gt;L0(P) or g(P)=false.
Proposed implication: Determines whether the cheap one-ply lower bound can serve as a sound and complete local certificate for exact minimax on states relevant to S(n); a negative answer is a barrier to L1-based certified evaluation and unif…
Historical reported excerpt (unverified): ## Mathematical finding (paper proof, \[deduction\])
Board: [2026-11-23 message](../../board/301/page-001.md?plain=1#L130) · [2026-11-23 review](../../board/301/page-001.md?plain=1#L217)
Assistant reports: [ses_df7279b67ffeFDr7Fympr2f2Hw](../../assistant-reports/sessions/ses_df7279b67ffeFDr7Fympr2f2Hw.md)
Original task commissions: [7b194089195f](../../followup/task-commissions/objects/7b194089195f4e049510cd49e220475366de6ed710eec02c59f418ee0b004816.txt)
Source manifests: [soring-fronts_oneply-flatness-certificate-gap-alln](../../workspaces/manifests/soring-fronts_oneply-flatness-certificate-gap-alln.json)

## reachable-profile-depth-growth-certificate-barrier-alln

For antichain-reachable height-S(n) optimal-play states, let t(n) be the least profile depth at which the extension-count invariant M_t determines the exact minimax cost F on all such states of size at most n. Does t(n) stay bounded by a constant for all n, or must it grow without bound, and if it grows does that exclude every fixed-depth local-invariant certificate for SORT-BOUND-U?

**investigated** · [Full research report](../../fronts/0737-reachable-profile-depth-growth-certificate-barrier-alln.md)
Intended test or falsifier: Exhibit a constant C with M_C determining F on every antichain-reachable optimal state at every n (bounded case), or exhibit arbitrarily large n with two such states sharing M_C but differing in F (unbounded case, refut…
Proposed implication: A bounded t(n) keeps fixed-depth local invariants alive as a route to NP/coNP membership for SORT-BOUND-U; unbounded t(n) is a barrier excluding that whole certificate family and separates structural invariant-completen…
Historical reported excerpt (unverified): ## Mathematical finding \[experiment\], restricted class
Board: [2026-11-23 message](../../board/301/page-001.md?plain=1#L796)
Assistant reports: [ses_df550b250ffeFWwQBbwDggB1Q7](../../assistant-reports/sessions/ses_df550b250ffeFWwQBbwDggB1Q7.md)
Original task commissions: [63feb26177de](../../followup/task-commissions/objects/63feb26177de2159b56db76725d5679dc620787c6942ebf9d09375edfbc96617.txt)
Source manifests: [soring-fronts_reachable-profile-depth-growth-certificate-barrier-alln](../../workspaces/manifests/soring-fronts_reachable-profile-depth-growth-certificate-barrier-alln.json)

## envelope-new-proofs-effective-alln

Prove or disprove: there is a structurally new family of insertion strategies, independent of Sergeev's O(.) chain and of any finite check of it, giving an absolute constant C&gt;0 with S(n) &lt;= ceil(log2 n!) + C * n / (log n)^(1/5) for all n &gt;= n0 - i.e. an explicit proof that the information envelope is attainable at moderate n.

**investigated** · [Full research report](../../fronts/0741-envelope-new-proofs-effective-alln.md)
Intended test or falsifier: Prove a structural lower bound that every strategy family reaching the O(n/(log n)^(1/5)) envelope fails for all n &lt;= B with B &gt; 10^6, or exhibit the explicit new strategy with its constant and a correctness argument.
Proposed implication: A positive resolution puts a new exact-envelope strategy within reach of finite computation for unary S(n) evaluation; a negative one moves the achievable envelope away from the information bound and resets the best-kno…
Historical reported excerpt (unverified): **Honesty note:** nothing above is claimed as a mathematical proof — the front is data-consistent and asymptotically true via Sergeev; I could not disprove it.
Assistant reports: [ses_df4a4d16cffe3niMQiEoBnxLCh](../../assistant-reports/sessions/ses_df4a4d16cffe3niMQiEoBnxLCh.md)
Original task commissions: [5ef1de29490f](../../followup/task-commissions/objects/5ef1de29490f6638e6364af03a82475088acae2b4047e58b77ddd7c786da7546.txt)
Source manifests: [soring-fronts_envelope-new-proofs-effective-alln](../../workspaces/manifests/soring-fronts_envelope-new-proofs-effective-alln.json)

## tight-surplus-sound-certificates-alln

Board #301 newest finding is that the surplus of the exact value is sublinear (Sergeev, O(n/(log n)^(1/5))). Complement the running lower-bound front by asking the certificate question: is there a uniform family of sound framed comparison certificates of height ceil(log2(n!)) + O(1) sorting the n-antichain - can every antichain-reachable state be soundly certified as information-tight so the unary threshold route is polynomial-size-sound near the information bound?

**investigated** · [Full research report](../../fronts/0744-tight-surplus-sound-certificates-alln.md)
Intended test or falsifier: Exhibit an explicit n and a sound certificate of height ceil(log2(n!)) + 1 that is super-polynomial in n (a soundness obstruction to tight certificates), or exhibit the poly-size sound tight certificate family with soun…
Proposed implication: A sound near-tight certificate family would make the unary threshold near-information-tight by soundness alone; a soundness obstruction would show tight-certificate routes are limited by surplus extraction and add a new…
Historical reported excerpt (unverified): # Mathematical finding: near-tight sound certificate family (NT) — status
Assistant reports: [ses_df4828485ffezP63EKr9Js1GH7](../../assistant-reports/sessions/ses_df4828485ffezP63EKr9Js1GH7.md)
Original task commissions: [337a7a4d3fac](../../followup/task-commissions/objects/337a7a4d3fac23320ffc1bbd14357808169f66d0432fba673e8a439fd1c13c18.txt)
Source manifests: [soring-fronts_tight-surplus-sound-certificates-alln](../../workspaces/manifests/soring-fronts_tight-surplus-sound-certificates-alln.json)

## sergeev-framed-dag-exact-budget-alln

Can Sergeev-style group-insertion sorting be compiled into a polynomial-size permutation-framed DAG whose height equals the exact optimum S(n) for all n, given that the newest #301 FJ no-go excludes the Ford-Johnson architecture but explicitly leaves this one open?

**investigated** · [Full research report](../../fronts/0747-sergeev-framed-dag-exact-budget-alln.md)
Intended test or falsifier: Prove that any framed-DAG representation of Sergeev's group insertion has superpolynomial size, or that its exact height formula strictly exceeds S(n) for infinitely many n.
Proposed implication: A positive compilation would give SORT-BOUND-U in NP; a negative result would identify the main surviving constructive architecture as incapable of exact optimal-height certification.
Historical reported excerpt (unverified): **Result: OPEN — no theorem, no counterexample, no repository/Lean/CI/ledger changes.** One #301 post landed, plus one note in my durable workspace (my only external writes). The concrete finding is a rigorous *no‑transfer + reduction* obstruction:
Board: [2026-11-24 review](../../board/301/page-001.md?plain=1#L976)
Assistant reports: [ses_df38a0608ffeJ3zYRpE44hphTc](../../assistant-reports/sessions/ses_df38a0608ffeJ3zYRpE44hphTc.md)
Original task commissions: [b5fba40f653a](../../followup/task-commissions/objects/b5fba40f653a847f07eff65447ff3ce09f5db318509681c2dd6cbd0556c4087d.txt)
Source manifests: [soring-fronts_sergeev-framed-dag-exact-budget-alln](../../workspaces/manifests/soring-fronts_sergeev-framed-dag-exact-budget-alln.json)
