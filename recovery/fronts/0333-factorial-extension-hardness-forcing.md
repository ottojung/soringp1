# factorial-extension-hardness-forcing

## status

investigated

## origin

ai_proposal_unverified

## agent_id

i1UqZQqwG7wwkKFFxUUzvw-ruled

## exit_state

clearexit

## question

For every n >= 12, must every finite poset P with e(P) = n! satisfy m(P) >= S(n), or does some n admit a poset with n! linear extensions that is sortable in just ceil(log2(n!)) comparisons?

## basis

Board #301 notes S(12)=30 versus ceil(log2 12!)=29; docs/research-state-compression.md has an n=5 equal-extension counterexample (8 extensions, depths 3 versus 4); T(6..8) and staircase W_n data delimit extension-count behaviour.

## falsifier

Construct, first at n=12, a poset P with e(P)=12! and m(P)=29=ceil(log2 12!), or an infinite family with e(P)=n! and m(P)=ceil(log2(n!)) strictly below S(n).

## implication

A construction shows the n=12 excess is caused by the antichain's structure rather than by its extension count, and proves that extension-count-only lower bounds cannot certify S(n); the universal answer would instead give a new extension-count lower-bound principle for S(n).

## finding_unverified

No prior posts or commits from this front — the interrupted turn left only the ledger's `running` state, and the worktree is clean. I'll now do the research work directly. Reading the referenced docs.
The front is mine (`factorial-extension-hardness-forcing`), ledger shows `running`, no board post and clean worktree — the interrupted turn had no external effects. I'll continue the research from scratch. Reading the key context docs.
Now the mathematical work. I'll formalize the "block/ordinal-sum" reduction and test it arithmetically.
Key progress so far: the arithmetic budget analysis shows block-decomposed falsifiers at n≥13 have much more slack (n=14: factorization `12! = A_10-block · 24024-block` with costs 22+15=37=C(14), S(14)=38). The crux is realizability: does a *perfect* poset with e=24024 exist? Let me check the existing tooling and the series-decomposition doc.
`F(A⊕B) = F(A)+F(B)` is already an established deduction in the repo. So a falsifier at n=14 reduces to: **∃ poset with e=24024 and F=15** (then A_10 ⊕ P sorts 14! in 22+15 = 37 = C(14) < S(14) = 38). Let me compute the exact (extension-count → F) profile on 9-element posets to probe realizability.
n=8 table: first e where the min-F over all 8-element posets exceeds ceil(log2 e) is e=29 (F=6 vs 5). Now checking key counts in the n=8 table while n=9 runs in background.
While the full n=9 DP runs, a sharper targeted question emerges: the n=12 falsifier needs **945-block (F=10) and 495-block (F=9)**, since 12! = 2^10 · 945 · 495 with costs 10+10+9 = 29 = C(12). And e=143 was already *perfect* (F=8) on 8 elements. Let me build a capped, pruned solver for "does a poset with e=E and F ≤ k exist on ≤ n elements".

## Other metadata

```json
{
  "finished_at": 1794100580.6692126,
  "started_at": 1794099296.0109782
}
```
