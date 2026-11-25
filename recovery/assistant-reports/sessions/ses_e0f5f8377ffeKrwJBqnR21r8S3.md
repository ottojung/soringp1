# antonina-E5eOMlNvrqA8RX0YsfWUsW-dragging

Session: ses_e0f5f8377ffeKrwJBqnR21r8S3
Workspace: /home/lubko/soring-fronts/cpsat-fr-n12-exact
Created: 1795038411994; updated: 1795042288148

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f0a07ec0001MQR2x2wh8QwZpq)

I'll start with the recovery/side-effect audit as required, before any external side effect. Let me run independent checks in parallel.

## Output 29 (msg_1f0a08bde0014nHckorcaOllky)

Worktree is clean at the required HEAD. Now let me read the research plan and scan #301 (all pages) for prior posts by my exact author string.

## Output 44 (msg_1f0a09a12001XLsJS2UXSm4Lfk)

Page 1 has exactly 50 messages — I must check page 2. Let me also read the directly-related prior posts (n=12 CP-SAT, budget-tight-nontransitivity, kply barrier) to avoid duplicating and to understand the exact context.

## Output 59 (msg_1f0a0ae0200156irznx5Fk0d2s)

Let me check page 3 (if it exists) and scan all pages for my exact author, while reading the most relevant prior n=12 posts.

## Output 74 (msg_1f0a0cad9001N7xcAJadiPgfYC)

I've confirmed my exact author string does not appear on pages 1–4. Let me finish the full duplicate scan across all remaining pages and check the available solver/tooling environment in parallel.

## Output 89 (msg_1f0a220a3001HFpvcoRyG8EUwZ)

Full duplicate scan done: 2860 messages across 58 pages, **0 posts** by my exact author — no duplicate. No SAT/CP solvers are preinstalled. Let me check whether I can install one, and set up my scratch directory.

## Output 109 (msg_1f0a283f6001BQA30XkCwqn2aZ)

python-sat installed into scratch. Let me also try ortools (CP-SAT), then design the encoding.

## Output 120 (msg_1f0a2c349001lfbc55xfot4x2e)

Both SAT backends are available. For the exact search I need fast canonicalization of posets under relabeling — let me try installing `pynauty` (nauty C library), which would make symmetry reduction practical.

## Output 131 (msg_1f0a3506600103pStpJ2FVuFrs)

pynauty is available. Let me build and test the core exact engine: poset representation, transitive closure, exact linear-extension counting, and nauty-based canonicalization, validating on small n first.

## Output 149 (msg_1f0a3951d001tclsPXwlwHtw7H)

Core verified: e(R)=119750400=12!/4 and ceil(log2 e(R))=27 exactly. Now let me implement the exact minimax / feasibility engine with canonicalization and validate on n=5,6,7.

## Output 167 (msg_1f0a3c302001LxL8RfhOdk7z8m)

Engine validates perfectly on n=5,6,7. Now let me implement the materially-distinct method: **proof-number search (PNS)** with nauty canonicalization, transposition table, and information pruning — a best-first AND/OR proof search rather than the stalled depth-first / frontier methods.

## Output 219 (msg_1f0a6605f0014YGCdqqRpQtsaG)

Found the PNS bug: selection must skip already-solved children. Let me fix the descent.

## Output 237 (msg_1f0a69998001ovlPF1L30jANHM)

PNS validates on all small n for both horns. Now let me set up the **root-case reduction** at n=12 (soundly reducing F(R)=27? to a few candidate-child feasibility questions) and probe PNS performance on each candidate child.

## Output 255 (msg_1f0a8a5c7001dnPMHgk1RMT9qZ)

Output buffering hid progress. Let me add flushing and rerun with a longer timeout.

## Output 266 (msg_1f0aa9c0e001gP3J9ozzkS10oz)

Excellent — the reduction is clean: at root R only the **two-free comparison** can possibly achieve 27 (all other comparison orbits have a child with e>2²⁶, forcing F≥27). So **F(R)=27 ⟺ F(Q)=26**, where Q=R+(2<3), e(Q)=12!/8. Let me add progress reporting to PNS and attack this single decisive question.

## Output 307 (msg_1f0acfa1e001fsITfkqJcdNkpP)

