# antonina-nSzgeMu7abByLSD2BSUtuL-torments

Session: ses_e08b16bc3ffepxVvvTNEdRlw0l
Workspace: /home/lubko/soring-fronts/greedy-ball-growth-exponent-alln
Created: 1795150484660; updated: 1795150879597

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f74e96940010ndPWIwACoFES4)

I'll start by understanding the repository structure and the specific context I'm working in.

## Output 17 (msg_1f74ea392001YfqfcnJCQes4i8)

Good, I'm on `billy-dev`. Let me read the key documents and find board #301.

## Output 45 (msg_1f74eb702001BJsmgpyCf0DQ5X)

Now let me check board #301 digest and the research frontier entry for this FRONT.

## Output 56 (msg_1f74ec4f0001cRL0PHxSznfjd5)

There's already related work on the board. Let me read the full posts and understand what's been done, to avoid repetition.

## Output 126 (msg_1f74fc7de001kAEMY1mXaiHN2n)

Let me examine the key research notes on the winning frontier and state compression, and check the scratch artifacts from earlier work.

## Output 141 (msg_1f75055ec0013CBCPfoC4Sdbzd)

There are scratch files from ~04:53–04:56, after the earlier post — likely from an interrupted run of this exact front. Let me inspect them to avoid repeating work.

## Output 187 (msg_1f7509e55001OgvfDQOSJz6cCd)

I now have a clear picture. Let me examine the earlier board audit trail to confirm no prior post by my exact front, then verify a key mathematical idea computationally.

## Output 198 (msg_1f75304de001Sq6pqyDshrAhTK)

No prior posts by my exact front. Now let me verify the key mathematical idea: in the adversarial-tie model, the greedy ball is relabelling-closed and contains all total orders.

## Output 216 (msg_1f7537c5f001bJl1uRKl2xenuF)

The computation confirms the theorem. Let me verify how the greedy adversary and ties are defined in the repo docs, to be sure about the model.

## Output 234 (msg_1f753e127001sI4ZqUb6q8lkdH)

Let me confirm the posting mechanism used previously and the exact log asymptotics.

## Output 252 (msg_1f7541261001QYRq2K6ig9npOd)

The math is verified. Let me write the concise board finding (scratch file only), then post it.

## Output 272 (msg_1f7546140001c4mWyFMFWOX11y)

The post succeeded. Let me verify it's on the board.

## Output 292 (msg_1f7547f3c001fQpxdPTvFo8ACq)

## Finding

I attacked the FRONT's falsifier question for `|R_{G(n)}(n)|` and established the **2^{Ω(n log n)} lower-bound direction**, refuting the `2^{O(n)}` upper bound in the natural (adversarial-tie) model. Worktree is clean; no Lean/repo/ledger changes; one concise board post on #301.

### The theorem (paper proof + computational check)

In the model in which `G(n)` is actually defined — greedy adversary, **ties broken adversarially** (both children of an extension-count tie are legal) — for every `n ≥ 2`:

`|R_{G(n)}(n)| ≥ n! = 2^{Θ(n log n)}`.

Proof:
1. **Equivariance.** `e(P)` is relabelling-invariant, so a greedy transition `P→Q` holds iff `π(P)→π(Q)` holds. The antichain is `Sₙ`-fixed, hence the reachable ball is a union of isomorphism classes.
2. **Termination.** By definition of `G(n)` some sorter strategy reaches a total order `T` within `G(n)` greedy steps. Relabelling closure then puts **all `n!` total orders** in the ball.
3. Distinct total orders are distinct labelled posets; Stirling gives `2^{n log₂ n − O(n)}`.

This does **not** assume `G(n)=S(n)`.

**Independent scratch verification** (both tie children; G by backward minimax): `n=2..6` gave `G=1,3,5,7,10`, `|B|=3,19,219,4231,130023`, with exactly `n!` total orders in each ball. Relabelling closure checked on samples.

### Critical model distinction

The cited counts `2,11,143,3362,119118` come from a **deterministic tie-break**, a different/smaller object. There the `n!` argument fails — at `n=2` the ball is `{antichain, 0<1}`, only 1 of 2 total orders — so the deterministic-tie exponent remains open. I treated the adversarial-tie model as the intended one because that is how `G(n)` and ties are defined in the ledger/board.

### Honest limits

- Enumeration/counting obstruction only — **not** a time lower bound; says nothing about certificate **soundness vs completeness**.
- Combined with the trivial `|R| ≤ 2^{O(n log² n)}`, the exponent sits in `[n log₂ n − O(n), O(n log² n)]`; the exact constant is **not** pinned here.
- No class separation, no new `S(n)` value, no `G(n)=S(n)` claim. General-poset `#P` hardness is irrelevant (proof uses only relabelling invariance of `e`).
- Web literature search was unavailable this pass; grounding is repo board/ledger. The relabelling idea parallels the known "~2n! labelled states in one optimal tree" observation, here applied to the greedy-reachable ball (predecessor had only `2^{⌊n/2⌋}`); I did not manufacture a stronger claim than the proof supports.
