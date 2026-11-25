# antonina-gnEHOwyyDXDdZwRhMcdPYI-struggles

Session: ses_e455e57adffe0LMs0N5vWPY8Y0
Workspace: /home/lubko/soring-fronts/constant-round-am-sortbound
Created: 1794132519241; updated: 1794133906731

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 648 (msg_1bab4b9800017HkPFvJYu7qy21)

**Verdict:** I did not find an \(O(1)\)-round Arthur–Merlin protocol for `SORT-BOUND-U`, and I did not find a proof that every constant-round protocol fails. The front remains open. I did isolate a precise obstruction: the natural AM attack reduces to certifying a **threshold boundary**, and the missing step is a **universal no-witness check** (coAM-like), not “compressing the game’s alternation.” No repository or Lean changes were made; the worktree is clean at `6a96398`.

## 1. Claim attacked

\[
\textbf{Claim A: }\ \text{SORT-BOUND-U}\in \mathrm{AM}.
\]
Equivalently, since constant-round public-coin AM collapses to two messages, there is a public-coin protocol with one Arthur challenge and one Merlin response, perfect completeness, and soundness error \(<1/3\), for all unary inputs \((n,k)\).

The negation is:

\[
\textbf{Claim B: }\ \text{SORT-BOUND-U}\notin \mathrm{AM}.
\]

I could not falsify either. What follows is the strongest exact reduction I obtained.

## 2. Facts used

- `[literature]` \(\mathrm{APTIME}=\mathrm{PSPACE}\) (Chandra–Kozen–Stockmeyer), hence `SORT-BOUND-U` \(\in \mathrm{PSPACE}\) via the comparison game \(G(n,k)\).
- `[literature]` Constant-round public-coin AM equals two-message AM; private coins do not add power (Babai; Goldwasser–Sipser).
- `[literature]` \(\mathrm{AM}\subseteq \Pi_2^{\mathrm P}\), and \(\mathrm{AM}\subseteq \mathrm{NP/poly}\) by Adleman’s argument.
- `[literature]` Exact \(S(n)\) is known only through \(n\le 22\); for \(n\ge 23\) the value is open. Finite values cannot decide an all-\(n\) AM claim.
- `[literature]` General decision-tree/network hardness (Hyafil–Rivest, Laber–Nogueira, Parberry) concerns arbitrary tests or fixed networks and gives no reduction to the fixed antichain threshold \(S(n)\).

## 3. The useful reduction: a boundary normal form

`[deduction]` First, `SORT-BOUND-U` is polynomial-time equivalent to a **tally** language: encode the pair \((n,k)\) by a unary string of length \(t(n,k)=\mathrm{poly}(n+k)\). Thus any theorem about tally AM languages would apply.

Now suppose `SORT-BOUND-U` \(\in \mathrm{AM}\) with perfect completeness and soundness error \(\delta\). By amplification take \(\delta<1/(10m)\), where \(m=n+k+1\). For a fixed \(n\), all relevant thresholds \(k\le m\) are polynomially many. A union bound gives a single random string \(r_n\) of polynomial length such that, for **all** \(k\),

\[
k\ge S(n)\iff \exists \text{ Merlin message } w\ \text{with } V(n,k,r_n,w)=1.
\]

So AM membership yields a **nonuniform boundary certificate**: the whole cutoff \(S(n)\) is determined by one polynomial-size advice string \(r_n\). If the family \(\{r_n\}\) were polynomial-time computable from \(n\), the language would be in NP: the NP machine would compute \(r_n\), guess the witness \(w\), and use the fact that \(r_n\) is good for every \(k\). The hard step is exactly **derandomizing/finding the good advice**, not simulating \(k\) alternations.

There is also a self-reduction normal form. Merlin sends a candidate boundary \(s\le k\) and two messages \(m_+,m_-\). Arthur samples \(r_+,r_-\), and accepts iff

\[
V(n,s,r_+,m_+)=1
\quad\text{and}\quad
V(n,s-1,r_-,m_-)=0.
\]

- If \(k\ge S(n)\), Merlin takes \(s=S(n)\). Perfect completeness gives an accepting witness at \(s\); soundness says that at \(s-1\) almost every \(r_-\) has **no** accepting message, so Arthur accepts with high probability.
- If \(k<S(n)\), every \(s\le k\) is a no-instance; soundness at \(s\) makes Arthur reject with high probability.

