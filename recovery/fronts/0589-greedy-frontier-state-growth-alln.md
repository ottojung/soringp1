# greedy-frontier-state-growth-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

xUXMudZRwNefHp5KNUZs49-portfolio

## exit_state

clearexit

## question

Let G(n) be the value of the sorting game against the maximum-linear-extension adversary and let R_k(n) be the set of poset states reachable from the n-antichain by any sorter strategy under greedy-adversary answers within k comparisons. Determine whether |R_{G(n)}(n)| is bounded by a fixed polynomial in n for all n, or grows superpolynomially.

## basis

docs/research-winning-frontier-barrier.md proves exponentially many winning states for the full adversary; independent beam searches here produced thousands of distinct greedy-adversary states already at n=8-9; docs/research-compression-next.md fixes the poset-state model. No ledger front studies the greedy-reachable frontier.

## falsifier

Exhibit an infinite family of n for which the greedy-adversary reachable state set at the optimal budget has size exp(Omega(n)) by a counting or entropy argument, or conversely prove a uniform polynomial bound on the number of such states.

## implication

A uniform polynomial bound would make G(n) evaluable in polynomial time by explicit greedy-frontier search and, if G(n)=S(n), would yield an FP algorithm for S(n); a superpolynomial bound shows the greedy restriction evades the known winning-frontier enumeration barrier.

## finding_unverified

r `n=4,6,8` are distinct, reachable, and every resolution is a verified extension‑count tie.

## Complexity implication [deduction]
The polynomial alternative is refuted, so the proposed route — evaluating `G(n)` (and `S(n)` if `G(n)=S(n)`) by explicitly enumerating the greedy‑frontier ball in polynomial time — is blocked: that ball is already exponential.

## Distinctions and honest limits
- This is an **enumeration/counting obstruction, not a time lower bound** — a selective or symbolic search need not list all states (same caveat as `research-winning-frontier-barrier.md`).
- It is a direct construction **at the antichain root**, not a general‑poset hardness result, and it says nothing about **certificate soundness vs. completeness** for any certificate system.
- It does **not** settle whether `G(n)=S(n)` for all `n` (open; true for `n≤6`), and yields no class separation for `SORT-BOUND-U`.
- **Lower bound only**; true growth may be larger (small‑`n` data ≈ `2^{2.8n}` at `n=6`). The proof uses only equality of two extension counts via an automorphism, so the general `#P`‑hardness of computing `e(P)` is irrelevant.
- Web literature search was unavailable this pass, so literature grounding is limited to the repo's baseline notes; the max‑LE adversary is the standard adversary behind the halving/information bound, and I found no prior treatment of this specific reachable‑set question there.

I did not manufacture a stronger claim than I can defend: the concrete result is the `exp(Ω(n))` lower bound, and the polynomial bound is disproved.
Recovery inspection (no actions repeated):

- **Git / repo state:** `billy-dev` at `6a96398`, worktree clean (`git status` empty). No commits, no Lean files, no tests, and no `main`/CI changes were made.
- **Board (durable external effect):** exactly **one** post by this front is present on Antonina #301 (page 1, `2026-11-20T04:25:51.332Z`, author `SoringP1 frontier: greedy-frontier-state-growth-alln`), verified via `board_digest.py --contains "greedy-frontier-state-growth-alln"` on page 1 (1 match) and page 2 (0). `/tmp/opencode/post_result.json` records exit 0. I did not and will not post again.
- **Scratch/local artifacts (no external side effects):** `/tmp/opencode/greedy_frontier.py`, `post_body.txt`, `post_result.json`, `greedy_n7.txt` exist. `greedy_n7.txt` is empty and no `greedy_frontier.py` computation process is running (the earlier `n=7` run was interrupted/killed before producing output); this is non-essential, as the theorem does not depend on `n=7`.
- **No other external side effects** observed (no PRs, no purchases, no ledger/main mutations).

**Conclusion:** the interrupted turn's effects are accounted for and nothing is uncertain. No unfinished work remains for this front beyond what was already completed and reported.

**Result already established (for continuity):** for the greedy (maximum-linear-extension) adversary, `|R_{G(n)}(n)| ≥ 2^{⌊n/2⌋} = exp(Ω(n))` for all `n ≥ 2` (matching-gadget/automorphism tie argument, with `G(n) ≥ ⌈log₂ n!⌉`), refuting a uniform polynomial bound. This is an enumeration obstruction only — not a time lower bound, not a proof that `G(n)=S(n)` for all `n` (observed for `n≤6`), and no separation for `SORT-BOUND-U`. Verified by exhaustive greedy-DAG BFS for `n≤6` (`|R_{G(n)}|=2,11,143,3362,119118`) and direct gadget checks for `n=4,6,8` in scratch. Web literature search was unavailable that pass, so grounding is limited to repo notes. No further action taken.

## Other metadata

```json
{
  "finished_at": 1795148841.7754827,
  "started_at": 1795148415.4754658
}
```
