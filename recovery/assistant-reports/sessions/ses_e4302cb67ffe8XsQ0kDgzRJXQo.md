# antonina-cZJaQwddVz337JVq4cbJVX-bridges

Session: ses_e4302cb67ffe8XsQ0kDgzRJXQo
Workspace: /home/lubko/soring-fronts/positive-density-framed-completeness
Created: 1794172073195; updated: 1794173289224

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 162 (msg_1bd0d29ef001Nd7RfNMQtN1saU)

## Report: density front for exact-height framed certificates

**Status: no repository or Lean changes; worktree clean. I did not post to board #301.** I read `AGENTS.md`, `docs/problem.md`, the board digest around #301, `docs/research-framed-certificate-frontier.md`, `docs/research-strategy-certificates.md`, `docs/research-certificates-barriers.md`, the checker, and the primary-source summaries (Sergeev ECCC TR20-096; Stober–Weiß arXiv:2206.05597). The main finding is a **model/complexity-implication obstruction**, not a resolution of the density question.

### 1. The front is not falsifiable as written without fixing the polynomial convention

Let `size_opt(n)` be the minimum number of nodes of a framed DAG accepted by `scripts/check_framed_strategy.py` whose height equals `S(n)`. The full optimal decision tree, with identity frames, is an accepted framed DAG of height `S(n)` and size `2·n! − 1`; so `size_opt(n)` is finite for every `n`.

Under the **pointwise** reading “for each `n` there exists some polynomial bound depending on `n`,” the set is trivially all of `N`: for `n ≥ 2`, choose `c_n = ceil(log_n(2·n! − 1))`, then `2·n! − 1 ≤ n^{c_n}`. Hence the answer would be “density one” for a completely non-complexity reason. The intended reading must be a **single fixed polynomial** `p` (or fixed degree `c`), with

\[
A_p=\{n:\ size_{opt}(n)\le p(n)\}.
\]

Even then one must specify positive upper density versus positive lower density versus existence of asymptotic density; a set need not have a density at all. The front currently conflates these.

### 2. The stated complexity implication is false

The front says positive density would “localize the all-n obstruction to NP membership … to a density-zero exceptional set.” That does not follow.

- If `A_p` has positive density `δ`, its complement can have density `1−δ`, not zero.
- Even density one allows an infinite complement, e.g. `N \ {2^j}`.
- NP membership of `SORT-BOUND-U` needs a certificate for **every** yes input, including boundary inputs `(n, S(n))` for exceptional `n`.

What is true is:

**Lemma A (cofinite exact completeness suffices).** If some fixed polynomial `p` has `A_p` cofinite, then `SORT-BOUND-U ∈ NP`.

*Proof.* For all sufficiently large `n`, guess the exact-height certificate of size `≤p(n)`; the checker verifies soundness and height `≤k`. If `S(n)≤k`, the exact-height certificate has height `S(n)≤k`; if `S(n)>k`, soundness rejects every accepted DAG. The finitely many smaller `n` have fixed thresholds `S(n)` and can be hardwired. ∎

Positive density gives none of this. Even density one is insufficient unless the infinite density-zero exceptional set has an independent polynomial-time decision procedure or its own certificates. Thus the only clean density-to-NP sufficient condition is **cofiniteness**, not positive density.

Also, exact-height completeness is stronger than necessary for NP: a yes instance `(n,k)` with `k>S(n)` only needs a framed certificate of height `≤k`, not exactly `S(n)`. Density zero of `A_p` would therefore show incompleteness of the *exact-optimal* framed compression, not necessarily of the framed grammar as a threshold-certificate system.

### 3. What density can actually transfer: an additive `O(log n)` gap

The strongest natural density strengthening short of cofiniteness is **syndeticity** (bounded gaps).

**Lemma B (deduction).** Suppose some fixed polynomial `p` and constant `C` are such that every interval `[m−C,m]` meets `A_p`. Then every `m` has an accepted framed certificate of size `poly(m)` and height

\[
\le S(m)+C\lceil \log_2 m\rceil .
\]

*Proof sketch.* Choose `n∈[m−C,m]` with an exact certificate. Append after every leaf the standard binary-insertion framed sub-DAG for the at most `C` new elements. Each insertion costs at most `ceil(log₂ j)` comparisons for `j≤m`, so the added height is at most `C ceil(log₂ m)`. A size-`N` DAG has at most `N` leaves, so the number of appended copies is polynomial; the insertion sub-DAG has polynomial size. Composition preserves soundness. ∎

So even a fairly strong density hypothesis yields only a **logarithmic surplus**, not exact `S(m)`. This is a precise obstruction to moving from positive density to exact all-`n` completeness by the obvious lifting route.

### 4. The natural exact lift fails concretely

Binary insertion from an optimal `n`-certificate gives height

\[
S(n)+\lceil \log_2(n+1)\rceil .
\]

This exceeds `S(n+1)` already at small `n`:

| `n→n+1` | `S(n)` | insertion height | `S(n+1)` |
|---|---:|---:|---:|
| 4→5 | 5 | 8 | 7 |
| 8→9 | 16 | 20 | 19 |
| 16→17 | 46 | 51 | 50 |

Thus exact-height framed completeness is **not** closed under the naive `+1` lift, so a positive-density set cannot be propagated upward by insertion. This is a concrete failed approach to either density horn.

