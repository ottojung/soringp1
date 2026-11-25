# antonina-yhyCWfgUybt8bKftrPbFji-desultory

Session: ses_e037c1ff7ffeW5sVg7c6jdti38
Workspace: /home/lubko/soring-fronts/fotc-isomorphism-quotient-20261121
Created: 1795237863493; updated: 1795238038926

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 307 (msg_1fc8682ce001jlbrBoZ6XtGaIU)

Posted to Antonina issue #301.

Result summary:

**Table (reachable optimal-play states)**

| n | Labelled states | Isomorphism classes |
|---|---|---|
| 5 | 1551 | 19 |
| 6 | 65551 | 134 |

(Reference: n=1–4: 1/1, 3/2, 19/5, 181/12.)

**Invariant test:** Even combined, (linear-extension count, width, height) gives only 11 distinct tuples vs 19 classes at n=5, and 48 vs 134 at n=6; every individual invariant also has multi-class collisions.

**Verdict:** Scalar invariants do **not** identify the poset isomorphism class among reachable optimal-play states. An FO(TC)-definable canonical form for this restricted family cannot be obtained from these invariants; the state-dispatch route still requires full isomorphism canonicalization or a new structural invariant. This supports the prior FO(TC) small-n blocker. No repository changes were made.
