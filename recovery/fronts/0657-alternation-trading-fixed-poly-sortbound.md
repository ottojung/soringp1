# alternation-trading-fixed-poly-sortbound

## status

investigated

## origin

ai_proposal_unverified

## agent_id

0jKofSEh8iy2lleieXApTR-loyalists

## exit_state

clearexit

## question

Can the alternation-trading method — simulating alternating computation by deterministic time with a fixed, smaller alternation budget — yield an unconditional fixed-polynomial lower bound SORT-BOUND-U not in DTIME(N^c) for some specific constant c>1 on unary input length N=n+k+1, or does the tally/sparse form of the language together with the absence of any class-completeness handle make alternation trading inherently incapable of yielding information about this single fixed language?

## basis

AGENTS.md lists fixed-polynomial lower bounds such as SORT-BOUND-U not in DTIME(N^2) as not blocked by any open separation but with no known technique; board #301 at 20:14Z and 20:23Z closed numeric and representation-theoretic lower-bound families while leaving complexity lower bounds open; a keyword census of the 656-front ledger returns zero occurrences of 'alternation trading', while the generic fixed-poly and PSPACE-completeness fronts were already settled by sparsity.

## falsifier

Either exhibit a correct alternation-trading argument establishing SORT-BOUND-U not in DTIME(N^c) for a fixed c with full encoding fidelity, or prove that the method must fail here because every instance of it presupposes hardness or completeness for a class, which the sparsity of this tally language rules out for all-n reductions.

## implication

A positive result would be the first unconditional time lower bound for a natural tally PSPACE language without proving P not equal to PSPACE, filling the 'no known technique' gap; a rigorous no-go would close the last lower-bound method family outside the numeric-value route after the 20:23Z Fourier barrier.

## finding_unverified

METHOD-SCOPE NO-GO (no theorem completion). Alternation trading's established template (Williams CCC 2007; on CKS ATIME=PSPACE + time hierarchies) is a CLASS-INCLUSION method: assume L in DTIME(n^c), use L's <=_m^p-completeness for a class C to get C subseteq DTIME(n^{cr}), trade alternations for time, then contradict a hierarchy theorem. The completeness handle at the class-inclusion step is the only conversion of a single-language assumption into a class-wide statement, hence is necessary for the template. SORT-BOUND-U has no usable handle: (a) sparse <=_m^p NP-hard forces P=NP (Mahaney), so an NP handle is tied to an open collapse and cannot give an unconditional bound; (b) PSPACE handle is unconditionally false by this repo's sort-bound-u-pspace-complete sparse-hard collapse vs P strictly subset PSPACE; Turing-hardness gives only PSPACE subseteq P/poly; (c) no near-linear <=_m^p-completeness for any DTIME(n^a)/NTIME(n^a) is known (tally/sparse-hard obstructions). Encoding fidelity: SORT-BOUND-U in DTIME(N^c) <=> S(n) in poly(n) (binary search on k, N <= n^2+n+1), so the question is exactly the numeric-value route. Falsification attempts (minimax ATM, self-reduction in k, Turing handle, insertion recurrences) all failed to yield a positive result. HONEST LIMITS: barrier about an informal proof family, not a theorem over all proofs; did NOT prove SORT-BOUND-U in/out of DTIME(N^c); S(n) time complexity stays open; PSPACE case relies on repo's established sparse-hard collapse. No repo/Lean/CI changes; scratch only (/tmp/opencode/alternation_trading_no_go.md). Posted once to board #301 at 2026-11-21T21:01:19.716Z.

## Other metadata

```json
{
  "finished_at": 1795294904.613384,
  "started_at": 1795294120.9664772
}
```
