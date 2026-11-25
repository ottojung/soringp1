# antonina-DAQTY0m1Bufi3Q0yXHEsh8-sweating

Session: ses_e05fa52e8ffeyd53xi8aT3nMz0
Workspace: /home/lubko/soring-fronts/verify-tightness-propagation-20261120
Created: 1795196038551; updated: 1795196687636

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 58 (msg_1fa05eafc001jVQlgPnGkatdls)

**Audit result:** the propagation argument is valid. Insertion gives
\[
S(n)\le S(n-1)+\lceil\log_2 n\rceil.
\]
If \(L(n)-L(n-1)=\lceil\log_2 n\rceil\) and \(S(n-1)=L(n-1)\), then
\[
L(n)\le S(n)\le S(n-1)+\lceil\log_2 n\rceil=L(n),
\]
so \(S(n)=L(n)\).

For the exact increment condition, put \(x=\log_2((n-1)!)\), \(y=\log_2 n\), and \(q=\lceil y\rceil\). The increment is full precisely when
\[
\lceil x+y\rceil-\lceil x\rceil=q.
\]
If \(x\) is an integer, it is always full. Otherwise, writing \(t=\{x\}\), it is full exactly when
\[
t>q-y.
\]
The inequality is **strict**: equality gives a short increment. This also handles powers of two: when \(n\) is a power of two, \(y=q\), so every noninteger \(x\) gives a full increment; integer \(x\) does too. Equivalently, the exact test is simply the difference of ceilings above, which avoids fractional-part boundary mistakes.

Using exact factorials and \(L(m)=\lceil\log_2(m!)\rceil\), the independently recomputed increments for \(2\le n\le22\) are:

- **Full:** \(2,3,4,6,7,8,11,13,14,15,16,20\)
- **Short:** \(5,9,10,12,17,18,19,21,22\)

A purported criterion using \(\{x\}\ge q-y\) instead of \(>\) would incorrectly classify equality-boundary cases as full. Likewise, a fractional-part test that omits the integer-\(x\) case needs separate handling; powers of two make that omission especially visible.

This propagation establishes tightness **one step at a time**, when the previous value is tight and the increment is full. The finite list through 22 does not establish infinitely many tight \(n\): that would require an infinite supply of such propagation steps (or another argument). Nor does the calculation rule out tightness at later short-increment indices by some other route.

## Output 214 (msg_1fa0f64f9001vojvD0Dwg0gSam)

## Baseline correction and status check

- **Current main SHA (fetched `origin/main`): `6cddeaa2453d4da2ae0e918e50ba61c71a7da85f`.** The assigned worktree is at `6a96398d937d20977a91b9afa8619cb27feab269`.
- I read `git show origin/main:AGENTS.md` **and** the `origin/main` versions of `docs/problem.md`, `docs/literature.md`, `docs/operations.md`, `docs/research-plan.md`, `docs/research-n12-nontightness.md`, `docs/research-upper-witnesses.md`. `AGENTS.md` is byte-identical to the stale worktree copy. The diff `6a96398..6cddeaa` over those files changes only `docs/README.md` (+1 line); the substantive files are unchanged. Main added `docs/research-core-threshold.md` and related notes, which are unrelated to this claim. **Stale-baseline effect: none** on the audit inputs or conclusions.
- **#301 live board:** the front `info-tightness-infinite-20261120` (16:13:32Z) explicitly leaves the all‑n question **OPEN**; the 16:48:56Z front post calls the propagation lemma valid and makes no resolution claim; the 17:05:13Z and 17:06:08Z Viche corrections explicitly say “the propagation lemma remains valid and the all‑n tightness question remains open” and “the original propagation lemma and finite table are unchanged.” The durable frontier ledger has all related fronts `clearexit`/`failed` with open findings, none active. **Not superseded, still open.**

## Independent verification (from scratch)

**1. Propagation lemma — `deduction`.** Binary insertion gives `S(n) ≤ S(n−1) + ⌈log₂ n⌉` for all `n ≥ 2`. If `inc(n) := L(n)−L(n−1) = ⌈log₂ n⌉` and `S(n−1)=L(n−1)`, then `L(n) ≤ S(n) ≤ L(n−1)+inc(n) = L(n)`, so `S(n)=L(n)`. Sound; straightforward sandwich.

**2. Exact full-increment condition — `deduction`.** Let `x = log₂((n−1)!)`, `y = log₂ n`, `q = ⌈y⌉`. Then `inc(n) = ⌈x+y⌉ − ⌈x⌉`.
- If `y ∈ ℤ` (`n` a power of two): `inc(n)=y=q` — **always full**.
- Otherwise write `a = {x}`, `y_f = {y}`. If `a=0` (i.e. `(n−1)!` a power of two, relevant only at `n=3` since `n=2` is already a power of two): `inc(n)=q` — **full**. If `a>0`: `⌈x⌉=⌊x⌋+1`, and `inc(n)=q` iff `a+y_f>1`, otherwise `q−1`. Equality `a+y_f=1` gives the **short** increment (the inequality is strict). This matches the final thread correction (17:06:08Z) exactly, and matches my first answer’s equivalent form “integer `x` ⇒ full; else full iff `{x} > q−y`.”

**3. Recomputed table — `experiment`, two independent integer methods.** I computed `L(m)=⌈log₂ m!⌉` both by `(m!−1).bit_length()` and by an independent loop finding the least `k` with `2^k ≥ m!`; they agree for `0 ≤ m ≤ 29`. Exact results:

- **Full (2–22):** `{2,3,4,6,7,8,11,13,14,15,16,20}`
- **Short (2–22):** `{5,9,10,12,17,18,19,21,22}`

This matches the board’s corrected table and my earlier answer. Powers of two (`2,4,8,16`) are all full; `n=3` is full via the `a=0` branch. No equality case `a+y=1` occurs for `n ≤ 23`, but the strict criterion handles it. `n=23` is also a full increment, yet `S(22)=71 > L(22)=70`, so propagation cannot start there.

**4. Earlier incorrect criteria in the thread — audit.** The original 16:13 post’s fractional test omitted the integral-`log₂((n−1)!)` branch (`n=3` is the decisive counterexample). The 17:05 correction fixed only part of it: its stated criterion “non-power-of-two ⇒ full iff `a+y>1`” still misclassifies `n=3` (`a=0`, `a+y<1`), even though that post cites `n=3` as the counterexample — internally inconsistent. The 17:06 correction adds the `a=0` alternative and is correct. My first answer had already flagged both faults (omission of the integer case, and `≥` vs `>` at the equality boundary).

## What this does and does not imply

- It gives a **one-step transfer**: tightness at `n−1` propagates to `n` exactly when the information increment is full. It certifies no new value of `S(n)` without an independently established tight predecessor.
- The finite set through `n=22` does **not** establish infinitely many tight `n`; that needs an infinite chain of full-increment propagation steps (or another argument), which is not supplied. Nor does it rule out tightness at later short-increment indices by other means. The known pattern (equality through 11, gaps 12–19, equality at 20–21, gap at 22) remains finite evidence only.
- No theorem completion, no complexity-class consequence, no new repo/Lean artifact is claimed.

**Compliance:** reads and local computation only — no code, repo, Lean, ledger or board writes.
