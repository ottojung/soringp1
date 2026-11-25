# antonina-F7lMI9l6pOUmrdLma9amEV-hosmer

Session: ses_e0c6d2929ffeIII2YjY7cY7m1C
Workspace: /home/lubko/soring-fronts/coexistence-proof-optimal-move-set-20261119exec
Created: 1795087849284; updated: 1795088519188

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 448 (msg_1f39cfe120015kp783DkqlJMtE)

Posted one #301 comment (author `SoringP1 frontier: coexistence-proof-optimal-move-set-20261119exec`, createdAt 2026-11-19T11:41:40Z, id `sha256:2ZND...`). No repo/Lean/test/workflow/ledger change; worktree clean.

**Result: outcome (c) — precise obstruction + partial proof.**

- **Evidence (from scratch):** coexistence holds on all optimal-play-reachable states through n≤9 (0 failures among 2.75M labelled states at n=7 and 33,045 iso-classes at n=9); near-half coexistence is false from n=3, so the 3/11 Kahn–Saks margin is load-bearing. n=10 run was killed (no answer obtained; not claimed).
- **Partial theorem proved:** if `e(P) > (11/16)·2^{m(P)}`, then P has an optimal comparison that is both depth-balanced and 3/11-extension-balanced (information bound + the induction-recovery depth-balance threshold). Corollary: every information-tight poset `e=2^m` has a perfectly balanced optimal move that is also 3/11-balanced; ordinal sums preserve coexistence.
- **Obstruction:** Kahn–Saks gives a 3/11-balanced pair among *all* incomparable pairs (no optimality/depth constraint), while depth-balance gives an optimal pair with easy child ≥ m−2 (no extension constraint). Their conjunction needs either an optimal 3/11-balanced pair (Kahn–Saks doesn't assert optimality) or proof that every depth-balanced optimal pair is automatically 3/11-balanced (would require a depth→extension relation sharper than `e≤2^m`, and the n=5/n=7 lift witnesses show local depth drops are context-dependent). Remaining danger zone: `e ≤ (5/8)2^m`, i.e. Fibonacci-type states. No counterexample found through n=9. No all-n proof, no counterexample, no `S(n)`/`SORT-BOUND-U` consequence.
