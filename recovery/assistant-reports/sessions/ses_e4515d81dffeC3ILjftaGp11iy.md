# antonina-PoRcdNWPakpWZsvPwd3hkF-noise

Session: ses_e4515d81dffeC3ILjftaGp11iy
Workspace: /home/lubko/soring-fronts/minimax-lp-integrality-gap-rate
Created: 1794137270393; updated: 1794137935479

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 20 (msg_1baea3e33001tA8j6zgWGaieDC)

I'll start by inspecting the current state: working directory, Git status, and any durable records of prior work, before touching anything.

## Output 480 (msg_1baf2e5d3001cArNs6h1McNDuQ)

**Recovery audit.** The worktree is clean at `6a96398`; no commits, repo files, or Lean files were touched. The ledger entry `minimax-lp-integrality-gap-rate` had no prior finding and board #301 had no post for this front, so nothing was duplicated. One new board post was made at `2026-11-08T11:37:04Z`. Checks are in `/tmp/opencode/gap_rate_check.py`; the post text is `/tmp/opencode/gap_rate_post.md`.

## Mathematical finding

Let

- `I(n)=ceil(log2 n!)`,
- `e_S(n)=S(n)-log2 n!`,
- `e_f(n)=f(n)-log2 n!`,
- `C_min(n)=(q+1)-2^q/n!`, `q=I(n)`, the unrestricted Kraft minimum for a binary tree with `n!` leaves.

Then `C_min=log2 n!+rho(n)` with `0<=rho(n)<=0.086071`.

**Exact bookkeeping.** Every correct comparison tree has exactly `n!` leaves after pruning one-child nodes, so Kraft/Jensen gives

```
f(n) >= C_min(n) >= log2 n!
```

and therefore

```
0 <= e_f(n) <= e_S(n),
S(n)-f(n) = e_S(n)-e_f(n).
```

Moreover `S-f <= S-C_min = (S-I)+(I-log2 n!)-rho`.

**The front's `c n` falsifier is impossible.** Sergeev (ECCC TR20-096, Thm. 3; 2021 journal version) proves

```
S(n) = log2 n! + O(n/(log n)^(1/5)) = log2 n! + o(n).
```

Hence

```
0 <= S(n)-f(n) <= e_S(n) = o(n).
```

No infinite family can have `S(n)-f(n) >= c n`, or even `>= n/polylog(n)`. The strongest unconditionally available upper bound is `O(n/(log n)^(1/5))`.

**The complexity implication in the front is misstated.** Since `f >= log2 n!` and `S <= log2 n!+o(n)`, the natural LP value already satisfies `S-f=o(n)` in value. An unbounded gap (necessarily `o(n)`) therefore does **not** rule out an `o(n)` additive approximation. In fact `I(n)=ceil(log2 n!)` is polynomial-time computable from `1^n` and is already an `o(n)`-additive lower approximation to `S`, independently of any LP. A bounded gap would add only constant-additive approximation in value; it would not produce a polynomial-size LP, since the tree LP has `n!` variables/constraints. A polynomial-size explicit LP with value `S` is exactly `S_unary in FP`.

**Small-`n` exact data.** For `n=3..10`, using exact `S` and the known exact `f` values:

```
n=3: 1/3, 4: 1/3, 5: 1/15, 6: 19/45,
7: 194/315, 8: 13/21, 9: 1261/2835, 10: 2209/14175.
```

The largest is `0.6190` at `n=8`. For all `n<=22`, exact `S(n)` plus `f>=C_min` gives the unconditional bound

```
S(n)-f(n) <= max_n (S-C_min) = 1.6817
```

(the maximum of the bound is at `n=15,16`). So the bounded horn is verified with constant `<2` through `n=22`, but this uses exact `S(n)` only up to `22`.

## Exact obstruction

The front is not an independent LP question. It is a localization of the open “excess” question:

- **Bounded horn follows from bounded excess:** if `S(n) <= I(n)+c` for all `n`, then `S-f <= c+1`. This is the same open arithmetic conjecture as the `O(1)`-additive-approximation frontier. It is known only for `n<=22` (`S-I in {0,1}` there); no infinite family with `S-I>=2` is known.
- **Unbounded horn requires unbounded excess:** since `e_f>=0`, `S-f=e_S-e_f`; an unbounded gap implies `e_S` unbounded. No lower bound `S(n)>=I(n)+1` for infinitely many `n` is known.
- **A sufficient route to unboundedness:** if `e_f=O(1)` and `e_S=omega(1)`, the gap is unbounded. Neither hypothesis is known. Only `e_f=o(n)` follows from Sergeev; the best explicit average algorithms still have linear excess (Iwama–Teruyama, coefficient `-1.4106` versus information `-1.4427`).

So the answer to the front is: **not settled, but the linear-growth horn is ruled out; the positive horn is implied by the open bounded-excess conjecture, and the negative horn requires a lower bound on the excess that current techniques do not supply.**

## Soundness versus completeness

The bound `f<=S` is sound but incomplete; `S-f` is exactly the incompleteness. A bounded gap would make the relaxation approximately complete in value, not a complete certificate or an exact decision procedure. The identity `R_rnd=f` uses the transitive `S_n` action at the antichain root: uniform input is the optimal adversary. For a general poset the uniform distribution need not be optimal, so no general-poset LP or extension result transfers.

## Honest limits

No new lower bound, no infinite family, no `n` beyond `22`, and no Lean/repository change. The exact `f` values are known only through `n=10`; the `n=7,8` values exceed `C_min` by `1/105` and `2/315`. The reduction shows the front is a localization of the open excess question, not a new independent LP hypothesis.

## Output 537 (msg_1baf43922001ZoDjsjFHZR2eTf)

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
