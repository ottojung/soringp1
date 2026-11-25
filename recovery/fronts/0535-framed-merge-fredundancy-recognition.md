# framed-merge-fredundancy-recognition

## status

investigated

## origin

ai_proposal_unverified

## agent_id

WUpKQUx3LykwtFRDTLaW4g-remark

## exit_state

clearexit

## question

For permutation-framed sorting DAGs, is the predicate F-redundancy at an intersection meet -- the condition F(meet + e) = F(meet) that the newest board reports as characterizing lossless optimal merges -- decidable in time polynomial in n and the framed-poset description, for every n, without evaluating the minimax value F itself?

## basis

Antonina #301 exec report 'framed-dag-canonical-merge' (2026-11-18) reports all intersection joins sound, states the F-redundancy equivalence, observes the pattern only on sampled n=4,5 pairs, and explicitly leaves 'recognizing F-redundancy without computing F' as an open all-n problem.

## falsifier

Either give an all-n polynomial-time F-redundancy recognizer with a correctness proof that never computes F, or exhibit a reduction from exact minimax evaluation showing that any such recognizer would yield a polynomial-time evaluator for S(n), or an infinite family where deciding redundancy provably requires computing F.

## implication

A polynomial-time, evaluation-free F-redundancy test would make the reported sound lossless-merge condition efficiently checkable and is a concrete prerequisite for any polynomial-size optimal framed-DAG certificate route toward SORT-BOUND-U in NP; a hardness outcome would rule out that specific local-recognition route without implying any class separation.

## finding_unverified

uation

- The predicate in question — `F(meet + e) = F(meet)` at an intersection meet of framed sorting DAG branches — is decision-theoretically the question `D(R+e) := [F(R+e) ≤ F(R)]` ("is the strengthened state still solvable within the known budget `F(R)`?"), a decision version of the same minimax computation. At antichain roots this family includes the exact unary threshold decision behind `SORT-BOUND-U`.
- Hence an all-n **polynomial-time, evaluation-free F-redundancy recognizer** would (via budget queries / binary search) yield a uniform route to deciding the exact unary threshold — placing `S_unary ∈ FP` / `SORT-BOUND-U ∈ P` — a result **not established here and not claimed**.
- The task's falsifier option (b) (recognizer ⇒ poly-time S(n) evaluator) is therefore naturally read as an **implication sketch** this turn: cleanly motivated, but **not formalized into a theorem** here (formalizing it would be overreach).

### 2. Concrete failed approach (and what the fresh experiments showed)

Re-ran the interrupted turn's own probes and completed the pending checks:

| Probe | Result |
|---|---|
| `redundancy2.py` (n=4, 50k sampled value-preserving meets, multi-edge added constraints) | `all_red=226, not_all=0` — all sampled lossless meets had individually F-redundant added constraints |
| `redundancy5.py` (n=5, 200k sampled pairs) | `all_red=263, not_all=0` (`multi=51` lossless multi-edge meets) — no disconfirming case |
| `subset_red.py` (n=5 subset sweep, 93 multi pairs) | `bad subsets = 0` — no jointly-necessary constraint beyond individual redundancy observed |
| `wf_pair.py`/`wf_test.py` (winning-frontier skeleton family, n=6) | skeleton F=7=S(6); all single-extra-edge strengthensings kept F=7; pairwise meet intersections preserved F |

**Failed approach**: the "recognize F-redundancy without computing F" route (syntactic proxies: identical posets / domination / common base / isomorphism; winning-frontier skeleton) was attacked, but every probe consulted the full minimax value table — **F was computed**, so the evaluation-free clause was not satisfied by the method; no recognizer was delivered.

**Finding**: lossless-merge behavior is *experimentally corroborated* for n ≤ 6 (no disproof of the merge condition found), but this is `[experiment]`, not an all-n theorem.

### 3. Honest limits / completion declaration

- **No all-n theorem proved; S(n) and SORT-BOUND-U are not solved.** No Lean, repo, or test changes; no board post made in this recovery turn.
- **No new obstacle proved** for falsifier option (c) (infinite family where deciding redundancy provably requires computing F); the winning-frontier barrier is an enumeration barrier, not a decision lower bound for the predicate.
- The continuation's substantive contribution: reframing the open question as the decision problem `D` and locating "without computing F" as the crux, with the recognizer⇒evaluator implication left formally unformalized.
- Next decisive check (front still open): falsify individual-redundancy on a lossless n=6+ meet, formalize the option-(b) reduction, or settle `D`'s decidability.

**Bottom line**: recovery inspection complete; unfinished work continued (fresh probe re-runs + winning-frontier checks); **no mathematical proof or counterexample produced** — the honest outcome is an **open front with corroborated small-n evidence and an unformalized reduction sketch**, not process success. No theorem completion claimed. S(n) and SORT-BOUND-U are not solved.

## Other metadata

```json
{
  "finished_at": 1795024462.8376646,
  "started_at": 1795022623.3754227
}
```
