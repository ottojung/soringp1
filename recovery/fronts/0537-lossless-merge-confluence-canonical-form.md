# lossless-merge-confluence-canonical-form

## status

investigated

## origin

ai_proposal_unverified

## agent_id

vjNFei316jv1dUMDzav9Vl-folk

## exit_state

clearexit

## question

For antichain-reachable comparison states at the exact optimum budget S(n), is the pairwise-lossless intersection-merge relation reported on board #301 (meet R = P1 and P2 is lossless iff F(R) = F(P1) = F(P2), equivalently every non-common constraint is F-redundant at R) a congruence: transitive and compatible with meet, so that greedy lossless merging is order-independent and converges in polynomially many steps to a unique F-preserving normal form for every n? Or is there an all-n family where the relation is non-transitive and greedy merging gets stuck in order-dependent, non-canonical local optima?

## basis

Antonina #301 executive report 'framed-dag-canonical-merge' (2026-11-18) proves all intersection joins sound and states the F-redundancy losslessness criterion with n=4 sample statistics; research-framed-certificate-frontier.md and the investigated front framed-dag-canonical-form-tightness identify join-incompatibility as the core gap but never study confluence, transitivity or order-independence, and no confluence/Church-Rosser front exists in the 536-entry ledger.

## falsifier

Exhibit a fixed n and three antichain-reachable states P1, P2, P3 with P1 losslessly merging with P2 and P2 with P3, yet P1 and P3 lossy (meet strictly raises F), or two merge orders yielding terminal states of different F; ideally an infinite family showing greedy lossless merging cannot yield a unique polynomial-size normal form.

## implication

Congruence plus polynomial convergence would give an order-independent canonicalization of optimal strategy DAGs and a polynomial-size complete framed certificate, advancing SORT-BOUND-U toward NP; a non-confluence family would be a barrier specifically to greedy/canonical-merge compression, without implying any class separation.

## finding_unverified

g normal form) and check meet-compatibility on budget-tight states at n=5.
I now have a complete mathematical finding. Before posting, let me re-verify no prior post by this front exists and find the exact board-posting mechanism.
Let me re-verify freshly that no post by this front exists before posting exactly once.
Confirmed: the only occurrence is a Viche Executive status note, not a report by this front. I'll post exactly once. Let me compose the report.
Now I'll post exactly once to board #301, redirecting output to a file.
Post succeeded. Let me verify it landed exactly once.
Post landed exactly once. Let me do a final state audit.
Done. Here is the complete outcome.

## Recovery audit (first, before any side effect)
- Worktree `billy-dev` @ `6a96398`, clean; no stash, no commits, no repo/Lean/test/ledger/canonical-main changes from this or the interrupted turn.
- Ledger front `lossless-merge-confluence-canonical-form` was `running`; I only read it.
- Fresh #301 scan showed **no prior report** by this front (the only id occurrence was a Viche status line), so I posted exactly **one** comment and verified it landed once. Scratch code lives only in `/tmp/opencode`.

## Mathematical finding — the claim is FALSE (disproved, not just inconclusive)

The front asked whether the pairwise-lossless intersection-merge relation `P~Q ⟺ F(P&Q)=F(P)=F(Q)` is a congruence on budget-tight antichain-reachable states. It is **not**, at fixed n=5 — verified independently by two separate minimax implementations.

**Non-transitivity witness** (all three states budget-tight at S(5)=7, reachable at depth 3 = 7−4):
- `P1=(0,0,0,1,11)` `{3<0,4<0,4<1,4<3}`, F=4
- `P2=(0,0,0,3,11)` `{3<0,3<1,4<0,4<1,4<3}`, F=4
- `P3=(0,0,0,2,11)` `{3<1,4<0,4<1,4<3}`, F=4

`P1&P2=P1` (F=4), `P2&P3=P3` (F=4), but `P1&P3` has **F=5>4**. So `P1~P2`, `P2~P3`, yet `P1!~P3`.

**Why:** individual-vs-joint F-redundancy. At `R=P1&P3` the extras `(3,0)` and `(3,1)` are each F-redundant alone (F drops 5→4) but jointly necessary (adding both recovers P2, F=4). Element 3 has an "either/or" that dies under intersection.

**Consequences:** meet-compatibility also fails (explicit all-eligible n=5 witness); greedy merging on `{P1,P2,P3}` gets stuck in **every** one of the 6 orders at two states whose global meet has F=5>4 — so **no F-preserving normal form exists**, the exact failure of canonical-merge compression the front targeted. (The global meet is order-invariant by associativity of `&`; the failure is absence of a single F-preserving state, not differing terminal F.)

**Persistence:** budget-tight violations found at n=6,7; a parametric either/or gadget is budget-tight for n=5–7; an ordinal-sum construction gives an infinite family of antichain-reachable states for all n≥5 (honestly labelled *not* budget-tight).

## Honest limits
- **Soundness untouched**: all intersection joins remain sound; framed-DAG checker unaffected. This is a completeness/normal-form barrier only.
- The correct *joint*-redundancy losslessness criterion is not refuted — only transitivity/congruence/confluence-to-canonical-state.
- No complexity separation (no NP/PSPACE claim, no super-polynomial certificate claim). Finite witnesses plus a general-poset infinite family; no all-n **budget-tight** family is proved. I did not confuse process success with a proof — the deliverable is a concrete, independently checkable counterexample.

No Lean or repository changes were made; the finding was reported to Antonina #301.

## Other metadata

```json
{
  "finished_at": 1795028862.097027,
  "started_at": 1795025675.1509671
}
```
