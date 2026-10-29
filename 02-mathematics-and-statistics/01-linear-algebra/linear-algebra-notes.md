# Linear Algebra and Matrices

Readable notes from my handwritten notebook, in simple language.

[Mathematics and Statistics](../README.md) · [Original handwritten PDF](Linear%20Algebra%20%26%20Matrices.pdf)

**How to read:** Follow the sections in order. The examples come from the handwritten notes. Short explanations labelled **Extra explanation** are added to make the ideas easier to follow. **Correction** boxes identify mathematical slips in the original; the PDF is unchanged. Page references use the PDF's page order, 1 to 38.

## Contents

1. [Scalars, vectors and vector types](#1-scalars-vectors-and-vector-types)
2. [Vector addition and subtraction](#2-vector-addition-and-subtraction)
3. [Coordinates, magnitude and direction](#3-coordinates-magnitude-and-direction)
4. [Dot product and projection](#4-dot-product-and-projection)
5. [Vector norms](#5-vector-norms)
6. [Changing coordinates](#6-changing-coordinates)
7. [Linear dependence, independence and basis](#7-linear-dependence-independence-and-basis)
8. [Matrices and linear transformations](#8-matrices-and-linear-transformations)
9. [Matrix operations and types](#9-matrix-operations-and-types)
10. [Rank, null space and nullity](#10-rank-null-space-and-nullity)
11. [Solving linear equations](#11-solving-linear-equations)
12. [Least squares and minimum-norm solutions](#12-least-squares-and-minimum-norm-solutions)
13. [Projection onto a subspace](#13-projection-onto-a-subspace)
14. [Lines, planes, hyperplanes and halfspaces](#14-lines-planes-hyperplanes-and-halfspaces)
15. [Eigenvalues and eigenvectors](#15-eigenvalues-and-eigenvectors)
16. [Quick revision](#16-quick-revision)
17. [Original-page reading map and corrections](#17-original-page-reading-map-and-corrections)

## 1. Scalars, vectors and vector types

*Original: page 1.*

A **scalar** tells us only the amount, or magnitude. Examples: height, weight, and speed of 40 km/h.

A **vector** tells us the amount **and** the direction. Example: velocity of 40 km/h towards the south.

We draw a vector as an arrow. The start is its **tail**, the end is its **head**, and the arrow's length represents its magnitude. We write it as $\vec a$ or $\overrightarrow{AB}$.

| Type | Simple meaning |
|---|---|
| Zero vector | All components are zero; magnitude is zero. |
| Unit vector | Magnitude is 1. |
| Co-initial vectors | Start at the same point. |
| Collinear vectors | Lie along the same line or parallel lines. |
| Equal vectors | Same magnitude and same direction, even if drawn at different positions. |
| Negative/opposite vectors | Same magnitude, opposite direction: $\vec a$ and $-\vec a$. |
| Like vectors | Point in the same direction; lengths can differ. |
| Unlike vectors | Point in opposite directions; lengths can differ. |

**Clarification:** A zero vector does not have a unique direction. The statement “a vector has magnitude and direction” needs this exception.

## 2. Vector addition and subtraction

*Original: pages 2-5.*

### 2.1 Head-to-tail method

To add $\vec u$ and $\vec v$:

1. Draw $\vec u$.
2. Place the tail of $\vec v$ at the head of $\vec u$.
3. Draw an arrow from the first tail to the final head. This is $\vec u+\vec v$.

![Head-to-tail vector addition](assets/vector-addition.png)

### 2.2 Parallelogram method

Draw both vectors from the same starting point. Complete the parallelogram. Its diagonal from the common starting point is the resultant.

### 2.3 Subtraction

Subtracting a vector means adding its negative:

$$
\vec u-\vec v=\vec u+(-\vec v).
$$

Reverse the direction of $\vec v$, then use head-to-tail addition.

### 2.4 Addition properties

$$
\begin{aligned}
\vec u+\vec v&=\vec v+\vec u &&\text{commutative}\\
(\vec u+\vec v)+\vec w&=\vec u+(\vec v+\vec w) &&\text{associative}\\
\vec v+\vec 0&=\vec v &&\text{identity}\\
\vec v+(-\vec v)&=\vec 0 &&\text{additive inverse}.
\end{aligned}
$$

### 2.5 Resultant magnitude and direction

Suppose two vectors have magnitudes $A$ and $B$, with angle $\theta$ between them. Place the first along the horizontal axis.

The second vector has horizontal component $B\cos\theta$ and vertical component $B\sin\theta$. So:

$$
R_x=A+B\cos\theta,\qquad R_y=B\sin\theta.
$$

Using Pythagoras:

$$
\begin{aligned}
R^2&=(A+B\cos\theta)^2+(B\sin\theta)^2\\
&=A^2+B^2+2AB\cos\theta,\\
R&=\sqrt{A^2+B^2+2AB\cos\theta}.
\end{aligned}
$$

The direction $\phi$ measured from the first vector satisfies:

$$
\tan\phi=\frac{B\sin\theta}{A+B\cos\theta}.
$$

**Extra explanation:** In code, `atan2(R_y, R_x)` handles the quadrant correctly. The zero resultant has no unique direction.

> **Correction - page 5:** The boxed magnitude expression misses the square root. Without the square root, it gives $R^2$, not $R$.

## 3. Coordinates, magnitude and direction

*Original: pages 3-4 and 29-30.*

The standard unit vectors are $\hat i$ in the x-direction, $\hat j$ in the y-direction, and $\hat k$ in the z-direction.

The same vector can be written in different forms:

$$
\vec a=2\hat i+3\hat j+4\hat k
=\begin{bmatrix}2\\3\\4\end{bmatrix}.
$$

The column contains the vector's coordinates. In data science, a sample with $n$ numerical features can be represented in $n$ dimensions, even when we cannot draw those dimensions.

### Magnitude

$$
\|\vec a\|_2=\sqrt{a_1^2+a_2^2+\cdots+a_n^2}.
$$

Examples from the notes:

- $3\hat i+4\hat j$ has magnitude $\sqrt{9+16}=5$.
- $4\hat i+3\hat j$ also has magnitude 5, but points in a different direction.
- $7\hat i+2\hat j$ has magnitude $\sqrt{53}$.

### Unit direction

For a nonzero vector:

$$
\hat a=\frac{\vec a}{\|\vec a\|_2}.
$$

In simple words: divide by the length to keep only the direction. The resulting vector still has a magnitude - exactly 1.

### Distance between two points

Distance is the length of their difference:

$$
d(A,B)=\|B-A\|_2.
$$

For $A=(2,7)$ and $B=(5,3)$:

$$
d(A,B)=\sqrt{(5-2)^2+(3-7)^2}=\sqrt{25}=5.
$$

Their unit directions from the origin are $(2,7)/\sqrt{53}$ and $(5,3)/\sqrt{34}$. These are different from the direction of the displacement $B-A$.

## 4. Dot product and projection

*Original: pages 6-8; recap on pages 29-30.*

### 4.1 Dot product

The dot product combines two vectors into a **scalar**:

$$
\vec a\cdot\vec b=\vec a^T\vec b
=\sum_{i=1}^{n}a_i b_i
=\|\vec a\|_2\|\vec b\|_2\cos\theta.
$$

For the vectors on page 6:

$$
\vec a=\begin{bmatrix}2\\3\\4\end{bmatrix},\qquad
\vec b=\begin{bmatrix}1\\7\\8\end{bmatrix},
$$

$$
\vec a^T\vec b=2(1)+3(7)+4(8)=55.
$$

Remember:

- $\theta=0^\circ$: dot product equals the product of the magnitudes.
- $\theta=90^\circ$: dot product is zero; the vectors are **orthogonal**.
- The dot product can be negative when the vectors point more against each other than along each other.

The resultant formula also becomes:

$$
\|\vec a+\vec b\|_2^2
=\|\vec a\|_2^2+\|\vec b\|_2^2+2\vec a^T\vec b.
$$

> **Correction - page 6:** The dot product is related to projection; it is not the projection length itself. Divide by the length of the target vector to obtain that length.

### 4.2 Scalar and vector projection

![A vector and its perpendicular projection onto another vector](assets/projection.png)

Projection asks: **how much of $\vec a$ lies along $\vec b$?** Assume $\vec b\ne0$.

The signed scalar projection is:

$$
p=\frac{\vec a^T\vec b}{\|\vec b\|_2}.
$$

To turn this into a vector, multiply by the unit direction of $\vec b$:

$$
\operatorname{proj}_{\vec b}(\vec a)
=p\frac{\vec b}{\|\vec b\|_2}
=\frac{\vec a^T\vec b}{\vec b^T\vec b}\vec b.
$$

For $\vec a=(2,3)$ and $\vec b=(7,6)$, as on page 7:

$$
\vec a^T\vec b=14+18=32,\qquad \|\vec b\|_2=\sqrt{85}.
$$

So:

$$
p=\frac{32}{\sqrt{85}},\qquad
\operatorname{proj}_{\vec b}(\vec a)
=\frac{32}{85}\begin{bmatrix}7\\6\end{bmatrix}
=\begin{bmatrix}224/85\\192/85\end{bmatrix}.
$$

**Extra explanation:** $p$ is signed. The magnitude of the projection is $|p|$. The residual $\vec a-\operatorname{proj}_{\vec b}(\vec a)$ is perpendicular to $\vec b$.

### 4.3 Check the angle before using it

Page 7 also lists $\vec a=(3,4,7)$, $\vec b=(7,0,3)$, and an angle of $30^\circ$.

> **Correction:** The listed components imply $\vec a^T\vec b=42$ and an angle of approximately $50.13^\circ$, not $30^\circ$. For those components, $\|\vec a+\vec b\|=\sqrt{216}=6\sqrt6$. If $30^\circ$ was intended, the vector components need changing.

## 5. Vector norms

*Original: page 8.*

A norm is a way of measuring vector size.

| Norm | Formula | Example for $\vec a=(-3,4)$ |
|---|---|---|
| L1 | $\|\vec a\|_1=\sum_i\lvert a_i\rvert$ | $3+4=7$ |
| L2 | $\|\vec a\|_2=\sqrt{\sum_i a_i^2}$ | $\sqrt{9+16}=5$ |
| Infinity/max | $\|\vec a\|_\infty=\max_i\lvert a_i\rvert$ | $4$ |

The general p-norm, for $p\ge1$, is:

$$
\|\vec a\|_p=\left(\sum_{i=1}^{n}\lvert a_i\rvert^p\right)^{1/p}.
$$

The notes connect these to controlling overfitting:

- **Lasso:** uses an L1 penalty on model coefficients.
- **Ridge:** uses a squared L2 penalty on model coefficients.

**Extra explanation:** The L2 norm is a square root; the usual ridge penalty is its square. They are closely related but are not the same expression.

## 6. Changing coordinates

*Original: pages 9-10.*

The vector stays the same. We describe it using different reference directions.

Take the example in the notebook:

$$
\vec a=\begin{bmatrix}5\\7\end{bmatrix},\quad
\vec x_1=\begin{bmatrix}2\\-1\end{bmatrix},\quad
\vec x_2=\begin{bmatrix}1\\2\end{bmatrix}.
$$

First check that the new directions are perpendicular:

$$
\vec x_1^T\vec x_2=2(1)+(-1)(2)=0.
$$

Both have length $\sqrt5$. Since they are orthogonal, their coefficients can be found separately:

$$
\lambda_1=\frac{\vec a^T\vec x_1}{\vec x_1^T\vec x_1}
=\frac{10-7}{5}=\frac35,
$$

$$
\lambda_2=\frac{\vec a^T\vec x_2}{\vec x_2^T\vec x_2}
=\frac{5+14}{5}=\frac{19}{5}.
$$

So:

$$
\vec a=\frac35\vec x_1+\frac{19}{5}\vec x_2
=\begin{bmatrix}5\\7\end{bmatrix}.
$$

The scalar projection lengths are $3/\sqrt5$ and $19/\sqrt5$; the coordinates in the **non-unit** basis are $3/5$ and $19/5$. Do not mix these up.

> **Clarification:** Some signs in the handwritten working are inconsistent. The choice $(2,-1)$ matches the diagram, the zero dot product, and the coefficient $3/5$. Also, these new axes are orthogonal but not unit length: this is not just a pure rotation of unit axes.

## 7. Linear dependence, independence and basis

*Original: pages 10-12 and the exercise on page 30.*

### 7.1 Linear combination

A linear combination means multiply vectors by scalars and add them:

$$
\vec v=c_1\vec v_1+c_2\vec v_2+\cdots+c_k\vec v_k.
$$

Example:

$$
\vec v_1=\begin{bmatrix}1\\2\\3\end{bmatrix},\quad
\vec v_2=\begin{bmatrix}2\\4\\6\end{bmatrix}=2\vec v_1,\quad
\vec v_3=\begin{bmatrix}0.5\\1\\1.5\end{bmatrix}=\frac12\vec v_1.
$$

They all lie along one direction. The set is **linearly dependent**.

### 7.2 Test for independence

Consider:

$$
c_1\vec v_1+\cdots+c_k\vec v_k=\vec0.
$$

- If the **only** solution is $c_1=\cdots=c_k=0$, the vectors are independent.
- If a solution exists with **at least one** nonzero coefficient, they are dependent.

It is not necessary for every coefficient in a dependence relation to be nonzero.

The standard vectors $(1,0,0)$, $(0,1,0)$ and $(0,0,1)$ are independent.

For the page 11 example:

$$
\vec a_1=\begin{bmatrix}1\\2\\3\end{bmatrix},\quad
\vec a_2=\begin{bmatrix}0\\0\\1\end{bmatrix},\quad
\vec a_3=\begin{bmatrix}0\\0\\2\end{bmatrix},
$$

$$
0\vec a_1+2\vec a_2-\vec a_3=\vec0.
$$

Therefore the set is dependent. The heading on that handwritten example says “independent”, but its conclusion correctly says “not independent”.

### 7.3 Basis vectors

A **basis** is a set that:

1. Is linearly independent.
2. Can generate every vector in the space using linear combinations. This is called **spanning** the space.

In $\mathbb R^2$, the standard basis is:

$$
\vec e_1=\begin{bmatrix}1\\0\end{bmatrix},\qquad
\vec e_2=\begin{bmatrix}0\\1\end{bmatrix}.
$$

Examples from page 12:

$$
\begin{bmatrix}2\\1\end{bmatrix}=2\vec e_1+\vec e_2,
\qquad
\begin{bmatrix}1\\3\end{bmatrix}=\vec e_1+3\vec e_2.
$$

Basis vectors are **not unique**. A basis for $\mathbb R^n$ contains $n$ vectors, but they do not have to be the standard unit vectors.

### 7.4 The larger basis exercise

Page 30 asks us to find a basis from a list of four-component vectors. The reading of that list is:

| Vector | Components |
|---|---|
| $v_1$ | $(6,3,8,4)$ |
| $v_2$ | $(1,2,3,4)$ |
| $v_3$ | $(9,4,7,10)$ |
| $v_4$ | $(-3,1,1,1)$ |
| $v_5$ | $(3,-1,-1,-1)$ |
| $v_6$ | $(14,7,12,17)$ |
| $v_7$ | $(11,8,13,18)$ |
| $v_8$ | $(7,0,1,2)$ |
| $v_9$ | $(2,-3,-4,-5)$ |
| $v_{10}$ | $(7,7,4,15)$ |

**Handwriting check:** A few digits in this exercise are less clear than in the rest of the document, especially the first entry of $v_3$ and the first entry of $v_7$. Check this table against page 30 before using it as an answer key.

To solve the exercise, place the vectors into matrix columns, find pivot columns by row reduction, and take the corresponding **original** columns as a basis for the column space. Using the readings above, the matrix has rank 4. The handwritten suggestion of rank 2 should not be treated as a general rule: the number of basis vectors equals the actual dimension of the span.

## 8. Matrices and linear transformations

*Original: pages 13-15 and 18.*

A matrix is a rectangular arrangement of numbers. It can store data or transform a vector.

The notes first describe a car using attributes such as engine capacity, number of doors, and colour. For a numerical matrix, categories such as colour need a numerical representation; they cannot simply be treated as numerical distances.

### 8.1 Equations as a matrix

$$
x-y=1,\qquad 2x+y=5
$$

can be written as:

$$
\underbrace{\begin{bmatrix}1&-1\\2&1\end{bmatrix}}_A
\underbrace{\begin{bmatrix}x\\y\end{bmatrix}}_{\text{input}}
=\underbrace{\begin{bmatrix}1\\5\end{bmatrix}}_{\text{output}}.
$$

The solution is $x=2$, $y=1$.

### 8.2 What do matrix columns mean?

Applying $A$ to the standard basis gives:

$$
A\begin{bmatrix}1\\0\end{bmatrix}=\begin{bmatrix}1\\2\end{bmatrix},
\qquad
A\begin{bmatrix}0\\1\end{bmatrix}=\begin{bmatrix}-1\\1\end{bmatrix}.
$$

These are exactly the columns of $A$. **Each column tells us where a standard basis vector goes.**

![Standard basis vectors and their transformed positions](assets/matrix-transformation.png)

A linear transformation keeps the origin fixed. Straight lines remain straight or can collapse to a point. A general matrix can rotate, stretch, shear, reflect, or collapse directions; it need not be a pure rotation.

### 8.3 Data as a matrix

The convention used in these notes is:

- Rows = samples or observations.
- Columns = features or attributes.

For three example observations on page 15:

$$
X=\begin{bmatrix}
150&45&12\\
155&60&24\\
170&65&6
\end{bmatrix}.
$$

The attributes are height, weight, and hair length. A sample is a vector such as $(150,45,12)$.

The original table contains two further observations, $(185,90,8)$ and $(173,75,9)$, plus handwritten M/F labels. Those label marks are not needed for the matrix operations and some are unclear, so they are not guessed here. This example illustrates rows and columns, not a reliable method of inferring a person's sex or gender from appearance.

> **Correction - page 15:** The later feature-wise matrix appears to write 85 where the earlier table has 65. The numerical example above follows the original table's 65.

Images are another example: a grayscale image can be represented by a matrix of pixel values. Colour images typically have multiple channels. Models can use numerical image representations for recognition tasks.

## 9. Matrix operations and types

*Original: pages 15-18.*

### 9.1 Shape

A matrix of shape $m\times n$ has $m$ rows and $n$ columns.

### 9.2 Addition, subtraction and scalar multiplication

Addition and subtraction require the same shape. Work element by element:

$$
\begin{bmatrix}1&2\\3&4\end{bmatrix}
+\begin{bmatrix}5&6\\7&8\end{bmatrix}
=\begin{bmatrix}6&8\\10&12\end{bmatrix}.
$$

Negation changes every sign:

$$
-\begin{bmatrix}1&3\\2&4\end{bmatrix}
=\begin{bmatrix}-1&-3\\-2&-4\end{bmatrix}.
$$

Scalar multiplication multiplies every entry:

$$
2\begin{bmatrix}1&3\\2&4\end{bmatrix}
=\begin{bmatrix}2&6\\4&8\end{bmatrix}.
$$

### 9.3 Matrix multiplication

The inner dimensions must match:

$$
(m\times n)(n\times p)\longrightarrow(m\times p).
$$

Each output entry is a row-column dot product. The worked example on page 16 is:

$$
\begin{bmatrix}1&2\\4&5\\1&1\end{bmatrix}
\begin{bmatrix}1&2&3\\6&7&8\end{bmatrix}
=\begin{bmatrix}13&16&19\\34&43&52\\7&9&11\end{bmatrix}.
$$

For example, the top-left entry is $1(1)+2(6)=13$. The second row is $(4(1)+5(6),\;4(2)+5(7),\;4(3)+5(8))=(34,43,52)$.

> **Correction:** The bottom-right entry is $1(3)+1(8)=11$. The handwritten final value is unclear/incorrect there.

### 9.4 Matrix types

| Type | Meaning | Example |
|---|---|---|
| Square | Same number of rows and columns | Any $3\times3$ matrix |
| Symmetric | $A=A^T$ | Entries mirror across the main diagonal |
| Upper triangular | Entries below the main diagonal are zero | See $U$ below |
| Lower triangular | Entries above the main diagonal are zero | See $L$ below |
| Diagonal | Off-diagonal entries are zero | $\operatorname{diag}(1,2,3)$ |
| Identity | Diagonal entries 1, all others 0 | $I$ |

$$
U=\begin{bmatrix}1&2&3\\0&4&5\\0&0&6\end{bmatrix},\quad
L=\begin{bmatrix}1&0&0\\2&4&0\\3&5&6\end{bmatrix},\quad
I=\begin{bmatrix}1&0&0\\0&1&0\\0&0&1\end{bmatrix}.
$$

> **Correction - page 16:** The matrix drawn under “symmetric” has some mismatched off-diagonal pairs. The definition is $a_{ij}=a_{ji}$, not merely “rows = columns”. Square does not automatically mean symmetric.

### 9.5 Useful properties

For compatible dimensions:

$$
\begin{aligned}
A+B&=B+A,\\
A+(B+C)&=(A+B)+C,\\
A(BC)&=(AB)C,\\
(A+B)C&=AC+BC,\\
A(B+C)&=AB+AC,\\
I_mA&=AI_n=A\quad\text{for }A\in\mathbb R^{m\times n}.
\end{aligned}
$$

In general, $AB\ne BA$; sometimes one product is not even defined.

> **Correction - page 17:** The second distributive rule ends with $AC$, not $BC$.

### 9.6 Transpose

Transpose means interchange rows and columns:

$$
\begin{bmatrix}1&2&3\\4&5&6\end{bmatrix}^T
=\begin{bmatrix}1&4\\2&5\\3&6\end{bmatrix}.
$$

$$
(A^T)^T=A,\quad (A+B)^T=A^T+B^T,\quad
(AB)^T=B^TA^T,\quad (kA)^T=kA^T.
$$

Remember to **reverse the order** when transposing a product.

## 10. Rank, null space and nullity

*Original: pages 19-22.*

### 10.1 Why do we need rank?

The notes ask:

1. Are all features important?
2. Can we reduce the data matrix by removing unnecessary features?
3. How do we find correlation and linear relationships?

The car example lists speed, engine power, engine capacity, mileage, fuel type, and number of doors. Domain knowledge helps us understand relationships; the notes also mention power = torque × angular velocity.

**Clarification:** Rank measures **exact linear dependence** in the represented matrix. It does not automatically establish feature importance, statistical independence, causation, or every nonlinear relationship. A relationship such as mileage = a function of engine characteristics need not be linear.

### 10.2 Rank

Rank is the number of linearly independent columns. It is also the number of linearly independent rows.

For:

$$
A=\begin{bmatrix}1&2&1\\3&6&0\\5&10&1\end{bmatrix},
$$

column 2 is twice column 1. Column 3 contributes a different direction, so $\operatorname{rank}(A)=2$.

### 10.3 Null space

The null space contains all coefficient vectors that become zero when multiplied by $A$:

$$
\operatorname{Null}(A)=\{\vec z:A\vec z=\vec0\}.
$$

If the columns of $A$ are features, a null-space vector gives coefficients of a linear relationship between those features.

**Nullity** is the **dimension** of the null space - the number of vectors in a basis for it.

> **Correction - page 20:** The zero vector belongs to the null space. Nullity is not the total number of vectors in it. A one-dimensional null space contains infinitely many real vectors but has nullity 1.

### 10.4 Rank-nullity theorem

For an $m\times n$ matrix:

$$
\operatorname{rank}(A)+\operatorname{nullity}(A)=n.
$$

The right side is the **number of columns**, not the number of rows.

### 10.5 Worked examples

**Example 1 - independent columns**

$$
A=\begin{bmatrix}1&2\\2&7\\5&6\end{bmatrix}.
$$

There are two independent columns: rank = 2, nullity = $2-2=0$. Only $\vec z=0$ solves $A\vec z=0$.

**Example 2 - dependent columns**

$$
A=\begin{bmatrix}1&2&1\\2&4&0\\4&8&1\end{bmatrix}.
$$

Column 2 = twice column 1, so rank = 2 and nullity = 1.

To find the null space, solve:

$$
\begin{aligned}
z_1+2z_2+z_3&=0,\\
2z_1+4z_2&=0,\\
4z_1+8z_2+z_3&=0.
\end{aligned}
$$

From the second equation, $z_1=-2z_2$. Substitution gives $z_3=0$. Therefore:

$$
\vec z=t\begin{bmatrix}-2\\1\\0\end{bmatrix},\qquad t\in\mathbb R.
$$

This says $-2\times\text{column 1}+\text{column 2}=0$.

The intermediate matrix on page 21 with rows $(1,2,3)$, $(2,3,4)$, and $(5,6,7)$ illustrates the same idea: it has the dependence “column 1 - 2 column 2 + column 3 = 0”, rank 2, and nullity 1.

**Extra explanation:** Numerical rank depends on tolerance when columns are nearly dependent. In NumPy, `np.linalg.matrix_rank(A)` estimates rank using singular values.

## 11. Solving linear equations

*Original: pages 23-25.*

Write the system as:

$$
A\vec x=\vec b,\qquad
A\in\mathbb R^{m\times n},\quad
\vec x\in\mathbb R^n,\quad \vec b\in\mathbb R^m.
$$

### 11.1 Determinant and inverse

For a $2\times2$ matrix:

$$
A=\begin{bmatrix}a&b\\c&d\end{bmatrix},\qquad
\det(A)=ad-bc.
$$

If $\det(A)\ne0$:

$$
A^{-1}=\frac1{ad-bc}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}.
$$

The determinant measures **signed area scaling** in 2D. Its absolute value is the area scaling. In higher dimensions it gives signed volume scaling. For the identity matrix, the determinant is 1.

![The unit square and its transformed parallelogram](assets/determinant.png)

### 11.2 Cofactors and adjugate

For a square matrix, delete row $i$ and column $j$ to obtain the minor matrix $M_{ij}$. Its cofactor is:

$$
C_{ij}=(-1)^{i+j}\det(M_{ij}).
$$

For $A=\begin{bmatrix}a&b&c\\d&e&f\\g&h&i\end{bmatrix}$, examples from page 23 are:

$$
C_{11}=ei-fh,\quad C_{12}=-(di-fg),\quad C_{13}=dh-eg.
$$

The **adjugate** is the transpose of the complete cofactor matrix:

$$
\operatorname{adj}(A)=C^T,\qquad
A^{-1}=\frac{\operatorname{adj}(A)}{\det(A)}.
$$

> **Correction - page 23:** Do not forget the transpose when constructing the adjugate. An inverse exists only for a nonsingular square matrix.

### 11.3 A complete two-equation example

The notebook gives:

$$
3x+2y=10,\qquad 2x+5y=12.
$$

Here $\det(A)=15-4=11$, so:

$$
\begin{bmatrix}x\\y\end{bmatrix}
=\frac1{11}\begin{bmatrix}5&-2\\-2&3\end{bmatrix}
\begin{bmatrix}10\\12\end{bmatrix}
=\begin{bmatrix}26/11\\16/11\end{bmatrix}.
$$

### 11.4 Square, full-rank system

On page 24:

$$
\begin{bmatrix}1&3\\2&4\end{bmatrix}
\begin{bmatrix}x_1\\x_2\end{bmatrix}
=\begin{bmatrix}7\\10\end{bmatrix}.
$$

The determinant is $4-6=-2$. The inverse is:

$$
A^{-1}=\begin{bmatrix}-2&1.5\\1&-0.5\end{bmatrix}.
$$

Therefore $\vec x=(1,2)^T$. This solution is unique.

### 11.5 Singular and inconsistent system

On page 25:

$$
\begin{bmatrix}1&2\\3&6\end{bmatrix}\vec x
=\begin{bmatrix}10\\19\end{bmatrix}.
$$

The second left side is three times the first, so its right side would need to be 30, not 19. There is **no exact solution**.

If the right side were $(10,30)^T$, the system would instead have infinitely many solutions.

The single equation $2x+3y=0$ also has infinitely many solutions, for example $(x,y)=t(-3,2)$.

> **Correction - page 25:** This is different from $c_1(1,0)+c_2(0,1)=0$, which forces both coefficients to zero. Do not confuse one scalar equation with a vector equation containing two scalar equations.

## 12. Least squares and minimum-norm solutions

*Original: pages 24-28.*

The notes divide systems into three shapes. Shape helps us choose a method, but **rank and consistency also matter**.

| Shape | Typical situation | What to check |
|---|---|---|
| $m=n$ | Same number of equations and unknowns | Full rank gives a unique exact solution. |
| $m>n$ | More equations than unknowns | Exact fit may or may not exist; least squares finds the best residual fit. |
| $m<n$ | More unknowns than equations | If consistent, there are infinitely many exact solutions; choose one by an extra criterion. |

### 12.1 Least squares: minimize the residual

Let $\vec e=A\vec x-\vec b$. Minimize the sum of squared errors:

$$
f(\vec x)=\|A\vec x-\vec b\|_2^2
=(A\vec x-\vec b)^T(A\vec x-\vec b).
$$

Expand:

$$
f(\vec x)=\vec x^TA^TA\vec x-2\vec b^TA\vec x+\vec b^T\vec b.
$$

Differentiate and set the gradient to zero:

$$
\nabla f(\vec x)=2A^TA\vec x-2A^T\vec b=0,
$$

giving the **normal equations**:

$$
A^TA\vec x=A^T\vec b.
$$

If the columns of $A$ are independent:

$$
\vec x=(A^TA)^{-1}A^T\vec b.
$$

> **Correction - page 25:** $(A\vec x-\vec b)^T=\vec x^TA^T-\vec b^T$. A handwritten intermediate line reverses this sign. The final normal equations above use the corrected expansion.

### 12.2 An example with residual error

Using the matrix shown in the substitution on page 26 and repeated on page 27:

$$
A=\begin{bmatrix}1&0\\2&0\\3&1\end{bmatrix},\qquad
\vec b=\begin{bmatrix}1\\-0.5\\5\end{bmatrix}.
$$

The least-squares answer is $\vec x=(0,5)^T$, giving:

$$
A\vec x=\begin{bmatrix}0\\0\\5\end{bmatrix},\qquad
\vec e=\begin{bmatrix}-1\\0.5\\0\end{bmatrix},\qquad
\|\vec e\|^2=1.25.
$$

We cannot make every equation true, but we can minimize the total squared error.

**Source clarification:** The first matrix on page 26 appears to have 5 in its third row's first position, while its substitution and page 27 use 3. The calculation above consistently uses 3. The answer $(0,5)$ happens to be unchanged for this particular right side under either reading.

### 12.3 An overdetermined system can still fit exactly

Page 27 uses the same $A$ with $\vec b=(1,2,5)^T$. Then $\vec x=(1,2)^T$ satisfies all three equations exactly. “More equations than unknowns” does not automatically mean nonzero error.

### 12.4 Minimum-norm solution

When several vectors satisfy $A\vec x=\vec b$, choose the one with the smallest length:

$$
\min_{\vec x}\frac12\vec x^T\vec x
\quad\text{subject to}\quad A\vec x=\vec b.
$$

Use the Lagrangian:

$$
L(\vec x,\lambda)=\frac12\vec x^T\vec x+\lambda^T(A\vec x-\vec b).
$$

Differentiate with respect to $\vec x$:

$$
\vec x+A^T\lambda=0\quad\Rightarrow\quad\vec x=-A^T\lambda.
$$

Substitution gives $-AA^T\lambda=\vec b$. If the rows are independent:

$$
\lambda=-(AA^T)^{-1}\vec b,\qquad
\vec x=A^T(AA^T)^{-1}\vec b.
$$

> **Correction - pages 27-28:** The final formula has a **positive** sign. The two negative signs cancel.

For the page 28 example:

$$
A=\begin{bmatrix}1&2&3\\0&0&1\end{bmatrix},\qquad
\vec b=\begin{bmatrix}2\\1\end{bmatrix},
$$

the minimum-norm answer is:

$$
\vec x=\begin{bmatrix}-0.2\\-0.4\\1\end{bmatrix}.
$$

Check: $-0.2+2(-0.4)+3=2$ and $x_3=1$. It fits **exactly**, despite the handwritten remark “with some error”.

### 12.5 Moore-Penrose pseudoinverse

The pseudoinverse $A^+$ provides a general expression:

$$
\vec x=A^+\vec b.
$$

It gives the minimum-norm least-squares solution, including rank-deficient cases. Singular value decomposition (SVD) can be used to calculate it.

**Extra explanation - practical Python:** Use `np.linalg.solve` for a suitable square system, `np.linalg.lstsq` for least squares, or `np.linalg.pinv` for a pseudoinverse. Explicitly forming $(A^TA)^{-1}$ is useful for understanding the derivation but is usually not the best numerical implementation.

## 13. Projection onto a subspace

*Original: pages 31-32.*

Suppose a plane through the origin is spanned by $\vec v_1$ and $\vec v_2$. We want to project a vector $\vec x$ onto that plane:

$$
\hat{\vec x}=c_1\vec v_1+c_2\vec v_2.
$$

Write the original vector as:

$$
\vec x=\hat{\vec x}+\vec r.
$$

The residual $\vec r$ is perpendicular to the plane. Therefore:

$$
\vec v_1^T\vec r=0,\qquad \vec v_2^T\vec r=0.
$$

If the two spanning vectors are orthogonal:

$$
c_1=\frac{\vec v_1^T\vec x}{\vec v_1^T\vec v_1},\qquad
c_2=\frac{\vec v_2^T\vec x}{\vec v_2^T\vec v_2}.
$$

**Important:** Independence alone does not justify these separate coefficient formulas. They require an orthogonal basis.

### Worked example

$$
\vec x=\begin{bmatrix}1\\2\\3\end{bmatrix},\quad
\vec v_1=\begin{bmatrix}1\\-1\\-2\end{bmatrix},\quad
\vec v_2=\begin{bmatrix}2\\0\\1\end{bmatrix}.
$$

Check $\vec v_1^T\vec v_2=2-2=0$. Then:

$$
c_1=\frac{1-2-6}{1+1+4}=-\frac76,\qquad
c_2=\frac{2+3}{4+1}=1.
$$

So:

$$
\hat{\vec x}=-\frac76\begin{bmatrix}1\\-1\\-2\end{bmatrix}
+\begin{bmatrix}2\\0\\1\end{bmatrix}
=\begin{bmatrix}5/6\\7/6\\20/6\end{bmatrix}.
$$

> **Correction - page 32:** Multiply the coefficients by $\vec v_1$ and $\vec v_2$, not by the original $\vec x$ as one intermediate line suggests. The final projected vector above agrees with the handwritten final result.

The projected vector still has **three coordinates**, but lies in a **two-dimensional subspace**. Its coordinates relative to that plane's basis are the two numbers $(-7/6,1)$.

**Extra explanation:** For a full-column-rank, possibly non-orthogonal basis matrix $V$:

$$
\hat{\vec x}=V(V^TV)^{-1}V^T\vec x.
$$

## 14. Lines, planes, hyperplanes and halfspaces

*Original: pages 30-35.*

### 14.1 Equation of a line

The familiar form is:

$$
y=mx+c,\qquad m=\tan\theta.
$$

It can also be written:

$$
ax+by+c=0.
$$

Using $\vec x=(x,y)^T$ and normal vector $\vec w=(a,b)^T$:

$$
\vec w^T\vec x+c=0.
$$

The normal is perpendicular to the line. To see why, let $\vec x_1$ and $\vec x_2$ lie on the line. Subtract their equations:

$$
\vec w^T(\vec x_2-\vec x_1)=0.
$$

The displacement along the line has zero dot product with the normal.

### 14.2 Hyperplanes

In $\mathbb R^n$, a hyperplane has dimension $n-1$ and can be written as:

$$
\vec w^T\vec x+b=0,\qquad \vec w\ne0.
$$

- In 2D: a line.
- In 3D: a plane.
- In higher dimensions: the same idea, with more coordinates.

> **Correction - page 33:** Hyperplanes are not only objects “above 2D”. A line in 2D is also a hyperplane.

### 14.3 Positive and negative halfspaces

![A line dividing the plane into positive and negative halfspaces](assets/halfspaces.png)

The sign tells us which side a point lies on:

$$
s(\vec x)=\vec w^T\vec x+b.
$$

| Value | Position |
|---|---|
| $s(\vec x)=0$ | On the boundary |
| $s(\vec x)>0$ | Positive side, towards the normal |
| $s(\vec x)<0$ | Negative side, opposite the normal |

The notebook example uses $\vec w=(1,3)^T$ and $b=4$:

$$
x_1+3x_2+4=0.
$$

For example, $(0,0)$ gives 4, so it lies on the positive side. $(0,-2)$ gives -2, so it lies on the negative side.

### 14.4 Why does the sign work?

Take a point $\vec x_0$ on the boundary and write another point as $\vec x=\vec x_0+\vec d$:

$$
\begin{aligned}
\vec w^T\vec x+b
&=\vec w^T\vec x_0+b+\vec w^T\vec d\\
&=\vec w^T\vec d\\
&=\|\vec w\|\|\vec d\|\cos\theta.
\end{aligned}
$$

So the sign comes from the angle between the normal and the **displacement from the boundary**, not necessarily the point's position vector from the origin.

The angle between two vectors is conventionally in $[0^\circ,180^\circ]$: acute gives positive cosine, obtuse gives negative cosine. The full-circle diagram on page 35 expresses the same cosine-sign idea using directed angles.

**Clarification:** We may reverse the normal, but must also reverse $b$: $(\vec w,b)$ and $(-\vec w,-b)$ describe the same boundary and swap positive/negative side labels. A normal cannot point in an arbitrary direction; it must remain perpendicular to the boundary.

## 15. Eigenvalues and eigenvectors

*Original: pages 35-38.*

### 15.1 The idea

Usually, multiplying by a matrix changes a vector's direction. Are there special directions that stay on the same line?

Yes. A nonzero vector $\vec v$ is an eigenvector when:

$$
A\vec v=\lambda\vec v.
$$

$\lambda$ is its eigenvalue. The transformation only scales that vector:

- $0<\lambda<1$: shrinks it.
- $\lambda>1$: stretches it.
- $\lambda=1$: leaves it unchanged.
- $\lambda<0$: also reverses its orientation.
- $\lambda=0$: sends it to zero.

The last three cases clarify the original “direction remains the same” wording. Eigenvectors preserve their **line**, but a negative eigenvalue reverses the arrow, and zero collapses it.

### 15.2 Finding eigenvalues

Rearrange:

$$
(A-\lambda I)\vec v=0.
$$

For a nonzero $\vec v$ to exist, $A-\lambda I$ must be singular:

$$
\det(A-\lambda I)=0.
$$

At an eigenvalue, the nullity of $A-\lambda I$ is at least 1. It is **not** correct to say the “rank of the null space” must be at least 1.

### 15.3 Worked example

The notebook uses:

$$
A=\begin{bmatrix}8&7\\2&3\end{bmatrix}.
$$

Its characteristic equation is:

$$
\begin{aligned}
\det(A-\lambda I)
&=(8-\lambda)(3-\lambda)-14\\
&=\lambda^2-11\lambda+10\\
&=(\lambda-1)(\lambda-10)=0.
\end{aligned}
$$

So the eigenvalues are **1 and 10**.

**For $\lambda=1$:**

$$
(A-I)\vec v=0\quad\Rightarrow\quad v_1+v_2=0.
$$

Choose $\vec v=(1,-1)^T$. A unit version is:

$$
\hat{\vec v}=\frac1{\sqrt2}\begin{bmatrix}1\\-1\end{bmatrix}.
$$

**For $\lambda=10$:**

$$
-2v_1+7v_2=0.
$$

Choose $\vec v=(7,2)^T$. A unit version is:

$$
\hat{\vec v}=\frac1{\sqrt{53}}\begin{bmatrix}7\\2\end{bmatrix}.
$$

Check:

$$
A\begin{bmatrix}1\\-1\end{bmatrix}=\begin{bmatrix}1\\-1\end{bmatrix},\qquad
A\begin{bmatrix}7\\2\end{bmatrix}=\begin{bmatrix}70\\20\end{bmatrix}.
$$

> **Corrections - pages 36-37:** Eigenvectors do **not** have to be unit vectors; normalization is a useful choice. For $\lambda=1$, the second component must have the opposite sign to the first. $(1,1)^T/\sqrt2$ is not an eigenvector of this matrix.

### 15.4 Symmetric matrices

For a **real symmetric** $n\times n$ matrix:

- All eigenvalues are real.
- We can choose $n$ real orthonormal eigenvectors.
- Eigenvectors with zero eigenvalue span the null space.
- Eigenvectors with nonzero eigenvalues span the column space.

The notebook's final example is:

$$
A=\begin{bmatrix}
0.36&0.48&0\\
0.48&0.64&0\\
0&0&2
\end{bmatrix}.
$$

Its eigenpairs are:

| Eigenvalue | Unit eigenvector |
|---|---|
| $0$ | $(-0.8,0.6,0)^T$ |
| $1$ | $(0.6,0.8,0)^T$ |
| $2$ | $(0,0,1)^T$ |

For example:

$$
A\begin{bmatrix}-0.8\\0.6\\0\end{bmatrix}
=\begin{bmatrix}-0.288+0.288\\-0.384+0.384\\0\end{bmatrix}
=\vec0.
$$

There is one zero eigenvalue: nullity = 1 and rank = 2. The last two eigenvectors span the **column space**, not all of $\mathbb R^3$.

**Extra explanation:** Symmetric matrices matter in data science because covariance matrices are symmetric. Their eigenvectors describe principal directions; this connects to PCA.

## 16. Quick revision

| Concept | Remember it this way |
|---|---|
| Vector | Amount plus direction; coordinates encode it. |
| Unit vector | Divide a nonzero vector by its length. |
| Dot product | Multiply matching coordinates and add. |
| Orthogonal | Dot product is zero. |
| Projection | The part of one vector along another direction/subspace. |
| Basis | Independent directions that span the space. |
| Matrix columns | Where the standard basis vectors go. |
| Rank | Number of independent column directions. |
| Null space | Coefficients that make $A\vec z=0$. |
| Nullity | Dimension of the null space. |
| Least squares | Make the total squared residual as small as possible. |
| Minimum norm | Choose the shortest solution among exact solutions. |
| Hyperplane | A boundary described by $\vec w^T\vec x+b=0$. |
| Eigenvector | A nonzero direction scaled by a matrix. |

### Small self-check

1. What is the difference between a dot product and a scalar projection?
2. If a matrix has 5 columns and rank 3, what is its nullity?
3. Can a system with more equations than unknowns fit exactly?
4. Is a square matrix always symmetric?
5. Must an eigenvector have length 1?

<details>
<summary>Show answers</summary>

1. The scalar projection onto $\vec b$ is $(\vec a^T\vec b)/\|\vec b\|$; the dot product has not yet been divided by that length.
2. $5-3=2$.
3. Yes, if the right-hand side lies in the column space.
4. No; symmetry requires $A=A^T$.
5. No. It must be nonzero; normalization is optional.

</details>

## 17. Original-page reading map and corrections

Use this if you want to compare the Markdown with the [original 38-page notebook](Linear%20Algebra%20%26%20Matrices.pdf). Repeated recap material is combined above rather than copied twice.

| PDF pages | Where the content appears |
|---|---|
| 1 | Section 1: scalars and vector types |
| 2-3 | Section 2: addition, subtraction, and properties; Section 3: axes |
| 4-5 | Sections 2-3: components, magnitude, and resultant derivation |
| 6-7 | Section 4: dot product, angle, and projection examples |
| 8 | Sections 4-5: projection direction and norms |
| 9-10 | Section 6: coordinate change; Section 7: combinations |
| 11-12 | Section 7: independence and basis |
| 13-14 | Section 8: matrices, transformed basis, and data layout |
| 15-16 | Sections 8-9: sample table and matrix arithmetic |
| 17-18 | Section 9: matrix types, algebra, transpose; Section 8: image data |
| 19 | Section 10: feature relationships and rank |
| 20-22 | Section 10: null space, rank-nullity, and worked examples |
| 23-24 | Section 11: inverse, determinant, adjugate, and square systems |
| 25-26 | Sections 11-12: inconsistency and least-squares derivation |
| 27-28 | Section 12: exact overdetermined fit, minimum norm, pseudoinverse |
| 29 | Sections 3-4: vector recap, distance, unit direction, orthogonality |
| 30 | Sections 7 and 14: larger basis exercise and normal form of a line |
| 31-32 | Sections 13-14: subspace projection and line equation |
| 33-34 | Section 14: hyperplanes, halfspaces, and sign derivation |
| 35 | Section 14: cosine signs; Section 15: eigenvector intuition |
| 36-37 | Section 15: characteristic equation and worked eigenpairs |
| 38 | Section 15: symmetric matrices, null space, and column space |

### Items to review against the handwriting

- **Page 15:** The numerical table is transcribed; unclear M/F marks are not guessed. A later 85/65 discrepancy is identified above.
- **Page 26:** One matrix entry varies between the first display and its substitution; the chosen reading is stated in Section 12.
- **Page 30:** The long basis-exercise vector list has a few less-clear digits. The numerical rank statement is conditional on the listed readings.

### Mathematical corrections made explicit

The corrections in the relevant sections cover the missing square root, dot product versus projection, inconsistent angle, coordinate signs, independence labels, matrix arithmetic and symmetry, distributivity, nullity, adjugate transpose, least-squares signs, minimum-norm signs, projection assumptions, hyperplane definition, eigenvector normalization and eigenvector sign.

The original PDF remains the source record. This Markdown is an edited learning version, not a claim of character-for-character transcription.
