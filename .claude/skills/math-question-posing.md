---
name: math-question-posing
description: Generate new, creative mathematical questions from an existing problem, theorem, or topic using established problem-posing frameworks (Brown & Walter's "What-If-Not", reverse engineering, extremal pushing, generalize/specialize, etc). Use this whenever the user wants fresh variants of a math problem, help writing olympiad/competition questions, ways to extend or remix a known result, a richer problem set from one seed problem, or is stuck trying to "make up" original math questions. Trigger even if the user just says something like "give me new ways to ask this" or "how can I vary this problem" — this is exactly the design workflow this skill exists for.
---

# Math Question Posing

A skill for turning one known problem, theorem, or topic into a set of new, well-formed mathematical questions — using repeatable problem-posing frameworks rather than raw inspiration. This is a craft, not a lucky-strike: every technique below is a lever you can pull deliberately on any starting point.

## When to use which mode

- **Reference mode** — the user wants to understand or be reminded of the techniques themselves ("what are some ways to generate new math problems?"). Just explain the relevant technique(s) from the library below.
- **Generation mode** — the user gives (or points to) a seed problem/theorem/topic and wants actual new questions produced. Run the workflow below and return structured output.

Default to generation mode whenever a concrete seed problem or topic is present in the request, even if the user didn't ask for a specific technique by name.

## The technique library

The unifying principle across all of these is **deliberate perturbation**: take something known, change exactly one thing about it, and ask what happens. Creativity here is mostly a matter of making a problem's implicit assumptions explicit — and then denying them, one at a time.

1. **What-If-Not (Brown & Walter)** — the canonical, systematic method. List every attribute of the seed (assumptions, constraints, given conditions), then negate/remove/alter one at a time. "What if this weren't a right triangle? What if the field weren't real?" Cycle repeatedly for increasing depth.
2. **Reverse engineering** — give an answer, ask what question(s) produce it. Forces exploration of the whole space of problems mapping to that result, and exposes which constraints are necessary vs. merely sufficient.
3. **Push to the extremes** — exhaust one problem: vary parameters toward limiting/boundary cases (n → ∞, a dimension collapsing to zero), remove a constraint and ask if the result survives, add a constraint and ask what new structure appears, restate in an equivalent form. Results that survive most perturbations but fail at one boundary are often the richest.
4. **Disguise and repurpose** — take a neat, well-known fact and reframe it in a setting where the truth isn't obviously the same fact. Change the data, change what's asked for, change the domain (geometry → number theory, algebra → combinatorics). The solver rediscovers a known result by a non-obvious path.
5. **Invert closed → open** — replace a single-answer question with one admitting a family of answers, shifting the task from computation to characterization. "Find the area of this 8×3 rectangle" → "how many rectangles have area 24?"
6. **Generalize and specialize** — specialize: solve a simpler/more specific case first, then ask what pattern generalizes. Generalize: take a specific result and ask what broader conditions preserve it ("does this extend to higher dimensions? other rings? non-commutative settings?"). Every general theorem also invites a search for sharpness — is the hypothesis necessary, what's the counterexample when relaxed?
7. **Ask before the method** — pose the question before teaching/applying the standard technique, so intuition runs first (conjecture-before-proof). Fermi-style estimation questions serve the same purpose: they open reasoning up rather than closing it down with a single expected method.
8. **Cross-domain translation** — restate the problem in another field's language (algebraic identity → geometric construction, divisibility question → group action, probability statement → combinatorics). The translation itself is the creative act, and sometimes reveals two "different" problems are the same problem.

## Generation workflow

When given a seed (problem, theorem, or topic), work through these steps:

### 1. Pin down the seed
Restate the seed problem/theorem precisely and list its attributes explicitly: given conditions, implicit assumptions, the domain/structure it lives in, what's being asked for. This attribute list is the raw material every technique operates on — do this even in your head, but for non-trivial seeds write it out, since half of What-If-Not is just noticing an assumption was there at all.

### 2. Select techniques
Pick 2–4 techniques from the library that fit the seed and the user's evident goal (e.g. competition prep favors What-If-Not + push-to-extremes + generalize/specialize; a "make this feel deep" request favors disguise-and-repurpose + cross-domain translation). If the user asked for a specific technique, use only that one. If unsure, default to a spread across different techniques rather than several variants of the same one — variety is the point.

### 3. Generate candidates
For each selected technique, produce 1–3 new questions. Actually solve or sanity-check each one enough to confirm it's well-posed (has an answer, isn't vacuous, isn't secretly identical to the seed). Discard anything that doesn't survive this check rather than presenting it.

### 4. Tag each question
For every surviving question, assign:
- **Technique used** — which of the 8 above (or a named combination, e.g. "What-If-Not + generalize").
- **Difficulty relative to the seed** — `easier`, `comparable`, or `harder`, plus a one-line reason (e.g. "harder — drops a constraint that did most of the work in the original proof").

### 5. Present as structured output
Use this format:

```
## [Seed problem, restated in one line]

### 1. [New question text]
- **Technique:** [technique name]
- **Difficulty:** [easier / comparable / harder] — [one-line reason]
- **Note:** [optional: what's interesting about this variant, or a hint at its answer/approach]

### 2. [New question text]
...
```

Order candidates roughly easiest → hardest unless the user asked for something else (e.g. grouped by technique). If a generated question turns out to be open or research-level rather than solvable, say so explicitly rather than presenting it as routine.

## Worked example (olympiad level, ages 12–14)

**Seed:** In a triangle, the sum of any two sides is greater than the third side (triangle inequality). Given sides of length 5 and 9, find the range of possible values for the third side.

**Applying the workflow:**

### 1. Attributes of the seed
Three positive lengths; the constraint is pairwise sum > third side; two side lengths are given as fixed numbers; the question asks for a range (already somewhat open).

### 2. Techniques selected
What-If-Not (vary the shape constraint), generalize (n-gon instead of triangle), reverse engineering (given the range, find the sides), push-to-extremes (degenerate boundary case).

### 3–5. Structured output

```
## Seed: Given two triangle sides 5 and 9, find the range of the third side.

### 1. What if it's a quadrilateral instead of a triangle?
Given three sides of a quadrilateral (5, 9, and 7), find the range of possible values
for the fourth side.
- **Technique:** Generalize (triangle → n-gon)
- **Difficulty:** harder — the polygon inequality generalizes cleanly, but students
  must first realize *why* it generalizes (convexity isn't required, only that each
  side is less than the sum of the others).

### 2. What if you're given the range instead of the sides?
Find all pairs of positive integers (a, b) such that a triangle with sides a, b, and 9
has third-side range exactly 4 < c < 14.
- **Technique:** Reverse engineering
- **Difficulty:** comparable — same inequality, but now solved backward, which exposes
  that only |a − b| and a + b matter, not a and b individually.

### 3. What if one side is allowed to degenerate?
As the third side approaches its lower bound of 4, what happens to the triangle's
shape and area?
- **Technique:** Push to the extremes
- **Difficulty:** easier computation, but conceptually new — introduces the idea of a
  degenerate ("flat") triangle and area → 0 as a limiting case, a first taste of
  continuity arguments.

### 4. What if not all three inequalities need to hold at once?
Suppose you only require 5 + 9 > c (dropping the other two triangle inequalities).
What third-side values does this weaker condition allow, and why is it not sufficient
on its own?
- **Technique:** What-If-Not (remove a constraint) + generalize/sharpness
- **Difficulty:** comparable — same algebra, but the point is conceptual: it shows
  which of the three pairwise inequalities is actually doing the work at each boundary.
```

## Notes

- Always solve/verify before presenting — a beautifully-posed but broken question undermines the whole exercise.
- Prefer variety of technique over volume of questions; 4 well-chosen variants beat 10 near-duplicates.
- When a seed is very simple (a single computation), lean on Invert-closed-to-open and Reverse-engineering first — these are the two techniques most reliable at turning arithmetic into structure.
- When the audience is stated (e.g. competition level, grade level), let it guide technique selection and the difficulty tags, but don't invent an audience if none was given — ask, or default to "comparable to the seed's apparent level."
