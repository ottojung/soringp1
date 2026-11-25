# antonina-woqZenqy18eAdNIXAeXM4K-losing

Session: ses_e025a5e20ffeZVSPF6Xf9dLZN3
Workspace: /home/lubko/soring-fronts/defect-maximizer-chain-uniqueness-alln
Created: 1795256853075; updated: 1795257608350

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 13 (msg_1fdad10d9001RKot3v4WazEA7a)

I'll start by inspecting the current state carefully, since a previous turn may have left side effects. Let me gather information in parallel.

## Output 28 (msg_1fdad1f5c001soYnfaMp42YgQ1)

The working tree is clean. Let me read the operational docs and search for board #301 and any durable task records.

## Output 47 (msg_1fdad3113001NGnQcj2fIlxilM)

Working tree is clean and on `billy-dev`. Let me check the durable ledger and the board digest (read-only) to see what may have already happened.

## Output 62 (msg_1fdad5a08001jzN92hYmyiB2H7)

The board shows the 10:20Z chain-extremality result and Viche's 10:28Z verification. My front is a *new* uniqueness question. Let me check whether a previous turn already posted about this specific front, and inspect scratch state.

## Output 77 (msg_1fdadba1c001IZoc0OWGtmmS3j)

No board post exists for this front yet — so no duplicate post risk. Let me inspect the ledger entry and recent scratch files to see what the interrupted turn actually did.

## Output 105 (msg_1fdadfcef001inV3uv4y8w95ZK)

No scratch files exist for the current front; the ledger shows it "running" since ~10:27Z. So no prior side effects from my front. Let me read the full 10:20Z result post and the verification to understand exact definitions.

## Output 120 (msg_1fdae38bd001RuDLZvtLzt59Um)

I now understand the setup. I have a candidate rigorous infinite family. Before committing, let me check literature and prior board posts to avoid duplicating an existing finding, and read Viche's verification in full.

## Output 135 (msg_1fdaf61ff001Ft9nc6GQMTkCcj)

Literature checked; no prior board post addresses maximizer uniqueness. Now let me verify my candidate infinite family with a fresh, independent exact-minimax computation (scratch only, no repo changes).

## Output 153 (msg_1fdafab77001btCpo8BJRoNlzu)

The independent exact minimax confirms the family ties the chain for every tested b (3–8) and reproduces the cited (1,4) example. Now let me determine the board-posting mechanism so I can report the falsification once (no prior post exists).

## Output 186 (msg_1fdaff283001cNLQ6L4mOwLk5W)

I have a rigorous result: a general sufficient condition for equality in the chain-extremality law at `a=1`, plus an explicit infinite family. It also explains the previously observed `(1,4)` tie. Let me write the board report (one post only) and verify no duplicate exists immediately before posting.

## Output 215 (msg_1fdb09a88001yn1mpqwKlmFjuF)

Post succeeded. Let me verify it appears exactly once.

## Output 235 (msg_1fdb108fe001d4fMZajgjOV7bc)

## Result: uniqueness is refuted — an infinite family of non-chain maximizers at `a = 1`

**Recovery audit.** No side effects from the interrupted turn: worktree clean at `6a96398` on `billy-dev`, no scratch files for this front, and board #301 pages 1–5 had **0** posts with my author tag. I made exactly **one** board comment (verified: 1 hit, `2026-11-21T10:39:18Z`). No repo, Lean, test, CI, ledger, or main changes.

### The theorem (paper proof)

Let `F(P)` be the exact adaptive minimax cost of identifying the unknown linear extension, `delta(A_a,B) = F(B ⊔ A_a) − F(B) − S(a)`, and "information-tight" mean `F(P) = ⌈log₂ e(P)⌉`.

**T0 (sufficient condition, `a = 1`).** If a `b`-element host `B` is information-tight with `e(B) = 2^k`, then `delta(A_1,B) = delta(A_1,C_b) = ⌈log₂(b+1)⌉`.

*Proof:* `F(B) = k`. From the 10:20Z composition bound, `F(B ⊔ A_1) ≤ F(B) + F(C_b ⊔ A_1) = k + ⌈log₂(b+1)⌉` (binary insertion is optimal for `C_b ⊔ A_1`). The information bound gives `F(B ⊔ A_1) ≥ ⌈log₂(2^k(b+1))⌉ = k + ⌈log₂(b+1)⌉`. Both bounds coincide, so `delta = ⌈log₂(b+1)⌉`. ∎

**Corollary (infinite family).** For every `b ≥ 3`, let `Vcap_b = {x<y, x<z, y,z < t₁ < … < t_{b−3}}` (the 3-element `V` when `b=3`). It is non-chain, `e = 2`, `F = 1`, so T0 applies. These are pairwise non-isomorphic, information-tight, non-chain maximizers for **all** `b ≥ 3`: `C_b` is not the unique isomorphism-type maximizer, and there are infinitely many `b` with non-chain maximizers.

T0 also *explains* the previously observed `(1,4)` tie: `V`-plus-isolated has `e = 8 = 2³`, `F = 3`, hence `delta = 3 + ⌈log₂5⌉ − 3 = 3 = delta(A_1,C_4)`.

**Independent check (experiment).** A fresh from-scratch minimax over sets of surviving linear extensions (no project code) reproduced `S(1..5) = 0,1,3,5,7` and `delta(Vcap_b,A_1) = 2,3,3,3,3,3,4` for `b = 3..8`, each equal to `⌈log₂(b+1)⌉`; it also reproduced `F(V+isolated)=3, F(+A₁)=6, delta=3`.

### Honest limits

- **What fails is uniqueness only.** Chain *extremality* (T1, 10:20Z) is untouched: the family attains the maximum and never exceeds it; the "strictly above" falsifier remains impossible by T1's proof.
- **T0 is sufficient, not necessary** — I do not claim a full equality classification.
- **No extension to `a > 1`**: power-of-two `e(B)` makes ceilings additive only for `a=1`; for `a>1`, `F(C_b ⊔ A_a)` can exceed `⌈log₂ C(a+b,a)⌉`, which is the exact obstruction to the same argument.
- **No complexity consequence.** This is structural (sharpening the equality cases of the disjoint-union defect envelope). It separates no class; `S(n)` and `SORT-BOUND-U` remain open. No Lean or repository changes were made.

Board report: Antonina #301, `10:39:18Z`, author `SoringP1 researcher: defect-maximizer-chain-uniqueness-alln` (posted once).
