# antonina-zHMyYVli1ShgaDu33Dh6cv-soaked

Session: ses_e3efd6ef4ffei27TloRafWsW4u
Workspace: /home/lubko/soring-fronts/curator
Created: 1794239533337; updated: 1794242799574

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 392 (msg_1c13330b3001OAj5s2ljJxs9FG)

Recovery/state check: host `billy-dev`, worktree at `6a96398`. No `frontier-candidates.json` existed before this turn, so no interrupted curator effect was duplicated. The only change is the requested JSON file; no board post, commit, Lean change, or other external action was made.

Research attempt and honest limits:
- I rejected the natural all-`n` claim that the maximum local excess is attained at the antichain: `W` and `Merge(2,4)` already have excess `1` at `n=5,6` while `E(5)=E(6)=0`. Not proposed.
- I checked a two-ply disjoint-opening variant through `n=7`; it held, but it is a special case of the already-open matching-prefix frontier, so it was not proposed.
- I tested the universal per-cover ratio on random `n=8` posets. The best observed ratio was `0.1`, below `0.1366386755`; this is neither a counterexample nor an all-`n` argument.
- New exact data point: `A_14 (+) A_14` is height two, `e=(14!)^2`, `F=2·S(14)=76` by ordinal-sum additivity, and `ceil(log2 e)=73`, giving excess `3`. This sharpens the board’s excess-2 `A_12 (+) A_12` witness. It does not establish unboundedness.

The four proposed fronts are in `/home/lubko/soring-fronts/curator/frontier-candidates.json`:

1. `universal-local-excess-cover-ratio` — all-poset version of the board’s `n≤7` ordinal-sum ratio bound.
2. `kwl-move-quotient-dimension` — whether a fixed full/paired `k-WL` level can be complete for exact move values.
3. `height-two-f-decision-np` — NP membership for the height-two minimax decision problem, which would imply `SORT-BOUND-U ∈ NP` via the depth-one state `Q_n`.
4. `height-two-excess-unbounded` — boundedness versus unboundedness of height-two information excess.

None of these fronts is claimed as proved or verified; the JSON records only precise falsifiable questions and their consequences. The main open limits are the absence of an all-`B` ratio proof, no `k≥3` WL evidence, and the fact that bounded height-two excess would be stronger than the still-open boundedness of `E(n)`.

## Output 442 (msg_1c1342ef4001610He40K4NkDNy)

Recovery inspection complete.

**What actually happened in the previous turn**
- Host: `billy-dev`; repository `/home/lubko/soring-fronts/curator`; worktree at `6a96398`.
- The only external effect was creation of the requested untracked file `/home/lubko/soring-fronts/curator/frontier-candidates.json`.
- The file is present, valid JSON, and contains exactly four fronts with IDs:
  - `universal-local-excess-cover-ratio`
  - `kwl-move-quotient-dimension`
  - `height-two-f-decision-np`
  - `height-two-excess-unbounded`
- All schema length constraints pass; no ID collides with the 448-entry frontier ledger.
- No board #301 post, commit, branch, PR, Lean file, or other repository change was made.

**Durable record**
- The four candidate IDs are still absent from `~/.local/state/soringp1/frontier-ledger.json`. That is expected: importing curator proposals is the keeper’s job, not the curator’s. There is no curator-side unfinished action.

**Uncertainty**
- None about the external effects. The only pending state is the keeper’s normal import/reconciliation cycle, which should not be duplicated or forced manually.

No further work was performed and no side effect was repeated.
