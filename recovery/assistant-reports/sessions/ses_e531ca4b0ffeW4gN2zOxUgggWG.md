# antonina-MIwqKcTlgaSEntV75Osxzf-hasn

Session: ses_e531ca4b0ffeW4gN2zOxUgggWG
Workspace: /home/lubko/soring301
Created: 1793901943638; updated: 1793902002086

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 87 (msg_1ace3b652001Hj36o6ge5KGzJE)

**Result: no improved all-\(n\) bound or model-specific lower bound established.** The requested frontier remains open. The main obstruction is precise but limited: Savitch-style recomputation can shrink the *reachability workspace*; it does not by itself remove the DFS’s stored history of alternative choices. Conversely, that accounting is not a lower bound against other implementations.

### Exact DFS accounting

For \(1^n\#1^k\), first handle \(n\le1\) and the trivial-yes case \(k\ge U(n)=n\lceil\log_2 n\rceil\). Otherwise \(k=O(n\log n)\). The exact minimax DFS has depth at most \(k\), with an \(O(\log n)\)-bit candidate-pair cursor per existential sorter frame. The universal adversary’s two outcomes are explored sequentially: after the first returns, the frame must remember whether to try the second. A transcript edge costs \(O(\log n)\) bits, and the path has up to \(k\) edges. Thus this implementation stores \(O(k\log n)\) bits of transcript and cursors.

Comparability can be recomputed from the transcript. A straightforward graph search uses \(O(n\log n)\) workspace; it is shared, not replicated per frame. Total space is therefore
\[
O(k\log n+n\log n)=O(n\log^2 n)
\]
bits for the unary **function** computation. For threshold decision the bound is \(O((n+k)\log(n+2))=O(N\log N)\), where \(N=n+k+1\). Read-only unary input need not be copied: its head positions and counters cost \(O(\log N)\) bits. Binary search for \(S(n)\) uses \(O(\log n)\) threshold calls, with \(O(n\log n)\) maximum budget.

### Why recomputation does not settle it

Savitch’s theorem gives directed reachability in \(O(\log^2 n)\) space, so replacing BFS can remove the \(O(n\log n)\) reachability term. But the transcript and, crucially, the suspended DFS frames’ cursors remain. The resulting bound is still \(O(k\log n)=O(n\log^2 n)\). Savitch does **not** erase the path: its recursive reachability algorithm stores its own bounded recursion, and it says nothing about the outer game’s pending existential choices and universal obligations.

A checkpoint/replay idea faces the same issue. Keeping every frame’s cursor retains \(O(k\log n)\) bits. Keeping fewer checkpoints requires replaying the prefix to recover earlier cursors and determine which universal branch remains; this can multiply time substantially. No schedule or encoding was found that proves \(O(n\log n)\) or \(O(n)\) space while retaining a uniform deterministic evaluator and accounting for all pending obligations. The \(O(n^2)\)-bit alternating-game state does not solve this either: \( \mathrm{APTIME}=\mathrm{PSPACE}\) establishes polynomial space, not the desired smaller bound.

This is an obstruction to these direct DFS/replay approaches, **not** a lower bound for the implementation, let alone for all machines deciding `SORT-BOUND-U`. The full winning-frontier theorem rules out methods that enumerate all those states, but explicitly does not rule out selective or symbolic evaluation.

### Falsification and status

The proposed shortcut “use Savitch to remove path storage” fails because it confuses reachability’s workspace with the DFS stack. The proposed shortcut “discard cursors and recompute them” has no demonstrated time bound: cursor state includes the frame’s position in the existential enumeration and which adversary answer is next. Known exact values through \(n=22\) can test finite implementations but cannot establish either asymptotic space claim. No computation, tracked edit, Lean work, or external posting was made.

**Primary sources:** Savitch, “Relationships between nondeterministic and deterministic tape complexities,” *JCSS* 4 (1970), 177–192, DOI [10.1016/S0022-0000(70)80006-X](https://doi.org/10.1016/S0022-0000(70)80006-X); Chandra, Kozen & Stockmeyer, “Alternation,” *JACM* 28(1) (1981), 114–133, DOI [10.1145/322234.322243](https://doi.org/10.1145/322234.322243). For the sorting-specific frontier, see the project’s exact DFS accounting and winning-frontier barrier, plus Sergeev, “On the asymptotic complexity of sorting,” ECCC TR20-096 (2020), for \(S(n)=\log_2(n!)+o(n)\).

**Next decisive step:** either exhibit a uniform checkpoint/reconstruction scheme with a proved bound on peak storage for *all* pending choices and its time blowup, or prove a lower bound for a clearly delimited DFS configuration model. Neither would, by itself, settle unrestricted deterministic space for unary threshold evaluation.

## Output 111 (msg_1ace42eef001xs5pvjIa7StfmD)

The previous research task’s effects are clear: it made **no tracked edits, commits, Lean changes, or external posts**. The working tree is clean on `billy-dev`; `HEAD` is `6a96398` (also `main`), with no new commit attributable to that task. The only files found in the workspace are existing repository records.

The research deliverable was completed in the prior response, so there is nothing unfinished to continue. I found no evidence of an interrupted or uncertain external side effect requiring review.
