# antonina-ENPQOieRIqKXSqv1VF7Wtg-timely

Session: ses_e49f8b1b6ffelIOJOWz5Ef97wF
Workspace: /home/lubko/soring-fronts/exec-fotc-encoding-spec-20261107
Created: 1794055294615; updated: 1794055328302

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 27 (msg_1b6076a530011wqOMeOmjMnpJf)

## Result: the encoding gap is constructively dischargeable

**[paper proof]** A supplied framed DAG of \(M\) nodes, on \(n\) labels, with budget \(k\), can be compiled into a certificate-augmented explicit relational structure and one fixed-variable FO(TC) strategy. The construction is uniform in the supplied certificate; it does **not** show that polynomial-size DAGs of height \(S(n)\) exist for all \(n\).

Let \(C\) be the explicit certificate length. Use a domain of size
\[
D=\max\{2,n,M,k+1\},
\]
with unary predicates for the disjoint indexed ranges `Label`, `Node`, `Slot`, `Outcome`, and `Position`; their elements encode \(0,\ldots,n-1\), \(0,\ldots,M-1\), and so on. Padding elements belong to none of these ranges. The domain and all relations are explicitly tabulated. Use the fixed vocabulary below, with maximum arity 4:

- `Query(u,a,b)`, `Leaf(u)`, `Child(u,o,w)`, `Perm(u,o,i,j)`;
- `H(i,j)`, the current query-history relation (“\(i\) was returned smaller than \(j\)”);
- `Ann(u,i,j)`, the compiler-validated guaranteed strict order at node \(u\);
- `Rank(i,r)`, `Out(r,i)`, the precomputed output relation described below.

The compiler first validates the supplied certificate using the framing checker’s intended semantics: root 0 starts with the empty guaranteed order; both branch outcomes and all forward child edges and permutations are present; permutations are bijections; impossible branches are identified; reachable guaranteed orders are closed transitively and intersected at joins; every reachable leaf’s guaranteed order is total; and the maximum reachable query-path depth is at most \(k\). It computes and tabulates `Ann` at every reachable node. This is polynomial in \(n+M+C\): the checker’s closure, renaming, intersection, and depth operations are polynomial in the explicit graph and \(n\). Malformed certificates are rejected. Unreachable nodes need no annotations and are never entered.

`Rank(i,r)` and `Out(r,i)` are computed once from the root-coordinate labels: `Rank(i,r)` means label \(i\) has rank \(r\), and `Out(r,i)` is its inverse. They are explicit tables, not an order oracle. For the strategy to emit correctly, output is in the current frame, so at a leaf the path-specific slot map is used to convert each root label to its current slot.

The program store contains a current node \(u\), a slot map \(f\) from root labels to current slots, and \(H\). Initially \(u=0\) and \(f\) is identity. The state for transitive closure is \((u,s)\), with \(s\) a slot. A fixed-variable transition formula can be written schematically as:
\[
\begin{aligned}
\mathrm{Step}((u,s),(w,t)) \equiv {}&
\exists a\,b\,o\,j\;[
 \mathrm{Query}(u,a,b)\land \mathrm{Slot}(s)\land\mathrm{Slot}(t)\\
&\land ((H(a,b)\land o=\mathrm{lt})\lor(H(b,a)\land o=\mathrm{gt}))\\
&\land \mathrm{Child}(u,o,w)\land\mathrm{Perm}(u,o,s,t)].
\end{aligned}
\]
Here the transition’s slot component obeys exactly
\[
f_{\mathrm{new}}(i)=\mathrm{Perm}(u,o,f_{\mathrm{old}}(i)).
\]
Thus `Perm` is old-slot-to-new-slot, matching the checker’s `_rename` convention; it is not applied in the inverse direction. The state transition retains the node and maps each tracked old slot to its new slot. A query action is issued on the current slots corresponding to the certificate’s query pair; its branch is selected from `H` by the returned smaller label, as above. On a leaf, the TC-reached slot map supplies the current slots of the labels, and `Rank`/`Out` specify the emitted sequence in increasing rank. No counting, numeric rank computation, or hidden-order access occurs during execution. (Equivalently, the compiler can tabulate the leaf output for each reached leaf/path-map pair; the explicit `Rank`/`Out` form makes the required output relation visible.)

This description needs a **repair to the draft definition**: it must specify the certificate-augmented input relations and current frame store, and make the node’s query pair and edge permutation refer to the current slots. A query result is a label, not an implicit slot; the state must retain the label-to-slot map (or its equivalent) so the outcome is tested against `H` and the edge permutation is applied in the stated direction. It must also define leaf output via an explicit relation and the path map, rather than assuming an order is available at a leaf.

For fixed variable bound, the schema and transition formula have constant length independent of \(n,k,C\). The compiler’s relation tables have polynomial size: in particular, `Ann` and `Perm` use at most \(O(Mn^2)\) and \(O(Mn^2)\) tuples, while `Rank` and `Out` use \(O(n)\); the total explicit structure is polynomial in \(n+M+C\). With \(M\le C\), its domain size is polynomial in \(n+k+C\). Formula evaluation and each action are polynomial in that domain size by the fixed-variable FO(TC) bound in the draft. There are at most \(k\) charged comparisons on any path; the DAG is forward, so a run visits at most \(M\) query nodes and performs at most \(O(Mn)\) slot-map/output actions (or polynomially many if map maintenance is implemented by explicit table updates). Parsing, compiler validation, table construction, formula evaluations, history/store updates, and output checks therefore fit one fixed polynomial clock in \(n+k+C\). If \(C\le (n+k)^e\) for a fixed \(e\), the clock is a fixed polynomial in \(n+k\); its exponent depends on \(e\) and the fixed interpreter, not on the instance or certificate.

**Qualification:** This establishes a uniform encoding/compiler lemma for any supplied accepted framed DAG. It does not establish unrestricted `NP` or \(\Sigma_2^P\) membership, nor polynomial-certificate completeness at height \(S(n)\).
