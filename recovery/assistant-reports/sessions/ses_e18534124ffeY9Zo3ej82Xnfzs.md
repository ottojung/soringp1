# antonina-7HL0p4yS2dF6jVcuAQHVmF-elemental

Session: ses_e18534124ffeY9Zo3ej82Xnfzs
Workspace: /home/lubko/soring301-exec-info-gap-invariant-20261117
Created: 1794888220385; updated: 1794888920912

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 223 (msg_1e7b7013f001ghaohDm5qc9wjg)

**Inspected existing state (no duplicated external actions taken):**
- Worktree: `/home/lubko/soring301-exec-info-gap-invariant-20261117` (HEAD `6a96398`, detached, `git status` clean except untracked state created by this run: `exec-report.md` and `/tmp/opencode/*` artifacts; no prior `exec-report.md`).
- Reviewed: `AGENTS.md` (in-session), `docs/problem.md`, `docs/research-plan.md`, `docs/literature.md`, `docs/operations.md`, relevant notes (`research-n12-nontightness.md`, `research-one-ply-obstruction.md`, `research-structural-lower-bounds.md`, `research-sergeev-asymptotic.md`, `kernel-results.md`), and `docs/research-frontier.json` (no existing `info-bound-gap-invariant-alln` entry).
- Board check before posting: `scripts/board_digest.py --contains "info-bound-gap-invariant" --page 1..3` returned no matches; I posted **once** after writing the report (not a retry/duplicate). Post recorded: Antonina #301 comment `sha256:TV0Zy33AmQWIluPUXHb8ksXHAjc0V-QczdRavc8tl9k` (2026-11-17T04:14:48.763Z, author `iceman-contributor-free`). No repo/Lean/PR changes made.

**Frontier:** `info-bound-gap-invariant-alln` — gap `g(n)=S(n)-ceil(log2(n!))`, `C(n)=ceil(log2(n!))`, unary input `1^n`.

**Sharp, falsifiable all-`n` question (Q, effective gap-window invariant):**  
Is there `W: N -> N` computable in time `poly(n)` on input `1^n` such that for all `n>=1`, `C(n) <= S(n) <= C(n)+W(n)` with an explicit finite (ideally sublinear/asymptotically shrinking) window `W(n)`? Falsifier targets by class: exhibit `n` with `S(n)>C(n)+W(n)` for a proposed `W`; or show no `W` in a stated computable class (e.g. initial-slack/leaf-only `C_leaf`, extension-count-only `C_e`, local merge-factor aggregation without root-quantified strategy closure) is sound for all `n`; or show Sergeev’s asymptotic excess cannot be made into an explicit finite all-`n` poly-time `W` under a stated formalization.

**Consequence for evaluating `S(n)` / `SORT-BOUND-U`:**
- Exact tracking `I(n)=g(n)` in `poly(n)` => `S(n)=C(n)+I(n)` in `poly(n)` => `S_unary ∈ FP` ⇔ `SORT-BOUND-U ∈ P` (unary threshold equivalence, `docs/problem.md`). Not claimed.
- A sound poly-time upper-gap `W(n)` would immediately resolve thresholds with `k < C(n)` (NO) and `k >= C(n)+W(n)` (YES), narrowing exact evaluation/decision to `[C(n), C(n)+W(n)]` — an upper-bound/search-window aid, not by itself NP/P membership or a separation.
- A sound, nontrivial all-`n` root lower-gap invariant (`g(n)>=L(n)`) would give uniform structural lower bounds but requires a strategy-quantified adversary argument; none established.

**Investigation / refutation attempts (paper-first; small exact computation only for sanity):**
- `[literature/definition]` Baseline: `C(n)<=S(n)`; `g(n)=0` for `1<=n<=11`, `g(12)=g(16)=g(17)=g(18)=1` on known exact values (Wells; Stober–Weiß); Sergeev (ECCC TR20-096, Thm. 3) gives `g(n)=O(n/(log n)^(1/5))=o(n)`, but asymptotic form does not supply explicit constants/a finite all-`n` computable bound (`docs/research-sergeev-asymptotic.md`).
- `[experiment/support, trivial]` Recomputed `C(n)=ceil(log2(n!))` for known points `{1..12,16,17,18}`: matches stated gaps (0 through 11, 1 at 12/16/17/18). Discriminates only reporting, not the all-`n` question.
- `C_leaf` (initial slack/`C(n)`-only): refuted for tracking/prediction — efficiency pruning ≡ node leaf bound (Peczarski, per repo notes) and slack ratio does not predict tightness/gap (e.g. tight/non-tight inversions documented in `docs/research-n12-nontightness.md`).
- `C_e` (extension-count/leaf-count state invariants): information-insufficient — same `e(P)` can yield different minimax depths (smallest same-`e` witnesses in repo notes) and sortability not monotone in `e`; one-ply/local bounds (`L0<=L1<=F`) are sound but not shown as a poly-time global closed-form gap invariant.
- Certified merge/structural local bounds: sound local gaps exist (e.g. `Merge(2,4)`), but not quantified over all root strategies for `S(n)`; no all-`n` root-gap lower invariant derived.
- Effective Sergeev extraction (`C_Sergeev-eff`): **blocker** — no explicit finite, poly-time computable all-`n` `W(n)` extracted/audited in this pass from the constructive proof.

**Bottom line (evidence-bearing, no theorem completion):** No poly-time computable all-`n` gap-tracking or nontrivial class-wide upper/lower invariant established. Precise blocker: **effective finite extraction/audit of Sergeev’s group-insertion bound into an explicit all-`n` computable `W(n)`**, or a class-specific barrier for such invariants; either would materially affect the uniform evaluation/search window for `S(n)` / `SORT-BOUND-U`. No complexity-class separation claimed; `SORT-BOUND-U` remains in the known PSPACE/sparse/tally setting per project docs.

**Deliverables:**
- Report: `exec-report.md` (written in this worktree) — includes question, consequences, labeled evidence, refutation attempts, and blocker.
- Board: posted findings to SoringP1 #301 as “SoringP1 frontier: info-bound-gap-invariant-alln” (`sha256:TV0Zy33AmQWIluPUXHb8ksXHAjc0V-QczdRavc8tl9k`).
