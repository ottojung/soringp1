# antonina-Dqxad2ARVcgj1Ym3e8KV57-peterson

Session: ses_e11988ff1ffe32bP7RFnysxOQb
Workspace: /home/lubko/soring-fronts/hooklength-pendant-realizability-nontight
Created: 1795001118805; updated: 1795001581916

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 209 (msg_1ee6cf1ec001Vt7Cc6iQGJ13oT)

# Report: hook-length pendant-merge realizability for non-tight `n` (board #301 front)

**Scope / sources studied (billy-dev checkout).** Read `AGENTS.md`, `docs/problem.md`, `docs/literature.md`, `docs/operations.md`, `docs/research-framed-certificate-frontier.md`, `scripts/check_framed_strategy.py`, and Antonina board #301 (digest + full bodies) for `cheap-coarsening-optimal-root-play` (2026-11-17T23:11:08Z), `pendant-anchor-realizability` (2026-11-17T23:57:41Z), `adversary-forced-nontightness` (2026-11-17T23:13:03Z), and `n8-alltight-resolution`. Primary literature anchors: Sergeev, ECCC TR20-096 (2020), `S(n)=log2(n!)+o(n)`; Stober–Weiß, ALENEX 2023 / arXiv:2206.05597, exact values incl. `S(12)=30 > C(12)=29`; standard rooted-forest/chain+pendant hook-length (linear-extension) counts as used in the framed-certificate frontier. No repository, Lean, test, or workflow changes were made.

## 1. Claim attacked (as stated) and precise reading

**Front.** For every non-tight `n` (`S(n) > C(n)`, `C(n)=ceil(log2(n!))`), does there exist an optimal minimax strategy tree for the `n`-antichain in which every internal node is either a standard comparison move or a realizable pendant-merge coarsening move whose validity follows from hook-length identities on the corresponding poset classes?  
**Falsifier.** Some non-tight `n` such that in every optimal-height strategy for the `n`-antichain, some internal node cannot be realized as any pendant-merge coarsening permitted by hook-length identities.  
**Stated implication.** Positive all-`n` ⇒ coarsening-based exact evaluator/normal form compressing optimal strategies for non-tight instances (potential uniform upper-bound improvement for `S(n)`); counterexample ⇒ delimits when structural coarsening applies.

**[definition/deduction] Literal model issue.** In the fixed comparison model (`docs/problem.md`, `SoringP1/Model.lean` minimax/`S_eq_adv_univ` context), a deterministic adaptive comparison *tree* has only comparison internal nodes. Hence “every internal node is either a standard comparison move or …” is vacuously satisfiable by any optimal comparison tree (all nodes are comparisons, no coarsening nodes), independent of non-tightness and hook-length identities; conversely a comparison tree cannot contain non-comparison merge/coarsening nodes. Coarsening/joins are features of a *strategy DAG/certificate* (cf. framed DAG, `scripts/check_framed_strategy.py`: joins arise by intersection of guaranteed relations at shared nodes), not of a tree. Therefore the claim is not well-typed as a strong normal form of comparison trees as literally written.

