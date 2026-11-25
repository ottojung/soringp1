# antonina-xUXMudZRwNefHp5KNUZs49-portfolio

Session: ses_e08d0fcbdffeOcOZgCmxzotGIR
Workspace: /home/lubko/soring-fronts/greedy-frontier-state-growth-alln
Created: 1795148415836; updated: 1795148814798

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f72f07b0001WP35dikwTYj654)

I'll start by orienting myself: checking the git state/branch and reading the required documents.

## Output 21 (msg_1f72f116f00183JIcp0aXhWSRK)

I'm on `billy-dev`. Let me locate the research board and the referenced research docs.

## Output 36 (msg_1f72f1b3b001jIBuwvfXw1qIFn)

Let me read the operations guide and query the board digest (redirecting output to a file as instructed).

## Output 58 (msg_1f72f3524001Nn7Tdc5Knzt1mu)

Let me read the two key research docs and check for prior work in this worktree.

## Output 73 (msg_1f72f46bb00129fasvqeSkpEOm)

Let me look for prior work in this worktree (scripts, notes, beam searches) and check the git log.

## Output 88 (msg_1f72f5c9d001qq4qDCiFbxom5p)

Let me check the frontier ledger for this specific front and look for beam-search code.

## Output 112 (msg_1f72f7e1c001o8gcCC5EPrhWUM)

This is a well-studied front. Let me pull the relevant earlier board entries to understand the established definitions and counts before I design my own attack.

## Output 134 (msg_1f7309b4b00144DEyIRCh4AcFZ)

Let me search across all board pages for the relevant terms.

## Output 152 (msg_1f731248b001E015HphXz67Eax)

The digest truncates. Let me see the board script and find a way to read the full message.

## Output 179 (msg_1f73150040017Q3FYpXYUWE7q0)

I now have the definitions I need. Let me look at the exact `minimax`/poset helpers I can reuse, then build a scratch experiment in `/tmp/opencode` (no repo changes).

## Output 190 (msg_1f73240b4001ODHljh8W5BHm0o)

Now let me write a scratch experiment (in `/tmp/opencode`, no repo changes) to compute the greedy-adversary game value `G(n)` and the reachable ball `|R_{G(n)}(n)|` for small `n`, and verify the matching gadget lower bound.

## Output 208 (msg_1f7329e59001dwmC1TicUJbCbi)

Small-n results confirm superpolynomial growth and `G(n)=S(n)` for n≤6. Let me verify the matching-gadget lower bound directly and try n=7 in the background.

## Output 228 (msg_1f732d084001m6q6rLcWmHWpgd)

The gadget is verified and the theorem is airtight. Let me confirm there's no existing board post by this front and find the posting mechanism.

## Output 248 (msg_1f7338959001H8gFoidXTpYYpQ)

Let me study the primary-literature summary to ground the max-LE adversary and check for any known result on this exact reachable-set question.

## Output 281 (msg_1f733fbd80016o2YkYoR7SnpBr)

The theorem is proved and verified. Let me post the finding to board #301 exactly once (redirecting JSON output to a file as required), then verify.

## Output 292 (msg_1f7344a140017g2FHM2EW5u2RG)

Let me verify the post landed exactly once.

## Output 303 (msg_1f73463f1001HtkCdeaPfqwhxN)

Let me confirm the worktree is clean and check whether the n=7 background computation finished.

## Output 329 (msg_1f7348822001dp84akUAN13y0R)

Done. Here is the honest outcome.

## Setting verified
Branch `billy-dev`, worktree clean at `6a96398` throughout; no Lean, repo, test, ledger, or `main` changes. I read `AGENTS.md`, `docs/problem.md`, board #301, the two cited notes (`research-winning-frontier-barrier.md`, `research-compression-next.md`), and the ledger's other greedy/adversary fronts to avoid repeating claims. No prior post existed for this front; my finding is now posted exactly once to #301.

## Mathematical finding — the polynomial-bound hypothesis is FALSE (all‑n disproof)

**Definitions.** Greedy adversary = at a comparison of incomparable `x,y`, answer with the orientation whose resulting poset has *more* linear extensions (deterministic tie‑break). `G(n)` = sorting‑game value against it; `R_k(n)` = posets reachable from the antichain in ≤ k greedy comparisons.

**Theorem [paper proof].** For every `n ≥ 2`,
$$\lvert R_{G(n)}(n)\rvert \;\ge\; 2^{\lfloor n/2\rfloor}=\exp(\Omega(n)).$$

*Proof, two steps.*

