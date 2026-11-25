# antonina-XNXqmDRTDChwk9qd6uwgs1-moan

Session: ses_e32996c55ffewIIrTDM1FdHHwN
Workspace: /home/lubko/soring-fronts/n8-threshold-finish-20261112
Created: 1794447414188; updated: 1794456797485

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 354 (msg_1cdf51310001EbYNlNU3k91XtH)

## Recovery / no-duplication check
- Inspected cwd/git/board before acting: clean worktree at `f89f6d0` on branch/worktree `n8-threshold-finish-20261112` (`git status` clean). No commits, no checkpoint/script edits, no prior external post by this session.
- Audited prior #301 state for this exact question (`e(P) >= F_{m(P)+2}`, `F1=F2=1`, n=8): `fibonacci-threshold-n8-20261111` (0/16999), `fibonacci-threshold-n8-completion-20261111` (0/16999), `fibonacci-threshold-n8-ordered-20261111` (16965/16999), `fibonacci-threshold-n8-ordered-resume` (16965/16999), plus Executive verifications. I did not rerun the existing driver or duplicate compute; I only audited artifacts and posted one update (below) with new verified evidence.

## Audit of prior artifacts / code (sources)
- Active checkpoint/run: `/home/lubko/soring-fronts/fibonacci-threshold-n8-ordered-20261111/`
  - `checkpoint_n8_ordered.jsonl` (16965 lines), `classes_n8.json` (16999), `e_values_n8.json` (16999), `summary_n8_ordered.json`, `n8_ordered.py`, `run_n8_ordered.log`, `xcheck_independent.{py,log}`, `xcheck_hard.{py,log}`, `comment_301*.md`.
- Earlier attempt dirs: `fibonacci-threshold-n8-20261111` (`n8_fib.py`, 0/16999 log/comment context), `fibonacci-threshold-n8-completion-20261111` (`n8_complete.py`, `classes_n8.json`, no checkpoint), `fibonacci-threshold-n8-resume-20261111` (empty).
- Core primitives (read-only, depended on by above): `/home/lubko/soring-fronts/fibonacci-threshold-20261111/solve_fib.py` — refined-canonical class enumeration from antichain, exact `e(P)` by subset/downset-prefix DP, exact minimax `m(P)` by poset-state memo (`m_poset_state`, branching on incomparable pairs with transitive-closure extension), independent extension-set minimax `m_extension_set`, Fibonacci `F1=F2=1`.
- Driver logic (`n8_ordered.py`): precompute/cache all `e(P)`, sort classes by `e` ascending, compute `m(P)` in that order via multiprocessing pool, per-class JSONL checkpoint (flush+fsync), running min slack, early violator exit, inline cross-checks on small-e samples. `summary_n8_ordered.json` reports `status=incomplete, done=16965/16999, complete=false, count_ok=true, min_slack=0, tight=33, violator=null, cross_agree=30, cross_total=30, stalled next_idx=16922 next_e=4480 pending_count=34, status_note=timebox` (final 2400s segment).

## Independent validation performed (this audit)
- **Checkpoint integrity [experiment/deduction, own read]:** 16965 JSONL lines, 16965 distinct `idx`, 0 malformed, 0 violations (`slack<0`), `min_slack=0`, 33 tight (`slack==0`). Pending = 34.
- **Class/enumeration count [experiment]:** `classes_n8.json` length 16999 = `A000112(8)` (matches prior). `e_values_n8.json` length 16999.
- **`e(P)` recomputation [experiment]:** recomputed `count_linear_extensions` for **all 34 pending** classes and **50 random completed** classes — **0 mismatches** vs `e_values_n8.json`/checkpoint.
- **Record arithmetic [deduction/experiment]:** sampled completed records satisfy `bound == F_{m+2}` and `slack == e-bound` (spot checks 0 bad). Tight examples present (e.g. idx 15: e=3,m=2; idx 16: e=2,m=1; idx 17: e=1,m=0).
- **Cross-check evidence present [experiment, prior artifacts]:** driver inline 30/30 `m_poset_state` vs `m_extension_set` (log/summary), `xcheck_independent.log` 24/24 agree (stratified, e=7..324, seed 20261111), `xcheck_hard.log` 9/9 agree (e=836..1920) — 63/63 reported, 0 mismatches. (I did not rerun these full cross-checks; I verified the logs/scripts/artifacts exist and are consistent.)
- **Pending set characterized [experiment]:** exact 34 missing `idx` include {0..3,16758,16812,16857,16900,16901,16914,16921,16922,16962,16969,16971,16972,16977,16978,16982,16983,16985..16998}. `e(P)` distribution: {4480:1,4704:4,5040:7,5376:2,5760:2,6048:2,6720:6,8064:2,8400:1,10080:3,13440:2,20160:1,40320:1}. `idx 0` is the 8-antichain `(0,0,0,0,0,0,0,0), e=40320`.
- **Feasibility probe [experiment]:** timed `m_poset_state` on smallest pending `idx 16922` (`e=4480`) for 120s — **no result returned (timeout)**.

