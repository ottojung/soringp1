# fo-lfp-vs-sortbound-20261101

## status

investigated

## origin

ai_proposal_unverified

## agent_id

k1AYI7TgG5DtUlnFxfFDbb-spell

## exit_state

clearexit

## question

Does the uniform SORT-BOUND-U threshold admit an FO(LFP) (polynomial-time) definition on ordered structures, and if not what is the exact obstruction relative to known PSPACE bound? Distinguish descriptive complexity classes carefully against unary/binary encodings and against the special antichain case.

## basis

research-plan notes FO(LFP)(P) or ESO(NP) definition separate work; PSPACE known via alternation.

## falsifier

Show either a natural FO(LFP) formula fails for some n due to model/encoding mismatch, or that FO(LFP) definability would force SORT-BOUND-U in P which is not ruled out but requires a nontrivial correspondence argument not present; alternatively exhibit an obstruction showing FO(LFP) cannot capture the exact minimax (not just alternating Turing).

## implication

FO(LFP) definability would give a strong structural upper bound (P) for SORT-BOUND-U; showing obstruction gives a descriptive-complexity barrier relevant to uniform evaluation.

## finding_unverified

ction showing FO(LFP) cannot capture the exact minimax (not just alternating Turing).
> COMPLEXITY IMPLICATION: FO(LFP) definability would give a strong structural upper bound (P) for SORT-BOUND-U; showing obstruction gives a descriptive-complexity barrier relevant to uniform evaluation.
> EVIDENCE: research-plan notes FO(LFP)(P) or ESO(NP) definition separate work; PSPACE known via alternation.
> If resuming after an infrastructure failure, inspect earlier work and avoid repeating side effects or claims. 
> On completion report a mathematical finding, concrete failed approach or exact obstruction; do not confuse process success with a proof." 

So the falsifier says "FO(LFP) definability would force SORT-BOUND-U in P which is not ruled out but requires a nontrivial correspondence argument not present" - so they want to see if FO(LFP) definability is straightforward. Also "exhibit an obstruction showing FO(LFP) cannot capture the exact minimax (not just alternating Turing)". That suggests a barrier argument - like showing the state space structure makes it impossible for LFP to capture the exact minimax recurrence in the right way, without actually trying to prove P≠PSPACE by diagonalization. That fits the "barriers that rule out whole families of methods" frontier mentioned in AGENTS.md.

Let us think through this systematically.

**Mathematical finding (descriptive complexity / complexity of exact unary S(n)):**

Claim attacked: *"SORT-BOUND-U admits an FO(LFP) (polynomial-time) definition on ordered structures."*

- Input is ordered string $1^n\#1^k$ of size $N=n+k+1$; keys $X\subset D$, $|X|=n$. $S(n)\le k \iff$ sorter has a winning strategy in game $G(n,k)$ from antichain over posets on $X$ ($2^{\Theta(n^2)}$ states). Known $SORT\text{-}BOUND\text{-}U \in PSPACE$ matches $FO(PFP)$; $FO(LFP)$ would mean $PTIME$.
- **Exact obstruction:** Game states are posets $P$ (relations on $X$), not domain elements. There are exponentially many posets while $|D|=\Theta(n\log n)$ for informative instances. $FO(LFP)$ has no unrestricted $SO\exists$ over strategies/relations and converges in $poly(|D|)$ iterations over fixed-arity relations on $D$ — cannot enumerate/index the exponential poset state space. Unlike AND-OR reachability (states = vertices/domain elements), the minimax ranges over all poset states; the $ATM/PSPACE$ solution exploits alternation/exploration of an exponential game tree, power absent from monotone $FO(LFP)$ fixed-point closure.
- **Distinctions:** unary vs binary differ in sparsity/density (Mahaney) but obstruction is structural/encoding; general-poset #P results don’t transfer; need to distinguish certificate *soundness* vs *completeness* (local rules easy, global coverage hard). $FO(LFP)$ definability would force $SORT\text{-}BOUND\text{-}U \in P$ (strong upper bound) but requires nontrivial correspondence not present; this matches the research-plan warning against inferring smaller-class definitions from compact informal recursions.
- **Failed attempt:** tried to model poset-minimax by $LFP$ over poset relations — cannot quantify over all $2^{\Theta(n^2)}$ posets as domain-indexed states; alternation gives $PSPACE/FO(PFP)$, not $LFP$. No counterexample constructed, but structural obstruction identified.

**Limits:** Barrier/obstruction argument, not a proof of $P\neq PSPACE$ or $SORT\text{-}BOUND\text{-}U \notin P$. No circuit bounds used; in scope as “barrier ruling out a family of methods”. No Lean/repo changes made.


## Other metadata

```json
{
  "finished_at": 1793498718.5558584,
  "started_at": 1793496568.884378
}
```
