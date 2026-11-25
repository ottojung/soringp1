# antonina-glctZ6qEsYh7VOZlfGs0cA-astounded

Session: ses_e47384152ffeeJ5p4UPOyn9lF5
Workspace: /home/lubko/soring-fronts/exec-lemmaA-core-20261108
Created: 1794101460671; updated: 1794101588875

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 37 (msg_1b8c9a4ee001NYgGD7EFzpakWU)

Given time constraints, I couldn't fully re-run the n=9 DP (the predecessor's process ended and no persisted artifact). But I did independently test the structural lifting question on n≤8 (all 6467 gap≥3 core cases: x-comparison succeeds) and identified that the 8 reported failures at n=9 are non-core-A cases (A=P−x not a core), so they don't contradict the inside-A induction. The open sub-lemma remains: for a core P with maximal x whose deletion A is also a core, show either an inside-A comparison or an x-comparison lifts by the gap; data supports it for n≤8, and the n=9 count of 8 failures needs the inside-A check (not yet run on n=9 due to DP time). Exact state: Lemma A verified computationally for n≤8 (and predecessor claims n=9); proof not closed; open sub-lemma is the gap-lifting step for core→core maximal insertion.
