# antonina-V2OoIjlCB6hohn2zG251VL-paid

Session: ses_e15f33b36ffeS8UomgA6NUuM1Y
Workspace: /home/lubko/soring301-exec-opt-fib-split-alln-20261117c
Created: 1794928067859; updated: 1794928178230

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 92 (msg_1ea0e4f6f001ckqUV3S8DRnXLd)

Wrote `exec-report.md` in `/home/lubko/soring301-exec-opt-fib-split-alln-20261117c` (no other repo edits, no Lean, no PR/comments).

**Report covers (fresh tack, `optimal-fibonacci-split-alln`):**
- **Hypothesis (all $n$):** Ford–Johnson merge-insertion as the canonical Fibonacci/Jacobsthal-split strategy achieves/characterizes the optimum, i.e. $S(n)=F(n)=\sum_{i=1}^{n}\lceil \log_2(3i/4)\rceil$ for all $n$ (and the large-$n$ variant).
- **Analysis:** Cites in-repo/literature baselines (known exact $S(n)$ for $n\le 22$, FJ/Knuth, Wells/Peczarski, Stober–Weiß, Sergeev) and local exact computation showing $F(n)=S(n)$ for all $n\le 22$ but $F(n)-\lceil\log_2 n!\rceil$ grows ~linearly in sampled ranges.
- **Result/obstruction:** No finite counterexample on known values ($n\le 22$ consistent), but the all-$n$/large-$n$ equality is **asymptotically refuted/obstructed**: $S(n)=\log_2 n!+o(n)$ (Sergeev) while $F(n)=\log_2 n!+\Theta(n)$, hence $S(n)<F(n)$ for all sufficiently large $n$; Jacobsthal-split optimality in the FJ instantiation cannot extend to all large $n$. A Sergeev-compatible $o(n)$ Jacobsthal-like/control structure remains open (distinct question).
- **Consequence:** FJ gives a valid polynomial-time-computable upper bound but not an all-$n$ exact evaluator of $S(n)$ (so no implication for $S_{\mathrm{unary}}\in \mathrm{FP}$ / `SORT-BOUND-U ∈ P`); residual productive question is polynomial-state/$o(n)$-surplus realization, per `docs/research-framed-certificate-frontier.md`.
