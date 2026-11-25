# antonina-l9OJh33pRaOM8AWVP0iExS-expulsion

Session: ses_df90bcba3ffePiGgJuBuZkkLgX
Workspace: /home/lubko/soring-fronts/framed-dag-n12-explicit-construction-alln-20261123b
Created: 1795412997217; updated: 1795415520212

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_206f437650019Sz24NpWFocFrc)

I'll start by orienting myself as instructed — reading all the required context files in parallel.

## Output 29 (msg_206f44f2b001WB10gnB7vyT7H6)

I've oriented on the contract. Now let me check the durable ledger for my exact front, read the framed-certificate frontier doc, and find the verifier code.

## Output 48 (msg_206f462ae00165e8BW3tP55zWX)

My exact front is not in the ledger, though related fronts are. Let me check the board for my exact slug, inspect the ledger details, and read the verifier code.

## Output 67 (msg_206f48962001MSSXNMXlhUlGtQ)

I now understand the verifier semantics precisely. Notably, the premise "n=12 is not a Ford–Johnson tree" needs checking — F_FJ(12)=30=S(12). Let me examine the existing n=12 framed-DAG work in the repo read-only (git show/log only, no file modification) and scan more of the board.

## Output 99 (msg_206f53c1f0015MUzzPljoqInB6)

Let me look at the actual content of the n=12 framed-DAG branches and any existing scripts/notes for concrete evidence.

## Output 127 (msg_206f5c0c00017f8ODqM1q8qnKf)

I have the core machinery. Let me look for existing Ford–Johnson construction code and check what state counts were measured, then set up scratch tooling.

## Output 164 (msg_206f640350013fjCtwRf4pKf6g)

I now have the FJ implementation and verifier semantics. Let me set up scratch tooling and build a symbolic FJ compiler, validating the pipeline on small n first.

## Output 175 (msg_206f760f00019HarusoC1SDBQw)

Now let me write the symbolic FJ compiler with explicit state machine and hash-consing, then validate on small n against the verifier.

## Output 268 (msg_206f92f4d001WpzdQg5j89kF0S)

With identity frames the compiled FJ tree has exactly n! nodes (no sharing). Let me measure how many distinct canonical (isomorphism-class) posets arise — that bounds what frame-based merging could achieve.

## Output 286 (msg_206f971fe001chLYr1WY3giEWp)

Excellent — only ~O(n) isomorphism classes of posets are reachable. Frame-based merging could give a tiny DAG. Let me implement canonicalization with permutation frames and build the actual framed certificate.

## Output 329 (msg_206fa880d001k6TXgMW3Sj1yuQ)

Found the bug — the canonicalizing frame was cached from the first incoming config rather than recomputed per incoming edge. Let me fix the cache to store only node ids.

## Output 435 (msg_206fba273001JErbALDEj3v2mG)

Found it — delegating calls returned the nested frame instead of the current one. Let me fix all delegating returns.

## Output 446 (msg_206fbc873001cE9o3NR6MUyPM7)

n=3 now verifies. Two issues remain: backward edges (needs topological reordering) and control-state errors for n≥5. Let me add topological sorting first.

## Output 491 (msg_206fc99a6001MdPTMeLwz6g2p1)

Let me test whether the errors come from unsound state merging (cache) or a control bug, by disabling hash-consing.

## Output 520 (msg_206fd1c04001H5KUXzwLtb3Gqx)

Found a real bug — the recursive straggler was set from the parent. Let me fix it.

## Output 538 (msg_206fd43e1001VUDZNTdXmD0imC)

All small n verify with tiny node counts and correct optimal depths. Now the decisive run — n=8 through 12.

## Output 565 (msg_20706af67001WOemdcgXJfKhg7)

I'll first verify what actually happened — no board post should exist yet, and I need to check scratch state after the SIGKILL.

## Output 584 (msg_20706e939001U0YY3NmPgzkxpt)

Two board comments reference my slug but by "Viche Executive" — likely referee notes, not my deliverable. Let me read them fully and check the n=11 artifact.

## Output 595 (msg_20707213c001WKRAkCADyS4dGP)

The two board comments are Viche's commissioning/executive notes, not my result — my deliverable is still owed and nothing was duplicated. Let me verify the n=11 artifact and try n=12.

## Output 606 (msg_207077c31001pNu2CnQLC9C043)

n=11 was killed (truncated artifact). My construction already exceeds 10000 nodes at n=9–10. Let me try a memory-optimized run for n=11/12 to get exact counts, with a hard cap.

## Output 617 (msg_2070d5b43001YgmNF3XYTOmf3X)

n=11 completed: 1,247,431 nodes, depth 26 (correct). Let me launch n=12 with a cap in the background while I prepare the result.

## Output 637 (msg_2070db61300136PDdtQv4eoL22)

Let me check on the n=12 run and then finalize the result file.

## Output 657 (msg_2070fc6be001uClqGO0lfyXlee)

The n=12 background process died (likely OOM, no output). Let me make one bounded attempt with a lower cap to get a concrete count.

## Output 677 (msg_207108dba001VheHXnBI04qs95)

The bottleneck is the O(n!) canonical-labeling enumeration at the root antichain. Let me special-case it and retry n=12.

## Output 697 (msg_20719bb7a001I9IvMOx0cnLyWr)

n=12 hit a 2.5M-node cap (no exact transcript). I have decisive evidence for the verdict. Let me capture the exact verifier CLI output, then write and post the single result comment.

## Output 717 (msg_2071a31f20011mD15vzYTLF9Ba)

No prior result post by me exists (only Viche's commissioning notes). Posting the single deliverable now.

## Output 728 (msg_2071a6eb0001PKj75bQ72CCjIB)

Let me verify the comment appears exactly once on page 1.

## Output 739 (msg_2071a94a0001o9m695JZgqZ5Nf)

Done. The single deliverable is posted and verified on Antonina board #301 (exactly one post by my author, timestamp 2026-11-23T06:31:34Z, 5025 chars).

**Summary of the result (verdict c — honest inconclusive):**

- **Premise correction [literature+computation]:** n=12 is *not* the first non-Ford–Johnson case — F_FJ(12)=30=S(12). It is the first case where the information bound fails (C(12)=29 < 30).
- **Concrete evidence [experiment]:** I compiled the explicit FJ strategy into permutation-framed DAGs with colour-refined isomorphism canonicalization and ran the *unmodified* verifier. All passed with depth = S(n): n=3→4 nodes, …, n=8→2,535, n=9→22,695, n=10→113,431, n=11→1,247,431 nodes. The ≤10,000 target is already missed at n=9; n=12 hit a 2.5M-node cap (no transcript obtained).
- **Obstruction:** the verifier's meet-at-join plus frame relabeling cannot merge continuations whose FJ control state (insertion schedule, exact pending-loser rank windows) isn't a function of the poset annotation — matching the earlier `framed-dag-exact-budget-hybrid-alln` finding (weak windows give 39 > 30; exact positions split exponentially).
- **Next decisive obstacle:** a join-safe frame discipline making control a function of the poset annotation at each meet, or a rigorous non-mergeability lower bound at height 30 for n=12.

No repo, Lean, test, CI, ledger or canonical-main changes were made — all scratch under `/tmp/opencode`.
