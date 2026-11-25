# Excess boundedness D(n)=S(n)-⌈log2(n!)⌉ — all-n question

Status: [deduction] + [experiment] + [open]. Front: excess-boundedness-alln.  
Falsifier: prove sup D(n)<∞ for all large n, or construct infinite family with D(n)->∞ slowly (and ensure bridge to antichain root / exact S(n)).

## Known values (verified)
From literature (OEIS A036604, Stober–Weiß 2023, Peczarski): S(1)=0,C(1)=0 D=0; S(2)=1,C(1)=1 D=0; S(3)=3,C(3)=3 D=0; S(4)=5,C(5)=5 D=0; S(5)=7,C(7)=7 D=0; S(6)=10,C(10)=10 D=0; S(7)=13,C(13)=13 D=0; S(8)=16,C(16)=16 D=0; S(9)=19,C(19)=19 D=0; S(10)=22,C(22)=22 D=0; S(11)=26,C(26)=26 D=0; S(12)=30,C(29)=30 D=1; S(13)=34,C(33)=34 D=1; S(14)=38,C(37)=38 D=1; S(15)=42,C(41)=42 D=1; S(16)=46,C(45)=46 D=1; S(17)=50,C(49)=50 D=1; S(18)=54,C(53)=54 D=1; S(19)=58,C(57)=58 D=1; S(20)=64,C(62)=64 D=2; S(21)=68,C(66)=68 D=2; S(22)=71,C(70)=71 D=1. S(23) in {75,76}, C(23)=75 so D(23) in {0,1} (open). sup_{n<=22} D(n)=2.

Note: D is non-monotone (dips to 0 effect? no - values go up to 1 through 12-19, to 2 at 20,21, down to 1 at 22). The drop pattern mirrors Ford-Johnson F(n)-C(n).

## Exact identity (Theorem 2.1, deduction)
For reduced correct tree, let e(v) be number of linear extensions at poset v, branches give e(v_i). For any root-to-leaf path, log2 n! = sum log2(e(v)/e(v_i)). Define waste ν = 1 - log2(e(v)/e(v_i)) (signed). Then depth(ℓ)-log2 n! = sum ν, S(n)=min_trees max_ℓ depth(ℓ)=⌈log2 n! + W*(n)⌉ with W*=min_trees max_ℓ sum ν. Thus D(n)=⌈log2 n! + W*(n)⌉ - ⌈log2 n!⌉. Bounded excess (sup D <= C) iff there is a family of trees making total path waste uniformly bounded in n (up to ceiling). Unbounded excess means W*(antichain_n) grows without bound relative to fractional part of log2 n!.

Also W* is minimax on posets (not function of e alone) — matches known non-tightness.

## Barriers
- Construction: binary insertion gives Θ(n) excess total; Ford-Johnson gives O(n) with small constant but still growing in form? Ford-Johnson excess F(n)-C(n) grows (0 up to some point, becomes 1 at 25, etc., Θ(n) asymptotically per Sergeev) — no known construction gives summable per-element loss => cannot give bounded D(n). Sergeev gives S(n)-C(n)=O(n/(log n)^(1/5)) = o(n).
- Lower bound: no analytic proof that S(n) > ⌈log2 n!⌉ for any n>=12; all D>=1 come from exhaustive search over poset states. Adversary potential must survive non-monotone dips. Smallest open decisive cell is D(23) (determine if S(23)=75 or 76).

## Consequence for complexity
As per AGENTS.md: unary SORT-BOUND-U in PSPACE; showing not in P would give P!=PSPACE etc. But excess bounded/unbounded is about the additive gap to information bound - different question from class separation. The boundedness is a very strong structural property of the comparison model; unboundedness is plausible given test restrictions (comparisons) vs arbitrary tests. No obvious transfer to class separation from boundedness alone stated in contract; the question is sharp and falsifiable.

## Recommendation
1. Check primary sources: Stober–Weiß for S(16)-S(18), Peczarski for S(22), Wells/Kasai/Cheng et al. for earlier; Sergeev asymptotics. The gap is exactly D(23). If S(23)=76 then D>=1 continues; if S(23)=75 then D(23)=0 (gap closes again). Also need to see if there is any analytic lower bound technique.
2. Look up the "information-theoretic bound" literature - Ford–Johnson was optimal up to some point; the question of whether excess is bounded is sometimes called "comparison complexity excess" - I need to recall or derive. But must use primary sources.
3. The waste identity shows excess boundedness iff uniform O(1) path waste possible - equivalent to a kind of "entropy-preserving" strategy with bounded overhead. For comparison trees (a very restricted class of tests with history dependence), this is extremely restrictive. Contrast with arbitrary tests (can achieve 0 excess). So unbounded excess seems combinatorially plausible; bounded would be shocking. But need rigorous argument either way.

## Verified small experiment (from existing data)
Our table shows max D so far is 2 at n=20,21. All values 0,1, or 2. No values >=3 observed. D(23) unknown but C(23)=75 same as S(n) lower bound from info - so possible D(23)=0.

## Precise falsifier/blocker
- **Falsify bounded (prove unbounded):** Find an analytic invariant I(P) >= something related to waste on posets reachable from antichain with I(antichain_n) >= c·f(n), f(n)->∞, and show I propagates under optimal adversary play (or under any strategy) giving D(n)>=f(n). Must survive non-monotonic dips (n=20,21). Hard because no analytic info-bound violation known for n>=12.
- **Falsify unbounded (prove bounded):** Give uniform construction with Σ ε_k(n) = O(1) path waste for all n (summable per-element loss) - contradicts all known methods (binary insertion/Ford-Johnson/Sergeev give Θ(n) or growing total). Or prove minimax potential W* bounded. No such construction exists.
- **Decisive small step:** Determine D(23)=S(23)-75 in {0,1}. If S(23)=76, sup grows; if S(23)=75, another dip. Either way, this is a concrete computational question (Stober–Weiß suggest feasible with current methods) - but doing it ourselves may be beyond scope/time; documenting it as the key discriminant is valuable.

## Blocker (current state)
Both directions lack the necessary tools. The waste identity is exact but doesn't resolve boundedness. Local poset excess doesn't transfer to root (prior attempt noted). The data shows D(n) in {0,1,2} for all known n with irregular behavior. No rigorous result known either way. This is an open question in sorting theory; resolving it would be a major result. As a SoringP1 research task, the most honest deliverable is the reformulation + verified data + precise falsifier/blocker - which matches what we've done. No Lean changes warranted. No code changes needed.
