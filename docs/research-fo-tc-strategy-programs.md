# FO(TC) strategy programs for exact optimal sorting

**Status:** research note (model, soundness/cost accounting, examples, barriers). Coordinates with umbrella Antonina #301 and issue #47 (forgetful framed-DAG certificates). **Not Lean-checked.**

## 1) Model: syntax, semantics, cost accounting

### Syntax (abstract)
A strategy program $p$ is a finite structure over a fixed vocabulary that maintains **mutable knowledge state** $K$ (a partial order on keys $[n]$ encoded relationally: e.g. relations $<^K, \mathit{incomparable}$, and their TC/closures). Rules are guarded by formulas (first-order, possibly with transitive closure over $K$ and auxiliary relations):
- **Query rule**: guard selects an incomparable pair $(i,j)$ (not yet ordered) to compare next; on outcome adds $(i<j)$ or $(j<i)$ to $K$ (closure update) and branches.
- **Output rule**: guard fires when $K$ is a total order, producing permutation $\pi$.
- **Halt/fail**: only allowed if total and correct.

The program has no direct access to input order $X$ (unknown total order); comparisons are oracle queries $\mathsf{cmp}(i,j;X)$ returning the relation in $X$.

### Semantics
$\mathsf{Run}(p,X)$: initialize $K=\emptyset$; while not output: apply enabled rule (deterministic) — if query, call oracle with $(i,j)$, update $K := \mathit{cl}(K \cup \{outcome\})$ (cost +1), branch; if output, return $\pi$. 
**Correctness:** $\forall$ total $X$, $\mathsf{Run}(p,X)$ outputs the total order of $X$ and terminates. 
**Worst-case cost:** $k(p)=\max_{X} (\text{\#comparisons})$.

### Cost accounting
- **Program size** $|p|$: number of rules/symbols (description length). For polynomial-size certificates we want $|p| = \mathrm{poly}(n+k)$.
- **Per-step cost**: oracle queries charged 1; rule evaluation/updates charged according to interpreter.
- **Uniform polynomial interpreter** $\mathsf{IP}$: takes $(p, n, X)$ (or access to $X$ via oracle) and executes $\mathsf{Run}(p,X)$. 
- **Combined complexity warning**: FO(TC) has NL **data complexity** for fixed formulas, but evaluating a **growing program text** $p$ (growing with $n,k$) is a **combined complexity** question. Data-complexity NL does not automatically give a uniform polynomial bound over all $p$ of size $\mathrm{poly}(n)$. We require either (a) a bounded-variable/arity fragment with explicit combined bounds, or (b) a fixed interpreter with a proved uniform polynomial-time bound in $|p|,n$.

## 2) Soundness, verification, complexity class placement

**[deduction] Soundness:** If $p$ is correct with budget $k$ for all $X$ on $[n]$, then $S(n) \le k(p) \le k$.

**[deduction] Verification (universal):** Given $p,n,k$, question $V(p,n,k): \forall$ total orders $X \in S_n,\, \mathsf{Run}(p,X)$ sorts with $\le k$ comparisons. 
This is a $\forall X\, \exists^?$ (tree of fixed shape given $p$, but $X$ adversarial) — more directly a $\forall$ over $n!$ inputs with a polynomial-time (uniform, if bounded) execution: $V \in \mathrm{coNP}$ in general if $n!$ large? Or in $\Pi_2^P$? Better: $V(p,n,k) \iff \neg \exists X\, (\mathsf{Run}(p,X)\,\text{wrong or uses}>k)$. If $\mathsf{IP}$ is uniform polytime, $\exists X$ of that bad behavior is in NP (guess $X$ / comparison outcomes path consistent with some $X$) so $V \in \mathrm{coNP}$. But combined with existential choice of $p$: $SORT\text{-}BOUND\text{-}U = \{\langle 1^n,1^k\rangle : \exists p\, (|p|\le \mathrm{poly}(n,k) \land V(p,n,k))\} \subseteq \exists \mathrm{poly}\,\forall^{\mathrm{poly}}$? Wait — $V \in \mathrm{coNP}$ relative to fixed $p$, so $\exists p\in\mathrm{poly}\, V(p,\ldots) \in \Sigma_2^P$ **provided** the interpreter is uniform polynomial-time and $p$ is poly-sized guess. Writing FO(TC) formulas alone doesn't guarantee uniform polynomial interpreter for growing texts; this is the "combined evaluation" gap.

**Key point (task 6):** Keep existential program choice separate from universal adversarial outcomes. The $\Sigma_2^P$ upper bound is *conditional* on a uniform polynomial interpreter, not automatic from "FO(TC) source code".

## 3) Elementary examples (task 3)

### Insertion sort (program sketch)
Maintain sorted prefix $S_m \subset [n]$ as a chain $K_m$. For each new element $x$, do binary search over $S_m$ using pairwise comparisons $(y,x)$: each comparison adds order to $K$, branch, until position found; insert $x$ (update $K$ to include all relations). Worst-case comparisons $\sum_{i=1}^{n} \lceil \log_2 i \rceil$ (and up to $n(n-1)/2$ naive), program size $O(n \log n)$ in description if parameterized, or $O(1)$ schema with size parameterized by $n$? Or treat $n$ as fixed in program for fixed instance class - but need poly(n+k) in terms of $n$. Alternatively a uniform schema program that reads $n$ (from input encoding) and runs insertion sort: description length $O(1)$ (rules) but with parameters; size polynomial in $n$ if we count encoding. More carefully: for input $1^n\#1^k$, a uniform program $p_n$ of size $\mathrm{poly}(n)$ can implement insertion sort.

### Merge sort
Divide-and-conquer over subsets; needs to merge two sorted lists by pairwise comparisons with knowledge of subset orders. State must track partial orders of subsets being merged. Program size grows with recursion structure - still polynomial in $n$ (schema) or explicit tree small.

### Optimal small sorters (n<=6)
For fixed $n$, optimal decision tree has height $S(n)$; can be encoded as a program that branches on comparison outcomes to reach the optimal tree structure? But storing the full tree: single-policy DAG is tree with $2n! - 1$ nodes for $n\ge2$ (observation from research-strategy-certificates) - exponential in $n$. A program that **enumerates/searches for optimal tree at runtime** is bad (task says "A short program that first exhaustively searches for the optimal tree does NOT satisfy the runtime condition"). So we must have a **compact description** (rules/schema) giving the strategy, not a table of the exponential tree.

This is the compression point: can the *strategy* be described compactly by rules (FO(TC) over state) even if the decision tree is large?

## 4) All-n conjecture, barriers (tasks 4,5)

**[conjecture, falsifiable]** (all-n exact-completeness): For every $n$, there is a strategy program $p_n$ with $|p_n| = \mathrm{poly}(n + S(n))$ and uniform polynomial interpreter runtime $\mathrm{poly}(n)$ per execution such that $p_n$ is an optimal $S(n)$-comparison sorter.

**Barriers found:**
- **Split-schema barrier** (proved): sorting a fixed $m$-subset first then completing gives lower bound $S(m)+C(m,n) \ge S(m)+\lceil \log_2(n!/m!) \rceil$; phase coupling makes counting bound unachievable in many cells where it looked exact (e.g. $(4,6),(3,6),(4,7),(6,9)$ miss; $(5,8)$ exact). Fixed split points are insufficient for all $n$.
- **Tree size**: optimal strategies may have exponentially large decision trees; explicit storage impossible if poly-sized program required.
- **Runtime constraint**: cannot search for optimal tree at runtime.
- **Forgetful framed DAGs** (issue #47): question of whether logical programs can simulate forgetful framed DAGs efficiently with compression beyond explicit DAGs. Need to examine.

**Relation to framed DAGs:** A forgetful framed DAG may identify states differently than full poset-isomorphism; a rule-based program can compute/store state by formulas (FO(TC)) over relations - potentially more flexible than explicit node identity? Or maybe can implement forgetful joins? Simulation overhead needs analysis.

## 5) Concrete next experiments
1. Define a minimal concrete rule language (IR) for strategy programs; write interpreter skeleton with explicit cost counting.
2. Encode insertion sort and merge sort as IR programs, measure $|p|$.
3. Try to encode a known compact optimal strategy for some $n$ (if exists) vs tree; see if rules compress.
4. Extend split-schema to check more cells $(m,n)$ for fixed-$m$ families, look for pattern of exactness/failure.
5. Analyze combined evaluation complexity for the IR on growing $n$.
