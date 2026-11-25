# SoringP1: research synthesis at suspension (November 24, 2026)

This is a retrospective of the archived work, not a new mathematical publication.
It distinguishes kernel theorems, paper deductions, historically independently
refereed results, finite computations, and open conjectures. A historical
agent or referee's verdict is not a new proof check by the archival operator.

## 1. The problem and what remains open

Let S(n) be the least worst-case depth of a deterministic adaptive comparison
tree sorting n distinct labeled keys. For a finite poset P, let F(P) be the
corresponding minimax cost given its known relations, e(P) its number of
linear extensions, L(P)=ceil(log2 e(P)), and D(P)=F(P)-L(P).
S(n)=F(A_n), where A_n is the antichain. In particular, the problem is not
sorting in polynomial time, but uniformly computing the optimal number of
comparisons. The active decision language was SORT-BOUND-U, with both n and k
unary. A finite n result, generic-poset separation, or restricted policy
barrier does not in itself settle the complexity of this language.

The project did not solve the main open problem. No new P, NP, coNP, or PH
placement follows from the recovered results. No superpolynomial lower bound
for an arbitrary exact evaluator was established.

## 2. Existing mathematical baseline

- [Kernel inventory](../docs/kernel-results.md): existence of a sorting tree,
  attainment and minimality of S, information lower bound, monotonicity,
  insertion upper bound n(n-1)/2, exact S(0..6)=(0,0,1,3,5,7,10), and
  correspondence with the minimax recurrence. No Lean machine-cost theorem
  is claimed here. The archival run did not rerun Lean.
- [Problem and encodings](../docs/problem.md) and [research plan](../docs/research-plan.md):
  the documented paper bounds include SORT-BOUND-U in PSPACE and
  SORT-BOUND-B in EXPSPACE. The transcript-only budgeted DFS gives
  2^O(N log N) deterministic time and O(N log N) work bits for unary threshold
  input of length N=n+k+1; for numeric evaluation on unary n, the corresponding
  bounds are 2^O(n log^2 n) time and O(n log^2 n) space.
- [Sparsity barriers](../docs/research-hardness-boundaries.md):
  the unary threshold language is sparse. Ordinary many-one NP-hardness
  would imply P=NP; general-poset and sorting-network hardness cannot be
  transferred by merely identifying a similar game.
- [Framed certificates](../docs/research-framed-certificate-frontier.md):
  polynomial-checkable sound permutation-framed strategy DAGs exist; explicit
  polynomial-size constructions for adaptive merge-sort and certain insertion
  families exist. Exact-optimal all-n completeness is open. An ordinary
  comparison tree with all redundant nodes removed has n! leaves, so it
  cannot directly be a polynomial-size certificate.
- [Winning-frontier barrier](../docs/research-winning-frontier-barrier.md):
  a very large number of nonisomorphic winning states survive information
  pruning even at the exact optimum, with a bound of
  2^((1/4-o(1)) n log^2 n) on the documented family. This excludes explicit
  exhaustive state enumeration as the hoped-for faster evaluator, not all
  compressed or symbolic methods.

## 3. Substantive recovered results and obstacles

