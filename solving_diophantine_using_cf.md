
You typically use continued fractions to solve specific classes of Diophantine equations, most prominently linear equations \(ax + by = c\) and Pell-type equations \(x^2 - Dy^2 = N\). The precise method depends heavily on which type you have. [pi.math.cornell](https://pi.math.cornell.edu/~hatcher/TN/TNch2rev.pdf)

Since your query is generic, I’ll outline both patterns and give explicit worked examples.

***

## 1. Linear equations \(ax + by = c\)

Assume integers \(a,b,c\) with \(\gcd(a,b)\mid c\). Continued fractions here are essentially a structured way of running the extended Euclidean algorithm. [reddit](https://www.reddit.com/r/learnmath/comments/k9on7a/recreational_math_using_continued_fractions_to/)

### Idea

1. Reduce to \(ax + by = \gcd(a,b)\) by dividing by \(d = \gcd(a,b)\). [pi.math.cornell](https://pi.math.cornell.edu/~hatcher/TN/TNch2rev.pdf)
2. Express \(a/b\) (or \(b/a\)) as a simple continued fraction.  
3. Compute convergents; these give the coefficients you need to express \(\gcd(a,b)\) as an integer linear combination of \(a\) and \(b\). [pi.math.cornell](https://pi.math.cornell.edu/~hatcher/TN/TNch2rev.pdf)
4. Scale that particular solution to get a solution for general \(c\).

### Example: \(172x + 20y = 1000\)

From the reference, \(\gcd(172,20)=4\). So first solve [crypto-kantiana](https://crypto-kantiana.com/elena.kirshanova/teaching/science_tools_2020/tasks/040.pdf)
\[
172x + 20y = 4.
\]
Then multiply a particular solution by \(1000/4 = 250\). [crypto-kantiana](https://crypto-kantiana.com/elena.kirshanova/teaching/science_tools_2020/tasks/040.pdf)

1. Compute the continued fraction of \(172/20\).

Run Euclidean algorithm:
- \(172 = 8\cdot 20 + 12\)
- \(20 = 1\cdot 12 + 8\)
- \(12 = 1\cdot 8 + 4\)
- \(8 = 2\cdot 4 + 0\). [crypto-kantiana](https://crypto-kantiana.com/elena.kirshanova/teaching/science_tools_2020/tasks/040.pdf)

Thus
\[
\frac{172}{20} = [8;1,1,2].
\]

2. Compute convergents \(p_k/q_k\) of \([8;1,1,2]\). [pi.math.cornell](https://pi.math.cornell.edu/~hatcher/TN/TNch2rev.pdf)

Initial conditions:
- \(p_{-2}=0, p_{-1}=1\)
- \(q_{-2}=1, q_{-1}=0\). [pi.math.cornell](https://pi.math.cornell.edu/~hatcher/TN/TNch2rev.pdf)

For partial quotients \(a_0=8, a_1=1, a_2=1, a_3=2\),
\[
p_k = a_k p_{k-1} + p_{k-2},\quad q_k = a_k q_{k-1} + q_{k-2}.
\]

You obtain:
- \(k=0\): \(p_0=8, q_0=1 \Rightarrow 8/1\)
- \(k=1\): \(p_1=9, q_1=1 \Rightarrow 9/1\)
- \(k=2\): \(p_2=17, q_2=2 \Rightarrow 17/2\)
- \(k=3\): \(p_3=43, q_3=5 \Rightarrow 43/5\). [pi.math.cornell](https://pi.math.cornell.edu/~hatcher/TN/TNch2rev.pdf)

The last convergent \(p_3/q_3 = 172/20\) as expected (after simplifying).

3. Extract Bezout coefficients from the backwards substitution.

From the Euclidean steps: [crypto-kantiana](https://crypto-kantiana.com/elena.kirshanova/teaching/science_tools_2020/tasks/040.pdf)

- \(4 = 12 - 1\cdot 8\)
- \(8 = 20 - 1\cdot 12\)
- \(12 = 172 - 8\cdot 20\).

Substitute \(8\) into the first:
\[
4 = 12 - (20 - 1\cdot 12) = 2\cdot 12 - 20.
\]

Substitute \(12\) into that:
\[
4 = 2(172 - 8\cdot 20) - 20 = 2\cdot 172 - 17\cdot 20.
\]

So one solution to \(172x + 20y = 4\) is
\[
x_0 = 2,\quad y_0 = -17.[]
\]

4. Scale to get solution for \(1000\).

Multiply by \(250\):
\[
x = 2\cdot 250 = 500,\quad y = -17\cdot 250 = -4250.
\]

Check:
\[
172\cdot 500 + 20\cdot (-4250) = 86000 - 85000 = 1000.[]
\]

General solution:
\[
x = 500 + \frac{20}{4}t = 500 + 5t,\quad
y = -4250 - \frac{172}{4}t = -4250 - 43t,\quad t\in\mathbb{Z}.[]
\]

So the continued fraction here is just a structured way of packaging the extended GCD computation.

***

## 2. Pell-type equations \(x^2 - Dy^2 = N\)

Continued fractions become essential for Pell’s equation \(x^2 - Dy^2 = 1\) and variants \(x^2 - Dy^2 = \pm 1, \pm N\), \(D\) nonsquare. The key is the periodic continued fraction expansion of \(\sqrt{D}\). [isres](https://www.isres.org/books/chapters/CSBET2021_10_03-01-2022.pdf)

### Core facts

- If \(D\) is a nonsquare positive integer, \(\sqrt{D}\) has a periodic simple continued fraction \(\sqrt{D} = [a_0; \overline{a_1,\dots,a_\ell}]\). [isres](https://www.isres.org/books/chapters/CSBET2021_10_03-01-2022.pdf)
- Convergents \(p_k/q_k\) approximate \(\sqrt{D}\) and satisfy
  \[
  p_k^2 - D q_k^2 = (-1)^{k+1}r_k,
  \]
  where \(r_k\) is typically small; particular indices \(k\) give solutions of Pell-type equations. [sas.rochester](https://www.sas.rochester.edu/mth/undergraduate/honorspaperspdfs/maddox2025.pdf)

Standard results:

- If the period length \(\ell\) of \(\sqrt{D}\) is even, the convergent \(p_{\ell-1}/q_{\ell-1}\) gives the minimal solution to \(x^2 - Dy^2 = 1\). [isres](https://www.isres.org/books/chapters/CSBET2021_10_03-01-2022.pdf)
- If \(\ell\) is odd, then \(p_{2\ell-1}/q_{2\ell-1}\) gives the minimal solution to \(x^2 - Dy^2 = 1\), while \(p_{\ell-1}/q_{\ell-1}\) solves \(x^2 - Dy^2 = -1\). [isres](https://www.isres.org/books/chapters/CSBET2021_10_03-01-2022.pdf)

These give you a fundamental solution \((x_1,y_1)\); all other solutions can be generated via powers of the fundamental unit \(x_1 + y_1\sqrt{D}\). [sas.rochester](https://www.sas.rochester.edu/mth/undergraduate/honorspaperspdfs/maddox2025.pdf)

***

### Example: \(x^2 - 2y^2 = 1\)

1. Compute continued fraction of \(\sqrt{2}\).

We know (and can rederive) that
\[
\sqrt{2} = [1;\overline{2}] = [1;2,2,2,\dots].[]
\]
The period length is \(\ell=1\) (odd).

2. Compute convergents \(p_k/q_k\).

Partial quotients: \(a_0=1, a_k=2\) for \(k\ge 1\). [isres](https://www.isres.org/books/chapters/CSBET2021_10_03-01-2022.pdf)

Using the same recurrence, the first few convergents are:
- \(k=0\): \(1/1\)
- \(k=1\): \(3/2\)
- \(k=2\): \(7/5\)
- \(k=3\): \(17/12\)
etc. [isres](https://www.isres.org/books/chapters/CSBET2021_10_03-01-2022.pdf)

3. Select the right convergent.

The rule (period odd) says minimal solution for \(x^2 - 2y^2 = 1\) is \(k = 2\ell-1 = 1\) or \(2\ell\) depending on the precise convention; for \(\sqrt{2}\), check small convergents: [isres](https://www.isres.org/books/chapters/CSBET2021_10_03-01-2022.pdf)

- \(1^2 - 2\cdot 1^2 = -1\)
- \(3^2 - 2\cdot 2^2 = 9 - 8 = 1\).

So \((x_1,y_1) = (3,2)\) is the minimal solution to \(x^2-2y^2=1\). [isres](https://www.isres.org/books/chapters/CSBET2021_10_03-01-2022.pdf)

4. Generate all solutions.

Every solution is given by
\[
x_n + y_n\sqrt{2} = (3 + 2\sqrt{2})^n,\quad n\ge 1.[][]
\]

For example:
- \(n=1\): \((3,2)\)
- \(n=2\): \((3+2\sqrt{2})^2 = 17 + 12\sqrt{2}\Rightarrow (17,12)\)
- \(n=3\): \((3+2\sqrt{2})^3 = 99 + 70\sqrt{2}\Rightarrow (99,70)\), etc. [sas.rochester](https://www.sas.rochester.edu/mth/undergraduate/honorspaperspdfs/maddox2025.pdf)

Each pair \((x_n,y_n)\) satisfies \(x_n^2 - 2y_n^2 = 1\).

***

### Example: \(x^2 - 3y^2 = -1\)

1. \(\sqrt{3} = [1;\overline{1,2}] = [1;1,2,1,2,\dots]\), with period length \(\ell=2\) (even). [sas.rochester](https://www.sas.rochester.edu/mth/undergraduate/honorspaperspdfs/maddox2025.pdf)

Convergents:
- \(1/1\)
- \(2/1\)
- \(5/3\)
- \(7/4\)
- \(19/11\), etc. [sas.rochester](https://www.sas.rochester.edu/mth/undergraduate/honorspaperspdfs/maddox2025.pdf)

Check:
- \(2^2 - 3\cdot 1^2 = 4 - 3 = 1\)
- \(1^2 - 3\cdot 1^2 = -2\)
- \(5^2 - 3\cdot 3^2 = 25 - 27 = -2\)
- \(7^2 - 3\cdot 4^2 = 49 - 48 = 1\).

So minimal solution to \(x^2 - 3y^2=1\) is \((2,1)\), which matches the rule (period even; \(k=\ell-1=1\)). There is no integer solution to \(x^2 - 3y^2 = -1\) because the relevant convergents never give \(-1\); the continued fraction structure detects that. [sas.rochester](https://www.sas.rochester.edu/mth/undergraduate/honorspaperspdfs/maddox2025.pdf)

***

## 3. Quick comparison: linear vs Pell via CF

| Equation type             | Continued fraction object         | What convergents give                            | Typical outcome                          |
|---------------------------|------------------------------------|--------------------------------------------------|------------------------------------------|
| \(ax + by = c\)           | CF of \(a/b\) or \(b/a\)          | Bezout coefficients for \(\gcd(a,b)\)           | One particular solution, then parametrize [crypto-kantiana](https://crypto-kantiana.com/elena.kirshanova/teaching/science_tools_2020/tasks/040.pdf) |
| \(x^2 - Dy^2 = 1\)        | Periodic CF of \(\sqrt{D}\)       | Fundamental solution from certain period index   | All solutions by powers of fundamental unit [isres](https://www.isres.org/books/chapters/CSBET2021_10_03-01-2022.pdf) |
| \(x^2 - Dy^2 = -1,\pm N\) | Same CF of \(\sqrt{D}\)           | Some convergents solve variants if solvable      | Sometimes no solution; CF detects this [isres](https://www.isres.org/books/chapters/CSBET2021_10_03-01-2022.pdf) |

***
