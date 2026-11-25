# antonina-7SdWltLyM68O4lRjPBBdNC-brand

Session: ses_e4b7c3261ffe3lp1sCnjb3PmQM
Workspace: /home/lubko/soring-fronts/exec-optimal-minimal-basis-20261107
Created: 1794029899210; updated: 1794029957463

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 117 (msg_1b4843cc9001nyrlQgh0CeHyjM)

The exact-optimal transfer has a clean arithmetic bottleneck: the matching family has `e(P)=n!/2^t`, so the stated Fredman guarantee gives `F(P) ≤ log₂(n!)−t+cn`, whereas winning at `S(n)` requires `F(P) ≤ S(n)−t = log₂(n!)−t+o(n)`. I’m checking whether a sharper structural estimate for these particular states follows from their product-of-chains structure; if not, I’ll report the precise obstruction without adding an artifact.

## Output 147 (msg_1b4846b1e001BhUn24b37gJ2D3)

## Conclusion

**No transfer is established** from the relation-inclusion minimal-basis argument to the exact budget `S(n)` or to Sergeev’s sublinear-surplus window for the requested matching states. The linear-surplus result remains valid, but its winning-state step uses slack that the exact-optimal budget does not provide.

For `t = ⌊n/4⌋`, the oriented disjoint-pair family has
\[
\frac{n!}{(n-2t)!\,t!}=2^{(1/4+o(1))n\log_2 n}
\]
distinct labelled states. Each is reachable in exactly `t` comparisons, has exactly `t` strict relations, and is inclusion-minimal among states reachable at that depth: any reachable substate must have at least `t` distinct comparable pairs, so inclusion forces equality. **That counting and minimality argument does not depend on the budget.** The unresolved condition is whether these states are winning.

For each matching state, `e(P)=n!/2^t`, so leaf counting gives
\[
F(P)\ge \lceil\log_2 e(P)\rceil=C(n)-t.
\]
This is a **lower bound** on `F(P)`, not evidence that the state wins. To be winning at budget `K(n)`, one needs the **upper bound** `F(P)≤K(n)-t`. Fredman’s cited guarantee supplies only
\[
F(P)\le \log_2(n!)-t+cn.
\]
It proves winning at `H_D(n)=C(n)+Dn` when `D` is sufficiently large, but it does not imply winning at `S(n)=C(n)+o(n)`. The gap is exactly the unabsorbed `cn` term; the earlier winning-frontier theorem concerns a different construction and does not establish this matching-family claim.

**Sharp conjecture:** for all sufficiently large `n`, every oriented matching state with `t=⌊n/4⌋` satisfies
\[
F(P)\le \log_2(n!/2^t)+o(n),
\]
uniformly over the matching and orientations. This would imply winning at `S(n)` only if the error is bounded by the *actual* surplus `S(n)-C(n)` (up to rounding), which Sergeev’s asymptotic bound alone does not guarantee. A precise sufficient conjecture is
\[
F(P)\le S(n)-t\quad\text{for every such state and all sufficiently large }n.
\]
Its falsifier is an infinite sequence of `n` and oriented matchings with `F(P)>S(n)-⌊n/4⌋`; even one such counterexample refutes the all-`n` version.

No structural upper bound for these states follows from the consulted sources. Their product-of-two-element-chains structure gives the extension count, but not an exact minimax sorting strategy within sublinear additive loss. The small checks recorded in the preserved worktree do not discriminate the asymptotic hypotheses. Establishing or refuting this stronger bound would require a new argument (or targeted exact values), not a restatement of Fredman or Sergeev.

**Scope:** even a superpolynomial minimal-basis result here would concern only explicit inclusion-minimal-state enumeration at fixed `(n,t,r)`. It would not imply a lower bound for arbitrary evaluators or for `SORT-BOUND-U`. No repository artifact was added.

## Output 166 (msg_1b484ad6b001S0dBz7WHQbpAsp)

Working tree is clean and no external side effects occurred (no commits, no posts, no files created). No unfinished work. Done.
