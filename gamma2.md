
Here are 30 properties, tricks, and tips about the Gamma function, tuned for someone who will actually use them in analysis / asymptotics / probability rather than just memorize formulas.

***

## 1–6: Core definitions and basic identities

1. **Integral definition (Re\(z\) > 0)**  
   \(\Gamma(z) = \int_{0}^{\infty} t^{z-1} e^{-t}\, dt\) is the standard definition and the starting point for most analytic properties. [geeksforgeeks](https://www.geeksforgeeks.org/engineering-mathematics/gamma-function/)

2. **Domain of analyticity and poles**  
   The integral definition gives an analytic function on \(\text{Re}(z) > 0\), which can be meromorphically continued to \(\mathbb{C}\) with simple poles at \(z = 0,-1,-2,\dots\). [math.lsu](https://www.math.lsu.edu/system/files/WM1%20paper.pdf)

3. **Residues at negative integers**  
   At \(z = -n\) for \(n \in \mathbb{N}\cup\{0\}\), \(\Gamma(z)\) has a simple pole with residue  
   \(\operatorname{Res}_{z=-n}\Gamma(z) = \dfrac{(-1)^n}{n!}\). [math.lsu](https://www.math.lsu.edu/system/files/WM1%20paper.pdf)

4. **Factorial relation (discrete interpolation)**  
   For \(n \in \mathbb{N}\), \(\Gamma(n) = (n-1)!\), so \(\Gamma\) is the canonical analytic extension of the factorial from \(\mathbb{N}\) to \(\mathbb{C}\setminus\{0,-1,-2,\dots\}\). [britannica](https://www.britannica.com/science/gamma-function)

5. **Functional equation (recurrence)**  
   \(\Gamma(z+1) = z\Gamma(z)\) for all \(z\) away from poles; many manipulations reduce to repeatedly applying this recurrence (e.g., shifting arguments). [probabilitycourse](https://www.probabilitycourse.com/chapter4/4_2_4_Gamma_distribution.php)

6. **Special values at 1 and 1/2**  
   \(\Gamma(1) = 1\) and \(\Gamma\!\left(\tfrac{1}{2}\right) = \sqrt{\pi}\), the latter obtained via a Gaussian integral trick and used constantly in probability and analysis. [geeksforgeeks](https://www.geeksforgeeks.org/engineering-mathematics/gamma-function/)

***

## 7–11: Reflection, duplication, and related formulas

7. **Euler reflection formula**  
   \(\Gamma(z)\Gamma(1-z) = \dfrac{\pi}{\sin(\pi z)}\) for \(z \notin \mathbb{Z}\); this is your go-to for relating values at \(z\) and \(1-z\), and for converting trigonometric products into Gamma ratios. [math.libretexts](https://math.libretexts.org/Bookshelves/Analysis/Complex_Variables_with_Applications_(Orloff)/14:_Analytic_Continuation_and_the_Gamma_Function/14.02:_Definition_and_properties_of_the_Gamma_function)

8. **Legendre duplication formula**  
   \(2^{2z-1}\Gamma(z)\Gamma\!\left(z+\tfrac{1}{2}\right) = \sqrt{\pi}\,\Gamma(2z)\), extremely useful for reducing products of Gamma at half-offset arguments and in Beta/Binomial-type integrals. [wikiwand](https://www.wikiwand.com/en/articles/gamma_function)

9. **More general multiplication formula (Gauss)**  
   For positive integer \(m\), there is a multiplication formula expressing \(\Gamma(mz)\) in terms of \(\prod_{k=0}^{m-1}\Gamma\!\left(z+\frac{k}{m}\right)\); a special case is the duplication formula above. [wikiwand](https://www.wikiwand.com/en/articles/gamma_function)

10. **Using reflection to evaluate “awkward” arguments**  
    If you need \(\Gamma(-\tfrac{1}{2})\), use reflection with \(z=\tfrac{1}{2}\) to get \(\Gamma(-\tfrac{1}{2}) = -2\sqrt{\pi}\); this general trick converts many negative noninteger arguments into positive ones plus a sine factor. [geeksforgeeks](https://www.geeksforgeeks.org/engineering-mathematics/gamma-function/)

11. **Symmetry for complex conjugation**  
    For real-valued integrand in the defining integral, \(\Gamma(\bar{z}) = \overline{\Gamma(z)}\); this simplifies working with complex conjugate pairs in residues and contour integrals. [math.libretexts](https://math.libretexts.org/Bookshelves/Analysis/Complex_Variables_with_Applications_(Orloff)/14:_Analytic_Continuation_and_the_Gamma_Function/14.02:_Definition_and_properties_of_the_Gamma_function)

***

## 12–16: Product and series representations

12. **Weierstrass infinite product**  
    A standard representation is  
    \[
    \Gamma(z)^{-1} = z e^{\gamma z} \prod_{n=1}^{\infty}\left(1 + \frac{z}{n}\right)e^{-z/n},
    \]  
    where \(\gamma\) is Euler’s constant; very useful conceptually for uniqueness and growth estimates. [math.libretexts](https://math.libretexts.org/Bookshelves/Analysis/Complex_Variables_with_Applications_(Orloff)/14:_Analytic_Continuation_and_the_Gamma_Function/14.02:_Definition_and_properties_of_the_Gamma_function)

13. **Logarithmic derivative (digamma) via series**  
    Taking logs and differentiating gives  
    \(\psi(z) = \dfrac{\Gamma'(z)}{\Gamma(z)} = -\gamma + \sum_{n=0}^{\infty}\left(\dfrac{1}{n+1} - \dfrac{1}{n+z}\right)\),  
    which is often the most convenient representation for \(\psi\) in analysis. [wikiwand](https://www.wikiwand.com/en/articles/gamma_function)

14. **Higher derivatives (polygamma functions)**  
    Differentiating repeatedly yields integrals like  
    \(\Gamma^{(k)}(z) = \int_0^\infty t^{z-1} e^{-t} (\log t)^k\, dt\),  
    which give moments of \(\log T\) when \(T\) is Gamma-distributed. [math.lsu](https://www.math.lsu.edu/system/files/WM1%20paper.pdf)

15. **Logarithmic convexity (Bohr–Mollerup)**  
    \(\log \Gamma(x)\) is convex on \((0,\infty)\); together with the recurrence and normalization this characterizes \(\Gamma\) among positive functions on \((0,\infty)\). [mathsisfun](https://www.mathsisfun.com/numbers/gamma-function.html)

16. **Entire function \(1/\Gamma(z)\)**  
    While \(\Gamma(z)\) is meromorphic with simple poles at nonpositive integers, \(1/\Gamma(z)\) is entire and vanishes at the nonpositive integers; this is handy for constructing entire functions with prescribed zeros. [math.libretexts](https://math.libretexts.org/Bookshelves/Analysis/Complex_Variables_with_Applications_(Orloff)/14:_Analytic_Continuation_and_the_Gamma_Function/14.02:_Definition_and_properties_of_the_Gamma_function)

***

## 17–21: Asymptotics and growth

17. **Stirling’s formula (basic form)**  
    For large \(|z|\) with \(\text{Re}(z) > 0\),  
    \(\Gamma(z+1) \sim \sqrt{2\pi}\,z^{z+1/2} e^{-z}\).  
    This recovers \(n! \sim \sqrt{2\pi}\,n^{n+1/2}e^{-n}\) for integers. [wikiwand](https://www.wikiwand.com/en/articles/gamma_function)

18. **Refined Stirling expansion (log Gamma)**  
    One usually works with  
    \(\log \Gamma(z) = \left(z-\tfrac{1}{2}\right)\log z - z + \tfrac{1}{2}\log(2\pi) + O(1/z)\),  
    with known asymptotic series in descending powers of \(z\). [math.libretexts](https://math.libretexts.org/Bookshelves/Analysis/Complex_Variables_with_Applications_(Orloff)/14:_Analytic_Continuation_and_the_Gamma_Function/14.02:_Definition_and_properties_of_the_Gamma_function)

19. **Growth along rays**  
    Stirling’s formula shows that \(|\Gamma(\sigma + it)|\) grows roughly like \(|t|^{\sigma-1/2} e^{-\pi|t|/2}\) along vertical lines, which is crucial in complex analytic number theory and contour estimates. [math.libretexts](https://math.libretexts.org/Bookshelves/Analysis/Complex_Variables_with_Applications_(Orloff)/14:_Analytic_Continuation_and_the_Gamma_Function/14.02:_Definition_and_properties_of_the_Gamma_function)

20. **Practical numerical tip: use log-Gamma**  
    Because \(\Gamma(z)\) overflows quickly, compute \(\log \Gamma(z)\) numerically and exponentiate only when safe; many statistics libraries internally work with log-Gamma for this reason. [statlect](https://www.statlect.com/mathematical-tools/gamma-function)

21. **Monotonicity on positive reals**  
    For \(x>1\), \(\Gamma(x)\) grows quickly and is strictly increasing beyond a small region; combined with log-convexity this gives useful inequalities (e.g., bounding \(\Gamma\) between exponentials). [statlect](https://www.statlect.com/mathematical-tools/gamma-function)

***

## 22–26: Connections to Beta function, probability, and integrals

22. **Connection with Beta function**  
    The Beta function is \(B(x,y) = \int_0^1 t^{x-1}(1-t)^{y-1}\,dt\), and satisfies  
    \(B(x,y) = \dfrac{\Gamma(x)\Gamma(y)}{\Gamma(x+y)}\),  
    which lets you convert many Beta-type integrals into Gamma ratios. [mit](https://www.mit.edu/~jeffery/gamma_beta.pdf)

23. **Scaling integral trick**  
    For \(\alpha>0,\lambda>0\),  
    \(\int_0^\infty x^{\alpha-1} e^{-\lambda x}\,dx = \dfrac{\Gamma(\alpha)}{\lambda^\alpha}\);  
    this is a common trick for quickly evaluating Laplace-type integrals and normalizing densities. [probabilitycourse](https://www.probabilitycourse.com/chapter4/4_2_4_Gamma_distribution.php)

24. **Normalizing Gamma distribution**  
    The Gamma distribution with shape \(\alpha\) and rate \(\lambda\) has density  
    \(f(x) = \dfrac{\lambda^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\lambda x}\), \(x>0\);  
    the normalization follows directly from the scaling integral above. [probabilitycourse](https://www.probabilitycourse.com/chapter4/4_2_4_Gamma_distribution.php)

25. **Expectation and moments via Gamma ratios**  
    For \(X \sim \text{Gamma}(\alpha,\lambda)\),  
    \(E[X^k] = \dfrac{\Gamma(\alpha + k)}{\Gamma(\alpha)\lambda^k}\),  
    so many moment calculations reduce to using the recurrence \(\Gamma(z+1) = z\Gamma(z)\). [mit](https://www.mit.edu/~jeffery/gamma_beta.pdf)

26. **Gaussian integral as a Gamma special case**  
    The standard Gaussian integral \(\int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi}\) follows from the \(\Gamma(\tfrac{1}{2})\) evaluation, and many even-moment integrals of Gaussians boil down to \(\Gamma\) at half-integers. [mit](https://www.mit.edu/~jeffery/gamma_beta.pdf)

***

## 27–30: Practical tricks and tips in analysis / computation

27. **Use recurrence to move to a “good strip”**  
    For real \(x\), repeatedly apply \(\Gamma(x+1)=x\Gamma(x)\) or its inverse to shift \(x\) into a numerically stable region, e.g. \([1,2]\), then evaluate there and multiply by the product of \(x\pm k\). [britannica](https://www.britannica.com/science/gamma-function)

28. **Avoid poles with reflection and shifting**  
    When expressions feature \(\Gamma(z)\) near a negative integer, try to rewrite using reflection and recurrence so the Gamma arguments move away from the poles and you expand in terms of regular functions plus simple poles. [math.lsu](https://www.math.lsu.edu/system/files/WM1%20paper.pdf)

29. **Asymptotics of ratios**  
    Ratios like \(\dfrac{\Gamma(z+a)}{\Gamma(z+b)}\) appear constantly; from Stirling’s formula  
    \(\dfrac{\Gamma(z+a)}{\Gamma(z+b)} \sim z^{a-b}\) as \(|z|\to\infty\) with bounded argument, a very efficient way to estimate tail behaviour and simplify limits. [math.libretexts](https://math.libretexts.org/Bookshelves/Analysis/Complex_Variables_with_Applications_(Orloff)/14:_Analytic_Continuation_and_the_Gamma_Function/14.02:_Definition_and_properties_of_the_Gamma_function)

30. **Use log-convexity for inequalities**  
    Many inequalities for factorials and binomial coefficients are cleanly proven using the convexity of \(\log \Gamma\) on \((0,\infty)\); you can interpolate between integer points and then restrict back to \(\mathbb{N}\). [mathsisfun](https://www.mathsisfun.com/numbers/gamma-function.html)

***
