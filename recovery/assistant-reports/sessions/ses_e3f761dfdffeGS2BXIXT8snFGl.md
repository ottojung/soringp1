# antonina-84RI6SncZfp5tYimiWh16n-winning

Session: ses_e3f761dfdffeGS2BXIXT8snFGl
Workspace: /home/lubko/soring-fronts/two-wl-move-quotient-soundness
Created: 1794231624256; updated: 1794237934275

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 1143 (msg_1c0e9463c0018G6BsW2ArVyUyE)

**Finding: the claim is variant-dependent. The folklore 2-WL move quotient is false at n=8; the full/paired 2-WL quotient survives exhaustively through n=9.**

Posted once to board #301; repository remains clean at `6a96398`; no Lean, commit, or repo change.

### 1. Folklore 2-WL counterexample (soundness failure)

Using the standard separate-multiset update

`c_{t+1}(i,j) = (c_t(i,j), multiset_k c_t(i,k), multiset_k c_t(k,j))`,

take the board’s height-2 poset

`P = (0,0,0,0,0,1,7,25)`, i.e. `5<0; 6<0,6<1,6<2; 7<0,7<3,7<4`.

Exact minimax gives

- `F(P) = 11`
- `T(1,2) = 10`
- `T(1,3) = 11`
- `T(3,4) = 10`

but the incomparable pairs `{1,2}`, `{1,3}`, `{3,4}` all receive the same stable folklore-2-WL colour. So identical colour, different exact move value. This is a genuine soundness counterexample, not merely a completeness gap. Exhaustive n≤7 found no such collision, so n=8 is minimal for this variant.

### 2. Full/paired 2-WL: no counterexample through n=9

For the stronger update

`c_{t+1}(i,j) = (c_t(i,j), multiset_k (c_t(i,k), c_t(k,j)))`,

which is the “full 2-WL” that separates the earlier n=8 witness:

- **n≤8:** all unlabelled posets, including all 16,999 at n=8: no `T` collision.
- **n=9:** all 183,231 unlabelled posets: no `T` collision.
- **Stronger structural check at n=9:** in every one of those 183,231 posets, every same-colour class of incomparable pairs has a constant unordered pair of oriented-child isomorphism types. Thus through n=9 the quotient is sound for a structural reason: it does not conflate non-isomorphic moves, so equality of `T` is not an arithmetic coincidence.
- **n=10:** about 900,000 random dense posets and ~48,000 exact-checked collision candidates; no counterexample. This is sampling, not exhaustive.

### 3. Honest limits and complexity implication

The all-n full/paired-2-WL claim is neither proved nor refuted here; the first possible counterexample is n≥10. The folklore-2-WL version is refuted at n=8.

The earlier statement that “full 2-WL separates the witness” is a completeness fact about that witness, not a soundness theorem for move values. Also, even a sound move quotient does not by itself give a polynomial-size exact invariant for root-reachable states or an NP certificate: the DP state is still the whole poset, and `T` still invokes exact child minimax values. No complexity-class consequence follows from this finite result.

## Output 1192 (msg_1c0e9fcd6001DZ0d0fSttNpGWi)

**Recovery audit complete — no external action repeated.**

What I verified:

- **Host:** `billy-dev`.
- **Git:** worktree clean at `6a96398`; no commits, branches, Lean files, or repository edits.
- **Board #301:** the front’s result appears **exactly once**, posted at `2026-11-09T15:24:05.722Z` under `SoringP1 frontier: two-wl-move-quotient-soundness`. No duplicate post was made.
- **Background processes:** none still running.
- **Scratch artifacts:** `/tmp/opencode/twowl/board_post.md`, `board_post_result.json`, and `FINDINGS.md` exist with matching timestamps.
- **Ledger:** the durable record still shows `status: running`, `exit_state: null`, `finding_unverified: null`. That is keeper-managed reconciliation state, not an unfinished research action; I did not edit it manually.

The completed result remains:

- **Folklore 2-WL** move quotient is **false at n=8** on `P=(0,0,0,0,0,1,7,25)`: pairs `{1,2}`, `{1,3}`, `{3,4}` share the same stable colour, but exact values are `T(1,2)=10`, `T(1,3)=11`, `T(3,4)=10`.
- **Full/paired 2-WL** has no counterexample through an exhaustive check of all 183,231 unlabelled posets at n=9, and at n=9 every same-colour move class has the same unordered pair of child isomorphism types.
- n=10 remains sampled only, not exhaustive; the all-n full-2-WL question is open.

No unfinished work remains and no post, commit, or other side effect was duplicated.
