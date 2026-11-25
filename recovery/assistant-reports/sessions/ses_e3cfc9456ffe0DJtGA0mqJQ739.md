# antonina-Rord1aEkuBTwYlHQVOJnbI-observant

Session: ses_e3cfc9456ffe0DJtGA0mqJQ739
Workspace: /home/lubko/soring-fronts/curator
Created: 1794273143776; updated: 1794273530189

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 276 (msg_1c30941df001XOBJyP3zwcqetQ)

Wrote `/home/lubko/soring-fronts/curator/frontier-candidates.json` with two new fronts:

1. **`antichain-reachable-abc-tree-completeness`** — lifts the newest general-poset A/B/C incompleteness counterexample (n=6) to the exact all-n antichain question. This is the scope the 01:03Z #301 post explicitly left open.
2. **`prime-excess-vs-antichain-gap`** — tests whether series/parallel-indecomposable local excess is controlled by the global antichain excess `E(n)=S(n)-ceil(log2 n!)`, grounded in the new n=17 and n=19 prime counterexamples where excess is 2 while `E=1`.

Honest limits recorded during the check:
- I verified the candidate schema and checked the durable ledger for collisions; both IDs are absent from prior fronts.
- A scratch exact-minimax check found fully certified optimal trees from `A_n` for `n <= 6`; `n=7` exceeded the local time budget. This is finite negative evidence, not a proof.
- No board post, commit, Lean file, or repository change was made. Only the candidate JSON is new.
