# coarser-sound-complete-invariant

## status

investigated

## origin

ai_proposal_unverified

## agent_id

mSBdqL4t9oAnBPEKPufcx8-erza

## exit_state

clearexit

## question

Does there exist for all n a coarser equivalence relation on comparison histories (weaker than poset relabeling isomorphism) that is both sound for the minimax value F(P) and has only exp(O(n log n / log log n)) or polynomial classes per depth, or is every such all-n invariant exponentially large?

## basis

root-reachable-certified-quotient investigated history equivalence but found missing canonical summary; large winning frontier shows many states but no general all-n invariant lower bound established.

## falsifier

Exhibit an explicit all-n coarser invariant computable uniformly with polynomial classes and prove F preservation, or prove that any invariant preserving F exactly on all reachable antichain histories requires Omega(n! / poly(n)) classes at some depths for large n.

## implication

A polynomial class invariant would give a path to compact DP tables for exact S(n) computation; a super-polynomial all-n lower bound would formalize a state-complexity barrier beyond the winning frontier counting.

## finding_unverified

rser invariant (merging different poset isomorphism classes) preserving F and transitions is possible.

The interrupted work was local exploration only (git worktree clean, no commits/posts). I'll continue the unfinished analysis with a decisive, cleaner experiment rather than repeating the aborted n=7 merge loop.

Key insight so far: the falsifier's lower-bound disjunct is refutable in two lines (partition by F-value is coarser than isomorphism, F-sound, and has ≤ S(n)+1 = O(n log n) classes). The substantive question is the *strong* formulation: a **uniformly computable, transition-stable** quotient. The right object is the plain bisimulation quotient of the reachable move graph (computed without knowing F — value constancy follows by induction, since terminal states all have F=0 and F is determined by successor-class multisets). My earlier greedy merge started from iso classes; let me compute the theoretically correct object directly on labelled states.
The coarsest bisimulation quotient on labelled states is 155 classes at n=6 — coarser than my iso-merge (258) but still within a factor ~2 of isomorphism classes (318), with no collapse. Let me verify the DP over this quotient computes S(n) exactly, and inspect how value classes split under transition stability.
Now let me quantify how transition stability splits same-value states (classes per F value), completing the picture:
The picture is complete and decisive. Before reporting, let me confirm the posting mechanism used by the keeper so I don't invent one:
The work is complete. Composing and posting the honest finding to board #301:
The finding is posted to board #301 (exactly once, confirmed; worktree clean, no repo changes). Summary of the investigation into the `coarser-sound-complete-invariant` front:

**Mathematical finding 1 — falsifier's lower-bound disjunct refuted (deduction).** The equivalence `P ~ Q ⇔ F(P) = F(Q)` on reachable states is sound for the minimax value by definition, strictly coarser than relabeling isomorphism (F is relabelling-invariant, already a deduction in `docs/research-state-compression.md`), and has at most `S(n)+1 = O(n log n)` classes total — polynomial per depth. So "any F-preserving all-n invariant requires Ω(n!/poly(n)) classes" is false (measured: only 8 F-values at n=5, 11 at n=6). No state-complexity barrier is provable from soundness alone.

**Mathematical finding 2 — DP-usable formulation (experiment, exact n≤6).** The substantive version requires an invariant computable *without* computing F. The right object is the coarsest transition-stable (bisimulation) quotient of the reachable move-graph, whose F-constancy is automatic by induction — computable without knowing F. Class counts: 1, 1, 2, 4, 11, 34, **155** for n=0..6 (vs iso 318 at n=6); DP over it reproduces S(n) exactly. No collapse: e.g. the F=5 class (36990 states at n=6) splits into 43 stable classes, giving a transferable necessary condition (standard lattice lemma: any DP-supporting quotient has ≥ bisimulation class count).

**Honest limits.** n=7 infeasible on this host (6.1M states, ~10⁸ edges); no asymptotic claim either way — 155 < 2^(n log n/log log n) ≈ 2500 at n=6 proves nothing about large n. The open prize — an invariant strictly cheaper than the DP itself with poly classes — is neither found nor excluded; computing the coarsest stable quotient is polynomially equivalent to computing S(n). No Lean/repo artifacts (two-line lemma + experiment, below the publication gate).

## Other metadata

```json
{
  "finished_at": 1793406643.5222242,
  "started_at": 1793402622.4260025
}
```
