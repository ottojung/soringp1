# antonina-OOvVbqh1SNEVEm79YMTG0Z-formally

Session: ses_e0866ca99ffe5DOvy6P2fXFARk
Workspace: /home/lubko/soring-fronts/optimal-node-etie-minimax-collision-alln
Created: 1795155375518; updated: 1795157118506

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f799374d001g1iYkh0MuAS75w)

I'll start by understanding the repository state, the problem definition, and the current board. Let me gather context in parallel.

## Output 25 (msg_1f7994583001eqxixAvXo6qgR8)

Let me check the board digest, literature, and look for any earlier work in this front directory (in case of a prior infrastructure failure).

## Output 44 (msg_1f79958d6001WYpYSi7m56OvNq)

Let me check whether this exact front has prior work or board posts (in case of an infrastructure failure), and search the board for related terms.

## Output 59 (msg_1f7998336001VlzAVN2eQTIO7F)

I see very recent scratch files `tiebreak_probe.py` and `tiebreak_example.py` that relate to this front. This looks like a resume after an infrastructure failure. Let me inspect them and the ledger entry.

## Output 78 (msg_1f79993da001eyjk4AGjwtoFE7)

This is a resume after an infrastructure failure — recent scratch files `tiebreak_probe.py` and `tiebreak_example.py` exist. Let me run them to recover prior results and avoid redoing work.

## Output 98 (msg_1f7a1dc0d001MkELfk6yuaPVSc)

I've recovered the prior work. Key fact: the n=6 "harmful tie" example is actually **not** minimax-optimal at its parent (`1+max(4,5)=6 > F(parent)=5`); the earlier `opt_any` flag was misleading. This is important. Let me now write a clean, exhaustive analysis to attack the real question: does every poset have a non-harmful optimal comparison (which would prove the positive horn by greedy construction), or do "forced-harm" posets exist?

## Output 116 (msg_1f7a2f94d001s8s68hDrcBZzIn)

My enumeration was wrong — I only generated posets compatible with the label order (4824), missing the asymmetric one from the prior evidence. Let me fix enumeration to generate **all** labeled posets and verify against the known counts (A001035: 1,3,19,219,4231,130023).

## Output 164 (msg_1f7a4376a001E4yE2iMM0JnEBR)

All labeled posets now enumerated correctly (counts match A001035). Strong result: **for n≤6, no optimal comparison is ever a harmful tie** (553,725 optimal comparisons checked, zero harmful). Let me probe *why* — measuring the gap between harmful ties and the true optimum, and testing candidate structural invariants.

## Output 182 (msg_1f7a51b97001jitd0mWT26QEvN)

Very clean pattern at n≤6: every harmful tie has gap exactly 1 and satisfies the stronger bound `F(P) ≤ 1+min(F0,F1)`. This suggests a general **balanced-pair lemma**: if `e0=e1` then `F(P) ≤ 1+min(F0,F1)`, which would prove the FRONT. Let me inspect the mechanism on a concrete example, then test at n=7.

## Output 200 (msg_1f7a567be001BlMddmpuxoJHW5)

The mechanism is clear: whenever a balanced-e split has unequal F (child F=5 vs 4), there's an alternative optimal comparison with both children F=4. This suggests the stronger **Theorem A**: every poset has an optimal comparison whose two children have equal minimax value. Let me test this exhaustively.

## Output 218 (msg_1f7a5fe40001TCVzhemgn3Ig8o)

The stronger "Theorem A" is **false** (many states lack an equal-child-F optimum), so the right conjecture is the narrower local lemma. Let me push the search to n=7 by random sampling (computing F only on the descendants of sampled posets), to look for any counterexample where an *optimal* comparison is a harmful tie.

## Output 236 (msg_1f7aa77f2001O7nDscXYafClPH)

At n=7 the local lemma **fails**: there exist optimal comparisons that are harmful ties. This kills the simple constructive proof. Now the decisive question is whether any state has **all** its optimal comparisons harmful (forced-harm), which would be a genuine obstruction to the positive horn. Let me inspect these counterexamples in detail.

## Output 254 (msg_1f7aaaed1001yrx735sxBSecy3)

At n=7, counterexamples to the local lemma exist, but each has 5–8 *other* optimal comparisons that are non-harmful — so an optimal tree can simply avoid them. The decisive obstruction is a **forced-harm** state (all optimal comparisons harmful). Let me search for those, and also verify weak-local-lemma behavior.

