# antonina-z7trIOqKTxPrysmtJePd0m-chairman

Session: ses_e436921d2ffecpHjlWu6qS6vGD
Workspace: /home/lubko/soring-fronts/curator
Created: 1794165366345; updated: 1794166255244

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 519 (msg_1bca32f4b001A56sQG8xY0vC1g)

I studied `AGENTS.md`, `docs/problem.md`, the board digest for #301 (pages 1–2), the ledger, and the relevant notes (`one-ply-obstruction`, `counting-oracle` history, `research-plan`, `upper-bound`). I made no Lean or repository changes. The only new file is the required curator output.

## Claim attacked: constant-depth extension-count lookahead at the antichain

Define

- `L_0(P) = ceil(log2 e(P))`
- `L_{t+1}(P) = 0` if `P` is total, else `1 + min_{x||y} max(L_t(P+x<y), L_t(P+y<x))`.

So `L_t <= F`, and `L_t(P) <= L_0(P)+t`. The precise all-`n` claim was:

> There is an absolute constant `t` with `L_t(A_n) = S(n)` for every `n`.

What I established or checked:

- **Deduction:** `L_1(A_n) = ceil(log2 n!)` for `n >= 2`, since `n!` is even and `ceil(log2(n!/2)) = ceil(log2 n) - 1`. So one ply is useless at the root.
- **Computation:** `L_2(A_12) = 29 < 30 = S(12)`. Hence the convergence depth at `n=12` is at least `3`. My `L_3(A_12)` run did not finish in this turn.
- **Key consequence:** if such a finite `t` existed, then `S(n) <= ceil(log2 n!)+t`, and, more importantly, `S(n)` would be computable in polynomial time: a depth-`t` state is the union of a poset on at most `2t` touched elements with an antichain, so its extension count is `e(P_0) * n!/r!` for `r <= 2t`. The recursion then has `(n^2)^t` nodes, polynomial for fixed `t`.
- **Barrier:** the known general-poset fence theorem gives `d(W_n)=Omega(n)`, but that is about arbitrary posets, not reachable antichain-optimal states. It does **not** transfer to `A_n`.
- **Honest limit:** I neither proved nor disproved bounded lookahead at the antichain. Unbounded excess `S(n)-ceil(log2 n!)` would disprove it, but that is itself open.

I also ran independent small exact checks on fixed-seed defects `D_Q(n)=S(n)-F(Q ⊔ A_{n-|Q|})`:

- `D_{C_2}(n)=1` (matches the board’s `t=1` lemma);
- `D_{C_3}(3..7)=3,3,2,2,3`;
- `D_{C_4}(4..6)=5,4,4`;
- `V` and `L` seeds: `2,2,1,1`;
- diamond seed: `4,3,3`.

The `C_3` sequence does **not** yet show a plateau, so eventual constancy is questionable; boundedness remains open.

I also tested the binomial strengthening `S(a+b) >= S(a)+S(b)+floor(log2 C(a+b,a))-1` against every pair of published exact values `n <= 22`. It held for all pairs, with minimum margin exactly `-1`, achieved at `(3,17)`, `(4,16)`, `(6,14)`, and others. This is finite evidence, not a proof; the weaker `S(a+b) >= S(a)+S(b)` has a plausible independent block-adversary argument, but I did not formalize it.

None of this yields certificate completeness: `L_t` is a lower-bound hierarchy and the superadditivity inequality is a value inequality. General-poset hardness and local-gap results do not automatically transfer to the antichain root.

## Curator output

I wrote three nonduplicate, all-`n` falsifiable fronts to `frontier-candidates.json`:

1. `antichain-lookahead-depth` — constant-depth count lookahead at `A_n`; a positive answer would put `S_unary` in FP.
2. `fixed-pattern-defect-bound` — boundedness of `S(n)-F(Q ⊔ A_{n-|Q|})` for each fixed seed `Q`.
3. `binomial-superadditivity-defect` — a new one-bit-slack lower bound quantifying the cost of merging two unordered blocks.

The file is valid JSON, all schema length constraints hold, and none of the IDs collide with the durable ledger. No board post was made and no commit was created.

## Output 605 (msg_1bca441f2001XUlTA7dEa4u6Mb)

Inspected the workspace, Git state, board, and durable ledger before doing anything.

## Effects that actually happened

- **`frontier-candidates.json` exists and is the only working-tree change.** It is untracked, 3,060 bytes, valid JSON, containing exactly the three candidates:
  - `antichain-lookahead-depth`
  - `fixed-pattern-defect-bound`
  - `binomial-superadditivity-defect`
- **No commit was created.** `git log` is still at `6a96398`, and `git status --short` shows only `?? frontier-candidates.json`.
- **No board post was made.** The #301 digest has no comment from this curator turn and none of the three candidate IDs appear on the board.
- **No candidate was imported into the ledger.** None of the three IDs occur in `frontier-ledger.json`; the ledger’s only running entry is the unrelated `gpc-dimension-three-threshold`.
- **No Lean files, notes, branches, or PRs were created or modified.**

## Unfinished work

There is no unfinished external or repository action from the previous turn. The required deliverable is present and valid. The ledger transition/import of these candidates belongs to the keeper after this curator session exits.

The only incomplete item was a non-required local `L_3(A_12)` computation that was interrupted; it is a scratch calculation, not an external effect, and does not need to be repeated.

No duplicates were created. No uncertain external effect remains.
