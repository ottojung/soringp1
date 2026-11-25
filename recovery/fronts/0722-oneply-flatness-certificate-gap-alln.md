# oneply-flatness-certificate-gap-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

9Nb3jTJ2d04ikJqPIrwIbs-embrace

## exit_state

clearexit

## question

The one-ply bound obeys L0 <= L1 <= F and the sound predicate g implies root flatness L1(P)=L0(P). Does root flatness fail to certify defect-freeness or g-certifiability on states reachable along height-S(n) optimal play for infinitely many n? My independent n<=6 enumeration found 10050 general posets that are L1-flat but not g-certifiable, e.g. succ=(38,0,2,16,0,2) with e=30, L0=L1=5, F=6.

## basis

docs/research-one-ply-obstruction.md (L0<=L1<=F) and #301 14:05Z/14:19Z on g; my independent exhaustive n<=6 computation found the 10050 witnesses above, which are finite general-poset facts, not antichain-reachable or all-n.

## falsifier

Show that for all large n every L1-flat state on optimal antichain play is g-certifiable and defect-free, or exhibit an infinite family of reachable optimal-play states with L1(P)=L0(P) but F(P)>L0(P) or g(P)=false.

## implication

Determines whether the cheap one-ply lower bound can serve as a sound and complete local certificate for exact minimax on states relevant to S(n); a negative answer is a barrier to L1-based certified evaluation and uniform small-e pruning.

## finding_unverified

 effects from this session**: no commits/PRs/repo changes. I created scratch files only under `/tmp/opencode` (`oneply_check.py`, `optreach.py`, `optreach2.py`, etc.) and ran local computations. I posted **exactly one** #301 comment as `SoringP1 frontier: oneply-flatness-certificate-gap-alln` (2026-11-23T15:08:25.784Z, id `sha256:nBsgNtXUnI_qZJBvpLA_2NB8Nwtot3Z7gTQj8920ZvU`). I did not repeat any post.

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

## Other metadata

```json
{
  "finished_at": 1795446584.337944,
  "started_at": 1795444728.6229184
}
```
