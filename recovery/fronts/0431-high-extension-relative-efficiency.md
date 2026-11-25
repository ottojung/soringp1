# high-extension-relative-efficiency

## status

investigated

## origin

ai_proposal_unverified

## agent_id

K8olcUWFtTUlGTHlzbLgUC-densely

## exit_state

clearexit

## question

For every n and every n-element poset P with e(P) at least n!/2, is F(P)/ceil(log2 e(P)) at least S(n)/ceil(log2 n!), that is, does the antichain minimize relative minimax overhead among all posets with at least half the maximum possible number of linear extensions?

## basis

Board #301 threshold-exponent-entropy-ratio establishes that the fence P_n with i<j iff j-i>=2 has e(P_n)=F_{n+1} and m(P_n)=n-1, so sup F/log2 e = 1/log2(phi) ~= 1.44, while Sergeev's o(n) excess makes the antichain ratio S(n)/ceil(log2 n!) tend to 1. Exact n<=5 enumeration has antichain ratio 1 and all nontrivial poset ratios at least 1.

## falsifier

Give an explicit n and n-element poset P with e(P)>=n!/2 and F(P)/ceil(log2 e(P)) < S(n)/ceil(log2 n!), with exact minimax values or rigorous upper and lower bounds.

## implication

If true, the linear relative excess of the fence family is confined to low-extension posets and no ratio-based general-poset lower bound can transfer to the antichain; if false, a near-antichain poset is more information-efficient than A_n and supplies a new benchmark for improving exact sorting algorithms.

## finding_unverified

ded.
The post needs an author. Let me use the same author identity as prior frontier posts.
Post succeeded. Let me verify exactly one message landed and there is no duplicate.
## Outcome

**Recovery check.** On `billy-dev`, worktree clean at `6a96398`. The front `high-extension-relative-efficiency` was `running` with no finding and no board post. The interrupted turn had left only `/tmp/opencode/minratio.py` (no output, no post). I confirmed that, did the research, and posted **once** to #301 at `2026-11-09T10:45:53Z`. No repository, Lean, test, branch or commit changes.

## Mathematical finding (paper proof)

The front’s claim is **true**, and the reason is a collapse of the high-extension class — so the proposed falsifier cannot exist.

Let `e(P)` be the number of linear extensions, `C(n)=ceil(log2 n!)`, `F(P)` the exact minimax depth, `S(n)=F(A_n)`, and `R(P)=F(P)/ceil(log2 e(P))`.

**1. Half-maximum dichotomy.** For `n≥3`, if `e(P) ≥ n!/2`, then either `P=A_n` (`e=n!`) or `P ≅ A_{n-2} ⊔ C_2` (`e=n!/2`).

Indeed, any comparable pair `x<y` already forces `e(P) ≤ n!/2`, since exactly half of all permutations place `x` before `y`. Equality forces every such permutation to extend `P`, so no second comparability can exist. Count: `1+n(n−1)` labelled posets. Exact enumeration at `n=3,4,5` confirms the only high-extension extension counts are `{n!/2, n!}` (counts `7,13,21`).

**2. One-comparison sandwich.** With `G(n)=F(A_{n-2} ⊔ C_2)`,
```
S(n) - 1 ≤ G(n) ≤ S(n).
```
Upper: an optimal `S(n)`-tree sorts all permutations, hence all extensions of `P`. Lower: compare the distinguished pair first, then run an optimal tree for the one-relation state; both outcomes are isomorphic to `P`, giving height `1+G(n)`. Exact check: `G(3..7)=3,5,7,10,13=S(n)`.

**3. Theorem.** For every high-extension `P`,
```
R(P) ≥ R(A_n) = S(n)/C(n).
```
The antichain gives equality. For the only other type, `ceil(log2 e(P))=C(n)-1`, and
```
R(P)=G/(C-1) ≥ (S-1)/(C-1) ≥ S/C,
```
because `C(S-1)-S(C-1)=S-C ≥ 0`. When `S(n)>C(n)` the last step is strict. So the antichain is the **unique** minimizer in the non-information-tight regime (`n=12..19,22,...`); ties are possible only when `S=C`, e.g. `G=C-1`.

**Falsification attempt.** The only possible counterexample is `A_{n-2} ⊔ C_2`. Halving `e` lowers the denominator by exactly one, while one known comparison can save at most one comparison — the arithmetic cannot reverse. At the first possible index `n=12`, the dangerous value would be `G(12)=28`, but the sandwich gives `G(12)∈{29,30}`, so `29/28 > 30/29`. No counterexample can exist.

## Complexity reading and limits

- This is a **value-level structural barrier**, not a certificate result: it uses only extension counting and the existence of sorting trees. It makes no NP/PSPACE claim and does not touch certificate completeness; the soundness/completeness gap for `SORT-BOUND-U` remains untouched.
- Consequence: high-extension posets are too rigid to serve as a ratio-based testing ground; no such transfer to the antichain can beat the antichain. The fence family’s `1/log2(phi)` ratio lives entirely in the low-extension regime (`e(F_n)=F_{n+1} ≪ n!/2`).
- Honest limits: `n=1,2` are degenerate (`0/0` for `C_2`). The exact `G(n)∈{S,S-1}` is not determined — the proof needs only the sandwich. Nothing is claimed for `e(P)<n!/2` or about computing `S(n)`; no uniform bound or new `S(n)` value follows. The enumerations were sanity checks; the theorem rests on the paper argument.

## Other metadata

```json
{
  "finished_at": 1794221210.1925335,
  "started_at": 1794220125.8358827
}
```
