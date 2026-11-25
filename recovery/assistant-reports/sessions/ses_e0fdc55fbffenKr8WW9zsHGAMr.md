# antonina-8JgLl8sY4XxqJY7xbQFDIS-protest

Session: ses_e0fdc55fbffenKr8WW9zsHGAMr
Workspace: /home/lubko/soring-fronts/join-reduced-canonical-strategy-alln
Created: 1795030231680; updated: 1795031110671

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f023ad7c001T8IQSWoffiTgfj)

I'll start by understanding my environment and the repository. Let me check where I am and what "billy-dev" refers to.

## Output 17 (msg_1f023b9e4001PYqBpYSyKUBGeJ)

I'm on `billy-dev` as required. Let me study the key documents and find the research board #301.

## Output 40 (msg_1f023cde4001wWh1EkG2pCxXQi)

Now let me read the board digest and find the specific front details and prior work (including `curator_verify.py`).

## Output 72 (msg_1f023f792001wGehVaSWzXVwUy)

Let me get the full text of the key board posts and understand the board tool's options.

## Output 100 (msg_1f0241ef6001myDjFkq5YTAl1Y)

A fresh worktree with no prior board post from my front. Let me read the curator scratch files that motivated this front.

## Output 119 (msg_1f02432610018jn3wmZYFuCjhY)

Let me understand the underlying model code used by the prior work, then examine the framed-DAG "state count" meaning from the board.

## Output 134 (msg_1f024d7c6001ZYK71tQpYdncoZ)

Let me verify the prior computations and analyze exactly what the "state counts" include.

## Output 145 (msg_1f02535b4001vgvcxsQYEaRFyv)

Let me examine the framed-DAG certificate work to understand precisely how "state count" is defined there.

## Output 203 (msg_1f025f9f700170xdHtoI8pcZE2)

Let me read the full text of the most relevant prior certificate/framed-DAG reports to avoid repeating findings and to pin down the "state" definition.

## Output 214 (msg_1f0260fee001QPevvgMIcyjp8R)

The prior work reveals a crucial tension. Let me read the framed checker and frontier doc to understand whether "n! leaves" is a valid lower bound for certificates.

## Output 240 (msg_1f0269831001FmCmJgw9jXKddr)

I now have a strong theoretical lead. Let me verify it rigorously with independent computation: the claim that *every* deterministic comparison strategy reaches exactly `2n!−1` distinct posets (path→poset injective), which would make the FRONT's "polynomially many states" impossible.

## Output 251 (msg_1f027e33c001WbrIJHj2Thx0qG)

Let me stress-test the injectivity claim across many strategies (including non-optimal ones) and check whether non-join-reduced optimal strategies exist.

## Output 262 (msg_1f0288093001cAUbpgKRJyv6UM)

Let me read the two freshest confluence reports in full to understand exactly what witnesses they found and reconcile with my sampling.

## Output 277 (msg_1f028ae4c0014kd96wJjL6cgn7)

Let me check two things: (i) whether optimal strategies are always "tight", and (ii) whether the confluence witness states can co-occur in a single optimal strategy's reachable set.

## Output 288 (msg_1f02a86cf001r7l2bYw5tshKEA)

Let me check the posting mechanism and confirm no prior post exists from my front, then check git state for side effects.

## Output 341 (msg_1f03062c1001kGoDADO3Ayhqrc)

All checks confirm the theorem. Let me write the board report and post it to #301.

## Output 359 (msg_1f030d3dc001jtiRDt804Jri3u)

Let me verify the post landed and confirm the worktree is still clean.

## Output 370 (msg_1f030eb5d001ubC0uESYmrV15y)

Done. I worked entirely on `billy-dev` in the assigned worktree, studied the contract/problem/board #301 and the relevant primary literature, and attacked the FRONT claim. Here is the honest outcome.

## Mathematical finding (deduction, all n): the FRONT is false

**Theorem.** For *any* deterministic comparison‑sorting strategy Σ on n distinct labelled keys, the map (root‑to‑node outcome path) → (poset at that node) is injective, so Σ has **exactly 2n!−1 distinct reachable posets** (n! chains + n!−1 internal states).

*Proof.* A correct sorter has one leaf per input permutation = n! distinct total orders, hence n!−1 internal nodes. Two distinct paths share a maximal prefix ending at state S, then diverge at a comparison (i,j): one branch adds i<j, the other j<i (i,j incomparable in S). All later states are transitive closures of consistent supersets, so they permanently contain i<j vs j<i — a poset cannot contain both. So distinct paths never yield the same poset. ∎

**Corollary.** 2n!−1 is superpolynomial for n≥4, so *no* strategy — canonical or otherwise, join‑reduced or not — has polynomially many reachable states. The FRONT's existence claim fails for every n≥4. Verified computationally: 47/239/1439 = 2n!−1 for n=4/5/6, path‑injective for optimal and hundreds of random non‑optimal strategies.

## Correction of the premise (experiment + deduction)

The cited "join‑reduced optimal strategies at n=5 (239 states) and n=6 (1439 states)" are precisely **2·5!−1 and 2·6!−1 — the full reduced trees**, the maximum possible count. They are not "compact canonical optima"; the ratio 1439/239≈6 exposes factorial growth. So the basis does not support the FRONT — it refutes it.

## Structural clarification (exact obstruction)

Two objects were conflated: (a) reachable labelled posets of one strategy (universally 2n!−1, never polynomial; this is where join‑reducedness lives), and (b) framed‑DAG annotation states (compressible to polynomial via join+frame identifications, e.g. the known 19‑node n=7 certificate). Compression happens on (b), so join‑reducedness of (a) is irrelevant to certificate size. Moreover, a lossless join `F(P)=F(Q)=F(P&Q)` is exactly the merge join‑reducedness forbids — so requiring it removes the only surplus‑free state identification, and cannot produce compactness. The genuinely open question (framed‑DAG completeness / no‑cheap‑coarsening) is a different front.

## Honest limits

- Refutation holds under the stated "reachable labelled posets" reading; if "states" meant framed‑DAG annotations or isomorphism classes, that is a separate, already‑tracked question.
- This does **not** show SORT‑BOUND‑U ∉ NP, does not prove superpolynomial certificates, and leaves SORT‑BOUND‑U ∈ PSPACE unchanged — no complexity‑class result.
- "Every optimal strategy is join‑reduced" is only experimental (n≤6, thousands of sampled strategies; confluence‑witness states never co‑occur in one strategy), **not proved**.
- No genuine new theorem about certificate completeness was found; I did not manufacture one.

**Deliverables:** one concise finding posted to Antonina #301 (timestamp 19:44:50Z); worktree clean at `6a96398`, no stash, no repo/Lean/test/workflow/ledger changes (scratch code only in `/tmp/opencode`).
