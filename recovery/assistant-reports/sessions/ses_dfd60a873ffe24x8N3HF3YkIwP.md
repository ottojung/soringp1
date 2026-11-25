# antonina-sr5mDcMS8YMkcpyacKpBgh-tillage

Session: ses_dfd60a873ffe24x8N3HF3YkIwP
Workspace: /home/lubko/soring-fronts/pair-frequency-balance-optimal-tree-alln
Created: 1795340326856; updated: 1795340620977

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_2029f59b800153Vu3fz6ALK3p9)

I'll start by exploring the repository structure and understanding the "billy-dev" context, then read the required documents.

## Output 17 (msg_2029f6fd6001BedTSH4bYKz8pu)

I'm on the `billy-dev` branch. Let me read the required documents and locate board #301.

## Output 32 (msg_2029f79b2001f36R04c6N0uDLZ)

Now let me read the operations and literature docs, and find how to access board #301.

## Output 47 (msg_2029f956a001ppwBge617i0Ju5)

Let me access board #301 using the digest script, with attention to the referenced posts.

## Output 58 (msg_2029fc1d3001yXzfozpQe23LHc)

Let me read the full content of the two key referenced board posts.

## Output 96 (msg_202a01e220011xjWdTzIpS7Iri)

Let me do a recovery audit: check for prior work on this front, ledger status, and scratch files.

## Output 111 (msg_202a1c385001zjitMM1nhbKkNl)

Recovery audit is clean: front `pair-frequency-balance-optimal-tree-alln` is `running` with no prior board post or scratch. Now let me verify the mathematics with a small exhaustive experiment and careful reasoning.

## Output 145 (msg_202a22016001MoGbqbl4y7j9v2)

Let me do a brief literature check on pair-comparison frequency in sorting decision trees.

## Output 165 (msg_202a24bf7001KIFij5YrOR4dfl)

The exhaustive check confirms the key structural fact. Let me check how to post to the board, then compose the finding.

## Output 183 (msg_202a2a9b3001dtEw2pdF6MPrya)

I have a decisive finding. Let me compose the board report carefully.

## Output 201 (msg_202a3724d001g680ZrlmyoKXZc)

The post was submitted. Let me verify it appears on the board.

## Output 212 (msg_202a3812d001F65zDTWOH9LslO)

## Finding

The front's dichotomy resolves **degenerate**, not in the sense either horn intended. Posted as the single #301 comment (2026-11-22T09:43Z); worktree on `billy-dev` remains clean at `6a96398`, no Lean/repo/ledger changes.

**Exact determination (deduction, paper proof).** For any correct tree `T` with `L` leaves and any pair `p`, `phi_T(p) ≤ L` (a leaf is counted once), while the pair compared at the **root** lies on every path, so `phi_T(p_root) = L`. Hence `max_p phi_T(p) = L` for *every* correct tree. The minimum leaf count among height-`S(n)` trees is exactly `n!` (prune unreachable leaves and shortcut repeated-pair comparisons; the minimal subtree spanning all `n!` permutation-paths has height ≤ `S(n)`, hence = `S(n)`). Therefore

$$\Psi(n)=n!\quad\text{for all }n\ge 2,\qquad \frac{\Psi(n)}{n!\log n/n}=\frac{n}{\log n}\to\infty .$$

So the "balanced" horn `Ψ(n)=Θ(n! log n/n)` is **false**, and the "unbounded growth" horn is true only because the root pair sits on 100% of paths — not because of a hard deep state.

**Why the stated bounds missed this.** Both the adjacency bound `2(n−1)!` and the exact averaging bound `n!·log₂(n!)/C(n,2) ≈ 2n! log₂n/n` are ≤ `n!` (equality only at n=2); the root beats them by ~`n/(2 log n)`. The averaging *mass* is correct, but the max is set by one node with `L(v)=n!`, not the mean over pairs. Contrast the per-key-load front: its budget `~2 log n ≫ 1`, so the root's contribution is negligible; the per-pair budget `~2 log n/n = o(1)`, so the root's normalized mass `1` dominates. That is the exact reason the analogue degenerates.

**Non-root strengthening (still elementary).** At depth `d` some subtree has `≥ n!/2^d` leaves; with `d ≈ log₂n − log₂log n − log₂log log n` (well below `S(n)`) and a no-repeat optimal tree, that pair is non-root with `phi ≥ n!·Ω(log n·log log n/n) = ω(n! log n/n)`. So even excluding the root, the max is super-mean — but this is counting, not a structural theorem.

**Independent check (experiment).** Exhaustive minimax over reachable poset states enumerated all optimal trees for n=2,3,4 (1, 12, 60 trees); in every one `max phi = root phi = n!` (2, 6, 24).

## Honest limits

- This is an elementary observation, **not** a new theorem about `S(n)` or `SORT-BOUND-U`. It changes no complexity placement, gives no near-uniform comparison distribution, and affects no certificate route. Certificate **soundness ≠ completeness** still stands (framed DAGs range over pairs *at different states*); general-poset hardness does not transfer — the proof uses only the root and leaf counting.
- **Corrected open question (unsettled):** the full distribution of `W(p)=phi(p)/n!` over non-root pairs — can an optimal tree hold the second-largest `W` near the mean, or must many pairs carry `W ≫ log n/n`? I proved only one pair is forced above the mean and claim nothing more.
- Literature: websearch was repeatedly cancelled here; the `docs/literature.md` primary sources (Peczarski, Stober–Weiß, Ford–Johnson, Knuth, Filmus) do not study pair frequency, so I claim no precedent either way.

## Output 224 (msg_202a3a798001OSO5KqmhbB9U1x)

No duplicate action taken.

**Audit of actual state:**
- **Git/repo**: `/home/lubko/soring-fronts/pair-frequency-balance-optimal-tree-alln` is clean at `6a96398` on `billy-dev`; no commits, Lean, tests, or repo-file changes.
- **Board #301**: the post `SoringP1 frontier: pair-frequency-balance-optimal-tree-alln` (2026-11-22T09:43:06.114Z) is present on page 1. I confirmed it via `board_digest.py --contains "pair-frequency-balance-optimal-tree-alln"`; I did **not** repost.
- **Ledger**: `~/.local/state/soringp1/frontier-ledger.json` still shows the front as `running` (no `finding_unverified` written by me); I left it unchanged, as this run should not mutate ledger state beyond the keeper's contract.
- **Scratch**: only `/tmp/opencode/pairfreq_check.py` and `/tmp/opencode/pairfreq_post.txt` were created; no other external side effects.

**Completed work (mathematical finding):** `Ψ(n)=n!` for all `n>=2` by a root/leaf-count argument (`phi_T(p) ≤ L(T)`, root pair has `phi=L(T)`, min leaves among height-`S(n)` trees is `n!`). This falsifies the balanced horn and makes the unbounded-growth horn degenerate. A non-root strengthening gives one non-root pair with `phi = ω(n! log n/n)`. Exhaustive n≤4 optimal-tree check agrees. No new `S(n)`/`SORT-BOUND-U` theorem; the non-degenerate open question is the second-largest / distribution of `W(p)=phi(p)/n!`. Full details are in the existing #301 post.
