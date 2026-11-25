# antonina-EhH2eegHH4igoJnQyuzkjs-construct

Session: ses_e05c46132ffepb9MGSR08SfOrd
Workspace: /home/lubko/soring-fronts/antichain-reachable-power2-halving-obstruction
Created: 1795199573828; updated: 1795200496848

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1fa3ba214001B063wweeQoUTiI)

I'll start by understanding the repository state, the "billy-dev" branch context, and the key documents.

## Output 17 (msg_1fa3bb079001IVaIVbI0x2d1N3)

I'm on `billy-dev` with a clean tree. Let me read the key documents and find board #301.

## Output 32 (msg_1fa3bbb4f001U00xKGFVneoDH8)

Now let me read operations.md to understand the board, and search for board #301.

## Output 47 (msg_1fa3bc47e001qU6MlTtipaH7ud)

Let me get the board digest and read my specific front from the ledger/frontier.

## Output 62 (msg_1fa3c020b001Tx4HuW2U4ipHgG)

Let me search the board for the specific concepts in my front: halving obstruction, power-of-two e(P), reachability window, one-bit-slack, sibling budget.

## Output 73 (msg_1fa3c95030018PsjsQru7ObJi9)

Let me examine the board tool and the key research docs about the obstruction, excess boundedness, and one-bit slack.

## Output 92 (msg_1fa3ca8890010SnO8fNCdojKxU)

Let me find the "one-bit-slack recurrence", "realizability window", and "height-C tree" documents, and read the excess-boundedness research note.

## Output 107 (msg_1fa3cd8f70019vTGeuak3qaCVg)

Let me search the full board across pages for the specific notes referenced (one-bit slack recurrence, realizability window, height-C trees).

## Output 118 (msg_1fa3d6185001BEiQ2v6ELaekNq)

Let me fetch the full bodies of the specific referenced notes: "one-bit slack" recurrence and "realizability window".

## Output 129 (msg_1fa3dae170019TopsFCkwm3qcD)

Let me find and read the realizability-window note and check the notes directory.

## Output 156 (msg_1fa3e1d85001VzMXO37N6KQxna)

Let me read the realizability-window note from a couple of relevant worktrees.

## Output 171 (msg_1fa3e3967001nJpbliIsJxJNZn)

Let me read the full recent board posts that define the "ceiling-loss identity" and "propagation lemma" (one-bit slack) to understand the intended test.

## Output 182 (msg_1fa3ea4e2001euGVNJjOAaBDYl)

I now have the full context. Let me set up an independent exact computation in scratch space (no repo changes) to test the reachability claim for powers-of-two states.

## Output 245 (msg_1fa41eaee001EdJUxVWZ3wz7M3)

Q is exactly the obstruction: e=8, no halving pair, F=4>3. Now I must independently verify reachability with the full joint-child sibling budget.

## Output 272 (msg_1fa427217001AsqamJBj6JWneM)

The n=6 computation produced many power-of-two obstruction states. I need to verify this independently and carefully before trusting it. Let me write a from-scratch verifier with a different representation.

## Output 290 (msg_1fa44a21100164DUIl2wPoyltQ)

The n=6 witness is fully verified by an independent implementation. Let me verify the window statistics and the "steep ceiling drop" mechanism in detail.

## Output 301 (msg_1fa44e983001CnWwGpyjaHfyYm)

I have a fully verified n=6 counterexample. Let me also confirm the n=7 witness reachability via the published explicit path, as an independent second witness.

## Output 321 (msg_1fa483ccc001XXWD0lLzgodP5p)

Let me produce a complete split profile for the n=6 witness and double-check the sibling budget arithmetic one final time.

## Output 332 (msg_1fa48881e001bgsf4BLyqasrS3)

Let me do a final duplication check on the board before posting.

## Output 343 (msg_1fa48c4050012aLIit67tsnlTC)

There are very recent posts on closely related topics. Let me read them fully to distinguish general-poset results from my reachability finding.

## Output 354 (msg_1fa48e66d001rcB2QWKJ3P5N9Q)

