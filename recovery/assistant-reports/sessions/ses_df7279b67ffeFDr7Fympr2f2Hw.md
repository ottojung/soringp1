# antonina-9Nb3jTJ2d04ikJqPIrwIbs-embrace

Session: ses_df7279b67ffeFDr7Fympr2f2Hw
Workspace: /home/lubko/soring-fronts/oneply-flatness-certificate-gap-alln
Created: 1795444729057; updated: 1795446557732

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 13 (msg_208dfd43d001jSjw9AqbvF1h9O)

I'll start by carefully inspecting the current state — git branch, working directory, and existing durable records — before doing anything, since a previous turn may have performed side effects.

## Output 28 (msg_208dfe138001OTWWHEX1VmEcsp)

Good — I'm on `billy-dev`, clean worktree. Now let me read the key documents and look for durable task records from the interrupted turn.

## Output 47 (msg_208dff7ae0012FrN0C55vDK7z3)

Let me read the one-ply obstruction doc, the frontier ledger (durable task record), and check the board digest for #301.

## Output 66 (msg_208e00ad3001nJ7ZzBDQpxjC9g)

Let me find the specific ledger entry for this front and get the board digest with valid parameters.

## Output 81 (msg_208e02dcc001ZCdFhoeZ3G0SYp)

Let me locate the exact ledger entry for this front and the specific board posts on `g` at 14:05Z/14:19Z.

## Output 96 (msg_208e04f35001nacif48kvkWov2)

I found the exact ledger entry: `oneply-flatness-certificate-gap-alln`, status `running`, agent `9Nb3jTJ2d04ikJqPIrwIbs-embrace`, with an **empty** finding. So no result has been recorded. Now let me check the board for any prior post from this front (to avoid duplication) and read the referenced 14:05Z/14:19Z posts on `g`.

## Output 107 (msg_208e06737001cAtUsHNk3KfCXt)

Let me fetch the board JSON locally (to a temp file) so I can search all posts for this front and the referenced 14:05Z/14:19Z `g` posts without flooding context.

## Output 136 (msg_208e0ae170015zNS0O9GvzckXp)

I now have the full picture. Let me note the key facts established so far before deeper work:

**Side-effect audit (recovery):**
- On `billy-dev`, worktree clean, no commits from this session.
- Ledger entry `oneply-flatness-certificate-gap-alln` is `running` with an **empty** finding — no result recorded.
- Board #301: no prior post from this front; the 14:05Z/14:19Z posts are the `g` referee report and the sharp-necessary-condition theorem (which I've now read).

So there is nothing to undo. I'll continue the unfinished mathematical work. Let me first verify the definitions and the front's example computationally in scratch space.

## Output 154 (msg_208e25ac9001Bzzi7h7l2PCS5z)

This is a promising direction. I found **flat-but-defective states reachable at n=6** (a tight n), e.g. `(2,0,3,0,0,0)` at depth 2 with `e=120, L0=L1=7, F=8` and `d+F=10=S(6)`. But I must check the stronger, correct notion of reachability: a state lies on a height-`S(n)` tree only if every move on the path is `S(n)`-safe (at slack 0, F-optimal). Let me compute that.

## Output 272 (msg_208f3d9cf001zis4EE0fE4eP8S)

## Recovery / side-effect audit (billy-dev)

- **Host/worktree**: on `billy-dev`, `/home/lubko/soring-fronts/oneply-flatness-certificate-gap-alln`, branch `billy-dev`, clean (`git status --short` empty, HEAD `6a96398`).
- **Durable records inspected**: `~/.local/state/soringp1/frontier-ledger.json` shows `oneply-flatness-certificate-gap-alln` as `running` (agent `9Nb3jTJ2d04ikJqPIrwIbs-embrace`, empty finding). I inspected #301 board (page 1 JSON) and found no prior post for this front.
- **External side effects from this session**: no commits/PRs/repo changes. I created scratch files only under `/tmp/opencode` (`oneply_check.py`, `optreach.py`, `optreach2.py`, etc.) and ran local computations. I posted **exactly one** #301 comment as `SoringP1 frontier: oneply-flatness-certificate-gap-alln` (2026-11-23T15:08:25.784Z, id `sha256:nBsgNtXUnI_qZJBvpLA_2NB8Nwtot3Z7gTQj8920ZvU`). I did not repeat any post.

