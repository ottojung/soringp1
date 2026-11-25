# antonina-zoZdS5Z4Ba46ZZpyAG0qjT-throats

Session: ses_e4a0a4e82ffe3kzsY4hTlU1MQ2
Workspace: /home/lubko/soring-fronts/exec-fotc-framed-dag-compiler-20261107
Created: 1794054140355; updated: 1794054192101

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 43 (msg_1b5f5d0d30015E7Aco2jIM60b7)

The two representations are not identical at their operational boundary: framed-DAG edges apply arbitrary slot renamings after an outcome, whereas the FO(TC) model maintains a history of comparisons among fixed labels. I’m checking whether that gap is only a polynomial bookkeeping translation or whether it requires a relation the fixed-variable program cannot maintain.

## Output 115 (msg_1b5f63ce1001ikFgwzbN1rTBQz)

**Result: the bridge works, under the stated FO(TC)\(_v\) model.** A polynomial-size framed DAG can be compiled uniformly into a polynomial-size program in that model, with polynomial combined runtime, preserving its charged comparisons and correctness on every input permutation. This is a representation bridge, not an all-\(n\) completeness result.

Given the explicit certificate table, compile one FO(TC)\(_v\) control rule for each DAG node. At node \(v\), the rule reads its listed pair \((a,b)\) and issues `Ask(a,b)`. On the returned outcome, it follows the corresponding listed edge to node \(w\). The edge’s permutation \(\pi\) changes the *meaning of slot indices* at \(w\): interpret each index \(i\) there as the prior index \(\pi^{-1}(i)\). Thus the compiler stores a static node-indexed map from slots to original labels, composed along the traversed path. It does **not** apply a frame by learning or computing an order relation. At a leaf, it emits the labels in the order specified by that leaf’s current slot map.

This addresses the main apparent mismatch: framed DAGs relabel slots, while the FO(TC) program’s query history is over fixed labels. A current slot-to-label map bridges those conventions. For \(M\) DAG nodes, storing one \(n\)-entry map per node takes \(O(Mn\log n)\) bits; node and label indices need \(O(\log M+\log n)\) bits. The static certificate tables—node instructions, edge destinations, permutations, and leaf data—have polynomial size in \(n+k+C\), where \(C\) is the encoded certificate size. They may be represented as explicit relations of fixed arity (tuples can index a table and its fields), rather than as a dynamically generated, arbitrarily high-arity relation. Each rule can use constant-size formula text plus node-specific constants, or read these tables from the explicit input/store. Either way, total program size is polynomial in \(n+k+C\); the number of control labels and rule applications is \(O(M)\) on an execution, with only polynomial overhead for table lookup and output.

Every comparison is a charged `Ask`. The program branches only on its returned answer; it neither consults the hidden permutation nor treats the DAG checker’s propagated partial-order annotations as runtime information. An impossible edge may be present in the certificate, but no real input permutation can traverse it. For each actual input, the compiled execution follows exactly its DAG path, so it makes the same comparisons, has the same path-height bound, and reaches a leaf whose output is correct if the framed certificate is sound. The leaf output must be available from the certificate or derivable from the leaf slot map; soundness of the checker guarantees it is a total order on every feasible execution.

If \(C\) and the encoded DAG are polynomially bounded, the explicit tables, fixed-arity vocabulary, and polynomially many rule evaluations fit the preserved draft’s polynomial combined-complexity result. Its fixed-variable/explicit-table assumptions matter: adding an oracle relation or a succinct encoding that hides arbitrary table computation would not be covered. The current model allows an output check against the full permutation only in the *outer verifier*; the compiled program itself uses query outcomes only, as required.

**Limitation:** the compiler is uniform as a transformation of a supplied certificate, not a polynomial-time method for finding an optimal certificate. The framed-certificate frontier does not establish polynomial-size framed DAGs at height \(S(n)\) for every \(n\). Therefore this bridge does not establish NP or \(\Sigma_2^P\) membership for unrestricted `SORT-BOUND-U`, nor all-\(n\) optimal completeness. The result is a direct encoding lemma, not a resolution of the broader FO(TC) completeness conjecture. No files, commits, or posts were changed.
