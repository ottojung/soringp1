# Hunt for genuinely new research gaps

Session: ses_dfde98cd1ffeUbY4GoRxosCyF8
Workspace: /home/lubko/soring-fronts/curator
Created: 1795331355450; updated: 1795331542050

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 5 (msg_20216734b001IX4SJSb25DmPet)

I'll start by reading the required documents and the ledger in parallel.

## Output 172 (msg_20218f513001Pi1erMrXBt25R5)

I've read the contract, problem/operations/literature docs, the newest notes (`research-plan.md`, `research-realizability-window.md`, `research-fo-tc-strategy-programs.md`, `research-core-threshold.md`, `research-width-two-threshold.md`), the 7-day board digest, and mined all 687 ledger entries (ids + full question/falsifier/implication/basis text) with targeted keyword searches for each idea below.

## Verdict: frontier is near-saturated, but I found 2 defensible genuinely-new directions

Both are all‑n, sharp, falsifiable, grounded in the model, and — by exhaustive keyword audit of the ledger — not duplicates of any existing front, nor of the inversion/Claim‑C, slack/excess/defect/Fibonacci/disjoint‑union/WL/height‑two clusters. (Closest existing fronts are `pairwise-vs-arbitrary-test-gap`/`comparison-restriction-hardness` — which restrict *test type*, not the *pair set* — and `optimal-tree-depth-spread`, which is a different polarity; neither covers these.)

---

### Candidate 1 — Minimum comparison-graph sparsity for optimal sorting
**Question (all‑n):** For a graph $G$ on $[n]$, let $S_G(n)$ be the min worst-case comparisons to sort $n$ distinct keys when every comparison must be an edge of $G$ (so $S_{K_n}(n)=S(n)$, and $G$ must be connected). Define $g(n)=\min\{|E(G)|:S_G(n)\le S(n)\}$. Does there exist a fixed $c$ with $g(n)\le c\,n\log n$ for all $n$ (sparse graphs suffice for optimal sorting), or is $g(n)=\Omega(n^2)$ for infinitely many $n$ (the complete graph is essentially necessary)?
**Concrete falsifier:** Either exhibit, for every $n$, a poly-time-constructible $G_n$ with $O(n\log n)$ edges and a written minimax solver certifying $S_{G_n}(n)=S(n)$ (e.g. start with $n=4,5$: is a 4-cycle enough for $S(4)=5$?); or prove an $\Omega(n^2)$ edge lower bound for any $G$ supporting height $S(n)$. A single $n$ with $g(n)>c n\log n$ refutes the stated constant.
**Complexity implication:** Positive answer reduces the root minimax branching from $\Theta(n^2)$ candidate pairs to $O(n\log n)$, a concrete route to shrinking the $2^{O(n\log^2 n)}$ exact-evaluator exponent (an "achievable in principle" target in `problem.md`); negative answer is a barrier ruling out this sparsification route.
**Why new / one-line reason:** Ledger has zero hits for "sparse graph / graph of allowed comparisons / minimum edges / sorting on a graph / distinct pairs compared"; the existing restriction fronts concern arbitrary-vs-pairwise *tests*, not a restricted edge set.

### Candidate 2 — Bounded per-key comparison load in an optimal tree
**Question (all‑n):** For each $n$, let $\Lambda(n)$ be the least $L$ such that there is a height-$S(n)$ correct sorting tree in which every key participates in at most $L$ comparisons on every root-to-leaf path. Is $\Lambda(n)\le c\log n$ for all $n$ and some fixed $c$ (an optimal sorter where each element's rank is decided locally), or does some infinite family force a single key into $\omega(\log n)$ comparisons on some path of every optimal tree? (Lower bound $\Omega(\log n)$ is immediate; merge sort attains $O(\log n)$ but is not height-optimal, while Ford–Johnson-style main-chain elements plausibly incur linear load.)
**Concrete falsifier:** Compute exact $\Lambda(n)$ with a faithful minimax solver tracking max per-key incidence for $n=6,7$ and search for a height-$S(n)$ tree with all per-key loads $\le c\log n$; refute by exhibiting $n$ where every height-$S(n)$ tree has a key of load $>c\log n$, or prove the $O(\log n)$ bound.
**Complexity implication:** A positive answer supplies a new *local* structural restriction on optimal strategies, usable toward polynomial-size succinct strategy certificates (the live NP/coNP frontier); a negative answer rules out element-local/compositional evaluation routes that assume bounded key load.
**Why new / one-line reason:** Ledger has no front on per-key or per-element comparison participation; `optimal-tree-depth-spread` and `s-optimal-tree-average-depth-gap` concern leaf depths/averages, not per-key incidence along paths.

---

**Saturation note:** Beyond these two, I could not isolate a third independent direction that survives the exclusions and the ledger audit. Every other angle I tested (fixed-gap decision, inverse/level-set function, best-case depth, rounds-of-adaptivity/network depth, word-RAM/branching-program/LP-SOS certificates, descriptive-class membership, entropy/greedy strategies, self-reducibility, census growth exponents) is already represented by one or more ledger fronts, or collapses into the explicitly excluded clusters. I would treat any further proposed front in those areas as a duplicate. No files were written.
