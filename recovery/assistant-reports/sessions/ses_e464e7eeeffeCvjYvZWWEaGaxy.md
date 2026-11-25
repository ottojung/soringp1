# antonina-zZ1SSH94Rb5udAmjBMX3jM-threatens

Session: ses_e464e7eeeffeCvjYvZWWEaGaxy
Workspace: /home/lubko/soring-fronts/reachable-depth-cover-audit
Created: 1794116780309; updated: 1794117229118

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1b9b18137001BZHLXKCm1DTw0e)

I'll start by understanding the repository context and the problem model, then write an independent enumerator.



## Output 45 (msg_1b9b24a48001V1NPjkBIyR9Pl2)

The erratum confirms the 01:40Z script was buggy. I'll now write a fresh enumerator with two independent representations: BFS from the antichain, and a recursive poset generator (not subset closure) for independent verification.



## Output 92 (msg_1b9b4eda9001hoPb6uqlHsaCQw)

The generator's extension validity is missing a condition: since `x<e<y` forces `x<y`, the old poset must already contain `D×U`. That caused the duplicates. Fixing:



## Output 110 (msg_1b9b51d30001oFgDsobECsHxLg)

n≤4 reproduce exactly: counts 1, 13, 73, 201, 219. Note the edge-level nuance: a comparison can change cover count by −1, 0, or +1, but never by more than +1. Now n=5, with all three methods.





## Output 121 (msg_1b9b5a016001VHmLLxcNbrjjgu)

n=5 passes, and the subset-closure method independently reproduces all 4231. Now n=6 (130,023 states), BFS by levels:



## Output 132 (msg_1b9b5edc5001qiWNqHqsAvC54n)

All checks pass through n=6. Let me extract explicit witness posets for the edge-level cover-count behaviour (Δ can be negative even though the distance result holds), and save logs.



## Output 152 (msg_1b9b74cf7001MVHnk4xJErNOpj)

Let me also constructively verify the sufficiency algorithm (compare target covers one by one, in a fixed order) on every poset through n=6, rather than relying only on BFS existence.





## Output 181 (msg_1b9b7fe2d001GlgpQ1Xv3C9Xcz)

**Verdict: HOLDS-ALL-N.** The finite audit gives `HOLDS-TO-6`, and the lemma has a short all-`n` paper proof. No counterexample; every set comparison at every `k` matched exactly.

## 1. Independent enumerators

Script: `/tmp/opencode/reachable_depth_cover_audit.py` (untracked; no repo files changed, worktree clean at `f89f6d0`).

Three independent methods:

- **A. BFS from the antichain** (`bfs_distances`). State = strict poset stored as `(up, down)` bit masks. Pair `{a,b}` is admissible iff neither `a<b` nor `b<a` is already implied; both orientations are expanded. `dist(P)` = shortest-path comparison count.
- **B. Recursive labelled-poset generator** (`generate_posets`), *not* subset closure. A poset on `[m+1]` is built from its induced subposet on `[m]` by the new element's downset `D` and upset `U`, with the necessary condition `D×U ⊆ P` (because `x<e<y` forces `x<y`). This generates every labelled strict poset exactly once; uniqueness, strictness and transitivity are asserted. Totals match A001035: `1,1,3,19,219,4231,130023`.
- **C. Strict subset-closure brute force** (`subset_closure_posets`), for `n≤5`: close every subset of ordered pairs and reject closures containing `(a,a)` or both `(a,b),(b,a)`. This is the strict version of the buggy 01:40Z check.

For each `n`, every generated poset was compared with BFS distance and cover count, and the cumulative sets were compared explicitly, not just by cardinality.

## 2. Counts

Cumulative `|{P : dist(P) ≤ k}|` equals `|{P : |cov(P)| ≤ k}|` at every `k`:

| n | #posets | max cov | counts for k=0,1,… |
|---:|---:|---:|---|
| 3 | 19 | 2 | 1, 7, 19 |
| 4 | 219 | 4 | 1, 13, 73, 201, 219 |
| 5 | 4231 | 6 | 1, 21, 201, 1081, 3171, 4131, 4231 |
| 6 | 130023 | 9 | 1, 31, 451, 3931, 21481, 69253, 113173, 128173, 129883, 130023 |

