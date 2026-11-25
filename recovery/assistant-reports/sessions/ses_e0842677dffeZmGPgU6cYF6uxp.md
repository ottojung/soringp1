# antonina-UBE6WyugKddHq2nHg80zK4-unwritten

Session: ses_e0842677dffeZmGPgU6cYF6uxp
Workspace: /home/lubko/soring-fronts/non-eindex-greedy-profile-alln
Created: 1795157760228; updated: 1795160048666

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f7bd9b14001Vkjt9aHlDMojcY)

I'll start by studying the required documents and understanding the environment. Let me read the key files in parallel.

## Output 25 (msg_1f7bdb857001EyK3V5OIKybZ5M)

Now let me look at the research board #301 digest. I need to source the profile before Antonina calls. Let me check the board digest script and get the recent results.

## Output 45 (msg_1f7bddd0e001iuXWl9hq20NkVu)

Let me read the full 06:42Z result and my independent verification comment. Let me find the board data source.

## Output 56 (msg_1f7bdec920013dIM6GNhbIoQ6O)

Let me fetch the raw board JSON to a file and extract the specific messages in full.

## Output 76 (msg_1f7be178c0017jZHYdYaJcOTQE)

Let me look for the independent verification comment related to the 06:42Z result, and check whether this exact front has posted before.

## Output 105 (msg_1f7be813b001w3lAYK3eC2Qbo0)

Found the independent verification comment at 06:56Z. Let me read it in full, plus check this front hasn't posted before.

## Output 125 (msg_1f7bec843001yLDws9BxB340Pe)

I now have full context. Let me examine the scratch code from prior fronts to nail down the exact definition of V (greedy max-extension value) before building my own solver.

## Output 160 (msg_1f7bf13f5001QSfJhXyzxfilcY)

Now I understand the exact model. V(P) = min over incomparable pairs of [1 + V(max-e child)] (tie → max of both). Let me build my own from-scratch solver and search for a chain-union gadget pair with equal (e, h) but different V.

## Output 194 (msg_1f7bf9892001ho18vPt7uffUaF)

My solver reproduces the verified collision exactly. Now let me search chain-union partitions for a gadget pair with equal (e, h) but different V.

## Output 212 (msg_1f7c191c1001nVclwn0vjPRN72)

The brute-force search is slow. Let me add caching for `le_count` to speed it up.

## Output 264 (msg_1f7cf8a3b001DKYSATXU9ZZ9lC)

Brute-forcing V for all partitions is too expensive. Let me first find candidate partition pairs with equal `(∏a_i!, max)` cheaply, then compute V only for those few candidates.

## Output 282 (msg_1f7d0407a001iOuMWmZQLSzXDg)

Many `(∏a_i!, max)` collisions exist. Let me focus on small n0 where V is computable and list candidate pairs.

## Output 293 (msg_1f7d0a78b001NgFFVSj1vX1L8S)

Let me compute V for the n0=11 and n0=12 candidate pairs (with a timeout) to see if they differ.

## Output 311 (msg_1f7d317f30014ZTMAAil0M0cwX)

Let me instrument the V computation to see how many states it explores for a single larger chain-union.

## Output 329 (msg_1f7d5db3f001Too39pnoyqIu2Y)

The state count is large but tractable. Let me run one to completion with a higher cap.

## Output 340 (msg_1f7da5e7b001IpE1PYa6Gax2Pj)

Let me quickly test the small n=5 posets mentioned on the board (equal e, different F) for equal h and different V.

## Output 358 (msg_1f7daadad0016lgggoErJgtqb8)

Found a much better gadget: n=5 posets P1=(8,12,8,0,12), P2=(26,0,10,0,8) have **e=8, h=3, V=3 vs V=4** — exactly equal (e,h), different V. Let me verify they're reachable in the greedy ball from the 5-antichain.

## Output 376 (msg_1f7dafada001Vug4iXsWndLQB7)

Both gadgets are reachable (depths 4 and 5). Now let me verify ordinal-sum additivity and the amplification construction computationally with small prime-set chain-unions.

## Output 394 (msg_1f7db385e001HY0UD9AgkRiaNj)

The amplification is verified computationally. Let me also check rank profiles of P1/P2 and construct a clean reachability proof.

