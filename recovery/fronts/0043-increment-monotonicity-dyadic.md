# increment-monotonicity-dyadic

## status

investigated

## origin

executive_manual_dispatch

## agent_id

SoiSrNjK2T1LkcR7PCaYSZ-quiet

## exit_state

clearexit

## question

Is d(n)=S(n)-S(n-1) non-decreasing in n, and is d(2^k)=k (insertion lower bound achieved at powers of two)? For known n<=22 values d appears non-decreasing and equals ceil(log2 n) at powers of two; prove or disprove general all-n monotonicity and characterize when d(n)=ceil(log2 n).

## basis

Known exact values show d non-decreasing up to 16 and d(2^k)=k; recent board post suggests power-of-two case gives equality to the insertion lower bound ceil(log2 n).

## falsifier

Find any n>=3 with d(n) < d(n-1), or prove monotonicity fails for all large n, or show d(2^k) > k for some k via a better insertion lower bound.

## implication

Monotonicity of the increment would give strong structural constraints on the sorting number function and might imply new bounds or help relate S(n) to the information bound across scales.

## finding_unverified

=4 (k=2): d=2$, $n=8 (k=3): d=3$, $n=16 (k=4): d=4$. All equal $k=\lceil \log_2 n\rceil$.
- Equality $d(n)=\lceil \log_2 n\rceil$ holds at other $n$ too (e.g. 3,6,7,11,12,13,14,15,22 in this list), not just powers of two.
- $d(n) \ge \lceil \log_2 n\rceil$ is **false in general** (n=5: 2>=3 no, n=9: 3>=4 no, n=10: 3>=4 no). The board’s “insertion lower bound” phrasing is confused - you cannot deduce this from placing a single element into a fixed sorted list for the global optimal $S$ (the global strategy can interleave comparisons).

### Monotonicity of $d(n)$
- Observed monotonic up to $n=22$. No known counterexample in exact values.
- $d_C(n)$ (info bound increments) is **not** monotonic (drops at 12,20,21...). $S$ tracks info bound tightly in many places but also has gaps; known values stay monotonic despite $d_C$ oscillating.
- **Status:** This is widely regarded as open in general. I cannot find a published proof of “$S$ is convex” ($d$ non-decreasing) for all $n$, nor a published counterexample. With $S(23)$ unknown, a counterexample cannot be constructed from current exact tables.

### $d(2^k)=k$
- For all known powers of two, equality holds. Also $d_C(2^k)=k$ always.
- Where $S(2^k)=C(2^k)$ and $S(2^k-1)=C(2^k-1)$ (info bound tight on both sides), $d_S = d_C = k$ is immediate. Where gaps exist on both sides by same amount (e.g. 15,16 both gap +1), equality is preserved. 
- Can we get $d(2^k)>k$ via a “better insertion lower bound”? Any lower bound giving $d_S >= k+\epsilon$ would need to beat $d_C=k$; but $d_S >= C(2^k) - S(2^k-1)= k + C(2^k-1) - S(2^k-1)= k - \delta$ where $\delta = S(2^k-1)-C(2^k-1)\ge0$ is the gap above info bound at $2^k-1$. So a strong lower bound on $d_S$ relative to $k$ would require showing $S(2^k-1)$ cannot be much larger than $C(2^k-1)$. I know of no published argument that forces $d_S > k$ at some power of two; conversely no obvious obstruction to equality if gaps stay aligned.

### Complexity implication (honest)
- Monotonicity of $d(n)$ (convexity) would give structural constraints, but is not obviously equivalent to a standard complexity separation and doesn’t directly touch the P/NP/PSPACE boundaries discussed in AGENTS.md except through structural properties of $S$. The P/log advice argument uses $S$ monotonicity ($S_mono$) and $f(n)=n+S(n)$ strictly increasing - that only needs $S(n+1)\ge S(n)$, not convexity of $S$. So the stated complexity implication is plausible as structural constraint, but I don’t see a clean chain to P≠PSPACE from convexity alone.

### Conclusion (tried to disprove)
- **Cannot disprove monotonicity of $d(n)$** with known exact values (all monotonic to 22). No published counterexample; constructing one would require unknown $S(23+)$.
- **Cannot disprove $d(2^k)=k$** with known values; the info-bound increment forces $k$ and known $S$ achieve it. No obvious “better insertion lower bound” gives $>k$.
- **Can disprove the board’s specific inequality** $d(n)\ge \lceil \log_2 n\rceil$ generally (n=5,9,10 counterexamples) - this is a false general claim as stated.

**Obstruction:** The falsifiable claims as stated are either false in a stated form ($d(n)\ge\lceil\log_2 n\rceil$ generally) or appear true on known data but are open in general (monotonicity of $d(n)$, exactness of $d(2^k)=k$ for all $k$). Without new exact values of $S(n)$ for large $n$ or a general combinatorial proof/disproof, I cannot produce a concrete counterexample or a theorem here. This is an honest limit.

## Other metadata

```json
{
  "finished_at": 1793346346.764238,
  "started_at": 1793342986.277639
}
```
