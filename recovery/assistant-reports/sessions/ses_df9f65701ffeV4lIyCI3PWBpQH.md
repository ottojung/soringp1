# antonina-isblCwWjWWwLYnbmY9LFlI-went

Session: ses_df9f65701ffeV4lIyCI3PWBpQH
Workspace: /home/lubko/soring-fronts/excess-gap-two-alln
Created: 1795397626469; updated: 1795399330932

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 14 (msg_206186b12001kZ7Of5yUrp6ykX)

The server restarted — let me re-establish context: check the repo state, worktrees (looking for "billy-dev"), and the board/docs.

## Output 29 (msg_20618dc97001CLWgrY2ilDyUJz)

We're on `billy-dev` as required. Let me pull board #301 digest and read `docs/problem.md`.

## Output 44 (msg_206190b79001mJBcsGsj4J0sQ7)

We're on `billy-dev` with a clean worktree. Now let me study the literature index, find the structural-lower-bounds doc, and locate definitions of `F`, `antichain`, excess, and any existing solvers/experiments.

## Output 67 (msg_20619a028001ooZKr4XoLoHQgs)

Now let me read the structural-lower-bounds doc (defines `F`), the literature index, the frontier ledger entry for this question, and the obstruction-next doc.

## Output 90 (msg_20619c37e001rXUKP134q29JDh)

Good context now: `F(antichain_n) = S(n)` (the exact query complexity to identify the linear extension — so `F(antichain_n) ≥ C(n)+3` is equivalent to `D(n) ≥ 3`), `C(n) = ceil(log2 n!)`, and `D(n) = S(n) − C(n)`. Let me compute the information-bound table `C(n)` for small `n`, see what tools the repo has, and fetch the OEIS data for exact `S(n)` values.

## Output 109 (msg_2061e13b6001Mn8Q5d6mbwiebA)

OEIS A036604 gives the exact `S(n)` values:

```
n:  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22
S:  0  1  3  5  7 10 13 16 19 22 26 30 34 38 42 46 50 54 58 62 66 71
C:  0  1  3  5  7 10 13 16 19 22 26 29 33 37 41 45 49 53 57 62 66 70
D = S-C: 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 1
```

So within the literature range (n ≤ 22), `D(n) ∈ {0,1}` — the user's data is confirmed, and no `D(n) ≥ 2` is present. `S(23)+` is open (Stober–Weiss).

Key reformulation: since `S(n) = 1 + F(2-chain + (n-2) isolated)` (the state after the first antichain comparison), we have `D(n) = F(P₁(n)) − info(P₁(n))` with `info(P₁(n)) = C(n)−1`. So `D(n) ≥ 2` ⟺ `F(P₁(n)) ≥ C(n)+1`.

Now let me look at the repo's exact minimax DP (to verify `F` computationally), and fetch the primary sources (Stober–Weiss paper, Sergeev).

## Output 128 (msg_206224869001EMIPLgLl0cWVP6)

The repo's `Minimax` DP computes `F(P)` exactly over reachable posets — I can reuse it to compute `F(P₁(n)) = D(n) + info(P₁(n))` independently. Let me fetch the primary sources: the Stober–Weiss paper, OEIS A000112 (poset counts, to size a DP run) and A003070 (the `C(n)` bound itself).
