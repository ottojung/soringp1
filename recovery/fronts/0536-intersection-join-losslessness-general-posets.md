# intersection-join-losslessness-general-posets

## status

investigated

## origin

ai_proposal_unverified

## agent_id

kwOiTVgvarwnpkJYbouqIY-practiced

## exit_state

clearexit

## question

Does the reported intersection-join losslessness characterization -- F(meet) = F(incoming) iff every non-common constraint is F-redundant at the meet -- hold for every pair of n-element finite posets and all n, or does it hold only for posets reachable from the antichain root under optimal comparison play?

## basis

The #301 'framed-dag-canonical-merge' report frames the merge condition for framed sorting DAGs only; AGENTS.md and docs/research-hardness-boundaries.md section 8 warn that general-poset results do not transfer to the fixed antichain-root family without an argued reduction.

## falsifier

Exhibit a fixed n (or infinite family) with two general n-element posets for which the equivalence fails, while checking that the same failure does not occur for antichain-reachable states; alternatively show the equivalence is provably restricted to the sorting family and identify the exact reachability property it needs.

## implication

A general-poset theorem would supply a structural minimax result usable for all antichain-reachable states and strengthen the merge-based certificate foundation; a failure would show that antichain-reachability is essential, so general-poset join results cannot be transferred to the exact S(n) certificate route by assumption.

## finding_unverified

a concise board update is warranted.
All effects are now fully accounted for. Here is the closing report for this turn.

## Recovery-turn report — intersection-join losslessness front (#301)

### 1. Recovery audit (what actually happened)

| Effect | Status |
|---|---|
| Repo (`billy-dev` @ `6a96398`) | Clean working tree; **no commits, no Lean/tests/workflows/ledger/`main` changes made by me** |
| Worktrees | `framed-dag-canonical-merge-20261118exec` and `intersection-join-losslessness-general-posets` both clean except untracked `exec-report.md` (one per worktree) |
| Board #301 posts | **No duplicates.** Exactly **two** messages exist from author `SoringP1 frontier: intersection-join-losslessness-general-posets`: (a) `2026-11-18T18:01:12.762Z` (my n=4 falsification), (b) `2026-11-18T18:18:29.746Z` (my n=5 follow-up). The interrupted turn never posted under this author — confirmed by author-history scan + first-fetch timestamps |
| Ledger `~/.local/state/soringp1/frontier-ledger.json` | Front `intersection-join-losslessness-general-posets`: still `running`, `started_at 2026-11-18T16:00:23Z`, no finding/exit recorded (keeper-managed; left alone) |
| Processes | No probe/scan processes lingering; agent pool keeper healthy; Antonina reachable |

### 2. Mathematical finding (this turn's work)

The reported intersection-join losslessness characterization is **false as stated**, and the failure is **not n=4-specific**.

- **Claim under attack:** `F(meet) = F(incoming)` ⟺ every non-common constraint is `F`-redundant at the meet (`F(meet + e) = F(meet)`).
- **Falsification:** individual `F`-redundancy at the meet is **necessary but not sufficient**; losslessness requires **joint/set-level** redundancy.

**Evidence (all via the repo's own memoized exact oracle `scripts/one_ply_obstruction.minimax`, itself validated `L0 ≤ L1 ≤ F`):**

- **n=4** (exhaustive over all 219 labelled posets, 24,090 pairs): **204** lossy joins (`F(meet) > F(incoming)`) whose every extra is individually redundant — verified independently twice, plus a third clean hand-check.
- **n=5** (exhaustive over all 4,231 labelled posets, 8,952,796 pairs): **51,860** such lossy joins.

**Concrete witness (n=4):** `P1 = succ(0,0,0,3)` [F=3], `P2 = succ(0,0,1,7)` [F=2], meet `R = P1`, `F(R)=3 > F(P2)=2` → join **lossy**; extras `(2,0)`, `(3,2)` each keep `F` at 3 in isolation, but jointly `F(R + extras) = 2 < 3` → collectively **non**-redundant.

### 3. Honest limits

- Finite exhaustive disproofs at n=4 and n=5 over **general labelled** posets; no all-n infinite family yet exhibited.
- The **antichain-reachability** half of the front's falsifier (do reachable pairs ever fail?) was **not** re-checked.
- The disproof refutes the reported *criterion*; it does **not** touch join soundness (Claim 1) or budget compatibility (Claim 2).
- No Lean, no new theorem — the deliverable is a falsification only.

### 4. Status of unfinished work / next moves

1. **Antichain-reachability check** for the delivered failing pairs (front falsifier's alternative).
2. **All-n family** (e.g., ordinal-sum / chain extensions) exhibiting the same individual-vs-joint redundancy failure.

### Bottom line (for the board and for you)

A concrete, now-n=5-confirmed **falsification** of the reported merge condition is posted on Antonina #301; `S(n)` / `SORT-BOUND-U` remain unsolved, and no process success is being confused with a proof. No further external actions will be taken in this turn without your direction.

## Other metadata

```json
{
  "finished_at": 1795025996.1905236,
  "started_at": 1795022623.8191867
}
```
