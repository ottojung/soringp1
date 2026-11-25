# antonina-JMtjHmtnKqm8F47D3pGeAp-grimesby

Session: ses_e49f14bcbffeP317n2Db0HAEYm
Workspace: /home/lubko/soring-fronts/exec-fotc-frame-store-review-20261107
Created: 1794055779451; updated: 1794055828671

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 62 (msg_1b60f0494001K3t4IP92Eltchy)

**Verdict:** The proposed frame-store extension is internally coherent and supports the stated path invariant, provided the extension makes frame updates atomic and requires the leaf annotation to be a permutation of all slots. It is a distinct model from the draft’s original-label-only actions; it does **not** prove polynomial-size certificates for optimal strategies or membership for unrestricted `SORT-BOUND-U`.

### Invariant and correctness

Let \(P\) be the actual root-to-current-node edge path, and let \(\rho_P\) be the composition of its edge permutations in traversal order, with \(\rho_\emptyset=\mathrm{id}\). The invariant is:

\[
M(a,i)\quad\Longleftrightarrow\quad i=\rho_P(a).
\]

It holds at the root by identity initialization. On an edge with permutation \(\pi\), the stipulated update

\[
M_{\rm new}(\pi(a),i)\iff M_{\rm old}(a,i)
\]

gives \(M_{\rm new}(s,i)\iff i=\rho_P(\pi^{-1}(s))=(\rho_P\circ\pi^{-1})(s)\). Thus the invariant holds if the path-frame convention is \(\rho_{P e}=\rho_P\circ\pi^{-1}\). This is exactly the inverse-index direction induced by the checker’s `_rename`: old slot `i`’s relation moves to new slot `perm[i]` (lines 32–41, and application at line 103). Equivalently, the checker’s representation maps an old slot to its new slot, while the proposed `M` maps a current slot back to its original label.

At a query, uniqueness of the two `M` images follows because every edge permutation preserves the invariant’s bijection. Distinct slots therefore yield distinct original labels. `Ask(i,j)` charges one comparison and records its outcome in `H` indexed by original labels; neither joins nor repeated queries break the invariant, since it is defined by the *actual traversed path*, not a node-local state. At a join, different incoming paths may induce different `M` values: the store is runtime state, so it follows the selected path rather than merging the checker’s abstract guaranteed-order relations.

For a leaf annotation \(s_1,\ldots,s_n\) that is a total order of slots, emitting \(\rho_P(s_1),\ldots,\rho_P(s_n)\) is correct exactly when that annotated order is sorted in the current frame. This must be a certificate condition, not an assumed consequence of `H`: the draft explicitly requires checking output against the hidden order \(X\) (combined draft, lines 53–70). For every \(X\), correctness follows if every reachable leaf’s annotation agrees with the actual comparisons on that path; impossible branches need not be correct, but both edges remain syntactically specified as in the checker (checker lines 85–100). A verifier must reject if a reachable leaf annotation is not a permutation or does not sort for some consistent \(X\).

### Feasibility and resource bounds

For explicit certificate bit size \(C\), let \(m\) be the number of nodes/actions represented. With \(n,k\) unary and \(C=\mathrm{poly}(n+k)\), a certificate-augmented domain of size \(N'=\Theta(n+k+C+1)\) suffices: use disjoint tagged elements for key labels, slots, control labels, certificate positions/symbols, and any padding. All encodings and relation tables must be explicit.

Fixed-arity tables suffice: retain the draft’s fixed vocabulary arity bound \(v\), and add fixed-arity relations for slot-to-label frame `M`, immutable certificate data, control, output, and `H`. A fixed global variable bound is, for example, **\(v=6\)**: the draft’s FO(TC) condition is \(a+2m\le v\) with all local and nested variables drawn from the same globally fixed set (lines 21–40). This accommodates binary tables and a TC closure on pairs with bounded context; formula text may grow with the certificate, but variable names cannot. The proposed action rule must be written within that syntax; merely naming `v=6` does not establish that every desired rule is expressible.

For any fixed action exponent \(d\), permit at most \(L^d\) rule applications, where \(L=n+k+C+2\), and choose one fixed ordinary-TM clock exponent \(c\) large enough to cover parsing, validation, table initialization, rule evaluations, updates, queries, and final checking. The draft’s formula-evaluation argument gives \(O(|\phi|N'^{2v})\) table operations per rule, with ordinary indexing/parsing overhead absorbed into a fixed polynomial (lines 79–127). Thus total time is polynomial in \(n+k+C+|p|\) for fixed \(v,d,c\). Certificate and program size are polynomial by assumption; actions are at most \(L^d\); charged comparisons are at most \(k\); a full frame rewrite costs \(O(n)\) table updates per `Goto`, hence at most \(O(nL^d)\); and each rule evaluation is polynomial as above. Preprocessing/validation is polynomial in explicit input and certificate size. For \(C,|p|=\mathrm{poly}(n+k)\), these are polynomial in \(n+k\). No claim follows if certificate/program size is unbounded or table relations are succinct.

### Mismatches and gaps

- The draft’s actions are `Ask(i,j)` on original labels and `Emit(position,i)` (lines 42–55); it has no mutable slot frame, edge permutation update, or leaf order annotation. This is a real model extension, not an interpretation of existing semantics.
- Checker edges carry `perm` for both outcomes, validated as permutations (lines 85–95), and `_rename` moves old slot relations to `perm[old]` (lines 32–41). The checker has no runtime `M`, query translation through `M`, or leaf annotation; its leaf test instead checks that propagated guaranteed-order relations compare every pair (lines 69–77).
- A join in the checker intersects incoming order relations (line 107), whereas runtime frame state follows the selected incoming path. Those semantics are compatible only if the certificate’s per-leaf correctness is verified against every reachable path; the checker’s node-level intersection is not itself the runtime frame semantics.
- “Total order” must mean a **permutation listing** of every slot once, and frame updates must preserve a bijection. If either is omitted, uniqueness or leaf-permutation correctness can fail.
- The draft’s quantified predicate is a polynomial-size program existentially followed by all \(X\), and its soundness implication is explicit while completeness is open (lines 71–77, 130–136). The extension does not close that completeness gap or establish unrestricted NP/\(\Sigma_2^P\) membership.

**Sources:** `research-fo-tc-combined.md` lines 21–40, 42–77, 79–127; `/home/lubko/soring301/scripts/check_framed_strategy.py` lines 20–41, 44–53, 63–111.
