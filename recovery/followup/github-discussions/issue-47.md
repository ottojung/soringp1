# Issue #47: All-n optimal sorting: prove or refute complete polynomial framed strategy certificates

Upstream: https://github.com/ottojung/soringp1/issues/47
State: open
Created: 2026-10-22T19:49:25Z

## Objective

Find a **uniform, exact, polynomially verifiable certificate** for (S(n)le k), or rigorously kill a specific proposed compression model. The only target is the **unary** language `SORT-BOUND-U = {1^n#1^k : S(n)≤k}`, not generic-poset hardness and not the binary encoding.

**Execution policy:** Research can be written in GitHub while `billy-dev` is down. All remote agent execution, if/when restored, must run on **billy-dev only**. This is a mathematical investigation, **not** a Lean formalization task. Do not generate Lean source or spend CI on small finite lemmas.

## A concrete conjecture to prove or falsify

For each (n), some optimal height-(S(n)) comparison policy has a **polynomial-size framed strategy DAG**, with nodes representing (n)-element partial orders, outgoing query edges for both outcomes, and explicit *polynomially verifiable* label-permutation frames identifying child states with DAG representatives.

First, specify a syntactically precise certificate format and give a polynomial-time checker: transitive-closure updates; relabelled-poset equality; query validity; decreasing height ranks; total-order sinks; antichain root. This gives **soundness** for YES-instances, not NP until polynomial **completeness** is proved. Explicitly account for the unary input length (N=n+k+1).

Then attack completeness via two *independent* methods:

1. **Constructive:** Find a class of recursively optimal sorters (not merely merge sort) with polynomially many distinct framed states and an all-(n) optimality theorem. Ford–Johnson/Sergeev are only upper bounds; no implication that they attain (S(n)).
2. **Adversarial:** Construct a family showing that a proposed normal form / framing / local minimax rule needs superpolynomially many nodes, **within every optimal sorter** of that family. Counts of all reachable posets (or even information-admissible posets) are **not** sufficient.

## Literature relevance

