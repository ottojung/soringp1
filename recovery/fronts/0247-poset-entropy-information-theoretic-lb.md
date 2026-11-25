# poset-entropy-information-theoretic-lb

## status

investigated

## origin

executive_commissioned

## agent_id

HPLl7yaQ5ad0u0DymhPLuG-busy

## exit_state

clearexit

## question

Derive an information-theoretic lower bound for S(n) using the actual structure of reachable posets (not just n! permutations) and see if it explains the n=12 gap or forces gaps infinitely often.

## basis

Linear-extension counts vary; leaf counts alone don't determine minimax cost (research-state-compression shows).

## falsifier

Show the poset-structure information bound is always equal to or weaker than log2(n!) and cannot explain any known gap beyond the trivial combinatorial bound.

## implication

A better structural information bound would narrow the search window for exact algorithms.

## finding_unverified

Let us look up what "information budget on optimal paths" might mean. Also look at the board more - maybe there's more context in recent messages?

Let us explore this more systematically.

Let us look up this case:

Inspecting prior-turn state first: the interrupted action was a local, in-memory Python computation (an L3 bound probe) — no board posts, commits, or file writes were made (only `/tmp/test_lk.py`, a temp probe script). Nothing to undo; continuing only the unfinished reporting step.
Ladder check confirms the proved lemma (n=6, c=1: L1=9=C_log2(360)). Working tree is clean — no repo drift from the interrupted turn. Now locate the board posting command.
No conflicting post for this front exists on pages 1–2, so the report was never delivered before the failure. Posting exactly once now:
The response echoes the issue description rather than confirming my comment. Verifying delivery with a single read (no re-post):
Delivered exactly once (confirmed on page 1, `2026-11-03T18:32:45Z`). Side-effect audit complete: the interrupted turn had made **no** external effects (only reads/computation; the sole artifact was `/tmp` probes), so nothing was duplicated — this board comment was the only unfinished deliverable, posted once. No commits, no Lean, no repo files: worktree clean.

**Mathematical finding (report): for every n, the adversarial-ply structural information bound provably collapses to the trivial bound at the antichain root.**

- **Lemma (all n, proof + checks):** let `L_k` be the k-fold iterate of the one-ply operator (`L_k = 1 + min-over-pairs·max(L_{k−1}(children))`, `L_0 = ⌈log₂ e(P)⌉`). Then for n ≥ 2, k ≥ 1, c ≤ (n−2)/2: `L_k(P_c(n)) = ⌈log₂(n!/2^c)⌉`, where `P_c(n)` = c disjoint 2-chains + n−2c free keys. In particular at the root: `L_k(A_n) = ⌈log₂ n!⌉` for all n — via the free-transposition automorphism giving exact ½ splits, the no-power-of-2 argument on `n!/2^c`, and the monotone chain `L₀ ≤ L₁ ≤ … ≤ F` (Thms 1–2 of `research-one-ply-obstruction.md`).
- **Checks:** root `L₁ = L₂ = L₀` for n = 1…12 (29 at n = 12); ladder `n=6, c=1: L₁ = 9 = ⌈log₂ 360⌉`.
- **Consequences for the falsifier:** proved *for this family* — no ply-depth ≤ n/2 refinement, compositional merge-fit bound, or efficiency pruning lifts to the root for any n; strict local gains (n=5 e=8 witness, Merge(2,4)) never transfer. Hence this entire route cannot explain `S(12)=30 > 29`.
- **Honest limits:** does not exclude depth > n/2 ply bounds, non-ply invariants, or non-monotone/strategic bounds; the free-free prefix keeps constant slack `12!/2²⁹ = 0.892 < 1` through c = 6, matching Wells' deep (S₂₄) obstruction; "gaps infinitely often" remains unsupported either way; no complexity-class claim.
- **Obstruction stated:** gap explanation requires bounds that are non-monotone under balanced prefixes — consistent with the n12-nontightness note's "strategic, not scalar" conclusion.

## Other metadata

```json
{
  "finished_at": 1793730813.5913467,
  "started_at": 1793725000.2548537
}
```
