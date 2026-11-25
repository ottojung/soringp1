# antonina-BMma8vbpmASE8WjWp6DaSp-recalled

Session: ses_e032a89f0ffe3bG67xfZvVkvb5
Workspace: /home/lubko/soring-fronts/exec-du-defect-size12-20261121
Created: 1795243210317; updated: 1795247092647

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 1033 (msg_1fd1029c8001wT18q4Ff6A5daN)

Finished. Recovery audit first: no prior post under the tag `SoringP1 researcher: exec-du-defect-size12-20261121` was found, git status was clean at `6a96398`, and no repo/Lean/test/CI/ledger/main changes were made. All scratch work stayed in `/tmp/scratchpad`. The only external side effect is **one** Antonina #301 post, created at `2026-11-21T07:43:57.433Z`.

**Result:** the disjoint-union defect inequality holds at total size 12 for both required splits; no counterexample exists there.

**Coverage:** all unlabelled component pairs were covered by a rigorous reduction, not by direct enumeration of the ~6 million 12-element unions:

- `(3,9)`: 5 × 183231 = 916,155 pairs.
- `(2,10)`: 2 × 2567284 = 5,134,568 pairs.
- Total: 6,050,723 pairs.

**Key evidence:** with `r(P)=F(P)-log2 e(P)`, the identity `e(A⊔B)=binom(a+b,a)e(A)e(B)` and the information bound give  
`F(A⊔B)-F(A)-F(B) ≥ log2 binom(a+b,a) - r(A) - r(B)`.  
Since the defect is integral, `r(A)+r(B) < log2 binom(a+b,a) - min(a,b)` proves surplus ≥ 0.

An independent from-scratch Go evaluator reproduced A000112 counts through n=10 and the known R(n) values through n=9, then gave `R(10)=9-log2 89=2.524267` over all 2,567,284 ten-element classes. Arithmetic:

- `(3,9)`: `r(A)+r(B) ≤ 0.415037+2.218640 = 2.633678 < 7.781360-3`.
- `(2,10)`: `r(A)+r(B) ≤ 0+2.524267 = 2.524267 < 6.044394-2`.

No theorem-completion claim for `S(n)` or `SORT-BOUND-U`; the all-n inequality remains open.

## Output 1061 (msg_1fd10a260001E2599GFgPyAk61)

Recovery audit complete — no unfinished work remains.

- **Git state:** clean at `6a96398`; no repo, Lean, test, CI, ledger, or main changes.
- **Board #301:** exactly one unique message under `SoringP1 researcher: exec-du-defect-size12-20261121`, posted at `2026-11-21T07:43:57.433Z`. The result reported: inequality holds at total size 12 for both `(2,10)` and `(3,9)`, no counterexample.
- **Scratch:** computations and post draft remain only in `/tmp/scratchpad`.

No duplicate post or other external action was performed.
