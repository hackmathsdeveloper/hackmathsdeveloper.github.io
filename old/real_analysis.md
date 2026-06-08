
# Real Analysis: Proof Techniques Roadmap & Counterexample Library

This guide is structured around how expert analysts teach and learn the subject: **progressive abstraction, hypothesis stress-testing, and quantifier discipline**. Use it as a living document: annotate each technique, collect your own proof drafts, and update the counterexample log as you encounter new edge cases.

---

## 🗺️ I. Study Roadmap (Phase-by-Phase Progression)

| Phase | Core Topics | Proof Techniques Introduced | Mastery Milestone |
|-------|-------------|-----------------------------|-------------------|
| **1. Foundations & Quantifiers** | Logic, sets, real number axioms, sup/inf, completeness | Direct proof, contradiction, quantifier manipulation, sup/inf arguments | Prove √2 is irrational; show every nonempty bounded-above set has a least upper bound |
| **2. Sequences & Series** | Convergence, Cauchy criterion, monotone convergence, series tests | Squeeze theorem, tail estimates, comparison strategies, index shifting | Prove Bolzano-Weierstrass in ℝ; classify conditional vs absolute convergence |
| **3. Limits & Continuity** | ε-δ limits, sequential characterization, uniform continuity, intermediate/extreme value theorems | ε-δ construction, bounding/triangle inequality, contradiction via sequences | Prove continuity of polynomials; show f(x)=1/x is not uniformly continuous on (0,1) |
| **4. Differentiation & Integration** | Mean Value Theorem, Darboux property, Riemann sums, integrability criteria | Partition refinement, upper/lower sum estimates, derivative limit manipulation | Prove FTC Part 1; construct a continuous nowhere-differentiable function sketch |
| **5. Topology & Compactness** | Open/closed sets, metric spaces, compactness, connectedness, Arzelà-Ascoli (intro) | Open cover extraction, subsequence diagonalization, finite subcover bounding, uniform convergence swaps | Prove Heine-Borel; show continuous image of compact is compact; justify limit/integral swap |

**Dependency Rule:** Do not advance until you can *reproduce* the core proofs of the current phase from memory, and *explain why each hypothesis is necessary* using a counterexample.

---

## 🧰 II. Core Proof Techniques: Templates & Strategies

### 1. ε-δ & ε-N Proofs
- **Purpose:** Rigorously verify limits, continuity, uniform continuity.
- **Logical Structure:** `∀ε>0 ∃δ>0 ∀x (0<|x−a|<δ ⇒ |f(x)−L|<ε)`
- **Key Moves:**
  1. Work backward from `|f(x)−L| < ε` to isolate `|x−a|`
  2. Restrict δ (e.g., `δ ≤ 1`) to bound nuisance terms
  3. Use triangle inequality, monotonicity, or algebraic factorization
  4. Define δ explicitly as `min(1, ε/C)` where C bounds the remaining factor
- **Pitfalls:** Forgetting to handle `x=a` in continuity; letting δ depend on x (breaks uniformity); dropping quantifier order.
- **Template Phrase:** `Let ε>0. Choose δ = min(1, ε/M). Assume 0<|x−a|<δ. Then |f(x)−L| ≤ M|x−a| < M·(ε/M) = ε.`

### 2. Convergence & Cauchy Arguments
- **Purpose:** Prove sequence/series convergence without knowing the limit.
- **Logical Structure:** `∀ε>0 ∃N ∀n,m≥N |aₙ−aₘ|<ε`
- **Key Moves:**
  1. Identify structure: monotone + bounded → MCT; positive terms → comparison; alternating → Leibniz
  2. Bound tails using integrals, geometric series, or telescoping
  3. For series: split into partial sums; estimate remainder
  4. Use `|aₙ| ≤ |aₙ−L| + |L|` to pass from convergence to boundedness
- **Pitfalls:** Assuming bounded ⇒ convergent; misapplying ratio test when limit=1; ignoring domain of comparison functions.
- **Template Phrase:** `Let ε>0. Since (aₙ) is Cauchy, ∃N s.t. ∀n,m≥N, |aₙ−aₘ|<ε. Fix m=N and let n→∞ to obtain |aₙ−L|≤ε.`

### 3. Compactness Arguments
- **Purpose:** Convert local/global properties, guarantee extrema, swap limits.
- **Logical Structure:** In ℝⁿ: `Closed + Bounded ⇔ Sequentially Compact ⇔ Compact (finite subcover)`
- **Key Moves:**
  1. Extract convergent subsequence (Bolzano-Weierstrass)
  2. Assume non-compactness → construct open cover with no finite subcover → contradiction
  3. Use compactness to bound quantities uniformly (e.g., `|f(x)| ≤ M` on K)
  4. Combine with continuity to upgrade pointwise → uniform properties
