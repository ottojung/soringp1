# antonina-PBm3R2xXadmsPVejgX0mgE-exercised

Session: ses_e3ce73526ffeno4gcPD4Uls6QA
Workspace: /home/lubko/soring-fronts/prime-excess-unboundedness
Created: 1794274544534; updated: 1794275820061

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 16 (msg_1c318e368001jir2urxcRIr7O8)

I'll start by inspecting the existing state before doing any work.



## Output 29 (msg_1c318eb98001pTYURHkX3jNAO9)

Clean worktree, no scratch dir. Now let me check board #301 for any post already made by the interrupted turn.



## Output 107 (msg_1c319d6f60012SzDY3ZjM0r207)

No post for this front exists (newest board comment is the 01:33:18Z Executive check), so the interrupted turn did not post. Setting up scratch and starting the mathematics.



## Output 118 (msg_1c32075b2001vIfgIDjGwVIVlL)

Two independent counters agree on the base, and the n=34 doubling already gives excess ≥ 4. Let me now scan the full deleted-ordinal-sum family and verify the key lemma exhaustively on small posets.



## Output 138 (msg_1c320cfdb001IGFZ7wgikGy0Kv)

This is turning into a decisive result. Let me verify the base at n=27, the doubling construction, the key counting lemma, and primeness rigorously.



## Output 149 (msg_1c321c08a0019Iosr0TPJuxBjf)

Base n=27 verified with excess 3. Now checking the iterated construction at larger c, and scanning alternative prime families for smaller witnesses.



## Output 169 (msg_1c323813a0015ThujO26sdTiUu)

All checks pass. Now let me independently validate the core amplification inequality (F monotonicity + counting lemma) by exact minimax on small posets, to catch any direction error.



## Output 232 (msg_1c32848a5001KKhfnMyyBO0Uo0)

All mathematics checks out. Let me verify the posting interface and then assemble the board update.



## Output 243 (msg_1c329c2cb001LuaeTCvSYA7dKz)

All verification passed. Writing the board update now.



## Output 290 (msg_1c32b353b001zRp5qRol2mEt4Q)

Everything is verified. Posting the single board update.



## Output 310 (msg_1c32bc9c8001rJgZs86pI0nTdk)

The post is live at 01:56:17Z. Two new comments appeared concurrently (01:36, 01:37) that weren't visible when I checked; let me read them to ensure no duplication or conflict.



## Output 321 (msg_1c32be32c001uTToogbOWXt3J1)

The board update is live (01:56:17Z). I read the two comments that appeared concurrently during the run: neither duplicates this front; the 01:36:45Z Executive check explicitly dispatches `prime-excess-unboundedness` as a separate front, so this post is its answer.

## Summary

**Recovery check first.** The interrupted previous turn left no board comment, commit, or scratch state (`/tmp/opencode/primeunb` did not exist, worktree clean at `6a96398`). I inspected all 8 pages of #301 before posting; the newest comment at inspection time was the 01:33:18Z Executive check. Nothing was duplicated.

**Result (posted): prime excess is UNBOUNDED.** For every `c ≥ 1` there is a prime poset `P_c` on `27c` elements with
`F(P_c) − ceil(log2 e(P_c)) ≥ 2c+1`.

**Mechanism.**
- **Base (`n=27`):** `P_1 = (A_13 ⊕ A_14)` minus one cross relation. Prime (both graphs connected), `e(P_1) = 13!14! + 12!13! = 545843785537290240000` with `ceil(log2 e)=69`, and `F(P_1) ≥ S(13)+S(14)=34+38=72`, so excess ≥ 3.
- **Amplification lemma (paper proof):** for prime `X,Y`, maximal `x∈X`, minimal `y∈Y`, the poset `P=(X⊕Y)−{(x,y)}` is prime and satisfies `e(P) ≤ 2e(X)e(Y)`, `F(P) ≥ F(X)+F(Y)`, hence `d(P) ≥ d(X)+d(Y)−1`.
- **Iteration:** gluing one new copy per step gives `|P_c|=27c`, `F≥72c`, `e<2^{70c−1}`, hence `d≥2c+1`.

**Falsification work.** Base `e` computed by two independent exact counters plus a third shuffle count; primeness recomputed by BFS and union-find for `n=27,54,81`; the counting lemma and `F`-monotonicity checked on 400 random poset pairs and all 100 prime `n=8` gluings. Exact `e(P_2)=299583934975889577931693474027929600000000` (ceil 138) gives excess ≥ 6 at `n=54`.

**Also addressed in the post.** The full fan family `A_m⊕A_k` with `r` deleted relations (exact `e` formula) has max excess 3 over all published `S` values — it cannot grow; the `W=C1⊕Q⊕C1` trick preserves `e,F` but destroys primeness; the family's unboundedness comes from the gluing, not from deleting more relations.

**Honest limit stated on the board.** The construction has height `2c`, so the height-2 (fixed-height) prime supremum remains open; that is the next decisive question.

No repository, Lean, branch, test, or PR changes. Scratch is only `/tmp/opencode/primeunb`.
