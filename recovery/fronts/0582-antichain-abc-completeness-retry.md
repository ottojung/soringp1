# antichain-abc-completeness-retry

## status

investigated

## origin

executive_blocked_front_retry

## agent_id

7sYqRQmwTMB3deGbZGTHFH-motor

## exit_state

clearexit

## question

For every n, does the n-element antichain admit a height-S(n) comparison tree in which every internal node's chosen comparison satisfies the node-local Peczarski A/B/C condition at that node?

## basis

Board #301 01:03Z recursive-abc counterexample at n=6 and its explicit open antichain scope; Peczarski Order 23 (2006) Facts 1-2; AGENTS.md soundness-versus-completeness warning. [EXECUTIVE RETRY 2026-11-19T19:5xZ] Fresh retry of a ledger front whose Antonina agent FAILED WITHOUT A FINAL TEXT (context/tool failure, not a mathematical resolution). FIRST read the current #301 board digest and the already-investigated adjacent fronts: recursive-abc-exact-height-completeness, succinct-cert-complete-antichain, abc-certificate-checking-complexity. Decide whether the EXACT question below is already settled by them; if so, report that precisely with evidence and STOP (do not repeat their work). Otherwise attack the exact question below. Keep scratch small; never paste large outputs or media into context; post ONE concise decisive finding/obstruction to #301.

## falsifier

Exhibit an n and an exact minimax proof that no height-S(n) A/B/C-certified tree exists from A_n, or show that a certificate-starved optimal state is reachable from A_n at optimal depth.

## implication

A positive answer would give a complete local certificate grammar on the antichain and a candidate succinct exact-verification scheme; a negative answer would lift the n=6 general-poset incompleteness to an S(n) obstruction.

## finding_unverified

 is self-contained, rather than merely citing the board.
The computation timed out due to repeated extension-counting. Let me memoize extension counts globally.
Both load-bearing witnesses reproduce exactly. Let me also verify the crucial point that Q8 is **avoidable** — i.e. `G(A_8)=true` — from the antichain directly.
My independent check reproduces both witnesses (Q8: e=784,F=10,H=11; n6 general: F=4,H=5, only optimal root uncertified). Computing `H(A_8)` from scratch times out, so I'll cite the board's independently-verified census for that point. Let me check the posting interface.
Let me confirm no prior post exists under this exact front author (to avoid duplicating side effects), and check the credential setup.
No prior post under this exact author. I'll compose one concise, honest finding and post it once.
My post landed exactly once (author `SoringP1 frontier: antichain-abc-completeness-retry`, 20:08:19Z). Let me confirm the worktree is clean — no repository/Lean changes.
Done. Summary of this retry:

**Host/state:** Confirmed `billy-dev`. Read `AGENTS.md`, `docs/problem.md`, `docs/operations.md`, `docs/literature.md`, the #301 digest, and the relevant front posts. Worktree left clean at `6a96398`; scratch only under `/tmp/opencode`; no repo/Lean/ledger/main changes. posted exactly one #301 comment under the exact author string (20:08:19Z).

**Decision on adjacency (the requested first step):** The exact question — ∀n, does `A_n` admit a height-`S(n)` tree with every node A/B/C-certified (i.e. `G(A_n)` ⟺ `H(A_n)=F(A_n)`) — is **NOT settled**; it stays OPEN. But it is already thoroughly investigated, so I did not repeat that work:
- `recursive-abc` (01:03Z) refutes the **general-poset** case at n=6 — which I reproduced from scratch (`e=14, F=4, H=5`, only optimal root `{b,e}` uncertified) — but per AGENTS.md this does not transfer to `A_n` (series-prime, so composition is vacuous).
- `abc-certificate-checking`: checking dichotomy open; NP implication invalid (A/B/C certify GPC, not `S(n)≤k`).
- `succinct-cert-complete-antichain`: no report exists.
- The two **on-point** fronts (02:10Z, 00:41Z) establish `G(A_n)=true` for n≤10 by full census (starved states at n=8/9 exist but are avoidable), FJ and its lower-mid repair fail at n=7/9; all-n INCONCLUSIVE.

**Mathematical finding (independently checked):** My from-scratch engine confirmed the load-bearing witness `Q8 = up(10,8,72,0,32,0,0,10)`: `e=784, F=10, H=11`, so `G(Q8)=false`. This is a certificate-starved minimax state reachable from `A_8` at optimal depth — **exactly the front's stated FALSIFIER (2nd disjunct)**. So the front is internally mismatched: its falsifier is already met at n=8, while its literal existential question survives.

**Honest limits / obstruction:** A reachable bad state (`H>F`) is necessary but not sufficient to refute `G(A_n)` — another optimal tree can avoid it. Certification and F-optimality are independent at nodes (n=6, n=7 FJ), so A/B/C is sound but **incomplete** as a node-local grammar: a positive answer would give only "one all-certified optimal tree per `A_n`," not a complete grammar, and no complexity result (checking A/B/C needs extension counts). Deciding all-n needs either a forced-starvation lemma (none known; starvation avoidable through n≤10) or an all-n certified-closed optimal scheme (FJ/tie-breaks fail); exhaustive n=11 (~47M posets) is infeasible here. I obtained **no all-n proof or counterexample** — process success is not a proof.

## Other metadata

```json
{
  "finished_at": 1795118954.28914,
  "started_at": 1795117876.2771473
}
```
