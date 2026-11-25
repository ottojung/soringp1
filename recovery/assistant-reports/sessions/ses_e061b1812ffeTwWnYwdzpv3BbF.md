# antonina-08PnUbiMfAh6iXdQwyCQKu-towels

Session: ses_e061b1812ffeTwWnYwdzpv3BbF
Workspace: /home/lubko/soring-fronts/verify-tight-fj-20-21
Created: 1795193890931; updated: 1795193956582

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f9e4eaad0014E9j8R71H2JEY1)

I’ll check the post’s provenance and cited primary sources, then independently recompute the recurrence and inspect the argument connecting its recursive comparison macro to worst-case tree height. I’ll keep this as a verification report only—no repository or Lean changes.

## Output 88 (msg_1f9e551540010Uksg6p8FrF6w1)

## Verdict

The numerical claim is correct, and the implication to optimality is valid **provided the standard Ford–Johnson worst-case bound is being applied to its usual adaptive comparison-sort model**. The claim describes an explicit upper-bound construction; it should not be presented as a new historical proof of the exact values.

**Exact arithmetic — independently recomputed.** For \(F(n)=\sum_{j=1}^n\lceil\log_2(3j/4)\rceil\), the summands are:

- \(n=10\): \(0,1,2,2,2,3,3,3,3,3\), sum \(22\).
- \(n=20\): those terms followed by \(4\) for each \(j=11,\ldots,20\), sum \(62\).
- \(n=21\): the \(n=20\) sum plus \(4\), giving \(66\).

The information bound agrees: \(2^{21}<10!<2^{22}\), \(2^{61}<20!<2^{62}\), and \(2^{65}<21!<2^{66}\). Thus \(L(n)=\lceil\log_2(n!)\rceil\) is respectively \(22,62,66\). Ford–Johnson gives \(S(n)\le F(n)\); the decision-tree information bound gives \(S(n)\ge L(n)\). Equality follows for these three sizes.

**Model and source check.** The repository’s problem definition is minimum worst-case height of a finite adaptive binary comparison tree sorting distinct labelled keys. Ford–Johnson’s merge-insertion algorithm is a comparison sort in that model—not a sorting network. The repository’s literature review identifies Ford and Johnson’s 1959 *A Tournament Problem* as the primary algorithm source, and Knuth, *TAOCP* vol. 3 §5.3.1, as a standard account of the bound. I could not retrieve the 1959 paper’s full text in this check, so I have not independently audited its original proof line by line. The local note `docs/research-upper-witnesses.md` records the same formula as the classical worst-case bound and explicitly distinguishes the strategy from the optimum.

For historical context, Stober and Weiß’s primary paper, [*Lower Bounds for Sorting 16, 17, and 18 Elements*](https://arxiv.org/abs/2206.05597), says that before their work the values were known through \(n\le22\), except for \(16,17,18\), which their search settled. The post’s construction is therefore a direct upper-bound-plus-information-lower-bound argument at \(20,21\), not a replacement for the historical record or the computational lower-bound proofs elsewhere.

**Recursive macro-height scrutiny.** The recurrence is a bound on the *whole recursive algorithm*, not just on its final insertion phase. In the usual construction, pair comparisons, recursive sorting of winners, and scheduled loser/straggler insertions must all be accounted for; the Jacobsthal-based schedule controls insertion search lengths. The local executable reference in `scripts/upper_witness.py` implements those pieces, but its tests exhaustively check permutations only through \(n\le6\). That experiment alone does **not** certify height at \(20\) or \(21\); the all-\(n\) guarantee comes from the classical Ford–Johnson analysis. A macro/certificate argument must preserve winner–loser associations through the recursive sort and handle the odd unpaired key, as the caveat in `docs/research-framed-certificate-frontier.md` notes.

**Precise uncertainty:** I could not inspect the timestamped #301 post itself, so I cannot confirm its exact wording or timestamp. The mathematical assertions quoted in the request check out, conditional on the standard Ford–Johnson bound; no repository or Lean changes were made.

## Output 99 (msg_1f9e5b169001x88v2JeK16wwWJ)

I’m treating this as a recovery check, not a request to repeat the research or post anything. In the prior turn I only read local sources and fetched public references; I did not invoke Antonina or make repository edits. I’ll verify the current Git state and any durable local records before concluding.

## Output 122 (msg_1f9e5ce7f001SuXM0d0jqaBaN5)

Recovery check complete. The prior turn performed only local reads and public-reference fetches; it did not post to Antonina, commit, or edit files.

Git is clean: `HEAD` is `6cddeaa` (`Repair split-schema witness-tree builder (sound greedy upper bound)`), matching `origin/main`. No local `#301` or Antonina task record was found in the repository. The requested mathematical verification was already completed in the previous response. The post’s exact contents and timestamp remain unverified, so I’m not repeating or publishing anything.
