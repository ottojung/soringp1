# antonina-5dUsIStTVvhplHeMqPuDcA-denounce

Session: ses_e486b4416ffeMvWSzGClvbOmKl
Workspace: /home/lubko/soring-fronts/t5-min-extension-threshold
Created: 1794081340457; updated: 1794083339230

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 20 (msg_1b794cb16001sWFlzbRqD75MbE)

I'll start by inspecting the current state — working directory, Git status, durable records, and the referenced docs — to determine what already happened before doing any new work.

## Output 33 (msg_1b794e0530014W825hKyJjmquZ)

Clean tree, no uncommitted work. Now let me read the key docs and the board record.

## Output 104 (msg_1b796221c0011uHdRrhGWsSLbJ)

Prior work on this exact question already exists in a sibling worktree and a remote branch. Let me inspect it and the referee log before computing anything.

## Output 132 (msg_1b79745a400133qboe7KdTX3ae)

Key context found: board #301 already has a conditional **T(5)=20** post (18:39Z) with witness `pred=[0,0,1,3,7,15,31]`, and a referee log confirms it. The current front's **T(5)=27** claim conflicts with that. I will now independently verify the witness and the merge value with fresh code (no reuse of the prior scripts).

## Output 156 (msg_1b799587e001ghF3ozLuh5tpSw)

Independent computation confirms the witness (two different exact methods agree): **W has e=21, m=6**, and **Merge(2,6) has e=28, m=6**. So the front's "T(5)=27" is already refuted by a smaller poset. Now let me read the board's existing T(4)/T(5) claims in full to see what is actually established vs conditional.

## Output 167 (msg_1b79a1467001cMSDFgEesTxDJf)

The board's T(5)=20 is explicitly **conditional on T(4)=12**, which the board itself says remains unproved. I'll attempt to remove that dependency by directly checking all ordinal-indecomposable cores with e≤20 for exact minimax ≤5, using a fresh C++ enumerator.

## Output 196 (msg_1b79fdef0001JehAVq2rwkD93b)

This enumeration produced a strong result: **all 308 connected cores with e≤12 have exact m≤4**, and **all 305 cores at e=20 have m=5**. The e=11,12 counts (66+78=144) exactly match the independent T(4) audit's residual count. Let me verify the T(4) branch's saved 144 records against this, and check the Fibonacci pattern.

## Output 211 (msg_1b7a2355e001W5IkFSU8N9jNLH)

The T(4) branch's saved residual count (144 = 66+78) matches exactly, and its n-distribution matches. Let me check the repo's ordinal-sum facts so the factor argument is sourced, then decide on recording.

## Output 226 (msg_1b7a2994e001y2TfyQ5vCEr3SM)

The extremal witnesses form a clear family: `pred[i]=(1<<(i-1))-1` (each new element above all earlier ones except the immediately preceding). Let me verify its `(e,m)` pattern.

## Output 295 (msg_1b7a55e37001dfavR6bEEIGRIi)

The computational result is now solid and cross-validated: our enumeration exactly reproduces the independent T(4) audit's 144 residual records (same `e`, `n` distribution), and all recompute to F=4. Let me check the live board state and posting interface before adding anything.

## Output 398 (msg_1b7adbcb60015fuvhZ0qfzIc5n)

All max witnesses (e=1…20) were rechecked by two independent exact methods; all agree. I now have a complete, cross-validated result: **T(4)=12 and T(5)=20**, with the front's T(5)=27 refuted. I'll write a durable note and post one concise, non-duplicate board update.

## Output 434 (msg_1b7b0e84b001thDqDk7RJS6dcI)

The post succeeded. But a new board message at 20:20 (between my snapshot and my post) mentions a "Fibonacci fence" and falsifying an "e=13 extremal candidate". I must check it for conflict before claiming the result.

## Output 445 (msg_1b7b10fb5001saA4z7anYOCD93)

A new 20:20 board post independently proves the fence formula `e(S_n)=F_{n+1}`, `m(S_n)=n-1` for **all n**, and states the same `T(2..5)=4,7,12,20` pattern. That is consistent with, and strengthens, my note. I'll update the durable note to cite that all-n proof (I verified the argument) while keeping the open all-r equality as a conjecture.

## Output 465 (msg_1b7b2a8f00017pCCCPjAM40MCC)

## Mathematical finding

