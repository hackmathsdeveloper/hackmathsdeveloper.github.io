
Yes—**every root of a nonzero polynomial of finite degree with rational, integer, or algebraic coefficients is algebraic**, hence not transcendental. What Galois theory determines is not whether the roots exist or are algebraic, but whether they can be written using finitely many arithmetic operations and radicals. For a separable polynomial over \(\mathbb{Q}\), this happens exactly when its Galois group is solvable. [en.wikipedia](https://en.wikipedia.org/wiki/Algebraic_number)

For example, \(x^5-6x+3\) is a quintic whose roots are algebraic but cannot be expressed by radicals; a standard proof identifies a nonsolvable Galois group (typically \(S_5\)).  In contrast, polynomials of degree \(5\) and above can certainly still be solvable by radicals—there is simply no formula by radicals that works for **all** polynomials of those degrees. [math.mit](https://math.mit.edu/research/highschool/primes/materials/2022/May/6-1-Guo-Lee-Seetharaman.pdf)

## Important distinction

- A **polynomial’s degree** is finite by definition for an ordinary polynomial, e.g. degree \(5\), \(6\), or \(9\).
- A root \(\alpha\) of a nonzero \(f(x)\in\mathbb{Q}[x]\) is **algebraic over \(\mathbb{Q}\)**.
- A **transcendental** number such as \(\pi\) or \(e\) is not a root of any nonzero polynomial in \(\mathbb{Q}[x]\).
- “Not solvable by radicals” does **not** mean “transcendental.” It means there is no expression using rational numbers, \(+,-,\times,\div\), and finitely many \(n\)-th roots that produces all roots.
- For degree \(2,3,4\), every polynomial over \(\mathbb{Q}\) is solvable by radicals. For every degree \(n\ge5\), there are both solvable and nonsolvable examples. [core.ac](https://core.ac.uk/download/212814013.pdf)

## 50 Galois-theory questions

### Foundations

1. Define the splitting field of \(f(x)=x^3-2\) over \(\mathbb{Q}\), and compute its degree over \(\mathbb{Q}\).

2. Find the splitting field of \(x^4-2\) over \(\mathbb{Q}\). Which roots of unity must be adjoined?

3. What is the difference between a field extension \(L/K\), a normal extension, and a Galois extension?

4. State the Fundamental Theorem of Galois Theory for a finite Galois extension \(L/K\).

5. For \(f(x)=x^3-2\), describe the action of \(\operatorname{Gal}(f/\mathbb{Q})\) on its three roots.

6. Prove that the splitting field of \(x^3-2\) over \(\mathbb{Q}\) has Galois group isomorphic to \(S_3\).

7. Compute \(\operatorname{Gal}(\mathbb{Q}(\sqrt{2},\sqrt{3})/\mathbb{Q})\), and list all intermediate fields.

8. Let \(L=\mathbb{Q}(\sqrt [oeis](https://oeis.org/wiki/Algebraic_numbers){2},\omega)\), where \(\omega=e^{2\pi i/3}\). Find all automorphisms of \(L\) that fix \(\mathbb{Q}\).

9. Why does irreducibility of a polynomial over \(\mathbb{Q}\) imply transitivity of its Galois group on the roots?

10. Give an example of a reducible polynomial whose splitting field nevertheless has a nontrivial Galois group.

11. Explain why every finite extension of \(\mathbb{Q}\) is separable.

12. Define the minimal polynomial of an algebraic number. Find the minimal polynomial of \(\sqrt{2}+\sqrt{3}\) over \(\mathbb{Q}\).

13. Show that \(\mathbb{Q}(\sqrt{2}+\sqrt{3})=\mathbb{Q}(\sqrt{2},\sqrt{3})\).

14. Determine the degree \([\mathbb{Q}(\sqrt [core.ac](https://core.ac.uk/download/212814013.pdf){2},i):\mathbb{Q}]\).

15. What is the discriminant of a polynomial, and what information can its square class provide about the Galois group?

### Solvable groups and radicals

16. Define a solvable group using the derived series.

17. Show that every finite abelian group is solvable.

18. Show that \(S_3\) is solvable by writing down a normal series with abelian quotients.

19. Explain why \(S_5\) is not solvable.

20. Why is \(A_5\) simple and nonabelian, and why does this obstruct solvability by radicals?

21. State the Galois-theoretic criterion for a separable polynomial over \(\mathbb{Q}\) to be solvable by radicals.

22. What is a radical extension? How does it differ from an arbitrary finite algebraic extension?

23. Explain why adjoining an \(n\)-th root does not necessarily create a Galois extension.

24. Why are roots of unity important in the proof connecting radical extensions with solvable Galois groups?

25. Show that \(x^n-a\) is solvable by radicals over a field containing the relevant \(n\)-th roots of unity.

26. Is every polynomial with an abelian Galois group solvable by radicals? Explain why.

27. Is every polynomial with a solvable Galois group solvable by radicals? State any needed hypotheses.

28. Give an example of an algebraic number that is not expressible by radicals over \(\mathbb{Q}\).

29. Explain the difference between “a polynomial is solvable in radicals” and “its individual roots are algebraic.”

30. Why does Abel–Ruffini say there is no general radical formula for degree \(n\ge5\), rather than saying every degree-\(n\) equation is impossible to solve by radicals?

### Quintics

31. Factor and solve by radicals
   \[
   x^5-2x^3-2x^2+4=0.
   \]
   What does this example show about quintics?

32. Solve
   \[
   x^5-32=0
   \]
   by radicals, including all five complex roots.

33. Determine the splitting field and Galois group of
   \[
   x^5-2
   \]
   over \(\mathbb{Q}\). Is the group solvable?

34. Explain why
   \[
   x^5-2
   \]
   is solvable by radicals even though its splitting field may have degree \(20\).

35. For
   \[
   f(x)=x^5-6x+3,
   \]
   outline a strategy to prove irreducibility over \(\mathbb{Q}\).

36. For
   \[
   f(x)=x^5-6x+3,
   \]
   factor \(f\) modulo several primes and use the factorization patterns to infer possible cycle types in its Galois group.

37. Explain how finding a transposition and a 5-cycle in a transitive subgroup of \(S_5\) can help prove that the group is \(S_5\).

38. If an irreducible quintic has Galois group \(S_5\), why is it not solvable by radicals?

39. If an irreducible quintic has Galois group \(A_5\), why is it not solvable by radicals?

40. Give a solvable irreducible quintic over \(\mathbb{Q}\), such as a cyclotomic example, and determine its Galois group.

### Degrees 6–9

41. Solve
   \[
   x^6-2=0
   \]
   by radicals. Describe its splitting field over \(\mathbb{Q}\) and identify the roots of unity involved.

42. Explain why the degree-six polynomial
   \[
   x^6-2x^3+1=0
   \]
   can be solved by first substituting \(y=x^3\). Carry the solution through explicitly.

43. Let
   \[
   f(x)=x^6-2.
   \]
   Is its Galois group necessarily a subgroup of \(S_6\)? Why can the polynomial still be solvable by radicals?

44. Give an example of a sextic that factors into a quadratic and quartic over \(\mathbb{Q}\), then solve it by radicals using the lower-degree formulas.

45. For the cyclotomic polynomial
   \[
   \Phi_7(x)=x^6+x^5+x^4+x^3+x^2+x+1,
   \]
   determine its splitting field and Galois group over \(\mathbb{Q}\). Why is it solvable by radicals?

46. Solve
   \[
   x^7-2=0
   \]
   by radicals. What is the degree of its splitting field over \(\mathbb{Q}\), and why is the associated Galois group solvable?

47. Consider
   \[
   x^8-16=0.
   \]
   Find all roots and express them using radicals and roots of unity.

48. Solve
   \[
   x^8-10x^4+9=0
   \]
   by setting \(y=x^4\). Explain why this degree-eight equation is nevertheless solvable by radicals.

49. Solve
   \[
   x^9-8=0
   \]
   by radicals. How do the ninth roots of unity organize the full set of roots?

50. Let
   \[
   f(x)=x^9-3x^3+1.
   \]
   Use the substitution \(y=x^3\) to reduce the problem to a cubic. Solve the cubic by radicals and then recover the nine values of \(x\).

## Suggested investigation pattern

For a specific polynomial \(f(x)\in\mathbb{Q}[x]\), a practical Galois-theory workflow is:

1. **Factor over \(\mathbb{Q}\)** using rational-root tests, Eisenstein’s criterion, reduction modulo primes, or computer algebra.

2. **Check separability**. Over \(\mathbb{Q}\), this amounts to checking that \(f\) has no repeated roots, equivalently \(\gcd(f,f')=1\).

3. **Determine or constrain the Galois group**:
   - irreducibility gives transitivity;
   - factorization modulo primes reveals cycle types;
   - the discriminant tells whether the group lies inside an alternating group;
   - resolvent polynomials can distinguish remaining candidate groups.

4. **Test group solvability**. If \(\operatorname{Gal}(f/\mathbb{Q})\) has a composition factor \(A_n\) for \(n\ge5\), especially if it is \(A_5\) or \(S_5\), the polynomial is not solvable by radicals.

5. **Construct radicals only after solvability is known**, or exploit structure early—for example \(x^{mn}-a\), cyclotomic polynomials, compositions \(g(x^k)\), and polynomials that visibly factor into degrees at most four.

A useful caution: although the roots of every nonconstant \(f\in\mathbb{Q}[x]\) are algebraic, a degree-\(9\) polynomial can have Galois group \(S_9\), which is nonsolvable. Its roots are therefore algebraic but not expressible by radicals. The same phenomenon first appears generically in degree \(5\). [en.wikipedia](https://en.wikipedia.org/wiki/Algebraic_number)
