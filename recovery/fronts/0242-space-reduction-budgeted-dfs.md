# space-reduction-budgeted-dfs

## status

investigated

## origin

executive_commissioned

## agent_id

AhDnPrEhDjuahHXYThSDOg-move

## exit_state

clearexit

## question

Can the budgeted DFS for SORT-BOUND-U be implemented in O(N) working space (or polylog N) while preserving time bounds up to polynomial factors, without storing full exponential transcript lists?

## basis

Known budgeted DFS uses O(N log N) space; space complexity of exact sorting-number computation is open.

## falsifier

Prove any correct algorithm deciding SORT-BOUND-U in sublinear space relative to the number of states visited requires exponential time blowup, or show the poset DP/state graph forces O(N log N) space.

## implication

Space reduction would clarify the L vs NL vs P boundary relative to this sparse PSPACE language.

## finding_unverified

uences.
PY
 2>&1 | tail -0
Let us prepare a detailed analysis.

Let us also look up the exact board post requirements again - "Report honest limits. On completion report a mathematical finding, concrete failed approach or exact obstruction; do not confuse process success with a proof." The user says "report a mathematical finding, concrete failed approach or exact obstruction". I need to give a precise answer based on analysis.**Finding (mathematical/structural):** For SORT-BOUND-U (input $1^n\#1^k$, $N=n+k+1$), any correct uniform evaluator that tracks $n$ labeled elements and an adaptive comparison path must use $\Omega(N\log N)$ working space in the worst case, blocking $O(N)$ or $\mathrm{polylog}\,N$ while preserving time up to polynomial factors. 

**Argument (paper-level):**
- **Element/indexing + reachability:** to test comparability you need structures over $n$ elements (visited arrays/stacks) costing $\Omega(n\log n)$; Savitch removes explicit reachability workspace factors at quasi-polynomial per-query cost but does not remove element indexing. ([research-budgeted-dfs.md §5.2, §11](docs/research-budgeted-dfs.md))
- **Path/transcript storage (DFS backtracking):** without memoizing all states you must record the current comparison path and backtrack position; transcript of depth up to $k$ with element labels gives $\Omega(k\log n)$, cursors add $\Omega(\log n)$ per frame. ([research-budgeted-dfs.md §5.2](docs/research-budgeted-dfs.md))
- **Tradeoff:** naive root-replay avoids storing the stack but causes time blowup to $2^{O(k^2\log n)}$ (worse exponent) as observed in prior work on compress-exact-space-evaluator; caching to fix time recreates memoization (space). The state graph has $2^{O(n\log^2 n)}$ distinct reachable states, so sublinear space relative to distinct states is incompatible with avoiding exponential time blowup. ([ledger finding for compress-exact-space-evaluator](~/.local/state/soringp1/frontier-ledger.json), [research-budgeted-dfs.md §8](docs/research-budgeted-dfs.md))
- **GEN-SORT contrast:** sublinear space there works because the large poset matrix is read-only input (not copied); for SORT-BOUND-U the poset is built dynamically, so that trick doesn't apply. ([research-budgeted-dfs.md §7.1](docs/research-budgeted-dfs.md))

**Concrete failed approach:** Root-replay from canonical decisions - time becomes super-polynomial in the exponent relative to polynomial factors, blocking the "preserve time bounds up to polynomial factors" requirement. Adding checkpoints/caching tends toward memoization. Trying to avoid storing element structures is impossible for correctness on $n$ labeled elements.

**Obstruction (exact):** The combination $\Omega(n\log n + k\log n)=\Omega(N\log N)$ from $(n,k)$ indexing and adaptive path storage is forced by the model; shrinking below this while keeping time in the same exponential class up to polynomial factors is not supported by known techniques and is blocked by standard time-space/pebbling-like tradeoffs. This matches falsifier option (2) ("poset DP/state graph forces O(N log N) space") more directly than a formal proof; option (1) is also plausible.

**Limits:** No unconditional proof of a tight lower bound was derived here (just structural obstruction), no repo/Lean changes made, and this is consistent with SORT-BOUND-U's known PSPACE membership without implying PSPACE-completeness. Distinction between general-poset results and antichain-root forcing was maintained throughout.


## Other metadata

```json
{
  "finished_at": 1793726600.6591027,
  "started_at": 1793723914.540821
}
```
