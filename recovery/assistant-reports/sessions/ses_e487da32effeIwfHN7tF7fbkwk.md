# antonina-qrF4uFxDLfPHd0xgYEk3TA-simon

Session: ses_e487da32effeIwfHN7tF7fbkwk
Workspace: /home/lubko/soring-fronts/exec-core-extension-induction-20261107
Created: 1794080136503; updated: 1794080978175

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 27 (msg_1b782790e001sHgxQBvC0GlMte)

**Unresolved.** I have neither a proof nor a counterexample to the universal-element lemma. I can’t honestly supply the smallest counterexample or an exact extension count without one.

The deletion induction has a specific obstruction. Let \(x\) be maximal and \(Q=P-x\). Then
\[
e(P)=\sum_{L\in\mathrm{LE}(Q)}\bigl|\{\,\text{positions to insert }x\text{ into }L\text{ while preserving }P\,\}\bigr|.
\]
If \(Q\) has no universal element, an inductive bound on \(e(Q)\) might help, but it does not by itself control how many valid insertion positions there are. If **every** maximal deletion acquires a universal element, that induction supplies no core subproblem at all; I do not have a separate argument covering this case. The prior checked enumeration and the stated 392 deletion failures do not resolve either gap.

I did not verify a relevant literature source, and the web search was unavailable, so I have no citations to offer. The genuine missing step is a lower bound on the total valid insertion positions (or another argument covering the all-deletions-acquire-a-universal case), or an explicit counterexample.

## Output 245 (msg_1b78b1fba001NqRyRSaEEuMU7w)

## Recovery status (checked first; nothing repeated)

- This worktree is clean at `c865b23`; `git status --porcelain` is empty, the reflog has only the worktree checkout entry, and there are no new commits, stashes, or untracked files.
- The previous turn in this session performed two file reads and one web-search attempt (cancelled), then wrote the unresolved answer. It made no shell writes, no commit, and no board post.
- The board entry at 19:03 referring to this topic is a **Viche Recovery Steward** reconciliation of a different agent (`drz5…-groan`) in `exec-merge-tree-rounding-gap`, posted before this session’s worktree existed. It is not an effect of this session.
- I therefore continued only the mathematical work below. No repo or board action was taken.

---

## Result: the lemma is true

**Theorem.** Let \(P\) be a finite poset with \(|P|\ge 2\). If no element of \(P\) is comparable with every other element, then
\[
e(P)\ge |P|,
\]
where \(e(P)\) is the number of linear extensions.

The proof is self-contained. I did not verify a published source for this exact statement, so I cite none.

### Notation

- \(x\parallel y\) means \(x,y\) are incomparable.
- \(P-x\) is the induced subposet on \(P\setminus\{x\}\).
- \(\operatorname{Inc}(x)=\{y\in P:y\parallel x\}\).

### Lemma 1 (strict gain from deleting a non-universal element)

If \(x\in P\) is not universal, then
\[
e(P)\ge e(P-x)+1.
\]

**Proof.** Put \(Q=P-x\), and define
\[
D=\{d\in Q:d<x\},\qquad A=\{a\in Q:x<a\}.
\]
Choose \(u\in Q\) with \(u\parallel x\).

Since \(u\parallel x\):

- no \(d\in D\) satisfies \(u<d\), because \(u<d<x\) would give \(u<x\);
- no \(a\in A\) satisfies \(a<u\), because \(x<a<u\) would give \(x<u\);
- every \(d\in D\) is below every \(a\in A\), since \(d<x<a\).

Hence the relations of \(Q\), together with \(d<u\) for all \(d\in D\) and \(u<a\) for all \(a\in A\), are consistent. (A new cycle would require a \(Q\)-path \(u\to D\), an \(A\to u\), or an \(A\to D\); none exists.) Extend to a linear extension \(L\) of \(Q\).

Inserting \(x\) immediately before \(u\), or immediately after \(u\), gives two distinct linear extensions of \(P\): in both cases \(x\) is after all of \(D\) and before all of \(A\).

Conversely, for every linear extension \(M\) of \(Q\), all elements of \(D\) precede all elements of \(A\), so there is at least one slot in which \(x\) can be inserted between the last element of \(D\) and the first element of \(A\). Distinct \(M\) give distinct extensions of \(P\).

Therefore the extension \(L\) has at least two preimages under restriction, and every other extension of \(Q\) has at least one:
\[
e(P)\ge e(Q)+1.
\]
\(\square\)

### Lemma 2 (when every single deletion creates a universal element)

Suppose \(P\) has no universal element, and for **every** \(x\in P\), the poset \(P-x\) has a universal element. Then:

1. every element of \(P\) has exactly one incomparable partner;
2. \(P\) is a chain of \(|P|/2\) two-element antichain blocks;
3. \(e(P)=2^{|P|/2}\ge |P|\).