**The front’s claim is false: \(T(5)=20\), not 27.** The claim “every finite poset with at most 27 linear extensions is sortable in five comparisons” fails at a 7-element poset with only 21 extensions.

### Counterexample (exact, independently checked)

The staircase poset \(S_7\) with predecessor masks

\[
[0,0,1,3,7,15,31]
\]

has

\[
e(S_7)=21,\qquad m(S_7)=6.
\]

I verified this two independent ways: memoized minimax over reachable posets, and extension-subset DP. Both give \(e=21,\ m=6\). Hence

\[
T(5)\le 20.
\]

The front’s `Merge(2,6)` witness has \(e=28,\ m=6\), so it only gives \(T(5)\le 27\); it is **not** the sharp failing instance. `Merge(2,5)` has \(e=21,\ m=5\) and is tight, while the staircase \(S_7\) is the actual \(e=21\) failure.

### Exact thresholds

I also computed the full all-size thresholds without assuming the open \(T(4)=12\):

\[
T(4)=12,\qquad T(5)=20.
\]

Method, briefly:

1. Decompose any poset into its unique ordinal sum of ordinally indecomposable factors (the connected components of the incomparability graph). Under ordinal sum, \(e\) multiplies and \(m\) adds; this is already proved in the repository.
2. Exhaustively enumerate every ordinally indecomposable poset with \(e\le 20\) by maximal-element insertion. Completeness holds because every poset has a natural labelling; a new maximal element is inserted after an ideal of predecessors. Pruning at \(e>20\) is safe because \(e\) is nondecreasing. For a connected incomparability graph, \(n\le e\), so depth 20 covers all cores.
3. Compute exact minimax for every core. The maximum exact \(m\) by \(e=1,\dots,20\) is
   \[
   0,1,2,2,3,3,3,4,4,4,4,4,5,5,5,5,5,5,5,5.
   \]
   No core with \(e\le20\) has \(m>5\). Counts at \(e=18,19,20\) are \(324,304,305\); the \(e=11,12\) counts and \(n\)-distribution match the independent T(4) audit’s 144 saved records exactly, and all 144 recompute to \(F=4\).
4. The minimal extension counts for depth \(d\) are \(s(1)=2,s(2)=3,s(3)=5,s(4)=8,s(5)=13\). If a poset with \(e\le12\) had factor depths summing to at least 5, the extension product would be at least \(3\cdot5=15>12\), contradiction: \(T(4)=12\). If a poset with \(e\le20\) had factor depths summing to at least 6, the product would be at least \(3\cdot8=24>20\): \(T(5)=20\).

The extremal family is the staircase \(S_n\) with \(\mathrm{pred}[i]=(1\ll(i-1))-1\). It satisfies \(e(S_n)=F_{n+1}\) and \(m(S_n)=n-1\) for all \(n\) (the all-\(n\) portion is an elementary adversary argument: only adjacent pairs are informative, and every adjacent pair must be queried). Hence

\[
T(r)\le F_{r+3}-1
\]

for every \(r\), with equality verified for \(r=2,3,4,5\):

\[
T(2)=4,\quad T(3)=7,\quad T(4)=12,\quad T(5)=20.
\]

The all-\(r\) equality \(T(r)=F_{r+3}-1\) (equivalently a Fibonacci splitting induction) remains a conjecture; only the upper bound is proved for all \(r\).

## Honest limits

- This is an **exhaustive finite computation plus paper deductions**, not Lean and not kernel-checked. Its correctness rests on the stated completeness of the insertion enumeration and the \(n\le e\) spanning-tree bound.
- It is a **general-poset local-threshold theorem**, not a certificate-completeness or NP-membership result. It does not give a polynomial-size certificate for `SORT-BOUND-U`, and it does not improve the uniform complexity of computing \(S(n)\).
- \(T(5)\) is a local pruning base, not a statement about \(S(5)\); the relevant root threshold is \(T(S(n))\).
- The all-\(r\) Fibonacci equality remains open.

## Effects and records

- One new board #301 comment posted at `2026-11-07T20:26:12Z`; no duplicate of the earlier conditional \(T(5)=20\) post.
- Durable note and reproducible sources: `~/.local/state/soringp1/t5-exact-threshold-20261107.md` and `~/.local/state/soringp1/t5verify/` (`enum_t5.go` SHA-256 `d71b1d58…`).
- No repository changes; the worktree remains clean.
