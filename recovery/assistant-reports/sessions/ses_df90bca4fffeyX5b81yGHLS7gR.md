# antonina-cUGB2DgLiOB6h9tbCROulV-breaks

Session: ses_df90bca4fffeyX5b81yGHLS7gR
Workspace: /home/lubko/soring-fronts/admissible-heuristic-dominating-info-alln-20261123b
Created: 1795412997618; updated: 1795413293059

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_206f4386e001RpKUBYSovl56vg)

I'll orient myself first by reading the required files and checking current state. Let me run these in parallel.

## Output 29 (msg_206f44f8d001A6iesCB0LNnYJc)

Let me check the ledger and read the most closely-related existing comments and docs.

## Output 48 (msg_206f46408001NhxtjHoIebeId8)

The ledger has many related fronts but not my exact slug. Let me examine the detailed ledger entries for the most relevant prior investigations and read the rest of the nontightness note.

## Output 59 (msg_206f4dc68001lBKFgV0IGHpqZs)

This is a well-studied area. Let me examine the actual evaluator and key docs, plus check a few more relevant ledger entries, to ground my analysis precisely.

## Output 74 (msg_206f569820015zNs28nL1s251J)

Let me look at the exact evaluator to ground my computation, then I'll test a concrete infinite-family construction in scratch.

## Output 85 (msg_206f64fdb001jss1YxdLPyP3Gt)

The key insight is emerging. Let me verify a concrete infinite-family construction with an independent exact computation in scratch (`/tmp/opencode` only).

## Output 103 (msg_206f6edef001sryGrwXiX9p7UE)

Confirmed: `e(W_n) = Fib(n+1)`, `F(W_n) = n-1`, and the defect `F-L` is positive from `n=5` on. Let me verify a clean all-`n` inequality and scan the board for any prior post under my slug before writing up.

## Output 123 (msg_206f7cc12001i2SPcS0DsPVZXM)

All checks pass. Now I'll write the result file and post exactly one comment.

## Output 141 (msg_206f87ca2001tPezg9DRGeTrSq)

The comment posted (visible at `2026-11-23T05:54:26.583Z`). Let me verify it appears on page 1 by re-reading.

## Output 152 (msg_206f89f7e001x5naKa97EI66Bi)

Done. The single deliverable is posted and verified on Antonina board issue #301.

## Summary

**Verdict: (a) claim established.**

**Question:** Does a polynomial-time computable admissible heuristic `h(P) ≤ F(P)` exist that strictly dominates the information bound `L(P)=⌈log₂ e(P)⌉` on infinitely many antichain-reachable states?

**Result:** Yes — with an elementary all-`n` proof, using the staircase/fence poset family `Wₙ` (`i<j` iff `j≥i+2`):

- **Construction:** `h(P)=n−1` if `P` is `Wₙ` (or a relabel-isomorphic copy), else `0`. Recognition is `O(n²)`; `h` never computes `e(P)`, so it respects the `#P`-hardness of counting linear extensions.
- **Admissibility [paper proof]:** The only incomparable pairs in `Wₙ` are the `n−1` consecutive pairs; each comparison resolves at most one, so `F(Wₙ)=n−1=h(Wₙ)`; off-family `h=0≤F`.
- **Domination [paper proof + verified computation]:** `e(Wₙ)=Fib(n+1)`, and `Fib(n+1)≤2^(n−2)` for `n≥5`, so `L(Wₙ)≤n−2 < n−1=h(Wₙ)` — an infinite family. Independent scratch computation confirmed `e=1,2,3,5,8,13,21,34` and `F=0,…,7` for `n=1..8` (defect `F−L=1` from `n=5`). The states are reachable, even on optimal play for `n≥6`.

**Honest limits stated in the post:** this is a family-specific lookup (`h=0` elsewhere), so it is *not* a useful general prune and gives no exponent gain for `SORT-BOUND-U`; it does not establish a uniform/natural scalar rule dominating `L`, nor `h(Aₙ)>C(n)` at the root (that needs the open `S(n)>C(n)` infinitely-often question). No theorem completion; no repo/Lean/test/CI/ledger/main change.

**Next decisive obstacle:** a *uniform* poly-time lower bound dominating `L` on all positive-defect states — blocked by the `#P`-hard threshold `e(child)>2^(L−1)` and the root's open tightness question.

Verification: exactly one comment under the required author on page 1, correct first line and full body. No repository files were modified (scratch only under `/tmp/opencode`).