1. **`G(n) ≥ ⌈log₂ n!⌉ ≥ ⌊n/2⌋`.** With `e(P)` = # linear extensions, comparing `x,y` splits extensions into `a + b = e(P)`; the greedy adversary returns the larger child, so `e(next) ≥ e(P)/2`. From `e(Aₙ)=n!`, after `t` comparisons `e ≥ n!/2ᵗ`; a total order has `e=1`, forcing `t ≥ log₂ n!`.
2. **Matching gadget.** For `n=2m`, pair elements `{2k,2k+1}`. For each subset `T ⊆ [m]`, the sorter compares exactly the pairs in `T`. When pair `k` is compared, `{2k,2k+1}` is an isolated 2‑antichain component (no cross‑pair comparisons are ever made), so the transposition `2k↔2k+1` is an automorphism — hence the two children have *equal* `e` (a greedy tie) and the pair is resolved into a 2‑chain under any fixed tie‑break. Distinct `T` give distinct posets `P_T`, each at depth `|T| ≤ m ≤ G(n)`. So the `2^m` states `{P_T}` all lie in `R_{G(n)}(n)`. Tie‑break‑robust; odd `n` use `2m` plus an isolated element.

## Verification [experiment, scratch only]
Exhaustive greedy‑DAG BFS (`/tmp/opencode/greedy_frontier.py`): `G(2..6)=1,3,5,7,10` (so `G(n)=S(n)` on this range) and `|R_{G(n)}| = 2, 11, 143, 3362, 119118`. Direct check: the `2^{n/2}` gadget states for `n=4,6,8` are distinct, reachable, and every resolution is a verified extension‑count tie.

## Complexity implication [deduction]
The polynomial alternative is refuted, so the proposed route — evaluating `G(n)` (and `S(n)` if `G(n)=S(n)`) by explicitly enumerating the greedy‑frontier ball in polynomial time — is blocked: that ball is already exponential.

## Distinctions and honest limits
- This is an **enumeration/counting obstruction, not a time lower bound** — a selective or symbolic search need not list all states (same caveat as `research-winning-frontier-barrier.md`).
- It is a direct construction **at the antichain root**, not a general‑poset hardness result, and it says nothing about **certificate soundness vs. completeness** for any certificate system.
- It does **not** settle whether `G(n)=S(n)` for all `n` (open; true for `n≤6`), and yields no class separation for `SORT-BOUND-U`.
- **Lower bound only**; true growth may be larger (small‑`n` data ≈ `2^{2.8n}` at `n=6`). The proof uses only equality of two extension counts via an automorphism, so the general `#P`‑hardness of computing `e(P)` is irrelevant.
- Web literature search was unavailable this pass, so literature grounding is limited to the repo's baseline notes; the max‑LE adversary is the standard adversary behind the halving/information bound, and I found no prior treatment of this specific reachable‑set question there.

I did not manufacture a stronger claim than I can defend: the concrete result is the `exp(Ω(n))` lower bound, and the polynomial bound is disproved.

## Output 358 (msg_1f734e2e6001edhcU7HZfkqkTv)

Recovery inspection (no actions repeated):

- **Git / repo state:** `billy-dev` at `6a96398`, worktree clean (`git status` empty). No commits, no Lean files, no tests, and no `main`/CI changes were made.
- **Board (durable external effect):** exactly **one** post by this front is present on Antonina #301 (page 1, `2026-11-20T04:25:51.332Z`, author `SoringP1 frontier: greedy-frontier-state-growth-alln`), verified via `board_digest.py --contains "greedy-frontier-state-growth-alln"` on page 1 (1 match) and page 2 (0). `/tmp/opencode/post_result.json` records exit 0. I did not and will not post again.
- **Scratch/local artifacts (no external side effects):** `/tmp/opencode/greedy_frontier.py`, `post_body.txt`, `post_result.json`, `greedy_n7.txt` exist. `greedy_n7.txt` is empty and no `greedy_frontier.py` computation process is running (the earlier `n=7` run was interrupted/killed before producing output); this is non-essential, as the theorem does not depend on `n=7`.
- **No other external side effects** observed (no PRs, no purchases, no ledger/main mutations).

**Conclusion:** the interrupted turn's effects are accounted for and nothing is uncertain. No unfinished work remains for this front beyond what was already completed and reported.

**Result already established (for continuity):** for the greedy (maximum-linear-extension) adversary, `|R_{G(n)}(n)| ≥ 2^{⌊n/2⌋} = exp(Ω(n))` for all `n ≥ 2` (matching-gadget/automorphism tie argument, with `G(n) ≥ ⌈log₂ n!⌉`), refuting a uniform polynomial bound. This is an enumeration obstruction only — not a time lower bound, not a proof that `G(n)=S(n)` for all `n` (observed for `n≤6`), and no separation for `SORT-BOUND-U`. Verified by exhaustive greedy-DAG BFS for `n≤6` (`|R_{G(n)}|=2,11,143,3362,119118`) and direct gadget checks for `n=4,6,8` in scratch. Web literature search was unavailable that pass, so grounding is limited to repo notes. No further action taken.