## Output 292 (msg_1f7b2ddd7001yz73ermjEreNcb)

## Recovery / side-effect audit (billy-dev, 2026-11-20)
- Inspected: `AGENTS.md`, `docs/problem.md`, `docs/operations.md`, `docs/literature.md`, current board digest (#301 recent/matched terms), git state, `/tmp/opencode` scratch, and frontier ledger entry.
- Git: clean on `billy-dev...origin/billy-dev` at `6a96398` (`git status` empty, no uncommitted/staged changes, single worktree). No commits created.
- Board/ledger/repo: **no posts, no PRs, no Lean/tests/CI/main/ledger edits** were made in this turn. All computations were local scratch in `/tmp/opencode` (from-scratch Python solvers: `tiebreak_probe.py`, `tiebreak_example.py`, `local_lemma.py`, `harm_gap.py`, `inspect_state.py`, `theoremA.py`, `n7_sample.py`, `n7_inspect.py`, `n7_forced.py`).
- Interrupted action: `n7_forced.py` (random n=7 descendant search for a **forced-harm** state: every optimal comparison a harmful e-tie) was killed by SIGKILL and produced no final result; **no forced-harm example was observed in partial output before kill, but this search is incomplete/uncertain** and was not rerun to avoid uncontrolled long side effects.

## Front attacked (all-n, falsifiable)
- **Question:** Can every n be sorted by a height-S(n) optimal decision tree in which no comparison at any reachable state splits that state into two children of equal linear-extension count but unequal true minimax value?
- **Falsifier (negative horn):** for infinitely many n every height-S(n) sorting tree must use a comparison whose two children are extension-tied yet have different minimax values (equivalently, an unavoidable node/strategy-level forced harmful tie).
- **Definitions (model-consistent, from scratch):** P = transitively closed poset on [n] (partial information state, antichain root); e(P)=|LE(P)|; F(P)=exact minimax comparisons to sort P (= minimax height, S(n)=F(antichain_n)); comparison (i,j) optimal iff F(P)=1+max(F(c0),F(c1)); **harmful e-tie** iff e(c0)==e(c1) and F(c0)!=F(c1); **forced-harm** state iff every optimal comparison is a harmful e-tie. This is a local/structural property of optimal adaptive decision trees (not sorting networks, not general-poset hardness transfer, not certificate completeness).

## Mathematical findings (independently checkable, scratch experiments)

### 0. Correction to provided evidence (n=6)
The cited n=6 state (up-masks `[46,0,40,0,2,0]`, e=28, F=5) has comparison (1,3) with e-tied children (14,14) and child minimax values (5,4), but this comparison is **not** minimax-optimal at the parent: 1+max(5,4)=6 > F(parent)=5. The parent admits non-harmful optimal comparisons (e.g. a pair yielding children with equal F and/or non-tied e in the optimal set depending on labeling; concretely for the isomorphic inspected representative `[18,0,34,34,0,2]`, e=28,F=5: pair (2,3) is optimal with e=(14,14), F=(4,4), while (0,2),(0,3) are harmful e-ties but suboptimal with value 6). Thus the stated example is a harmful balanced split but **not** an instance of an optimal harmful tie.

### 1. Exhaustive n ≤ 6: no optimal comparison is a harmful e-tie (strong local property holds)
From-scratch exhaustive enumeration/generation of **all labeled posets** on n elements (counts 1,1,3,19,219,4231,130023 for n=0..6, matching A001035), with exact e(P) and exact F(P) by minimax DP over all states:

| n | posets | states F>0 | optimal comparisons | harmful **optimal** comparisons | states with ≥1 harmful optimal comparison | forced-harm posets |
|---|---:|---:|---:|---:|---:|---:|
| 2 | 3 | 1 | 1 | 0 | 0 | 0 |
| 3 | 19 | 13 | 21 | 0 | 0 | 0 |
| 4 | 219 | 195 | 378 | 0 | 0 | 0 |
| 5 | 4231 | 4111 | 12030 | 0 | 0 | 0 |
| 6 | 130023 | 129303 | 553725 | 0 | 0 | 0 |

**Consequence (n≤6):** the positive horn holds for n≤6 by a trivial local strategy: at every reachable state pick any optimal comparison (none is a harmful e-tie). Equivalently, harmful extension-ties are never forced and never even optimal on [2,6].

Refinement (balanced-pair gap, exhaustive): at n=6 there are 102,345 e-balanced comparisons total; 100,905 have F(c0)==F(c1), 1,440 are harmful e-ties (F differs) and **all 1,440 are suboptimal with gap exactly 1**: `1+max(F0,F1)=F(P)+1` and `F(P) ≤ 1+min(F0,F1)` in every case. No harmful e-tie is optimal at n≤6.

### 2. n = 7: harmful optimal e-ties exist, but no forced-harm found in inspected cases (local lemma breaks, obstruction not found)
From-scratch sampled n=7 states/descendants (bitmask posets, exact e/F on the computed descendant closure): **harmful optimal comparisons do occur at n=7** (refuting the strong n≤6 local property “no optimal comparison is a harmful tie”). Five concrete instances (each independently recomputable):

- `up=[4,29,0,5,0,85,0]`, e=56, F=7: (0,6) e=(28,28), F=(6,5), val=7 **OPT HARM**; 8 other optimal comparisons are non-harmful.
- `up=[118,52,32,80,0,0,16]`, e=28, F=6: (4,5) e=(14,14), F=(5,4), val=6 **OPT HARM**; 5 others non-harmful.
- `up=[2,0,27,3,0,83,0]`, e=56, F=7: (0,6) e=(28,28), F=(6,5), val=7 **OPT HARM**; 8 others non-harmful.
- `up=[62,0,50,2,32,0,10]`, e=28, F=6: (1,5) e=(14,14), F=(5,4), val=6 **OPT HARM**; 5 others non-harmful.
- `up=[28,93,16,0,0,72,8]`, e=28, F=6: (3,4) e=(14,14), F=(5,4), val=6 **OPT HARM**; 5 others non-harmful.

In every inspected n=7 counterexample state, **not all optimal comparisons are harmful** (each has multiple non-harmful optimal alternatives), so the state is avoidable within an optimal strategy at that node. **No forced-harm state (all optimal comparisons harmful) was found.** Because the broad forced-harm search was interrupted (incomplete), this is **not** evidence that none exists at n=7 or all n.

### 3. Failed approach (disproved strengthening)
**“Theorem A” (stronger avoidance):** every poset has an optimal comparison whose two children have equal minimax value F(c0)=F(c1). **False** already at small n by exhaustive check: failures among states with F>0 are 6/13 at n=3, 72/195 at n=4, 1320/4111 at n=5, 28800/129303 at n=6. Therefore equal-F optimal splitting is not a general structural property (and is unnecessary for the front); only non-harmful-among-optimal matters.

## Exact obstruction / honest limits (open status of the front)
- **Positive horn (all-n): OPEN.** It would follow from a local/strategy lemma: every poset reachable on some height-S(n) strategy has ≥1 optimal comparison that is not a harmful e-tie (in particular, no forced-harm state is unavoidable on all optimal strategies). This is proved here for n≤6 but refuted in its “every optimal comparison is safe” strong form at n=7; the weaker “some optimal comparison is safe at every encountered state” remains unproved and unrefuted in general.
- **Negative horn / falsifier: OPEN.** A valid falsification would require, for infinitely many n, a state unavoidable on **every** height-S(n) tree such that all its optimal comparisons are harmful e-ties (a forced-harm obstruction), or an equivalent global argument. I did not find such a state; the n=7 search was incomplete after interruption.
- **Why this is hard:** at n=7 harmful optimal ties first appear, showing the phenomenon is real at optimal nodes (unlike n=6 evidence suggested), but optimal decision trees retain choice; certifying “unavoidable on all optimal strategies” is a global property of the minimax game (all optimal policies) and was not resolved here.
- **Complexity implication (status):** neither the pruning restriction (positive) nor the forced-handling necessity (negative) is established all-n. No claim about S(n) values, SORT-BOUND-U membership/separation, NP/coNP certificates, or EXPTIME/PSPACE improvements follows from these finite computations; this is structural evidence/obstruction only.
- **Scope caveat:** results are for the exact comparison-tree minimax model on labeled inputs/poset states (as in the problem); exhaustive results are n≤6, n=7 is sampled/partial — not a proof for all n. Primary literature on exact S(n) (Peczarski 2012; Stober–Weiß 2023; Wells/Knuth/OEIS context per `docs/literature.md`) was consulted for framing; no contradiction with known exact values found (S(6)=10, S(7)=13 consistent). No external side effects were duplicated; interrupted forced-harm search remains for review if a fuller n=7 pass is desired.
