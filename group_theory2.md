
The classification of finite simple groups gives a complete catalogue of the **building-blocks** of finite group theory: every nontrivial finite simple group is isomorphic to a member of 18 infinite families or to one of 26 sporadic groups. The 18 families comprise one cyclic family, one alternating family, and 16 families of Lie type. The standard count includes the Tits group with the Lie-type groups. [en.wikipedia](https://en.wikipedia.org/wiki/Classification_of_finite_simple_groups)

The crucial distinction is that this classifies finite simple groups, not all finite groups. The Jordan–Hölder theorem tells us which simple factors occur inside a finite group, but reconstructing the group from those factors requires additional extension data. [crypto.stanford](https://crypto.stanford.edu/pbc/notes/group/jordanholder.html)

## 1. The overall taxonomy

A nontrivial group \(G\) is simple if its only normal subgroups are \(1\) and \(G\). It may have many proper subgroups; simplicity forbids only proper, nontrivial normal subgroups. [en.wikipedia](https://en.wikipedia.org/wiki/Sporadic_group)

The classification, up to isomorphism, has this structure: [en.wikipedia](https://en.wikipedia.org/wiki/List_of_finite_simple_groups)

```text
Finite simple groups
│
├── 1. Cyclic groups of prime order
│       C_p, p prime
│
├── 2. Alternating groups
│       Alt(n), n ≥ 5
│
├── 3. Groups of Lie type: 16 families
│   │
│   ├── Untwisted classical: 4
│   │       A_n, B_n, C_n, D_n
│   │
│   ├── Untwisted exceptional: 5
│   │       E_6, E_7, E_8, F_4, G_2
│   │
│   ├── Steinberg twisted: 4
│   │       ²A_n, ²D_n, ²E_6, ³D_4
│   │
│   └── Suzuki–Ree: 3
│           ²B_2, ²G_2, ²F_4
│           Including the Tits group ²F_4(2)'
│
└── 4. Sporadic groups: 26 individual exceptions
```

Thus the family count is

\[
1+1+(4+5+4+3)=18.
\]

Here “family” means a parameterized construction, not necessarily a disjoint collection: different families have some isomorphic small members. [en.wikipedia](https://en.wikipedia.org/wiki/List_of_finite_simple_groups)

## 2. The 18 infinite families

### Notation and construction

Write \(q=p^f\) for a prime power and \(\mathbb F_q\) for the field with \(q\) elements. To avoid a notation collision, use \(\operatorname{Alt}(n)\) for alternating groups and \(A_n(q)\) for Lie-type groups. [en.wikipedia](https://en.wikipedia.org/wiki/List_of_finite_simple_groups)

Groups of Lie type are finite-field analogues of groups arising from Lie theory. The classical examples come from linear transformations preserving determinants or bilinear, quadratic, and Hermitian forms. One commonly takes an appropriate subgroup and then quotients by its center to obtain a simple group. For example,

\[
A_n(q)=\operatorname{PSL}_{n+1}(q)
=\operatorname{SL}_{n+1}(\mathbb F_q)/Z\!\left(\operatorname{SL}_{n+1}(\mathbb F_q)\right).
\]

The twisted families incorporate symmetries of the underlying Lie-theoretic construction together with field automorphisms. [en.wikipedia](https://en.wikipedia.org/wiki/List_of_finite_simple_groups)

In the tables below, the twisted notation uses \({}^{2}A_n(q)\), rather than \({}^{2}A_n(q^2)\). Under this convention, \({}^{2}A_n(q)=\operatorname{PSU}_{n+1}(q)\), whose matrices are defined over \(\mathbb F_{q^2}\). Both conventions occur in the literature. [en.wikipedia](https://en.wikipedia.org/wiki/List_of_finite_simple_groups)

### Families 1–6: cyclic, alternating, and untwisted classical groups

| No. | Family | Description and parameter restrictions |
|---|---|---|
| 1 | \(C_p\) | Cyclic group of prime order \(p\). These are the only abelian finite simple groups. |
| 2 | \(\operatorname{Alt}(n)\) | Even permutations of \(n\) letters, \(n\ge5\); order \(n!/2\). |
| 3 | \(A_n(q)\) | \(\operatorname{PSL}_{n+1}(q)\), \(n\ge1\); exclude \((n,q)=(1,2),(1,3)\). |
| 4 | \(B_n(q)\) | Odd-dimensional orthogonal type, conventionally \(\mathrm P\Omega_{2n+1}(q)\), \(n\ge2\); exclude \(B_2(2)\). |
| 5 | \(C_n(q)\) | Symplectic type, \(\operatorname{PSp}_{2n}(q)\). Use \(n\ge3\) to avoid duplicating \(C_2(q)\cong B_2(q)\). |
| 6 | \(D_n(q)\) | Split even-dimensional orthogonal type, \(\mathrm P\Omega^+_{2n}(q)\), \(n\ge4\). |

These descriptions refer to the simple projective versions, with the stated small exceptions removed. In even characteristic, \(B_n(q)\cong C_n(q)\); thus some overlap remains between the conventional families. [en.wikipedia](https://en.wikipedia.org/wiki/List_of_finite_simple_groups)

The geometries distinguish the classical types: \(A_n\) is linear, \(B_n\) and \(D_n\) are orthogonal, and \(C_n\) is symplectic. The \(+\) in the orthogonal notation indicates the split form. [en.wikipedia](https://en.wikipedia.org/wiki/List_of_finite_simple_groups)

### Families 7–11: untwisted exceptional groups

| No. | Family | Parameters and a useful interpretation |
|---|---|---|
| 7 | \(E_6(q)\) | All prime powers \(q\); exceptional type with associated Lie algebra of dimension 78. |
| 8 | \(E_7(q)\) | All prime powers \(q\); associated Lie algebra of dimension 133. |
| 9 | \(E_8(q)\) | All prime powers \(q\); associated Lie algebra of dimension 248. |
| 10 | \(F_4(q)\) | All prime powers \(q\); connected with exceptional Jordan algebras. |
| 11 | \(G_2(q)\) | All prime powers \(q\), except \(q=2\); connected with octonion/Cayley algebras. |

“Exceptional” here is a Lie-theoretic designation, not a synonym for “sporadic.” Each row is an infinite family obtained by varying the finite field. The notation means the appropriate simple version; for example, one must account for centers in types \(E_6\) and \(E_7\). [en.wikipedia](https://en.wikipedia.org/wiki/List_of_finite_simple_groups)

### Families 12–15: Steinberg twisted groups

| No. | Family | Description and restrictions |
|---|---|---|
| 12 | \({}^{2}A_n(q)\) | Projective special unitary groups \(\operatorname{PSU}_{n+1}(q)\), \(n\ge2\); exclude \((n,q)=(2,2)\). |
| 13 | \({}^{2}D_n(q)\) | Nonsplit even-dimensional orthogonal groups \(\mathrm P\Omega^-_{2n}(q)\), \(n\ge4\). |
| 14 | \({}^{2}E_6(q)\) | Twisted exceptional \(E_6\) groups; all prime powers \(q\). |
| 15 | \({}^{3}D_4(q)\) | Triality-twisted \(D_4\) groups; all prime powers \(q\). |

The superscripts \(2\) and \(3\) indicate the order of the diagram symmetry involved in the twist, not exponentiation of the group. Unitary groups preserve a Hermitian form; triality comes from the unusually rich diagram symmetry of \(D_4\). [en.wikipedia](https://en.wikipedia.org/wiki/List_of_finite_simple_groups)

### Families 16–18: Suzuki and Ree groups

| No. | Family | Allowed field sizes for the simple members |
|---|---|---|
| 16 | \({}^{2}B_2(q)\), or \(\operatorname{Sz}(q)\) | Suzuki groups, \(q=2^{2m+1}\), \(m\ge1\). |
| 17 | \({}^{2}G_2(q)\) | Small Ree groups, \(q=3^{2m+1}\), \(m\ge1\). |
| 18 | \({}^{2}F_4(q)\) | Large Ree groups, \(q=2^{2m+1}\), \(m\ge1\), together with the special simple group \({}^{2}F_4(2)'\). |

These exceptional twists exist only in the specified characteristics and odd-degree field extensions. [en.wikipedia](https://en.wikipedia.org/wiki/List_of_finite_simple_groups)

### Small exceptions, overlaps, and the Tits group

The classification catalogue is a list of isomorphism types, not a list of distinct names. Important overlaps include

\[
\operatorname{Alt}(5)\cong\operatorname{PSL}_2(4)\cong\operatorname{PSL}_2(5),
\]

\[
\operatorname{Alt}(6)\cong\operatorname{PSL}_2(9),
\qquad
\operatorname{Alt}(8)\cong\operatorname{PSL}_4(2),
\]

and

\[
\operatorname{PSL}_2(7)\cong\operatorname{PSL}_3(2).
\]

Some excluded nonsimple groups have simple derived subgroups already represented elsewhere: \(B_2(2)'\cong\operatorname{Alt}(6)\), \(G_2(2)'\cong\operatorname{PSU}_3(3)\), and \({}^{2}G_2(3)'\cong\operatorname{PSL}_2(8)\). Here \(G'\) denotes the subgroup generated by commutators. [en.wikipedia](https://en.wikipedia.org/wiki/List_of_finite_simple_groups)

The Tits group is

\[
T={}^{2}F_4(2)',\qquad |T|=17{,}971{,}200.
\]

Although \({}^{2}F_4(2)\) is not simple, its derived subgroup is simple and has index two. Conventionally \(T\) belongs with the Ree family, preserving the count of 26 sporadic groups; sources that count it separately sometimes speak of 27 sporadic groups. [en.wikipedia](https://en.wikipedia.org/wiki/List_of_finite_simple_groups)

## 3. The 26 sporadic groups

The following table lists every sporadic group, grouped by name rather than by order. These are individual isomorphism types, not infinite parameterized families. [en.wikipedia](https://en.wikipedia.org/wiki/List_of_finite_simple_groups)

| Named grouping | Groups | Count |
|---|---|---:|
| Mathieu | \(M_{11},M_{12},M_{22},M_{23},M_{24}\) | 5 |
| Janko | \(J_1,J_2,J_3,J_4\) | 4 |
| Conway | \(\mathrm{Co}_1,\mathrm{Co}_2,\mathrm{Co}_3\) | 3 |
| Fischer | \(\mathrm{Fi}_{22},\mathrm{Fi}_{23},\mathrm{Fi}_{24}'\) | 3 |
| Higman–Sims | \(\mathrm{HS}\) | 1 |
| McLaughlin | \(\mathrm{McL}\) | 1 |
| Held | \(\mathrm{He}\) | 1 |
| Rudvalis | \(\mathrm{Ru}\) | 1 |
| Suzuki sporadic | \(\mathrm{Suz}\) | 1 |
| O’Nan | \(\mathrm{O'N}\) | 1 |
| Harada–Norton | \(\mathrm{HN}\) | 1 |
| Lyons | \(\mathrm{Ly}\) | 1 |
| Thompson | \(\mathrm{Th}\) | 1 |
| Baby Monster | \(\mathbb B\) | 1 |
| Monster | \(\mathbb M\) | 1 |
| Total | | 26 |

Two notation cautions matter:

- The simple Fischer group is \(\mathrm{Fi}_{24}'\), not the larger nonsimple group \(\mathrm{Fi}_{24}\).
- The sporadic Suzuki group \(\mathrm{Suz}\) is different from the infinite Suzuki family \({}^{2}B_2(q)\). [en.wikipedia](https://en.wikipedia.org/wiki/List_of_finite_simple_groups)

### Their structural relationships

The sporadic groups are not entirely unrelated exceptions. Twenty, including the Monster itself, form the “happy family”: they occur as subquotients of the Monster. A subquotient means a group \(H/N\), where \(H\le\mathbb M\) and \(N\triangleleft H\); it need not be a subgroup of \(\mathbb M\). [en.wikipedia](https://en.wikipedia.org/wiki/Sporadic_group)

They can be organized into three generations: [en.wikipedia](https://en.wikipedia.org/wiki/Sporadic_group)

| Generation | Members | Main connection |
|---|---|---|
| First: 5 | \(M_{11},M_{12},M_{22},M_{23},M_{24}\) | Highly transitive permutation groups. |
| Second: 7 | \(\mathrm{Co}_1,\mathrm{Co}_2,\mathrm{Co}_3,\mathrm{Suz},\mathrm{McL},\mathrm{HS},J_2\) | Symmetries associated with the 24-dimensional Leech lattice. |
| Third: 8 | \(\mathbb M,\mathbb B,\mathrm{Fi}_{22},\mathrm{Fi}_{23},\mathrm{Fi}_{24}',\mathrm{Th},\mathrm{HN},\mathrm{He}\) | Groups closely related to Monster subgroups and element centralizers. |

The six remaining sporadic groups are the “pariahs”:

\[
J_1,\ J_3,\ J_4,\ \mathrm{O'N},\ \mathrm{Ru},\ \mathrm{Ly}.
\]

They do not occur as Monster subquotients. [en.wikipedia](https://en.wikipedia.org/wiki/Sporadic_group)

### The Monster group

The Monster is the largest sporadic group, with order

\[
\begin{aligned}
|\mathbb M|
={}&2^{46}3^{20}5^9 7^6 11^2 13^3\\
&{}\cdot17\cdot19\cdot23\cdot29\cdot31\cdot41\cdot47\cdot59\cdot71\\
\approx{}&8.08017\times10^{53}.
\end{aligned}
\]

It is an automorphism group of the Griess algebra and of the Monster vertex operator algebra, and it is connected with monstrous moonshine. [en.wikipedia](https://en.wikipedia.org/wiki/List_of_finite_simple_groups)

“Largest sporadic” does not mean “largest finite simple group”: the infinite families contain groups of arbitrarily large order. [en.wikipedia](https://en.wikipedia.org/wiki/List_of_finite_simple_groups)

## 4. Composition series: extracting the simple factors

A composition series of a finite group \(G\) is a chain

\[
1=G_0\triangleleft G_1\triangleleft\cdots\triangleleft G_r=G
\]

such that each quotient

\[
S_i=G_i/G_{i-1}
\]

is nontrivial and simple. The \(S_i\) are the composition factors. [crypto.stanford](https://crypto.stanford.edu/pbc/notes/group/jordanholder.html)

Only adjacent normality is required:

\[
G_{i-1}\triangleleft G_i.
\]

A term need not be normal in the whole group \(G\). Every finite group has a composition series: repeatedly choose a maximal proper normal subgroup of the current group; the corresponding quotient is simple, and strict decrease in order ensures termination. [crypto.stanford](https://crypto.stanford.edu/pbc/notes/group/jordanholder.html)

The orders satisfy

\[
|G|=\prod_{i=1}^{r}|S_i|,
\]

but this numerical product records only a small part of the structure.

### Worked example: \(S_4\)

Let

\[
V_4=\{1,(12)(34),(13)(24),(14)(23)\}.
\]

A composition series is

\[
1
\triangleleft\langle(12)(34)\rangle
\triangleleft V_4
\triangleleft A_4
\triangleleft S_4.
\]

Its factors, read upwards, are

\[
C_2,\quad C_2,\quad C_3,\quad C_2.
\]

The order check is \(24=2\cdot2\cdot3\cdot2\). Notice that \(\langle(12)(34)\rangle\) is normal in \(V_4\), but not in \(S_4\), illustrating why composition series require adjacent normality rather than global normality. [crypto.stanford](https://crypto.stanford.edu/pbc/notes/group/jordanholder.html)

For \(n\ge5\), the chain

\[
1\triangleleft A_n\triangleleft S_n
\]

is already a composition series, with factors \(A_n\) and \(C_2\). [crypto.stanford](https://crypto.stanford.edu/pbc/notes/group/jordanholder.html)

## 5. The Jordan–Hölder theorem

The Jordan–Hölder theorem says that any two composition series of a group have the same length and the same composition factors up to isomorphism and reordering, with multiplicities counted. [crypto.stanford](https://crypto.stanford.edu/pbc/notes/group/jordanholder.html)

Precisely, if one series has factors \(S_1,\ldots,S_r\) and another has \(T_1,\ldots,T_s\), then

\[
r=s
\]

and there is a permutation \(\sigma\) such that

\[
S_i\cong T_{\sigma(i)}
\qquad(1\le i\le r).
\]

Thus the multiset of simple factors is an invariant of \(G\). The theorem does not say that the subgroup chains themselves are unique. [crypto.stanford](https://crypto.stanford.edu/pbc/notes/group/jordanholder.html)

### Why uniqueness holds: proof idea

Use induction on \(|G|\), comparing two maximal proper normal subgroups \(A,B\triangleleft G\).

- If \(A=B\), apply induction inside \(A\).
- If \(A\ne B\), their product is \(AB=G\). Set \(D=A\cap B\). The isomorphism theorems give
  \[
  A/D\cong G/B,\qquad B/D\cong G/A.
  \]
  Compare the chains through \(A\) and \(B\) with chains passing through \(D\). Above \(D\), the same two simple factors appear in opposite orders; below \(D\), induction gives the same factors.

This establishes equality of the factor multisets. [crypto.stanford](https://crypto.stanford.edu/pbc/notes/group/jordanholder.html)

### What it does not establish

The groups \(C_6\) and \(S_3\) both have composition factors \(C_2,C_3\), but they are not isomorphic: \(C_6\) is abelian and \(S_3\) is not. Consequently, Jordan–Hölder is a uniqueness theorem for the factors, not for the way they are assembled. [crypto.stanford](https://crypto.stanford.edu/pbc/notes/group/jordanholder.html)

## 6. How finite groups are classified—and what remains difficult

### Simple factors plus extensions

Each step of a composition series yields a short exact sequence

\[
1\longrightarrow G_{i-1}
\longrightarrow G_i
\longrightarrow S_i
\longrightarrow1.
\]

Thus \(G_i\) is an extension of \(G_{i-1}\) by the simple group \(S_i\). In principle, classifying arbitrary finite groups requires:

1. The catalogue of possible simple factors.
2. Classification of the possible extensions at each step.
3. Identification of constructions that produce isomorphic groups. [math.stackexchange](https://math.stackexchange.com/questions/236816/applications-of-the-jordan-h%C3%B6lder-theorem)

The classification of finite simple groups solves the first problem. Jordan–Hölder makes the factor multiset intrinsic to a given group. Neither solves the extension problem. [en.wikipedia](https://en.wikipedia.org/wiki/Classification_of_finite_simple_groups)

The example \(C_6\) versus \(S_3\) makes the missing information concrete:

\[
C_6\cong C_3\times C_2,
\qquad
S_3\cong C_3\rtimes C_2.
\]

In the second group, the \(C_2\) factor acts on \(C_3\) by inversion. The same simple ingredients therefore produce different multiplication laws. [crypto.stanford](https://crypto.stanford.edu/pbc/notes/group/jordanholder.html)

### Solvable versus nonsolvable groups

A finite group is solvable if and only if all of its composition factors are cyclic of prime order. Thus solvable groups use only family 1 as their composition factors, while every nonsolvable finite group has at least one nonabelian simple composition factor. [crypto.stanford](https://crypto.stanford.edu/pbc/notes/group/jordanholder.html)

For example:

- \(S_4\) is solvable, with factors \(C_2,C_2,C_3,C_2\).
- \(S_5\) is nonsolvable, with factors \(A_5,C_2\).

This also shows why “all factors are cyclic” does not imply that the original group is cyclic—or even abelian. [crypto.stanford](https://crypto.stanford.edu/pbc/notes/group/jordanholder.html)

### The scope of the classification theorem

A complete classification of finite simple groups means that every simple isomorphism type appears in the catalogue, subject to the parameter restrictions and duplicate identifications. It does not provide a comparable explicit catalogue of all finite groups. Even knowing the exact composition factors leaves the assembly problem unresolved. [en.wikipedia](https://en.wikipedia.org/wiki/Classification_of_finite_simple_groups)

The relationship can therefore be summarized as

\[
\boxed{
\begin{array}{c}
\text{Classification of finite simple groups}\\
\text{lists the possible simple constituents;}
\\[4pt]
\text{Jordan–Hölder}\\
\text{makes their multiset unique for a given group;}
\\[4pt]
\text{extension theory}\\
\text{determines how those constituents can fit together.}
\end{array}
}
\]
