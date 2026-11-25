# antonina-57pHJ9w7B3HOXYUbuydzmu-screwed

Session: ses_e08b56aa2ffeNMxLEGQWpw7FEJ
Workspace: /home/lubko/soring-fronts/curator
Created: 1795150222700; updated: 1795150465907

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f74a95af001kiQLjxz1h6pVTM)

I'll start by studying the repository documentation and understanding the current state, then check board #301.

## Output 25 (msg_1f74aa426001SdiRVsHWiQN6vc)

Let me check the git state, the existing frontier definitions, and the recent board digest.

## Output 79 (msg_1f74ae846001MqL6iRD7qcQv7C)

Let me examine the full set of previously investigated questions to ensure novelty, focusing on areas near my candidate ideas.

## Output 203 (msg_1f74d799b001A6L0kMP6jibU87)

I've thoroughly reviewed the documentation, the board, and all 589 ledger fronts. Let me do a quick independent scratch check of the newest board's greedy-ball construction to ground my proposals, then write the deliverable.

## Output 221 (msg_1f74deb71001kTZtubc5Md7hSm)

My scratch check independently confirms the key extension-count tie (isolated pair gives 6 vs 6) and super-polynomial ball growth. Now I'll write the curator deliverable.

## Output 248 (msg_1f74e337f001JA4HQMR1Q7BCUD)

Done. I worked only on **billy-dev**, created no Lean/repository changes and made no board posts; the sole artifact is the required curator output.

## What I studied
- `AGENTS.md`, `docs/problem.md`, `docs/literature.md`, `docs/operations.md`, `docs/research-frontier.json`, `docs/research-budgeted-dfs.md`, `docs/research-fo-tc-strategy-programs.md`.
- The newest **#301** digest (through 2026-11-20T04:31Z): the verified greedy-frontier exponential-ball result, the fixed-hitting-set collapse, and the FO(TC) variable-bound collapse.
- All **589** ledger fronts (plus the 22 PREVIOUS entries) to filter duplicates. The frontier is extremely saturated, so I only proposed directions opened by the *newest* results.

## Independent scratch check (grounding, not a repo change)
In `/tmp/opencode/check_greedy_ball.py` I re-derived the decisive #301 fact: an isolated 2-antichain comparison is a genuine extension-count tie (6 vs 6 at n=4), and the greedy reachable ball grows super-polynomially. This is an experiment, **not** a proof.

## Output: `frontier-candidates.json` (2 fronts)
1. **`greedy-ball-compact-index-alln`** — asks whether the exponential greedy ball admits a polynomial-size index enabling subexponential exact evaluation of `G(n)`, directly targeting the Executive's explicit caveat that "a selective or symbolic search need not enumerate the ball." Falsifier is a root-level counting obstruction, deliberately *not* a general-poset NP-hardness transfer.
2. **`greedy-ball-growth-exponent-alln`** — asks for the tight asymptotic exponent of `|R_{G(n)}(n)|` (2^{Θ(n)} vs 2^{Ω(n log n)}), refining the already-settled "not polynomial" question.

## Honest limits
- These are **unverified research questions**, not results; I claim no proof, counterexample, class separation, or S(n) value.
- Front 1 is conditional on the still-running `greedy-adversary-sufficiency-alln` (`G(n)=S(n)`) for its strongest implication; front 2 is a structural refinement.
- I did not post to #301 — the specified deliverable was the JSON file only, and repeating external actions without a genuine finding is inappropriate.
- Git is clean at `f89f6d0` apart from the untracked deliverable `frontier-candidates.json`.
