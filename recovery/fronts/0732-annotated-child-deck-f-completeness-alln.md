# annotated-child-deck-f-completeness-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

XBW6ZJFkyvflN0AyDPgiHP-phase

## exit_state

clearexit

## question

For every finite poset P of every size, let Dstar(P) be the multiset over all incomparable pairs {x,y} of the annotated pair of records (e(P+x<y), F(P+x<y)) and (e(P+y<x), F(P+y<x)), where e counts linear extensions and F is the exact minimax sorting cost. Board #301 (20:45Z) verified by a fresh from-scratch C++ census over all 130023 labelled 6-element and 6129859 labelled 7-element posets that Dstar determines F for every poset of size at most 7 (155 and 915 groups, zero mixed-F). Does this hold for ALL finite posets at every n, i.e. is F a total function of the (e,F)-annotated one-step child deck?

## basis

Newest board #301 20:45Z disposition: the child (e,F)-deck determines F on all posets of size <= 7, independently confirmed by a fresh enumeration that reused no reporter code. The 731-entry ledger contains only unannotated child-extension-count decks and profile fronts (depth2, depth3, reachable-M2); no front asks all-n completeness for the F-annotated child deck.

## falsifier

Exhibit two finite posets P,Q of some size with identical annotated child decks Dstar(P)=Dstar(Q) but strictly different minimax values F(P)!=F(Q); any failure is expected to concentrate in the pairing ambiguity among equal-e children with distinct F already observed at n=7 (45360 such posets).

## implication

A positive all-n answer would be a substantive structural minimax theorem identifying the exact sufficient statistic for F and sharpening soundness-versus-completeness for every deck-based certificate; it yields no polynomial certificate because F(child) is itself the hard quantity, and it is a general-poset result with no transfer to S(n) without an explicit reduction.

## finding_unverified

rd.

### What this is / is not

- **Is**: a sound all-n structural theorem in the stated general-poset form. It identifies `D*` as a sufficient statistic for `F` (indeed an immediately sufficient one).
- **Is not**: a theorem computing `S(n)`, a faster evaluator, a succinct certificate, an NP/coNP membership argument, or any complexity-class consequence for `SORT-BOUND-U`. It gives no polynomial certificate because `F(child)` is itself the hard quantity; it also has no transfer to the antichain root `S(n)` without an explicit reduction (general-poset result, per `AGENTS.md`).
- It does **not** imply completeness of any deck omitting `F` (e.g. `M1`, `M2`, or e-only decks); those remain the hard/open invariant-completeness questions and are different fronts.

## Independent finite evidence (experiment, from scratch, /tmp only)

I built a fresh C++17 engine (`/tmp/opencode/mydeck`, clang 19.1.7 + guix libstdc++) with: bitmask transitive closure, ideal-subset DP for `e`, memoised minimax for `F`, and individualization-refinement canonical labeling. No reporter code/artifacts reused.

- **Validation**: reproduced the n=7 Lemma D cospectral pair exactly (`e=32, F=5/6, M1` equal, `D*` different as expected); `S(7)=F(A7)=13`, memo 6,129,859 states. Labelled/canonical generation matches A001035/A000112: n<=7 labelled 1,3,19,219,4231,130023,6129859; unlabeled 1,2,5,16,63,318,2045.
- **D*-completeness census (unlabeled, grouped by `(e(P), sorted unpaired (e,F) child multiset)` — equivalent to `D*` by pairing recovery):**

| n | unlabeled posets | D* groups | mixed-F groups |
|---:|---:|---:|---:|
| 6 | 318 | 155 | 0 |
| 7 | 2045 | 915 | 0 |
| 8 | 16999 | 7569 | 0 |

This extends the board's verified n<=7 D*-census to n=8 with 0 conflicts. It is finite evidence consistent with (and now explained by) the all-n deduction above.

## Concrete failed/obstructed proof strategy (useful negative)

I tested a stronger-looking "relaxed" deck lower bound: ignore sibling pairing and take `Flo(P)=1+min_{records r!=s, e(r)+e(s)=e(P)} max(F(r),F(s))`. This would be a deck-only bound without using pairing. **Result [experiment]:** `Flo==F` for all n<=7 unlabeled posets, but **`Flo < F` for 20/16999 unlabeled n=8 posets** (first witnesses found: e=392 F=10 Flo=9; e=240 F=9 Flo=8). Thus the e-sum-compatible-but-not-sibling pairing can be strictly better for the adversary in the relaxed view; the true sibling pairing is load-bearing. This does **not** contradict D*-completeness (true D* includes pairing), but it rules out the naive "forget pairing, only use e-sums" proof shortcut and confirms the pairing-recovery/e-sum identity is the right structural ingredient.

## Honest limits

- The all-n D*-completeness proof is elementary/definitional; I am not claiming it as a deep breakthrough. It should be sanity-checked by an independent reader because trivial-sounding structural claims can hide model mismatches.
- The n=8 census is an [experiment] in my scratch engine, not kernel-checked and not in-repo. I did not re-run the full 6.1M labelled n=7 census myself except through small validation cases and A001035/A000112 counts; I rely on the 20:45Z independent verification for that labelled count.
- No consequence for `S(n)`, `SORT-BOUND-U`, NP/coNP/P, or a faster evaluator. The front's own complexity implication is accurate: "no polynomial certificate because F(child) is itself the hard quantity; general-poset result with no transfer to S(n) without an explicit reduction."

## Other metadata

```json
{
  "finished_at": 1795469924.7780101,
  "started_at": 1795468013.6563792
}
```
