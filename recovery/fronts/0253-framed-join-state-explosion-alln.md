# framed-join-state-explosion-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

1TiEpplLPvf9V53k22eNn3-hypertext

## exit_state

clearexit

## question

For all n and k = S(n), is there an all-n obstruction showing that every framed DAG of height <= k sorting the antichain A_n must have >= 2^(c n log n) distinct states due to unavoidable poset-intersection joins, even when allowing arbitrary comparison choices (not just tree unfolding)?

## basis

docs/research-framed-certificate-frontier.md notes join/intersection constraints; antichain-hetero-framed-tightness shows tree<->framed height collapse but not size compression; distinct from tree-size (tree may be exponential) by allowing DAG joins.

## falsifier

Construct for arbitrarily large n some framed DAG of height S(n) with only poly(n) states that is accepted by the framed checker on A_n, or prove a general state-compression theorem achieving subexponential state count for all optimal strategies.

## implication

A uniform exponential lower bound on framed states for all-n optimal height would rule out polynomial-size framed-DAG certificates, hence provide a strong barrier to SORT-BOUND-U in NP without claiming a full complexity class separation.

## finding_unverified

tate-explosion-alln/docs/research-strategy-certificates.md` — background: tree vs hash-consed DAG sizes and quotients Table; Mahaney barrier framing (Observations 4.2, 4.3).
- `/home/lubko/soring-fronts/framed-join-state-explosion-alln/docs/research-certificates-barriers.md` and `docs/research-decision-encoding.md` — barriers vs encodings; concrete next-step experiment for n≤10 distinct poset states on optimal plays.
- `/home/lubko/soring-fronts/framed-certificate-polynomial-completeness-barrier/docs/research-framed-certificate-completeness-obstruction.md` — sibling/lossy-merge obstruction analysis; n=5 C2⊕A3 and n=6 finite witnesses; passes all questions intoDice-jam "structural obstruction" language but NOT a formal all-n proof.
- `~/.local/state/soringp1/frontier-ledger.json` — front ledger (framed-join-state-explosion-alln running, agent `1TiEpplLPvf9V53k22eNn3-hypertext`).
- `/home/lubko/soring-fronts/framed-join-state-explosion-alln/tests/test_framed_strategy.py` and `tests/test_strategy_dag.py` — sanity-check suite; run via `python3 -m unittest tests.<name>`.
- `python3 /home/lubko/soring301/scripts/board_digest.py` — board #301 digest access (--contains, --page N, --max-chars; NOT --limit).
Continue if you have next steps, or stop and ask for clarification if you are unsure how to proceed.
No external side effects occurred — the interrupted call was only a local `strategy_dag_probe` computation (no commits, posts, or board writes were made). State check: worktree clean, ledger still shows the front as `running`, and nothing was duplicated.

Where the session stands:

**Data collected (new, executed experiments):**

| n | quotient(1) | quotient(all) |
|---|---|---|
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 4 | 5 |
| 4 | 7 | 12 |
| 5 | 11 | 19 |
| 6 | 27 | 134 |
| 7 | 34 | 802 |

(n=8 was the interrupted run — too slow to complete in-shell.)

**Interpretation so far:**
- `quotient(all)` (poset-isomorphism classes reachable on *some* height-S(n) optimal play) grows fast: 19 → 134 → 802. This is consistent with `docs/research-strategy-certificates.md` Observation 3.2's suspicion that it is not polynomially bounded, but seven points can't decide.
- This connects directly to the front's obstruction hypothesis: if the optimal-play reachable class count alone is super-polynomial, a framed DAG at exact height S(n) must carry at least that many distinct guaranteed-relation sets (its node annotations), which would push any compression theorem into serious trouble.
- However, the literature notes stress these are **poset states**, not framed-DAG nodes; the framed checker's intersection/`_rename` machinery is a different object, and the proven obstruction at n=5 (C2⊕A3) and n=6 is finite-witness only.

**Honest status:** No all-n theorem (neither the obstruction proof nor a poly-state construction), no repo changes, no board post — per the front contract, insufficient for either.

**Options for next step** (your call):
1. Continue the attack: try to *formally* link the 2^((1/4−o(1)) n log²n) winning-state theorem (`docs/research-winning-frontier-barrier.md`) to framed-node counts — the strongest near-proof route for the obstruction.
2. Attempt the falsifier concretely: construct a small framed DAG with genuine multi-parent joins accepted at exact S(5)/S(6) and count nodes (cheap, and would strengthen or weaken the n=6 counterexample precedent).
3. Stop the front here and report the honest limit ("no theorem, no counterexample") without a board post.

## Other metadata

```json
{
  "finished_at": 1793742493.3017373,
  "started_at": 1793731827.3369653
}
```
