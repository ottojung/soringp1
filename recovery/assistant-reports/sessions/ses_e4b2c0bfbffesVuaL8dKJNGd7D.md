# antonina-V4Ey5Khk5WYtL9HTmhPW7G-http

Session: ses_e4b2c0bfbffesVuaL8dKJNGd7D
Workspace: /home/lubko/soring-fronts/exec-budgeted-dfs-turing-audit-20261107
Created: 1794035151938; updated: 1794035207125

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 47 (msg_1b4d4167f0017Cdt9a5QqVdvCa)

The central counting argument looks plausible, but the note currently jumps from a Python DFS/prototype accounting to “polynomial time per node” on a Turing machine. I’m checking the parameterized node bound and edge handling explicitly; those determine whether the claimed exponents follow without treating arbitrary-precision or stack operations as free.

## Output 91 (msg_1b4d45136001aXtbNo6X4T35PW)

## Audit result

**Conclusion: the intended bounds can be defended, but the current note does not yet supply the requested deterministic Turing-machine cost proof.** I found no counterexample to the DFS decision procedure. Its correctness and node-count argument are sound, and an explicit multi-tape implementation yields the advertised bounds. The gap is in making that implementation and its cost accounting explicit—not in the asymptotic exponents.

This is a **paper-proof derivation**, not a machine-checked result. I made no repository edits, commits, posts, or Lean changes.

### A precise cost bound

Use a deterministic, fixed finite number of work tapes, with read-only input tape for threshold decision. Let `n` be the parsed unary first-field length, `k` the second, and `N=n+k+1`. For a call with budget `d`, let `B=binom(n,2)`. A transcript has at most `d` directed comparison edges.

A concrete implementation can store the transcript as packed fixed-width endpoint labels on a work tape, plus an explicit DFS stack. At each node it:

1. checks whether the transcript’s directed graph is total by testing reachability for all label pairs;
2. if not total and budget remains, scans the `B` pairs in lexicographic order, tests incomparability by reachability, and recursively explores the two orientations according to the OR/AND recurrence;
3. pops the child transcript before continuing the parent’s scan.

Reachability can scan the transcript edge list while performing a graph search. Even using a deliberately simple implementation—repeatedly scanning the edge list to enumerate outgoing edges—the search costs polynomial time in `n+d`; candidate enumeration and totality testing do too. Counters and labels have `O(log(n+d+2))` bits. Copying or undoing a transcript, advancing pair cursors, binary counter arithmetic, pushing/popping stack records, and parsing/rewinding the input all cost polynomial time in `n+k+d+2` per visited node. Thus, for an absolute constant `c`, a conservative bound is

\[
T_{\rm node}(n,d) \le (n+k+d+2)^c,
\]

where the `k` term is only needed for input handling; a threshold call itself need not repeatedly scan the input.

The recursion depth is at most `d+1`. Each node has at most `B` candidate pairs and at most two recursive calls per candidate, so the total number of nodes is bounded by

\[
1+(2B)+\cdots +(2B)^d \le (2B+1)^{d+1}.
\]

This deliberately overcounts short-circuiting, failed branches, and early total-order returns. Therefore the fully charged running time is at most

\[
(n+k+d+2)^c(2B+1)^{d+1}
=2^{O(d\log(n+2))}\operatorname{poly}(n+k+d+2).
\]

The polynomial per-node factor is charged, not assumed free. For `d≤k≤N`, `n≤N`, it is absorbed in `2^{O(N log(N+2))}`. Hence `SORT-BOUND-U` is decidable in deterministic time `2^{O(N log(N+2))}`.

For space, the explicit stack stores at most `d+1` frames, each with a pair/candidate cursor and `O(log(n+d+2))` bits of counters. The shared transcript is length at most `d`; reachability uses polynomial workspace (for example, a visited vector and a queue of labels). No closure matrix or pair list per frame is needed. This gives polynomial space; the sharper `O((d+n)log(n+2))`-bit claim follows with packed transcript/stack records and one BFS workspace. The Python scripts are prototypes, not implementations that establish these machine costs.

### Function computation and edge cases

For `n≥2`, `U(n)=n⌈log₂ n⌉` is a valid merge-sort comparison bound. Binary search over `[0,U(n)]` takes `O(log(U(n)+1))` probes. Summing the per-probe bounds (each depth at most `U(n)`) gives

\[
2^{O(U(n)\log(n+2))}\operatorname{poly}(n)
=2^{O(n\log^2(n+2))}
\]

time to compute `S(n)` on input `1^n`, with polynomial space. The polynomial factors at recursive nodes remain charged; there are only `O(log U(n))` probes, and their costs are bounded by the largest-depth estimate times that probe count.

For threshold inputs, reject malformed encodings first. If `n≤1`, then `S(n)=0`, so accept for every valid `k`. Otherwise, if `k≥U(n)`, accept by the merge-sort upper bound. In the remaining case, run the DFS at depth `d=k`. The binary-search computation of the function does **not** have input length `N=n`; its probes use budgets as large as `U(n)`, which is why its exponent is `n log² n`, not the threshold language’s `N log N`.

The note’s stated unary decision proof uses a read-only input tape and its exact space wording depends on how parsing/counters are implemented; the explicit construction above supports polynomial space, with the sharper stated space bound under the packed representation. The numeric-function time claim is also a machine-cost deduction, not a consequence of the Python benchmark.

### Correctness and complexity interpretation

The recursion is correct by induction on remaining budget: a sorter chooses an incomparable pair, and must win for both adversary answers. A comparable pair cannot improve the information state. Each legal answer preserves acyclicity; reaching a total order means the transcript determines the unique ranking. Thus `CanSort(∅,k)` decides exactly whether a sorting decision tree of height at most `k` exists, i.e. whether `S(n)≤k`.

Consequently:

- `SORT-BOUND-U ∈ DTIME(2^{O(N log(N+2))})` with polynomial space.
- `S_unary ∈ FEXP` with time `2^{O(n log²(n+2))}` and polynomial space.
- As in `docs/problem.md`, threshold membership and unary-function evaluation are polynomial-time equivalent using the known `O(n log n)` upper bound and polynomially many unary threshold queries. This does not make their displayed exponential bounds identical.
- These are upper bounds only. They imply no lower bound, hardness result, or class separation.

### Specific caveats found

- The geometric node bound is valid, including the root and shallow leaves; it is safer to state the geometric sum rather than just `(2B)^d`, especially at `d=0`.
- “Polynomial time per node” needs an explicit machine implementation and must include transcript scans/copies, reachability, pair enumeration, counters, input operations, and backtracking. The derivation above supplies such a conservative bound.
- `scripts/budgeted_dfs.py` stores transitive-closure bitmasks and uses Python integers/lists; its runtime and space do not themselves prove a Turing-machine bound. `scripts/transcript_dfs.py` demonstrates the shared-transcript idea but is likewise not a cost proof.
- The DFS result is a valid route to the machine-time bridge, but it does not retroactively turn the separate memoized-DP sketch into a machine-cost theorem. The exact claim should be attributed to this explicit budgeted DFS construction.
- The “already-total `P`” behavior is right. The empty and singleton cases need no search. The `k≥U(n)` shortcut applies only to the empty initial poset, as used for `SORT-BOUND-U`.

No lower-bound or class-separation conclusion follows: this is an algorithmic upper bound for a fixed unary threshold language and its associated function, not a hardness argument.
