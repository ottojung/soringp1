# antonina-rQcBlIV1ty7CEUQugF6Nis-redress

Session: ses_df7279d8cffeSsVVaHOWHk8jEz
Workspace: /home/lubko/soring-fronts/g-completeness-sharp-band-constant-alln
Created: 1795444728524; updated: 1795447372386

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 13 (msg_208dfd16c001PMhW6aA3yhyfYT)

I'll start by inspecting the current state carefully — git state, working directory, the key documents, and any durable task records — to avoid repeating side effects from the interrupted turn.

## Output 28 (msg_208dfdfba001djK3llD0m2ez4d)

We're on `billy-dev` (hostname matches), and the worktree is clean — no partial repository changes. Let me read the key documents and find the board #301 and any durable task records.

## Output 47 (msg_208dfecdd0019qEoMS6uzX6TRj)

Let me check the board digest, the durable ledger entry for this front, and any earlier work in this directory.

## Output 66 (msg_208e008f4001W8jfkFHvPFX4fF)

Let me retrieve the full relevant board posts, this front's ledger entry, and check for earlier scratch work in `/tmp/opencode`.

## Output 81 (msg_208e01c7a001yG2afNjsrhp5QT)

Let me find this front's exact ledger entry and any earlier scratch work specific to the "sharp band constant" question.

## Output 96 (msg_208e0467c001rTn7OrKRVS0OK8)

I found my front `g-completeness-sharp-band-constant-alln` (status: running, agent `rQcBlIV1ty7CEUQugF6Nis-redress`, started 2026-11-23). Let me check for a prior board post from this exact front and read the key proof artifact and full board posts.

## Output 111 (msg_208e0af19001DnUhRP5RR3bBRw)

Let me check for scratch files created by this front (started 14:38:48Z) and inspect the board posts that define g and the sharp condition.

## Output 126 (msg_208e1c31c001Vcos3AsgAEFhb7)

No prior post or scratch work from this front exists — the failure happened at launch. Let me read the full prior posts and the earlier library to build on it.

## Output 186 (msg_208e2415d001uoatGnkH8jIiAM)

I now have full context. No prior work from this front exists. Let me build a fresh exact checker and attack the band. First, let me understand the smallest defective posets and verify the structure.

## Output 220 (msg_208e3de1c001lh6GDe8xmGnPzF)

Library verified (F(antichain)=S(n)). Now let me run the exhaustive band search for n=6,7,8.

## Output 231 (msg_208e3f381001D1QpajM4gRqkZ1)

The reporting had a variable bug (printed stale `e`); the actual filter is correct. Let me fix it and run n=7 and n=8.

## Output 258 (msg_208e4c17e001mlVY2cC4CC2qgF)

Let me verify the generation is complete, then extend the search to larger n and higher L bands.

## Output 269 (msg_208e4f448001ZrPFwlEDoO9CI8)

Generation confirmed complete. Let me broaden to higher bands and n=9,10.

## Output 356 (msg_20900258c001U5JmCcJ3hy3tmx)

## Recovery / side effects

- Inspected git state: `billy-dev...origin/billy-dev`, worktree clean, no commits/branches/PRs created.
- Inspected durable records: frontier ledger shows `g-completeness-sharp-band-constant-alln` as `running` (agent `rQcBlIV1ty7CEUQugF6Nis-redress`, started 2026-11-23T14:38:48Z). No prior board post by this front/agent found. No repo files created.
- Scratch only in `/tmp/opencode` (fresh `band_lib.py`, `band_search.py`; reused read-only artifacts like `theorem1.md`, `g_completeness_check.py`). No external posts/commits/purchases made by me. An interrupted n=8 emax=96 run timed out after generation and produced no recorded result; n=9 emax=96 was SIGKILLed earlier. No uncertain external effects.

## Front

