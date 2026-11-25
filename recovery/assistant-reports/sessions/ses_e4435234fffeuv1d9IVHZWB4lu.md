# antonina-QyCQyotX7Gs3Mxg5aOUaWk-dramatic

Session: ses_e4435234fffeuv1d9IVHZWB4lu
Workspace: /home/lubko/soring-fronts/haeupler-heapsort-antichain-excess
Created: 1794151996848; updated: 1794152633940

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 373 (msg_1bbd38700001JJ67kZclNT2cPs)

## Result

I studied `AGENTS.md`, `docs/problem.md`, the current #301 board, and the primary sources (arXiv:2404.04552v4, especially Sections 4–5 and Appendix C). I did not create Lean or repository changes. I posted a correction and a new theorem to #301.

### 1. The front is based on a citation error

Appendix C of arXiv:2404.04552v4 is **not** a Haeupler heapsort variant. It describes only the alternative algorithm of van der Hoog–Rotenberg–Rutschmann [48]: find a longest path `P`, initialize `L=P`, then insert the remaining vertices by exponential/binary search. The paper explicitly calls that algorithm **“topological insertion sort.”**

Haeupler et al.’s own algorithm is **topological heapsort** in Sections 4–5. Thus the already-posted `A(n)=Σ⌈log₂ j⌉` lower bound is a valid obstruction for [48]’s insertion family, but not for Haeupler’s heapsort.

### 2. The actual antichain specialization is ordinary heapsort

For `n ≥ 2`, the `n`-antichain has all `n` vertices on level 1, so it has no bottlenecks (`b=0`). Topological heapsort with lookahead then puts all sources in `H`, leaves `B` empty, and every iteration is Case 1: `delete-min(H)`. It is exactly Algorithm 1, i.e. heap-based selection sort — not insertion or merge sort.

The insertion-sort adversary does **not** transfer: on the antichain every key is already in the heap, and the heap root is already known to be the minimum.

### 3. New all-`n` lower bound for the concrete pairing-heap implementation

**Theorem.** Let `T_n` be the comparison tree of topological heapsort (with or without lookahead) on the `n`-antichain, using a pairing heap whose insertion compares the new item only with the current root. Then for all `n ≥ 8`,

\[
\operatorname{height}(T_n)\;\ge\; n-1+\left\lceil \log_2((n-1)!)\right\rceil
\;\ge\; \log_2(n!)+\frac n2 .
\]

So the excess over the information bound is `Ω(n)`, not `o(n)`.

**Proof.** Fix any insertion order, even an adaptive one. The adversary answers every insertion comparison with “new item > current root.” Then the root is always the first inserted item `r`, and every later item is attached as a direct child of `r`. No comparisons among the non-root items are made during insertion.

After all insertions, the known poset is exactly the star

\[
r < x \quad\text{for every }x\ne r,
\]

which has `(n-1)!` linear extensions. The insertion phase used exactly `n-1` comparisons. By the decision-tree lower bound, completing the sort from this state needs at least `⌈log₂((n-1)!)⌉` further comparisons. Adding gives the result, using `log₂(n!) = log₂ n + log₂((n-1)!)`.

This also explains why the paper’s analysis cannot be sharpened to `o(n)` on the antichain: Lemma 4.5 is tight there, giving

\[
\sum_v \log_2 w(v)=n\log_2 n
=\log_2(n!)+\frac{n}{\ln 2}-\tfrac12\log_2(2\pi n)+O(1/n),
\]

so the method naturally produces an additive `Θ(n)` term.

### Honest limits

- The theorem applies to the **concrete pairing-heap instantiation**. The abstract “heap with the working-set bound” is not a single algorithm: a heap that spends more comparisons during insertion could leave a stronger poset, so the family still has no single well-defined height function.
- This does **not** prove anything about `S(n)` or `SORT-BOUND-U`. It is a lower bound for one algorithm family, not for all comparison sorters.
- It is not the insertion-sort obstruction. The extra comparisons here come from the fact that the `n-1` insertions only establish a star/tournament minimum, not from `i+1` possible insertion positions.
- The general-poset `O(log T)` guarantee is an upper-bound sorting theorem, not a completeness certificate for `S(n)`; it says nothing about optimality of the tree height.

So the front’s first alternative (`log₂(n!)+o(n)`) is false for Haeupler’s natural heapsort implementation. Its second wording (“insertion/merge family”) is also wrong, but the `Ω(n)`-excess conclusion holds for a different reason.

## Output 426 (msg_1bbd47f05001wE49knsegir20o)

State check complete. No repeated external actions were taken in this turn.

**Verified effects**
- Git worktree: clean at `6a96398`; no repository changes, commits, Lean files, or tests were created.
- Durable board record on #301: exactly two comments from this work exist:
  - `2026-11-08T15:41:15Z` — citation correction and the antichain specialization obstruction.
  - `2026-11-08T15:42:40Z` — the all-`n` `Ω(n)` lower bound for the concrete pairing-heap implementation.
- Local evidence files remain under `/tmp/opencode/post_haeupler*.md` and `post_haeupler*_result.json`.

**Unfinished work**
- None from the research task. The mathematical finding was completed and reported, and the board posts were already made.
- I did **not** repost either comment.

**Finding, for the record**
Appendix C of arXiv:2404.04552v4 is the van der Hoog–Rotenberg–Rutschmann insertion-sort algorithm, not a Haeupler heapsort. Haeupler’s antichain specialization is ordinary heap-based selection sort. For the standard pairing-heap insert, an adversary can force the `n−1` insertions to reveal only a star poset, giving

\[
\operatorname{height}(T_n)\ge n-1+\left\lceil\log_2((n-1)!)\right\rceil
=\log_2(n!)+n-O(\log n)=\log_2(n!)+\Omega(n).
\]

So the `o(n)`-excess alternative is false for that concrete implementation. The abstract family with an unspecified working-set heap remains ill-posed as a single all-`n` height function. This is a lower bound for the algorithm family, not for `S(n)` or `SORT-BOUND-U`.
