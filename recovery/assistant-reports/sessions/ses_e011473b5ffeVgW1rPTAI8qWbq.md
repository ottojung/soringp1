# antonina-1eHCAVrOu0tdG5qZjCbNPV-pomp

Session: ses_e011473b5ffeVgW1rPTAI8qWbq
Workspace: /home/lubko/soring-fronts/superadditivity-tight-split-finiteness-alln
Created: 1795278212281; updated: 1795278963588

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 13 (msg_1fef2fb55001bA2HdbOWi88jkf)

I'll start by inspecting the current state carefully, as instructed, to avoid repeating any side effects from the interrupted turn.

## Output 36 (msg_1fef30c6a001K5MfsQ59bBh1oC)

I'm on `billy-dev` as required, and the worktree appears clean. Let me inspect durable task records, the board, and any prior work on this specific front before doing anything else.

## Output 55 (msg_1fef3361a001vxqQV6eOBwPQ6y)

The worktree is clean at `6a96398`. I need to find whether the interrupted turn on THIS front already did anything. Let me search the board for this specific front and check scratch space.

## Output 70 (msg_1fef35bf1001tltb9RKa0m9khL)

Let me check the full board JSON and scratch for any trace of THIS specific front (the L recurrence / defect-tight split) to see if the interrupted turn already posted or computed anything.

## Output 90 (msg_1fef3869e00105ZjB6d5HpV13S)

I've confirmed no prior side effects from this front (no board post, no scratch, no repo change). Now let me study the exact values and literature.

## Output 114 (msg_1fef3e6e7001e3MipBmj4VEItY)

The key structure is now clear. Let me verify the central arithmetic claim — that `ceil(log2 n!) > L(n)` for all n≥7 — over a wide range, since that would give an unconditional proof not even needing the defect inequality.

## Output 125 (msg_1fef4830e001QpA3QjciLhHgtI)

I now have a complete picture. Let me independently verify the main theorem with a fresh from-scratch implementation (exact integer bit-length for the information bound), and stress-test the induction inequalities.

## Output 136 (msg_1fef57b57001U7IBYxdbdhLTJH)

The theorem verifies independently. Let me check the board posting mechanism before reporting (to avoid duplicating or mis-formatting any external write).

## Output 156 (msg_1fef5afdd001m2ggWFe8OHVpot)

Let me confirm the exact posting mechanism used previously (from recorded dispatch files), so the single report post is well-formed.

## Output 185 (msg_1fef6038f001oginBLmKBr5ORE)

I have a complete, verified result. Let me post ONE concise finding to board #301 (the established reporting channel; confirmed no prior post from this front), then verify it landed.

## Output 203 (msg_1fef6ad14001MDOHMrdNghWMCE)

The post succeeded (rc=0). Let me verify it actually landed on #301.

## Output 214 (msg_1fef6ca160010JhKKSPxBcbGK6)

The finding is posted and verified on #301. Final state check:

## Output 225 (msg_1fef6dc74001sxBqRCtYrZAXhY)

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
