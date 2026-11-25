# antonina-TJoXhTNtZcZSAxXDm5l55z-jasmine

Session: ses_e4a9ab7e5ffezojb2e8QL0vyNI
Workspace: /home/lubko/soring-fronts/exec-sorting-proof-number-20261107
Created: 1794044676198; updated: 1794044701990

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1b5654a1f001z7269aWnhcd5Mi)

I’ll first check the named paper, research note, and current search scripts, then determine whether the existing machinery supports a bounded comparison without changing the decision semantics. I’ll keep the worktree untouched unless the task yields a qualifying, independently checkable result.

## Output 45 (msg_1b5657238001DqOVfxbcH9ZPRn)

**Result: no benchmark or code change.** The paper’s §6 proof-number search is a plausible lead, but the repository’s `scripts/budgeted_dfs.py` implements recursive Boolean DFS—not df-pn—and has no proof/disproof-number machinery, transposition table, or compatible node-counting interface. Implementing those components just to create a comparison would exceed this bounded task, so I stopped without edits.

For the exact budgeted game, let \(C(P,d)\) mean the sorter can finish from poset \(P\) within \(d\) comparisons. Its recurrence is

\[
C(P,d)=\bigvee_{q\in I(P)}
\left(C(P_q^+,d-1)\land C(P_q^-,d-1)\right),
\]

where \(I(P)\) is the set of incomparable pairs. Its refutation is

\[
\neg C(P,d)=\bigwedge_{q\in I(P)}
\left(\neg C(P_q^+,d-1)\lor \neg C(P_q^-,d-1)\right).
\]

Thus proving the root losing requires refuting **every** comparison; for each, one failing answer suffices. This polarity matters: proof-number search aimed at finding a winning strategy is not automatically a lower-bound refutation search.

A sound proof/disproof-number implementation would need explicit terminal values: total orders are proved at any remaining budget; a non-total state at \(d=0\) is disproved; and unexplored states must remain unknown rather than be treated as failures. At OR nodes, proof cost combines by minimum and disproof cost by sum; at AND nodes, proof cost combines by sum and disproof cost by minimum. These numbers guide search but are not themselves certificates: a sound completed refutation must account for every legal comparison and exhibit a failing child for each. Completeness requires finite branching, decreasing budget, exhaustive expansion without cap termination, and correct terminal propagation. Memoization is sound for identical closed labelled posets with the same budget; isomorphism canonicalization additionally requires preserving the game structure and budget. A capped/incomplete run cannot establish a lower bound.

**Literature:** Cremer, *Selecting the 7th Smallest of 16 Elements Takes Exactly 28 Comparisons*, arXiv:2610.18740v1 (13 Oct 2026), §6 “Proof-number search,” reports df-pn helping construct winning selection algorithms, while budget refutations remained expensive. That is motivation, not evidence that the opposite-polarity sorting refutation will improve over DFS. The repo note `docs/research-winning-frontier-barrier.md`, lines 206–212, likewise lists proof-number search as not excluded, not as a demonstrated route.

**Experiment:** none run; therefore no seeds, caps, measurements, or cross-checks to report. No files changed; worktree remains clean at base `c865b23968388d59316cc994501508d3782be90a`.

**Next falsifiable test:** only after a standalone df-pn implementation exists, compare it against DFS on one safely tractable known losing threshold, with identical node accounting, fixed ordering/seed, hard resource caps, and independent confirmation by `scripts/evaluate.py` or a published exact \(S(n)\). Stop on any cap hit; do not interpret an incomplete search as a refutation.
