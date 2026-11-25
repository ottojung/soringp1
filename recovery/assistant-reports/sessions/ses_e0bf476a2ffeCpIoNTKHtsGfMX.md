# antonina-tKzPJw0563yPFvuBlULbAm-sides

Session: ses_e0bf476a2ffeCpIoNTKHtsGfMX
Workspace: /home/lubko/soring-fronts/reachable-poset-class-universality-alln
Created: 1795095759236; updated: 1795095833716

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 207 (msg_1f40c9fee001ifJ8pVubYDeF1P)

Posted to #301.

Result: every unlabelled poset class on `n` elements is reachable from the `n`-element antichain by comparison learning. The proof is the standard labelled-poset reachability argument (enumerate target comparabilities; skip those already implied by closure, so the rest are legal moves), then project labelled paths under isomorphism. The symmetry-quotient DP already reaches all `A000112(n)` classes for `n≤9` (counts match exactly), so no invariant excludes any class; the excluded family is empty.

Consequence: reachability gives no `2^{o(n²)}` compression route — the unlabelled quotient state space remains `2^{Θ(n²)}`. The remaining open compression question is the smaller *optimal-play* subset, not reachability.

Worktree remains clean at `6a96398`; no repository, Lean, test, or workflow changes were made. Scratch stayed under `/tmp/opencode`.