## Mathematical finding (paper proof, [deduction])

Model as in `docs/problem.md` / `docs/research-one-ply-obstruction.md`: finite poset `P`, `e(P)` linear extensions, `F(P)` minimax comparisons, `L0(P)=ceil(log2 e(P))`, `L1(P)=0` if total else `1 + min_{i~j} max(L0(P+i<j), L0(P+j<i))`, and `L0<=L1<=F`. The sound predicate `g(P)` (balanced split by `e<=2^(L(P)-1)` recursively) implies `F=L0` and `L1=L0`.

### 1) Root obstruction (unconditional)

For the antichain `A_n` (`n>=2`), every incomparable pair splits `n!` extensions equally into `n!/2, n!/2`. Therefore
`L0(child)=ceil(log2(n!/2)) = ceil(log2 n!) - 1 = C(n)-1`, so
`L1(A_n)=1 + C(n)-1 = C(n)=L0(A_n)`.
`A_n` is on every height-`S(n)` optimal play.

Hence **L1-flatness fails to certify defect-freeness or `g`-certifiability at `A_n` whenever `D(n)=S(n)-C(n)>0`**: `L1=L0=C(n)` but `F=S(n)>C(n)`, and `g(A_n)` is false because `g => F=L0`.

Using established exact values ([literature], Wells/Peczarski/Stober–Weiß as recorded in `docs/literature.md`): `D(n)=1` for `n in {12,13,14,15,16,17,18,19,22}`. Explicit optimal-play witnesses: `A_12,...,A_19,A_22`. Example: `n=12`, `e=479001600`, `L0=L1=29`, `F=S(12)=30`.

### 2) Infinitely-many-`n` status (open)

- The “infinitely many `n`” failure horn holds **conditionally if** `D(n)>0` for infinitely many `n`; this is open.
- The falsifier horn “for all large `n` every L1-flat state on optimal antichain play is `g`-certifiable and defect-free” would imply `D(n)=0` for all large `n` by applying it to `A_n` — at least as hard as the open asymptotic gap question. I did not settle either horn unconditionally.

## Small-n optimal-play experiment ([experiment], scratch, exhaustive n<=6)

I enumerated states reachable from `A_n` by F-optimal comparisons (both children of any pair with `1+max(F child)=F(P)`, i.e. height-`S(n)` optimal-play states): `n=4: 181 reachable, 0 L1-flat&defective; n=5: 1551, 0; n=6: 65551, 0`.

The 2280 weakly budget-reachable (`d+F<=S`) L1-flat&defective `n=6` states are **not** F-optimal-reachable. Representative: `C3 ⊔ A3`, succ `(6,4,0,0,0,0)`, `e=120, L0=L1=7, F=8`, reached by a comparison at `(2,0,0,0,0,0)` whose two children are `F=8` and `F=9`, so `1+max=10 > F(parent)=9` (non-F-optimal move).

## Obstruction / limits

- **Sound but not complete on optimal play**: `L1` is a cheap sound lower bound, but it cannot certify defect-freeness/g at known gap roots because antichain symmetry makes the first ply information-balanced while minimax can be defective. A complete local certificate must separate “balanced in `e`” from “balanced in `F`” on optimal-play states — exactly the defect/minimax gap.
- I did **not** find a non-root L1-flat defective F-optimal-reachable state for `n<=6`, and I did **not** construct an infinite non-root family. The root family gives unconditional finite witnesses and a clean conditional/obstruction answer to the “infinitely many `n`” question.
- No complexity-class separation is claimed. No Lean/repo changes were made; the result is a paper/experimental obstruction, not a kernel-checked theorem.
