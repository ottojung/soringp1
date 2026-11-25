# depth2-extension-profile-minimax-completeness-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

lHkqbRIDcoxbSTGLvAyleZ-delay

## exit_state

clearexit

## question

For a finite poset P let M2(P) be the depth-two extension-count profile: the multiset, over every incomparable pair {x,y} and both orientations, of the child extension-count deck of each one-step child; more generally M_t is the recursive depth-t profile. Is there an absolute constant t such that M_t determines the exact minimax value F(P) for every finite poset P, given that the newest #301 result refuted the depth-one case (F is NOT a function of (e,M1)) with an explicit n=7 pair having e=M1=32 but F=5 versus F=6, and that M1-determination is known to hold at n<=6?

## basis

Newest #301 Lemma D refutation (2026-11-23, n=7 M1-cospectral pair F=5 vs F=6, independently refereed) and the investigated child-deck/lookahead fronts in the ledger; extension counting is #P-hard in general (Brightwell-Winkler), so this is an invariant-completeness question, not a claimed algorithm.

## falsifier

For each candidate constant t, exhibit two finite posets with identical M_t profiles but provably different F; the sharp first test is whether M2 separates the known n=7 (e,M1)-cospectral F=5/F=6 pair, and an unbounded-depth family would refute every fixed t.

## implication

A positive answer is a bounded-lookahead structural invariant completing the minimax value and constraining any extension-count-based certificate; a negative answer rules out every bounded-depth extension-count invariant as a complete invariant. This is general-poset scope only and does not transfer to S(n) without an explicit reduction.

## finding_unverified

he M1 failure is not a pairing twist. Let me check the board posting mechanism.
I have a complete, verified picture. Let me write up the finding and post one concise update to board #301 (no repository changes).
Let me verify the post appeared exactly once.
My post appeared exactly once (the other match is a referee comment on a *different* front). Let me quickly check that related front's result for overlap, and confirm clean git state.
## Outcome

I attacked the front's all‑n question on `billy-dev` and tried hard to refute it. **No all‑n verdict was reached, but the sharp first falsifier test was refuted and several new finite facts were established.** One #301 comment was posted (verified exactly once); the worktree is clean at `6a96398` — no repo, Lean, test, CI or ledger changes.

### What I verified (independent from‑scratch implementation, reproducing all board values)

- The known n=7 cospectral pair (`e=32`, identical `M1`, `F=5` vs `F=6`) is **separated by M2**: at the first differing child, P has child‑M1‑deck `(2,2,7,7,8,8,8,8,9,9,14,14)` and Q has `(2,2,6,6,7,7,9,9,10,10,14,14)`. So the Lemma D counterexample is *not* a counterexample at t=2.
- **Full global n=7 census** (all 6,129,859 labelled 7‑element posets): the only `(e,M1)` group with mixed F is the 7560‑member group containing that pair; inside it M2 takes exactly three profiles with F‑sets `{6},{5},{5}` — **zero M2 conflicts**. Together with n≤6 (155 keys, 0 conflicts; iso child deck 314 groups, 0 mixed‑F), this means **the depth‑2 profile determines F on every poset with ≤7 elements**.
- **Mechanism**: grouping n=7 posets by the flattened multiset of child `(e,F)` pairs gives 915 groups and **0 mixed‑F groups**. So the M1 failure is *not* a sibling‑pairing twist — it is that equal‑e children have different F, which M2 repairs by reading grandchildren.

### Failed falsification routes / exact obstruction

- **Composition amplification** (ordinal/parallel sums) preserves `(e,M1)`‑cospectrality but **not** M2‑cospectrality (it needs matching of `(e(C),M1(C))` over children), so the known pair cannot generate constant‑depth families.
- All **816 one‑element extensions** of each member to n=8 were checked: 6 common depth‑2 profiles, all F‑consistent — no M2 counterexample.
- **Structural obstruction** `[deduction]`: `M_t` is a multiset of unfold trees and never records which two children are siblings (orientations of one pair), yet `F = 1 + min_{siblings} max(child F)`. Completeness of any fixed t therefore requires the pairing to be recoverable from extension counts; I found no reason it must be, and no witness of its loss up to n=8.

### Honest limits

The claim "*some absolute constant t makes M_t F‑complete on all finite posets*" remains **open**. M2 is strictly stronger than M1 and is verified F‑complete through n=7, but I found neither a proof nor a counterexample for all n. The decisive obstacle is the forgotten sibling pairing and the absence of any depth‑t‑cospectral F‑conflict for t≥2. This is **general‑poset invariant completeness only** — extension counting is #P‑hard (Brightwell–Winkler), so this is not an algorithm, soundness ≠ completeness, and nothing transfers to `S(n)` without an explicit reduction. No new theorem, bound, or class placement was claimed. My post is complementary to (and slightly stronger on the global n=7 census than) the separate `reachable-depth-two-profile-f-completeness-alln` front, whose referee also left the all‑n question open.

## Other metadata

```json
{
  "finished_at": 1795462353.9502757,
  "started_at": 1795455236.2725463
}
```
