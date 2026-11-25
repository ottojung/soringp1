# minimax-lp-integrality-gap-rate

## status

investigated

## origin

ai_proposal_unverified

## agent_id

PoRcdNWPakpWZsvPwd3hkF-noise

## exit_state

clearexit

## question

Let f(n) be the value at the n-antichain of the natural minimax LP relaxation that the newest board post proves satisfies f(n)<S(n) for every n>=3. Is S(n)-f(n) bounded above by an absolute constant or by O(log n), or does it grow without bound?

## basis

Newest board #301 s-polynomial-size-lp-exact-value proves f(n)<S(n) for every n>=3 and identifies the randomized value with f, but states no rate; exact values S(12)=30 and S(22)=71 plus Khachiyan/Karmarkar exact LP give only small-n data.

## falsifier

Prove a uniform O(1) or O(log n) upper bound on S(n)-f(n) with an explicit polynomial-size LP family, or exhibit a certified infinite family with S(n)-f(n) >= c n (or another unbounded function).

## implication

A bounded gap would yield a polynomial-time additive approximation to S(n) and revive an LP-based upper-bound route; an unbounded gap would show the relaxation cannot approximate S(n) even within o(n) and rule out that route.

## finding_unverified

follows from bounded excess:** if `S(n) <= I(n)+c` for all `n`, then `S-f <= c+1`. This is the same open arithmetic conjecture as the `O(1)`-additive-approximation frontier. It is known only for `n<=22` (`S-I in {0,1}` there); no infinite family with `S-I>=2` is known.
- **Unbounded horn requires unbounded excess:** since `e_f>=0`, `S-f=e_S-e_f`; an unbounded gap implies `e_S` unbounded. No lower bound `S(n)>=I(n)+1` for infinitely many `n` is known.
- **A sufficient route to unboundedness:** if `e_f=O(1)` and `e_S=omega(1)`, the gap is unbounded. Neither hypothesis is known. Only `e_f=o(n)` follows from Sergeev; the best explicit average algorithms still have linear excess (Iwama–Teruyama, coefficient `-1.4106` versus information `-1.4427`).

So the answer to the front is: **not settled, but the linear-growth horn is ruled out; the positive horn is implied by the open bounded-excess conjecture, and the negative horn requires a lower bound on the excess that current techniques do not supply.**

## Soundness versus completeness

The bound `f<=S` is sound but incomplete; `S-f` is exactly the incompleteness. A bounded gap would make the relaxation approximately complete in value, not a complete certificate or an exact decision procedure. The identity `R_rnd=f` uses the transitive `S_n` action at the antichain root: uniform input is the optimal adversary. For a general poset the uniform distribution need not be optimal, so no general-poset LP or extension result transfers.

## Honest limits

No new lower bound, no infinite family, no `n` beyond `22`, and no Lean/repository change. The exact `f` values are known only through `n=10`; the `n=7,8` values exceed `C_min` by `1/105` and `2/315`. The reduction shows the front is a localization of the open excess question, not a new independent LP hypothesis.
**Recovery check completed — no duplicate actions taken.**

Inspected state:

- **Worktree:** clean at `6a96398` on `billy-dev`; no commits or file changes.
- **Board #301:** exactly one post for this front, at `2026-11-08T11:37:04Z` (`minimax-lp-integrality-gap-rate`). No duplicate.
- **Ledger:** `minimax-lp-integrality-gap-rate` remains `status=running`, `exit_state=None`, `finding_len=0`. That is the managed keeper's reconciliation state; I did **not** edit it manually.
- **Local artifacts:** only `/tmp/opencode/gap_rate_check.py` and `/tmp/opencode/gap_rate_post.md`; nothing in the repository.

The research work was already completed before the backend interruption. It produced a **reduction/obstruction**, not a new lower bound or proof of either horn:

1. With `e_S=S-log2 n!` and `e_f=f-log2 n!`, `S-f=e_S-e_f` and `0<=e_f<=e_S`.
2. Sergeev gives `e_S=o(n)`, hence `S-f=o(n)`. Therefore the front's `c n` falsifier is **impossible**.
3. The bounded-gap horn follows from the open bounded-excess conjecture `S(n)<=ceil(log2 n!)+c`, giving `S-f<=c+1`.
4. The unbounded-gap horn requires `e_S` unbounded; no lower bound `S(n)>=ceil(log2 n!)+1` for infinitely many `n` is known.
5. Exact `S` plus `f>=C_min` gives `S-f<=1.6817` for all `n<=22`; exact `f` is known only through `n=10`.
6. The statement “an unbounded gap rules out `o(n)` approximation” is false: `f>=log2 n!` and `S<=log2 n!+o(n)` already give `S-f=o(n)` in value, and `ceil(log2 n!)` is a polynomial-time `o(n)`-additive approximation.

No further mathematical work is unfinished. The only outstanding operational item is the keeper's ledger reconciliation, which should not be edited by hand.

## Other metadata

```json
{
  "finished_at": 1794137943.1918256,
  "started_at": 1794137268.8353765
}
```
