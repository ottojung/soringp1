# antonina-1S5Ex0NXXD09kRXcd52rFd-brain

Session: ses_e48aa7805ffeu47q218i3IIKnY
Workspace: /home/lubko/soring-fronts/exec-fotc-independent-audit-20261107
Created: 1794077198389; updated: 1794077234641

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 55 (msg_1b755cf3d001YFQbiSTla1rgSz)

## Audit result: the compiler claim is not established by the available materials

The cited `docs/research-fo-tc-combined.md` is absent from this checkout, and I found no other document defining the fixed-variable FO(TC)\(_v\) program model or the proposed compiler. So I can audit the framed checker’s permutation semantics, but cannot verify the claimed resource bound against the intended program semantics.

### Edge-permutation direction

The checker defines `perm[i]` as the **new slot occupied by old slot `i`**. It applies that convention to relations by mapping every pair `(i,j)` to `(perm[i],perm[j])` (`scripts/check_framed_strategy.py:32–41, 103`).

Thus, if a node’s map `M_v[s]` means “original label currently in slot `s`,” then after an edge permutation `p` the correct update is:

`M_child[p[s]] = M_parent[s]`

Equivalently, `M_child[t] = M_parent[p⁻¹[t]]`. Applying `p` directly to the map’s index in the opposite direction is wrong.

The outcome is added using the current slots first, then the relation is renamed by `p` (`:98–103`). Any compiler must likewise interpret the comparison and its result in the pre-permutation frame, and only then update the slot map. This direction is clear from the checker; whether the prior compiler used it correctly cannot be determined without its construction.

### Fixed-variable storage and runtime

A polynomial-size explicit DAG and its edge permutations are finite tables, but that alone does **not** show they can be stored and accessed by a fixed-variable FO(TC)\(_v\) program with polynomial combined runtime.

A valid translation needs to specify, at minimum:

- the encoding and domain for node IDs, slot IDs, table addresses, and labels;
- how the DAG and each edge’s permutation are represented and accessed by the program;
- how the current node and the entire slot-to-label map are represented as configurations of the fixed-variable transitive-closure relation;
- how each transition computes the next node and updated map in the stated combined-cost model;
- why all relation arities and the number of variables are bounded by the fixed model, rather than growing with `n` or certificate size.

An explicit list with `m` nodes and `n`-entry permutations has polynomial length when `m,n` are polynomially bounded. But if the program must query a table by a tuple containing node, edge, and all `n` slot values, that is growing arity—not a fixed-variable encoding. Conversely, a serialized configuration with local address-based lookups might suffice, but its operational semantics and runtime need to be proved. “One control rule per DAG node” does not supply that proof by itself.

### Advice and input-permutation access

The certificate and the program must be separated carefully. If the compiled program is specialized to a particular certificate, that certificate can serve as certificate-specific finite data—provided its length and lookup cost are included in the combined bound and it is not silently nonuniform advice depending on `n` or the input permutation.

The outer verifier’s access to an input permutation cannot simply be transferred to the program. The checker’s job is to validate a certificate against all possible input orders; it is not an execution of the compiled sorter on an input permutation. A program that reads the permutation as an oracle, or starts with its sorting order already encoded in the slot map, would not establish an adaptive sorting-program translation. The program should receive only the permitted input representation and discover comparison outcomes through its charged Ask operations.

### Scope of any positive result

Even a sound polynomial-cost compiler for each supplied framed DAG would establish only **certificate compilation**: given a DAG, produce a program preserving its charged Ask count and meeting the claimed size/runtime bounds. It would not prove that every `n` has a polynomial-size framed certificate at height `S(n)`. The frontier document explicitly identifies that all-`n` optimal-certificate completeness statement as open (`docs/research-framed-certificate-frontier.md:27–34, 189–191`).

**Conclusion:** permutation semantics are auditable and require the inverse-index update above. The FO(TC)\(_v\) storage, fixed-arity encoding, combined-runtime, and no-leakage claims remain unsupported here. I found no concrete counterexample to a suitably specified translation, but the current evidence does not justify asserting one.
