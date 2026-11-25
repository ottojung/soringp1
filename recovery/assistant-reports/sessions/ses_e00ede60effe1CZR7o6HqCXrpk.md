# antonina-JBM9oMcOCQhcrDkatBgKZw-duties

Session: ses_e00ede60effe1CZR7o6HqCXrpk
Workspace: /home/lubko/soring-fronts/cross-cost-additivity-ceiling-alln
Created: 1795280739061; updated: 1795284961204

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 20 (msg_1ff20fabc001B71MoCggfLdNHt)

I'll start by inspecting the current state carefully — host, git state, working directory, and durable records — before doing anything, per the recovery instructions.

## Output 31 (msg_1ff21071a001pRH9W4ppH2JXfF)

I'm on billy-dev, branch `billy-dev`, clean tree. Let me inspect the docs, board records, and any durable task records from earlier work.

## Output 46 (msg_1ff2118f0001sDUcO94TRl7vIm)

Working tree is clean; all files share a checkout timestamp. Let me read the key docs and find where board #301 lives and what durable records exist.

## Output 65 (msg_1ff21277a001peqmDHnb38LXT6)

Let me check the research board digest, the durable ledger, and any git/stash records of interrupted work.

## Output 80 (msg_1ff213852001doYMYPB0dZtFnc)

Let me check whether this exact front has already been worked/posted, and look for scratch work from the interrupted turn.

## Output 95 (msg_1ff219a640015gDa7PvRpz3QmE)

Let me examine the specific ledger entry for this front and search scratch files for related work from the interrupted turn.

## Output 140 (msg_1ff220263001WMPNmLg6csEVln)

I've confirmed: this front (`cross-cost-additivity-ceiling-alln`) started at 17:05:37; no board post, repo change, or scratch artifact from it exists yet. This is a fresh attempt. Now let me build a from-scratch exact minimax evaluator and attack the claim.

## Output 176 (msg_1ff25435b001RtKsQPvDwdFy0M)

I spotted a bug in my `disjoint_union` helper — it was adding spurious cross-relations (forcing B above the chain). Let me fix and validate against the known deficit-1 witnesses.

## Output 212 (msg_1ff2617b8001c4oewlhZ9Y10fF)

Validated the evaluator against known witnesses (all give D=1). Now let me search larger posets for larger excess (a proven necessary condition for D≥2) and test D on those.

## Output 223 (msg_1ff26fc90001IgWSD3pvCBVYtg)

The poset generator had a transitive-closure bug. Let me fix it and re-run the search.

## Output 261 (msg_1ff290e66001aabdf6aKbbwqCN)

Empirically D≤1 across all small posets. Let me investigate whether a general bound D≤1 (equivalently d(n)≥−1 for the a=1 antichain family) is a known theorem, via primary literature search.

## Output 272 (msg_1ff29856e001R3r8MZgK3QF4nr)

Let me read the full text of the key board posts (T1 cross-comparison theorem and the potential-method no-go) to avoid rediscovering closed routes.

## Output 290 (msg_1ff2a463b001gmLhMmD7sz3Cay)

Now let me test a potential-function proof strategy for the constant bound D≤1 on all reachable cross-augmented states — this is a distinct potential (log-interleaving count), not the closed m+1 one.

## Output 308 (msg_1ff2add940016y03lZ74fUZT4m)

The scalar-potential route fails (I show a concrete violation). Let me instead run a broader exhaustive falsification over all b=5 posets and larger a.

## Output 319 (msg_1ff2ca3d9001sj9qZb49Ek8CvX)

Let me check the literature for a known lower bound on the increment S(n)−S(n−1), which would settle the a=1 case of boundedness.

## Output 348 (msg_1ff2d3447001iuxK1kSHlomKrp)

Let me sample b=7 posets to find any with information excess ≥2 (necessary for D≥2), then test D on those.

## Output 359 (msg_1ff32162700122O7Z6FlCBM738)

Let me fetch the exact known sorting numbers to analyze the excess Δ(n)=S(n)−⌈log₂ n!⌉.

