# antonina-aKlUrqA8vjpKrGTpVjIPSg-shadow

Session: ses_e40a570adffeXh6ey51EnPxD4u
Workspace: /home/lubko/soring-fronts/near-optimal-partial-sorting-gap
Created: 1794211745685; updated: 1794215671688

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 775 (msg_1bf78e7cc001REMu7444DkZ9Ze)

Recovered the interrupted state, found the existing 08:06 #301 post, and continued only its open computational work. No repository or Lean changes; one new board post was made (not duplicated).

## Mathematical findings

**1. Exact n=8 value**

- `S(8)=C(8)=16`, `h(8)=14`, so there is no full height-15 comparison tree from `A_8`.
- `m_15(A_8)=32512 = (254/315)·8!` exactly, a deficit of 256 from `2^15`.
- `m_16(A_8)=8!`.
- The non-existence of a full height-15 tree was independently confirmed by a raw labelled-state search with no symmetry quotient.

**2. Correction to the earlier post**

The 08:06 ratios for n=4,5,6 were wrong. The exact values are:

| n | `m_{S(n)-1}(A_n)/n!` |
|---|---|
| 3 | 2/3 |
| 4 | 2/3 |
| 5 | 8/15 |
| 6 | 32/45 |
| 7 | 253/315 |
| 8 | 254/315 |
| 9 | 2048/2835 |
| 10 | 8192/14175 |

In particular `m_9(A_6)=512`, not 448. The number 448 was the `Mstates` memo count in the `n=6,h=10` run. Thus `m_{S-1} ≤ n!/2` already fails at n=3, not n=6.

Also, `d(n)=floor(log2 n!)-h(n)` is not monotone: `d(7)=d(8)=1`, while `d(9)=d(10)=0`.

**3. Insertion lemma [paper proof]**

If `A_n` has a full height-h tree, then for any `d` with `2^d ≤ n+1`, `A_{n+1}` has a full height-`h+d` tree. Therefore

`h(n+1) ≥ h(n) + floor(log2(n+1))`, and `d(n+1) ≤ d(n)+1`.

This gives `h(10)≥21`, `h(11)≥24`, and a one-key coverage propagation rule.

**4. Counting obstruction to the constant-gap branch [deduction]**

For every n with `S(n)>C(n)`, we have `S(n)-1 ≥ C(n)` and hence `2^{S(n)-1} ≥ 2^{C(n)} > n!`. So the leaf-count bound `m_b≤2^b` gives no coverage deficit at all on the known gap indices n=12–19,22. At tight n, `2^{C-1}/n!` can approach 1 when `n!/2^C` approaches 1/2.

Therefore a constant-gap theorem cannot be proved from height-leaf soundness alone; it must be a structural comparison-tree theorem. This is the precise soundness-vs-completeness gap relevant to coverage certificates.

## Honest limits

Exact `n=11` was not finished. The symmetry-quotient DP reached 11.7 GB while evaluating `W(A_11,25)` and was stopped. Two rigorous lower bounds remain:

- `h(11)≥24` by insertion;
- `m_25(A_11)≥28,835,840 = 0.7224·11!` by a split 2+9 construction.

The largest exact ratio remains `254/315` at n=8, so any universal δ must satisfy `δ ≤ 61/315 ≈ 0.1937`. The front’s main dichotomy remains open; no infinite family or constant coverage gap is claimed.

The new board record is at #301, `2026-11-09T08:42:01Z`, author `SoringP1 frontier: near-optimal-partial-sorting-gap`. Worktree remains clean at `6a96398`.

## Output 974 (msg_1bf966234001zYYKbsf6DjnlBy)

Recovery inspection complete. No duplicated external actions.

## State verified

- **Working tree:** clean at `6a96398` on `billy-dev`; no commits or Lean/repo changes.
- **Board #301:** exactly **one** post by `SoringP1 frontier: near-optimal-partial-sorting-gap`, at `2026-11-09T08:42:01Z` (3,348 chars). No duplicate was made.
- **Prior post contents:** the corrected n=3..10 coverage ratios, exact `m_15(A_8)=32512=254/315·8!`, `h(8)=14`, `h(9)=18`, `h(10)=21`, the insertion lemma, and the leaf-count obstruction are all recorded.
- **Uncertain effects:** none remaining. The only prior external effect was that single board comment, now confirmed.

## Unfinished work attempted

The only unfinished mathematical item was exact n=11. I implemented a memory-capped version of the symmetry-quotient DP and ran `W(A_11,25)`.

It ran for about 29 minutes with stable memory (~1.4 GB) but did not finish, so I stopped it. No new board post was made, because there was no new result.

Therefore the previous n=11 statement remains current and honest:

- `h(11) ≥ 24` by the insertion lemma;
- `m_25(A_11) ≥ 28,835,840 = 0.7224·11!` by the split 2+9 construction;
- exact `h(11)` and `m_25(A_11)` remain unresolved at this resource scale;
- the best exact coverage ratio remains `254/315` at n=8, so any universal δ must satisfy `δ ≤ 61/315 ≈ 0.1937`.

No additional mathematical claim was added this turn, and no external side effect was repeated.