BFS shortest-path level sizes (`dist(P)=k`) also equal the `|cov(P)|=k` counts:

- n=3: `1, 6, 12`
- n=4: `1, 12, 60, 128, 18`
- n=5: `1, 20, 180, 880, 2090, 960, 100`
- n=6: `1, 30, 420, 3480, 17550, 47772, 43920, 15000, 1710, 140`

n=0,1,2 were checked too (`1`, `1`, `1,3`). The n=6 BFS was done level by level, not by enumerating `2^30` pair subsets.

This reproduces the erratum: the true strict counts at n=4 are `13` for `k=1` and `73` for `k=2` on **both** sides; the 01:40Z “149” and “209” cover-side values were inflated by reflexive pseudo-posets. At n=3,k=1 the true value is `7`, not `17`.

## 3. General proof

**Theorem.** For every `n` and every strict poset `P` on `[n]`, the minimum number of adaptive comparisons from the antichain to `P` is exactly `|cov(P)|`. Hence the states reachable within `k` comparisons are exactly `{P : |cov(P)| ≤ k}`.

**(a) Necessity.** Two equivalent arguments:

- *Direct-cover argument.* Every cover `(x,y)` of the final `P` must have been compared directly. If `x<y` first appears through the new outcome `(u,v)` with `x ≤_P u <_P v ≤_P y` and `(u,v) ≠ (x,y)`, then either `x<u<y` or `x<v<y` in `P`, so `(x,y)` is not a cover. Distinct covers are distinct pairs, so at least `|cov(P)|` comparisons are needed.
- *Potential argument.* For one legal comparison `a<b`, put `Q = tc(P∪{(a,b)})`. Every new relation is `x<y` with `x≤_P a<b≤_P y`; any such relation other than `a<b` has an intermediate (`a` if `x<a`, `b` if `b<y`). Old covers of `Q` are covers of `P`. Therefore `cov(Q) ⊆ cov(P) ∪ {(a,b)}`, so `|cov(Q)| ≤ |cov(P)|+1`. Starting from `0`, after `k` comparisons `|cov(P)|≤k`.

**(b) Sufficiency.** List the covers of `P` in any order and compare each pair directly with the outcome dictated by `P`. Before a cover `(a,b)` is added, the current state `Q` is a subposet of `P`. If `Q` implied `a<b`, there would be a path `a<…<b` in `P`, contradicting cover-hood; and `b<a` is impossible because `P` contains `a<b`. So the comparison is admissible. After all covers have been added, the state contains `tc(cov(P)) = P`, hence equals `P`. This takes exactly `|cov(P)|` comparisons. I also verified this constructive path on **every** poset through n=6 (`constructive_sufficiency.py`, zero failures).

**Important edge-level nuance.** A single comparison can *decrease* the cover count, so “each comparison adds exactly one cover” is false. Examples:

- n=4: `P={2<0,2<1,3<0,3<1}` has `cov=4`; comparing `0<1` yields `cov=3` (`Δ=-1`).
- n=5: `P={3<0,3<1,3<2,4<0,4<1,4<2}` has `cov=6`; comparing `3<4` yields `cov=4` (`Δ=-2`).

This does not affect the theorem: only the upper bound `Δ≤+1` is used for necessity, and the minimum-distance target is still `cov(P)`. The negative-`Δ` edge is a non-optimal detour.

## 4. Reproduction

Logs and commands:

```text
python3 /tmp/opencode/reachable_depth_cover_audit.py 3 4 5 --subset-check --edges
python3 /tmp/opencode/reachable_depth_cover_audit.py 6
python3 /tmp/opencode/constructive_sufficiency.py
```

Logs: `/tmp/opencode/logs/n3-n5.log`, `/tmp/opencode/logs/n6.log`, `/tmp/opencode/logs/constructive.log`.

No tracked file was edited, committed, or pushed; nothing was posted to the board.
