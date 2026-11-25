# antonina-sGoK59sp29C76nsT95SMt0-tiresome

Session: ses_e040add66ffetJN7TGN4N22M2Y
Workspace: /home/lubko/soring-fronts/excess-at-most-one-alln
Created: 1795228508905; updated: 1795229549505

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1fbf52492001B9US99Z8rqu7WU)

I'll start by studying the contract docs and the current board state, then dig into the literature and attack the front.

## Output 38 (msg_1fbf76b43001Zp4KS7ylCLDBFs)

I'm on billy-dev as required. Now let me read the research board #301 digest and the ledger entry for this front.

## Output 109 (msg_1fbfafae90013deYDUpVrOEx2C)

Now I have the full front spec. Let me check the running agents, verify the user's excess table with exact integer arithmetic, search the board efficiently (parallel page fetches), and check the Antonina CLI for posting.

## Output 132 (msg_1fbfd9ab3001mEjHQCPE6rWE1f)

The ledger shows a near-duplicate front `single-bit-excess-dichotomy` ("S(n) ≤ ceil(log2 n!)+1", status investigated). I need its finding — that's on board #301. Let me debug the board fetch.

## Output 168 (msg_1fbff0b8b001M1XXiTvrMlEuqz)

Board fetched. Web search is unavailable right now — I'll use direct URL fetches for the primary sources. First, search the board for prior posts on this front and the adjacent `single-bit-excess-dichotomy` front.

## Output 200 (msg_1fbffdf13001iFdsUn8thcNzQa)

The board search surfaced rich context. Key facts so far: my front (`excess-at-most-one-alln`) duplicates the adjacent `single-bit-excess-dichotomy` front (same claim "E(n)∈{0,1}"), whose finding says no counterexample is certified and the split-merge class is ruled out at n=25. Now let me fetch the primary literature (Stober–Weiß, Peczarski, OEIS tables) and compute the Ford–Johnson vs counting table.

## Output 227 (msg_1fc010a410017gtlBLRd2GXSZY)

Excellent — OEIS A003070 confirms the counting bound values (C(23)=75, C(25)=84) and A036604 the S values. Now let me read the two most relevant prior findings in full: `single-bit-excess-dichotomy` (the adjacent duplicate front) and `excess-constant-bounded-alln`.

## Output 242 (msg_1fc0271f9001h6zjCthyFxB34h)

I now have a complete picture of this front and its adjacent sibling. Let me compose the research finding and post it to board #301 as the contract requires ("post only when something changed: a result, a falsification, or a precise obstacle").

## Output 262 (msg_1fc04051d0018cRpxatC8q3FY8)

The finding is posted to board #301 (2026-11-21T02:51:10Z, author `SoringP1 frontier: excess-at-most-one-alln`). Here is the report.

## Claim attacked

**e(n) = S(n) − ⌈log₂ n!⌉ ≤ 1 for all n ≥ 2** (equivalently S(n) ≤ ⌈log₂ n!⌉ + 1; the antichain-root minimax value m(A_n) = S(n), C(n) = the information lower bound).

## Verified data (experiment; OEIS A036604/A003070, literature)

Using exact integer arithmetic on the certified tables:
- e(n) = 0 on {2..11, 20, 21}; e(n) = 1 on {12..19, 22} (e.g. S(12)=30, C(12)=29; S(19)=58, C(19)=57; S(20)=62=C(20); S(21)=66=C(21); S(22)=71, C(22)=70).
- e(24) ≤ 1 by **deduction**: FJ(24)=81=C(24)+1 and S(24) ≤ FJ(24).
- Ford–Johnson excess FJ(n)−C(n): =1 at {23,24,40,41,42,43}; **first 2 at n=25** (C(25)=84, FJ(25)=86); 3 at n=28 (C=98, FJ=101) and 46–47 (C=192/198, FJ=195/201); 13 at 122.
- Stober–Weiss 2022 (arXiv:2206.05597): S(16)=46, S(17)=50, S(18)=54; **S(28) ≥ 99 = C(28)+1**. Manacher 1979 (per board): FJ(n) > S(n) infinitely often, first at n=47.

## Falsification status — no falsifier found

No certified S(n) ≥ C(n)+2 exists in the certified data; the maximum certified excess is 1. The FJ(25)=86=C+2 instances are **upper bounds**: S(25) ∈ {84, 85, 86} is uncertified, and there is no certified lower bound above 84. (At n=24 the claim is automatic by deduction.)

