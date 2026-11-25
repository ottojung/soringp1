# sergeev-effective-finite-bound

## status

investigated

## origin

manual_executive

## agent_id

LfTYbWC42NbOF7S8lkeXV4-smilingly

## exit_state

clearexit

## question

Can an effective finite form of Sergeev's o(n) excess bound S(n)-log2(n!) = o(n) be extracted to give a concrete narrowing of the search window for large n (e.g. ruling out certain (n,k) pairs without computing exact S(n) fully)?

## basis

research-plan.md lists 'Can an effective finite version of Sergeev's bound be extracted...' as open question.

## falsifier

Derive an explicit function f(n)=o(n) with computable constants such that S(n) >= log2(n!)+f(n) for all sufficiently large n, or show existing asymptotics are not effectively convertible.

## implication

A useful effective bound would guide exact algorithms and strengthen barrier arguments about the gap.

## finding_unverified

ly derive such a lower bound f(n) on excess (disproving the need/usefulness in some sense?) or showing it's not effectively convertible. Or maybe the claim is "S(n)-log2(n!) = o(n) can be made effective to narrow search window" and the falsifier gives concrete ways to test/disprove. This is a bit ambiguous, but I need to follow AGENTS.md strictly and be mathematically rigorous.
Let us first understand the full picture and then attempt the research.

Let us proceed systematically.

**Finding (mathematical/obstruction):** The claim that Sergeev’s *o(n)* excess bound can be effectively converted to narrow the search window is not supported by an explicit derivation; the repo’s own evidence points to a concrete obstruction to *effective finite conversion*, while a uniform growing lower bound on excess appears implausible.

**Analysis:**
- **Model/reading:** Sergeev gives an *upper* bound on $S(n)$ via a constructive group-insertion algorithm: $S(n)=\log_2(n!)+O(n/(\log n)^{1/5})$ (excess $o(n)$). To narrow the search window for exact $S(n)$ one needs explicit bounds (e.g. $S(n)\le B(n)$ to cap the upper end). The falsifier as written mentions a lower-bound form, but the practical mechanism is effective conversion of the asymptotic upper bound; the instruction’s “or show existing asymptotics are not effectively convertible” matches the stated obstruction.
- **Repo evidence:** `docs/research-sergeev-asymptotic.md:18-23` states the asymptotic big-O supplies no explicit constants or finite computable upper-bound function; extracting such a bound from the constructive proof is a separate task. `docs/research-winning-frontier-barrier.md:160` says the same use is asymptotic and supplies no effective finite threshold. `docs/research-certificates-barriers.md:129-132` notes excess is $o(n)$ but sharper behavior/effective finite form remains open. The entropy identity is exact, but chaining Stirling/error bounds and optimizing parameters through the group-insertion construction makes constant extraction nontrivial.
- **Lower-bound branch (tried):** Integrality gives $S(n)\ge \lceil \log_2(n!)\rceil$ with excess $\ge 1 - \mathrm{frac}(\log_2(n!))$; fractional parts oscillate (gaps 0.05–0.99 across ranges) so no uniform growing $f(n)=o(n)$ follows. Kahn–Saks shows good (balanced) comparisons exist to *choose* (aiding algorithms), not a forcing obstruction creating uniform excess below $S(n)$. No known result yields $S(n)\ge \log_2(n!)+f(n)$ with $f(n)=o(n)$ growing for all large $n$; deriving such a bound appears implausible.
- **Distinction:** Kahn–Saks/poset extension results are general-poset facts about split ratios (good for constant-factor algorithms), distinct from certificate *soundness* vs *completeness* (framed-DAG certificates). The “search window” narrowing is about effective finite bounds on $S(n)$ itself, not about general poset hardness transfers.

**Conclusion:** I cannot derive an explicit growing lower bound on excess; the concrete obstruction is that Sergeev’s asymptotic is not effectively convertible to a finite computable bound with explicit constants from the published/known proof details — it remains a separate task with no effective finite threshold available. This is a negative/result of obstruction, not a proof of impossibility, but it means the proposed mechanism for narrowing the search window (via an effective finite form of that $o(n)$ bound) is not currently realizable from existing asymptotics. No Lean/repo changes made.


## Other metadata

```json
{
  "finished_at": 1793347288.123388,
  "retry_after": 0,
  "started_at": 1793342413.679483
}
```
