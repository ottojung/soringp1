# bias-path-worstcase-sergeev-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

bHLMfmeOG5OTeNIqHiKvu1-papaya

## exit_state

clearexit

## question

Fix delta in (0,1/2). For every sufficiently large n, does there exist a height-S(n) sorting tree in which, along EVERY root-to-leaf path, the number of comparisons whose conditional outcome probability has bias at least delta is o(n), i.e. the worst-case-path strengthening of Sergeev's expectation-only o(n) bound on biased comparisons?

## basis

docs/research-sergeev-asymptotic.md records the exact entropy identity k-log2(n!)=E[k-D]+sum_v q_v(1-h2(p_v)) and only an expectation-level o(n) bias consequence; the 2026-11-23 board #301 audit confirms just the ineffective asymptotic is published in the primary source.

## falsifier

Exhibit some delta>0 and infinitely many n such that every height-S(n) tree has a root-to-leaf path containing omega(n) delta-biased comparisons, so the excess is concentrated on adversarial branches rather than spread evenly.

## implication

A positive answer would give a uniform structural constraint on optimal trees usable for succinct near-balanced certificates; a negative answer shows the sublinear excess lives on rare adversarial paths and blocks expectation-based certificate and pruning methods.

## finding_unverified

** aggregate identity (Kraft, the per‑path identity, $E[\#\text{biased}]=\Theta(1)=o(n)$) while having a path with $\omega(n)$ biased comparisons. Hence no entropy/expectation argument can prove either horn; the missing ingredient is **realizability by an actual poset decision tree**.

### 4. Discriminating experiment (n≤6, exhaustive)

Worst‑path bias is **not tree‑invariant**: at n=6, δ=0.2, some optimal trees have zero δ‑biased comparisons anywhere, others have paths with 2. Small n cannot decide an $o(n)/\omega(n)$ asymptotic, but it confirms the front is a genuine design question about *which* optimal tree.

### 5. Primary literature check

Sergeev's Theorem 3 proves only the total count $S(n)=\log_2 n!+O(n/\log^{1/5}n)$; §4–6 split each interval's "reserve" **equally** among subintervals (near‑balanced comparisons) but state **no per‑path bias theorem**. The board's 2026‑11‑23 audit already confirms the asymptotic is ineffective.

### Verdict and honest limit

I did **not** exhibit the falsifier's counterexample, and did **not** prove the front. The decisive obstacle is that settling it requires a structural bound on the worst‑path minority Kraft surplus $R$ in Sergeev's group‑insertion tree (or some optimal tree); equal‑reserve splitting suggests the front may be true, but nothing in the primary source establishes it, and the published expectation bound is provably insufficient. I did not confuse the verified expectation/majority‑path bound with the worst‑case‑path theorem the front asks for.
I'll audit the actual state before doing anything — no posts, commits, or writes until I know what already happened.
Git is clean, one board post landed, ledger untouched. Let me scan all board pages for any duplicate of my distinctive post content before concluding.
## Recovery audit — complete, no action taken

I inspected the conversation, working directory, Git state, board #301, and the durable ledger. **No new external side effects were performed this turn** — only read-only checks.

### Effects that actually happened (previous turn, confirmed exactly once)
- **Board #301 post**: exactly one, timestamped `2026-11-23T06:18:54.544Z`, author `SoringP1 frontier: bias-path-worstcase-sergeev-alln`. I scanned all 12 board pages for the distinctive phrase `EXACT PER-PATH IDENTITY` — it appears once. There is no duplicate to remove or re-post.
- **Scratch files** in `/tmp/opencode/` (`sergeev_tr20_096.pdf`, `sergeev_text.txt`, `pathbias.py`, `verify_identity.py`, `board_post_bias_path.md`) — local, outside the repository, not external actions.

### Effects that did NOT happen (verified)
- **Git**: worktree clean, `HEAD` unchanged at `6a96398`, no staged or unstaged diffs, no new commit.
- **Ledger**: entry `bias-path-worstcase-sergeev-alln` still `status=running`, `exit_state=None`, no `finding_unverified`. I never wrote to it.
- No PR, issue, CI run, Lean file, or repository note was created.

### Unfinished work
None from my research turn. The mathematical finding was delivered in the final answer and the board post landed successfully. The ledger's `running` status is infrastructure-managed by the keeper (per `docs/operations.md`, a process exit is only a recorded investigation, not a proof); I deliberately did not flip it, since that would be guessing at an external state change that isn't mine to make.

Nothing to repeat, nothing to clean up. I report this audit for review and will not re-post, re-commit, or otherwise duplicate any effect.

## Other metadata

```json
{
  "finished_at": 1795414905.7488859,
  "started_at": 1795414035.566234
}
```