## Exact obstruction

A counterexample requires a *certified lower bound above C(n)*. Concrete failed approaches:
1. **Certified-data scan**: max certified excess = 1 through 22 + S(28) ≥ 99.
2. **FJ-excess route**: FJ−C = 2 at n=25..27 — but S ≤ FJ, and S(25) ∈ {84,85,86}; splitting/merge-based routes to those heights are ruled out at 25 (Peczarski 2007), a class-restricted counterexample only.
3. **Counting-family route**: flatness L_t(A_n) = C(n) for all t ≤ n/2 — no standard extension-count/lookahead family certifies C+2 at the root.
4. **General-poset → root transfer**: excesses F(P) − ⌈log₂ e(P)⌉ are large/unbounded on some posets (ordinal-sum families etc.), but local gaps on reachable posets do not certify the antichain root; conversely certificate *soundness* (local L0/L1 rules, valid witness rules) is not *completeness* for the global predicate S(n) ≤ k — so sound local objects are not falsifiers of the all-n claim either.

**Credible windows for a certified falsifier**: n = 25 (S(25) = 86 since 84 ≤ S ≤ 86) and n = 47 (S(47) ∈ {198,199,200}; S(47) = 200 or 201 would be the first).

## Honest limits

- S(23) is open per the ledger (exec-s23-search-window-20261121): 75/76, so e(23) ∈ {0,1} — not a falsifier.
- S(25) is uncertified; FJ(25)=86=C+2 is only an upper-bound window.
- User-suggested next step: a computer-assisted minimax enumeration over n ∈ [23, 30] — but reproducing S(23) is a flagship search, and even with S(23)=76 the front stands (e ≤ 1).

**Conclusion**: the claim is unrefuted; it is consistent with all certified data (max excess 1, plus S(28) ≥ C+1). No Lean or repository changes were made (no new independently checkable theorem or counterexample). This front also duplicates the investigated adjacent front `single-bit-excess-dichotomy`, which found the same obstruction class.

## Output 300 (msg_1fc04e068001AE3BoZTyKVA6KH)

Recovery inspection results:

- **Git state**: worktree clean at `6a96398`; no commits, no modified/tracked files, no untracked files. No repository or Lean changes were made.
- **Board #301 (live)**: the finding post from 2026-11-21T02:51:10.661Z by `SoringP1 frontier: excess-at-most-one-alln` exists and is **single** (the most recent item; not duplicated). The earlier local `/tmp/opencode/board/` cache simply predates the post, which is why it shows 0 matches.
- **Ledger**: `excess-at-most-one-alln` is still `running` with `exit_state=None` — expected while the agent is active; the keeper owns the `running → investigated/blocked` transition on exit. I did not edit the ledger.
- **Scratch only**: all computations (e-table, FJ−C arithmetic) and literature reads were under `/tmp/opencode/`; nothing was written to the repo.

**Unfinished work**: none. The deliverable (a board report of the mathematical finding, failed disproof attempts, and exact obstruction) was posted once and verified. I am not repeating the post, not editing the ledger, and not creating repository changes.

**Summary of the finding reported** (full text is on #301):
- Claim: e(n) = S(n) − ⌈log₂ n!⌉ ≤ 1 for all n ≥ 2.
- Verified data (OEIS A036604/A003070 + literature): e = 0 on {2..11, 20, 21}; e = 1 on {12..19, 22}; e(23) ∈ {0,1}; e(24) ≤ 1 by deduction (FJ(24)=81=C(24)+1); FJ−C first reaches 2 at n=25, 3 at 28/46–47.
- No falsifier: no certified S(n) ≥ C(n)+2 exists (max certified excess = 1; S(28) ≥ 99 = C+1). FJ(25)=86=C+2 is an upper-bound window only (S(25) ∈ {84,85,86}).
- Exact obstruction: a counterexample needs a certified lower bound above C(n); general-poset excesses do not transfer to the antichain root; standard counting families cap the root at C(n) (flatness L_t(A_n)=C(n) for t≤n/2); sound local certificates are not complete for S(n) ≤ k.
- Honest limits: S(23) open (75/76); S(25) uncertified; next step is the user-suggested computer-assisted minimax over n ∈ [23, 30], which would not by itself produce a falsifier.
- Duplicates the investigated adjacent front `single-bit-excess-dichotomy`; no Lean/repo change (no new theorem or counterexample).