**Proof.** For each \(x\), choose \(u_x\) universal in \(P-x\). Since \(P\) has no universal element, \(u_x\) is not universal in \(P\), hence \(u_x\parallel x\). But \(u_x\) is comparable with every element of \(P-x\), so
\[
\operatorname{Inc}(u_x)=\{x\}.
\]
The map \(x\mapsto u_x\) is injective: if \(u_x=u_y\), then \(\{x\}=\operatorname{Inc}(u_x)=\operatorname{Inc}(u_y)=\{y\}\), so \(x=y\). Since \(P\) is finite, this map is a bijection. Thus every element \(z\) equals \(u_x\) for a unique \(x\), and therefore
\[
\operatorname{Inc}(z)=\{x\}.
\]
So every element has exactly one incomparable partner. The partner map is a fixed-point-free involution, partitioning \(P\) into pairs \(\{z,z'\}\) with \(z\parallel z'\).

Elements from different pairs are comparable. If \(\{z,z'\}\) and \(\{w,w'\}\) are two such pairs and \(z<w\), then transitivity forces
\[
z'<w,\qquad z<w',\qquad z'<w';
\]
otherwise \(z<z'\) or \(w'<w\), contradiction. Hence the pairs are totally ordered as blocks.

Therefore a linear extension of \(P\) is obtained by ordering the blocks in their forced chain order and choosing one of the two internal orders in each block:
\[
e(P)=2^{|P|/2}.
\]
Writing \(p=|P|/2\), we have \(2^p\ge 2p=|P|\) for every \(p\ge1\). \(\square\)

### Proof of the theorem

Induct on \(n=|P|\).

**Base \(n=2\).** If the two elements were comparable, each would be universal; hence they are incomparable, and \(e(P)=2!=2=n\).

**Inductive step \(n\ge3\).** Assume \(P\) has no universal element.

- **Case A: some \(x\in P\) has \(P-x\) universal-free.**  
  Since \(P\) has no universal element, \(x\) is non-universal. By Lemma 1,
  \[
  e(P)\ge e(P-x)+1.
  \]
  The poset \(P-x\) has \(n-1\ge2\) elements and no universal element, so the induction hypothesis gives
  \[
  e(P-x)\ge n-1.
  \]
  Hence \(e(P)\ge n\).

- **Case B: every \(P-x\) has a universal element.**  
  Lemma 2 applies directly and gives
  \[
  e(P)=2^{n/2}\ge n.
  \]

This covers all possibilities. \(\square\)

### The maximal-deletion case

The proof does **not** require a maximal deletion to leave a core poset. The dichotomy is over all elements:

- If **some** deletion \(P-x\), maximal or not, is universal-free, then Case A applies and the single strict gain of Lemma 1 closes the induction.
- If **every** deletion, maximal or not, acquires a universal element, then Case B applies. In that case the maximal elements are exactly the upper elements of the top paired block; deleting any maximal element leaves its partner universal in the remainder, so the condition “every maximal deletion acquires a universal element” is automatic. The global count \(e(P)=2^{n/2}\) then finishes the argument.

Thus the 392 cases in which a maximal deletion fails to remain core are not counterexamples to the strategy: they simply force one into Case B unless another deletion is core-preserving.

### Equality examples

- \(C_{n-1}\sqcup\{\text{isolated point}\}\) has \(e(P)=n\) and no universal element; it is handled by Case A.
- The two-element antichain has \(e=2=n\).
- The poset consisting of two incomparable pairs \(\{a,a'\}\) below two incomparable pairs \(\{b,b'\}\), with all cross relations \(a,a'<b,b'\), has \(n=4\), \(e=4\), and no universal element; it is the \(p=2\) Case B equality.

## Output 257 (msg_1b78eac2c001hS8mZL6JNsJ8EF)

Recovery check: I’ll verify the worktree and durable session/board records for effects from the previous answer. I won’t redo the proof or post anything unless inspection shows that work is unfinished.

## Output 293 (msg_1b78ee15f001s3QuDuhM9GOpiF)

I’ll first check whether the referee analysis already completed in a durable agent/session record, then verify repository and board state. I won’t relaunch the literature review or make any external changes.

## Output 324 (msg_1b78f2253001XV5urC6Kb9cRoH)

The previous referee response completed and is preserved in the session record. It gave a self-contained proof of the core lemma; no repo edits or board post were made. The worktree is clean at `c865b23`.

The subsequent independent referee request is **not yet complete**: its agent session is still marked running, and the recorded activity ends during recovery checks, before a line-by-line audit or answer. The only board match is the older 19:03 reconciliation; no post from this referee session appears. I have not repeated the audit or taken external action.
