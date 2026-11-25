# antonina-tG13D135SVuKIwm7jY3AmU-supremacy

Session: ses_e3cf63415ffebQ6oXdM5Pi98kU
Workspace: /home/lubko/soring-fronts/antichain-reachable-abc-tree-completeness
Created: 1794273561889; updated: 1794276642404

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 929 (msg_1c3389cc4001kyGHPIe74bzp7m)

## Outcome

The front’s **stated reachability falsifier is met** at `n=8` (and again at `n=9`), but this does **not** disprove the front’s literal existential claim. The exact finding is a **closure failure of the A/B/C certificate grammar along optimal antichain play**, not a proof that no height-`S(n)` certified tree exists.

No repository or Lean changes were made; the worktree is clean at `6a96398`.

## Exact computation

For each `n`, I enumerated all unlabeled posets (`genposetg`), computed exact extension counts by subset DP, exact minimax `F`, and the minimum certified-tree height `H`. `H(A_n)=F(A_n)` means an all-certified optimal tree exists.

| n | unlabeled posets | posets with `H>F` | `F(A_n)` | `H(A_n)` | optimal-reachable states | bad among them |
|---|---|---|---|---|---|---|
| 7 | 2045 | 1 | 13 | 13 | 802 | 0 |
| 8 | 16999 | 52 | 16 | 16 | 5102 | 18 |
| 9 | 183231 | 839 | 19 | 19 | 33054 | 153 |

`F(A_7)=13`, `F(A_8)=16`, `F(A_9)=19` agree with the published `S(n)`, validating the minimax layer.

## Concrete obstruction

From `A_8`, the six comparisons

`(0,1),(2,3),(4,5),(1,3),(2,6),(7,1)`

are all optimal and reach the state

`Q8 = (10,8,72,0,32,0,0,10)`

with `F(Q8)=10` but `H(Q8)=11`: **no all-certified height-10 tree exists from Q8**. A second, independent Python implementation of the certificate/boolean recurrence confirms `G(Q8)=false`. Thus a certificate-starved optimal state is reachable from `A_8` at optimal depth. The `n=9` analogue `Q9=(10,8,8,0,32,0,128,0,10)` has `F=13`, `H=14`, and was independently rechecked as well.

## Honest limit

At `n=8` and `n=9`, `H(A_n)=F(A_n)`, so **some other optimal tree is fully certified**. Therefore:

- the stronger statement “every optimal antichain strategy can be certified” is **false at `n=8`**;
- the literal front “there exists a height-`S(n)` all-certified tree” **survives through `n=9`**;
- the all-`n` question remains open.

A direct lift of the `n=6` general-poset counterexample did not work; the antichain-reachable obstruction only appears at `n=8`. Exhaustive `n=10` would require 3,238,100 unlabeled posets and was not attempted.

## Reporting

One finding was posted to board `#301` at `02:10:21Z` under `SoringP1 frontier: antichain-reachable-abc-tree-completeness`. No prior post for this front existed, so nothing was duplicated. Scratch work is in `~/soring-scratch/antichain-abc`.
