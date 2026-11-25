# antonina-DCdBkJCIu5N2ZWF4jYOZUY-chronic

Session: ses_e42a2307dffeNKzhBPH7wlDg1w
Workspace: /home/lubko/soring-fronts/succinct-farkas-dual-certificate
Created: 1794178404311; updated: 1794178953581

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 315 (msg_1bd6606e5001V2t69UaraCjZUc)

## Result

**The universal succinct-Farkas claim is false.** On billy-dev I found an infinite all-`n` family of genuine non-sortable unary instances for which **every** Farkas certificate of the faithful state-expanded LP has exponential support, hence certainly not polynomial in `N=n+k+1`.

Take even `n ≥ 4` and `k=n/2`. Since `n! > 2^{n/2}`,

\[
S(n)\ge \lceil \log_2 n!\rceil > n/2 = k,
\]

so these are NO instances of `SORT-BOUND-U`. I proved:

\[
\operatorname{support}(y)\ \ge\ \#\{\text{perfect matchings of }K_n\}
=(n-1)!! \ge (n/2)!.
\]

Because `N = n+n/2+1 = Θ(n)`, this is

\[
2^{\Theta(n\log n)}=2^{\Theta(N\log N)},
\]

so support is not merely superpolynomial; it is exponential in `N log N` on this family. The coefficient-bit-length clause is therefore moot.

## Proof core

In the dual, normalize the root multiplier to `r=-1`, giving `a_{A_n,0}>0` for the root state multiplier. For any non-total state `P` at depth `t<k` with `a_{P,t}>0` and any incomparable pair `e`, the dual inequality for the corresponding `x`-variable is

\[
a_{P,t}+b_{Q_1}+b_{Q_2}+h_e\le 0,
\]

where `Q_1,Q_2` are the two children and `h_e≥0` is any upper-bound multiplier. Thus at least one child has `b_Q<0`. Along a set of pairwise disjoint comparisons, both children remain non-total and no transitive closure is forced. Induction shows every `t`-matching produces a distinct labelled poset at layer `t` carrying a nonzero dual multiplier.

At `t=k=n/2`, these are distinct perfect-matching states, all non-total. So every Farkas certificate must have at least `(n-1)!!` nonzero multipliers.

The argument is robust to the `0≤z,x≤1` bounds: setting `h_e≥0` only weakens the child inequality, and the root multiplier still satisfies `a_root≥1+h_root≥1`.

## Meaning and limits

- This is a **proof-size barrier**, not a correction to LP exactness or the rank-0 result. The LP remains exact; its CG rank remains `0`. Rank and dual succinctness are genuinely different.
- It blocks the proposed “polynomial Farkas certificate ⇒ coNP” route **for this state-expanded encoding**.
- It is not a general-poset hardness result; the argument is entirely at the antichain root and uses only the information bound.
- It does **not** prove `SORT-BOUND-U ∉ coNP`, does not rule out other LP or certificate encodings, and does not address near-optimal `k=S(n)-1`. The family has `k≈n/2`, far below `S(n)`.
- A claimed polynomial-support certificate for these matching instances would directly contradict the matching count, so the claim is sharply falsifiable.

## Side effects / state

- Inspected the existing ledger front (`succinct-farkas-dual-certificate`, previously `running` with empty finding), board #301, the relevant rank-0 correction, and prior refuter/certificate work. No prior post from this front existed.
- Posted exactly one new board comment to #301: message index `2530`, `createdAt 2026-11-08T23:02:10.237Z`, id `sha256:WRXHEVE4XsQzTrO7lU4HJeAcXgulMEzbvO8wPXiuzdE`.
- No Lean files, repository commits, or worktree changes were made. `git status` remains clean on `billy-dev`.
