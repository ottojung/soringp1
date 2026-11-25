# antonina-M1FCPxUYNbr4yBM0Hm2ITc-calhoun

Session: ses_e3b81c01fffeQ5zSCCIbHjQEQ4
Workspace: /home/lubko/soring-fronts/curator
Created: 1794297970663; updated: 1794300335468

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 386 (msg_1c49b2a290011ml2MD3zfhjthx)

I've completed a thorough survey. Let me record the key independent computation I ran and then write the curator output.

## Output 428 (msg_1c4a20eec001yp4dNUEjLTJoGQ)

I studied `AGENTS.md`, `docs/problem.md`, the 496-front ledger, and the newest board #301. The board is saturated with general-poset certificate work (A/B/C soundness, GPC, excess, certificate starvation), and every recent post explicitly states "no `S(n)`/`SORT-BOUND-U` consequence." The ledger already covers time/space bounds, class membership, certificate completeness, barriers, and structural theorems.

**Claim attacked.** "The number of distinct poset states on some height-`S(n)` optimal play from the antichain is polynomially bounded." I computed the exact counts independently for `n=0..7`:

| n | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| optimal-play states | 1 | 1 | 3 | 19 | 181 | 1551 | 65551 | 2769663 |
| `A001035(n)` | 1 | 1 | 3 | 19 | 219 | 4231 | 130023 | 6129859 |
| ratio | 1 | 1 | 1 | 1 | 0.826 | 0.367 | 0.504 | 0.452 |

The counts are exact minimax values (verified against `scripts/evaluate.py`: `S(6)=10`, `S(7)=13`), and the BFS follows only moves with `max(F(child₁),F(child₂)) = F(P)−1`. This is evidence against the polynomial claim, but it is **not a disproof**: the ratio is non-monotone (`0.83, 0.37, 0.50, 0.45`), `n=8` is infeasible on this host, and no all-`n` argument is obtained. The claim remains open.

**Curator output.** I wrote one new front to `frontier-candidates.json` (validated, no exact id/question duplicate in the ledger): `optimal-play-state-fraction-lower-bound`, asking whether the optimal-play state count is at least a constant fraction of `A001035(n)` for all `n≥4`. It is grounded in the computation above and in `docs/research-certificates-barriers.md` §8, which names this measurement as the smallest compelling next step.

**Honest limits.** The front is a follow-up to the existing `optimal-play-state-count-census` front (which left `n≥6` uncomputed), so it may be read as a refinement rather than a fully independent direction; I judged the new lower-bound question distinct enough to propose. The computation is exact only through `n=7`. No Lean, repository, or board changes were made; the worktree is clean at `6a96398` with only the required untracked `frontier-candidates.json`.
