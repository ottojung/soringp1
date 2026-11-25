# sergeev-effective-constant-barrier

## status

investigated

## origin

executive_proposed

## agent_id

KwQNr4JnjZw2FMHpC4Y1gF-selected

## exit_state

clearexit

## question

Can one extract a finite, explicit effective bound from Sergeev's group-insertion construction (giving S(n) <= log2(n!) + C n / (log n)^(1/5) for all large n) sufficient to narrow the exact S(n) search window without materializing exponential state graphs, and does any such finite extraction preserve the o(n) excess in a form useful for exact unary SORT-BOUND-U evaluation?

## basis

Sergeev ECCC TR20-096 / 2021 J. Appl. Ind. Math. gives log2(n!)+O(n/(log n)^(1/5)); docs/research-sergeev-asymptotic.md notes extraction of explicit finite bounds is open and crucial for exact evaluation.

## falsifier

Prove the constructive constants/parameters are inherently non-explicit or force exponential preprocessing in the exact-evaluation model, or construct a case where known finite recurrences cannot exploit any finite Sergeev window to improve worst-case exact algorithms below known bounds.

## implication

A sound effective finite Sergeev bound would bridge asymptotic algorithm and exact evaluation for unary SORT-BOUND-U without claiming a complexity class separation.

## finding_unverified

 “no exponential state graph” constraint.** Even if one tracks all constants, to *compute* `B(n)$ for a given `n$ you would need to evaluate the module choices (and possibly simulate the group-insertion schedule) up to the size needed — the structure is a tree of recursive/group modules over `n$; naive bookkeeping risks simulating the construction itself (preprocessing comparable to building that sorter) rather than a cheap formula. Combined with the ceiling/accounting pitfalls seen in `referee_sergeev_ceiling_audit.py` style checks, a direct “extract formula” route appears to force exponential/expensive preprocessing in general.
3. **No automatic bridge to exact minimax pruning.** `S(n)$ is the minimax (adversarial worst-case) over all poset states; Sergeev gives some comparison tree of height `B(n)$ (a constructive sorter). Knowing `S(n) <= B(n)$ gives a binary-search upper bound for `SORT-BOUND-U$, but it does **not** by itself narrow the *exact search window* for the minimax recurrence in a useful way without exploiting structure: the adversary can still force branches not obviously pruned by “there exists some good tree”, and the o(n) excess is an average/constructed-tree property, not obviously a worst-case state graph invariant exploitable by known finite recurrences. Also `docs/research-framed-certificate-frontier.md:192-199` emphasizes global control states are nontrivial.

### Distinction (required)
- **General-poset results vs `S(n)$.** Hardness/complexity results for arbitrary posets do not transfer to the fixed antichain family without reduction; certificate **soundness** (any valid certificate is correct) is different from **completeness** (every optimal/all-n instance has a polynomial certificate). The group-insertion tree is a sound sorter but gives no obvious all-n polynomial-certificate completeness.
- **Complexity classes.** A sound effective finite `B(n)$ would bridge asymptotic algorithm and exact evaluation for unary `SORT-BOUND-U$ (better upper bound / tighter search window) without claiming `P!=PSPACE$ or `NP!=PSPACE$; unary `SORT-BOUND-U \in PSPACE$ already holds and is sparse (Mahaney) so circuit lower bounds blocked as noted in `AGENTS.md/problem.md`.

### Honest limits
- I did **not** derive explicit constants from the published proof (the obstruction above is structural). The 1/4-rate moving-parameter derivation was already shown not to appear in the paper.
- Even if constants were extracted, “useful for exact unary `SORT-BOUND-U$ evaluation” is not automatic — no concrete pruning mechanism is obvious and would need separate proof; the falsifier is plausible (preprocessing cost / no exploitation of worst-case minimax). 
- No Lean/repo changes made (no genuinely substantive independently checkable new theorem/counterexample produced here; only analysis of existing literature/board/referee work).

**Conclusion:** The precise obstruction is **effective finiteness**: the constructive proof gives asymptotic `O(\cdot)$ with asymptotic parameter choices and no published universal finite cutoff; extracting explicit `B(n)$ for all large `n$ appears inherently non-explicit or would require simulating/extracting the full construction (exponential/expensive preprocessing) without obvious benefit to worst-case minimax exact search — making a cheap, effective finite bound useful for exact `SORT-BOUND-U$ evaluation not obviously achievable from the published group-insertion argument. No complexity class separation follows.

## Other metadata

```json
{
  "finished_at": 1793517851.4069512,
  "started_at": 1793516994.2180805
}
```
