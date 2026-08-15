
Good — that scopes it nicely. Here's a framework for an LLM-agent system that hunts for genuine mathematical discoveries across geometry and number theory, rather than just answering known questions.

## The core problem to solve first

Most "AI does math" demos fail at one of two things: agents hallucinating plausible-sounding but false patterns, or agents rediscovering trivia already in OEIS/Wikipedia and calling it novel. The plan below is built around avoiding both — heavy verification, and an explicit novelty-check step before anything gets called a "discovery."

## Pipeline architecture (multi-agent, LangGraph-shaped)

**1. Generator agent — conjecture proposal**
- Seeded with a domain (e.g. "lattice point counting in convex polygons," "multiplicative structure of prime gaps")
- Produces candidate statements in a structured form (formal-ish: quantifiers, objects, relation) rather than prose, so downstream agents can act on them mechanically
- Two modes worth running in parallel: (a) pattern-mining from data (see step 2) feeding hypotheses back up, and (b) analogy-transfer — take a known theorem in one area and propose the structurally analogous statement in another (e.g. transfer a Diophantine result to a Gaussian-integer analogue)

**2. Computational exploration agent**
- For number theory: brute-force sequence generation, feed into an OEIS lookup, run symbolic search (SymPy/PARI-GP) for closed forms, check against small counterexamples aggressively before anything moves forward
- For geometry: symbolic/numeric computation via SymPy, SageMath, or a CAS; for combinatorial geometry, generate random or exhaustive small configurations and measure invariants
- This agent's whole job is to try to kill the conjecture. Optimize for counterexample-finding, not confirmation — confirmation bias is the main failure mode of LLM-driven "discovery"

**3. Novelty-check agent**
- Before anything is treated as a real candidate: search OEIS, arXiv, Wikipedia, MathSciNet-adjacent sources (whatever's accessible) to check it isn't already known
- This step gets skipped by almost every "AI mathematician" demo and is why most of them produce nothing new

**4. Proof-attempt agent**
- Given a conjecture that survived counterexample search and is plausibly novel, attempt a formal or semi-formal proof
- Worth pairing with a proof assistant (Lean is the strongest current option) rather than trusting LLM-generated proof prose — an unverified "proof" from an LLM is close to worthless in this domain specifically, since these systems are notoriously good at writing convincing-looking but wrong proofs
- If full formalization is too heavy for your use case, at minimum require: independently-checkable proof steps, and a separate agent instance whose only job is adversarial proof-checking

**5. Critic/aggregator agent**
- Rejects anything that: fails novelty check, has a counterexample, has no proof attempt beyond "it seems to hold for small cases," or is a restatement of a known result with cosmetic changes

## Practical build order

1. Start narrow — pick one small domain (e.g. a specific class of Diophantine equations, or a specific polygon/lattice geometry question) and get the full pipeline working end-to-end before generalizing
2. Get the computational verification and OEIS/novelty-check agents solid first — these are the cheap, high-value, low-hallucination-risk parts
3. Add the generator agent once verification is trustworthy, so you're not drowning in unverified noise
4. Add Lean integration last — it's the highest-effort piece but the only thing that makes "proof" mean something

## Honest expectations

Genuinely novel, publishable-grade results are rare even for professional mathematicians doing this full-time; realistic outcomes for a system like this are: rediscovering known results (useful as a sanity check), finding small/incremental extensions of known results, and finding patterns in specific finite computational domains that are true-but-narrow (e.g. "true for all n < 10^6" without a proof). Occasionally something bigger — but that's the tail, not the median outcome.

Want me to go deeper on any one stage — e.g. concrete LangGraph node design, or which computational libraries fit each domain?
