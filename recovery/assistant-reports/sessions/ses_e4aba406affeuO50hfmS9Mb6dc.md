# antonina-oMCVY6WQUN8yCelzXtrsUW-lion

Session: ses_e4aba406affeuO50hfmS9Mb6dc
Workspace: /home/lubko/soring-fronts/exec-s23-instrumented-20261107
Created: 1794042609614; updated: 1794042642381

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1b545c1bf001u5EGI90g1t4fW2)

I’ll first verify the isolated worktree and read the governing research and algorithm documents alongside the cited paper. I’ll keep any experiment bounded and will not start an n=23 search.

## Output 61 (msg_1b546015b001GBxFYVgFdOG45Q)

## Result

The actual Stober–Weiß §4 pipeline is **not ready for a faithful, bounded n=23 prototype in this worktree**. I made no file changes and launched no search.

**Evidence — literature:** The cited paper specifies the partial-backward-search coverage lemma and describes implementation techniques, but reproducing the reported pipeline requires more than adding counters to the existing toy prototype. The toy implementation explicitly lacks the efficiency-threshold pass, congruence reduction, and predecessor enumeration. The paper’s implementation also relies on particular canonicalization/isomorphism handling, linear-extension computation, storage/chunking, and search parameters. The documents inspected here do not supply a runnable reference implementation or a validated n=23 configuration with measured per-layer workloads.

**Coverage semantics:** Lemma 4.2 supports an absence-as-NO conclusion only for forward-reachable states within the stated coverage conditions—particularly the efficiency threshold and the full-layer boundary. An incomplete or heuristic table cannot use absence as proof. A sound result excluding sorting in 74 comparisons would establish `S(23) ≥ 75`; proving `S(23)=75` additionally requires the matching upper bound.

**Next falsifiable experiment:** Obtain the authors’ implementation (or independently specify and validate each of the missing components), then run a small, bounded reproduction at a documented reference setting—cross-checking `n=16..18` outcomes or exact small-n cases—before estimating n=23. Record per-layer states, congruence classes, extension-count calls and work, memory/disk, and wall/CPU usage. Only after that validation should an n=23 preflight estimate be considered. No n=23 limits or run are proposed from this evidence.

## Worktree and provenance

- Worktree is clean at `c865b23968388d59316cc994501508d3782be90a`.
- No files or hashes changed.
- Primary source consulted: Stober–Weiß, arXiv:2206.05597v2, especially §§4–5.7. The repository’s existing toy-prototype limitations are recorded in `docs/research-bidirectional-advice.md`.
- Unresolved: availability of the authors’ implementation, its exact configuration for `C=74`, and measured extension-count and per-layer data needed for a credible resource estimate.
