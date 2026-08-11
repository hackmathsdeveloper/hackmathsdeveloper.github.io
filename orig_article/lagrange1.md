
Lagrange multipliers solve an optimization problem **with an equality constraint**: maximize or minimize \(f(x_1,\ldots,x_n)\) while requiring \(g(x_1,\ldots,x_n)=c\). The key condition is

\[
\nabla f = \lambda \nabla g,
\]

meaning that, at a constrained optimum, the objective’s gradient is parallel to the constraint’s gradient. Geometrically, the best reachable contour of \(f\) just touches the feasible curve/surface rather than crossing it. [ocw.mit](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/d97c53ed0a6734b4bc266478fe6423c1_MIT18_02SC_notes_21.pdf)

Equivalently, form the Lagrangian

\[
\mathcal L(x,\lambda)=f(x)-\lambda\bigl(g(x)-c\bigr),
\]

then solve \(\nabla_{x,\lambda}\mathcal L=0\). The multiplier \(\lambda\) is often a **shadow price**: approximately how much the optimal objective changes when the constraint is relaxed by one unit. [en.wikipedia](https://en.wikipedia.org/wiki/Lagrange_multiplier)

## General recipe

1. Define the objective \(f\) and equality constraint \(g=c\).
2. Write \(\mathcal L=f-\lambda(g-c)\).
3. Set every partial derivative of \(\mathcal L\) to zero.
4. Solve the resulting equations and evaluate \(f\) at feasible candidates.
5. Interpret \(\lambda\), including its sign, according to how you wrote the constraint.

## 1. Closest point on a circle

**Application:** A robot or drone must remain exactly 5 m from a beacon. Which allowed position is closest to a target at \((6,8)\)?

Minimize squared distance:

\[
f(x,y)=(x-6)^2+(y-8)^2
\]

subject to the flight-radius constraint:

\[
g(x,y)=x^2+y^2=25.
\]

The Lagrange equations are

\[
2(x-6)=2\lambda x,\qquad 2(y-8)=2\lambda y,\qquad x^2+y^2=25.
\]

The target lies 10 units from the origin, so the nearest point on the radius-5 circle is in its direction:

\[
(x,y)=5\left(\frac{6}{10},\frac{8}{10}\right)=(3,4).
\]

Thus, the closest feasible position is **\((3,4)\)**, at distance 5 from the target.

## 2. Product design: maximum-volume box

**Application:** Design a closed rectangular package with a fixed amount of material. For a fixed surface area, what dimensions maximize volume?

Maximize

\[
f(x,y,z)=xyz
\]

subject to a fixed surface area

\[
2(xy+xz+yz)=S.
\]

The equations \(\nabla f=\lambda \nabla g\) give

\[
yz=2\lambda(y+z),\quad
xz=2\lambda(x+z),\quad
xy=2\lambda(x+y).
\]

Comparing the equations yields \(x=y=z\). Therefore the optimal package is a **cube**:

\[
x=y=z=\sqrt{\frac{S}{6}}.
\]

This is a standard engineering design pattern: under a symmetric material constraint, symmetric dimensions maximize enclosed volume. Related constrained material-minimization box examples appear in MIT’s calculus notes. [ocw.mit](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/d97c53ed0a6734b4bc266478fe6423c1_MIT18_02SC_notes_21.pdf)

## 3. Consumer spending under a budget

**Application:** Allocate a fixed budget between two goods to maximize utility.

Let utility be Cobb–Douglas:

\[
U(x,y)=x^{1/2}y^{1/2},
\]

where \(x\) and \(y\) are quantities purchased. Suppose prices are \(p_x=2\), \(p_y=1\), and budget is \(B=100\):

\[
2x+y=100.
\]

Set

\[
\mathcal L=\sqrt{xy}-\lambda(2x+y-100).
\]

First-order conditions lead to

\[
\frac{MU_x}{p_x}=\frac{MU_y}{p_y},
\]

which says the consumer allocates spending until the **marginal utility per dollar** is equal across goods. Here that produces

\[
x=25,\qquad y=50.
\]

So the buyer spends \$50 on each good: \(2(25)=50\) on \(x\) and \(1(50)=50\) on \(y\). Budget-constrained utility optimization is a canonical use of the method. [ocw.mit](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/d97c53ed0a6734b4bc266478fe6423c1_MIT18_02SC_notes_21.pdf)

## 4. Power-grid economic dispatch

**Application:** A grid operator must meet a specified electricity demand at minimum generation cost.

For two generators, minimize

\[
C(P_1,P_2)=C_1(P_1)+C_2(P_2)
\]

subject to power balance

\[
P_1+P_2=D.
\]

The Lagrangian is

\[
\mathcal L=C_1(P_1)+C_2(P_2)-\lambda(P_1+P_2-D).
\]

The necessary conditions are

\[
C_1'(P_1)=\lambda,\qquad C_2'(P_2)=\lambda.
\]

Therefore, at the least-cost dispatch,

\[
\boxed{C_1'(P_1)=C_2'(P_2)}
\]

—each online unit has the same incremental cost. Here \(\lambda\) is the marginal cost of supplying one additional unit of load, closely related to a system energy price. Economic dispatch is a well-known Lagrange-multiplier application in power systems. [sces.phys.utk](https://sces.phys.utk.edu/~moreo/mm08/method_HLi.pdf)

## 5. Machine learning: normalized model weights

**Application:** Optimize a score while forcing a model vector to have unit norm, which is useful when only direction—not scale—should matter.

Maximize alignment with a vector \(a\):

\[
f(w)=a^\top w
\]

subject to

\[
\|w\|^2=w^\top w=1.
\]

Use

\[
\mathcal L(w,\lambda)=a^\top w-\lambda(w^\top w-1).
\]

Differentiating with respect to \(w\):

\[
a-2\lambda w=0
\quad\Rightarrow\quad
w=\frac{a}{2\lambda}.
\]

Imposing \(\|w\|=1\) gives \(2|\lambda|=\|a\|\). The maximizing choice is

\[
\boxed{w^\star=\frac{a}{\|a\|}},
\]

with maximum value

\[
a^\top w^\star=\|a\|.
\]

This is the same mathematical structure behind maximizing a dot product on a sphere and appears throughout machine learning derivations and constrained optimization. [khanacademy](https://www.khanacademy.org/math/multivariable-calculus/applications-of-multivariable-derivatives/constrained-optimization/a/lagrange-multipliers-examples)

## Important limitation

Classical Lagrange multipliers handle **equality constraints** cleanly. Constraints such as \(x\ge0\), budget not exceeded, capacity at most \(K\), or risk below a threshold require the broader Karush–Kuhn–Tucker (KKT) conditions, which add nonnegative multipliers and complementary-slackness conditions.
