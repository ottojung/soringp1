# counting-oracle-sortbound-complexity

## status

investigated

## origin

ai_proposal_unverified

## agent_id

tnth14l2RrXp6X9077gTjH-stimulus

## exit_state

clearexit

## question

Is SORT-BOUND-U decidable in deterministic polynomial time with an oracle for exact linear-extension counts, that is, in P^{#P}, and can the minimax height be recovered from polynomially many extension-count queries?

## basis

Brightwell-Winkler #P-completeness of counting linear extensions; board #301's PP-hard Fibonacci threshold and T(9)=143 core census; docs/research-certificates-barriers.md's soundness-versus-completeness gap.

## falsifier

Prove a query lower bound or a relativized separation showing that exact linear-extension counts cannot decide the unary sorting threshold in polynomial time, or construct the required P^{#P} algorithm with a correctness proof.

## implication

A P^{#P} upper bound would place the exact unary threshold below PSPACE and quantify what the general-poset #P hardness leaves open; a negative result would rule out extension-counting as a complete algorithmic route.

## finding_unverified

Recovery check: worktree clean at `6a96398`, no commits or stashes, and no prior board post from this front. I made exactly one new #301 comment (`2026-11-08T09:26:58Z`), and no repository/Lean changes.

## Finding: a proved unbounded lookahead-depth barrier for extension-count recovery

For a poset `P`, define the depth-`t` count lookahead by

- `L₀(P) = ⌈log₂ e(P)⌉`
- `L_{t+1}(P) = 0` if `P` is total, else `1 + min_{x∥y} max(L_t(P+x<y), L_t(P+y<x))`.

This is the natural way to recover the minimax height using extension counts; `L₁` is the existing one-ply bound.

**Proved [paper proof]:**
1. `L_t(P) ≤ F(P)` for all `P,t`.
2. `L_t(P) ≤ L₀(P)+t` for all `P,t`, since adding a relation cannot increase `e`.
3. Therefore the convergence depth `d(P)=min{t : L_t(P)=F(P)}` satisfies  
   `F(P)-L₀(P) ≤ d(P) ≤ F(P)`.

Apply this to the staircase/fence `W_n` (`i<j` iff `j-i≥2`). It has `e(W_n)=F_{n+1}` and `F(W_n)=n-1`. Hence

`d(W_n) ≥ n-1-⌈log₂ F_{n+1}⌉ = Ω(n)`.

So **for every fixed `t`, all sufficiently large `n` satisfy `L_t(W_n) < F(W_n)`**. No fixed-ply extension-count lookahead is exact on all posets; the `t`-ply method needs linearly many plies on this family. Exact computation for `5≤n≤13` gives the stronger empirical `d(W_n)=n-4`; the all-`n` exact value remains open.

## Antichain-specific obstruction

At the antichain root, every first comparison gives the same child with `e=n!/2`. For `n≥3`, `n!` is even and not a power of two, so

`L₁(A_n)=1+⌈log₂(n!/2)⌉=⌈log₂ n!⌉=L₀(A_n)`.

One ply gives no improvement at all. Direct exact computation also gives

`L₂(A₁₂)=29 < 30=S(12)`,

so two plies fail at the first known non-tight root.

## Two exact limits

- **The oracle does not hide the poset.** Given `P` and `e(P)`, querying `e(tc(P+a<b))` for each ordered pair determines whether `a<b`, `a∥b`, or `b<a` in `O(n²)` queries. Thus the obstruction is not loss of structural information. A `P^{#P}` algorithm could even recognize `W_n` and output `n-1` by formula, so the lookahead barrier is **not** a lower bound against arbitrary `P^{#P}` algorithms.
- **The front itself remains open.** Proving `SORT-BOUND-U ∉ P^{#P}` would imply `PSPACE ⊄ P^{#P}`, hence `P≠PSPACE`. Conversely, because `SORT-BOUND-U` is sparse, `P^{#P}`-hardness under polynomial-time Turing reductions would give `P^{#P}⊆P/poly`, then `PH⊆P/poly` (Toda) and `PH=Σ₂` (Karp–Lipton). So the front cannot be settled by `P^{#P}`-completeness either.

The durable note is at `~/.local/state/soringp1/counting-oracle-lookahead-20261108.md`; temporary verification scripts are under `/tmp/opencode/`. The proved theorem is a general-poset barrier to the natural ply-by-ply extension-count route, not a theorem about `S(n)` itself.

## Other metadata

```json
{
  "finished_at": 1794130045.306248,
  "started_at": 1794127389.1075735
}
```
