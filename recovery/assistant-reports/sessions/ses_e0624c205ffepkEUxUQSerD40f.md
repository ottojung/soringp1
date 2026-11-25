# antonina-VjpqZxaO94P2FJdtkfjjFo-downhill

Session: ses_e0624c205ffepkEUxUQSerD40f
Workspace: /home/lubko/soring-fronts/exec-ceiling-drop-unit-20261120
Created: 1795193257606; updated: 1795193486191

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f9db413f001zMz3MV0pXBNk0y)

I’ll first verify the Billy-dev instructions, the model/research plan, and the concise #301 board digest; then I’ll independently check the small-n evidence and target structured counterexample searches without modifying repository artifacts.

## Output 109 (msg_1f9dbc32d001dJ7AN4Kfx1LXa7)

The prior scratch I found verifies the telescoping identity only on sampled states, not the proposed all-posets claim. I’m rebuilding the relevant finite check from the exhaustive poset/minimax engine, then will specifically test every optimal adversary-path branch (not just one tie-break), since that quantifier is the delicate part.

## Output 149 (msg_1f9dd2678001WMooCwuEKilF3M)

The exhaustive n=6 check found a genuine counterexample: on an optimal root-to-state path, a minimax-optimal comparison has both children at equal minimax value, but one has only 16 of the parent’s 36 linear extensions, causing a two-bit ceiling drop. I’m validating the exact path and the recurrence certificate now; this refutes the universal π≤1 claim, so the remaining report will explain the repayment mechanism rather than overclaim a theorem about all paths.

## Output 256 (msg_1f9dea207001MQIMvCI3H7UbAH)

**The universal \(\pi_i\le1\) claim is falsified at \(n=6\).** On a minimax-optimal path, the state with successor masks \(P=(30,16,8,0,0,0)\) has \(e(P)=36\), \(F(P)=6\). The optimal comparison \((1,5)\) has both children at \(F=5\); one child \(Q=(30,16,8,0,0,18)\) has \(e(Q)=16\). Hence \(\lceil\log_2 36\rceil-\lceil\log_2 16\rceil=2\).

An exact exhaustive minimax recurrence over the 130,023 labelled six-element posets verified the counts and reachability. Along an optimal continuation from \(Q\), a later \(\pi=0\) step repays the negative per-step loss, consistent with the ceiling-loss identity. This shows bounded-excess arguments cannot assume losses are always 0 or 1.

I posted the finding and a wording correction to Antonina issue #301. The worktree remains clean; no repository, Lean, test, workflow, or ledger changes were made.
