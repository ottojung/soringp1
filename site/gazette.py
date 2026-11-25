"""Human-oriented editorial introduction to the archived sorting research.

The essays are deliberately selected and written by hand, not generated
from workflow labels. The links lead to the evidence register and its
qualifications. No new mathematical claims are certified here.
"""
from render import esc


def story(ident, desk, title, paragraphs, links, status):
    """Render a short article with explicit evidence pointers."""
    return (
        '<article class="gazette-story" id="'+esc(ident)+'">'
        '<div class="gazette-desk">'+esc(desk)+'</div>'
        '<h3>'+esc(title)+'</h3>'
        + ''.join('<p>'+esc(p)+'</p>' for p in paragraphs)
        + '<p class="gazette-status">'+esc(status)+'</p>'
        + '<div class="gazette-links">'+''.join(
            '<a href="'+esc(url)+'">'+esc(label)+'</a>' for url,label in links
        )+'</div></article>'
    )


def home(index, fronts, board, searchform):
    n=len(index.records)
    body='''<div class="gazette">
<header class="gazette-masthead">
  <div class="gazette-edition"><span>Research notebook &amp; mathematical curiosities</span><span>Archive edition · November 2026</span></div>
  <h1>The SoringP1 Gazette</h1>
  <p>On the hidden difficulty of putting things in order.</p>
</header>
<section class="gazette-intro" aria-label="Introduction">
  <p>Imagine someone gives you a pile of distinct objects and lets you learn only which of two objects is smaller. What is the fewest questions you need to guarantee their complete ordering? We explored this deceptively simple problem through algorithms, logic, combinatorics and thousands of small experiments. Here are some of the puzzles that made it worth investigating.</p>
  <div class="gazette-notation"><strong>S(n)</strong><span>The least possible worst-case number of comparisons for n distinct objects.</span><a href="guides/problem.html">The precise problem</a></div>
</section>
<section class="gazette-lead" aria-label="Featured stories">
  <article class="gazette-feature" id="one-extra-comparison">
    <div class="gazette-desk">Cover story · The information barrier</div>
    <h2>Why do twelve objects need one more comparison?</h2>
    <p class="gazette-deck">A question can have two answers, yet sorting is more constrained than simply asking twenty-nine yes-or-no questions.</p>
    <figure class="gazette-numbers">
      <div><strong>29</strong><span>Information lower bound</span></div>
      <div class="gazette-versus">versus</div>
      <div><strong>30</strong><span>Optimal worst case</span></div>
      <figcaption>Sorting twelve distinct elements: 12! possible orders, but not all binary questions are legal comparisons.</figcaption>
    </figure>
    <p>There are 479,001,600 possible orders for twelve objects. A binary tree with depth 29 has enough leaves to distinguish them all. But a comparison tree is not an arbitrary binary tree: every question must compare two elements, and its answers constrain the next legal partitions.</p>
    <p>The known exact answer is 30. That single extra comparison captures a much larger mystery: how much does the structure of legal questions cost, beyond the amount of information we need to acquire?</p>
    <p class="gazette-status">Established exact value · The general structure of the excess is open.</p>
    <div class="gazette-links"><a href="results/l01.html">Exact values and scope</a><a href="results/d09.html">Why a certificate can miss the gap</a></div>
  </article>
  <article class="gazette-side" id="identical-forecasts">
    <div class="gazette-desk">Counterexample of the issue</div>
    <h2>Same clues. Different futures.</h2>
    <p>Suppose you have already made some comparisons. There are 32 possible orders left. Surely counting how many remain after each possible next question should tell you how hard it is to finish?</p>
    <figure class="gazette-pair" aria-label="Two seven-element partial orders with equal extension counts and equal one-step decks, but different optimal comparison costs">
      <div><span>State P</span><strong>32</strong><small>possible orders</small><b>5 comparisons</b></div>
      <div><span>State Q</span><strong>32</strong><small>possible orders</small><b>6 comparisons</b></div>
      <figcaption>Identical multiset of one-step child extension counts.</figcaption>
    </figure>
    <p>Two seven-element partial orders have exactly that same one-step profile, but their optimal remaining costs are five and six. Repeat the construction using ordinal sums, and the gap grows without bound. A seemingly rich numerical summary has forgotten something essential about the geometry of the decision problem.</p>
    <p class="gazette-status">Finite witness independently checked; unbounded gap derived by ordinal additivity. Arbitrary partial orders, not necessarily forced states of optimal root sorting.</p>
    <div class="gazette-links"><a href="results/p01.html">The original witness</a><a href="results/p02.html">The unbounded gap</a></div>
  </article>
</section>
<section class="gazette-section">
  <div class="gazette-section-heading"><h2>Curiosities from the research desk</h2><p>What we tried, why it was tempting, and what survived.</p></div>
  <div class="gazette-columns">'''
    body+=story('balanced-questions','01 / The greedy trap',
        'Is the most balanced question the best question?',[
        'If a comparison splits the remaining possible orders exactly in half, it seems hard to improve on it. This is the natural greedy strategy: learn as much as possible in the next step.',
        'In a six-element witness with 28 remaining orders, three candidate comparisons each split them into 14 and 14. Only one is optimal. The immediate information gain is identical, but the future work is not.',
        'The puzzle is what deeper information would be enough to choose correctly without searching the entire game.'],
        [('results/p04.html','The equal-split witness'),('results/p05.html','A deeper lookahead')],
        'Finite counterexample · Not a refutation of all extension-count methods.')
    body+=story('second-look','02 / The lookahead detective',
        'Can two steps reveal what one step hides?',[
        'The seven-element collision raises a natural challenge: inspect not just the next comparison, but the possibilities after another one. Does the resulting two-step signature determine the optimal remaining cost?',
        'An independently rerun census of 16,999 eight-element partial-order classes found two collisions in the one-step signature with different costs, but none in the two-step signature. It is an intriguing success for a small finite universe, not a universal theorem.',
        'A proof of completeness or a larger counterexample would both tell us something valuable about what local observations can encode.'],
        [('results/p03.html','The eight-element census'),('results/p05.html','What remains open')],
        'Open question · Eight-element census independently reproduced.')
    body+=story('short-program','03 / Logic and compression',
        'Can a sorting tree fit inside a short program?',[
        'An explicit decision tree must account for every permutation of n elements. That means n! reachable leaves, even if the procedure has a beautifully simple description.',
        'We investigated compact strategy representations, including permutation-framed directed acyclic graphs and programs evaluated with first-order logic plus transitive closure, FO(TC). They can describe useful sorting strategies without spelling out the entire tree.',
        'The prize would be a compact, efficiently checkable description of an exact-optimal strategy for every n. That is a much stronger demand than merely describing a good sorting algorithm.'],
        [('results/c01.html','Framed strategy certificates'),('results/c02.html','FO(TC) program models'),('results/c05.html','A complexity consequence')],
        'Constructive partial results · Exact-optimal completeness remains open.')
    body+=story('perfect-start','04 / The cost of a good decision',
        'A perfect start can lead to an imperfect future.',[
        'Sorting six objects needs ten comparisons, exactly the rounded information lower bound. You might expect an optimal strategy to preserve that kind of efficiency at every subsequent position.',
        'But there is an optimal play that reaches a state after five comparisons with sixteen possible orders left. Four binary questions would be enough in an unconstrained world; the actual remaining minimax cost is five.',
        'An optimal worst-case algorithm can contain locally wasteful-looking positions. Understanding when such positions are avoidable is a different question from proving the root optimum.'],
        [('results/k02.html','The formal small-n values'),('results/d04.html','The defect witness')],
        'Finite counterexample · Does not rule out a different, defect-free strategy.')
    body+=story('winning-states','05 / The size of the search',
        'There can be too many good positions.',[
        'One way to solve exact sorting is to keep every position from which victory is still possible within the comparison budget. Prune everything else, and hope that the surviving frontier stays manageable.',
        'A construction in the archive shows that the winning frontier itself can be enormous, even with an exact budget on the constructed family. Restricting attention to winnable states does not automatically make enumeration cheap.',
        'The interesting escape route is to represent sets of states symbolically, or avoid this search altogether. Counting positions cannot rule out algorithms that never enumerate them.'],
        [('results/b02.html','The frontier construction'),('results/a03.html','A different exact search method')],
        'Paper argument · Barrier to explicit enumeration, not a general time lower bound.')
    body+=story('sorting-complexity','06 / The complexity of knowing',
        'Sorting is easy. Knowing how well we can sort is harder.',[
        'Ordinary sorting takes polynomial time. The problem here is different: given n and a comparison budget k, decide whether some strategy always finishes within k comparisons.',
        'The answer depends on how the numbers are encoded. The archived algorithms give a polynomial-space upper bound for the unary threshold problem. Its sparsity also severely restricts conventional many-one hardness claims.',
        'This makes it a curious candidate for studying complexity without assuming that familiar hardness results for more general sorting problems transfer to this one.'],
        [('results/a02.html','Space upper bounds'),('results/b01.html','Sparse language boundaries'),('guides/problem.html','The exact decision problem')],
        'Paper arguments · P, NP, coNP and PH membership remain unresolved.')
    body+='''</div></section>
<section class="gazette-section gazette-workbench">
  <div class="gazette-section-heading"><h2>At the referee’s desk</h2><p>Research is also the art of finding out what a result does not say.</p></div>
  <div class="gazette-columns two">'''
    body+=story('proof-correction','A proof that almost worked',
        'One step is not the whole induction.',[
        'A historical argument found a useful density condition that forces both children of an optimal comparison to be information-tight. It then tried to apply the same argument recursively.',
        'But the children need not satisfy the density condition again. The valid one-step deduction survives; the sweeping recursive conclusion does not follow. The revised argument still constrains the shape of a smallest possible counterexample.',
        'Preserving the failed step is valuable: it tells a future researcher exactly where a promising proof needs a new idea.'],
        [('results/d03.html','The surviving statement'),('guides/corrections.html#recursive-g-completeness','The corrected argument')],
        'Proof-scope correction · Stronger completeness claim remains open.')
    body+=story('certificate-exception','A lesson from local certificates',
        'One bad path is not the end of every path.',[
        'A local certificate system promised to recognize optimal sorting strategies. Experiments found optimally reachable states on eight and nine elements where the certificate method could not achieve the true optimal remaining cost.',
        'That disproves the stronger claim that every optimally reachable state is certifiable. It does not settle whether some entirely certified optimal tree exists for each input size.',
        'This distinction between a possible path and an unavoidable path recurs throughout the project. A useful counterexample is strongest when we state exactly which claim it refutes.'],
        [('results/c03.html','The certificate counterexamples'),('guides/open-questions.html','Open certificate questions')],
        'Finite negative result · Existence of a certified optimum remains open.')
    body+='''</div></section>
<section class="gazette-section gazette-reading">
  <div class="gazette-section-heading"><h2>Keep reading</h2><p>From the stories to the mathematics, proofs and original experiments.</p></div>
  <div class="gazette-reading-grid">
    <a href="guides/synthesis.html"><strong>The research in perspective</strong><span>A longer synthesis of the important directions and results.</span></a>
    <a href="results/index.html"><strong>Results and their evidence</strong><span>Formal theorems, finite computations, deductions and conditional claims.</span></a>
    <a href="guides/open-questions.html"><strong>The unanswered questions</strong><span>What we would investigate next if the project resumes.</span></a>
    <a href="topics/index.html"><strong>All mathematical topics</strong><span>Browse every research direction by subject.</span></a>
  </div>
</section>
<section class="gazette-archive" aria-label="Research archive">
  <div class="gazette-desk">The archive behind the gazette</div>
  <h2>Follow a curiosity all the way down.</h2>
  <p>Every story is a doorway into the original work: exact statements, referee discussions, source code, experiment outputs and historical corrections. Search by an idea or browse the entire collection.</p>'''
    body+=searchform('index.html')
    body+='<div class="gazette-archive-links"><a href="explore.html">Explore the research</a><a href="browse/index.html">Browse evidence collections</a><a href="guides/archive-guide.html">About the archive</a></div>'
    body+=f'<p class="gazette-archive-meta">{len(fronts):,} research directions · {len(board):,} board messages · {n:,} searchable records</p>'
    body+='''<p class="gazette-archive-meta">Research paused indefinitely on November 24, 2026. This edition preserves the findings and unresolved questions without restarting the project. Historical reports are not automatically mathematical proofs; see <a href="guides/corrections.html">the corrections</a>.</p>
</section></div>'''
    return body
