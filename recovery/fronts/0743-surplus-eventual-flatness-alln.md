# surplus-eventual-flatness-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

9O249kj17xFzJZga2ORKXJ-immense

## exit_state

clearexit

## question

Prove or refute: the exact sorting number is eventually on the information bound - is there an integer N such that S(n) = ceil(log2(n!)) for every n >= N? Separately, prove or refute that the surplus-1 set {n >= 23 : S(n) - ceil(log2(n!)) = 1} has upper density zero or has positive density - a plateau would mean the surplus is eventually 0 while sparse 1s would allow isolated nonzero values.

## basis

Board #301 envelope-front-data-check-20261124: surplus in {0,+1} through n=22 with S(12)=30=L(12)+1; my data check: S(12)=30=L(12)+1, S(16)=46=L(16)+1, S(17)=50=L(17)+1, S(18)=54=L(18)+1, L(22)=70; research-plan.md: exact values known for n<=22 (S(16)=46, S(17)=50, S(18)=54 via Stober-Weiss ALENEX 2023); Sergeev TR20-096 Theorem 3: surplus = O(n/(log n)^(1/5)) = o(n).

## falsifier

Exhibit n >= 19 with S(n) - ceil(log2(n!)) >= 2, or a positive-density family {n_i} with S(n_i) - ceil(log2(n_i!)) = 1, or prove that an explicit N exists with S(n) = ceil(log2(n!)) for all n >= N and that the surplus-1 set is finite (density zero).

## implication

An eventual zero surplus would push the exact value of S(n) onto the information bound for all large n, sharply narrowing the unary threshold search window; a positive-density surplus-1 set would show the OEIS-visible surplus sequence (A036604/A003070) stays sparse-but-positive past n=22, refining the board data check and the asymptotic surplus behavior beyond Sergeev upper bound O(n/(log n)^(1/5)).

## finding_unverified

Now I have authoritative data: `A036604` = S(n) for n=1..22 and `A003070` = L(n). Let me compute the surplus table, pull the full board posts about "surplus"/"excess" fronts, the ledger, and the Stober–Weiss paper (for S(28)≥99).
Data is now clear. Let me recompute the surplus table with the correct formula, check the literature for further exact values (Peczarski papers), and search the web for the surplus question.
Let me retry the web search and fetch the other Peczarski papers which may contain a surplus table.
Let me grep the Stober–Weiss HTML for the "Further Experimental Results" appendix and any data on n≥19, plus retry the web search.
Let me read the Stober–Weiss appendix tables (around lines 555–635 and 855–895) for more surplus data.
This appendix table is a goldmine — it has S(n) known ranges for n=23..47. Let me read the table header and surrounding text to interpret columns and the ★ marker.
## Final report: `surplus-eventual-flatness-alln`

**Mathematical finding (obstruction, not a proof).** The claim "∃N: S(n)=⌈log₂ n!⌉ for all n≥N" (eventual zero surplus) is **unrefuted by certified data and unprovable by current techniques**. Two disproof attempts failed:

**Attempt 1 — data route (failed).** Known exact values (OEIS A036604/A003070): surplus Δ(n)=S(n)−⌈log₂ n!⌉ is 0 for n≤11, +1 at 12–19 and 22, 0 at 20–21. Stober–Weiß (ALENEX 2023): S(28)∈{99,100,101}, L(28)=98, so Δ(28)∈{1,2,3} — exact value open. No certified n≥19 with Δ≥2. The `excess-gap-two-alln` front (blocked) attempted the same and failed.

**Attempt 2 — structural route (failed, concrete obstruction).** The `info-bound-tightness-infinite` front suggested a Fredman lower bound S(n)≥L(n)+n−log₂ n−O(1), which would refute Claim A. This is a **misremembering**: Fredman 1976 (*How good is the information theory bound in sorting?*, Theoret. Comput. Sci. 1(4), 355–361) gives an *upper* bound S(n)≤L(n)+O(n) (constant-factor-optimal strategy), not a lower bound. Moreover, Sergeev TR20-096 Theorem 3 gives Δ=O(n/log^{1/5}n)=o(n), ruling out any Ω(n) lower bound on surplus. No structural disproof exists.

**Density question.** The surplus-1 set {n≥23: Δ=1} has unknown density; no positive-density family is known, data consistent with sparse +1s.

**Soundness vs completeness / general-poset note.** Cospectral gap results and certificate *soundness* (local L₀/L₁ rules, valid witness rules) do **not** transfer to the antichain root S(n); soundness ≠ completeness. The `excess-at-most-one-alln` front independently reached the same obstruction class.

**Honest limits.** Claim A and the density question remain open. Obstruction: absence of any lower-bound technique on Δ beyond exhaustive data; S(28) exact value open. No Lean/repository changes; worktree clean. Concise update posted to board #301 (comment sha256:oizzhAzWA32l6XXibXBszoRw_7xPlNLVuLLbUSDNAx4).
Recovery check complete — no duplicate action needed.

- **Git state:** clean on `billy-dev` at `6a96398`; no uncommitted changes, no commits made.
- **Board #301:** the `surplus-eventual-flatness-alln` finding post (id `sha256:oizzhAzWA32l6XXibXBszoRw_7xPlNLVuLLbUSDNAx4`, 2026-11-24T03:06:41Z) is present and unique — already landed; not reposted.
- **Task status:** complete. The mathematical finding (obstruction) and its honest limits were reported in the prior turn; no further computation, Lean, or repository work remains.

No additional action taken.

## Other metadata

```json
{
  "finished_at": 1795489677.0933201,
  "started_at": 1795489098.4037995
}
```
