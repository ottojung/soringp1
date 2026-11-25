# SoringP1: Lean-checked complexity of optimal sorting numbers (phoebe-dev only)

3515 distinct messages in 71 pages.

## Original issue description

**CURRENT EXECUTION HOST: billy-dev ONLY (Founder assignment, 2026-10-23).** The old parenthetical phoebe-dev-only title is stale; it is NOT the current host rule. Every SoringP1 Viche agent runs on Billy. The research mandate remains open until the final precisely stated theorems are proved and independently checked, and genuine obligations have been closed. Empty research packets, successful agent exits, and the present absence of a proof are not completion. Reassess distinct promising mathematical fronts rather than generate filler work.

# SoringP1 — complexity of the exact sorting-number function S(n)

## Goal and scope

Determine the **uniform computational complexity of evaluating S(n)**, the optimal *worst-case* number of comparisons in deterministic adaptive sorting of n distinct keys. The endpoint is a genuinely new mathematical theorem on S itself (or its explicitly encoded threshold language), ultimately Lean kernel checked when the theorem merits formalization. This is not a request to solve P vs NP. A classification is presently unknown. Distinguish unary and binary n, numeric functions from decision languages, and ordinary comparison sorting from computing the sorting number.

Repository: https://github.com/ottojung/soringp1
Research contract: AGENTS.md; problem definition: docs/problem.md.

## Binding operational pivot — 2026-10-18

**Stop PR-driven research and premature formalization. The default output of a research session is a finding, counterexample, or honest unresolved obstacle, NOT a commit, issue, proof file, test suite, or PR.** No requirement to publish each elementary lemma, small-instance observation, search heuristic, or literature note. Existing Lean model, tested algorithms, and archival research contributions remain preserved.

Use agent intelligence for hard exploration, not routine packaging:
- Ask one precise, falsifiable question, state why answering it would constrain the complexity of the special **S(n)** problem, and attempt serious disproof / alternatives.
- Read relevant *primary* literature and extract the actual theorem, proof idea, model, assumptions, and applicability. Do not mistake a hardness theorem for arbitrary decision trees or all posets as one for fixed antichain S(n).
- Favor long mathematical reasoning, constructive searches for algorithms/reductions, and decisive minimal experiments; do not invent quantitative progress from passing CI or n<=6 data.
- Investigate substantial hypothetical avenues even if they fail. Distinguish evidence, deductions, conjectures and theorems; report the strongest failed approaches. Agents may conclude **no result**, without creating any artifact.
- Avoid returning repeatedly to incremental poset F(P) bounds, symmetry, lookahead, toy backward DP, or more small witnesses **unless** an explicit mathematical bridge is proposed from them to a new *uniform asymptotic bound*, *valid hardness reduction to S(n)*, *succinct certificate*, or other direct advance on complexity classification.
- Avoid converting every idea into a separate research PR or agent. No quotas for agent occupancy, test count, commits, paper sections, or Lean statements. Stop or redirect unproductive assignments; do not immediately replace them with more packaging work.
- New GitHub PRs / committed research notes require a **significant** and independently checked theorem, fundamentally new evaluator with honest asymptotic analysis, meaningful valid reduction, or essential correctness repair, with a clearly stated impact on S(n). A speculative or negative result can qualify if it rules out a major route; otherwise report it here and move on.
- **No additional Lean formalization as a default activity.** Kernel-check a mature significant claim only after a convincing independent paper argument and a specific model/cost/correspondence justification. The existing S_eq_adv_univ theorem is already established; routine small-n or helper proofs are not research priorities.

## Priority research questions (open-ended, not a checklist of deliverables)

A. **Uniform algorithms.** Could S(n) be computed in polynomial numeric-n time or subexponential numeric-n time? Is 2^{O(n log^2 n)} time fundamentally improvable, and by which exact recurrence / structural theorem? Analyze unary and binary input lengths separately. An algorithm for sorting the n keys is NOT an algorithm that outputs their *optimal comparison count*.

B. **Hardness for the special family.** What provable reduction or obstruction bears on exact S(n) or SORT-BOUND-U/B? General-poset CanSort(P,k), optimal binary trees with arbitrary tests, expected-case identification, and linear-extension counting are different problems. Do not transfer hardness without a uniform encoding-preserving reduction. Remember unary threshold sparsity and known nonuniform advice cutoff.

C. **Global characterization / succinctness.** Find a nonlocal structure, invariant, certificate or algorithm characterizing exact S(n) that avoids exhaustive adaptive-tree search. Identify which barriers in the known exact sorting literature are structural versus artefacts of current search.

## Research reporting (brief; not a deliverable pipeline)

Post an occasional compact comment on this issue only when there is substantive movement: **hypothesis → strongest argument/experiment and sources → falsification/obstacle → what changed about our beliefs on the complexity of S(n) → next decisive question**. A simple well-supported failure may be more informative than a polished PR. Do not make routine status comments or create busywork to fill the board.

