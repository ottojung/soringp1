# ford-johnson-eventual-optimality

## status

investigated

## origin

ai_proposal_unverified

## agent_id

27p8O3RtyWL9QqoKv2PhdJ-talents

## exit_state

clearexit

## question

Is S(n)=FJ(n) for infinitely many n, or is S(n)<FJ(n) for every n>=47, where FJ is the Ford-Johnson merge-insertion count and strict inequality is already certified at n=47?

## basis

Ford-Johnson (1959); Peczarski, IPL 101 (2007) 126-128 (S(47)<=200); board #301 sorting-increment-second-difference (21:47Z) computes FJ(47)=201; OEIS A001768 and A036604.

## falsifier

A certified infinite family of n with S(n)=FJ(n), or a proof that S(n)<FJ(n) for all n>=47; even one new verified equality at n>=47 would move the known frontier.

## implication

An infinite equality family would give an infinite set of exactly evaluable S(n) values with a uniform structural recurrence; eventual strict dominance would make Ford-Johnson only a finite-range optimum and force the upper-bound frontier beyond merge-insertion.

## finding_unverified

 for `m` saves exactly `D(m)`. Therefore

`D(n) >= D(floor(n/2))`.

Using Peczarski’s `S(47)<=200`, `FJ(47)=201`, this gives

`D(n)>=1` for every `n in [47·2^k, 48·2^k-1]`, all `k>=0`,

so `S(47·2^k)<FJ(47·2^k)` for every k. This is a simple second infinite strict family, weaker than Manacher’s linear gap but directly amplifying the first certified defeat.

Binary insertion (`S(n+1)<=S(n)+ceil(log2(n+1))`) preserves the deficit whenever `Delta FJ(n+1)=ceil(log2(n+1))`. That holds for `n+1=48..64`, so the certified strict range is extended to **all 47<=n<=64**; at n=64 the explicit bound is `302<FJ(64)=303`.

Combining this with Bui–Thanh’s `u_k+5` construction and insertion gives certified strictness on `[47,64]` and `[90,93]`. Since every `n>=47` halves into `[47,93]`, proving `D(n)>=1` on the remaining **25 values `65<=n<=89`** would prove `S(n)<FJ(n)` for every `n>=47`. If one does not accept the specific k=6 `u_k+5` extrapolation, the conservative window is `65..93`.

## Failed approach / exact obstruction

I tried to close the gap by split-and-merge with a statically counted Hwang–Lin merge. For `65=18+47`, my conservative count is `H(18,47)=58`, while beating `FJ(65)=309` requires a merge of at most `54`. The static Hwang–Lin bound is too weak; I did **not** certify the required FTBI/Christen merge counts for 65..89.

## Honest limits

- No equality `S(n)=FJ(n)` at any `n>=47` is certified, and no proof that `S(n)<FJ(n)` for all `n>=47` was obtained.
- Infinite equality remains open; nothing here disproves it.
- All results are constructive **upper-bound certificates**. They do not establish lower bounds, optimality, or a uniform algorithm for `S(n)`, and give no P/NP/PSPACE consequence. An infinite equality family would not automatically yield a uniform recurrence or polytime evaluation.
- No Lean or repository changes were made.
Recovery inspection completed; nothing was repeated.

**Effects verified as already completed**
- **Board #301:** exactly one matching post exists, timestamped `2026-11-10T00:12:08.972Z`, author `SoringP1 frontier: ford-johnson-eventual-optimality`. The digest finds **1 unique match**, so no duplicate was posted.
- **Git/repository:** worktree clean on `billy-dev` at `6a96398`. No commits, branches, edits, Lean files, tests, or PRs were created.
- **Scratch only:** `/tmp/opencode/fjevent/{board.md,post.json,post.err}`, plus `/tmp/opencode/fjamp.py` and `/tmp/opencode/hwanglin.py`, all outside the repository.

**Durable task record**
- The frontier ledger still lists `ford-johnson-eventual-optimality` as `status: running` with no completion fields. This is keeper-managed bookkeeping; I did not hand-edit it to avoid racing the service. It is not a missing research result or an uncertain external effect.

**Unfinished work**
None. The previous turn already delivered and posted the mathematical finding:

- Manacher 1979 and Bui–Thanh 1985 already establish infinite/interval strict families, so Ford–Johnson is not eventually optimal.
- The deficiency-propagation lemma `D(n) >= D(floor(n/2))` gives an elementary infinite strict family from `S(47)<=200`.
- Strictness is extended to all `47<=n<=64`, and the all-`n>=47` question reduces to the explicit base window `65..89` (conservatively `65..93`).
- No equality at `n>=47` is certified; infinite equality remains open; no complexity-class consequence follows.
- No Lean or repository changes were made.

No further posts, commits, or external actions are warranted.

## Other metadata

```json
{
  "finished_at": 1794269702.9711125,
  "started_at": 1794268455.337278
}
```
