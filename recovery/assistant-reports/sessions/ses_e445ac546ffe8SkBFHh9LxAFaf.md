# antonina-6qQziKmWqZguJRJYHZDeOD-ethics

Session: ses_e445ac546ffe8SkBFHh9LxAFaf
Workspace: /home/lubko/soring-fronts/explicit-dag-sorting-upper-bound
Created: 1794149530577; updated: 1794150311114

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 217 (msg_1bbafebd50019cHn02M51HxbH2)

## Finding: the DAG-sorting route fails on the antichain — `Θ(n)` additive excess, not `o(n)`

I studied `AGENTS.md`, `docs/problem.md`, the live #301 board, and the primary sources (arXiv:2407.21591v6 and arXiv:2404.04552v4). I found a clean disproof of the FRONT for the algorithm of the cited arXiv:2407.21591v6. **No repository or Lean changes; one board post.**

### Precise claim refuted

For the `n`-antichain, the van der Hoog–Rotenberg–Rutschmann algorithm is **topological insertion sort**: a longest directed path has one vertex, and the algorithm inserts each of the other `n−1` vertices exactly once into the growing sorted path. Every query is “new vertex vs. a vertex of the path”; two uninserted vertices are never compared.

**Theorem [paper proof].** Fix any source-removal strategy and any correct finger-search implementation. The induced comparison tree has height at least

\[
A(n)=\sum_{j=1}^{n}\lceil\log_2 j\rceil
    =n\lceil\log_2 n\rceil-2^{\lceil\log_2 n\rceil}+1 .
\]

*Proof.* At insertion `i` the path has `i` vertices, so the new vertex has `i+1` possible insertion positions. It has no prior comparisons and the input is an antichain, so all `i+1` positions remain consistent. Any binary decision tree for that insertion has a branch of depth at least `⌈log₂(i+1)⌉`. An adversary follows such a branch at every insertion; the answers remain consistent with one total order. Hence some root-to-leaf path has length at least `Σᵢ ⌈log₂(i+1)⌉ = A(n)`. ∎

### The gap

Using the exact formula, one checks `A(n) ≥ n log₂ n − n`, while Stirling gives `log₂(n!) = n log₂ n − (1/ln 2)n + O(log n)`. Therefore

\[
A(n)-\lceil\log_2(n!)\rceil
\;\ge\;\left(\frac1{\ln 2}-1\right)n-O(\log n)
\;\approx\;0.4427\,n-O(\log n)
\;=\;\Omega(n).
\]

Numerically the gap is `11` at `n=32`, `448` at `n=1000`, and `5158` at `n=10000`. So

\[
U(n)-\lceil\log_2(n!)\rceil \neq o(n),
\]

and the FRONT’s first requirement is false.

### Honest nuance about the stated falsifier

The literal FALSIFIER — “leading constant at least `1+ε`” — is **not** what happens: `A(n)/log₂(n!) → 1`. The obstruction is the additive `Θ(n)` term, not a constant-factor blow-up. The FRONT is still refuted because it demands sublinear excess.

For the other cited algorithm (Haeupler et al., arXiv:2404.04552v4), the antichain has **no bottlenecks** — level 1 contains all `n` vertices — so topological-heapsort-with-lookahead reduces to ordinary topological heapsort. That paper proves only `O(log T)` comparisons up to constant factors; its Lemma 4.4/4.5 analysis is tight for the all-equal-interval antichain, giving `n log₂ n = log₂(n!) + n log₂ e`, so its published analysis also gives no `o(n)` excess. I did **not** prove a lower bound for every working-set-heap implementation, so the Haeupler heapsort variant is not refuted here; the algorithm of the cited arXiv:2407.21591v6 is.

### Construction and certificate distinction

The algorithm is polynomial-time as an algorithm, but no explicit comparison tree of height `S(n)` can be output in `poly(n)` time: it has `n!` leaves. If “comparison tree constructible in poly(n)” means an explicit tree, that conjunct is impossible for output-size reasons; if it means a uniform algorithm, it is possible but does not give the claimed height. Certificate **soundness** (checking a supplied tree/DAG) is not **completeness** (existence of a short tree); nothing here yields a polynomial certificate for `SORT-BOUND-U`.

### What this does and does not show

- It kills the DAG-sorting effective-upper-bound route as stated.
- It says nothing about `S(n)` itself: Sergeev’s `log₂(n!) + o(n)` comparison bound stands.
- It says nothing about general posets or `SORT-BOUND-U` membership.
- A recursive hybrid using optimal base cases on large blocks and the DAG algorithm only for merging is a **different** algorithm and is not covered by this refutation.

The board post is on #301 under `SoringP1 frontier: explicit-dag-sorting-upper-bound`; the worktree remains clean at `6a96398`.

## Output 294 (msg_1bbb108230010ogRarflkxrXOb)

Recovery inspection complete. **No external action was repeated, and no new side effects were created.**

### Effects that actually happened
- **Board #301:** exactly **one** matching post exists, timestamped `2026-11-08T15:03:40.212Z`, author `SoringP1 frontier: explicit-dag-sorting-upper-bound`. It is the completed finding from the prior turn. A `--contains` digest over the current board page confirms **1 unique match**, so no duplicate was posted.
- **Git:** worktree clean at `6a96398`; no commits, branches, edits, or Lean changes.
- **Durable ledger:** the `explicit-dag-sorting-upper-bound` entry is still `status: "running"` under agent `6qQziKmWqZguJRJYHZDeOD-ethics`. This is normal keeper-managed bookkeeping, not an unfinished mathematical task; I did not edit it.
- **Temporary artifacts only:** `/tmp/opencode/dag.pdf`, `/tmp/opencode/haeupler.pdf`, `/tmp/opencode/dag_post.txt`. These are scratch files, not repository changes.

### Unfinished work
None. The prior turn had already:
1. studied `AGENTS.md`, `docs/problem.md`, board #301, and the primary papers;
2. proved the antichain specialization is topological insertion sort with height at least `A(n)=Σ⌈log₂ j⌉ = log₂(n!)+Ω(n)`, refuting the `o(n)`-excess requirement;
3. recorded the nuance that the literal “leading constant ≥1+ε” falsifier is not met, and that the Haeupler heapsort variant was not refuted;
4. posted the finding once to #301 and left the worktree clean.

The only outstanding state is the ledger’s `running` flag, which the keeper owns. I am not treating the repeated recovery prompt as a reason to re-run the research or post again.
