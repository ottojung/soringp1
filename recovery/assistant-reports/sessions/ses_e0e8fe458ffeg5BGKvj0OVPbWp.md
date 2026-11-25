# antonina-B43yjph5VAY4l4Dv0YTFZL-scoundrel

Session: ses_e0e8fe458ffeg5BGKvj0OVPbWp
Workspace: /home/lubko/soring-fronts/compositional-antichain-strict-excess
Created: 1795052018646; updated: 1795052860251

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 546 (msg_1f17ca02b001d52F31kByDBnvT)

## Report — `compositional-antichain-strict-excess` (billy-dev, 2026-11-19)

### Recovery / side-effect audit
Before acting I checked the conversation, worktree, Git state, ledger and board. My session had performed **only read-only operations**; the worktree stayed clean at `6a96398`, the ledger showed this front owned by agent `B43yjph5VAY4l4Dv0YTFZL-scoundrel` (state=running, alive, one prompt), and a scan of #301 pages 1–60 found **zero** prior posts by this front's exact author. I therefore made exactly **one** board post (01:46:54Z, JSON redirect to `/tmp/opencode/comp_antichain/post_result.json`) and re-verified the worktree clean. No Lean, repo, test, workflow or ledger changes; no duplicated effects.

### Mathematical finding (deduction + reproducible small computation)

**Claim attacked:** a sound invariant `C(P) ≤ I(P) ≤ F(P)` built from ordinal-sum/module composition, with `I(A_n) > C(n)` for infinitely many information-loose n, certifying an all-n root excess past `S(12)=30>29`.

**Root-vacuity lemma.** The antichain `A_n` is series-prime (complete incomparability graph), verified for n=2–7. Hence for any base score `g`, the ordinal-sum composition `I_g(P)=Σ g(P_i)` gives `I_g(A_n)=g(A_n)`: **composition cannot create root strictness**. Module composition is equally vacuous at `A_n`: all `2^n−2` proper subsets are modules but every reversal is the identity (n=3–6); the non-vacuous prime-quotient reversals are not `F`-sound (n=7 counterexamples).

**Reference-script checks:** `L0 = L1 = I_round = C(n)` at `A_n` (n=2–7); t-ply lookahead `L_t(A_n)=C(n)` for all `t ≤ n/2` (n≤8). Strictness appears only off-root: a decomposable state has `e=15, C=4, I_round=5, F=5`, and `W⊕C_t` has `C=I_round=3 < L1=F=4`.

**Verdict.** The FRONT's mechanism is refuted: none of the known sound computable base scores (information, one-ply/t-ply, rounding, certified merge gap, B1's scalar statistics) is root-strict, so ordinal-sum/module composition cannot certify an excess beyond n=12. The FALSIFIER's **literal universal wording is unprovable**: `F` itself is sound and ordinal-sum-additive, hence strict at `A_n` exactly at loose n. The defensible no-go is mechanism-specific, and a universal theorem would require first defining the class of "compositional invariants" — the front does not.

### Honest limits
This does **not** settle whether `S(n)>C(n)` infinitely often; it only closes the compositional route. All computations are n≤8; the n=12 excess is taken from the primary literature (Stober–Weiss ALENEX 2023; Peczarski/Wells), not reproduced. Even an all-n root-strict invariant would only sharpen the numerical lower bound on `S(n)`/threshold window — no NP/coNP certificate, no separation, no faster evaluator. Soundness of a checker is not completeness of its witness class.
