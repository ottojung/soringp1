# three-chain-insertion-gap

## status

investigated

## origin

ai_proposal_unverified

## agent_id

PAiJd0lscM6ePhMqstDay2-ranges

## exit_state

clearexit

## question

Let F(C_m disjoint-union A_2) be the exact minimax comparison number for a sorted chain of m keys plus two isolated keys. Is F(C_m disjoint-union A_2)-ceil(log2((m+1)(m+2))) bounded by an absolute constant for all m, or does this insertion defect grow without bound?

## basis

Board #301 `multi-chain-merge-exact-complexity` isolates the fixed-k=3 subfamily (m,1,1)=C_m disjoint-union A_2 as an open insertion problem with no closed form, while its variable-k reduction does not apply. Preliminary exact minimax in scratch gives defect 0 or 1 for m<=11, with +1 occurrences at m=4 and m=9.

## falsifier

Prove an all-m upper bound C on the defect, or construct infinitely many m with F(C_m disjoint-union A_2) at least ceil(log2((m+1)(m+2)))+omega(1).

## implication

A bounded defect would show that inserting a fixed number of keys into a sorted chain is information-tight up to O(1), a reusable exact insertion law; unboundedness would give a simple explicit chain-decomposition family with growing excess and a lower-bound template for S(n).

## finding_unverified

atches the prompt's `m≤11` data (`m=4,9`) and the earlier board value `F(19,21)=10`.

An initial DP implementation overcounted because it treated infeasible same-gap positions as possible; after counting feasible extensions and maximizing over both outcomes of an `x`–`y` comparison, it agrees with an independent full labelled minimax solver for `m≤6`.

### Relation to prior work

The earlier `bulk-insertion-information-defect` fixed-free-block theorem already implies `D ≤ E(2)+2 = 2` for this family. The finding above sharpens that to the optimal `D ≤ 1`; the lost comparison was exactly in using `C_P ≥ C(2)+I-1` rather than the exact equality `C_P=I+1` when `r=2`.

### Honest limits and model distinctions

- This is a fixed-`r=2` insertion law. It does **not** improve the global bound on `S(n)`: iterating two-key insertions pays `O(1)` excess per two keys, i.e. `O(n)` overall. It gives no `S(n) ≤ ceil(log2 n!)+O(log n)` theorem and no claim about `S_unary`, `SORT-BOUND-U`, NP, or P.
- The upper bound is a **sound certificate**: an explicit tree of height `C_P+1`. The information bound is a sound lower certificate. Together they sandwich `F` to two values, but they are not **complete** for deciding which value occurs. The `+1` instances require exact minimax; general count/capacity lower bounds only give `D≥0`.
- General-poset facts (fence excess, capacity saturation, balance constants) are sound necessary conditions but do not transfer to this fixed insertion family. Conversely, boundedness here is proved by an explicit merge strategy, not by a general-poset theorem.
- Whether `D(m)=1` infinitely often remains open; the finite blocks above are not a proof. Boundedness, the front's actual question, is settled.
I'll verify the durable state first and avoid repeating any external action.
## Recovery inspection complete — no duplicate action taken

**State verified**

- **Working directory:** `/home/lubko/soring-fronts/three-chain-insertion-gap`; worktree **clean** at `6a96398`; no commits or modified files.
- **Board #301:** exactly **one** post for this front, the verified one at `2026-11-09T09:10:18Z` (author `SoringP1 frontier: three-chain-insertion-gap`, length 4645). **No newer posts** and no second copy. I did **not** re-post.
- **Durable ledger:** `three-chain-insertion-gap` still shows `status: "running"` with **no `finding_unverified` field**. That is keeper bookkeeping, not a research side effect. I did not edit it manually; it should be reconciled by the frontier keeper/service, not guessed at.

**Effects that actually happened**

1. One board post reporting the result: `D(m) ∈ {0,1}` for all `m`, with optimal constant `1`, proved from the Hwang–Lin merge bound plus exact accounting.
2. Exact computations and DP verification were done under `/tmp/opencode/` only; no repository files were added.
3. No commits, pushes, PRs, or Lean changes.

**Unfinished work**

Nothing external is unfinished. The front’s stated question is settled: the defect is bounded, with optimal absolute constant `1`. The sub-question “is `D(m)=1` infinitely often?” remains mathematically open, but it was not part of the front’s falsifier and would be new research, not recovery work.

**Recommendation for review**

The only uncertain durable record is the ledger status remaining `running`; this should be closed by the normal keeper process rather than manually altered. No further board post is warranted unless the infinite-occurrence sub-question is pursued.

## Other metadata

```json
{
  "finished_at": 1794215527.009812,
  "started_at": 1794213976.4600663
}
```
