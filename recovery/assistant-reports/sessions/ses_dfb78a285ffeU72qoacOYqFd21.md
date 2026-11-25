# antonina-xD8w6xui28g1KFNvajP0Gs-sanguine

Session: ses_dfb78a285ffeU72qoacOYqFd21
Workspace: /home/lubko/soring-fronts/excess-one-band-polynomial-decision-alln
Created: 1795372310092; updated: 1795372610086

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_20487640b001inE8XohKM5H55e)

I'll start by exploring the repository structure and reading the key documents.

## Output 21 (msg_204877a98001BpzJh5rUT5ogYJ)

I'm on branch `billy-dev`. Let me read the key documents and find the board.

## Output 40 (msg_204878416001A2MviyfXfhjzWh)

Now let me check the research board and the frontier ledger for the relevant context.

## Output 55 (msg_20487ab33001AG4eFKpS67Igyb)

Let me get the full text of the key board posts and find the current front's ledger entry.

## Output 79 (msg_20487e67e001GbTJ8rv7Qg3uam)

Let me get the full text of the key prior board posts to understand exactly what was already established.

## Output 113 (msg_204883e55001H7re0Z1uew72Hu)

Let me fetch the full board JSON to a file and extract the key posts.

## Output 124 (msg_204884f8d001y42zsNXZCtp0Qw)

I have a thorough picture of the prior findings. Let me check a few more repo docs and then study the primary literature to ground the mathematical claims.

## Output 148 (msg_204895936001gmvjU4jFt513n4)

Let me study the primary literature to ground the mathematical claims about the excess.

## Output 190 (msg_204899e72001lJnmk3inZeAt0L)

Let me compute the dyadic data and test candidate predicates against known values.

## Output 208 (msg_20489d41d001Oll4NpJuE3ygcN)

Let me check for any prior scratch work (in case of resumption) and verify board posting conventions.

## Output 228 (msg_2048a77320016o2NgpRvwW5WTi)

I have a clear mathematical picture. Let me verify the board posting command syntax, then compose the finding.

## Output 239 (msg_2048aae65001BhyJ7dLYK8dEuB)

I've completed the mathematical analysis. Let me write up the finding for board #301.

## Output 250 (msg_2048aded2001CDaUU3vo2uTuk3)

Let me verify the numerical values in my write-up before posting.

## Output 270 (msg_2048b1a0c001GadLaimEGWor5o)

Now let me post the finding to board #301.

## Output 290 (msg_2048b8009001o6cz19X6tHvK0o)

The finding is posted. Let me confirm the worktree remains clean.

## Output 301 (msg_2048b9267001iS3hyTdrFFD6Oy)

## Report: `excess-one-band-polynomial-decision-alln`

I studied the contract, `docs/problem.md`, the primary literature (OEIS A036604/A003070, Sergeev ECCC TR20‑096, Stober–Weiss), and the full 16:24Z/16:27Z/17:41Z board posts, then attacked the front from all three falsifier directions. **The result is honest negative / exact obstruction, not a theorem.** No repository, Lean, test, or ledger changes; worktree is clean at `6a96398`. The finding is posted as the single #301 comment for this front.

### The mathematical finding

Let `C(n)=ceil(log2 n!)`, `D(n)=S(n)−C(n)`, and write **P1** for the open conjecture `D(n)≤1 for all n`:

- **Unconditional deduction:** `P1 ⇒ BAND_1 = {1ⁿ}` ⇒ `BAND_1 ∈ P` via the constant‑accept decider, *without computing S(n)*. Contrapositive: `BAND_1 ∉ P ⇒ sup D ≥ 2` (P1 false). Also `S ∈ FP ⇒ BAND_1 ∈ P`.
- So BAND_1's complexity is **not an independent question**: it is implied by the still‑open conjecture P1, and its hardness would refute P1. The front's dichotomy reduces to a tautology about correctness proofs (a correct decider rejects exactly where `D(n)≥2` and accepts exactly where `D(n)≤1`); it cannot be disproved because it has no content beyond "proving BAND_1 ∈ P requires proving the answers." A minor correction: for a decider with a finite rejection set, **both** fact kinds are needed (infinitely many `D(n)≤1` acceptances plus the rejections), not an either/or.

### Concrete failed approaches

1. **Dyadic predicate (horn 1):** once "signature" only means "poly‑time computable from unary n," this *is* `BAND_1 ∈ P` — no weaker notion exists. Natural surrogates fail even on the D=0/D=1 split: slack `1−frac(log2 n!)` is `0.749507` at n=11 (D=0) and `0.749860` at n=15 (D=1); the cheap‑zone‑count predicate is already false at n=9.
2. **Two n, opposite BAND_1 status (horn 2):** requires an n with `D(n)≥2`; none is known (all n≤22 have D∈{0,1}, S(23) open, C(23)=75). If P1 holds, no such pair exists. Blocked by the very conjecture it would test.
3. **"Every decider must certify excess ≥ 2" (horn 3):** false if P1 holds (constant‑accept is correct). Its truth also hinges on P1.

### Honest limits

No improved bound, algorithm, class placement, separation, falsifier, or new theorem. General‑poset hardness was not invoked (no reduction to the antichain root), certificate *soundness* was not confused with *completeness*, and sparsity/Mahaney was kept in its proper many‑one scope. The exact obstruction is P1: every branch of this front collapses to the open question `S(n) ≤ ceil(log2 n!)+1` for all n, or to the absence of a compact excess‑≥2 certificate (unknown even at n=12).

## Output 326 (msg_2048bd344001i3jiIF3lnKhjp7)

**Recovery check (no actions repeated).**

- **Git/worktree**: `/home/lubko/soring-fronts/excess-one-band-polynomial-decision-alln`, branch `billy-dev`, `git status` clean, HEAD `6a96398`. No commits or repo files were created by this session.
- **Board #301**: the front’s result is already posted once — `[2026-11-22T18:36:17.597Z] SoringP1 frontier: excess-one-band-polynomial-decision-alln` (honest negative / exact obstruction; no falsifier achieved; no theorem completion). I did **not** repost it.
- **Other side effects**: none detected (no PRs, no ledger edits, no purchases). Scratch files exist only under `/tmp/opencode/`.

**Status**: the requested investigation is complete. The finding was: `P1: D(n)=S(n)-ceil(log2 n!) <= 1 for all n` implies `BAND_1 ∈ P` by constant accept (without computing `S(n)`), and `BAND_1 ∉ P` would refute P1; horn 1 is just `BAND_1 ∈ P` in disguise, horn 2 requires an unknown `D(n)>=2` witness, horn 3 is false under P1. The front’s dichotomy is a tautology about correctness proofs; the exact obstruction is P1 / absence of compact excess-≥2 certificates. No further work is pending from this session.
