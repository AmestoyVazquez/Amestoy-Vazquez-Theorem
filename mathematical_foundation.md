# Mathematical Foundation of the Amestoy-Vázquez Conjecture

## 1. Historical Context

### Classical Magic Squares
For a normal magic square of order n (containing numbers 1 through n²),
the magic constant S is given by:

\[
S_{\text{classical}} = \frac{n(n^2 + 1)}{2}
\]

**Assumptions:**
1. Numbers are consecutive integers: {1, 2, 3, ..., n²}
2. Square is of dimension 2
3. Sequence starts at 1

## 2. The Problem

What if we want:
1. Different starting numbers?
2. Higher dimensions (cubes, hypercubes)?
3. Decimal numbers or negative numbers?

## 3. The Insight

Notice that the classical formula can be rewritten as:

\[
S = n \cdot 1 + \frac{n(n^2 - 1)}{2}
\]

Where:
- First term: \(n \cdot 1\) → n times the starting value (1)
- Second term: \(\frac{n(n^2 - 1)}{2}\) → sum of the remaining progression

## 4. The Generalization

If we start at an arbitrary value 'a' instead of 1:

\[
S(n, 2, a) = n \cdot a + \frac{n(n^2 - 1)}{2}
\]

## 5. Extension to Higher Dimensions

For a d-dimensional magic hypercube with n elements along each dimension,
containing numbers {a, a+1, a+2, ..., a+(n^d - 1)}:

\[
\boxed{S(n, d, a) = n \cdot a + \frac{n(n^d - 1)}{2}}
\]

## 6. Verification for d=2 (Squares)

### Case 1: Classical (n=3, a=1)
\[
S = 3 \cdot 1 + \frac{3(3^2 - 1)}{2} = 3 + \frac{3(8)}{2} = 3 + 12 = 15 ✓
\]

### Case 2: Starting at 100 (n=3, a=100)
\[
S = 3 \cdot 100 + \frac{3(8)}{2} = 300 + 12 = 312
\]

Let's verify with actual square construction...

## 7. Why This is Non-Trivial

The formula works because:
1. Each line contains exactly one of each "position" in the progression
2. The sum of positions 0 through (n-1) in each dimension is constant
3. The arithmetic distributes linearly across all lines

## 8. Open Questions (Research Directions)

1. **Formal Proof**: Needs rigorous mathematical proof
2. **Arbitrary Differences**: What if step ≠ 1? (a, a+δ, a+2δ, ...)
3. **Geometric Progressions**: (a, ar, ar², ...)
4. **Mixed Progressions**: Different progressions in different dimensions