## Output 412 (msg_1f7db77420010JyHbAWRCqHhjg)

The rank computation had an ordering bug. Let me fix it.

## Output 430 (msg_1f7dbc8960010Zpplmh5NSIL46)

P1/P2 have equal *sorted* level-size multisets but different ordered profiles. Let me search the reachable ball for a gadget with equal (e, rank-profile) and different V to also kill rank-profile invariants.

## Output 448 (msg_1f7dcbe4c001xeEtni3gfqvI51)

At n=6 there are reachable pairs with equal **(e, bottom-profile, top-profile)** and different V — this kills rank-profile invariants too. Let me extract a clean pair and verify depths and amplification.

## Output 466 (msg_1f7dec1bf001T1TKG5PfY6Lq6u)

Let me verify the depth inequality threshold and finalize the numbers for the write-up.

## Output 484 (msg_1f7df2367001H8KYK8Qi1Glr4v)

Let me verify the host, worktree cleanliness, and that this front hasn't posted before.

## Output 511 (msg_1f7df886c001ZRYX2Req9ThQWM)

No prior post by this front. Let me check how to post to the board via Antonina.

## Output 529 (msg_1f7dfb135001gr7hovRaXqnSUy)

Everything is verified. Let me write up the finding and post it to board #301.

## Output 547 (msg_1f7e028f7001bhGcjZr2htXTdO)

Let me verify the comment was posted correctly.

## Output 558 (msg_1f7e03f7e0013snNVKQFcI870d)

The post is live. Final worktree check:

## Output 569 (msg_1f7e05181001gq9KOsEqGOYNdF)

Done. Here's the concise summary of what I accomplished on `non-eindex-greedy-profile-alln` (billy-dev, isolated worktree at `6a96398`, clean throughout, no repo/Lean/test/CI/main/ledger changes; all scratch in `/tmp/opencode/nonindex`).

## Result — deliverable (a): `(e,h)` and rank-profile invariants fail

**Theorem (paper proof, all n ≥ 700):** there are `2^{Ω(√(n/log n))}` distinct values of `(e,h)` — in fact of `(e, bottom-rank-profile, top-rank-profile)` — each realized by two states in `B_{G(n)}(n)` with different greedy value `V`. So any invariant of this kind needs superpolynomially many exceptions.

**Gadget (my from-scratch solver, verified):** two reachable 6-element posets
- `Q1 = [14,8,8,0,0,0]`, `Q2 = [6,4,0,16,0,0]`
- both e=60, h=3, ordered bottom profile `(3,2,1)`, top profile `(3,2,1)`, but **V(Q1)=6, V(Q2)=7**; both reachable from `A_6` in 4 greedy comparisons.
- (Smaller `(e,h)`-only gadget also found: n=5, e=8, h=3, V=3 vs 4.)

**Amplification:** using L2 (V additive under ordinal sum, verified computationally) and L4 (prime-chain-unions `C_S`), set `P_S = Q1 ⊕ C_S`, `Q_S = Q2 ⊕ C_S` with `m=n−6`. Then `e, h, rank profiles` all agree while `V` differs by 1; depth `8n−44 ≤ ceil(log2 n!)` for `n≥700`; the `2^{Ω(√(n/log n))}` distinct prime sets give the exception lower bound.

## Falsification attempts (honest)
- Tried salvaging the verified n=8 gadget `U,W` (h 6 vs 5) by top-chain padding — cannot equalize both size and h.
- Brute-forced all chain-union partitions n0≤10 (no collision; first at n0=11 but V there needs >460k states) — switched to smaller general-poset gadgets.
- Exhaustively searched greedy balls n=5,6 — found the mixed groups used above.

## Limits reported
Finite V-values (not kernel-checked/hand proof); reachability uses prior verified L3 + `G(n)≥ceil(log2 n!)`. This excludes `(e,h)`, rank profiles and their coarsenings, **not** an arbitrary clever poly-time `g` that separates the gadgets — that general question stays open, with the concrete necessary condition that any such `g` must distinguish `Q1` from `Q2` off the poly exception set. No class separation, no S(n) value, no Lean.

Posted one comment to board #301 under author `SoringP1 frontier: non-eindex-greedy-profile-alln` (07:33:40Z), labeled definition/deduction/experiment/paper proof.
