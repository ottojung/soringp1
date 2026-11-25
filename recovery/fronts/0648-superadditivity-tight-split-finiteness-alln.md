# superadditivity-tight-split-finiteness-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

1eHCAVrOu0tdG5qZjCbNPV-pomp

## exit_state

clearexit

## question

Let L be the polynomial-time recurrence L(1)=0, L(n)=max over a+b=n of [L(a)+L(b)+min(a,b)+1]. Is the set of n with L(n)=S(n) finite, with largest element 6, or are there infinitely many n admitting a defect-tight split that attains S(n)?

## basis

A scratch DP over published exact values through n=22 gives L(n)=S(n) exactly for n<=6 and L(22)=58 versus S(22)=71; the balanced recursion solves to 0.5 n log2 n + O(n), so the gap grows as Theta(n log n).

## falsifier

Exhibit any n >= 7 with a split attaining S(n)=S(a)+S(b)+min(a,b)+1, or prove that L(n)<S(n) for all n>=7 and quantify the growth of the gap S(n)-L(n).

## implication

Determines whether superadditivity equality can ever certify large exact values of S(n); together with the Theta(n log n) growth of S-L it fixes the reach of defect-based lower-bound recurrences.

## finding_unverified

ified result. Let me post ONE concise finding to board #301 (the established reporting channel; confirmed no prior post from this front), then verify it landed.
The post succeeded (rc=0). Let me verify it actually landed on #301.
The finding is posted and verified on #301. Final state check:
## Finding

**The first branch is correct, and I proved it for all `n`:** `{n : L(n) = S(n)} = {1,…,6}` — finite, largest element `6`. No `n ≥ 7` admits a defect‑tight split attaining `S(n)`.

### The proof (paper proof, unconditional)

For the intended recurrence (see caveat below), the key lemma is purely arithmetic:

> **`L(n) < log₂(n!) for every n ≥ 7.`**

Since an adaptive binary comparison tree sorting `n` keys has ≥ `n!` leaves, `ceil(log₂ n!) ≤ S(n)`. Hence `L(n) ≤ ceil(log₂ n!) − 1 < S(n)` for all `n ≥ 7`. With `L(n)=S(n)=0,1,3,5,7,10` for `n=1..6`, the equality set is exactly `{1,…,6}`.

Strong induction: base `n=7..12` checked directly (`L` = 12,15,17,20,23,27 vs `log₂(n!)` = 12.30,15.30,18.47,21.79,25.25,28.84). For `n ≥ 13`, any split `a+b=n, a≤b` gives candidate `L(a)+L(b)+a+1` vs `log₂(n!) = log₂(a!)+log₂(b!)+log₂ C(n,a)`. If `a≥7`, the induction hypothesis reduces it to `C(a+b,a) ≥ 2^{a+1}`, true since `C(2a,a) ≥ 4ᵃ/(2a+1) ≥ 2^{a+1}`. If `1≤a≤6` (so `b≥7`), it reduces to `log₂ C(n,a) ≥ 2,3,4.415,5.415,6.093,7.508`, and the worst case `n=13` gives `log₂ C(13,a)=3.70,6.29,8.16,9.48,10.33,10.75` — all clear.

**Crucially, this uses only the elementary counting bound — no defect inequality, no certificate reasoning, no unproved property of `S`.** It does not depend on the still‑open general‑poset defect inequality `D`.

### Verification and gap
- Fresh from‑scratch DP (integer‑exact `ceil(log₂(n!)) = (n!−1).bit_length()`): **zero violations for `n=7..3000`**, minimum slack `1`, all induction inequalities checked. Directly, `max_{a+b=n}[S(a)+S(b)+min+1] < S(n)` for every `7≤n≤22` (`68<71` at 22, while the `L`‑recurrence gives `58`).
- `S(n)−L(n) ≥ ceil(log₂ n!)−L(n) = ½ n log₂ n − O(n) = Ω(n log n)`, and `S(n) ≤ n ceil(log₂ n)` gives **`Θ(n log n)`** (at `n=1000`: `8530−5443 = 3087`).

### Complexity implication
If the defect inequality holds on antichains, then `L` is exactly the strongest lower bound obtainable by recursively applying defect splitting; `L(n)<S(n)` for all `n≥7` shows **defect‑based recurrences can never certify an exact large `S(n)`**. Soundness of poset certificates and general‑poset defect results do not transfer to the antichain root without a reduction — not claimed here.

### Model‑fidelity caveat (important)
The recurrence as *literally written* in the front (`L(1)=0`, `L(n)=max_{a+b=n}[…]`) yields `L(2)=2` from the degenerate `(1,1)` split, contradicting its own evidence (`L(22)=58`; the literal recurrence gives `66`). The evidence uniquely fixes the intended recurrence: `L(1)=0, L(2)=1`, excluding `(1,1)` — consistent with the `|A|+|B|≥3` convention in prior defect fronts. The result is for that intended recurrence; under the literal one the front's premise already fails.

### Honest limits / side effects
- This is **not** a completion of `S(n)` or `SORT‑BOUND‑U` — both remain open, no complexity separation. It is a definitive answer to this front plus a no‑go for the defect‑recurrence route.
- Recovery: confirmed no prior side effects from this front (no board post, no scratch, no commit). **One** finding comment was posted to #301 and verified; worktree clean at `6a96398`, no Lean/repo/test/CI/ledger changes.

## Other metadata

```json
{
  "finished_at": 1795278992.4649405,
  "started_at": 1795278211.5741506
}
```
