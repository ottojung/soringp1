# antonina-TDnLtZLtVF1PbpOS2ZRsPR-frontier

Session: ses_e4be00f70ffeI0EQfq6scDOr9p
Workspace: /home/lubko/soring-fronts/exec-budgeted-stack-space-20261107
Created: 1794023354573; updated: 1794023375860

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1b41ff2a800110Izxd1kVuqzoZ)

I’ll locate the current research plan and the budgeted DFS proof, then audit the specific stack representation and restoration behavior only. I’ll keep this read-only and distinguish an obstruction for that representation from any general space lower bound.

## Output 37 (msg_1b42010fe001on0Ju4nto0T2wg)

## Audit result

I do not see a reversible or succinct encoding that reduces the stack to \(O(n\log n)\) bits while preserving the full DFS state and its restoration behavior. There is a concrete obstruction for a natural, explicitly scoped representation: **a self-contained, fixed-width-per-level transcript stack that can be popped and restored directly** still needs \(\Theta(d\log n)\) bits in the worst case. This is not a lower bound on all ways to implement the algorithm.

### Why the current stack has \(O(d\log n)\) bits

At each recursion level, DFS must retain the existential comparison choice and enough universal-branch control to resume after a child returns. In the transcript implementation, these are represented by the comparison labels and a candidate-pair cursor, each using \(O(\log n)\) bits. At depth \(d=O(n\log n)\), that is \(O(d\log n)=O(n\log^2 n)\) bits, before the shared reachability workspace.

The choices cannot in general be reconstructed from the current poset: a poset can have many different comparison transcripts that induce it, while DFS’s continuation depends on which candidate pair and branch it was evaluating. A representation that stores only the current poset therefore loses necessary continuation state unless it also stores or recomputes that history.

### Obstruction for the natural stack representation

Scope the claim to a **locally decodable, directly restorable stack**: each level’s choice and continuation are encoded in its own fixed-width cell, and returning from a child restores the parent by popping, without replaying the DFS from an earlier checkpoint.

At a level with \(\Theta(n^2)\) candidate pairs, the parent cursor can take \(\Theta(n^2)\) values. A cell that distinguishes all those continuations needs \(\Omega(\log(n^2))=\Omega(\log n)\) bits. The comparison choice itself is also a pair of labels and has \(\Theta(\log n)\)-bit descriptions. Thus this representation requires \(\Omega(d\log n)\) bits when such levels occur at depth \(d\). Variable-length or reversible coding does not change the worst-case total if every level’s independently restorable continuation must remain represented: arbitrary valid paths can use choices and cursors throughout the stack, and popping a child must recover the exact parent continuation.

This falsifies a straightforward per-frame compression of the existing transcript-plus-cursor stack. It does **not** rule out a global encoding with shared information, a checkpoint-and-replay scheme, or a different DFS organization. Those alternatives may trade space for extra computation; the direct-stack argument does not establish that their time remains within \(2^{O(n\log^2 n)}\).

### Conclusion

The proposed reduction is obstructed for the natural direct-restoration stack representation, but the broader \(O(n\log n)\)-space direction remains unresolved. The proof note’s \(O(n\log^2 n)\)-bit bound is an upper bound, not a storage lower bound. No general space lower bound or complexity consequence follows.