I have a decisive, independently verified counterexample that exactly answers the open reachability front flagged by the two recent general-poset posts. Let me check the board posting interface.

## Output 372 (msg_1fa491515001fIh24aQmLQbDxe)

I have a decisive finding. Let me write the board report and post it to #301.

## Output 390 (msg_1fa4975e8001ku1nT5mYOamvpz)

The post succeeded (visible at 18:47:57Z). Let me confirm the worktree remains clean, as required.

## Output 401 (msg_1fa4991a0001xTxYq4kjCyllJT)

Worktree clean on `billy-dev` at `6a96398`; the only external side effect is one board post to #301 (18:47:57Z). All computation was scratch in `/tmp/opencode/p2halving`.

## Mathematical finding

**The front's "always exclude" hypothesis is false.** A poset with `e(P)` a power of two, no exact-halving continuation, and `F(P) > log2 e(P)` **does** occur on a height-`S(n)` optimal play from the antichain — already at `n = 6`, which is information-tight (`S(6)=C(6)=10`). The reachability window is decisive at `n=5` but is **not** a universal filter.

### Fully verified witness `W6` (n=6)
Successor masks `(0,17,1,19,0,5)`; relations `{(1,0),(1,4),(2,0),(3,0),(3,1),(3,4),(5,0),(5,2)}`.
- `e = 16 = 2^4` (brute force over all 720 permutations), `b=4`.
- `F = 5` (independent memoized minimax with a separate Warshall closure), so `eps = 1 > 0`.
- The 7 incomparable pairs split `e` as `(6,10),(10,6),(4,12),(2,14),(12,4),(9,7),(1,15)` — **no (8,8) split**, hence no exact-halving continuation. (This is exactly the primitive obstruction of the 18:45Z general-poset post, now shown reachable.)
- `covers=5`, `pi=1`.

### Genuine reachability with the joint-child sibling budget
Explicit path from `A_6`: `(0,1) j<i`, `(2,5) j<i`, `(0,2) j<i`, `(1,3) j<i`, `(1,4) i<j`. At depths `0–4` both children fit the remaining budget (`(9,9),(8,8),(7,7),(7,7),(5,5)` vs budgets `9,8,7,7,5`). At depth `5` the state is `W6` with remaining budget `5 = F(W6)`, so the minimax subtree below it is a height-5 strategy.

### Window test
`covers=5 ≤ d=5 ≤ S(6)−max(F,pi)=10−5=5` — the interval is the singleton `{5}` and is satisfied with equality. So the window is necessary but does **not** exclude the obstruction; the positive exclusion route is refuted.

### Mechanism and dependence
The ceiling-loss profile is `pi=1,1,1,1,2` (`b: 10→9→8→7→6→4`); the last step drops `b` by 2 (`e 36→16`), a negative signed-loss subsidy. With `D(6)=0`, `eps(W6)=0−(−1)=1`. So local non-tightness arises at an information-tight root via one steep step — the signed-ceiling-loss phenomenon. **The answer does not depend on `S(n)=C(n)`**: `n=6` is tight and admits the witness. At `n=5` (also tight) the analogous `e=8` obstruction has `covers=5 > S(5)−F=3`, so it is excluded — the filter is size-dependent, not universal.

## Honest limits
- Finite counterexample only (`n=6` fully verified; a second `n=7` witness `Q=(0,1,3,3,7,15,31)` — `e=8, F=4, no halving, covers=8, pi=2` — had its properties independently re-verified, but its reachability path is cited from prior independent work, not re-run here). No all-`n` reachability family is proved (an ordinal-sum embedding `P6 ⊕ C_t` is plausible but needs a separate sibling-budget induction, not attempted).
- This closes the proposed power-of-two tight-subproblem pruning rule and places the obstruction inside the root game. It yields **no** new value of `S(n)`, no speed-up for exact evaluation, and no P/NP/PSPACE consequence (per `docs/problem.md`). The 18:43Z/18:45Z results are general-poset results and do not transfer to `S(n)` without exactly this reachability argument.

I did not create any Lean, note, test, or repository changes — a clean worktree is the correct outcome here.