- **Pitfalls:** Assuming closed ⇒ compact; forgetting that compactness is topological, not metric-dependent in general spaces; misusing sequential vs open-cover definitions in non-metric spaces.
- **Template Phrase:** `Since K is compact, the open cover {Uₓ} has a finite subcover {U₁,…,Uₖ}. Let M = max{M₁,…,Mₖ}. Then ∀x∈K, |f(x)|≤M.`

### 4. Supremum/Infimum & Completeness
- **Purpose:** Handle bounded sets, prove existence without construction.
- **Key Moves:** Use ε-characterization: `s = sup S ⇔ (i) ∀x∈S, x≤s; (ii) ∀ε>0 ∃x∈S s.t. x>s−ε`
- **Template:** To show `sup(A+B) = sup A + sup B`, prove `≤` by definition, then use (ii) to get `≥`.

### 5. Uniform Convergence Swaps
- **Purpose:** Justify `lim ∫ = ∫ lim`, `lim fₙ' = (lim fₙ)'`, continuity preservation.
- **Key Moves:** 
  1. Prove uniform convergence via Weierstrass M-test or ε-N with x-independent N
  2. Split difference: `|∫fₙ − ∫f| ≤ ∫|fₙ−f| ≤ (b−a)·sup|fₙ−f|`
  3. For derivatives: require `fₙ'` uniformly convergent + `fₙ(x₀)` convergent
- **Pitfall:** Assuming pointwise convergence suffices for limit swaps.

---

## 📚 III. Counterexample Library: Hypothesis-Drop Scenarios

*Structure per entry:* **Theorem → Dropped Hypothesis → Counterexample → Why It Matters**

### 🔹 Limits & Continuity
| Theorem | Dropped Hypothesis | Counterexample | Why It Matters |
|---------|-------------------|----------------|----------------|
| Continuous on `[a,b]` ⇒ uniformly continuous | Compact domain | `f(x)=1/x` on `(0,1)` | Shows uniform continuity is a *global* property; fails near boundary singularities |
| `fₙ → f` pointwise, `fₙ` continuous ⇒ `f` continuous | Uniform convergence | `fₙ(x)=xⁿ` on `[0,1]` | Pointwise limits can create jumps; uniform convergence preserves continuity |
| `f` differentiable at `c` ⇒ `f` continuous at `c` | Differentiability | `f(x)=|x|` at `0` | Continuity is strictly weaker; cusp breaks derivative but not limit |

### 🔹 Differentiation
| Theorem | Dropped Hypothesis | Counterexample | Why It Matters |
|---------|-------------------|----------------|----------------|
| `f'` exists on `(a,b)` ⇒ `f'` is continuous | Continuity of derivative | `f(x)=x²sin(1/x)` (0 at 0) | Derivatives satisfy Darboux property but need not be continuous |
| Mean Value Theorem | Continuity on `[a,b]` | `f(x)=1/x` on `[-1,1]` (undefined at 0) or step function | MVT requires connected domain + continuity; breaks with jumps/asymptotes |
| `f'(c)>0` ⇒ `f` increasing near `c` | `f'` continuous near `c` | `f(x)=x + 2x²sin(1/x)` at 0 | Derivative can be positive at a point but oscillate wildly nearby |

### 🔹 Sequences & Series
| Theorem | Dropped Hypothesis | Counterexample | Why It Matters |
|---------|-------------------|----------------|----------------|
| Cauchy sequence ⇒ convergent | Completeness of space | `aₙ = (1+1/n)ⁿ` in `ℚ` | Convergence depends on space; ℚ lacks limit points for irrationals |
| Absolutely convergent ⇒ convergent | Absolute convergence | `∑(-1)ⁿ/n` | Conditional convergence relies on cancellation; fragile under rearrangement |
| Rearrangement preserves sum | Absolute convergence | Riemann rearrangement of `∑(-1)ⁿ/n` | Order matters for conditional series; absolute convergence removes this dependence |
| Bounded monotone ⇒ convergent | Monotonicity | `aₙ = (-1)ⁿ(1−1/n)` | Boundedness alone doesn't prevent oscillation |

