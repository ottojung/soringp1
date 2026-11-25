# Executive SoringP1 pass — in-flight preservation + one grounded front (2026-11-23 ~06:0xZ)

**Office:** executive, independent delivery on billy-dev; NOT a parliamentary sitting and NOT Clerk intake.
**No theorem completion** is claimed for S(n) or SORT-BOUND-U. No repo/Lean/test/CI/ledger/canonical-main/bill/ballot change.
**External writes:** one #301 comment (2026-11-23T06:10:11Z) and this durable record.

## State inspected at pass start

- Authoritative Constitution; government/executive-agenda.md; government/antonina-interface.md;
  this worktree AGENTS.md (fresh-session handover verified against durable state, not re-executed).
- SoringP1 main /home/lubko/soring301 at 6a96398 (billy-dev): AGENTS.md, docs/research-plan.md,
  docs/research-hardness-boundaries.md Cor 5.2 (lines 315-324), docs/literature.md.
- #301 pages 1-8 (400 messages parsed, no parser failures) and the 708-front authoritative ledger
  at ~/.local/state/soringp1/frontier-ledger.json (671 investigated / 33 blocked / 4 running).
- Operational chores: no live obligations, no open corrective cases, judiciary mailbox empty,
  no unsafe holds, all proceed requests addressed to executive answered, founder-inbox cursors fresh.

## In-flight work preserved

The two fronts commissioned at 05:5xZ were still running and left undisturbed:
- `gap-two-smt-reattack-alln` (8fFABSwHy2ruLjARhPWPOm-clamor): independently rebuilt an exact
  minimax evaluator, caught and fixed an ext-count caching bug, validated S(n) for n<=6, pushing further.
- `framed-dag-n12-explicit-construction-alln` (l9OJh33pRaOM8AWVP0iExS-expulsion): running.

Four curator fronts were also live by mid-pass: `winning-frontier-uniform-alln`,
`bias-path-worstcase-sergeev-alln`, `prime-defect-persistence-alln`, `structural-bound-allornothing-alln`.
No agent was steered, stopped or duplicated.

## One new front commissioned

- ID `dkOLXjFRatJGqIdBfMHrtk-nightmare`, `lin-ext-oracle-turing-placement-alln`,
  verified `state=running`, `prompts=1`, billy-dev worktree, Antonina-selected model.
- Question: poly-time Turing reduction computing F(P), hence S(n)=F(A_n), from an e(Q) oracle on
  DERIVED posets — i.e. can exact S(n) be placed in FP^#P with poly / 2^{o(n log^2 n)} queries?
- Basis: research-hardness-boundaries.md Cor 5.2 rules out the one-shot f(e(P)) route (n=5 witness)
  but states verbatim that "A more elaborate Turing reduction that queries e(·) on derived posets is
  not ruled out by this witness." The ledger's closest entries are the blocked LOWER-bound front
  `linear-extension-oracle-barrier` and blocked hardness front `linear-extension-count-obstruction`;
  neither is this UPPER-placement question (novelty confirmed against all 708 ledger fronts).
- Falsifiers issued: (a) explicit reduction + query bound + correctness; (b) information/adversary
  query barrier or superpoly query lower bound; (c) precise obstruction, never a manufactured result.
- Result to be independently refereed before any claim is treated as established.

## Why not more fronts

Novelty checked against all 708 ledger fronts, not just recent board pages. Randomized exact
evaluation (`randomized-exact-evaluator-speedup`), increment refinements
(`increment-cost-of-adding-one-key`, `increment-monotonicity-dyadic`, `s-non-decreasing-jump`,
`power-of-two-increment-exactness`), communication complexity (`exec-comm-complexity-barrier-alln`,
refuted), FO(LFP/PFP) (`fo-lfp-*` family) and the binary language (out of active scope — AGENTS.md
requires project-owner decision) are all already investigated or blocked. Further fronts here would
be filler, forbidden by the standing Founder priority.

S(n) and SORT-BOUND-U remain OPEN. No case closure, legislative action or Founder decision is implied.
