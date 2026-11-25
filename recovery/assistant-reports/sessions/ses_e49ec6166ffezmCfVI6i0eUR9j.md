# antonina-C5vKb6BYTkY2OUpDTCSmoE-http

Session: ses_e49ec6166ffezmCfVI6i0eUR9j
Workspace: /home/lubko/soring-fronts/exec-fotc-frame-action-formulas-20261107
Created: 1794056101592; updated: 1794056124579

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 27 (msg_1b613b8d1001X1Zp4s8xgHFtNF)

The precise gap is **not closed** by the combined draft or checker: they do not provide fixed-variable FO(TC) formulas for the mutable frame actions or establish compiler correctness for those formulas. Under the specified FO(TC)\(_v\) syntax, however, there is a concrete obstruction to the requested construction.

### Exact obstruction: preserving a frame in one action formula

For a certificate edge with permutation \(\pi\), the proposed atomic frame update is

\[
M_{\mathrm{new}}(\pi(o),\ell)\ \leftrightarrow\ M_{\mathrm{old}}(o,\ell)
\]

for every old slot \(o\) and original label \(\ell\). A direct relational-structure encoding of the new \(M\) requires carrying the old frame while relating an old and new slot and label. This is a **ternary transition relation** on \((o,\ell,\ell')\) only if the permutation is applied to slots; more explicitly, the update condition relates old slot \(o\), new slot \(s\), and label \(\ell\), with \(\mathrm{Perm}(node,outcome,o,s)\) and old \(M(o,\ell)\). Thus it needs the simultaneous variables `node,outcome,o,s,label` (five names), before also naming the next control node, query answer, or other action context.

The draft’s FO(TC)\(_v\) definition allows only a globally fixed set of variable names; renaming bound variables does not provide fresh names beyond that set. Consequently, even the straightforward action formula cannot be justified by the draft’s Lemma A: no actual formula or register encoding is supplied that keeps all needed values live within a fixed variable budget while updating the entire frame. This is an exposed proof gap, not a proof that every possible encoding needs unbounded variables.

### What the checker establishes—and does not

`check_framed_strategy.py` validates an explicit DAG with topologically forward edges, checks each edge permutation, propagates guaranteed partial orders, intersects incoming orders at joins, and rejects any *reachable* leaf whose guaranteed order is incomplete. Its `_rename` convention is old-slot \(\to\) new-slot: `renamed[perm[i]]` receives the renamed row for old slot `i`. It also checks budget against the longest reachable path.

It does **not** validate unreachable leaves’ sorting orders: lines 72–78 perform that check only when `relations[v] is not None`. Nor does it define a logical action semantics, verify output positions or permutation frames against inputs, or prove a uniform TM compiler theorem. Its join intersection is sound for the checker’s guaranteed-order abstraction, but is not itself a proof that an FO(TC) machine preserves the intended slot-to-original-label invariant on every input permutation.

### Required details remain unproved

The combined draft’s formula-evaluation bound applies to formulas already in its precisely defined syntax and explicit vocabulary. It does not establish the requested action formulas, certificate preprocessing, an augmented-domain/table-size bound, or a single clock covering the proposed frame updates. In particular, a mutable \(M\) update must touch \(n^2\) pairs per frame transition under an explicit table representation; that cost is polynomial, but must be counted together with formula evaluation and certificate preprocessing. Giving an `Ask` primitive that returns the smaller original label and increments the charged count is a model change/primitive interpreter operation, not an FO formula. Likewise, `Emit`, atomic replacement of \(M\), and `Halt` need explicit interpreter semantics unless separately encoded.

No complete fixed-variable construction or lower bound ruling all such constructions out follows from the two files. Therefore I cannot supply the requested exact rule formulas, prove the path invariant on every permutation, or claim a fixed variable limit and clock. The draft’s narrower FO(TC) evaluation lemma and the checker’s finite certificate checks remain separate results; neither closes this frame-action/compiler-correctness gap. No edits, commits, or posts were made.