- **Question**: For the sound local predicate `g`, is the 14:19Z necessary-condition constant sharp for all finite posets? I.e. is there a defect-free finite poset `P` with `F(P)=L(P)=ell` and `2^(ell-1) < e(P) <= 3*2^(ell-2)` (L=5: `17 <= e <= 24`) with `g(P)=false`, or can the threshold be lowered to `2^(ell-1)` for every finite poset?
- **Falsifier sought**: defect-free `P` in that band with `g(P)=false`; or a paper argument that `F=L, e>2^(L-1)` implies `g(P)` for all finite posets.
- **Complexity implication**: A counterexample in the band would refute completeness `C: F=L => g` (closing this g-certificate route as stated); a proof lowering threshold to `2^(ell-1)` would be the strongest local soundness/completeness theorem for this predicate, but still not a succinct NP certificate for `SORT-BOUND-U` (g needs exact `e(P)`, #P-hard on general posets, and explicit trees are exponential). This is a general-poset structural question; an arbitrary-poset counterexample need not be an antichain `A_n` and would not by itself settle `S(n)=ceil(log2 n!)` or any complexity class placement.

## Definitions [definition]

All finite posets. `e(P)` = #linear extensions; `L(P)=ceil(log2 e(P))`; `F(P)` = exact adaptive minimax comparison height; `D(P)=F(P)-L(P)>=0`.  
`g(P) := [e(P)=1 or exists incomparable {x,y} with e(child_i)<=2^(L(P)-1)` and `g(child_i)` for both children`]`.  
Soundness (board, independently rechecked): `g(P)=>F(P)=L(P)`. Completeness `C`: `F(P)=L(P)=>g(P)` is open.

## Mathematical finding

### 1) The 14:19Z theorem is sharp for the proof method, but lowering to `2^(L-1)` remains open [deduction, independently re-derived]

**Theorem (board 14:19Z, Viche-accepted).** If `P` is defect-free, `F(P)=L(P)=ell`, and `e(P)>3*2^(ell-2)`, then `g(P)`.

*Proof:* take an `F`-optimal pair; `max(F(ci))=ell-1`, so `e(ci)<=2^(ell-1)`. If some `e(c1)<=2^(ell-2)`, then `e(c2)=e(P)-e(c1)>2^(ell-1)`, contradiction; hence `2^(ell-2)<e(ci)<=2^(ell-1)`, so `L(ci)=ell-1=F(ci)` and both children are defect-free. Induction on `e` gives `g(ci)` and thus `g(P)`. QED.

**Why the constant is sharp for this argument:** assume only `e(P)>2^(ell-1)`. The same split gives `e(ci)<=2^(ell-1)`, but a child can be `e(c1)<=2^(ell-2)` while the other remains `e(c2)=e(P)-e(c1)>2^(ell-2)` (e.g. `ell=5, e(P)=17, e(c1)=8, e(c2)=9`). Thus `L(c1)` can drop to `ell-2` and `c1` can be defective (`F(c1)=L(c1)+1` is possible; defective `e=8` posets exist). The pair then fails the `g` witness condition. The proof cannot force `g` below `3*2^(ell-2)`.

**Exact remaining obstruction [deduction].** Any counterexample to lowering `3*2^(ell-2)` to `2^(ell-1)` (equivalently any defect-free non-`g` poset in the band) must be: `F(P)=L(P)=ell>=5`, `2^(ell-1)<e(P)<=3*2^(ell-2)`, and for every balanced `g`-candidate pair, at least one child is a one-level-hidden defect: defective `S` with `8<=e(S)<=2^(ell-2)` (smallest defective poset has `e=8`), while the other child may be defect-free with `L=L(P)-1`. This is the same hidden-defect obstruction as 14:19Z, now localized exactly to the band.

### 2) Finite falsification attempt: no counterexample in the L=5 band for n<=10 [experiment]

Fresh independent exact checker (`/tmp/opencode/band_lib.py`, `band_search.py`): transitive-closed bitmask posets; `e(P)` by subset DP over downsets; `F(P)` by memoized minimax; `g(P)` by recursive predicate. Sanity: `F(A_n)=S(n)` gives `0,1,3,5,7,10` for `n=1..6`. Generation completeness sanity: for `n=4`, all 40 transitive sub-orders of the chain equal cover-removal closure.

Searched all sub-orders of the `n`-chain (covers all labeled posets up to isomorphism by relabeling along a linear extension) with `e<=24`, i.e. including the entire L=5 band `17..24`:

| n | posets with e<=24 | band (17<e<=24, L=5) defect-free states | g-FALSE in band |
|---:|---:|---:|---:|
| 5 | 276 | 55 | 0 |
| 6 | 1377 | 626 | 0 |
| 7 | 4010 | 2258 | 0 |
| 8 | 8401 | 5134 | 0 |
| 9 | 14438 | 9249 | 0 |
| 10 | 22293 | 14787 | 0 |

Also checked defective `e=8` children exist (needed by obstruction): `n=5:8, n=6:16, n=7:24` labeled defective `e=8` posets in this representation. No band counterexample found. A larger `n=8, e<=96` run (covering higher bands) timed out during analysis after generating 175,962 states; **not a result**.

## Conclusion on the asked front

- **Is the `3*2^(ell-2)` constant sharp for the theorem?** Yes, for the 14:19Z proof: the implication step fails exactly at `3*2^(ell-2)` and cannot be lowered by that argument [deduction].
- **Is there a defect-free band poset with `g(P)=false`?** Not found. Exhaustive up to `n<=10, e<=24` finds 0 [experiment, finite only].
- **Can the threshold be lowered to `2^(ell-1)` for all finite posets?** **Open.** I obtained neither a counterexample nor an all-n proof. The band `(2^(ell-1), 3*2^(ell-2)]` is exactly the remaining possible location of `C`-counterexamples; closing it would require either constructing a hidden-defect band witness or proving every defect-free band state has an alternative g-witness.

## Failed / limited approaches

- **Direct threshold lowering in Theorem 1 proof**: fails because a child may have `e<=2^(ell-2)` and be defective. [deduction]
- **Finite exhaustive search n<=10, e<=24**: no counterexample; finite evidence only, not an all-n proof. [experiment]
- **Bigger e/n band scan (n=8,e<=96; n=9,e<=96)**: compute-limited / timed out; no completed result. [inconclusive]
- **“Forget relation” parent construction around defective e=8 child** (same idea as 14:19Z): observed alternative g-witnesses in tested cases, not a proof. [experiment]

## Honest limits

- No new theorem completing C, no counterexample, no new `S(n)` value, no SORT-BOUND-U class placement. 
- General-poset result only; not transferred to antichain `A_n`. 
- Soundness/completeness distinction preserved: `g` is sound; completeness remains conjectural.
- I did not post to #301 or change the repository; this is the requested report.
