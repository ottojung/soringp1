# antonina-ozstbvhkvhsx7OoTGL91Vu-streaming

Session: ses_dfd60aaa1ffelS1xWzE1V5TwYL
Workspace: /home/lubko/soring-fronts/per-key-load-additive-gap-alln
Created: 1795340326321; updated: 1795341491557

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_2029f5765001rEXNrT3BpG4v5q)

I'll start by understanding the repository state, the relevant documents, and the branch situation.

## Output 17 (msg_2029f67f7001pRrocm0mYHHUdO)

I'm already on `billy-dev` with a clean worktree. Let me read the key documents and find board #301.

## Output 45 (msg_2029f89630019TC41ok5p07U4f)

Let me read the frontier definition for this front and query board #301 via the digest script.

## Output 60 (msg_2029f99ee0014QA1xoVEWIFDWH)

Let me get the full text of the relevant board post #301 (07:42Z) and check the digest script options.

## Output 93 (msg_2029fe8c6001eLACxYFtdVMoim)

The digest caps excerpts at 2000 chars. Let me extract just the full body of the specific 07:42Z post directly (without dumping the whole board).

## Output 104 (msg_2029fffa0001BLLyhkZLNvUc6m)

I have the full board post. Let me now search the literature and the repository's own notes for relevant known results on per-key comparison load, to avoid rediscovery.

## Output 115 (msg_202a2957b0019g2psOYPAcZFJN)

Let me search the primary literature and web for known results on per-element comparison counts in optimal sorting.

## Output 157 (msg_202a31c84001IkbvQsJqlBR3aA)

Let me check the scratch files from the previous session and see whether a solver exists that I can reuse to extend the computation.

## Output 177 (msg_202a363e40014fM40DUcv4sCZd)

Let me check the board for prior "average depth" obstruction findings that may bear directly on this load question.

## Output 188 (msg_202a41d89001YeR1cVGSd5MOgm)

Let me examine the repository's "forced balanced prefix" analysis, which is directly relevant to load structure in near-tight optimal trees.

## Output 199 (msg_202a493f3001O6lxHiy5wD7Yhf)

Let me verify the existing solver reproduces the board values, then attempt the discriminating n=9 computation in the background.

## Output 230 (msg_202a6ea0a001iwlQOnmirlTrOZ)

The n=9 solver is running detached. Let me check its current progress once.

## Output 241 (msg_202a6f75d001lELoyAmqlyuJMC)

Let me check the n=9 job's progress once (it's been running while I analyzed the theory).

## Output 252 (msg_202a77933001KVQMAWdHO6lnhf)

Let me test a natural constructive route: greedy load-balancing restricted to optimal comparisons. This discriminates whether a simple potential strategy can achieve Λ(n).

## Output 270 (msg_202aa4c6d001TcRdBJjSqFH3r3)

Greedy load-balancing fails at n=8 even though Λ(8)=5. Let me extract the exact failing state and the unrestricted greedy load — a concrete failed approach.

## Output 306 (msg_202ab43b3001td6OiGpP88ziqa)

Let me test whether the greedy failure is robust across natural tie-breaking variants, strengthening the failed-approach result.

## Output 394 (msg_202ad1ef1001y5xsIJ87D6DUsq)

Let me verify the greedy stuck state is genuinely losing within the cap (not an artifact), using the exact game solver.

## Output 432 (msg_202add172001JWONxo9oh7GmWr)

Let me search for a sharp "no counting-only potential" witness: two reachable states with identical counting-style invariants but different load-game outcomes.

## Output 450 (msg_202aea3e9001ZR0a5zFdxtlBQD)

This is a strong no-go result. Let me extract an explicit minimal witness pair for the board report.

## Output 477 (msg_202af73dc001zCl6XBoWCEbBik)

I have a strong, independently checkable finding set. Let me write up the board post and submit it as my single external write.

## Output 531 (msg_202b06847001xRhPXV9wWxbxV9)

The board post is confirmed. Let me check the n=9 computation one final time.

## Output 551 (msg_202b09be90012pqG1fTQFLjLK9)

## Report — `per-key-load-additive-gap-alln` (billy-dev)

I studied `AGENTS.md`, `docs/problem.md`, `docs/literature.md`, the board #301 07:42Z per-key-load post, and the repo's related notes. I attacked the additive-gap claim with exact computation (scratch only) and paper analysis. **Neither horn is settled**, but I obtained one rigorous obstruction, one no-go theorem, and one concrete failed approach. No repository/Lean changes; my single external write is one #301 comment (confirmed posted, 09:57Z).

### 1. Exact obstruction — the additive reframing does not bypass the obstacle `[deduction]`