## Current exact validated coverage (census status)
- **Validated completed:** 16965/16999 unlabelled n=8 classes have recorded `(idx,e,m,bound,slack)` with 0 observed violations, `min_slack=0`, 33 tight. Coverage 99.80% of A000112(8).
- **Unvalidated/pending:** 34/16999 classes (all `e >= 4480`, up to 40320) have **no computed `m(P)`** in the checkpoint. For these, `e(P)` is independently revalidated but `m(P)`/inequality status is unknown.
- **Conclusion:** **no violator exhibited; no n=8 boundary/certified census** (cannot be claimed while 34 remain). Partial coverage carries no certifying weight for the remainder; no all-n claim.

## Feasibility and bottleneck
- **Completed exact census now:** not achieved. **Feasibility with current method (as-is, in-session): not feasible.** Evidence: 34 hardest/high-extension classes remain; smallest pending (`e=4480`) did not finish in 120s under poset-state minimax; prior tail rate degraded to ~0.006 classes/s (~2.7 min/class over 2 workers) and stalled at the e≥4480 band (logs/summary). The antichain case (`idx 0, e=40320`, `m=S(8)`) is a distinct hard instance (literature value of `S(8)` is known, but it is not computed in this checkpoint).
- **Rigorous boundary/violator:** only feasible if every pending class gets an exact, checkable `m(P)` (or a certified lower/upper argument strong enough to decide `e >= F_{m+2}` for that class). No such decisive certificate is present for the pending 34.

## Concrete falsifiable next step
- Resume from the durable ordered checkpoint and, for each of the 34 pending `idx` (starting at smallest-e pending, e.g. 16922,4480), compute **exact** `m(P)` with a stronger exact/pruned minimax strategy (e.g. proven alpha-beta/admissible lower bounds on `m`, move ordering, symmetry/reduction where sound for the canonical rep, or a different exact solver) and append verified records `(idx,e,m,bound,slack)`.
- **Falsifier/decider:** any single record with `slack = e - F_{m+2} < 0` is a decisive n=8 violator (disproof witness); independently cross-check that witness (and tractable pending results) via `m_extension_set` or a second exact method. Verified records for all 34 certify the n=8 boundary. Treat `idx 0` (antichain, needs `m=S(8)`) explicitly—if using a literature value, label it **literature** and separately supply/verify an exact computation or certificate.

## #301 update
- Posted **one concise update** to Antonina issue #301 (author: `SoringP1 audit: n8-threshold-finish`, 2026-11-12T04:12:27Z): <https://github.com/ottojung/soringp1/issues/301#issuecomment-> (comment recorded in board JSON at `createdAt 2026-11-12T04:12:27.404Z`, id `sha256:5eRCGKqq0CopFjf3AR3alHMUH1zM-GKeymOa-rikYMk`).
- Checked for duplicates before posting (`board_digest --contains "16965"` showed prior 16965/16999 reports). Posted because it adds verified evidence beyond existing incomplete reports: independent `e(P)` revalidation for all 34 pending + 50 sampled completed (all matched), sampled `bound/slack` arithmetic check, exact pending-by-`e` characterization, and a 120s `m_poset_state` timeout probe on smallest pending `idx 16922 (e=4480)`.

No repo/Lean edits; no publication-gate item met.
