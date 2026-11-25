# antonina-RkiSdf6Bk7XvEbB4DmIf1O-never

Session: ses_e011c644bffecQ0FReEFQAs0zk
Workspace: /home/lubko/soring-fronts/exec-lit-sweep-20261121
Created: 1795277691901; updated: 1795278555456

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1fee39dd8001DjkMBL0dTMiC9u)

I'll start by understanding the project baseline and the operational details (including how to access the Antonina board).

## Output 25 (msg_1fee3af89001ORA13esoL6JeaM)

Now let me understand the board posting mechanism and verify the worktree state.

## Output 71 (msg_1fee3fcbb001V3OHLi4InsVfT2)

Now I'll begin the literature sweep. Let me run a batch of targeted web searches in parallel.

## Output 94 (msg_1fee41533001TCeSucl7nMNZlf)

Web search calls were cancelled in parallel. Let me try sequentially.

## Output 114 (msg_1fee4386d001v3ENyru2UQo6Mt)

Web search appears unavailable. Let me test whether direct web fetch works, using known URLs and arXiv search endpoints.

## Output 129 (msg_1fee44763001w6ZLAEHf0npNZN)

Web fetch works. Web search tool is down, so I'll record that and use fetch-based search engines and APIs. Let me try several search endpoints in parallel.

## Output 148 (msg_1fee46453001cix1ZAxyS6p4bZ)

DuckDuckGo HTML and arXiv search work; Bing is noisy. Let me query structured APIs and targeted searches in parallel.

## Output 252 (msg_1fee53648001lCYEoPuoFPriUc)

Let me read the two most relevant "new technique" papers in full: Cremer 2026 (selection lower-bound technique) and SEA 2025 (exhaustive-search ideas).

## Output 263 (msg_1fee54e190014Rj03FuFy07HjA)

Let me check the board's prior no-go on the potential route (to avoid proposing something already refuted), and read the SEA 2025 full text.

## Output 274 (msg_1fee5cd470018ubA4vwYLah7jF)

I have strong leads. Let me finish the inventory with author/publication checks and audit the remaining OEIS-cited 2024 paper.

## Output 319 (msg_1fee6f2c5001Yu9f7xpx4Pe3vc)

I've completed the sweep. Let me write the finding to a scratch note, then post it once to board #301.

## Output 348 (msg_1fee80e09001873hBRWmIgXI5G)

The board caps comments at 10,000 characters. Let me condense the finding while keeping all required evidence.

## Output 375 (msg_1fee88525001OupgeW75X545fZ)

The comment posted. Let me verify it appears correctly on board #301 and confirm the worktree is still clean.

## Output 390 (msg_1fee8a871001pACEgDaeXkE9Ug)

Done. I posted exactly one findings comment to Antonina board **#301** under the author tag `SoringP1 researcher: exec-lit-sweep-20261121` (verified at 16:20:07Z), and the worktree is clean at detached `6a96398`. No repo, Lean, CI, main, or ledger changes; no theorem-completion claim.

**Outcome: rigorous negative result.** No accessible primary source published 2023-01 → 2026-11 establishes a new exact S(n) for n≥23, a lower bound beyond S(28)≥99, a sharpened Sergeev excess, a new Ford-Johnson/certificate theorem for S(n), or any SORT-BOUND-U complexity result.

Key evidence recorded in the post:
- **Inventory:** OEIS A036604 (last modified 2026-11-21) still ends at a(22)=71, no a(23); arXiv API searches (`minimum number of comparisons`, `Ford-Johnson`, `sorting numbers`); author checks (Stober → only 2025 *selection* paper; Peczarski → only 2025 pancake sorting); negative Sergeev-asymptotic and complexity queries. The `websearch` tool was cancelled on all 8 attempts, so I used fetch-based DuckDuckGo/arXiv/Crossref/OEIS instead — no primary source was paywalled.
- **Model audits:** Dörrer et al. (LIPIcs SEA 2025) and Cremer (arXiv:2610.18740, Oct 2026) are about *selection* V_i(n), not sorting S(n); Haeupler et al. (arXiv:2404.04552) sorts a *given poset* asymptotically with O(log e(P)) comparisons — weaker than Sergeev and not uniform evaluation. None transfers.
- **Bridge question + falsification:** The best new technique (Cremer's two-sided weight Φ*, largest valid leaf-weight) was lifted to sorting as a candidate all-n question. I refuted it in both natural readings with paper proofs: (i) the analogue Ψ_sort(A_n)=3ⁿ−n! goes strongly negative by n=7; (ii) any correct sorting tree has exactly e(P) minimal leaves, so no leaf-count functional can exceed ⌈log₂ e(P)⌉; (iii) any sorting decision DAG needs ≥ n! distinct leaves, so no poly-size NP certificate exists in unary; (iv) known-small checks (Z₃, C₂⊔Z₃) falsify relative-excess monotonicity and a Hwang-Lin-style strengthening of D. The only surviving extremal-charging reading is circular with D per the board's earlier verified no-go.

Scratch note: `/tmp/opencode/exec-lit-sweep-20261121-finding.txt` (post response: `/tmp/opencode/antonina-post-result.json`). S(n), SORT-BOUND-U, and D remain open, and this front warrants no further enumeration or formalization.

## Output 426 (msg_1fef08d66001Tqj19WhkFMNngN)

**Recovery check complete — no duplicate action taken.**

Inspected the worktree, Git state, and board; the previous turn’s external side effect already happened.

- **Board #301**: exactly one matching finding exists — `[2026-11-21T16:20:07.247Z] SoringP1 researcher: exec-lit-sweep-20261121` (negative literature-sweep outcome). No duplicate post found.
- **Git**: `/home/lubko/soring-fronts/exec-lit-sweep-20261121` is clean, detached at `6a96398d937d20977a91b9afa8619cb27feab269`; no commits/branches/PRs/Lean/CI changes.
- **Scratch artifacts**: `/tmp/opencode/exec-lit-sweep-20261121-finding.txt` (7695 bytes) and `/tmp/opencode/antonina-post-result.json` present, consistent with that single post.

No unfinished external work remains from the interrupted prompt. S(n), SORT-BOUND-U, and D remain open; no theorem-completion claim.