- Stober–Weiß, *Lower Bounds for Sorting 16, 17, and 18 Elements*, [arXiv:2206.05597](https://arxiv.org/abs/2206.05597): exact root optimality computations, not an all-(n) certificate.
- Sergeev, [ECCC TR20-096](https://eccc.weizmann.ac.il/report/2020/096/): (S(n)le log_2(n!)+o(n)), **not** exact (S(n)).
- Haeupler et al., [SODA 2025](https://doi.org/10.1137/1.9781611978322.134): (O(log e(P))) comparisons, **not** exact (F(P)).
- Rutschmann, [2026 preprint arXiv:2604.12653](https://arxiv.org/abs/2604.12653): (O(m)) preprocessing and (O(log e(P))) sorting time. Inspect the *state decomposition and transition semantics*, not merely complexity in (e(P)).
- Existing 7-element posets (A=(0,0,1,3,5,5,37)), (B=(0,0,2,1,1,9,59)) both have (e=60) but (F(A)=6,F(B)=7), so extension counts alone are insufficient for exactness.

## Output quality gate

Before proposing a PR or a Lean theorem, give (a) a **falsifiable all-(n)** statement, (b) its proof or a fully checked counterfamily, (c) the explicit implication for membership in NP/P, and (d) an adversarial check against shortcuts above. A substantive negative result is acceptable. Repeating finite (S(n)) computations or writing a summary of the same papers is **not** completion.

Cross-reference Antonina issue #301 for existing findings but do not flood it with routine progress notes.

## Comments

### None — ottojung
Comment ID: 6349997120
Upstream: https://github.com/ottojung/soringp1/issues/47#issuecomment-6349997120

### Strong all-n falsifier: same topological order, same extension count, **different exact minimax by Θ(n)**

This is a rigorously checked limit on reusing the 2026 *Unified Bound Heaps* partial-information representation for **exact** optimal sorting. Rutschmann [arXiv:2604.12653](https://arxiv.org/abs/2604.12653), Theorem 4, retains only a topological ordering after preprocessing in an algorithm with **O(log e(P))**-comparison guarantees. The latter is asymptotic, not the exact (F(P)).

Consider these transitive successor-mask posets on labels `0,1,2,3,4`:

| State | Successor masks | Linear extensions | Exact remaining F |
|---|---|---:|---:|
| `A` | `(26,16,24,0,0)` | 8 | 4 |
| `B` | `(16,28,16,16,0)` | 8 | 3 |

**Independent exact minimax check:**
- A has four incomparable queries: `(0,2), (1,2), (1,3), (3,4)`. Every possible first query has total worst-case cost **4**; there is **no** 4/4 split of its 8 linear extensions.
- B has four incomparable queries: `(0,1), (0,2), (0,3), (2,3)`. The unique optimal first query is `(2,3)`, splitting its 8 extensions **4/4**, and yielding a three-comparison decision tree; the other queries cost 4.
- The natural order `0<1<2<3<4` is a valid linear extension of **both** posets.

Thus no *general* exact-minimax value function determined only by **one arbitrary valid topological ordering plus the exact extension count** can be correct for both inputs.

**All-n amplification (n = 5q):** Define ordinal-sum posets `A_q=A⊕...⊕A` and `B_q=B⊕...⊕B` on q consecutive blocks, with all previous-block keys known smaller than later-block keys. By deterministic decision-tree direct sum, `F(A_q)=4q` and `F(B_q)=3q`; both have `e=8^q` and share the natural order `0<1<...<5q−1`. Consequently, for arbitrarily large n, the pair `(arbitrary topological ordering, exact e(P))` fails to determine `F(P)` by an **additive Θ(n)** amount. Padding with a known ordered chain extends this to every n≥5.

**Scope / crucial caveats.** This is a true all-n **generic-poset** obstruction, not a complexity theorem for the initially unordered SoringP1 input. It does **not** rule out a preprocessing algorithm that strategically chooses a different topological ordering for A and B (thus encoding extra state), a compact symbolic strategy for an optimal root sorter, or Rutschmann's claimed asymptotic guarantees. It *does* decisively eliminate the insufficient-state proposal “arbitrary topological order plus linear-extension count computes exact F”.

**Next substantive target for issue #47:** Find a polynomial-time-checkable exact strategy representation that preserves **branch structure** on states of *some globally optimal root sorting strategy*; not just topological ordering, extension count, or first-query balance. Do not Lean-formalize these elementary gadget calculations; they are falsification evidence, not the sought all-n complexity theorem.

### Stronger version: connected incomparability graphs still do not suffice

The ordered-sum amplification above has a trivial series decomposition. We can eliminate that objection while retaining an additive-linear gap.

For (q≥1), add **one new element (v)** incomparable with every existing element of (A_q) or (B_q). Call the resulting posets `A'_q` and `B'_q`. Their **incomparability graphs are connected** (the new vertex is adjacent to every other vertex). The same natural topological order placing (v) last works for both, and each has exactly **`(5q+1)·8^q` linear extensions** (insert (v) into any of the (5q+1) positions of each old linear extension).

Restricting `A'_q` to extensions where (v) is last yields `A_q`; comparisons involving (v) reveal no information about the old block orders in that restricted input family. Therefore
`F(A'_q) ≥ F(A_q)=4q`.
For `B'_q`, optimally sort its q ordered `B` blocks in `3q` comparisons, then binary-insert (v) into the resulting sorted list, using at most `ceil(log2(5q+1))` more:
`F(B'_q) ≤ 3q+ceil(log2(5q+1))`.
Hence
`F(A'_q)-F(B'_q) ≥ q-ceil(log2(5q+1))=Ω(q)`
for sufficiently large q.

This is a **uniform, incomparability-connected family** with the same (n=5q+1), same (e(P)), a common topological order, but linear separation in exact (F). It defeats any exact-cost rule relying only on *those* invariants, even under this connectivity restriction. Nonetheless, deleting (v) exposes an ordinal decomposition, and there is still **no implication for all-n root S(n) complexity**. No Lean work warranted; the target remains complete optimal-root certificates.

---

### None — ottojung
Comment ID: 6350513245
Upstream: https://github.com/ottojung/soringp1/issues/47#issuecomment-6350513245

### New all-(n) proof-carrying strategy design: **forgetful framed DAGs** (soundness proved; polynomial completeness OPEN)

A timely concrete precedent is Jonathan Cremer, *Selecting the 7th Smallest of 16 Elements Takes Exactly 28 Comparisons*, [arXiv:2610.18740](https://arxiv.org/html/2610.18740), published 13 Oct 2026. Section 3 uses an independently implemented **static checker** of small shared decision-graph certificates. In particular, the checker **intersects the relations guaranteed at every caller** rather than requiring identical full histories at each call. Its 16-key selection certificates can use hundreds/thousands of functions, and the author also verifies the fixed results in Lean. Selection is NOT sorting, and none of this shows a polynomial family over all n, but the representation is a useful proof-system precedent. No SoringP1 Lean work is warranted yet.

**A sound all-n generalization for SORT-BOUND-U:** A certificate for (S(n)le k) is a finite acyclic rooted graph, each node (v) carrying a poset (P_v) on (n) variable slots. An internal node names a pair ((a,b)); its two edges name successors (w_+,w_-) and explicit bijections (sigma_pm) of slots. The *local obligations* are:

1. Root's label (P_r) is the n-antichain.
2. Each internal query concerns two **incomparable** elements of (P_v) (for efficiency, not required for logical soundness).
3. For branch (+) ((a<b)) and (-) ((b<a)), the successor annotation obeys
   [
   P_{w_pm} subseteq sigma_pmigl(operatorname{TC}(P_vcup{a<b 	ext{ or } b<a})igr).
   ]
   **Crucially this is inclusion, not equality**: a callee may soundly **forget** known comparisons, allowing distinct histories with different posets to share code.
4. Every leaf's (P_v) is total; the longest root-to-leaf path has length at most (k).

**Soundness proof:** Maintain the invariant that the unknown true linear order, expressed in the current slot naming, extends the stored (P_v). It holds at the antichain root. Following either actual query outcome extends (operatorname{TC}(P_v+ab)); applying (sigma) then retains all the weaker (P_w) relations. At a leaf, a total annotated poset forces exactly one order, so the checker may output it. Acyclicity guarantees termination, and longest-path height bounds the comparisons for *every* input. Thus any accepted graph proves (S(n)le k). The verifier uses (O(|E|n^3)) or other polynomial time in its **explicit certificate length** and n: test poset axioms, permutations, transitive closures, inclusion, leaf totals and DAG longest path. If *every* true unary instance has a graph of size (operatorname{poly}(n+k)), then **SORT-BOUND-U belongs to NP**. *That completeness property is not proved or implied by Cremer's finite certificates.*

**Information-loss budget (new necessary all-n restriction):** Along the adversary path that always chooses an outcome preserving at least half of the currently compatible permutations, let (Q_t) be the actual comparison-history poset after t comparisons and (P_tsubseteq Q_t) the (appropriately unframed) certificate annotation. Then
[
 e(Q_t)ge n!/2^t,qquad e(P_t)le 2^{k-t},
 quad	ext{hence}quad
 log_2 rac{e(P_t)}{e(Q_t)}le k-log_2(n!).
]
The first inequality follows by choosing the majority child; the second follows because the accepted successor sub-DAG must correctly sort *all* (e(P_t)) extensions in at most (k-t) remaining comparisons. Consequently, for a height-(S(n)) certificate, Sergeev's (S(n)=log_2(n!)+o(n)) implies **at most (o(n)) bits of cumulative poset-information loss** (measured as extension-count ratio) at *every node of the majority-extension path*. It does not forbid large combinatorial graph sharing elsewhere or prove polynomial DAG size. The expression is an *instantaneous maximum loss bound*, not a sum over the nodes.

**Two decisive independent tasks:** (A) Implement a **small independent checker**, without Lean, for framed *inclusion*-edges, and experimentally compare exact-equality DAGs with forgetful DAGs for known optimal (S(5..9)) witnesses; measure node counts, not just accepted complexity. (B) Prove a structural *all-n* size bound for some exact optimal root strategy in this stronger class, or construct a family of **optimal-root-relevant** states for which even inclusion-based reuse fails. The latter, not static-checker soundness, is the missing NP theorem. Keep all computations on billy-dev if it returns; while offline, paper/GitHub-only review.

---

### None — ottojung
Comment ID: 6350594338
Upstream: https://github.com/ottojung/soringp1/issues/47#issuecomment-6350594338

### New necessary obstruction to DAG sharing: **common-knowledge incompatibility graph** (paper proof; no Lean)

This directly improves the research objective of #47 and avoids the earlier mistake of counting *all reachable* states rather than states on **one optimal root strategy**.

Fix a height-(k) sound **forgetful framed** comparison DAG as in the preceding comment. Take two comparison histories of equal depth (t) occurring in its unfolding, with actual transitive posets (Q_1,Q_2). Suppose their executions share the *same annotated DAG node* (v) after relabellings (sigma_1,sigma_2). The common node's annotation (P_v) must satisfy
[
P_vsubseteq sigma_1(Q_1)capsigma_2(Q_2).
]
Since a subtree rooted at (v) has at most (k-t) comparisons remaining and sorts *every* extension of (P_v),
[
oxed{eigl(sigma_1(Q_1)capsigma_2(Q_2)igr)
  le e(P_v)le 2^{k-t}.}
]
This is an **all-n necessary condition for two histories to merge**, *even if the shared subroutine deliberately forgets previously known comparisons*. Note that the intersection of strict partial orders is a strict partial order, so (e(cdot)) is well-defined.

**Conflict graph:** For a set (X) of *depth-(t) histories lying in one given correct height-(k) decision tree*, put an edge between (Q_i,Q_j) whenever
[
orallsigmain S_n,quad e(Q_icapsigma(Q_j))>2^{k-t}.
]
Any certificate from this form of the tree, even allowing arbitrary relabelling, information forgetting and DAG sharing, requires distinct depth-(t) DAG nodes for adjacent histories. Thus the number of distinct nodes at depth (t) is at least the chromatic number (chi(X)) of this graph (in particular, its clique number). This is a finite combinatorial **certificate-size lower bound for this proof-system grammar**, not a lower bound on computing (S(n)) by all possible algorithms.

**Research payoff / nontrivial quantifier:** To disprove polynomial-complete certificates for the *root sorting problem*, it is not enough to construct huge sets of budget-reachable (or even winning) posets. You would need to prove that **EVERY height-(S(n)) root sorting strategy**, or every equivalent strategy in the certificate grammar, generates a superpolynomial chromatic incompatibility graph at some depth. That is the missing (orall)-over-optimal-strategies step. Conversely, finding a polynomial coloring/cover by common-knowledge-compatible states may suggest a compression algorithm, but pairwise compatibility alone does **not** imply globally composable successor policies or a polynomial verifier.

The counting test (e(Q_icapsigma Q_j)) can be #P-hard for arbitrary posets, so this theorem is an *obstruction language*, not itself a polynomial-time test or NP-membership proof. Restrict to families with explicitly countable intersections, and seek a robust *optimal-root* structural theorem. No routine Lean formalization warranted.

---

### None — ottojung
Comment ID: 6350681492
Upstream: https://github.com/ottojung/soringp1/issues/47#issuecomment-6350681492

Further all-n certificate-design simplification (following the static-checker approach in Jonathan Cremer, arXiv:2610.18740, Section 3.2): **a framed sorting DAG does not need to carry guessed poset annotations**.

For each node v, compute the guaranteed partial order R(v) in DAG topological order. Set R(root) to the empty order. For an outgoing comparison outcome, extend R(v) with the observed inequality, close transitively, and rename slots by that edge's explicit permutation. Ignore an outcome inconsistent with R(v), since it is unreachable. At a child w, set R(w) to the INTERSECTION of all feasible incoming partial orders. Reject unless every reachable terminal has a total R(w) and every reachable root-to-terminal path uses at most k comparisons.

**Soundness (all n):** Induct over the reached comparison path. Any actual total ordering extending R(v) also extends the selected comparison outcome; transitive closure and renaming preserve it. Intersection retains only relations guaranteed across all callers. A terminal with total R therefore identifies the input ordering, and DAG longest-path bounds worst-case comparison count. This checker takes polynomial time in explicit DAG size and n (e.g., cubic time per edge for closure).

**Relative completeness:** If the same fixed DAG, queries and renaming edges admit ANY locally sound poset labels P(v), with P(root) empty, P(child) contained in the closure of each feasible parent's comparison outcome, and total labels at leaves, then P(v) is contained in computed R(v) everywhere reachable. This follows by DAG induction and monotonicity of closure; impossible branches need no obligations. The canonical meet-propagation consequently accepts any graph accepted by the older annotation-guessing checker. It eliminates the need to guess or search for label assignments but DOES NOT establish that every optimal sorter has a polynomial-size graph.

Next decisive task: test whether this strictly more permissive shared-subroutine grammar compresses an optimal root sorting witness beyond exact labelled/isomorphic state DAGs. Only a verified all-n polynomial-size completeness proof would imply SORT-BOUND-U in NP. This is a paper/algorithm direction, NOT a justification for new Lean formalization.

---

### None — ottojung
Comment ID: 6352265146
Upstream: https://github.com/ottojung/soringp1/issues/47#issuecomment-6352265146

### All-n constructive sanity test for the *forgetful framed-DAG* checker: triangular bubble sort

**Theorem (sound, constructive; not NP completeness).** For every (n\ge 1), the canonical meet/intersection checker described above accepts a framed sorting DAG with exactly (inom n2) comparison nodes, O(n²) edges, and worst-case comparison budget (k=inom n2). Consequently the grammar can compress an exponentially large sorting tree into a polynomial certificate even when histories are merged at **every** step. This does **not** prove optimal sorting certificates are polynomial; generally (S(n)<inom n2).

**Construction:** The DAG is a chain of conditional compare–exchange gates. For pass (p=0,…,n-2), compare adjacent *current slots* ((i,i+1)), with (i=0,…,n-p-2). Both outcome arcs lead to the same next node. The ((i<i+1)) outcome has identity slot frame; the reverse outcome has the transposition ((i\ i+1)) (swap the array slots). Invalid outcomes known to be impossible may be ignored by the checker. The final node is terminal. Total gates = (sum_{p=0}^{n-2}(n-p-1)=n(n-1)/2).

**Proof that meet propagation, not merely an ordinary sorting-network simulation, accepts:**
- Fix a pass ending at position (m-1). By induction on the preceding passes, the common relation (R) guarantees that all slots in ([0,m-1]) are below the already sorted suffix ([m,n-1]), and that suffix is increasing. Initially the suffix is empty.
- During the forward adjacent pass, after comparing slot (i-1) with (i), the canonical meet (R) guarantees (h<i) (value in slot (h) smaller than that in slot (i)) for **every** (h<i). Base (i=1): compare–exchange guarantees slot 0 < slot 1 on *both* frames. Induction: before comparing ((i,i+1)), every (h<i) is known below slot (i); in the no-swap branch transitivity yields (h<i+1), whereas in the swap branch the old slot (i) becomes the new slot (i+1) and those comparisons remain known. Both branches separately guarantee old/new (i<i+1), so their intersection does too.
- Relations that every remaining prefix slot is below the sorted suffix survive either swapping of two prefix slots. At pass end, new slot (m-1) exceeds the whole remaining prefix, and is below the previous suffix. Induct down to (m=1). The terminal canonical (R) is a total order. Hence the checker accepts.

Here `R` is the checker-computed meet of post-outcome/transposition closures. **Do not infer acceptance of an arbitrary sorting network** from semantic sorting correctness alone: meet abstraction discards disjunctive state information, so ordinary network correctness need not imply completeness of this abstract checker. This proof is specific to the triangular adjacent-pass network.

**Independent executable sanity check (not proof):** implemented the canonical transitive-closure / intersect-both-outcomes transformer and checked each pass invariant and total terminal relation for (2\le n\le12).

**Research consequence:** This is a controlled positive construction showing extreme sharing *is possible*, so a generic factorial-tree-size objection to this grammar is invalid. The remaining, sharp question is **near-information-bound exactness**: can a height-(S(n)=\log_2(n!)+o(n)) sorter for every n be expressed with polynomially many framed, forgetful nodes? A successful all-n answer would imply NP for unary SORT-BOUND-U. The bubble witness is not progress toward such completeness by itself. No Lean work recommended.

---

### None — ottojung
Comment ID: 6352430976
Upstream: https://github.com/ottojung/soringp1/issues/47#issuecomment-6352430976

### Decisive falsification: even an exact optimal 4-key network fails immediate-join meet checking

**Claim falsified:** "Every correct oblivious compare–exchange sorting network with m gates is accepted by the canonical forgetful/intersection framed-DAG checker as an m-node chain (both outcomes of each gate merge immediately)." The triangular-bubble construction above works, but the claim fails already for **n=4** (and also for standard 8-key bitonic sorting).

**Sharper and optimal-depth counterexample (n=4):** The five-comparator network `(0,1),(2,3),(0,2),(1,3),(1,2)`, with every gate sorting its two slots increasingly, is a correct comparison sorter for all 24 permutations and uses **S(4)=5** comparisons. But representing it as a five-node chain with immediate outcome merges, swapping the two slot names on the reverse outcome, causes the canonical meet checker to know only five of the six final pairs: it does **not** establish `2<3`. This was independently checked by enumerating all 24 inputs and propagating the strict-poset closures and intersections. Thus incompleteness is already visible in an **exactly optimal** small sorter. It does *not* rule out a different small DAG for that same sorting problem.

For a second, larger example, use the standard Batcher bitonic sorter, sequentializing its comparators as follows (0-based slots): for `k=2,4,8`, for `j=k/2,k/4,...,1`, visit every `i` with `i < (i XOR j)` and compare slots `i` and `i XOR j`; put the smaller element in the first slot when `(i & k)==0`, and the larger there otherwise. For each gate, merge both comparison-outcome arcs into the next node, framing the swap outcome with the corresponding slot transposition. This is a **24-comparison DAG chain** on 8 keys.

1. **Actual semantics:** independently simulated all **8!=40,320** labelled input permutations; all reach the output in increasing order. This is the standard correct bitonic network (Batcher, 1968: https://doi.org/10.1145/1468075.1468121).
2. **Canonical meet checker:** propagated exactly `TC(R ∪ {a<b})` along the non-swap branch, the appropriately permuted `TC(R ∪ {b<a})` along the swap branch, and INTERSECTED both successor relations after every gate. After the 24th gate, the computed terminal `R` knows only **24 of 28** pairwise comparisons. Specifically it fails to know `1<2`, `1<3`, `5<6`, and `5<7`. Thus the checker **correctly rejects this representation**, even though the actual network sorts every input.
3. Additional explorations using the same canonical transformer: n=4 bitonic network is accepted; n=16,32,64 versions retain incomplete terminal relations. Only the n=8 counterexample and the exact 40,320-input check are needed for the falsification.

**Reason:** taking the meet after each gate enlarges the represented set from the *union of feasible history-specific orders* to the linear extensions of one common partial order; it discards correlations ("this order OR that order"). Later gates can exploit such correlations in the real program, but the abstract checker has already forgotten them.

**Precise scope:** This refutes the one-node-per-gate **immediate join** encoding, NOT every framed DAG for the bitonic algorithm and NOT the conjecture that some optimal root sorter has polynomial-size proof-carrying framed DAGs. The latter remains open. Indeed the checker is still sound; an over-approximation can only introduce false negatives, not false positives. It shows that the proof-system design has a serious expressiveness/succinctness tradeoff even *before* exact optimality.

**Recommended next research:** compare (A) bounded-width disjunctive poset annotations with explicit polynomial entailment checker; (B) joins delayed until key input correlations become irrelevant; (C) additional locally proved structural summary rules. Identify an all-n bounded-width theorem (or counterfamily) rather than Lean-formalizing this n=8 example.

---

### None — ottojung
Comment ID: 6352570584
Upstream: https://github.com/ottojung/soringp1/issues/47#issuecomment-6352570584

### Research triage: a complexity barrier to *universally complete* proof-carrying comparator-network checkers (no Lean)

**Primary source:** Ian Parberry, *On the Computational Complexity of Optimal Sorting Network Verification* (PARLE 1991), https://ianparberry.com/research/sortingnetworks/ (author's bibliography and abstract; see also https://ianparberry.com/pubs/snverify.pdf). Correctness checking of an arbitrary explicitly given comparator network is **coNP-complete**, including restricted networks with depth only `4 log n + O(1)` greater than the optimal sorting-network depth. The source is about **oblivious sorting networks**, not our adaptive comparison-optimum `S(n)`; the near-optimal restriction concerns **parallel depth**, not comparison count.

**Conditional no-go theorem (immediate rigorous reduction):** Let `V(C,w)` be a polynomial-time predicate on a candidate comparator network `C` and a certificate `w`. Suppose (i) soundness: acceptance implies `C` sorts all inputs, and (ii) **universal polynomial completeness**: every correct comparator network `C` has a witness of size `poly(|C|)`. Then network correctness is in NP. By Parberry's coNP-completeness, **NP = coNP**. Therefore, unless NP=coNP, NO sound polynomial-time checker can accept *every correct comparator network* using polynomially sized auxiliary proofs. This is stronger than the observed finite failure of immediate-join meet propagation: a universally complete polynomial proof system is complexity-theoretically implausible irrespective of which abstract domain or local annotation grammar we choose.

**Scope matters enormously:** This does NOT rule out our main conjecture: for each `n` there might exist *some* optimal adaptive sorter of height `S(n)` with a polynomial-size, efficiently checkable framed-DAG certificate. Its completeness is existential over *one root-optimal strategy*, not universal over every network/program, and network depth != adaptive comparison budget. No P/NP classification of unary `SORT-BOUND-U` follows from Parberry alone.

**Immediate efficiency directive for researchers:** Stop targeting a polynomially complete generic analyzer/verifier of *arbitrary* sorting networks or all adaptive sorter programs. Favor a special **sound, structurally restricted certificate language with existential optimal-root completeness**. For bounded disjunctive poset annotations, explicitly (a) distinguish validity from polynomial **certificate size**, (b) test whether the special grammar contains a height-`S(n)` strategy for every n, and (c) keep Parberry's universal-program barrier in view. A short all-n impossibility conditional like the above is better than a new Lean treatment of n=4/n=8 network counterexamples.

---

### None — ottojung
Comment ID: 6352979483
Upstream: https://github.com/ottojung/soringp1/issues/47#issuecomment-6352979483

### All-n constructive result: **merge sort admits a canonical-meet framed DAG with quadratic nodes and O(n log n) depth** (paper proof; no Lean)

This strengthens the earlier triangular-bubble witness, which used n(n−1)/2 comparisons in the *execution*. Here the **certificate graph has n(n−1)/2 comparison nodes but each execution traverses only O(n log n) of them**. The distinction between graph size and root-to-leaf height is crucial.

**Theorem.** Fix any full binary *merge schedule* on n singleton keys, with a sequential fixed order of its internal merges. There is a permutation-framed, acyclic sorting DAG whose canonical intersection/closure checker accepts, with exactly
`sum_{internal merge nodes (p,q)} p*q = n(n−1)/2`
internal comparison nodes, plus one final leaf. Each execution uses at most
`sum_{internal merge nodes (p,q)}(p+q−1)`
comparisons. For balanced merges this is O(n log n); for n=2^r, it is at most `nr−n+1`. Explicit edge frames are permutations of n slots, so a literal certificate has polynomial encoding size (e.g. O(n³ log n) bits).

**Construct one merge of two known increasing contiguous blocks of initial lengths p and q.** Its control states are pairs `(a,b)`, where 1≤a≤p, 1≤b≤q count unconsumed elements in the left and right queues. At a state, the canonical slot layout is
`[already-output prefix] [left queue of a] [right queue of b]`,
all inside that merge's fixed contiguous segment. The *invariant guaranteed by the poset meet* is: the output prefix is increasing and less than **every** remaining element; each remaining queue is internally increasing. Compare the two queue heads. If the left head is smaller, make it the new end of the prefix (identity frame). If the right head is smaller, move that head left over the left queue to the next prefix position (explicit cyclic insertion frame). Each outcome decreases `a+b`; its respective successor is `(a−1,b)` or `(a,b−1)`. If either reaches zero, the entire block is now sorted, so connect **directly to the following merge module**, with no additional comparison node. All outside-segment slot names are untouched.

**Why canonical meet/intersection accepts:** For either outcome the chosen head is below (i) all other elements of its own sorted queue and (ii) the other queue head and therefore all members of that other queue. Thus the new prefix remains ordered and below all remaining keys. Both remaining queues preserve their internal order after the frame. These are the SAME structural guarantees for all arrivals to a given `(a,b)` state, regardless of earlier interleaving choices. Since transitive closure and intersection preserve every relation guaranteed by every arrival, the computed canonical poset entails this invariant at every graph node. At a zero-queue exit, prefix plus the one remaining chain is totally ordered, so the completed merged segment is guaranteed sorted. Joining all exits and beginning the following scheduled merge also preserves all previously completed sorted-block invariants. After the last merge, the canonical root-to-leaf meet is a total order; the checker accepts.

**Graph size.** A merge of p and q keys has precisely `pq` query states, not `2^{p+q}` histories. Over a binary merge tree on singleton leaves, every unordered pair of keys belongs to opposing child subtrees at exactly one merge, hence `Σpq=binom(n,2)`. This count holds for *every* merge-tree shape. Its branch permutations, initial/final-node connections and DAG topological order are explicit. Total query budget is the ordinary sum of `p+q−1` across calls. In particular n=4 yields **6 graph query nodes but at most 5 comparisons on a path**, which achieves S(4)=5: the n=4 immediate-join oblivious network counterexample does not prevent a *different* compact optimal DAG.

**Exact relevance and limitation:** This proves the grammar can encode a standard asymptotically efficient *adaptive* sorter with quadratic graph size, beyond the prior O(n²)-comparison bubble construction. It strengthens the plausibility of existentially compressed sorters, but it does **not** show polynomial-size **height-S(n)** certificates for every n, so does not establish unary `SORT-BOUND-U∈NP`. Balanced merge sort has a linear additive deficit above log2(n!), whereas Sergeev's upper bound permits o(n). The decisive next target is an all-n polynomial-size grammar realizing **exact optimal** budgets; an intermediate falsifiable target is whether the same canonical meet grammar can realize `log2(n!)+o(n)` comparisons with polynomial size, or whether some necessary state-disjunction width becomes superpolynomial.

**No Lean or finite census is warranted now.** Seek an independent proof audit of invariants/frames (especially joining different completed merge calls), then investigate near-information-bound constructions or a root-specific impossibility.

---

### None — ottojung
Comment ID: 6353079027
Upstream: https://github.com/ottojung/soringp1/issues/47#issuecomment-6353079027

Further research direction from Sergeev ECCC TR20-096, §§6–7 (https://eccc.weizmann.ac.il/report/2020/096/download): the universal pair-insertion comparison strategy has depth h=2s+3 and width at most s+4. Theorem 2 selects s=ceil(2 gamma log_2 a), gamma<=1/5, with a about log_2 n in the sorting application. Therefore its LOCAL branching has only 2^h=(log n)^O(1) leaves. This removes local strategy-tree size as the obvious obstacle to a polynomial-size framed-DAG witness realizing the known log_2(n!)+o(n) bound. The unresolved issue is GLOBAL sharing: a sequence of insertions leaves pending elements in different interval containers, and future comparisons may need to distinguish occupancy positions and pairing relationships. Do not conclude exponential complexity by merely counting potential occupancy vectors: only reachable histories and compatibility of their framed states matter. High-priority falsifiable test: specify a concrete signature of ordered-chain intervals, pairing links and pending-container state; prove polynomially many compatible reachable states with meet-preserving transitions, or exhibit an explicit growing family of incompatible executions of THIS algorithm. This is intermediate progress toward an exact-S(n) certificate, not NP membership. No Lean and no finite-only census.

---

### None — ottojung
Comment ID: 6353288888
Upstream: https://github.com/ottojung/soringp1/issues/47#issuecomment-6353288888

### New all-n NP sufficient condition: logarithmic **knowledge-reset checkpoints** (paper lemma, no Lean)

This is an *existential optimal-root* criterion, not the coNP-hard universal network verifier forbidden by Parberry.

**Checkpoint lemma.** Suppose that for every n there exist r(n) <= poly(n) fixed stage-boundary posets P_0,...,P_r on n slots, with P_0 the antichain and P_r total, and framed comparison *trees* T_i (one per stage) such that:
1. Each stage begins with every total order extending P_i as admissible input (no hidden history-dependent constraints).
2. All internal comparisons of T_i respect this model. Every leaf has an explicit permutation frame under which its comparison-closure entails P_{i+1}. Therefore all leaves may soundly merge at the same next-stage root, forgetting extra relations.
3. Stage i has worst-case height b_i <= c log_2(n+2) for one fixed constant c, and the sum of stage worst-case bounds is <= S(n). The number of stages is polynomial in n.

Then there exists an accepted canonical-meet framed DAG of size at most O(sum_i 2^{b_i}) <= poly(n), and height at most sum_i b_i <= S(n). The proof simply **expands each stage into its raw depth-b_i decision tree**, uses explicit frames to identify its leaves with a single next-stage entry, and inducts on the canonical guaranteed-poset R at each boundary. The actual root sorter is correct and uses at most S(n); by definition its height must therefore be exactly S(n). Hence unary SORT-BOUND-U is in NP IF such optimal checkpoints exist uniformly as a polynomial-size witness family. (No efficient *construction* of the witnesses is needed for NP; their explicit stage/tree/frames are guessed and checked.)

**Why this is nontrivial:** The assumption that a stage works for *every* extension of the common invariant is essential. A mere polynomial-time sorting program, or knowledge that all histories share a few comparisons, is insufficient: the next routine may rely on disjunctive correlations lost by the meet. The old optimal 4-key sorting-network immediate-join counterexample demonstrates this failure. The hypothesis also says exactly what an agent must prove before claiming completeness: at every checkpoint, the canonical common poset is a sufficient state for the remaining optimal budget. One must account for the sum of *independently maximized* stage costs, not merely the global optimum of the concatenated program.

**Examples and boundary:** Ordinary single-key balanced binary insertion satisfies this checkpoint property with n stages and b_i=ceil(log_2(i+1)); hence another polynomial certificate at a nonoptimal O(n log n) budget. Merge-sort has efficient polynomial DAGs by a DIFFERENT structural compression (queue-length states), because its largest merge can use Theta(n) comparisons and cannot be expanded into a polynomial-size raw stage tree. Sergeev's group-insertion algorithm has short LOCAL strategy subtrees, but the occupancy/pairing state of containers between pair insertions may prevent a common poset reset, despite the short per-pair comparison budget.

**Two independent falsifiable tasks:** (A) Find an optimal-root algorithm with a polynomial number of O(log n)-cost history-independent common-poset checkpoints; prove the exact cumulative worst-case cost, not an asymptotic surrogate. (B) Prove an explicit family of partial sorting histories in a named candidate near-optimal algorithm whose interval-container state is indispensable at checkpoints, so any proposed single-poset reset loses more than the remaining comparison slack. The first is a route to NP, the second a precise way to reject this sufficient-condition approach. Avoid routine Lean and finite-only census.

---

### None — ottojung
Comment ID: 6353303109
Upstream: https://github.com/ottojung/soringp1/issues/47#issuecomment-6353303109

### Primary-source correction for the checkpoint agenda: Sergeev's theorem needs **macroscopic groups**, not O(log n)-sized independent resets

I inspected the original Sergeev ECCC TR20-096 PDF, https://eccc.weizmann.ac.il/report/2020/096/download, especially Lemma 2 (PDF pp. 10–12), Theorem 2 (p. 28), Theorem 3 (pp. 29–30). This matters for issue #47's logarithmic checkpoint sufficiency lemma (comment 6353288888).

**Precise source fact:** Theorem 2's near-information-bound group-insertion guarantee assumes its number of pairs m satisfies `2^(a/4) <= m <= 2^(a/2)` for the parameter `a` governing interval-insertion cost. In Theorem 3, a is roughly `log_2 n`; groups contain `m ≈ sqrt(n)/log n` elements. In particular, **m must be at least n^(1/4-o(1)) for the proven Theorem-2 bound**, enormously larger than an O(log n)-comparison raw-tree microstage.

**Therefore:** It is WRONG to infer that Sergeev's local depth `h=O(log log n)` yields a global sorting algorithm consisting of O(log n)-comparison stages that can all be independently expanded into polynomial-size trees and merged at invariant checkpoints. Each local short comparison strategy recurses through the stateful collection of containers, and the near-optimal bound is amortized over large groups. The required locally stage-invariant, history-independent state has NOT been supplied by the paper.

**Second source fact:** §4 bounds total comparisons for m pair insertions by `rho*m + C*log_2(n+2m)`, where C is the number of leftover-element containers. Lemma 2 derives an *upper* bound on C using a recursive inequality (equations (19)–(20), p.12). Repeatedly flushing containers to force O(log n)-comparison checkpoints can therefore ruin the near-optimal estimate; but the paper's upper bound on C is NOT a lower bound, so this is a caution, not a no-go theorem.

**Next falsifiable task:** At a group boundary, a clean sorted-chain invariant exists. Inside a group of size m=Omega(n^(1/4-o(1))), find a polynomially sized *nested* proof-carrying DAG implementing its stateful interval-container processing, with a sound local join rule tracking the occupancy/pairing relations. Alternatively prove for a specified candidate quotient that histories differing only in container occupancy cannot always be merged within the exact remaining comparison budget. A purely O(log n)-stage expansion is not justified by Sergeev's established result. No Lean, no finite census.

---

### None — ottojung
Comment ID: 6353322141
Upstream: https://github.com/ottojung/soringp1/issues/47#issuecomment-6353322141

### All-n negative result eliminating a tempting certificate-completeness route: even **locally optimal balanced merging** loses Theta(n) globally

Source: Igor Sergeev, *Complexity of sorting and selection*, lecture notes dated 2025-03-05, §1.3, Lemma 1.3 and eqs. (1.1)–(1.2), https://igorssergeev.github.io/papers/S-lectures_eng_050325.pdf. The lemma establishes the **exact** worst-case cost to merge two independently sorted chains of equal length m: M(m,m)=2m−1. Its lower-bound witness is the alternating order b1<a1<b2<a2<...<bm<am: every adjacent cross-chain pair must be compared.

**Theorem (powers of two).** Consider the algorithm *architecture* that splits n=2^r labels into two predetermined equal halves, COMPLETELY sorts each half independently, then merges their two already sorted chains optimally; repeat recursively. Any algorithm restricted to this architecture has worst-case comparison cost at least
  C(n) = n log_2(n) − n + 1.
The usual balanced merge sort achieves equality.

**Proof of the lower bound:** Each half must be sorted on every input, and for any fixed pair of internal input orders an adversary may choose the relative interleaving of its independently sorted halves. There is an interleaving which requires 2m−1 additional cross-half comparisons; independent arbitrary within-half orders allow simultaneous hard cases for the recursive subproblems. Thus C(2m) >= 2 C(m) + (2m−1), with C(1)=0. The upper bound matches. (This is a restriction to an architecture *with independently completed halves*, not all comparison sorters.)

Stirling gives log_2(n!) = n log_2 n − (log_2 e)n + O(log n), so
  C(n) − log_2(n!) = (log_2 e − 1)n + O(log n) ≈ 0.442695n + O(log n).
Sergeev's 2020 algorithm gives S(n)−log_2(n!)=o(n), so this balanced-merge architecture is **provably nonoptimal for all sufficiently large powers of two**, despite every individual equal-size merge using the *optimal* number of comparisons.

**Research triage:** Our new compact framed-DAG merge-sort proof (comment 6352979483) is a valuable verification-grammar sanity witness, but improving only its DAG sharing without changing its decision-tree architecture cannot lead to all-n exact S(n) certificates. Any attempt to get exact optimality must BREAK independent sorted-halves boundaries (e.g. via correlated pair/group insertion) or use a genuinely different merge scheduling/algorithm architecture. Do not Lean-formalize this standard all-n fact: it serves as a rigorous stopping rule for an entire dead-end research direction.

---

