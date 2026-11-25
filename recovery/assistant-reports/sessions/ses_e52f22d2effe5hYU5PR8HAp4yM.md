# antonina-yJc3Gc75NR7WsrhujzRRvm-exalted

Session: ses_e52f22d2effe5hYU5PR8HAp4yM
Workspace: /home/lubko/soring-fronts/fo-tc-varying-block-program-20261105
Created: 1793904726948; updated: 1793904763872

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1ad0dd61f001dnJmuy7gcJGOiz)

I’ll treat this as a paper audit, not a repository task. I’ll first inspect the project’s model/encoding and the preceding result if it is present, then make the interpreter, fuel, and quantifier claims explicit and test the sorting bounds against one fixed polynomial.

## Output 41 (msg_1ad0e06c1001SUUzLwKKAvmRxg)

## Audit verdict

The **polynomial-runtime interpreter claim is salvageable**, but the stated fuel \(F=(L+n+k+2)^2\) does not, by itself, establish it. A universal interpreter’s overhead depends on the concrete machine encoding and simulation method; “standard sorts fit after a constant adjustment” needs an explicit bound. More importantly, runtime does not imply optimal-strategy completeness.

### A robust formulation

Use a fixed, self-delimiting encoding of deterministic multitape programs \(p\), with length \(L\), and a fixed universal deterministic **single-tape** interpreter. Its input encodes \(p\), \(1^n\), \(1^k\), and a permutation \(\pi\in S_n\). The interpreter simulates \(p\) on \((n,\pi)\), with comparisons supplied by an oracle answering which of two distinct labels precedes the other in \(\pi\).

Require the simulated program to halt with a purported output permutation. Reject if it fails to halt within the fuel, makes more than \(k\) oracle calls, queries a label against itself, or returns anything other than a permutation of \([n]\) in the correct \(\pi\)-order. The oracle-call counter must be separate from the interpreter’s fuel counter.

For a conventional universal simulation with fixed polynomial overhead, a defensible bound is
\[
F(L,n,k)=(L+n+k+2)^c
\]
for a **fixed sufficiently large integer \(c\)**, chosen to dominate the interpreter’s simulation overhead and the explicit verification work. The exact exponent is machine-model-dependent; it cannot be inferred from “single tape” alone. An alternative is to choose a fixed interpreter and write its proven overhead explicitly, then select \(c\) from that bound. Invalid outputs and exhausted fuel reject.

### Sorting witnesses fit one fixed polynomial

Let \(m=\lceil\log_2(n+1)\rceil\). A program can keep an array of at most \(n\) labels and implement either insertion sort or merge sort using oracle comparisons. With ordinary binary encodings and a straightforward multitape program:

- insertion sort uses at most \(n(n-1)/2\) queries and polynomial running time in \(n+\log(n+1)\);
- merge sort uses at most \(n\lceil\log_2 n\rceil\) queries (for \(n\ge2\)) and polynomial running time in \(n+\log(n+1)\).

Thus, for all \(k\) at least the corresponding comparison bound, a fixed program text and a sufficiently large **single fixed exponent** \(c\) make both algorithms fit \(F(L,n,k)\). This is uniform in \(n,k\); it does not require a per-input constant adjustment. But a polynomial fuel does **not** rescue a sorter whose query count exceeds \(k\): the query cap is an independent condition. For a witness to \(S(n)\le k\), only programs using at most \(k\) calls on every permutation count.

### Exact conditional statement

Define the language
\[
W=\{\,1^n\#1^k : \exists p,\ |p|\le q(n+k+1),\
\forall\pi\in S_n,\ \text{the capped, fuel-bounded interpreter accepts }(p,n,k,\pi)\,\},
\]
for a specified polynomial description-length bound \(q\) and the fixed polynomial fuel above.

Then \(W\subseteq\texttt{SORT-BOUND-U}\): an accepting program yields a correct sorting strategy using at most \(k\) comparisons on every permutation. Conversely, for each \(n,k\), membership in `SORT-BOUND-U` implies membership in \(W\) **only if** there is a polynomially bounded program (in the unary input length) that describes a sorting strategy of worst-case depth at most \(k\), and that program runs within the fixed interpreter fuel. That is an additional succinct-strategy hypothesis, not a consequence of the existence of a finite sorting tree.

In complexity terms, \(W\) has an \(\exists p\,\forall\pi\) bounded predicate with polynomial-size \(p,\pi\) and polynomial-time verification, hence \(W\in\Sigma^p_2\) (under the stated polynomial description bound). If the succinct-strategy completeness hypothesis holds for all unary inputs, then `SORT-BOUND-U` is in \(\Sigma^p_2\). **Without it**, the existential-program language is merely a sound sublanguage; this construction proves no corresponding upper bound for `SORT-BOUND-U`.

### Keep the three claims separate

1. **Interpreter/runtime:** fixed program text executes within a polynomial bound in its encoded input and fuel. This is an ordinary machine-simulation statement.
2. **All-\(n\) optimal-strategy completeness:** requires polynomial-size program descriptions for strategies achieving depth \(S(n)\). No such theorem follows from the interpreter, nor from the existence of an optimal finite tree; that tree can be exponentially large.
3. **FO(TC) fixed-formula data complexity:** a fixed FO(TC) formula is evaluated on a varying finite structure. This does not automatically express “there exists a polynomial-size program, and for every input permutation it sorts within \(k\) comparisons,” nor does it supply the missing succinct optimal-strategy theorem. A uniform interpreter encoding and its resource bound are not themselves a fixed-formula FO(TC) completeness result.

So the defect in the preceding claim is not that insertion/merge sort exceed every fixed polynomial fuel. They fit a suitable fixed polynomial. The gap is the unsubstantiated universal-simulation constant/exponent and, decisively, the missing query cap and the unjustified leap from polynomial interpreter runtime to completeness for all optimal sorting strategies.
