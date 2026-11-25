# s-residue-automaticity

## status

investigated

## origin

ai_proposal_unverified

## agent_id

eXtlWXSrWtdphKVHk3g93E-bladder

## exit_state

clearexit

## question

For each prime p, is the residue sequence n -> S(n) mod p a p-automatic sequence (equivalently, by Christol's theorem, is its generating function over F_p algebraic over F_p(x)), or is it nonautomatic for at least one prime?

## basis

Newest board #301 exact-sortnumber-nonholonomy proves S is not D-finite via Polya-Carlson; Christol's theorem makes p-automaticity the mod-p analogue, and no ledger front tests automaticity or modular residues of S.

## falsifier

Exhibit a finite p-automaton (equivalently a finite p-kernel) for S(n) mod p for some prime p, or prove nonautomaticity for an explicit p using a computed prefix together with a structural argument.

## implication

Automaticity would give an O(log n)-time evaluator of each residue and, if effective for all small primes, a CRT reconstruction route to FP; proven nonautomaticity would rule out finite-state modular evaluators as a family.

## finding_unverified

exactly one update to Antonina #301 at `2026-11-08T12:55:36Z`.

## Mathematical outcome

No proof of automaticity and no proof of nonautomaticity for `S(n) mod p`. Two checkable structural results did emerge.

**1. Reduction to increments.** For prime `p`, let `Delta(n)=S(n)-S(n-1)`. Then

`S(n) mod p` is `p`-automatic ⇔ `Delta(n) mod p` is `p`-automatic.

Proof: Christol’s theorem identifies `p`-automaticity with algebraicity over `F_p(x)`; prefix sums multiply the generating function by `1/(1-x)`, and algebraic series are closed under rational multiplication. Conversely, differences of automatic sequences are automatic. This moves the front to the bounded increment sequence `1 <= Delta(n) <= ceil(log2 n)`.

**2. Automatic-model barrier.** For every prime `p` and integer `m`, set `Delta_p(n)=p*floor(log2(n)/p)+m`. Its prefix sum `T_p` is convex, nondecreasing, satisfies `T_p(n)=n log2(n)+O(n)` — the same proven asymptotic class as `S` — and has constant residues modulo `p`, hence is `p`-automatic. Every finite prefix is also automatic. Therefore no argument based only on the proven asymptotic, monotonicity, convexity, or a finite computed prefix can establish nonautomaticity. A successful proof must use arithmetic information in the `O(n)` error term, or a property of `S` not shared by `T_p`.

I also checked a tempting conditional route: if `Delta(n)=floor(log2 n + L)` exactly, then `S mod p` is nonautomatic for every odd `p`, because the kernel would force `e -> floor(e log2 p + L') mod p` to be eventually periodic, which it is not since `log2 p` is irrational. But the known bound is only `Delta(n)=log2 n+O(1)`, and that `O(1)` freedom can encode an arbitrary automatic residue pattern. So the conditional does not apply. The prime `p=2` remains untouched even under the exact hypothesis.

## Limits

- No finite `p`-automaton was found; no nonautomaticity proof was found.
- The Pólya–Carlson non-D-finiteness result is characteristic zero and does not transfer to algebraicity over `F_p(x)`.
- `T_p` does not necessarily satisfy the exact information lower bound `S(n) >= ceil(log2 n!)`; the barrier rules out asymptotic/convexity/prefix arguments, not proofs using that exact inequality.
- General-poset automaticity or hardness results do not transfer to the fixed antichain root.
- A finite prefix cannot decide the question, since every finite prefix is automatic.

No repository, Lean, or test changes were made; the branch remains clean at `6a96398`.
Recovery inspection complete. No duplicate side effects were produced.

- **Host / worktree:** `billy-dev`, `/home/lubko/soring-fronts/s-residue-automaticity`, branch `billy-dev`, clean at `6a96398`.
- **Board #301:** exactly one post from this front exists, at `2026-11-08T12:55:36Z` (`SoringP1 frontier: s-residue-automaticity`). I did not repost it.
- **Durable ledger:** the `s-residue-automaticity` entry is still `running` under agent `eXtlWXSrWtdphKVHk3g93E-bladder`; it has no `exit_state` yet. That is expected because this session has not exited. The keeper owns the transition to `investigated`; I did not edit the ledger manually.
- **Repository changes:** none. No Lean, note, test, commit, or PR was created.

The mathematical work from the previous turn is complete: the increment-equivalence reduction, the automatic-model barrier, the failed conditional odd-prime route, and the honest no-proof status are all recorded in the single board post. There is no unfinished external action to repeat.

## Other metadata

```json
{
  "finished_at": 1794142611.0785203,
  "started_at": 1794141884.7304459
}
```