Fix `B(n,c)=ceil(2S(n)/n)+c`. "Gap ≤ c for all n" is exactly the statement that the **safety game** on states `(poset P, remaining load ℓ)` is won: Algorithm must choose an *optimal* comparison (`max child F = F(P)−1`) and decrements two loads; Adversary chooses the outcome; win means reaching `F=0` with all loads ≥ 0. This is a `∃∀` fixpoint, not a one-step potential: a pointwise "some low-load optimal comparison exists" lemma is necessary but **not sufficient**, because both children can be losing. So the additive-gap question and the board's `O(log n)` question are the *same* all-n anticipatory load-balancing lemma. Counting (`Σ load = 2S(n)` on a longest path) gives only `Λ(n) ≥ ceil(2S(n)/n)`; the additional fact that a worst path's comparison graph contains the sorted-adjacency Hamiltonian path adds no degree bound.

### 2. Counting-invariant no-go `[experiment, exact]`

At n=6, cap `L=4=Λ(6)`, two reachable states have **identical** counting-style invariants — `F=1`, `e(P)=2`, remaining-load multiset `(0,1,1,1,1,2)` — yet opposite game values:

- Winning: `succ=(34,0,51,51,35,2)`, unique incomparable pair `(2,3)`, loads `(1,1)`.
- Losing: `succ=(18,0,59,51,2,18)`, unique incomparable pair `(0,5)`, loads `(0,2)` — the zero-load key cannot be compared.

So `(F, #linear extensions, load multiset)` does not decide load-feasibility: **no counting-only potential can certify load-optimality**, independent of whether the gap is bounded. Mixed-invariant groups proliferate: 35 at n=6, 258 at n=7. This sharpens the front's complexity implication into an unconditional no-go for that invariant family.

### 3. Concrete failed approach — greedy load balancing `[experiment]`

Greedy among optimal comparisons (pick one minimizing the two keys' current max load) **fails at n=8 with cap Λ(8)=5** under all six natural tie-breaks. Explicit stuck state reachable under greedy: `succ=(254,252,136,128,236,204,136,0)`, loads `(2,5,4,4,3,5,5,2)`, `F=1`, `e=2`, unique incomparable pair `(2,6)` with key 6 already at cap; verified `G=False`. Unrestricted greedy uses max load 6 > Λ(8)=5. A winning strategy must be **anticipatory** (reserve capacity on keys needed for forced late comparisons), so no one-step greedy/potential proof works.

### Non-transfer and soundness `[deduction + literature]`

Kahn–Saks balanced pairs (`O(log e(P))` for arbitrary posets) and Hyafil–Rivest/Cardinal et al. give neither exact `S(n)` nor per-key load control; hardness for general posets/tests does not transfer to the fixed antichain root. Even an all-n `O(log n)` load normal form would be a **sound** structural restriction, not a polynomial-size **complete** NP/coNP certificate (`SORT-BOUND-U` trees still have exponentially many nodes); NP membership and the sparsity/Mahaney barrier are unchanged.

### Honest limits

- Neither the bounded-gap claim nor the unbounded-gap falsifier was proved; I found no potential beating counting.
- The n≤8 gaps `0,0,0,1,0,1,1` cannot settle all n. The n=9 search computed `S(9)=19` and all 183231 unlabelled 9-posets but the load-game search was incomplete; I stopped it rather than leave a runaway process, so **Λ(9) is not a result**.
- The decisive obstacle is unchanged: an all-n anticipatory load-balancing lemma. No new `S(n)`/`SORT-BOUND-U` theorem.

Verification artifacts are in `/tmp/opencode/` (`load_solver.py` reproduces Λ(2..8) exactly; `potential_witness.py`, `extract_witness.py`, `load_greedy*.py`). Worktree clean at `6a96398` on `billy-dev`.

## Output 572 (msg_202b0f8f2001WFXlw8MUWLPQic)

## Recovery check (no actions repeated)

Inspected git state, processes, and board #301. The previous turn’s effects already happened; I did **not** repost/commit/mutate anything.

- **Git**: `billy-dev` @ `6a96398`, working tree clean; no commits made by this front.
- **External post**: already present on Antonina #301 — `[2026-11-22T09:57:30.902Z] SoringP1 frontier: per-key-load-additive-gap-alln` (confirmed via board digest). Not duplicated.
- **Processes**: no `load_solver.py 9` running; I had stopped the incomplete n=9 run.
- **Artifacts**: scratch-only in `/tmp/opencode` (`load_solver.py`, `load_greedy*.py`, `potential_witness.py`, `extract_witness.py`, etc.).

**Completed finding (as reported):** additive-gap reframing does not bypass the anticipatory load-balancing obstacle; exact counting-invariant no-go (same `F,e,load` multiset, opposite `G` at n=6; 35/258 mixed groups at n=6/7); greedy load-balancing fails robustly at n=8, cap Λ(8)=5. Neither bounded-gap nor unbounded-gap horn proved; Λ(9) not computed. No new `S(n)`/`SORT-BOUND-U` theorem, no repo/Lean changes.
