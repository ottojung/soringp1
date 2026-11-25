# antonina-EatO8buxC7479kniyKXkRj-atoms

Session: ses_e0e6f6034ffetJFHqr4p1xUKql
Workspace: /home/lubko/soring-fronts/framed-optimal-height-polysize-existence
Created: 1795054149666; updated: 1795054672149

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f190a1b50018M0bsSWwqeSEKo)

I'll start by understanding the environment and the required documents. Let me explore the repository structure and git state in parallel.

## Output 21 (msg_1f190b0dc001kuP4Z7c0B89ZA0)

I'm already on `billy-dev` with a clean worktree. Let me read the key documents and find board #301.

## Output 44 (msg_1f190bbb8001m2E7F3zMJLUOTw)

Let me read the frontier evidence doc and fetch the board digest.

## Output 59 (msg_1f190cd2c001tB85XJYKr6zP0n)

Let me search the board for relevant prior work on framed certificates and check for any prior work from an infrastructure failure.

## Output 74 (msg_1f190e259001Q4I2dzS7UweLBi)

Let me check the ledger for my front and look at the framed strategy checker to understand the precise certificate grammar.

## Output 89 (msg_1f190f7830013ijp1KVkEM8tcn)

Let me find my exact front ID in the ledger and check for any prior work by this front.

## Output 117 (msg_1f1911dc6001LEw673a6GriZZ5)

My front is `framed-optimal-height-polysize-existence`, status running, no prior board post. Let me check for scratch work from a possible prior interrupted run, and read the framed strategy checker precisely.

## Output 132 (msg_1f191322e001Tv769csPLVvXWG)

I have a precise model now. Let me read the most relevant prior findings on the board (from cached dumps) to avoid repeating negative results, then build a fresh attack.

## Output 170 (msg_1f1925b3f001h1ogb3Xa6TksaA)

I found a potentially decisive approach. Let me verify a key claim about the model against the board's mentioned "19-node n=7 certificate" before proceeding — this is critical.

## Output 181 (msg_1f1951a42001Pe2p60quPspMwv)

The board references a 19-node n=7 certificate calling ACCEPT at depth 13 — this contradicts my initial lower-bound reasoning, so I must inspect it directly. Let me locate and verify it.

## Output 201 (msg_1f1960039001MyJgz0f632CL4q)

Let me simulate all 5040 inputs through this certificate to find the flaw in my lower-bound reasoning.

## Output 212 (msg_1f1961d33001jAeEEQBNnPTQuf)

The simulation reveals the flaw: nodes are reached at different depths on different paths. Let me quantify the path-length distribution and node reuse.

## Output 223 (msg_1f1964c8a001kiM41U4oWpCvyV)

The n=7 certificate shatters the level-based approach (single node served 2688 paths at three different depths). Let me verify a sharper structural claim: whether the checker's per-node relation can have minimax value exceeding the remaining budget — i.e., whether any local F-value invariant is even necessary.

## Output 234 (msg_1f196f0b60012HjsaAUShJLnFz)

Let me inspect the certificate's edge structure to document exactly why counting invariants fail, then verify the model-fidelity point about merges.

## Output 245 (msg_1f1973ec2001QEhfeW1pIXc8Gs)

This reveals the key mechanism: 10 of 18 nodes send both outcomes to the same child — outcomes are encoded in edge permutations, not graph branches. Let me find how to post to board #301.

## Output 272 (msg_1f1978da2001CNaaNnUhHjuuZY)

I have a clear picture now. Let me re-verify the worktree is clean, then write and post the #301 report.

## Output 301 (msg_1f19845640013zMKU3M4c7m0P1)

The post succeeded. Let me verify it landed on the board and confirm the worktree is still clean.

## Output 312 (msg_1f1985ff8001A7KM1l150AF7HM)

## Report: `framed-optimal-height-polysize-existence`

Worked on `billy-dev` (clean worktree at `6a96398`, no repo/Lean/test/ledger changes). One #301 post landed at `02:17Z`.

**Result: the FALSIFIER was NOT established; the FRONT remains open.** I attacked the claim and report a concrete failed approach plus the exact obstruction, not a proof.

**Concrete failed falsifier attempt (level-counting invariant).** I tried to prove that a node on "level S(n)−1" serves at most two longest paths, forcing ≥ (n! − 2^{⌊log₂ n!⌋})/2 ≈ 2^{Ω(n)} nodes — which would disprove the FRONT. This invariant is false. I verified the checker-ACCEPT 19-node, depth-13 certificate for n=7 by simulating all 5040 inputs:

- 5040 distinct root-to-leaf paths funnel into **one** leaf, reached at path positions **10–13**;
- internal node 17 is reached at positions 10, 11, 12 and serves 2688 inputs;
- 10 of 18 comparison nodes route **both** outcomes to the same child;
- 5040 paths are realized by 19 nodes.

So nodes have no unique depth, per-node path multiplicity is unbounded, and leaves/paths are heavily shared — every per-level or path-count invariant collapses.

**Where the information actually lives.** Each input corresponds to a distinct composed permutation frame σ with σ(π)=sorted. With V nodes there are ≤2V edge permutations whose products along paths number up to (2V)^{S(n)} ≫ n!, so there is no counting/group obstruction to encoding all n! inputs in poly size. This is the compression mechanism that defeats the counting approach.

**Soundness ≠ completeness (model fidelity).** The checker never evaluates minimax F at internal nodes; it checks only acyclicity, leaf totality, and max path ≤ budget. Soundness concerns the union of real inputs reaching a node, not LE(R_v). Hence the "lossless merge needs F(P∩Q)=F(P)=F(Q)" condition and its known n=5 non-transitivity constrain only fixed-tree meet-compression — they do **not** lower-bound sound framed DAGs. Likewise 2n!−1 reachable labelled posets (decision trees) and the winning-frontier state count are structural/general-poset results, not framed-DAG bounds.

**Exact obstruction.** A disproof requires showing no poly-size choice of comparisons + edge permutations realizes all n! sorting frames within height S(n) — a succinct-optimal-sorter representation lower bound. All available techniques fail for the reasons above, and such fixed-polynomial lower bounds are unprecedented here. Small-n data (9 nodes at n=4, 19 at n=7, both checker-ACCEPT at exact S(n)) also rule out starting the disproof by small counting. Crucially, even a full disproof would only block this grammar; it would not place SORT-BOUND-U outside NP.

No mathematical theorem or counterexample was produced — the FRONT stays open, consistent with the project's stated barrier.
