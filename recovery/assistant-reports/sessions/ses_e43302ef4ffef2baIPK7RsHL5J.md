# antonina-jPIFgTf1G3Vm9aRf68drjE-morally

Session: ses_e43302ef4ffef2baIPK7RsHL5J
Workspace: /home/lubko/soring-fronts/single-bit-excess-dichotomy
Created: 1794169098600; updated: 1794169858444

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 505 (msg_1bcda8834001OuDa9bGpfETCtT)

Recovery check: the worktree was clean, the ledger entry `single-bit-excess-dichotomy` had no recorded finding, and board #301 had **zero** prior posts for this front. I therefore posted exactly one finding, at `2026-11-08T20:29:48Z`; I did not duplicate anything and made no repo/Lean changes.

## Mathematical outcome

**No counterexample and no proof.** The front remains open, but it has a sharp first test point.

Let `C(n)=ceil(log2 n!)`, `E(n)=S(n)-C(n)`, and `F(n)` be the Ford–Johnson count.

1. **First non-automatic index is `n=25`.**  
   - For `n<=22`, published exact values give `E in {0,1}`.
   - For `n=23,24`, `S(n)<=F(n)=C(n)+1`, so `E<=1` is automatic.
   - At `n=25`, `C(25)=84` and `F(25)=86`. Hence `E(25)<=1` is exactly `S(25)<=85`. A falsifier is exactly `S(25)=86`, i.e. a certified lower bound `S(25)>=86`. The published range is `84..86`.

2. **The split-merge class already fails at `n=25`.**  
   Peczarski (IPL 101, 2007) proves that for `n<47` no split-merge algorithm—sort `m` and `n-m` by Ford–Johnson, then merge—beats Ford–Johnson. At `n=25` every such algorithm has height at least `F(25)=86=C(25)+2`. Thus bounded excess one is false throughout that architecture class at `n=25`; any sorter witnessing `E(25)<=1` must be genuinely non-split-merge. This is a class-restricted counterexample, not a counterexample for `S`.

3. **Sharp finite target at `n=47`.**  
   `C(47)=198`, `F(47)=201`, and `S(47) in {198,199,200}`. Thus `E(47)<=1` iff `S(47)<=199`; `S(47)=200` would be the first two-bit excess. Current certified lower bound is only `198`.

4. **Consequence for Ford–Johnson.**  
   If `E(n)<=1` for all `n`, then
   \[
   F(n)-S(n)\ge c_0 n-O(\log n),\qquad c_0=\log_2 3-3+1/\ln 2=0.0276575\ldots
   \]
   So bounded excess one would force a uniform linear additive improvement over Ford–Johnson, not merely infinite non-optimality.

5. **Barrier to the natural lower-bound route.**  
   The `t`-ply extension-count lookahead is exactly `C(n)` at `A_n` for `t<=floor(n/2)`. Thus it cannot certify `E(n)>=2` without depth at least `floor(n/2)+1`: depth `13` at `n=25`, depth `24` at `n=47`. Local poset excess and certificate soundness do not transfer to the antichain root; the missing ingredient remains the all-strategy root quantifier.

**Honest limits:** this is a reduction and obstruction, not a resolution. No counterexample was found; no all-`n` proof was found. The exact gap is a certified lower-bound gap: current values reach only `C` at `25,26,27` and `C+1` at `28`, while a falsifier needs `C+2`.

## Output 559 (msg_1bcdb4eef00177IGiWWNoVXQSM)

Recovery audit complete. I did **not** repeat the prompt or create any new external effect.

## Effects that actually happened

- **Board #301:** exactly **one** comment from this front exists:
  - author: `SoringP1 frontier: single-bit-excess-dichotomy`
  - timestamp: `2026-11-08T20:29:48.068Z`
  - the durable body matches the prepared text exactly modulo a stripped trailing newline; no duplicate post was made.
- **Repository:** worktree clean on `billy-dev` at `6a96398d937d20977a91b9afa8619cb27feab269`; no commits, edits, Lean files, or tests.
- **Scratch only:** `/tmp/opencode/single-bit-post.md` and `/tmp/opencode/single-bit-post-result.json`, outside the repository.
- **Durable ledger:** `single-bit-excess-dichotomy` remains `status: running`, `exit_state: None`, `finding_unverified: None`. This is the expected keeper-managed active-agent state; I did not edit it.

## Unfinished work

None. The previous turn had already completed the investigation and posted the finding. The mathematical result stands as reported:

- no counterexample and no all-`n` proof;
- first non-automatic index is `n=25`;
- split-merge class already has excess `2` there;
- `n=47` is a sharp finite falsifier target (`S(47)>=200` would refute);
- extension-count lookahead needs depth at least `floor(n/2)+1`, so the standard local counting route cannot establish the first counterexample;
- the complexity equivalence to the tightness set only localizes the hardness, it does not make exact `S(n)` easy.

No uncertain external effect remains.
