# antonina-WlTpUISvATnN5UivKXBNA5-yaroslavl

Session: ses_e49ff1d2fffeKD2LOOlIHAky9g
Workspace: /home/lubko/soring-fronts/exec-fotc-history-tc-independent-20261107
Created: 1794054873871; updated: 1794054914956

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 55 (msg_1b6012274001KCLNtCjSCtPKlu)

## Verdict

**The path-specific reflexive-transitive-closure construction is sound for replaying any supplied framed DAG under the stated deterministic-action model, but only after repairing the model’s domain and annotation encoding.** Under that repair, it gives a uniform polynomial-size `FO(TC)_v` program and polynomial-clock simulation for each explicitly supplied polynomial-size framed DAG. It does **not** show that polynomial-size framed DAGs exist for all `n` at height `S(n)`, or imply NP/Σ₂P membership for the unrestricted language.

### Replay correctness

Let `π_e` be the edge permutation, mapping each old slot `i` to new slot `π_e(i)`, as in checker `_rename` (lines 32–40). A history determines the outcome of every comparison on the actually executed path: `H(i,j)` means `i<j`, and a repeated query has the same answer. Thus the deterministic certificate, together with `H`, uniquely determines the next edge, including at joins.

Use states `(node,slot)`. Enable an edge transition only when `H` records the comparison outcome for that edge; carry its slot map through `π_e`. TC reachability from `(root,s)` then gives exactly the slot map obtained by following the enabled path. Because certificate nodes are topologically ordered, every transition moves strictly forward in the node coordinate. Consequently, a path that learned an outcome later cannot reach an earlier node and use it to enable a different earlier edge. Nor can a branch-specific outcome enable an edge on another branch: the source node must itself be reachable, and at each reachable comparison exactly the outcome recorded by `H` is enabled. At a DAG join, only the incoming path actually selected by the earlier outcomes is reachable; there is no merging of alternative histories in this replay relation.

The direction is the checker’s direction: old slot `i` moves to `perm[i]`, and a relation `i<j` becomes `perm[i]<perm[j]`. Applying that same map successively along the path reproduces the checker’s frame semantics.

### The essential model repair

As written, the proposed state relation cannot simply be added to the stipulated input/store structure:

* There are `M` certificate nodes and `n` slots, so `(node,slot)` needs `M n` states. The stated domain has `N=Θ(n+k+1)`, but the certificate may have size `C=|p|` and `L=n+k+C+2`. Neither `M` nor the required pair domain is guaranteed to fit in that domain.
* A fixed vocabulary with arity at most `v` does not permit an explicit relation of unbounded arity. “Fixed vocabulary” alone also does not grant a predicate for each certificate node. Certificate relations and node/slot pairs must be explicitly represented in the structure, not accessed through an oracle or a succinct relation.
* Leaf annotations may contain `n²` order facts for each node. The checker computes them by propagation and intersection; their size is polynomial, but they are not automatically available as atomic relations in the original store.

A suitable repair is to define the compiler’s explicit domain with size `N'=Θ(n+k+C)` (or use a padded domain of that size), with explicit unary node/slot/certificate-position encodings and fixed-arity tables for certificate fields, edge permutations, and checker annotations. Since `C` is polynomial in the supplied parameters, this still gives polynomial size. Equivalently, encode pairs by explicit elements in a domain large enough for all `M n` pairs. The definition must specify these encodings and their construction cost. Merely changing the asymptotic `N` symbol without defining the domain and relations is insufficient.

### Fixed variables, output, and costs

With the repaired encoding, the transition test needs a constant number of variables: source and target node/slot coordinates, the fixed comparison endpoints/outcome, and the query-history lookup. The context width plus twice the TC endpoint width is therefore bounded by a constant. The formula and its fixed-variable vocabulary can be chosen once, independent of the supplied certificate. The leaf test can consult the checker-propagated annotation table for that node and test whether every pair of current slots is ordered. A sound annotation is sufficient: every actual order reaching that leaf extends the annotation, so a total annotation guarantees the correct output order. The program must emit the labels according to this order (or use an explicitly supplied, checked leaf-output table); the verifier’s final check against `X` remains necessary.

For an explicit certificate with `M` nodes, checking validity and computing annotations costs polynomial time, for example `O(poly(M,n))`; table storage is polynomial. Compilation may do this once and include the checked tables in the program, or the fixed interpreter may check them at runtime. Either way, the cost is polynomial in `n+k+C`, not necessarily in `n+k` alone when `C` is unrestricted. Each replay step performs polynomially many table/formula operations, and each comparison action incurs exactly one charged query; repeated comparisons still count separately, as required. A path uses at most the DAG height in comparisons. Thus a polynomial-size certificate yields polynomial program length, polynomially many actions, and a fixed polynomial machine clock after fixing the certificate-size polynomial and the repaired encoding. This is a compiler for supplied certificates, not a compiler that discovers them.

The cited definitions are `research-fo-tc-combined.md` §§21–40, 42–70 and the checker’s explicit frame convention at `_rename` (lines 32–40). The former currently fixes `N=Θ(n+k+1)` and explicitly tabulated relations; that is the precise mismatch requiring repair. The checker’s annotations and join rule are at lines 63–108.

**Conclusion:** the replay lemma itself survives repeated comparisons, joins, and branch-specific outcomes. The proposed compiler claim is valid only with an explicit certificate-augmented domain/store definition and a precise leaf-output convention. Without those, the original model does not state the resources or vocabulary needed to express the proposed construction. No all-`n` optimal framed-DAG existence or complexity-class membership follows.
