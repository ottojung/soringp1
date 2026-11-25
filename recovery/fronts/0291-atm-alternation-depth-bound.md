# atm-alternation-depth-bound

## status

blocked

## origin

ai_proposal_unverified

## agent_id

JBl2QsRHlmeVDvd6SCMe6N-venereal

## exit_state

stopped

## question

For the alternating Turing machine deciding SORT-BOUND-U via the minimax game G(n,k), is the polynomial alternation depth O(k)=O(n log n) necessary for all-n instances, or can a uniform ATM decide it with alternation depth O(log^c (n+k)) for some fixed c (bounded or polylog alternation)?

## basis

Claim A of research-certificates-barriers.md gives APTIME=PSPACE via O(k) alternations on unary input; Chandra-Kozen-Stockmeyer alternation hierarchy and the distinction between fixed alternation levels and PSPACE remain untested against the specific sorting game structure.

## falsifier

Construct a uniform alternating Turing machine for SORT-BOUND-U with alternation depth O(log^c N) and polynomial time in unary input length N, or prove that every uniform ATM accepting SORT-BOUND-U must have alternation depth Omega(n / polylog n) on infinitely many unary inputs.

## implication

A bounded/polylog alternation bound would place SORT-BOUND-U in a strict subclass of PSPACE (below the full linear-alternation level) without invoking circuit lower bounds; a necessary linear alternation depth would clarify the game-theoretic complexity of the minimax search and constrain reductions to fixed-level alternating classes.

## finding_unverified

Let us look up the exact ATM description again carefully.

Let us look up more about the hardness of sorting-related problems.

Let us start by exploring the exact question more systematically. The key is understanding if the sorting game G(n,k) is PSPACE-complete or in lower levels of PH.

Let us read more about this.

Let us think about this question carefully.

Let us look up more about this specific game.

Now let us understand the exact question again:
> "For the alternating Turing machine deciding SORT-BOUND-U via the minimax game G(n,k), is the polynomial alternation depth O(k)=O(n log n) necessary for all-n instances, or can a uniform ATM decide it with alternation depth O(log^c (n+k)) for some fixed c (bounded or polylog alternation)?"

Also "FALSIFIER: Construct a uniform alternating Turing machine for SORT-BOUND-U with alternation depth O(log^c N) and polynomial time in unary input length N, or prove that every uniform ATM accepting SORT-BOUND-U must have alternation depth Omega(n / polylog n) on infinitely many unary inputs."

So this is asking about alternation depth in the ATM. From Chandra-Kozen-Stockmeyer, Σ_k^P (and Π_k^P) are languages accepted by ATMs that alternate k times starting with existential, in polynomial time. APTIME is PSPACE = union_k Σ_k^P in some sense? No wait - APTIME is ATMs running in polynomial time with any number of alternations (bounded by polynomial time) = PSPACE. The alternation hierarchy within PSPACE is related to how many alternations. Also, for polynomially bounded alternations you get PH, and if you allow polynomial number of alternations you get PSPACE.

But if an ATM runs in polynomial time, the maximum number of alternations it can do is at most polynomial in input length. Also, Σ_k^P are usually considered for fixed k and polynomial time. If k can grow (polynomially), that's PSPACE. 

Looking at the game: each round is "sorter picks a pair (existential move)" then "adversary answers (universal move)" - that's 2 alternations per round of comparison. The game goes up to k rounds. So the ATM does k rounds * 2 alternations = O(k) alternations. Since k can be O(n log n) and n is polynomial in unary input length N (N = n + k + 1), we get O(N log N) alternations total, which is polynomial in N. That matches APTIME = PSPACE.

The question is whether we can do better by using a different strategy - not playing round by round the same way, but doing some other computation that uses fewer alternations (like bounded or polylog alternation) while still polynomial time, thus placing SORT-BOUND-U in some subclass below PSPACE (like Σ_c^P union or related). Or is the linear/polynomial alternation depth necessary for all-n instances?

Also the falsifier wants to construct such ATM with O(log^c N) alternation depth and polytime, or prove every uniform ATM needs Ω(n/polylog n) alternations on infinitely many inputs.
Let us look up more about the sorting game / comparison game complexity. Also the "coin weighing game" or "mastermind"? Or more directly, "combinatorial search games" - some are PSPACE-complete? For example, the "Ulam’s game with lies" is PSPACE-complete? Or "coin weighing with a spring scale"?

Or another possibility is that determining the "graph’s pathwidth" via some games gives PSPACE-completeness? Or "graph bandwidth"? Let us search more specifically.


## Other metadata

```json
{
  "finished_at": 1793835467.7916088,
  "started_at": 1793825879.5479538
}
```
