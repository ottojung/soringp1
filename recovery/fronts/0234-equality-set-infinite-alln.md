# equality-set-infinite-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

Co3ce3Bn6jsrzH6lC3fmKM-midday

## exit_state

clearexit

## question

Is the set E = {n >= 0 : S(n) == ceil(log2(n!))} infinite, or does there exist some N0 such that for all n >= N0, S(n) >= ceil(log2(n!)) + 1?

## basis

Known equality through n=11, returns at n=17 (Stober-Weiss), gaps elsewhere; Fredman/excess questions remain open without effective all-n threshold (board #301).

## falsifier

Exhibit an infinite subsequence of n with S(n) == ceil(log2(n!)) via explicit optimal-tree constructions or known values extended by a constructive argument, or prove effective eventual separation from the information bound for all large n.

## implication

If E is finite, information-theoretic tightness is a transient phenomenon and all sufficiently large n require guaranteed additive surplus; if infinite, exact equality persists infinitely often with consequences for near-tight certificate classes and for the interpretation of o(n) excess bounds.

## finding_unverified

 frontier ledger and front checkout/agent process.
- Computed `ceil(log2(n!))` vs known `S(n)` across ranges (OEIS). Collected values for equality set E so far.
- Surveyed branch divisibility obstruction (`exact-reset-nonstar-obstruction` docs), structural lower bounds, merge-tape constraints.

### Active
- Interpreting the front: is E infinite or finite (eventual separation)?
- Evaluating competing evidence: rare returns at 20,21 vs long gaps; excess growth vs possible infinite equalities.
- Assessing whether known lower bounds force `S(n) >= ceil(log2(n!))+1` for all large n.

### Blocked
- `scripts/evaluate.py` (full poset minimax) times out for `n>=7` due to state explosion (cannot exhaustively verify large n locally).
- No confirmed all-n theorem found yet for either horn; status remains open/uncertain. Front text contains small inconsistencies (n=17 “returns”) to verify carefully.

## Next Move
1. **Fix hypothesis.** Attempt to DISPROVE “E infinite” first: check whether known lower bounds (e.g. `S(n)-log2(n!) >= c*n/polylog n`) imply eventual separation `S(n) >= ceil(log2(n!))+1` for all sufficiently large n; be explicit about fractional parts of `log2(n!)`.
2. **Test the other horn.** Or try to construct/extend an infinite subsequence with equality, scrutinizing branch divisibility constraints (propagation beyond `A_n->V_n`) and known perfect-split cases.
3. **Report.** Post a precise mathematical finding/failed approach/exact obstruction to Antonina #301, clearly distinguishing soundness vs completeness and not confusing process with proof.

## Relevant Files
- `/home/lubko/soring-fronts/equality-set-infinite-alln/AGENTS.md` – research contract
- `/home/lubko/soring-fronts/equality-set-infinite-alln/docs/problem.md` – model, encodings, realistic outcomes
- `/home/lubko/soring-fronts/equality-set-infinite-alln/docs/literature.md` – primary sources (Peczarski, Stober–Weiß, Knuth, Ford–Johnson)
- `/home/lubko/soring-fronts/equality-set-infinite-alln/docs/research-sergeev-asymptotic.md` – Sergeev excess bound `O(n/(log n)^(1/5))`
- `/home/lubko/soring-fronts/equality-set-infinite-alln/docs/research-n12-nontightness.md` – tightness vs local obstructions
- `/home/lubko/soring-fronts/equality-set-infinite-alln/docs/research-certificates-barriers.md` – barriers, states equality at `n<=11,n=20,21`
- `/home/lubko/soring-fronts/equality-set-infinite-alln/scripts/evaluate.py` – small-n exact minimax (slow)
- `/home/lubko/soring-fronts/exact-reset-nonstar-obstruction/docs/research-exact-reset-realizability.md` – odd-n divisibility obstruction `A_n->V_n`
- `/home/lubko/soring-fronts/equality-set-infinite-alln/docs/operations.md` – board/host/frontier ops
- `~/.local/state/soringp1/frontier-ledger.json` – ledger state for `equality-set-infinite-alln`
- `/home/lubko/soring301/scripts/board_digest.py` – Antonina #301 digest
Continue if you have next steps, or stop and ask for clarification if you are unsure how to proceed.
I reviewed the AGENTS.md, problem docs, literature, and board #301. Current front: **equality-set-infinite-alln** on billy-dev asking whether $E=\{n : S(n)=\lceil\log_2(n!)\rceil\}$ is infinite or eventually separated. Known equalities at $n\in\{1..11,20,21\}$, gaps elsewhere; branch-divisibility obstructions for odd $n$ exist but don't obviously force finite $E$. No definitive proof either way found yet; evaluating known lower bounds (excess grows) vs possible infinite subsequences is the main task. No repo/Lean changes made.

## Other metadata

```json
{
  "finished_at": 1793720740.7507827,
  "started_at": 1793711058.2384949
}
```
