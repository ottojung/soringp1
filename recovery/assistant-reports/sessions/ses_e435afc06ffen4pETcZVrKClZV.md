# antonina-J8OAui6rKQU6Q31OG8gr1i-cellar

Session: ses_e435afc06ffen4pETcZVrKClZV
Workspace: /home/lubko/soring-fronts/binomial-superadditivity-defect
Created: 1794166293692; updated: 1794167093577

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 548 (msg_1bcb05398001Oyv7oIGf1iGXR1)

Studied `AGENTS.md`, `docs/problem.md`, board #301, the Ford–Johnson/sorting-number literature, and the Stober–Weiß exact-value table. Worktree remains clean; no Lean or repository changes were made. I posted the finding to board #301.

## Mathematical finding

Let

- `C(n)=ceil(log2 n!)`, `E(n)=S(n)-C(n) >= 0`,
- `β(a,b)=floor(log2 binom(a+b,a))`,
- `δ(a,b)=C(a)+C(b)+β(a,b)-C(a+b)`.

Then `δ ∈ {-1,0,1}` always, and the claimed inequality

`S(a+b) >= S(a)+S(b)+β(a,b)-1`

is exactly equivalent to the **excess-superadditivity** statement

`E(a+b) >= E(a)+E(b)+δ(a,b)-1`.

So this is not an information-bound consequence. Plain superadditivity `S(a+b) >= S(a)+S(b)` does follow from ordinal-sum additivity plus extension monotonicity on the antichain. But the two-list merge bound applies to `Merge(a,b)` (two chains), not to antichain blocks, and no general-poset/direct-sum argument produces the binomial term. Certificate soundness for `S(n) <= k` gives upper bounds only; refuting this lower-bound claim requires an upper certificate at `a+b` and lower certificates at `a,b`.

## What the exact data show

Recomputing all pairs with `a+b <= 22` from the exact values `S(0..22)`:

- the inequality holds for every pair;
- the minimum margin is **0**, not `-1`;
- equality occurs at `(3,17),(3,18),(4,16),(4,17)`, and more.

Using exact values through 22, the Stober–Weiß intervals through 47, and the Ford–Johnson upper bound `F(n)`, no counterexample exists. The closest cases miss by **exactly one comparison**.

## Sharp obstruction

Let `d(n)=F(n)-S(n) >= 0`. The claim at `(a,b)` is equivalent to

`d(a+b) <= d(a)+d(b)+M(a,b)`,

where `M(a,b)=F(a+b)-F(a)-F(b)-β(a,b)+1`.

The first negative `M` for `a,b <= 30` is

`M(24,17) = -1`.

Since `S(17)=50=F(17)` and `S(41) <= F(41)=166`:

- if `S(24)=81`, then `81+50+37-1 = 167 > 166 >= S(41)`, so the claim is **false**;
- if `S(24)=80`, the claim forces `S(41) >= 166`, hence `S(41)=166`.

Thus the claim implies `S(24)=80` and `S(41)=166`. Similarly it forces `S(26)=89`, `S(27)=94`, `S(28)=99`, and then `S(42)=171`, `S(43)=177`. More generally it forces

`S(24..36) <= 80,85,89,94,99,104,109,115,120,125,130,135,140`,

so Ford–Johnson must be beaten at **every** `n=24..36`.

This is not a modest all-n lower-bound family: it is at least as hard as several open exact-value/algorithmic questions, including constructing an 80-comparison sorter for 24 and information-optimal sorters for 26 and 27.

## Failed approach / exact obstruction

No unconditional counterexample follows from current certified bounds. Every available refutation needs one new bit, for example:

`S(24)>=81`, `S(26)>=90`, `S(27)>=95`, `S(28)>=100`, or `S(41)<=165`.

Each would immediately refute the inequality with an explicit pair. Conversely, the natural proof route “Ford–Johnson is additive, then control the deficit” fails: `F` itself already violates the analogue at `(24,17)`, since

`F(24)+F(17)+β-1 = 167 > 166 = F(41)`.

For large balanced splits the FJ gap is asymptotically linear, so any proof must establish genuine non-additivity of the true deficit `d`, not merely merge accounting.

## Honest limit

This is a paper deduction plus finite exact arithmetic. It is **not** a proof of the claim and **not** a counterexample. It shows precisely where a disproof must come from and that the proposed inequality is much closer to the open exact-value frontier than its “one-bit strengthening” description suggests.

## Output 622 (msg_1bcb123a2001320PX48ZFy8IP0)

Recovery inspection completed; I did not repeat the research or post again.

Verified effects:

- **Board post:** exactly one comment exists for this front, authored `SoringP1 frontier: binomial-superadditivity-defect` at `2026-11-08T19:43:46.939Z`, ID `sha256:fZB-bF_f6zhxrEiENrs06ERCc57hYmq_Eg9hVg0VY1c`. No duplicate was made.
- **Git:** working directory `/home/lubko/soring-fronts/binomial-superadditivity-defect` is on `billy-dev`, clean, at `6a96398`. No commits or repository changes were created.
- **Local scratch:** only `/tmp/opencode/binomial_post.md` and `/tmp/opencode/post_result.json` remain from the completed turn. These are outside the repo.
- **Durable ledger:** `~/.local/state/soringp1/frontier-ledger.json` still records `binomial-superadditivity-defect` as `running`, with `started_at` populated. I did not edit it; status transition is keeper-managed.

The mathematical work and the single board report are complete. Nothing further was posted, committed, or purchased.
