# antonina-27p8O3RtyWL9QqoKv2PhdJ-talents

Session: ses_e3d4417b1ffeXGTgm6vdwYMNbz
Workspace: /home/lubko/soring-fronts/ford-johnson-eventual-optimality
Created: 1794268457316; updated: 1794269694044

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 718 (msg_1c2cc8f4f001kFttz72NFMA4Hc)

**Recovery/state.** No board post existed for `ford-johnson-eventual-optimality`; the worktree was clean at `6a96398`, and no prior repo/Lean/files effects were found. I saved scratch only under `/tmp/opencode`. I made exactly one new external effect: a single #301 comment at `2026-11-10T00:12:08Z`, verified unique by the board digest. The worktree remains clean.

## Mathematical finding

The front’s premise is outdated. The primary literature already proves much more than “strict at n=47”:

- **Manacher, JACM 26 (1979) 441–456:** constructively obtains infinitely many `t>189` with  
  `F(t)-S(t) = kt-O(log t)`, `k>0`. His winning bands are `t=(4/3)2^{k+f}`, `0<f<0.17`, first at `189..191` and widening. Hence Ford–Johnson is **not eventually optimal**.
- **Bui–Thanh, BIT 25 (1985) 70–75:** their FTBI merge proves `S(t)<FJ(t)` for whole consecutive ranges; their k=7 example is **every** `178<=t<=277`, and they state the pattern repeats for every k. They also record the `t=47` win: sort 5 and 42 by FJ, merge 5 into 42 in 22 comparisons, total `200<201`.

So the front’s dichotomy is not exhaustive: strict infinitely often is already known; infinite equality is not refuted; strict for every `n>=47` remains open.

## New elementary structural step

Let `D(n)=FJ(n)-S(n)` and `m=floor(n/2)`. Ford–Johnson first makes `m` pair comparisons, recursively sorts the `m` larger elements, then runs an insertion phase depending only on that sorted order. Replacing the recursive FJ sort by an optimal sorter for `m` saves exactly `D(m)`. Therefore

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

## Output 782 (msg_1c2cea9c0001gC0JBXgWRZZc0K)

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
