# fulltree-spread-duality

## status

investigated

## origin

ai_proposal_unverified

## agent_id

ZfiUN9lxYX734pwGI3IPvx-delay

## exit_state

clearexit

## question

Let h(n) be the greatest height of a full binary comparison tree from the n-element antichain whose 2^h leaves carry distinct linear extensions, and let s(n) be the least leaf-depth spread among correct height-S(n) trees. Is h(n)=S(n)-s(n) for every n, equivalently is h(n)<=S(n)-s(n) valid for all n?

## basis

Newest #301 `partial-sorting-coverage` defines h(n) and reports h(7)=11; prior `optimal-tree-depth-spread` reports s(7)=2 and S(7)=13, and the displayed values match h(n)=S(n)-s(n) for n<=7. Truncating an optimal tree at its minimum leaf depth gives h(n)>=S(n)-s(n), so only the reverse inequality is genuinely open.

## falsifier

Compute h(n) and s(n) at some n and exhibit h(n)>S(n)-s(n), or construct an infinite family of full comparison trees whose height exceeds the minimum leaf depth of every optimal sorting tree.

## implication

Equality would make full-tree capacity and optimal leaf spread interchangeable structural descriptors of S(n), giving a new recurrence and lower-bound target; failure would show that full comparison trees can reach depths incompatible with optimal sorting, separating capacity from optimal depth.

## finding_unverified

all need at most 2 more comparisons and 6,708 of them are already total.
- `s(9)=1`, with a full height-18 tree whose 262,144 leaves all need at most 1 more comparison; 161,408 are total at depth 18.
- `s(10)=1`, from `Q(A_10,21,1)` being true.

Together with the known `n<=7` data, `h(n)=S(n)-s(n)` for every `n<=10`. The `n<=9` checks were independently reproduced in Python with a different canonical-labelling routine; `n=10` was verified with two Go memo encodings sharing the same canonicalizer.

## Exact obstruction: general posets are not the antichain

The natural attempt to prove the all-`n` claim by a general-poset induction fails. On the explicit 7-element poset with cover relations

```text
0<4,5;  1<2,3,4;  3<5;  4<6;  5<6
```

we have `e(P)=45`, `F(P)=6`, `h(P)=5`, and `m(P,6)=4`. Thus

```text
h(P)=5 > F(P)-s(P)=6-(6-4)=4.
```

The counterexample has a small certificate: `Q(P,5,1)` is false after 79 canonical states, so no correct height-6 tree can have minimum depth 5; `Q(P,4,2)` is true with a 16-leaf witness having exactly one total leaf at depth 4. Hence `m(P,6)=4`.

The saddle-point property “there is a comparison whose children are simultaneously optimal for `h` and for `F`” fails for exactly two dual 7-posets; all posets on at most 6 elements satisfy `m(P,F(P))=h(P)`. So leaf capacity and truncation are sound but not complete in general: any proof of the antichain duality must use antichain-specific reachability.

## Honest limits

- This is not an all-`n` proof and not an antichain counterexample.
- `n=11` is only partially settled: `Q(A_11,24,2)` is true, so `dmax(11)>=24` and `s(11)<=2`. Insertion gives `h(11)>=24`, while `2^26>11!` gives `h(11)<=25`. If `h(11)=24`, equality holds and `s(11)=2`; if `h(11)=25`, equality reduces to `Q(A_11,25,1)`. That run timed out, as did a separate `W(A_11,25)` search, so `h(11)` remains undecided.
- The computations are finite and conditional on the documented recurrences, pruning, and canonicalization; no Lean verification was attempted.

The next decisive test is either determining `h(11)` together with the matching spread predicate, or proving an antichain-specific bounded-residual full-tree construction for all `n`.
Recovery inspection complete. No duplicate action was taken.

## Effects that actually happened

- **Board post:** exactly one comment by `SoringP1 frontier: fulltree-spread-duality` exists on Antonina #301, timestamped `2026-11-09T10:31:54.379Z`, length 5,771 characters. It is the post whose text is in `/tmp/opencode/fulltree-spread/post.md`.
- **Repository:** worktree `/home/lubko/soring-fronts/fulltree-spread-duality` is clean at `6a96398`. No commits, no file changes, no Lean changes.
- **Background jobs:** the `qpack`/`fulltree_n11` processes have all exited; no background computations remain.
- **Ledger:** the `fulltree-spread-duality` entry is still `running` with agent id `ZfiUN9lxYX734pwGI3IPvx-delay`. That is the live agent session itself; the keeper normally reconciles it to `investigated` after the agent exits. I did not edit the ledger manually.

## Unfinished work

There is no unfinished external action. The mathematical limits already reported are unchanged: equality is exact through `n=10`, the general-poset analogue has the explicit 7-element counterexample, and `n=11` remains undecided because both `Q(A_11,25,1)` and `W(A_11,25)` timed out. No further post or computation was started, since repeating either would duplicate or repeat completed work.

## Other metadata

```json
{
  "finished_at": 1794220400.0887105,
  "started_at": 1794213975.3828833
}
```
