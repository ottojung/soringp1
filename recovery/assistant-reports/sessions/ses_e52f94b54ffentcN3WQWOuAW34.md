# antonina-AjTDIXAythbQVR6tBzL3Q2-dusted

Session: ses_e52f94b54ffentcN3WQWOuAW34
Workspace: /home/lubko/soring301
Created: 1793904260274; updated: 1793904296576

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1ad06b4cc0013NO5UNIU2z0UC0)

I’ll keep this read-only and focus on a single concrete syntax/interpreter. I’ll first check the assigned issue’s context and the model notes so the construction doesn’t repeat the fixed-\(m\) audit.

## Output 41 (msg_1ad06dff9001WlYud1YHSJimBm)

## Result: a polynomial-time interpreter is possible, but only with an explicit execution cap

Here is one concrete syntax meeting the operational restriction. It gives a **verified construction**, not an all-\(n\) completeness result.

**Model.** Encode a program as a finite binary description of a deterministic, single-tape instruction machine. Its instructions may read and write its own tape, move its head, branch on tape symbols, and inspect the public parameters \(n,k\). A designated instruction requests a comparison of two indices \(i,j\in\{1,\ldots,n\}\); the oracle returns their relative order, which the machine may use in subsequent computation. The machine cannot inspect keys or the hidden permutation in any other way. It may halt with a proposed permutation of \(\{1,\ldots,n\}\).

For description length \(L\), set a fixed fuel limit \(F=(L+n+k+2)^2\). A fixed interpreter simulates at most \(F\) instructions, rejects malformed descriptions, out-of-range queries, and executions that exceed fuel, and otherwise returns the machine’s output. Encode \(n,k\) in unary in the input and indices and tape symbols in binary. A configuration has polynomial size in \(L+n+k\): the simulated tape can have at most \(F\) visited cells, and head position, state, counters, and output are polynomially bounded. Straightforward universal simulation therefore takes polynomial combined time in \(L+n+k\), including parsing, configuration updates, and oracle interactions. The number of oracle queries is at most \(F\); **the interpreter’s time bound counts all execution work, not just comparisons**.

The cap is essential. An unrestricted machine description can run for superpolynomially many steps before halting, so a universal interpreter cannot promise polynomial combined running time for unrestricted programs. The cap makes the runtime theorem true by construction; it does not establish that arbitrary FO(TC) programs have short executions or that the cap preserves every strategy of interest.

**Examples.** Ordinary insertion sort and balanced merge sort have polynomial-size machine descriptions under this syntax. Their ordinary comparison implementations run within the fuel bound for sufficiently large inputs, with a fixed constant-factor adjustment to the fuel polynomial if needed. Insertion sort has worst-case query count \(n(n-1)/2\); balanced merge sort has its usual worst-case merge-comparison count, at most \(n\lceil\log_2 n\rceil\) up to the standard additive/tightening details for the chosen implementation. These are counts of oracle queries, not of interpreter steps. The programs compute a sorted permutation on every distinct-key input. Small-\(n\) behavior and exact merge-sort counts depend on the specified implementation, not on the interpreter theorem.

This proves only that a **fuel-bounded encoded machine syntax** has a fixed polynomial-time interpreter and can express these two standard sorts. It does not prove that every strategy needed to witness \(S(n)\) has a polynomial-size description that runs within polynomial fuel, nor that the optimal worst-case query bound is polynomial-time checkable from such a description.

### Missing completeness theorem

To derive a complexity-class membership for `SORT-BOUND-U`, one still needs a sound, complete, polynomial-size certificate theorem: for every \(n,k\), \(S(n)\le k\) must hold exactly when there is a polynomially bounded certificate whose checker verifies a strategy sorting **all** input permutations with at most \(k\) queries on every run. In particular, one must prove the relevant uniform succinctness/completeness bound for strategies, not just simulate a supplied program efficiently. A mere FO(TC) formula or fixed-formula data-complexity bound does not supply that theorem: it concerns evaluation of a fixed description on an instance, not the size of descriptions needed across all \(n\), nor the universal worst-case correctness and query-depth verification required at the antichain root.

**Next experiment:** implement the exact encoding and fuelled interpreter, then run encoded insertion and merge sort across increasing \(n\), recording description size, total simulated steps, maximum visited tape, and worst-case oracle-query counts. This can validate the bookkeeping and catch encoding overhead errors; it cannot establish the missing all-\(n\) completeness theorem.

**Evidence status:** the construction and bounds above are direct model-level deductions, not claims from a verified primary source. No finite-model/computation source was consulted for this construction; source-backed FO(TC) claims are intentionally not made.
