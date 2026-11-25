# antonina-d7b2y5TBEwrOE3Jk8VAQFG-archduke

Session: ses_e0752b3f1ffed571Ls8ubZ0Vgw
Workspace: /home/lubko/soring-fronts/unified-bound-heaps-minimax-20261120/worktree
Created: 1795173469264; updated: 1795173525389

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f8ad4e05001o3MWsUFZKRVbLs)

I’ll inspect the repository’s current research framing and issue context, then read the paper’s v2 proof/source around the heap invariant and cost accounting. I’ll stop at a concrete bridge or a demonstrated barrier, without making repository or board changes.

## Output 134 (msg_1f8ade5fe001DoYCa1fb7EOUNf)

## Assessment — **B: the transfer is blocked**

**Literature (Rutschmann, arXiv:2604.12653v2, §§1–5).** The unified-bound heap is a data structure for *executing* a sorting algorithm, not a representation of minimax states. Its maintained state is a main tree over insertion indices plus balanced index trees of “leaders.” An `access(i)` reshapes the main tree and updates those indices; `addLeaf` appends an item; cleanup restores the structural invariants. In `UniTopSort`, the query rule is to insert items in a fixed topological order, then repeatedly extract the minimum. Comparisons implement that extraction for the hidden linear order. Neither the state nor the transition is defined by choosing an incomparable pair to minimize the worst child value.

The theorem’s accounting is also the wrong kind for exact evaluation: the heap operations have **amortized running-time** bounds in terms of insertion and access times; the sorting analysis derives **O(log e(P)) comparisons**, with a separate reduction handling small-edge inputs. This gives a sorting algorithm, not an equality for the exact minimax value \(F(P)\). The constant-factor \(O(\log e(P))\) bound does not say \(F(P)=\lceil\log_2 e(P)\rceil\), nor provide a recurrence for \(F\).

**Concrete falsifier for an \(e\)-only compression (project fact).** The seven-element states
`A=(0,0,1,3,5,5,37)` and `B=(0,0,2,1,1,9,59)` have the same `e=60`, but `F(A)=6` and `F(B)=7` (issues #47/#48 and the research notes). Thus a proposed transfer that identifies states solely by extension count cannot preserve exact minimax values. This does **not** refute the heap: its richer structural state may distinguish them. It shows that the paper supplies no justification for discarding the poset’s information in favor of `e`.

**Why it does not yield a framed certificate or root recurrence.** The heap theorem bounds the work of one sorting procedure on a given partial-order input. A polynomial framed certificate for `S(n)` must represent a correct adaptive comparison strategy from the **antichain root**, with sound joins and height exactly `S(n)`; an exact recurrence must account for both outcomes of each chosen query and their worst-case `F` values. The paper proves neither optimality of `UniTopSort` nor a polynomial-size representation of an *optimal* strategy. Its preprocessing cost is not comparison cost, and its comparison guarantee is asymptotic rather than an exact-budget bridge. At the antichain root, the DAG has no edges; the paper’s sparse-input reduction falls back to sorting from scratch. That remains a valid upper-bound route, but does not close optimal framed-DAG completeness or unrestricted unary membership.

**Scope and status.** This is a barrier to the proposed transfer, not a result about arbitrary-poset evaluation complexity or a lower bound for `S(n)`. The current research plan’s distinction between `O(log e(P))` sorting and exact `F(P)` is decisive here. The board’s recent entries retain `S(23)` as unresolved; nothing in this route changes that. No repository or board changes were made.