When there is no promising theoretical route, report that explicitly and stop that run rather than initiating Lean, writing documentation, or spawning the next agent for appearance's sake. **Progress is a change in knowledge about S(n), not merged PR count.**

Existing open research PRs (#22–#25 as of this pivot) should be reviewed/triaged once on their mathematical merits; do not treat closing that queue as a research milestone, and do not create derivative documentation tasks merely to finish it.

## Execution boundaries

**Every SoringP1 Viche/Antonina agent, worktree, manual build, and experiment executes ONLY on lubko://billy-dev.** Never move to marceline-dev or another host if Billy is unavailable; pause instead. GitHub-hosted Actions CI, hosting and PR review/merge remain permitted. All commits merged to main must be signed, and claims must distinguish Lean-kernel-checked from paper-level or experimental.

Keep this Antonina issue open until the actual classification question is settled; do not redefine completion as polishing research notes or closing PRs.

## Last recorded review

{
  "commit": "4abf2a6e047b4c4d4a4309c9e663c89ed4636387",
  "rationale": "YES. Independently re-derived every finite claim with disjoint primitives (permutation e-count, separate minimax, plain BFS components). Confirmed: chain L0<=L1<=B<=F (proof correct; exhaustive n<=4, 242 posets, 0 violations; n=5 B=L1 over all 4231 posets, 0 violations); maximal series decomposition (cross pairs comparable, factors series-prime, e multiplicative, F additive); n=7 witness P=(124,124,0,0,4,12,28) e=16,L0=4,L1=4,B=5,F=5 with F=5 direct (not only additivity); W^t splits 5/3,5/3,6/2,6/2 and L1(W^t)=3t+1, B=F=4t; Q^t e=3^t,F=2t and minimal-t per horizon {0:3,1:5,2:8,3:10,4:13,5:15}; capped census matches independent permutation census and prune_verdict(P,d) is False iff L1(P)>d (1452 checks, 0 mismatches), edge cases total/d=0/d<0 correct, no 2^n table. n=7 is in fact globally minimal: complete targeted enumeration of all ordinal sums with parts>=2, total<=6 (1111 combos) found 0 strict B>L1. Only defect: doc arithmetic 1+3+19+219+4231=4474 should be 4473 (cosmetic, no math depends on it). No counterexample found. Review branch research/review-composition-20261018 at 4cc0a02 (signed); reviewer script/tests/docs added there. Not merged, source branch unmodified.",
  "recordedAt": "2026-10-19T03:34:52.169Z",
  "reviewer": "SoringP1 independent reviewer",
  "verdict": "approve"
}

## Pages

- [Page 1](page-001.md)
- [Page 2](page-002.md)
- [Page 3](page-003.md)
- [Page 4](page-004.md)
- [Page 5](page-005.md)
- [Page 6](page-006.md)
- [Page 7](page-007.md)
- [Page 8](page-008.md)
- [Page 9](page-009.md)
- [Page 10](page-010.md)
- [Page 11](page-011.md)
- [Page 12](page-012.md)
- [Page 13](page-013.md)
- [Page 14](page-014.md)
- [Page 15](page-015.md)
- [Page 16](page-016.md)
- [Page 17](page-017.md)
- [Page 18](page-018.md)
- [Page 19](page-019.md)
- [Page 20](page-020.md)
- [Page 21](page-021.md)
- [Page 22](page-022.md)
- [Page 23](page-023.md)
- [Page 24](page-024.md)
- [Page 25](page-025.md)
- [Page 26](page-026.md)
- [Page 27](page-027.md)
- [Page 28](page-028.md)
- [Page 29](page-029.md)
- [Page 30](page-030.md)
- [Page 31](page-031.md)
- [Page 32](page-032.md)
- [Page 33](page-033.md)
- [Page 34](page-034.md)
- [Page 35](page-035.md)
- [Page 36](page-036.md)
- [Page 37](page-037.md)
- [Page 38](page-038.md)
- [Page 39](page-039.md)
- [Page 40](page-040.md)
- [Page 41](page-041.md)
- [Page 42](page-042.md)
- [Page 43](page-043.md)
- [Page 44](page-044.md)
- [Page 45](page-045.md)
- [Page 46](page-046.md)
- [Page 47](page-047.md)
- [Page 48](page-048.md)
- [Page 49](page-049.md)
- [Page 50](page-050.md)
- [Page 51](page-051.md)
- [Page 52](page-052.md)
- [Page 53](page-053.md)
- [Page 54](page-054.md)
- [Page 55](page-055.md)
- [Page 56](page-056.md)
- [Page 57](page-057.md)
- [Page 58](page-058.md)
- [Page 59](page-059.md)
- [Page 60](page-060.md)
- [Page 61](page-061.md)
- [Page 62](page-062.md)
- [Page 63](page-063.md)
- [Page 64](page-064.md)
- [Page 65](page-065.md)
- [Page 66](page-066.md)
- [Page 67](page-067.md)
- [Page 68](page-068.md)
- [Page 69](page-069.md)
- [Page 70](page-070.md)
- [Page 71](page-071.md)
