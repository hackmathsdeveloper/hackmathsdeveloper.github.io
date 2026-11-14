The transformation of the **Gregory-Leibniz series** into a **polynomial continued fraction** for $\pi$ is a classic demonstration of the **Euler transformation** at work. 

According to the sources, this process converts a series whose terms are rational functions of the index $n$ into a continued fraction where the elements are polynomial sequences.

### 1. The Starting Point: Gregory-Leibniz Series
The Gregory-Leibniz series for $\pi/4$ is defined as:
$$\frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \dots = \sum_{n=0}^{\infty} \frac{(-1)^n}{2n+1}$$
In this series, the terms are rational functions of the index $n$ where the denominator is a **linear function** ($2n+1$), representing a polynomial of **degree 1**.

### 2. The Euler Transformation
The sources define the **Euler transformation** as a method to equate an infinite series to a continued fraction:
$$\sum_{n \ge 0} a_n = a_0 + \frac{a_1}{1 + \frac{-a_2}{a_1 + a_2 + \frac{-a_1 a_3}{a_2 + a_3 + \dots}}}$$
If the terms of the original series are rational functions of $n$ of a fixed degree, the resulting continued fraction will have partial numerators with a degree at least **twice** that of the denominators.

### 3. Transformation into a Polynomial Continued Fraction
Applying this transformation to the Gregory-Leibniz series results in the continued fraction first published by **Lord Brouncker** in 1655:
$$\frac{4}{\pi} = 1 + \frac{1^2}{2 + \frac{3^2}{2 + \frac{5^2}{2 + \dots}}} = 1 + \mathbf{K}_{n=1}^\infty \frac{(2n-1)^2}{2}$$

This result demonstrates the polynomial nature of the transformation:
*   **Partial Numerators ($a_n$):** The sequence is $(2n-1)^2$, which is a **polynomial of degree 2**.
*   **Partial Denominators ($b_n$):** The sequence is the constant $2$, which is a polynomial of **degree 0**.

### 4. Analysis of the Phenomenon
The sources highlight this as a specific "phenomenon" of the Euler transformation:
*   **Degree Relationship:** Because the original series terms had a linear denominator (degree 1), the resulting continued fraction numerators are degree 2.
*   **Simplification:** The transformation takes the alternating rational terms and, through algebraic simplification, generates the squared odd integers as the numerator sequence of the continued fraction. 

A similar effect is noted for **Catalan's constant**, where a series with a degree 2 denominator transforms into a continued fraction where the numerator degree is four times that of the denominator.