### 🔹 Integration
| Theorem | Dropped Hypothesis | Counterexample | Why It Matters |
|---------|-------------------|----------------|----------------|
| Continuous ⇒ Riemann integrable | Continuity | Dirichlet function: `1_ℚ` on `[0,1]` | Riemann integral fails when discontinuities are dense; motivates Lebesgue |
| `fₙ → f` pointwise ⇒ `∫fₙ → ∫f` | Uniform convergence / Dominated convergence | `fₙ(x)=n·1_{(0,1/n)}` on `[0,1]` | Mass can escape to infinity or concentrate; need uniform/DCT control |
| `F(x)=∫ₐˣ f` ⇒ `F'=f` | Continuity of `f` | `f(x)=0` for `x<0`, `1` for `x≥0` | FTC requires continuity at point; jump discontinuities break differentiability of integral |

### 🔹 Compactness & Topology
| Theorem | Dropped Hypothesis | Counterexample | Why It Matters |
|---------|-------------------|----------------|----------------|
| Closed + bounded ⇒ compact (ℝⁿ) | Boundedness | `ℤ ⊂ ℝ` | Unbounded closed sets lack convergent subsequences |
| Closed + bounded ⇒ compact | Closedness | `(0,1) ⊂ ℝ` | Missing boundary points allow sequences to "escape" |
| Continuous image of compact is compact | Compact domain | `f(x)=1/x` on `(0,1)` | Image can be unbounded or non-closed |
| Nested intervals with `|Iₙ|→0` have unique intersection | Closed intervals | `Iₙ=(0,1/n)` | Intersection empty without closed endpoints |

---

## 🧠 IV. Expert-Recommended Mastery Framework

### 1. Quantifier Discipline
- Write out `∀, ∃` explicitly before starting any proof.
- Track dependencies: `δ` may depend on `ε` and `a`, but **not** on `x` for uniform continuity.
- Practice negating statements: `¬(∀ε∃δ∀x...) ≡ ∃ε∀δ∃x...`

### 2. Proof Construction Workflow
1. **Identify goal type** (limit, existence, inequality, equivalence)
2. **List hypotheses** and mark which are topological, algebraic, or metric
3. **Choose technique** from roadmap (ε-δ, compactness, sup/inf, etc.)
4. **Work backward** on scratch paper, then write forward cleanly
5. **Stress-test**: Remove one hypothesis → does proof break? Where? → Find counterexample

### 3. Counterexample Practice
- Keep a "Hypothesis Log": For each theorem, record what happens if you drop each condition.
- Reverse-engineer: Given a counterexample, identify the minimal hypothesis that would fix it.
- Use counterexamples to sharpen intuition: They reveal the *geometry* behind analytic conditions.

### 4. Recommended Resources & Study Rhythm
| Resource | Strength | How to Use |
|----------|----------|------------|
| Abbott, *Understanding Analysis* | Intuition + clear proofs | Read actively; pause to reconstruct proofs before checking |
| Tao, *Analysis I & II* | Rigorous, builds from foundations | Do every exercise; focus on quantifier discipline |
| Pugh, *Real Mathematical Analysis* | Topology + visualization | Use for compactness/continuity intuition |
| Rudin, *Principles of Mathematical Analysis* | Concise, proof-dense | Reference for standard proofs; not for first exposure |
| **Self-Study Rhythm** | 3 sessions/week: 1 technique drill, 1 counterexample lab, 1 proof synthesis | Maintain a proof journal: date, theorem, technique, hypothesis drops, pitfalls |

---

## ✅ Quick-Reference Checklist

- [ ] Can I state the definition of limit/continuity with correct quantifier order?
- [ ] Can I convert between ε-δ, sequential, and topological definitions?
- [ ] Do I know when to use Cauchy vs Monotone Convergence?
- [ ] Can I prove that compact ⇒ sequentially compact ⇒ complete + totally bounded?
- [ ] For every theorem I learn, can I name a counterexample for each dropped hypothesis?
- [ ] Do I explicitly check whether δ/N/M depends on x before claiming uniformity?
- [ ] Can I swap `lim` and `∫` or `lim` and `d/dx` with proper justification?

---

**Final Note from Expert Pedagogy:**  
Real analysis mastery is not about memorizing proofs; it's about recognizing *structural patterns* and understanding *why hypotheses exist*. Counterexamples are not exceptions—they are the boundaries that define the theory. When stuck, ask: *"What fails if I remove this condition?"* The answer will often reveal the core mechanism of the proof.

If you'd like a printable version, spaced-repetition flashcards for the counterexamples, or worked proof templates for specific theorems (e.g., Heine-Borel, FTC, Arzelà-Ascoli), let me know your current focus area.
