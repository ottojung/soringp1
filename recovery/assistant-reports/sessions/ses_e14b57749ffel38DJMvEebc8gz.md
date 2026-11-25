# antonina-FUEVJ6u2vJpQe5KL5HGCxM-selected

Session: ses_e14b57749ffel38DJMvEebc8gz
Workspace: /home/lubko/soring301-exec-n12-polytime-potential-adversary-20261117g
Created: 1794948892879; updated: 1794949031871

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 82 (msg_1eb4c751b001tZVNl8I5RCQiv1)

Created `exec-report.md` in this worktree with the requested analysis for front `n12-polytime-potential-adversary`.

**Contents include:**
- **Scope/model/baseline:** fixed adaptive comparison model, `C(12)=29`, `S(12)=30` (literature), arithmetic slack `2^29/12!≈1.120812` (experiment), and relevant barriers (no `#P` extension counting, non-scalar/strategic obstruction, prior front findings) with claim labels.
- **Precise potential class `C_polycd`:** poly-time computable `Φ(P,d)` from standard poset/comparability-graph and chain-decomposition data, explicit no-`e(P)`/#P-enumeration constraint, and formalized front conditions (I) initializable at `(A_12,29)`, (M) adversary-maintainable for every sorter comparison, (S) certifies `>=2` unresolved outcomes at depth 29.
- **Explicit Φ candidates in `C_polycd`:** `Φ_A` (width/chain-count residual), `Φ_B` (incomparability budget), `Φ_C` (chain-decomposition profile), `Φ_D` (TC-balance/one-ply proxy), each with poly-time checkability, maintenance/soundness analysis, and falsifiers/counterstrategy considerations.
- **Formal impossibility/falsifier for a precise subclass:** defined `C_invstat ⊂ C_polycd` (potentials depending only on fixed poly-time invariant tuple `Inv(P)=(n,w(P),h(P),m(P),π↓(P))`) and gave a deduction-level barrier argument that this subclass cannot satisfy (I),(M),(S) as a sound general deficit certificate (coarseness vs strategic n=12 obstruction, maintenance-soundness tension, tight-case consistency), while explicitly noting this is not a machine-checked metatheorem and not an impossibility proof for all `C_polycd`.
- **Small-n evidence/counterstrategy:** tight controls (`S(5)=7`, `S(10)=22`, `S(11)=26`), local-global separation/non-monotonicity facts from docs, n=12 numeric slack, and sorter balanced-proxy counterstrategy schema against proxy potentials.
- **Claim ledger/types:** literature, deduction, experiment, and conjectural/negative conclusions labeled throughout.
- **Obstacles and next decisive question:** expressiveness/soundness/maintenance/tight-vs-non-tight gaps, and a concrete next falsifiable step—existence (or a stronger subclass no-go) for `Φ∈C_polycd \ C_invstat` with a provable reply lemma and n=12-specific soundness lemma checkable without extension counting (e.g. via symmetry-reduced/quotiented finite verification path).