The evidence below is in closed [Antonina #301](board/301/README.md).
The page links contain the original reports and their referee dispositions,
including qualifications. See also the thematic and referee indexes.

### Poset invariants and lookahead

- A finite **general-poset counterexample** to the claim that F is a
  function of e and the one-step extension-count deck M1 was independently
  reproduced on November 23. On seven elements, e(P)=e(Q)=32 and
  M1(P)=M1(Q)=(4,4,14,14,16,16,16,16,16,16,18,18,28,28),
  but F(P)=5 and F(Q)=6. Ordinal squares were independently computed
  with e=1024 and costs 10 and 12. Using exact ordinal additivity and deck
  preservation, repeated ordinal sums yield an unbounded gap for this
  statistic. M2 separates the seed; this does not settle fixed depth >=2
  or forced optimal-root reachability. [Referee](board/301/page-001.md).
- The independently rerun **global n=8 census** covered all 16,999
  isomorphism classes. (e,M1) had 7,567 keys, two with mixed F.
  (e,M1,M2) had 7,573 keys, zero with mixed F. The reported n=9 census
  (183,231 classes) also found no M2 conflict, but was not independently
  rerun in the cited referee pass. The reported ordinal-lift reduction
  for higher decks is partly corroborated; its M2-preservation lemma
  still merits separate proof audit. Finding a first M2 conflict at
  n>=10 or proving completeness is an open discriminator, not an
  established algorithm. [Referees](board/301/page-001.md).
- Exact e-based greedy move selection can fail: the independently
  checked n=6 witness has e=28, F=5, and three pairs tied at child
  e=(14,14), only one of which is minimax-admissible. The n=7 census
  reports systematic failures, although the full census was not rerun
  by that referee. [Referees](board/301/page-002.md).
- Ordinal-sum factorization is exact, but the per-block certificate
  deficit is the uncertified prime-defect mass. The recovered
  accumulation identity separates rounding gains from actual defect
  gains. Enriched per-block completeness fails even at A_12:
  L=29, F=30. An intermediate n=11 state with L=7, a structural
  bound 8, and F=9 was independently reconstructed, with
  full optimal-play reachability not certified at every earlier ply.
  [Referees](board/301/page-002.md).

### Defect, balancing and strategy structure

- F-synchrony theorem (historical independently rederived paper proof):
  a poset admits an optimal tree in which F drops by exactly one on
  every edge iff e(P)=2^F(P). For the antichain and n>=3, this is
  impossible since n! is not a power of two. This rules out that
  particular depth-layered normal form. [Referee](board/301/page-002.md).
- For ANY comparison, if H is the child with larger F, then
  D(P)-D(H)<=1. Proof: F(P)<=1+F(H) and L(H)<=L(P).
  Defect need not be monotone on every hard-child transition. This
  does not bound the light child's drop or all optimal states'
  defect. [Referee](board/301/page-001.md).
- A defect-free state with e(P)>3*2^(L(P)-2) has two defect-free
  children at any F-optimal comparison. The historical proof of the
  stronger recursive g conclusion has an induction-scope gap: the
  children need not meet the same density hypothesis. The argument
  validly confines a **minimal** counterexample to completeness to the
  complementary band, not every counterexample. See the
  [archival correction](CORRECTIONS.md#recursive-g-completeness) and
  [historical referee](board/301/page-001.md?plain=1#L3).
- The project found that an information-tight root can have
  defect-positive reachable states. For example, a verified
  five-comparison path from A_6 reaches e=16,F=5, with 5+F=S(6)=10.
  The conjecture that *some* optimal tree is defect-free throughout
  is a different quantifier. Finite witness claims for n<=10 were
  reported at varying verification levels. A confirmed defective
  state within the n=11 Ford-Johnson tree (e=31,185, L=15, F=16)
  rules out that particular tree. Existence of a different
  defect-free optimal n=11 tree remains open; A_12 is already defective.
  [Referees](board/301/page-002.md).
- For two disjoint 2-chains plus n-4 free keys, FF_n, a fixed two-step
  root prefix shows F(FF_n)>=S(n)-2, so its defect is at least the root
  defect. The stronger conjecture that the second comparison must
  always use two free keys is refuted at n=7. [Referees](board/301/page-003.md)
  and [page 4](board/301/page-004.md).
- The optimal fixed Fibonacci/Jacobsthal merge-insertion schedule is
  not universal: the known n=22 comparison counts distinguish the
  schedule (71) from S(22)=70. The schedule remains a valid upper
  bound, not an exact evaluator. This is literature-backed negative
  evidence, not a newly discovered sorting number.
- Other investigated structural approaches include component reversal,
  forced orientation, reset realizability, cover counts, width, chain
  decomposition, antichain reachability, per-key comparison load,
  local entropy cutoffs, and exact/bounded halving. The individual
  questions and their outcomes are indexed in THEMES.md; generic-poset
  results are not silently transferred to the antichain root.

### Entropy, asymptotics and arithmetic regularity

- For a correct comparison tree with depth <=k, uniform permutations
  give E[depth]-log2(n!)=sum_v q_v(1-h2(p_v))<=k-log2(n!).
  Thus the expected number of comparisons with split bias at least
  delta is at most (k-log2(n!))/(1-h2(1/2+delta)).
  Combined with sublinear optimal surplus, Markov's inequality yields
  that almost all leaves have o(n) such comparisons. This is about
  leaf density, not all paths, and is not an algorithm.
  [Referee](board/301/page-002.md).
- A paper argument accepted by a historical referee: integer sequences
  a_n=o(n) are P-recursive iff eventually periodic (using
  Polya-Carlson and rational generating functions). Consequently,
  assuming the published sublinear sorting surplus, the excess
  sequence S(n)-ceil(log2(n!)) is P-recursive iff eventually periodic.
  Neither eventual periodicity nor its negation was established.
  Finite data through n=22 cannot resolve it. [Referee](board/301/page-001.md).
- Multiple fronts investigated extraction of effective finite constants,
  explicit schedules and exponent sharpening from the asymptotic upper
  bound. The last two ledger reports give competing derivation readings;
  one flags an apparent exponent discrepancy, but explicitly does not
  establish an erratum or disprove the published bound. Preserve both
  reports for future source audit; do not promote either to a settled
  result. [Front ledger](fronts/README.md).

### Algorithms, certificates and descriptive complexity

- Explicit tree-block alternating certificates with polynomial-size full
  subtrees only cover O(log N) levels per block. Historical analysis
  derives a superconstant Omega(N/log N) block count on informative unary
  inputs. This is a barrier for that explicit-block scheme, not a
  general lower bound on alternations or PH membership.
  [Referee](board/301/page-002.md).
- A polynomial-size circuit selecting an exact-optimal policy, if it
  exists uniformly in size for all n, would give a Sigma_2^p upper bound
  via existential circuit guess and universal response paths. Existence
  is open. Sound verification and complete succinct representation
  remain distinct. [Referee](board/301/page-002.md).
- The FO(TC) thread independently reviewed a fixed-variable table
  evaluator and a verifier whose query answers are charged and whose
  sorted output is checked for every order. This verifies the stated
  restricted program model, not exact-budget completeness or a new
  class placement. See the [full thread](board/JTsW4AnxTLzN18IBQibXea-fervor/README.md).
  A negative claim about uniform FO(TC) expressibility in some reports
  is not justified merely by unbounded recursion; preserve as an
  unverified claim rather than a theorem.
- The explored exact-budget certificate routes include framed DAGs,
  ABC trees, rank envelopes, reset grammars, defect-pruned policy trees,
  adversarial/coNP certificates and Farkas-style or entropy lower
  witnesses. Specific constructions and counterexamples exist, but
  no complete polynomial-size exact-optimal family was established.
  Positive small-n examples are not completeness.
- Transcript-only DFS, replay, checkpointing, pebbling, reversible
  and catalytic space, reachable-state quotients and bidirectional
  search were investigated. The documented O(N log N) space bound
  survives; O(N) work space for the unrestricted unary threshold
  problem and 2^O(n log n) or 2^O(n) numeric evaluation remain open.
  Method-specific barriers are not arbitrary-machine lower bounds.

## 4. Most consequential unresolved directions

This is a historical open-question register, not a work assignment.

1. Complete polynomial-size exact-optimal strategy or refutation
   certificates, or a general obstruction to a specified representation.
2. Exact evaluator improving the transcript DFS time or space without
   enumerating the huge winning frontier.
3. An all-n root-specific structural invariant that accounts for
   non-information-tight cases such as n=12, and preserves reachability.
4. Global M2 deck completeness or a first counterexample, with a
   separate root-transfer theorem if complexity consequences are sought.
5. Existence of a defect-free optimal A_11 tree; completeness of the
   recursive g predicate; extent of defect drops on optimal paths.
6. Exact excess-sequence regularity, effective asymptotic bounds,
   and independent audit of the apparent exponent issue.

## 5. How to recover any original result

The ledger front index includes all 750 questions, their falsifiers,
implications, statuses, and recovered findings. The thematic index groups
them, not by proof status but by rough topic. The board includes the entire
two closed issues, including rejected claims and corrections. The workspace
manifests map to deduplicated source objects and historical patch files.
Supplemental records recover retired worktree material and Viche's
research dispositions. The assistant-output archive preserves recoverable
assistant-visible reports, excluding private reasoning/tool traces.
The archive's coverage is limited by what survives on Billy and the board;
a missing scratch file cannot be reconstructed merely from a cited filename.
