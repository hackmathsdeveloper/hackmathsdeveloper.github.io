
This is a 26-minute VisualMath lecture called "What are...p-adic integers? Or: Climbing infinite trees" (June 30, 2021). It explains p-adic numbers by picturing them as infinite walks down a tree, then points toward the local-global principle as the payoff. It's a good intuitive introduction, but it's deliberately sketchy about the theorem itself, and there are a few verbal slips worth knowing about. [youtube](https://www.youtube.com/watch?v=FnfnlrHBABs)

One note before reading the transcript: the auto-captions write "p-adic" as "periodic" throughout. [youtube](https://www.youtube.com/watch?v=FnfnlrHBABs)

## How the video is built

| Segment | Content |
|---|---|
| Motivation | Solving polynomial equations over ℚ is hard. Solving them in another number system can tell you something about the original problem  [youtube](https://www.youtube.com/watch?v=FnfnlrHBABs). |
| Tree model | Fix a prime p. Each p-adic integer is an infinite walk down a tree that branches p ways at every node, one branch per remainder mod p. Digits are written right to left  [youtube](https://www.youtube.com/watch?v=FnfnlrHBABs). |
| Metric | Two walks that split at depth k are 1/pᵏ apart. A number with a long run of leading zeros is therefore close to 0  [youtube](https://www.youtube.com/watch?v=FnfnlrHBABs). |
| Arithmetic | Addition is ordinary column addition with carries in base p. In ℤ₇, −1 = …6666, which mirrors 1 = 0.999… in the reals. Multiplication is repeated addition  [youtube](https://www.youtube.com/watch?v=FnfnlrHBABs). |
| Formal definitions | ℤₚ is the inverse limit of ℤ/pⁿℤ, and ℚₚ is its field of fractions. Equivalently, ℚₚ is the completion of ℚ under the p-adic distance (Cauchy sequences modulo null sequences). Both are uncountable  [youtube](https://www.youtube.com/watch?v=FnfnlrHBABs). |
| Local-global principle | A rational solution always gives solutions in ℝ and in every ℚₚ. For "nice" equations, the converse also holds  [youtube](https://www.youtube.com/watch?v=FnfnlrHBABs). |
| Demo | A Mathematica demonstration runs Newton's method on x² − 2. It converges over ℝ for any start. Over the p-adics it works for p = 7 with starting value 3, and for p = 17 with starting value 6, but fails for p = 3 and p = 5  [youtube](https://www.youtube.com/watch?v=FnfnlrHBABs). |

## What works well

- The tree picture makes three facts feel obvious: ℤₚ is uncountable, it has a fractal shape, and its distance is ultrametric (two walks are as far apart as the point where they split).
- Comparing ℚₚ with ℝ, since both are completions of ℚ under different distances, is the right mental model.
- The −1 = …666 example shows how strange the p-adic world is while keeping it concrete.
- The Newton demo shows real analysis and p-adic analysis behaving differently. It also previews Hensel's lemma, which is linked in the description. [youtube](https://www.youtube.com/watch?v=FnfnlrHBABs)

## Gaps and slips

- The demo results look like luck in the video, but they follow from a simple rule. √2 exists in ℚₚ (for odd p) only when 2 is a square mod p. That's true for 7 (3² = 9 ≡ 2) and 17 (6² = 36 ≡ 2), and false for 3 and 5. Hensel's lemma then lifts a root mod p to a full p-adic root, as long as the derivative 2x isn't divisible by p. A root mod p also has to be the starting value, which is why the start matters.
- "Nice" is never defined. The precise statement is the Hasse–Minkowski theorem for quadratic forms, which the description links. Without that, the principle sounds more general than it is. It fails for cubics: Selmer's 3x³ + 4y³ + 5z³ = 0 has solutions in ℝ and every ℚₚ but no nontrivial rational solution. [youtube](https://www.youtube.com/watch?v=FnfnlrHBABs)
- The distance example appears to be off by one power. Walks …202 and …201 match at depths 0 and 1 and first differ at depth 2, so they should be 3⁻² apart, not the stated 1/3. This depends on how the slide indexes depth, which the transcript doesn't show.
- He says "with multiplication you have a subtraction." He means that addition gives you subtraction.
- Division is skipped. The key fact is that an element of ℤₚ is invertible exactly when its last digit is nonzero. That's also why ℚₚ only needs finitely many digits after the point.

## Try it yourself

This short Python snippet runs the same Newton/Hensel iteration and checks the demo's results:

```python
def sqrt2_padic(p, x0, k=8):
    m = p**k
    x = x0
    for _ in range(k):
        x = (x - (x*x - 2) * pow(2*x, -1, m)) % m
    return x, (x*x - 2) % m == 0

for p, x0 in [(7, 3), (17, 6)]:
    print(p, sqrt2_padic(p, x0))
```

For p = 3 or 5 the iteration fails: 2x can stop being invertible mod p, or the result never squares to 2 mod pᵏ. That matches the video.

For going further, the description links Tyler Hyde's notes, David Madore's notes, and MIT 18.782 Lecture 4, which cover the rigorous versions of these ideas. [youtube](https://www.youtube.com/watch?v=FnfnlrHBABs)
