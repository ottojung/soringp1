# antonina-SZdX7dL3w5oqUlsPFxY0oL-effective

Session: ses_e09f86602ffeAuInm0I3YyBVHq
Workspace: /home/lubko/soring-fronts/unitopsort-framed-cert-audit-20261120
Created: 1795129055809; updated: 1795129110761

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f6079c2b001pQOZVW5BckesvJ)

I’ll inspect the primary paper, certificate grammar/checker, and the referenced issue/research notes first. I’ll keep this bounded to an evidence-based paper audit and won’t edit or post anything.

## Output 61 (msg_1f607c67f001Pi3eZwdlaFNYm0)

The existing frontier note already separates soundness from completeness and warns about join correlation, but it predates this specific UniTopSort audit. I’m checking the checker’s exact transition semantics against Rutschmann v2 now; I’ll also verify whether the current #301 digest or prior notes already settled this proposal.

## Output 127 (msg_1f6082d280010ITrlmtusl7YVz)

## Finding: the conversion is **not established**; no general impossibility is proved

**Evidence reviewed.** Rutschmann, *Sorting under Partial Information with Optimal Preprocessing Time via Unified Bound Heaps*, arXiv:2604.12653v2 (8 Oct 2026), especially the abstract, Theorems 4 and 5, and §3, Lemmas 9–10. I compared these with `scripts/check_framed_strategy.py` and `docs/research-framed-certificate-frontier.md` §§1, 4–5. The latest #301 digest and its `UniTopSort` search returned no matching post; the frontier note still identifies exact-budget polynomial completeness as open. The existing `n=5` root-prefix counterexample in the note concerns a different network/compiler issue and does not settle this heap proposal.

### Why the paper does not give the requested certificate compiler

UniTopSort first computes a topological order, inserts all items into a unified-bound heap in that order, and then extracts them. Rutschmann’s Theorem 4 gives **O(log e(P) + n)** sorting time/comparisons for this execution; Theorem 5 obtains **O(log e(P))** after a separate preprocessing/reduction. These are bounds on sorting a *given poset* under partial information—not on the number of nodes or bits needed to encode that execution in this repository’s certificate grammar.

In the checker, a node carries only a guaranteed strict partial order. Each outgoing comparison adds an outcome, closes transitively, and applies a slot permutation; when paths meet, the checker intersects their guaranteed relations (`scripts/check_framed_strategy.py:98–108`). The heap algorithm’s next operation and its cost, however, depend on its evolving heap state and on insertion/extraction history. The paper’s interval analysis bounds those costs using per-item insertion/extraction ranks and intervals (§3, Lemmas 9–10); it does not show that those histories can be merged whenever their order-only guarantees intersect, nor that the merged abstract state preserves the heap’s future behavior.

Thus, simply annotating framed-DAG nodes with a topological order or the paper’s interval endpoints does not supply the missing join invariant. A valid construction would need to show how every merged node’s guarantee safely represents **all** incoming histories and how the prescribed successor operation remains valid for each of them.

### Bounds and implications

A literal decision-tree unfolding of a height-\(h\) execution has at most \(2^{h+1}-1\) nodes. The paper’s **O(log e(P))** guarantee therefore yields at best an \(e(P)^{O(1)}\)-type generic tree-size bound, not polynomial size in unary \(n\); for the antichain, \(e(P)=n!\). Theorem 4’s extra \(O(n)\) term does not repair this size issue. Nor does a sorting-phase bound establish polynomial-time preprocessing for the certificate compiler: Theorem 5’s preprocessing constructs a partial-information sorting algorithm, not a polynomial-size framed-DAG certificate.

This is an **obstruction to the proposed inference**, not a proof that UniTopSort has no polynomial framed-DAG representation. The checker’s grammar is sound for certificates it accepts, but the paper gives neither an all-posets compiler with polynomial node/bit/height bounds nor a counterexample showing every such compiler must fail. In particular, it does not settle the antichain-root case or establish height \(S(n)\).

**No NP consequence follows:** polynomial certificate size, polynomial verification, and height \(k\) at \(k=S(n)\) have not been proved. The remaining uncertainty is whether a richer invariant—or a suitable restructuring of heap execution—can provide sound joins with polynomial total certificate size, especially for the antichain.
