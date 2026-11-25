# antonina-uVUcDZ0j6TcGr1jRXyJOK0-earn

Session: ses_e4b28bb8bffeu9pk95MWZ5R9G1
Workspace: /home/lubko/soring-fronts/exec-budgeted-dfs-turing-audit-20261107
Created: 1794035369078; updated: 1794035404862

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 54 (msg_1b4d76783001I5vao8iBGgQSSx)

## Independent review

**Conclusion:** the DFS argument supports the claimed deterministic time bounds as a **paper proof**, subject to the ordinary fixed-multitape TM model and explicit polynomial-cost bookkeeping below. It does not, by itself, close `docs/kernel-results.md`’s machine-time proof gap as a **kernel-checked theorem**: the Lean library has no formal machine/resource model or proved implementation-to-cost correspondence.

### Bounds and accounting

Let \(B=\binom n2\), and use labels and counters in binary. A transcript of depth at most \(d\) has at most \(d\) directed comparison edges. Testing reachability by scanning that transcript for outgoing edges costs polynomial time and \(O(n\log(n+2))\) work bits: for example, a visited vector, a stack of at most \(n\) labels, and scan/index counters. A totality test and an on-demand scan of all candidate pairs use at most polynomially many such searches. Updating the transcript, maintaining the candidate cursor, and returning from a child also take polynomial time per node. Thus there is a fixed polynomial \(q\) such that the work at a DFS node is at most \(q(n+d+1)\); this is a TM implementation argument, not a conclusion from the Python prototypes.

The call tree has root depth \(0\), and every recursive call reduces \(d\) by one. With at most \(2B=n(n-1)\) child calls per node, its exact coarse bound is
\[
\sum_{i=0}^{d}(2B)^i
\]
for \(n\ge2\), rather than just \((2B)^d\). For \(d\ge1\), this is at most \((2B)^{d+1}\); for \(d=0\), it is \(1\). This gives
\[
T_{\rm DFS}(n,d)\le q(n+d+1)\sum_{i=0}^{d}(n(n-1))^i
=2^{O(d\log(n+2))}\operatorname{poly}(n+d+1).
\]
The root term handles the \(d=0\) case without relying on a zero exponent. Actual calls are further limited by short-circuiting; the coarse bound needs no assumption that every potential branch is reachable.

Each branch is legal: the selected pair is incomparable in the current transcript’s reachability order, so adding either orientation cannot create a directed cycle. Both answers are possible extensions of the current strict partial order. A transcript is precisely the path’s accumulated comparisons; when a child returns, its appended edge is removed and the parent resumes its cursor. Thus this DFS explores actual reachable game histories, not arbitrary posets or an imagined full tree stored in memory.

For \(n\ge2\), parse the unary input and count \(n,k\) with counters bounded by \(N=n+k+1\). Compute \(U(n)=n\lceil\log_2 n\rceil\) using integer bit-length arithmetic. If \(k\ge U(n)\), accept by the merge-sort comparison bound. Otherwise \(k<U(n)\), run the DFS with \(d=k\). Parsing, constructing counters, and the trivial cases cost polynomial time and space in \(N\). The DFS time is bounded by
\[
2^{O(k\log(n+2))}\operatorname{poly}(N)
\le 2^{O(N\log(N+2))},
\]
and its transcript stack plus one reachability workspace uses
\[
O((k+n)\log(n+2))=O(N\log(N+2))
\]
work bits. For \(n\le1\), \(S(n)=0\), so accept for every valid \(k\); this also covers \(k=0\). Malformed inputs can be rejected during parsing in polynomial time.

For the **function** input \(1^n\), binary-search the integer interval \([0,U(n)]\). Monotonicity of the threshold predicate makes this return the least feasible budget, namely \(S(n)\). There are \(O(\log(U(n)+1))\) probes; the largest budget is \(O(n\log(n+2))\), and all probes use unary threshold workspaces of the stated size. Consequently the total is
\[
2^{O(n\log^2(n+2))}
\]
time and \(O(n\log^2(n+2))\) work bits, including input scanning and outputting the binary answer. The decision input length is \(N=n+k+1\); the function input length is \(n\). These are distinct bounds. In particular, the decision bound is \(2^{O(N\log(N+2))}\), not obtained by silently substituting the function budget \(U(n)\) for the supplied \(k\).

### Issues checked

- The note’s \((2B)^d\) node expression omits the root for \(d=0\). The geometric-sum formulation above repairs this harmless edge case and preserves both asymptotic claims.
- The “polynomial per node” statement needs an explicit uniform implementation. Transcript scans and reachability supply one; even a deliberately loose polynomial in \(n+d+1\) is absorbed by the exponential node bound.
- A strict comparison transcript is acyclic by induction, but a TM implementation should rely on that invariant or explicitly reject cycles; it must not treat arbitrary inconsistent transcripts as legal game states.
- In `transcript_dfs.py`, the stated space accounting is an intended reference design, not a machine proof. In particular, Python’s recursion frames, list objects, adjacency construction, and garbage collection do not establish the claimed bit bound. The prose also says the reachability workspace is released before descent; that describes the intended implementation, not a guarantee supplied by Python.
- The separate `budgeted_dfs.py` uses closure bitmasks and materializes an incomparable-pair list, so it does not witness the transcript-only space bound. Both scripts are prototypes; their tests support small-instance correctness only.

### Status of the kernel-results gap

This independently supplies a paper-level uniform multitape runtime/space argument for the DFS-based bounds, and therefore sharpens the informal \(2^{O(n^2)}\) algorithm sketch in `docs/upper-bound.md` for these encodings. It does **not** close the specifically identified kernel-results gap as written: there is no kernel-checked theorem that an explicit machine implements the recurrence with these costs, nor a formal connection from that machine to the Lean sorting model. No lower-bound or class-separation inference follows. No files were changed.