Let me measure PNS throughput on n=12 with a short timed run (the earlier runs were cut off by the tool's 120s default, not by my budget).

## Output 318 (msg_1f0aebf66001k8mpgCEzpM2yVn)

PNS is correct but too slow in Python (~74 nodes/s). Let me test whether a cheap WL-based canonical key is isomorphism-invariant for these states — that would let me port to Go for a ~100× speedup.

## Output 329 (msg_1f0af59dc001y4UM6vI6wVm3Wf)

The WL-canonical matrix is a **sound** TT key (equal matrices ⟹ isomorphic states; worst case is only missed sharing). Let me port the whole search to Go for a large speedup, implementing PNS with WL-canonical transposition tables and exact subset-DP extension counts.

## Output 340 (msg_1f0afbdc0001fpmdjzUNJ7bIiY)

The Go PNS had a state-tracking bug (children states weren't registered). Let me store the state directly in each OR node — much simpler and correct.

## Output 365 (msg_1f0b01d030011Yz4EKTqb5cGOV)

Now let me rewrite `solve` to use each node's stored state:

## Output 381 (msg_1f0b0484f001tVGeYSpZBQYG4E)

Let me parameterize `n` in the Go program so I can validate it on n=5,6,7 before the n=12 run.

## Output 422 (msg_1f0b0f929001ee0EhDskAWzClI)

Go PNS validates on n=5,6,7. Let me measure throughput on the n=12 target.

## Output 433 (msg_1f0b26e99001ijMyFtOrLOht3Y)

Throughput is ~620 nodes/s — the WL canonicalization is the bottleneck. Let me cache canonical keys by exact state (child states recur heavily) and optimize.

## Output 451 (msg_1f0b40878001FJkHnNrxrTbfFc)

Let me add a stronger one-ply information prune: if every comparison has a child exceeding the remaining per-child budget, the node is immediately refuted. This should cut the search substantially.

## Output 469 (msg_1f0b5c944001VD2sfAqNYtImCu)

Let me check whether the one-ply information bound alone decides Q — i.e., whether every comparison at Q has a child exceeding 2²⁵. That would give a short, fully checkable proof of F(Q)=27.

## Output 480 (msg_1f0b6065c0016o7z2RqwoizEyB)

Q survives the one-ply bound (two balanced comparisons exist). Let me explore the **info-tight two-sided frontier** from Q — tracking all children of balanced comparisons with canonical dedup. If a level empties, F(Q)=27 (hence F(R)=28) with a short refutation; if it reaches depth 26, we get a witness strategy.

## Output 514 (msg_1f0b814d5001IzCJ0XExVzMkvN)

The frontier explodes. Let me optimize the Go PNS's dominant cost — compute each child's extension count via e(child₁)+e(child₂)=e(parent), halving the DP work — and tune GC.

## Output 573 (msg_1f0ba1c3f001GwXstKvol7iKKe)

e-counting dominates. Since e is isomorphism-invariant, let me key the e-cache by canonical form (not exact labels) — that should collapse hundreds of thousands of redundant counts.

## Output 614 (msg_1f0bbf7380019RnXI5mr0XEYDd)

Let me commit to a substantial PNS run (15 minutes) on the decisive Q-at-b=26 question, logging progress.

## Output 756 (msg_1f0db8aa1001DDvbkBGGdKKF4M)

Task complete. One durable deliverable was posted to Antonina #301.

What happened:

- Confirmed worktree `/home/lubko/soring-fronts/cpsat-fr-n12-exact` clean at `6a96398d937d20977a91b9afa8619cb27feab269`.
- Scanned `#301` twice; exact author `SoringP1 frontier: cpsat-fr-n12-exact` had **0 prior posts** before posting.
- Used proof-number AND/OR proof search, materially distinct from the stalled minimax/transcript DFS and one-sided admissible-frontier method.
- Validated the engine on n=5,6,7: reproduced `F(R)=5,8,11`, `F(P1)=4,7,10`.
- Verified exactly:
  - `e(R)=119750400=12!/4`
  - `ceil(log2 e(R))=27`
- Derived a sound n=12 root reduction:
  - `F(R)=27 iff Q is sortable within 26 comparisons`
  - otherwise `F(R)=28`
  - where `Q=R+(2<3)`, `e(Q)=59875200`.
- Result remains **INCONCLUSIVE**: about 19.75 minutes instrumented PNS across fresh attempts did not decide `can_sort(Q,26)`; no UNSAT refutation or verified height-27 witness exists.
- Posted one report as exact author `SoringP1 frontier: cpsat-fr-n12-exact`.
- Post-post audit: **exactly 1** post by that author, message id `sha256:CEWN7uXWSGn9jf2AxqJlSsdFlX5gB-Bp7v84V5sfWtU`, created `2026-11-18T22:50:28.644Z`; worktree still clean.

Limits stated in the post: this is a poset-minimax fact, not a complexity lower bound for `S(n)` or `SORT-BOUND-U`; no P/NP/PSPACE claim; no theorem completion claimed.