**[deduction] Substantive core (from #301 evidence).** The gap identified in `cheap-coarsening-optimal-root-play` is **realizability** of hook-length-style pendant merges along optimal play for non-tight `n`: existence, in some optimal-height strategy/DAG, of joins of *nonisomorphic* gapped-anchor pendant states (chain plus pendants, `e(P)` given by the rooted-forest hook-length formula) with sound intersection to a weak anchor, controlled forgetting `lambda`, and retained slack/budget. I attacked this core as the falsifiable mathematical content, while also assessing the stronger “every internal node/merge is of this form” reading.

## 2. Disproof attempts and analysis

### 2.1 Global reconvergence, not sibling-local (structural necessary condition)
**[deduction; consistent with #301 23:11Z, 23:57Z]** The hook-length pendant family (frontier §3 warning / #301 arithmetic) needs same-direction anchor diversity (e.g. anchors in `{3j,3j+1}`) so that distinct histories coalesce to a common weak-anchor state with small `lambda = log2(e(Q)/e(P))`. But the two outcomes of a single comparison on a pending element versus an anchor yield *complementary* constraints (`x < c_a` vs `c_a < x`, i.e. “≤a” vs “>a”), not `{a,a+1}`. Therefore any realizable nonisomorphic pendant-anchor merge requires **reconvergence of distant paths** at a common depth with compatible winning states in a DAG/strategy representation; it cannot be produced locally from sibling branches alone. This narrows realizability to a global property (path structure + budget compatibility) and blocks any purely local disproof *or* proof from single-comparison outcomes. It does **not** refute all-`n` realizability.

### 2.2 Slack/budget regime (necessary, not sufficient)
**[literature/experiment reported on #301; deduction]** For non-tight `n`, `S(n)-C(n) >= 1` so the root carries positive height-vs-information slack; exact reported values give first `>1`-bit slack at `n=12` (`log2(12!)=28.835`, `C=29`, `S=30`, slack `1.165`, Stober–Weiß/`research-plan` values as cited on board). For root/information-tight instances (`S=C`, slack `<1`), a complete height-`S(n)` framed certificate cannot sustain positive total forgetting while meeting the entropy/height accounting (and observed small tight cases admit isomorphism quotients, `lambda=0`); thus non-tightness is a necessary regime for nonzero-forgetting pendant merges in a complete optimal certificate, matching the claim’s restriction. It is not sufficient: meeting `lambda <=` global slack at example states does not imply those states are reachable as winning states on a common optimal path.

### 2.3 `n=12` evidence (smallest targeted non-tight case)
**[experiment reported on #301 23:57Z; deduction]** Ford–Johnson is optimal at `n=12` (`F_FJ(12)=30=S(12)`); after sorting winners it yields a chain of 6 plus 6 pendants with one-per-anchor (a comb permutation state), `e=10395` for all 720 assignments, so merges are **isomorphism quotients with `lambda=0`**, not nonisomorphic gapped-anchor coarsening. Gapped-anchor pendant states `{3,4}x{6,7}` are individually tight (`F=ceil(log2 e)`) with example `lambda` values (`0.61,0.42,0.19`) below `1.165`, but their realizability as common-depth winning states on any height-30 strategy was **not** established (and backward reachability attempts were explicitly discarded on board as incomplete). Thus the natural optimal `n=12` strategy does not realize the target phenomenon; realizability for *some* optimal `n=12` strategy remains **open**. I did not reproduce the n=12 optimal-strategy search (infeasible here, consistent with prior reported timeouts at `n>=7` for optimal-tree enumeration).

### 2.4 Exhaustive normal-form strength (“every internal node…”)
**[deduction]** If read over a DAG/strategy representation, the claim that every internal node is a standard comparison or a *pendant-merge coarsening move whose validity follows from hook-length identities on the corresponding poset classes* would forbid any other merge/coarsening types. Reachable states from the `n`-antichain are general partial orders; hook-length identities give closed `e(P)` formulas for special classes (e.g. rooted forests / chain+pendants), not for arbitrary posets. Hence an all-n, all-merges-of-this-special-form theorem would be extraordinarily strong and currently unsupported. However, I found **no** explicit non-tight `n` and no general proof that every optimal strategy must contain a non-pendant (or non-hook-length-validated) merge: certifying “for all optimal strategies” is beyond available enumeration/arguments.

### 2.5 Certificate soundness vs completeness (required distinction)
**[definition/deduction]** In the framed-DAG checker, an intersection join is **locally sound** with respect to guaranteed relations (it never adds unjustified knowledge). “Validity follows from hook-length identities” in this line of work refers to **counting/feasibility accounting** for pendant classes (`e(P)`, hence `lambda`, height/slack compatibility), not to the logical soundness of intersection. **Completeness/realizability** is separate: (i) reachability of the specific pendant states on some optimal root strategy, (ii) arrival at a common depth as winning states, and (iii, for compression aims) existence of enough such merges to yield a useful normal form. None of (i)-(iii) follows from hook-length identities or local join soundness alone.

### 2.6 General-poset results not transferred
**[deduction, model fidelity]** Hook-length/extension-count facts used here concern specific poset classes arising along plays from the fixed `n`-antichain root; hardness or counting phenomena for arbitrary partial orders do not transfer to `S(n)` without an encoding-preserving reduction, and are not invoked as such.

## 3. Serious falsification attempt — outcome

I attempted to refute the substantive claim by: (a) identifying a small non-tight `n` with a forced non-pendant/forbidden merge in every optimal strategy — `n=12` is the minimal >1-bit-slack case but optimal strategies are not exhaustively characterizable here; (b) deriving an all-`n` impossibility from the sibling-complementarity constraint — it rules out *local* sibling generation of the required diversity but not global DAG reconvergence; (c) finding a slack/entropy obstruction for the pendant family — reported examples at `n=12` fit within slack (`lambda << 1.165`). **No concrete counterexample and no all-`n` impossibility proof was obtained.** No realizability (existence) proof was obtained either.

## 4. Mathematical finding / exact obstruction (honest)

- **Finding [deduction].** The front, read literally as a property of “optimal minimax strategy trees”, is ill-typed/trivial in the standard comparison model (comparison trees have no coarsening/merge nodes; pure optimal trees satisfy the comparison disjunct vacuously but realize no pendant-merge coarsening). The substantive question is the all-`n` realizability, for non-tight `n`, of nonisomorphic hook-length-style pendant merges along some optimal-height strategy/DAG.
- **Status: open.** Neither proved nor disproved for all non-tight `n` (including the first targeted case `n=12`).
- **Exact obstruction (sharpened) [deduction + reported evidence].** Realizability requires **global** conditions beyond local soundness/hook-length counting: (1) distant-path reconvergence producing compatible gapped-anchor pendant states (sibling branches are complementary, not same-family), (2) common depth with winning states within the `S(n)` budget, and (3) merge forgetting compatible with available slack. Hook-length identities validate class extension counts/`lambda` accounting but do not certify (1)-(2). The natural optimal `n=12` strategy realizes only isomorphism (`lambda=0`) merges, so realizability is strategy-dependent and non-automatic.
- **On the exhaustive form.** A normal form claiming *every* merge/coarsening node is a hook-length-validated pendant merge is much stronger than current evidence supports and is not established; I also cannot produce a definitive all-strategies counterexample.

## 5. Complexity implication (careful)

**[deduction/conjectural scope]** A positive all-`n` realizability/normal-form result could, *if* such moves compose into sufficient compression with a checkable representation, aid a coarsening-based exact evaluator or succinct certificate for non-tight instances; by itself, existence of some pendant merges does not yield a polynomial-size complete framed DAG or an NP/cost bound (soundness ≠ completeness, and size/composition remain open). A counterexample would delimit this particular hook-length-pendant coarsening mechanism but would not by itself settle `SORT-BOUND-U` membership/separation questions. No complexity-class claim is made.

## 6. Limits

No theorem and no counterexample produced; no finite computation decided `n>=12` optimal realizability. Evidence from #301 posts is cited as reported (with labels) where not independently re-executed here; I did not audit those scratch computations beyond the logical/structural analysis above. The central realizability gap remains open and is, on current evidence, a global strategic property rather than a consequence of local hook-length/soundness facts.
