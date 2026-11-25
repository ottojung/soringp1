# antonina-qRhoYje3pNeL5YRw8pXOd4-rice

Session: ses_e0fe88fc2ffeNIooe72tG5rrh7
Workspace: /home/lubko/soring-fronts/fredundancy-confluence-corrected-criterion
Created: 1795029430391; updated: 1795029877392

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f017726f001FZuk5mJ3yHgLVf)

I'll start with the required recovery/side-effect audit and understanding the environment.

## Output 21 (msg_1f017804f001W0WbCaVw5kuo7H)

Worktree is clean on `billy-dev`. Let me read operations docs and locate the #301 board posts / Antonina tooling.

## Output 36 (msg_1f0178c97001Naqt3qmaohW5xU)

Now let me check the ledger, the #301 board digest, and the referenced report.

## Output 51 (msg_1f017a9c5001HtFXaN1JR1QD7Y)

I have the ledger and board state. Let me read the full body of the key referenced report and related posts, plus the framed-strategy checker and literature.

## Output 62 (msg_1f017c003001AmzJsZrIIIoWL0)

I now have the full context. Let me read the key scripts (the minimax oracle and framed checker) before writing my own independent scratch verification.

## Output 77 (msg_1f018dabd001iRdzCFaz4D7Neh)

I have a precise picture. Now let me write **independent scratch code** (in `/tmp/opencode`) to seriously falsify/verify the prior witness and the criterion-equivalence claim, without trusting the repo oracle.

## Output 95 (msg_1f019392f00160zkrJp0Oowjqr)

Independent verification confirms the prior witness exactly. Now let me push further: search for a **sharper** result — a family with genuinely order-dependent terminal states under the corrected criterion (the front's first falsifier disjunct), which would be new. I'll also check whether the corrected criterion is exactly equivalent to value equality over *all* budget-tight states (not just the witness).

## Output 113 (msg_1f01b90fc001FUQUahAhw5EDMS)

The brute search is too slow. Let me instrument and optimize — cache `F`/`meet`, count tight states, and bound the search.

## Output 131 (msg_1f01be8a2001PzKExZ183PkzIr)

Key results so far: (A) the corrected criterion matches value equality on all 20,000 sampled budget-tight pairs (0 mismatches); (B) no pairwise-compatible triple with lossy global meet at n=5. Let me do a bounded random search for any order-dependent terminal family (true non-confluence) at n=5.

## Output 149 (msg_1f01c61e7001T2BSaHg0M2583x)

No order-dependent terminal family found (150k random triples at n=5). Let me verify the prior front's second witness (failure of compatibility with `&`, completing the non-congruence claim), then finalize.

## Output 167 (msg_1f01ca62b001FvxA3bHSHq9Xjz)

Let me resolve the budget-tightness nuance for the compatibility witness by computing reachability at *exact* depths (a state can be reachable at multiple depths).

## Output 185 (msg_1f01ce476001h5gU0hTcx0CIOT)

All verified, including exact-depth budget-tightness of the compatibility witness. Let me check the Antonina CLI posting interface and confirm no duplicate post exists before posting.

## Output 227 (msg_1f01d79d0001sw8DJmA1gmlq2m)

Everything is verified and the host is `billy-dev`. Let me compose the board comment.

## Output 247 (msg_1f01de2e0001xPTO1RLeR2F0iy)

Let me verify the comment actually landed with the exact author.

## Output 258 (msg_1f01df8ea0019N8wpg00VkL6Qf)

The comment landed (2026-11-18T19:24:08Z, exact author, exactly one post). Final side-effect audit:

## Output 269 (msg_1f01e0c47001mLNJj6Trv171mq)

## Done — mathematical finding posted to Antonina #301

**Board comment:** authored exactly `SoringP1 frontier: fredundancy-confluence-corrected-criterion`, landed once at `2026-11-18T19:24:08Z` (verified: exactly one exact-author match). Worktree still clean on `billy-dev` @ `6a96398`, no stash, no repo/Lean/test/workflow/ledger/canonical-main changes — all computation was fresh scratch code in `/tmp/opencode`.

### The finding

**1. New lemma (deduction).** The "corrected set-level losslessness criterion" is *the same relation* as the direct value comparison used in the prior report. With `R = P∧Q`, extras `E_P = P\Q`, `E_Q = Q\P`, set algebra gives `R ∪ E_P = P` and `R ∪ E_Q = Q`, so "E_P jointly F-redundant at R" ⟺ `F(P)=F(R)`. Since F is antitone under relation inclusion (`F(R) ≥ F(P),F(Q)`):

  corrected criterion ⟺ `F(P)=F(Q)=F(P∧Q)` ⟺ `P~Q` (direct value).

The union+closure reading is stricter but classifies the witness identically. Independently confirmed on 20,000 sampled budget-tight n=5 pairs: **0 mismatches**.

**2. Consequence — the all-n claim is FALSE, and "set-level confluence remains open" is a false distinction.** By the lemma, the prior report's own n=5 non-transitivity witness applies to the corrected criterion. I re-verified it from scratch (own F, extension counts, meets, exact-depth reachability): S(5)=7; `P1=(0,0,0,1,11)`, `P2=(0,0,0,3,11)`, `P3=(0,0,0,2,11)` all have F=4 and are budget-tight (depth 3 = 7−4); `P1∧P2=P1`, `P2∧P3=P3`, but `P1∧P3=(0,0,0,0,11)` has F=5. So `P1~P2`, `P2~P3`, `P1!~P3` — non-transitive, not a congruence. Compatibility with `∧` also fails (verified, all inputs/outputs budget-tight). Greedy merging never reaches one F-preserving state: every order terminates at `{P1,P3}` (F=4), while the global meet has F=5.

**3. Honest new negative.** I searched exhaustively over pairwise-compatible n=5 triples and 150,000 random budget-tight triples for the sharper witness (two orders giving different terminal states/F-values): **none found**. So I do **not** claim order-dependence of the terminal set; the demonstrated failure is non-transitivity / no single normal form.

### Honest limits
- Finite n=5 counterexample; no all-n **budget-tight** infinite family (the prior ordinal-sum family is reachable but not depth-tight — that item stays open).
- Framed-DAG **soundness** is untouched; this is a completeness/compression obstruction only.
- No complexity separation: this one relation's failure does not prove super-polynomial optimal-DAG size nor SORT-BOUND-U ∉ NP/coNP (sparse tally language). S(n) and SORT-BOUND-U remain open.

Process succeeded (post landed, audit clean); the mathematical result is the §2 equivalence lemma plus an independently checked finite counterexample — not a proof of any complexity-class claim.
