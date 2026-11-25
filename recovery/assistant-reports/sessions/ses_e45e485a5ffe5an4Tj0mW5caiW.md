# antonina-0XAAsv8UW9476kwjPbUtdl-splints

Session: ses_e45e485a5ffe5an4Tj0mW5caiW
Workspace: /home/lubko/soring-fronts/t10-census-extension
Created: 1794123725470; updated: 1794168468668

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1ba1b7c5700162d3WrTBAagPno)

I'll start by inspecting the repository state and the census script.



## Output 168 (msg_1ba34e71f0010z9cS7VR1aTmv8)

The E=143 run was interrupted by the backend failure (log stops at level 13), and the staircase check was OOM-killed at W_12. Durable state: level pickles 2–13 are complete on disk. I'll resume the census from level 14 rather than recompute.



## Output 690 (msg_1bae4ffef001018nd05rWEDKHh)

The E=200 run is progressing but the host is heavily loaded by unrelated tenant processes (~0.5 effective CPU for 4 workers), so it's slower than the E=143 run. It's resumable level-by-level. Continuing to monitor.



## Output 842 (msg_1bb0c04800018jzKJRMnnJDta7)

The host keeps killing processes every ~20 min, and level 15 under cutoff 200 needs longer than that. I'll switch to a checkpointed runner so progress survives kills, and target E=160 (feasible cutoff) instead of 200.



## Output 1355 (msg_1bbc2449c001HFyMslZ7OB8YfA)

E=160 census complete. Now verifying totals, checking that the filtered prefix is exactly the cutoff-160 census, and that no core failed at h=10.



## Output 1395 (msg_1bbc30e1b001tHD2NprXF8zSJb)

I found a bookkeeping bug: a level with a generation pickle but no failure record was treated as complete, so level 54's checks were skipped. Let me inspect and repair.





## Output 1446 (msg_1bbc5559d001FaO8xcbweah7xS)

Filter equivalence validated (fresh cutoff-160 level 10 = filtered prefix, 17,151 cores). Now extending to E=200 with the now-fixed checkpointed runner.





## Output 1886 (msg_1bc55d142001zzUnnI0mPfbSD3)

The check phase is now the bottleneck for large-`n` thin cores. I'll skip comparable pairs cheaply using the poset's order, then benchmark.



## Output 1931 (msg_1bc5800d3001Zu7jSMuDioqXXW)

The verifier is right that levels 2–14 lack durable per-level failure records (the earlier parallel runs checked them, with `fails=0` in the logs, but wrote no R files). I'll keep the 15..200 driver running and add a durable low-level check pass for levels 2–14 afterward.



## Output 2006 (msg_1bc88c84d001REhotNobRhKONt)

E=200 levels 15–200 complete. Now the durable low-level pass the verifier asked for: filter levels 2–14 to e≤200 and run the checkpointed h=10 checks for them (writing R records).





## Output 2062 (msg_1bc9c93220013LFYBD0UkKB19c)

Low-level checks complete with zero failures. Now the final consistency validation and totals for E=200.





## Output 2080 (msg_1bca104a2001cauluGQzMuaylQ)

E=200 census is complete and self-consistent. Let me gather final statistics for the report.



## Output 2091 (msg_1bca1baa8001j2j4pDo4U2R577)

To make the low-level evidence fully durable (including e in 144–160, currently only in logs), I'll redo levels 2–14 with `--safe-e 143` so every e>143 core at those levels has an R record.



## Output 2174 (msg_1bcc1cfbd001Fk0j5lY4vJJAvc)

## Report — t10-census-extension

**Worktree untouched** (`git status` clean, main `f89f6d0`). No commit/push/merge and no board post. Drivers and artifacts are in `/tmp/t10` (see `SUMMARY.md`).

### 1. T(9) reproduced — E=143, h=9

Ran the repo implementation (`scripts/core_threshold_census.py`, imported read-only) through a streaming/parallel, resumable driver (the naive in-memory enumerator still OOMs; levels are pickled one per `n`):

```
census_stream.py --E 143 --h 9 --out /tmp/t10/lv143            (levels 2–13)
census_stream.py … --start 14                                  (levels 14–26)
census_par.py    … --start 27 --jobs 4 --exact                 (levels 27–34)
census_par.py    … --start 35 --jobs 4 --exact                 (levels 35–92)
census_par.py    … --start 93 --jobs 4 --exact                 (levels 93–143)
```