## Output 379 (msg_1ff32772b001nrmacg3j1YIF1T)

I've found a clean exact decomposition of the deficit. Let me test the remaining criterion (Δ(B)=1, g=1, Δ(P)=0) on the best candidate posets.

## Output 418 (msg_1ff50f83b001oXc3glMKMeZOI3)

I'll re-inspect state after the interruption before continuing.

## Output 433 (msg_1ff514f9d001qOmqGY4yj0zN0G)

State is clean — no external side effects from my front. Let me read the new board posts that reference this front before finalizing the analysis.

## Output 462 (msg_1ff518ea8001JLIW79NO68wfTT)

State is clean and I've completed the mathematical work. Let me find the correct board-post command, then make exactly one post.

## Output 480 (msg_1ff51da0d001TGB6Rc94XGVfKU)

I'll write the finding to a scratch file, then post exactly once to board #301.

## Output 500 (msg_1ff5238c0001zkF8CgRFOyyQk6)

The post command succeeded; let me verify exactly one comment landed.

## Output 511 (msg_1ff526332001nac5QI3CLb7b4x)

Done. After the backend-failure interruption I re-inspected state: the repo was clean at `6a96398`, no commit/stash/board post from this front existed, and the ledger still showed it `running`. No effects were duplicated. I resumed the computation, finished the analysis, and made exactly one board post (verified: a single comment, 18:15:35Z).

## Mathematical finding

**Exact decomposition (deduction, all-n).** Let `F` be the exact adaptive minimax, `e(P)` the extension count, and define the information excess `Δ(Q) = F(Q) − ⌈log₂ e(Q)⌉ ≥ 0`. For `P = C_a ⊔ B`, with `C = binom(a+b,a)` and `e(P) = C·e(B)`:

```
D(a,b,B) = Δ(B) − Δ(C_a ⊔ B) + g(a,b,B),   g = ⌈log₂e(B)⌉ + ⌈log₂C⌉ − ⌈log₂(e(B)·C)⌉ ∈ {0,1}.
```

So `D ≤ Δ(B) + 1`, and **`D ≥ 2` forces all three of**: `Δ(B) ≥ 1` (B strictly beats its own information bound), `g = 1`, and `Δ(C_a ⊔ B) = 0` (the union is information-tight). Unbounded `D` therefore requires unbounded `Δ(B)`. For the antichain family this reduces further to `D(1,b,A_b) = −d(b+1) = Δ(b) − Δ(b+1) − [ceiling bracket]`.

**Falsification search (from-scratch minimax, validated on S(n) for n≤6 and all three stated deficit-1 witnesses).** Exhaustive over all 4231 labelled b=5 posets (a=1,2), all b≤4 with a+b≤7, all 130023 b=6 posets screened for Δ plus top candidates tested, and 13602 sampled b=7 posets: **maximum observed D = 1**. No `D ≥ 2` witness. Best near miss: b=7, F(B)=6, e=21, a=2 has `Δ(B)=1` and `g=1` but `Δ(P)=1`, giving D=1.

**Concrete failed approach.** A natural non-closed potential `Φ(Q)=F(B_Q)+log₂ I_min(Q)−1` on cross-augmented states is refuted: at root (a=1,b=3,A₃), `Φ=4` but both children of a cross comparison have `Φ=2` (interleaving count collapses 4→1). This is a different obstruction from the already-closed `m+1` potential no-go — here the interleaving-count term itself is not 1-Lipschitz under cross transitivity.

## Honest limits

I did **not** prove `D ≤ 1` for all a,b,B, nor exhibit `D ≥ 2`, nor prove unboundedness. The question reduces to the all-n behavior of the minimax excess `Δ`: it is 0/1 for antichains through n=22 (OEIS A036604) and ≤1 for every poset I checked up to size 7, but its all-n behavior is open. This concerns exact minimax only — no general-poset hardness transfer and no certificate-completeness claim is made. No repository, Lean, test, CI, or ledger changes; scratch work is in `/tmp/opencode/crosscost/`. S(n) and SORT-BOUND-U remain open.
