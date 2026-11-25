# t4-uniform-base-exhaustive-alln

## status

blocked

## origin

executive_initiated

## agent_id

9tAM98QDfM9QVqRFvBc4Yu-seizing

## exit_state

failed

## question

For every n and every poset P on any number of elements with e(P) <= 16, is m(P) <= 4? Extend the certified uniform base: enumerate exhaustively on n = 7 (and propose n = 8) for a poset P with 13 <= e(P) <= 16 and m(P) >= 5, using a written minimax-exact solver; if none exists, state that every poset with e(P) <= 16 has m(P) <= 4 as the deliverable.

## basis

docs/research-obstruction-next.md sections 2-4 (T(r) table: T(3)=7 certified for all n, T(4)=12 certified for n <= 6, first failing e = 13; Kahn-Saks 3/11-8/11 bound; Hanamura-Iwata 2011 for e <= 7; exhaustive n <= 6 = 130023 posets).

## falsifier

Exhibit a poset P with e(P) <= 16 and m(P) >= 5, or prove every poset with e(P) <= 16 has m(P) <= 4 (i.e. extend T(4) = 12 to all n). Provide the poset or the proof, with an independent solver cross-check.

## implication

A uniform base beyond e <= 7 at budget 4 strengthens the exact S(n) backward-search pruning table; a negative result sharpens the uniform-base structure of the local pruning criterion.

## finding_unverified

I'll start by verifying the host, then reading the key docs and board.
I'll verify the host, then read the operations doc (for the board), the literature, and the companion probe script.
Now I have the definitions: `e(P)` = number of linear extensions, `m(P)` = minimax height of a decision tree sorting all linear extensions of `P`. The FRONT claim is: **every poset with `e(P) <= 16` has `m(P) <= 4`** (extending `T(4)=12`). The audit notes a witness with `e=13, m=5` at n=6. Let me check the host, the board, and run the repo probe.
I have the definitions and the repo's verified witness (`H2_P1`: n=6, e=13, m=5). Now let me check the host, enumerate counts from the repo's enumerator, and find the relevant front on the board.
The repo's own enumerator shows: n=6 → 130,023 posets; n=7 → 6,129,859 posets. Let me verify the host via `shell`, check the frontier ledger for the relevant front, and search the board digest for the e≤16 front.
I'm on `billy-dev`. The repo's own verified witness is `H2_P1 = (20,16,0,23,0,22)` (n=6, e=13, m=5) — which already breaks the claim "every poset with `e(P) ≤ 16` has `m(P) ≤ 4`" if true. Per the FRONT task I need an **independent solver** to attack the claim: verify the witness, cross-check e/m computations against the repo, enumerate n=7 exhaustively, and propose/run n=8.

Let me write the independent solver in /tmp/opencode.

## Other metadata

```json
{
  "finished_at": 1795311270.1330154,
  "retry_after": 0,
  "started_at": 1795309983.726073
}
```