**cores = 101,826, failures = 0** — levels 2–143, max `e`=143. Log: `/tmp/t10-census.log` (every level `fails=0`, final `E=143 h=9 DONE cores=101826 failures=0`). Pickles: `/tmp/t10/lv143/L002…L143.pkl` (210 MB).

Independent checks: all 101,826 objects are cores with `e≤143`; on a 500-core sample (`n≤12`) the extension count recomputed by ideal-lattice DP equals `len(exts)` and every stored permutation is a linear extension — 0 mismatches. `W_11` has `e=144, m=10` exactly, so E=143 is tight for T(9).

### 2. E=160, h=10 (intermediate, complete)

**152,796 cores**, levels 2–160, **failures 0, unknown 0** (146 per-level R records). `101,826 (e≤143) + 50,970 (144≤e≤160) = 152,796`. Artifacts `/tmp/t10/lv160/`.

### 3. E=200, h=10 (main new result)

**320,028 cores**, levels 2–200, **failures 0, unknown 0**, 199 per-level R records. Ranges: 101,826 (`e≤143`), 50,970 (`144–160`), 167,232 (`161–200`); max `e`=200; 0 structural violations. Artifacts `/tmp/t10/lv200/` (1.1 GB), raw cutoff-232 prefix in `/tmp/t10/lv200_raw/`.

Checks used a sound greedy decision-tree constructor first and a capped exact minimax fallback; `unknown=0` means no node-cap abort. Answering the verifier’s point: levels 2–14 were **re-run with durable R records** using `census_ckpt.py --E 200 --h 10 --safe-e 143`, so the claim no longer depends on log-only evidence.

Consistency:
- E=160 and E=200 agree exactly on every `e≤160` core at all levels 2–160 (0 key-set differences).
- Fresh cutoff-160 level-10 generation = filtered prefix (17,151 cores, identical keys); fresh cutoff-200 level-10 generation = filtered cutoff-232 prefix (28,358 cores, identical keys).
- 400-core sample: DP extension counts/validity 0 mismatches; 25 cores with `161≤e≤200`: exact minimax confirms “sortable in 10”, 0 disagreements.

### 4. E=232 — attempted, **not** completed

A cutoff-232 run completed levels **2–10 only**: 66,320 cores (level 10 = 38,494), h=10 checks for all `e>143`, 0 failures; 15,058 of these have `200<e≤232` and are sortable in 10. Levels 11–232 under cutoff 232 were not enumerated (level 11 alone is ≥36,779 cores; the host is heavily oversubscribed). Boundary reference: `W_12` has `e=233`, `is_core=True` (verified here) and `m=11` (task/prior-record reference, not recomputed).

### Verdict

**T10-HOLDS-TO-E<=200.** No core with `e≤200` has `m≥11`; nothing is claimed for 201..232, so **T(10)=232 is not established** (and was not refuted). This is a finite census — computational evidence conditional on the documented core generator, **not** a Lean proof.

## Output 2244 (msg_1bcc62442001R3pSxBPJduvJVM)

Posted and verified.

**Comment confirmed on Antonina issue #301** at `2026-11-08T20:07:35Z`, author `SoringP1 frontier: t10-census-extension` (visible via `board_digest.py --contains "T10-HOLDS"`).

The post states exactly:
1. **T10-HOLDS-TO-E<=200** — 320,028 cores with `e<=200` (levels 2–200, 199 per-level R records, levels 2–14 re-run with `--safe-e 143`), all sortable in 10 comparisons, failures=0, unknown=0.
2. Range counts: 101,826 (`e≤143`, from the h=9 reproduction) + 50,970 (144–160) + 167,232 (161–200) = 320,028.
3. **T(10)=232 is not established and not refuted**; the E=232 attempt reached only levels 2–10 (66,320 cores; 15,058 with `200<e≤232` sortable in 10) and was stopped.
4. Caveats: finite computational evidence conditional on the documented core generator, not a Lean proof; `W_12` has `e=233` with `m=11` as boundary reference (m=11 cited, not recomputed).

No repo commit; worktree remains clean at `f89f6d0`. Untracked artifacts and drivers remain under `/tmp/t10` (`SUMMARY.md`, `lv143/`, `lv160/`, `lv200/`, `lv232/`).
