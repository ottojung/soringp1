# info-lower-bound-additive-gap-boundedness

## status

investigated

## origin

ai_proposal_unverified

## agent_id

gh2hMxBEZMpogh549m75zU-deduced

## exit_state

clearexit

## question

Is there an absolute constant C such that for all n >= 1 the exact sorting number satisfies S(n) <= ceil(log2(n!)) + C, i.e. is the additive gap above the information-theoretic lower bound uniformly bounded over all n?

## basis

problem.md/literature.md: ceil(log2 n!) <= S(n) <= O(n log n), exact values known for n<=22 with gaps S(12)-29=1 and S(16,17,18)-ceil(log2 n!)=1 (Stober-Weiss ALENEX 2023); no all-n additive-gap theorem or unbounded-growth proof recorded on board #301.

## falsifier

Exhibit either (i) for every proposed C an explicit n with a proved value S(n) >= ceil(log2(n!)) + C + 1, establishing unbounded gap, or (ii) a proof that some fixed C works for all n.

## implication

A uniform additive bound would be a strong all-n structural theorem tightening the known Theta(n log n) sandwich for S(n) and could constrain exact-evaluation/certificate questions; unbounded gap would rule out constant-additive optimality of the information bound as a universal target.

## finding_unverified

r every `n`, a uniform/explicit comparison strategy (or a certified decision tree argument) of height `<= L(n)+C`. No such strategy/certificate is known; the repo records only `O(n log n)`-type algorithmic upper bounds at the problem level and sharper but still non-constant-additive-in-form bounds are not established here. I did not find a reusable invariant implying a global constant surplus. **No proof obtained.** `[literature/repo survey]`
- **Certificate/soundness vs completeness:** exhibiting one tree of near-optimal height for some `n` is a *sound* upper-bound witness for that `n` only; it gives no completeness/forall-`n` guarantee. Conversely, pruning/efficiency arguments (e.g. in n=12 analyses) are sound lower-bound obstacles for a fixed budget but, as noted in `research-n12-nontightness.md`, are equivalent in force to leaf/information constraints at the node level and do not by themselves yield a uniform additive lower bound over all `n`. **No all-`n` boundedness follows.** `[deduction]`

**Outcome:** no fixed-`C` theorem found.

## Exact obstruction

The decisive gap is **strategic and global**: `g(n)>0` at the root means that for height `L(n)+C` the information/efficiency necessary conditions cannot be satisfied along *every* root-to-leaf line of any single adaptive tree simultaneously (a quantified, all-strategy obstruction), yet for general posets the minimax cost is non-scalar (not determined by `e(P)` alone) and locally non-tight states do not force a global root gap. Therefore:
- to **falsify boundedness** one needs an all-`n` (or infinitely many explicit `n`) **adversary/forcing invariant** sound against every sorting strategy at the antichain root that accumulates `>C` deficit — none known;
- to **prove boundedness** one needs an all-`n` **constructive strategy or inductive invariant** whose height tracks `L(n)+O(1)` — none known.

Finite computation (exact `S(n)`) is currently feasible only for small `n` and has not revealed growth; asymptotic algorithmic upper bounds are too loose (additively) and do not control the optimum. This is the concrete barrier, not resolved here.

## Limits of this report

- No new proved value of `S(n)`, no new all-`n` bound, and no counterexample family; result is a **negative/inconclusive** front analysis. `[deduction]`
- Could not fully audit live board #301 beyond the local digest, and could not fetch external web sources in-session; claims about “no theorem recorded” are relative to studied repo docs + digest results and the in-repo literature baseline (esp. Stober–Weiß for `n<=22`).
- I did **not** run new exhaustive searches or attempt reproduction at larger `n` (and prior notes indicate pure-Python forward search does not reach `n=12`); no experiment discriminated the all-`n` question here.
- Per `AGENTS.md`, this is **not** a basis for Lean/repo changes. A genuine advance would require either (ii) a checkable all-`n` constant-additive strategy/certificate or (i) a proved infinite family (or theorem) forcing unbounded root deficit, each with a full paper argument against the root quantifier and model.
Recovery check complete. The worktree is clean, there are no `*301*` task files, and the latest commit is unchanged. The board digest search found no “additive gap” post on page 1; the prior turn explicitly reported that it did not post.

The mathematical report was already delivered in the conversation. No external action is confirmed or needed, so I made no changes and did not post.

## Other metadata

```json
{
  "finished_at": 1794553632.1243398,
  "started_at": 1794544448.5351138
}
```
