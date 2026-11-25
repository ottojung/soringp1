# antonina-K8olcUWFtTUlGTHlzbLgUC-densely

Session: ses_e40258cf8ffeG5RuKzhyjTGLNj
Workspace: /home/lubko/soring-fronts/high-extension-relative-efficiency
Created: 1794220127024; updated: 1794221184722

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 27 (msg_1bfda972d001vuiq0CrrdTwSWo)

I'll start by inspecting the current state: git status, working directory, and any durable task records, so I don't duplicate side effects.

## Output 42 (msg_1bfdab5ce001avfZ4GAO5WQPZu)

Clean worktree on `billy-dev`, no uncommitted changes. Let me read the operational docs and the research frontier/pack records to find board #301 and any prior work on this front.

## Output 65 (msg_1bfdace340014ItyzBRFt9fAo5)

Now let me inspect the board #301 records relevant to this front, and check for any prior incomplete work or side effects.

## Output 80 (msg_1bfdaebdd00159hKMY8nnLykq8)

The ledger is large. Let me search it for this exact front and related prior findings, and query the board for the key terms.

## Output 95 (msg_1bfdb3981001mSbS6YI0R0ivQe)

The front is in the ledger as `running` under agent `K8olcUWFtTUlGTHlzbLgUC-densely`, with no finding and a clean worktree — so the interrupted turn left no recorded result. Let me confirm there is no existing board post for this front and check for scratch artifacts before doing any math.

## Output 110 (msg_1bfdcb153001s7h4JSaX0sNYmS)

Recent scratch files `minratio.py` and `board_post.md` exist. I must determine whether the interrupted turn already posted for this front. Let me inspect them.

## Output 125 (msg_1bfddbdf1001ssv08UXTCwxBzf)

`minratio.py` (10:26) matches this front exactly — the interrupted turn wrote it but there's no board post and no output file. Let me inspect the supporting script and run it, then check the board once more for any post that may have landed.

## Output 140 (msg_1bfde180500114ZDTp5OGvN1ZH)

The interrupted turn's own scratch script confirms no post was made. I found a clean structural reduction. Let me verify it by exact enumeration and compute the exceptional poset's values for small `n`.

## Output 151 (msg_1bfe087a7001xYEawg2om0wei9)

Output was buffered and the run exceeded the default timeout. Let me split the verification and run it with proper timeouts.

## Output 162 (msg_1bfe7c01e001X3Pb0n9RTnLS7r)

The structural lemma is confirmed: for `n=3,4,5` the high-extension posets are exactly the antichain plus the labelled single-relation posets (counts `1+n(n-1)`, extension values `{n!, n!/2}`). Let me check the latest board messages to be certain no interrupted post landed, and inspect the posting interface.

## Output 204 (msg_1bfe86496001K0aCLfUyxxqGxO)

The result is a complete paper proof. Let me check how prior posts were invoked, then write and post the finding once.

## Output 215 (msg_1bfe8e104001d04HlmQrdkbs9Z)

The mathematical result is settled. I'll write the finding and post it exactly once to board #301, then verify it landed.

## Output 233 (msg_1bfe9bbab001vcHWK4ozWAfvk3)

The post needs an author. Let me use the same author identity as prior frontier posts.

## Output 271 (msg_1bfea2b89001GMKAjdVH5GvC7x)

Post succeeded. Let me verify exactly one message landed and there is no duplicate.

## Output 282 (msg_1bfea4660001S3l0HBDa35anZ4)

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
