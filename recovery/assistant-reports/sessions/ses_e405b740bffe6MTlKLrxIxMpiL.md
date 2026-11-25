# antonina-hy3AEo18u1SdUQZ5SHQXP2-osteoma

Session: ses_e405b740bffe6MTlKLrxIxMpiL
Workspace: /home/lubko/soring-fronts/fixed-free-block-insertion-defect
Created: 1794216594531; updated: 1794224492589

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1bfa48e4e001FwQoflmuQUd82W)

I'll start by studying the repository context and the current research board.

## Output 98 (msg_1bfa4e4ab001yVNf2b2uswyT4o)

I have the full board context. Let me set up an exact solver for the family `C_m ⊔ A_r` and compute `D_3(m)`.

## Output 902 (msg_1c01b03e7001yY2AcG1epAVR1j)

## Result

I studied `AGENTS.md`, `docs/problem.md`, the current board, and the Hwang–Lin primary source, then attacked the front's all-`r` claim. I did **not** falsify it, and I did **not** prove `D_3(m)≤1` for all `m`. The substantive finding is a boundary identity that changes the status of the front.

### 1. Mathematical finding: the front's boundary is the global sorting excess

Let `E(t)=S(t)-ceil(log2 t!)`. For the front's family,

\[
D_r(m)=F(C_m\sqcup A_r)-ceil(\log_2((m+r)!/m!)).
\]

Then for every `r≥1`:

\[
\boxed{D_r(0)=E(r)\qquad\text{and}\qquad D_r(1)=E(r+1).}
\]

Proof: `C_0` is empty, so `C_0⊔A_r=A_r`. For `m=1`, the single chain element is incomparable with every free element and the free elements are mutually incomparable, so `C_1⊔A_r=A_{r+1}`. Both are ordinary antichain sorting instances.

Consequences:

- If the bounded horn holds for **every** fixed `r` and all `m`, then `E(n)≤1` for every `n`, i.e.
  \[
  S(n)\le ceil(\log_2 n!)+1\quad\text{for all }n.
  \]
  This is a major open statement. Exact values only establish `E≤1` through `n=22` (`S(12)=30` vs `29`, `S(22)=71` vs `70`); `n=23` is open. The best published asymptotic excess is `o(n)`, not `O(1)`.
- If `E` is unbounded, then `sup_m D_r(m)≥D_r(0)=E(r)` is unbounded, so the growth horn automatically holds.
- A certified falsifier `D_r(m)≥2` is available exactly when some `r` has `E(r)≥2` (use `m=0`) or `E(r+1)≥2` (use `m=1`). No such `r` is currently known.

So the all-`r` bounded horn is **not** a self-contained fixed-size insertion law. It contains the global one-comparison sorting-excess problem at its boundary.

### 2. Exact `r=3` evidence and a concrete failed approach

Using exact minimax over linear extensions:

- `D_3(m)∈{0,1}` for `0≤m≤31`, with `D_3(m)=1` at `m=3,4,6,8,9,10,14,16,17,18,20,21,22,23,30` and `0` otherwise.
- `D_4(m)≤1` for `0≤m≤11`; `D_5(m)≤1` for `m≤4`.
- No `D_r(m)≥2` was found.

The natural “sort the three free keys, then merge” proof fails:

- `K(3,14)=11` while `I=ceil(log2 binom(17,3))=10`; sort-first costs `14`, but `C_P(14)=12` and the exact optimum is `F_3(14)=13`. So the optimal tree is genuinely interleaved.
- At `m=38`, `K(3,38)=15` (`I=14`; the Hwang–Lin generalized binary algorithm also gives `15`). All four natural pipelines cost `18` while the target is `17`. Nevertheless, an exact search found a height-`17` tree, so `D_3(38)≤1`.

Thus any all-`m` proof must use interleaved comparisons; no combination of the published sort/merge/insertion bounds suffices.

### 3. A second obstruction: the `δ≤1` route is false for `r=3`

With

\[
\delta_r(m)=F_r(m)-S(m+r)+S(m)\ge 0,\qquad
\eta_r(m)=C_P(r,m)-C(m+r)+C(m)\in\{0,1\},
\]

one has

\[
D_r(m)=E(m+r)-E(m)+\delta_r(m)-\eta_r(m).
\]

Using exact `S(16..21)`, `δ_3(16)=δ_3(17)=δ_3(18)=2`. So the natural strengthening `δ≤1` is false already for `r=3`; `D` stays `1` only because `η=1` or `E` decreases. This independently kills the lower-bound route based on `δ≤1`.

### 4. Soundness vs completeness

- Explicit insertion/merge trees are **sound upper certificates**.
- The leaf count `ceil(log2 e)` is a **sound lower certificate**.
- General-poset entropy/capacity theorems are sound but only multiplicative/asymptotic; they do not give the additive `+1`.
- Hwang–Lin explicitly call exact `K(3,n)` “very difficult”; only `K(2,n)` is exact in that paper.
- No available lower-bound method certifies the tight `m=14` or `m=38` instances; exact minimax does.

### 5. Honest limits

I did not prove `D_3(m)≤1` for all `m`, and I did not find a counterexample. The universal bounded horn cannot be settled by fixed-`r` insertion work alone: it implies `E(n)≤1` for all `n`, while any `n` with `E(n)≥2` would immediately give a falsifier at `m=0` or `m=1`.

The decisive next tests are:

1. find any `n` with `E(n)≥2` — this gives a certified `D_r(m)≥2`;
2. prove `D_3≤1` for all `m` by a genuinely interleaved construction;
3. exhaust the remaining finite discriminator at `m=38` (`h=16` feasibility).

I posted this to board #301 under the front’s author. The worktree remains clean at `6a96398`; no repository or Lean changes were made.

## Output 998 (msg_1c01cc0e6001IKGEqZ8JOp04X4)

## Recovery inspection

I checked the conversation, working tree, Git state, board #301, and the frontier ledger before doing anything.

**Effects that actually happened in the previous turn**

- **Board post: completed exactly once.**  
  Author: `SoringP1 frontier: fixed-free-block-insertion-defect`  
  Timestamp: `2026-11-09T11:39:02.751Z`  
  ID: `sha256:ZdkBD-yCV9E8gauFcKqyk2oEai2ZIg58sdqkZ8-R-Q8`  
  I searched board pages 1–3: there is **exactly one** matching post. I did **not** repost.

- **No repository changes.**  
  `git status --porcelain` is empty, no stash entries, HEAD remains `6a96398`. No commits, PRs, or Lean changes were made.

- **Scratch computation only.**  
  Solver scripts and result files are confined to `/tmp/opencode/defect`; they are not repository state.

**Durable task record**

The frontier ledger still shows `fixed-free-block-insertion-defect` with `status: "running"` and no `finding_unverified`. That entry is keeper-managed, so I did **not** manually edit it. The keeper reconciles it from agent status/output; manually changing it could race with the service.

**Unfinished work**

Nothing mathematical is unfinished from the previous turn. The finding was posted, the worktree is clean, and the report was delivered. The only pending operational step is the keeper advancing the ledger entry from `running`; that is external to the research result.

**No duplicate or uncertain external action remains.** The board post is confirmed, unique, and matches the intended content.