### 5. Why neither density-zero nor a positive-density family follows from current literature

**Known constructions do not give exactness.** The standard polynomial-size framed families have linear surplus over the information bound:

- For `n=2^r`, the balanced merge-sort framed construction has height `n log₂ n − n + 1`, while `C(n)=ceil(log₂ n!) = n log₂ n − (log₂ e)n + O(log n)`; the surplus is `(log₂ e−1)n+O(log n) ≈ 0.4427n`.
- Ford–Johnson has height `FJ(n)=C(n)+Θ(n)` (numerically about `0.1n` in the tested range), and Sergeev’s theorem gives `S(n)=C(n)+o(n)`, so Ford–Johnson cannot remain exact for all large `n`.

Hence the known poly-size framed families do **not** witness positive density. Sergeev’s `o(n)` improvement is an algorithmic sorting bound; its compatibility with a polynomial-size framed DAG with sound joins is exactly the open “Sergeev compatibility” item in `docs/research-framed-certificate-frontier.md §5`.

**No infinite exact `S(n)` family is known.** Primary literature determines `S(n)` only through `n≤22`, with partial lower bounds beyond (`S(28)≥99`). There is no known infinite family of `n` with `S(n)` exactly determined. A positive-density construction would require either such a family with explicit framed certificates or a universal optimal compression theorem. Neither exists.

**Density zero is also blocked by the known lower bound.** Any accepted framed DAG of height `h` has at most `2^h` root-to-leaf paths, and the `n!` input permutations require distinct paths, so `h≥ceil(log₂ n!)=C(n)`. That is the only universal lower bound. A polynomial-size DAG can have far more than `n!` paths, so path counting cannot force super-polynomial size. A density-zero theorem would therefore require a new super-polynomial lower bound on **optimal-height** framed DAG size. The entropy/forgetting identity in the note gives only an average `o(n)` forgetting condition along a special walk; it does not bound node count. General-poset results (Kahn–Saks, Kahn–Kim, Brightwell–Winkler) concern approximate sorting or counting for arbitrary posets and do not transfer to this antichain-root framed-DAG size question.

### 6. Corrected front and honest limit

The non-vacuous, complexity-relevant question is not positive density but:

> Fix a polynomial `p` and let `A_p={n: size_opt(n)≤p(n)}`. Is `A_p` cofinite for some `p`? Equivalently, does every sufficiently large `n` admit a polynomial-size framed DAG of height exactly `S(n)`?

A meaningful weaker density question is whether `A_p` has positive upper density for some fixed `p`. But:

- positive density of some `A_p` does **not** localize the all-`n` obstruction to a density-zero set;
- syndeticity of `A_p` gives only height `S(n)+O(log n)` for all `n`, not exactness;
- cofiniteness of `A_p` does imply `SORT-BOUND-U ∈ NP`;
- density zero of every fixed-`p` set would be a structural incompleteness of exact-optimal framed compression, but does not follow from current lower bounds and is not equivalent to non-membership in NP.

**Conclusion:** I did not prove either density horn. I did disprove the front’s stated complexity implication and identify the exact missing step: positive density is the wrong density notion for NP localization, and the natural density-to-all lifting loses an unavoidable-looking `O(log n)` comparison surplus. The remaining mathematical obstruction is a super-polynomial lower bound on optimal-height framed DAG size, or equivalently a proof that exact optimal sorting cannot be compressed into polynomially many framed states on a dense set of `n`. No such theorem is presently available.

## Output 263 (msg_1bd0f74ce001hQSnSFXmtbzK35)

Recovery inspection complete. I did not repeat the research prompt or create any new external effects.

**Verified state**
- Host: `billy-dev`.
- Working directory: `/home/lubko/soring-fronts/positive-density-framed-completeness`.
- Git: clean worktree, `HEAD = 6a96398`; no commits, edits, Lean files, or repository changes.
- Durable ledger: front `positive-density-framed-completeness` is still marked `running` under agent `cZJaQwddVz337JVq4cbJVX-bridges`, with no finding recorded yet. That is expected until the agent exits; I did not manually edit the ledger.
- Board #301: no comment from this front or agent. The only digest match for “positive-density” is an unrelated earlier front (`antichain-lookahead-depth`); searching the agent ID returns zero matches. No duplicate post was made.

**Effect assessment**
- Confirmed external effects from the previous turn: **none**.
- Confirmed repository effects: **none**.
- Uncertain effects requiring review: **none**.

**Prior result remains the completed deliverable**
The previous turn finished with a mathematical report, not a density theorem. Its substantive findings stand:
- The front’s stated complexity implication is false: positive density does not localize the all-`n` obstruction to a density-zero exceptional set; only cofiniteness gives a clean NP consequence.
- The natural exact-height lift fails concretely (`n = 4→5`, `8→9`, `16→17`), so positive density cannot be propagated by binary insertion.
- Syndeticity of a fixed-polynomial exact set would give only framed certificates of height `S(n)+O(log n)`, not exact `S(n)`.
- Neither density horn follows from current literature: no infinite exact-`S(n)` family is known, and the only universal framed lower bound is `height ≥ ceil(log₂ n!)`, far too weak to rule out polynomial-size optimal DAGs.

No unfinished side effect or duplicate action remains. The density question itself is still open; I have not converted the process into a proof.