This is a valid AM protocol of the same round complexity, but it is **circular** as a route to NP: the check “\(s-1\notin L\)” is a universal no-witness condition, i.e. coAM-like. Flipping the original AM protocol does not certify the complement: Merlin may choose a bad strategy on a yes-instance, and AM is not known closed under complement. Recursively replacing the \(s-1\) check by another boundary protocol descends one threshold at a time and produces only a polynomial-round IP/PSPACE protocol, not constant-round AM.

This is the concrete obstruction behind the front’s intuition: the difficulty is not the number of minimax alternations inside the game; it is the **one-sidedness of the threshold boundary**.

## 4. Barriers

`[deduction]` A proof of `SORT-BOUND-U` \(\notin \mathrm{AM}\) would imply

\[
\mathrm{PSPACE}\ne \mathrm{AM},
\]

because the language is in PSPACE. That is a major open separation, since \(\mathrm{AM}\subseteq \Pi_2^{\mathrm P}\).

`[deduction]` No relativizing proof of `SORT-BOUND-U` \(\notin \mathrm{AM}\) can work. For any language \(L\), the oracle \(O=L\) makes \(L\in \mathrm P^O\subseteq \mathrm{AM}^O\). A relativizing proof of \(L\notin\mathrm{AM}\) would also show \(L\notin\mathrm{AM}^O\) for every \(O\), a contradiction. Thus any lower-bound proof must be non-relativizing.

`[deduction]` The existing DAG/frontier/potential results are **soundness** results: they check a proposed lower bound, prune safely, or count reachable winning states. They do **not** supply a **complete** succinct certificate for all \(n\). The winning-frontier theorem rules out methods that must enumerate all winning states at a common depth; an AM message could in principle be selective and need not enumerate that frontier, so the frontier barrier is not an AM lower bound.

## 5. Honest limits

- No explicit AM protocol was found, even for the hard window between the information bound \(C(n)=\lceil\log_2 n!\rceil\) and a known constructive upper bound such as Ford–Johnson or merge sort.
- No proof was found that every constant-round protocol fails. Such a proof would be a non-relativizing separation of `SORT-BOUND-U` from AM and would imply \(\mathrm{PSPACE}\ne\mathrm{AM}\).
- General-poset hardness and finite computation through \(n=22\) do not decide the question.
- The most defensible new statement is the boundary-advice/self-reduction obstruction above: AM membership gives nonuniform boundary advice and a circular boundary protocol; the missing ingredient is a sound, uniform way to verify the no-side of the cutoff.

## Output 747 (msg_1bab6a700001qSrJ7QHs91KiqE)

## Recovery audit

I inspected the conversation history, working tree, Git state, board digest, and the durable frontier ledger before doing anything.

**Effects actually present:**

- Git: clean worktree at `6a96398` on `billy-dev`; no commits, branches, stashes, or file changes from this front.
- Repository: no Lean, docs, scripts, tests, or note files were created or modified.
- Board #301: the recent digest contains no AM/interactive-proof post from this front. No duplicate post was made.
- Durable ledger: the front `constant-round-am-sortbound` exists with agent `gnEHOwyyDXDdZwRhMcdPYI-struggles`, status `running`, and an **empty** `finding_unverified`. That is the only unfinished bookkeeping item. I did not edit the ledger manually, because it is keeper-owned and a concurrent write could corrupt or duplicate state.

No external action was repeated. I did not re-run the research prompt or post to the board.

## Mathematical status (carry-forward)

- No \(O(1)\)-round AM protocol was found for `SORT-BOUND-U`.
- No proof was found that every constant-round protocol fails.
- The useful exact obstruction is the **boundary-advice/self-reduction** result: AM membership gives, for each \(n\), a nonuniform polynomial-size advice string \(r_n\) that determines the entire cutoff \(S(n)\). The missing step to NP is finding/verifying that advice uniformly — not compressing the minimax game’s alternations.
- The natural boundary protocol is circular: verifying \(s=S(n)\) requires checking that \(s-1\notin L\), a universal no-witness/coAM-like condition. Flipping the AM protocol does not certify the complement.
- A lower bound \( \text{SORT-BOUND-U}\notin\mathrm{AM}\) would imply \(\mathrm{PSPACE}\ne\mathrm{AM}\), and it cannot be proved by relativizing methods (the oracle \(O=L\) makes \(L\in\mathrm P^O\subseteq\mathrm{AM}^O\)).
- General-poset hardness and the existing winning-frontier/DAG results do not transfer to the fixed antichain AM question; the frontier barrier concerns enumeration and does not establish AM non-membership.

**Recommended next action:** let the keeper record this run’s finding from the agent output, or flag the ledger entry for review. No further mathematical work or repository action is warranted from this turn.
