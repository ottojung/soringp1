# antonina-AqnE5hcXfa61MFisdqglvF-glycogen

Session: ses_e49e43dbeffem9DxJT2pXQB7fz
Workspace: /home/lubko/soring-fronts/exec-fotc-frame-store-independent-audit-20261107
Created: 1794056635015; updated: 1794056671152

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1b61bc4a3001cpBcVSEzuaIC2N)

I’ll inspect the candidate, the cited original draft, and checker as separate sources, then trace the formal encoding/runtime assumptions and report only an audit—no edits or posts.

## Output 23 (msg_1b61bd629001cueKsYGK1Yjkla)

**Verdict: not valid as written.** The central framed-store invariant and old-slot-to-new-slot direction are correct, and the checker supports soundness on reachable paths. But the candidate’s displayed formulas do **not** all satisfy the draft’s one-global-variable-set condition, its “fixed interpreter extension” is a proposal rather than an already specified machine, and the `n=0` leaf/output case is underspecified. These are repairable for a conditional compiler lemma; they do not establish polynomial-size exact-optimal certificates.

## Specific findings

1. **Global variable bound: fails for the displayed actions.**  
   The draft defines `FO(TC)_v` with one globally fixed set of at most `v` variable names, including local bound variables (original draft lines 21–36). Candidate lines 27–29 use `r,a,b,s`; lines 34–35 use `r,o,e,t`; and lines 42–43 use `r,p,x,y`, each using four names. But `Goto`’s update at lines 37–39 additionally binds `x` while retaining `e,w,y`. It therefore requires five names `{e,w,y,x}` only if disjoint from the rule’s names—and the action-selection rule already uses `r,o,e,t`. More importantly, the candidate does not specify how that update formula belongs to the **same globally fixed** rule syntax: under the natural reading that the action body and its operational update are one formula, the update needs names beyond the four-name selection formula. The candidate’s claim at line 39 that the update itself uses four names does not establish compliance of the whole query-program rule.  
   **Repair:** define updates as fixed interpreter primitives whose semantics are not FO formulas, and make clear that the only FO formulas are the four-variable action selectors. Alternatively give a complete rule syntax and demonstrate every formula—including any formula evaluated by the interpreter—fits one fixed set of four names.

2. **`AskSlot` is explicit but not part of the original model.**  
   Original draft lines 42–55 specifies `Ask(i,j)` on original labels, with the interpreter, store updates, and charged query. Candidate lines 3, 9, 25, and 31 correctly acknowledge a new extension, and line 31 describes one oracle call after reading `M`. That can be a legitimate *proposed* fixed interpreter primitive, but the cited draft does not define it, nor does the candidate fully specify a bytecode/program representation, behavior on invalid/non-bijective `M`, or the cost/clock semantics of its atomic read–query–write transition. Calling this “explicit” does not by itself make it an existing fixed interpreter.  
   **Repair:** state the extended interpreter’s fixed transition rules, invalid-state rejection behavior, and implementation cost. Ensure the only hidden-order access is exactly one charged query per `AskSlot`; all table/store work is ordinary deterministic computation.

3. **`Goto` direction: correct.**  
   Checker `_rename` at checker lines 32–40 maps each old relation fact `(i,j)` to `(perm[i],perm[j])`: old slot to new slot. Candidate lines 37–39 implement `M'(w,y) iff Perm(e,x,w) AND M(x,y)`. Thus the label formerly in old slot `x` is placed in new slot `w=perm(x)`, giving `rho_new(w)=rho_old(x)` and `rho_new=rho_old∘perm⁻¹` (candidate lines 49–53). This is the correct inverse-coordinate update for slot-to-original-label contents.

4. **Checker soundness: sound on actually reachable paths, including joins and impossible edges.**  
   The checker topologically processes all nodes, starts only at root 0 (lines 63–65), skips logically impossible outcomes (lines 96–100), and intersects incoming guaranteed relations at joins (lines 101–107). Inductively, each propagated relation is true of every actual run reaching that node; intersection is conservative. Forward edges are enforced (line 90). A node with no feasible incoming run has `relations[v] is None`, so its leaf is not required to sort (lines 72–78), which is sound because it is unreachable. The candidate’s line 55 account is therefore sound for reachable leaves.  
   Caveat: this establishes correctness of **the checker’s accepted certificates**, not that every mathematically valid framed strategy is accepted or that a certificate exists at exact `S(n)`.

5. **Leaf-order construction: polynomial, but `n=0` needs an explicit convention.**  
   For reachable leaves, the checker’s relation is a strict total order by its pairwise test (checker lines 72–78). A compiler can derive the unique increasing slot order in polynomial time from the explicit relation, and populate `LeafOrder` in `O(Cn)` tuples as claimed (candidate lines 21, 59). Unreachable leaves can safely have no rows.  
   However, for `n=0`, the empty relation is vacuously total, and the emitted order is empty. Candidate line 43’s “final sentinel” and line 21’s output-position setup do not specify how the machine reaches `Halt` when there are zero output positions.  
   **Repair:** define a sentinel/control convention that is initialized and permits immediate halt for `n=0`, without requiring an `Emit`.

6. **Polynomial resource claims: plausible with the stated fixed-polynomial qualification, not fully specified as a clock proof.**  
   For `C≤(n+k+2)^r` with fixed `r`, explicit tables of sizes polynomial in `n+C` are polynomial in `n+k`; `M,H` can be dense `O(n²)`, and a dense rewrite per `Goto` remains polynomial (candidate lines 59–61). The bounded run has at most `2C+n+1` actions as claimed. This is compatible with one fixed ordinary-TM clock exponent chosen for the fixed certificate polynomial and interpreter.  
   The original draft explicitly distinguishes table-operation bounds from ordinary-machine time and requires a fixed clock exponent (original draft lines 60–69, 81–89, 114–127). The candidate does not give a concrete encoding or account for all domain/table-index bit costs, and does not say how a fixed clock handles the certificate and polynomial-exponent constants. These are standard polynomial bookkeeping gaps, not evidence of an unbounded operation—provided `AskSlot` and `Goto` are implemented as fixed algorithms scanning explicit stores/tables, not unit-cost oracle updates.

## Precise conditional lemma after repair

Fix a certificate encoding and an extended deterministic interpreter with explicit finite tables, mutable `M,H` stores, and fixed `AskSlot`/`Goto` transitions. Suppose the checker accepts a framed DAG of bit length `C`, height at most `k`, all edge permutations are old-slot-to-new-slot bijections, and all reachable leaves have checked total orders. Then a compiler running in time polynomial in `n+C` can construct a program whose **only order-dependent operation** is one charged comparison per `AskSlot`, which follows the DAG on every input permutation, maintains the slot-to-original-label invariant through each frame update, and outputs the certified increasing order at a reachable leaf. Its comparisons are at most `k`; its actions and ordinary execution time are polynomial in `n+k` whenever `C` is bounded by a fixed polynomial in `n+k`. The `n=0` behavior and fixed clock/interpreter semantics must be specified as above.

This lemma concerns replaying **any supplied accepted framed DAG**. It neither proves that a polynomial-size accepted DAG exists at exact `S(n)` nor implies unrestricted NP or `Σ₂^P` membership. The candidate explicitly preserves those limits (lines 63–65); no inference to exact-optimal certificate completeness should be made.
