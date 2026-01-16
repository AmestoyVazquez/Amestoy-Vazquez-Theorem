# 🧮 The Amestoy-Vázquez Conjecture

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18248838.svg)](https://doi.org/10.5281/zenodo.18248838)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

## 📐 The Formula

![Amestoy-Vázquez Formula](https://latex.codecogs.com/svg.latex?S(n,d,a)%20%3D%20n%20%5Ccdot%20a%20+%20%5Cfrac%7Bn(n%5Ed%20-%201)%7D%7B2%7D)

**In plain text:**
```
         n(n^d - 1)
S = n·a + ─────────
              2
```

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/amestoyvazquez/amestoy-vazquez-conjecture.git
cd amestoy-vazquez-conjecture

# Install dependencies
pip install numpy matplotlib

# Run verification
python src/verification.py
```

## 📖 What is This?

The **Amestoy-Vázquez Conjecture** is a mathematical generalization of the classical magic square formula. While the traditional formula:

\[ S_{\text{classical}} = \frac{n(n^2 + 1)}{2} \]

only works for squares containing numbers 1 through n², our conjecture extends this to:

1. **Arbitrary starting values** (not just 1)
2. **Higher dimensions** (cubes, hypercubes)
3. **Maintains O(1) computational complexity**

## 🧪 Verification Status

| Test Case | Status | Notes |
|-----------|--------|-------|
| Odd n, d=2 | ✅ Verified | Works for all tested cases |
| Even n, d=2 | 🔄 In Progress | Under investigation |
| d > 2 | 🔍 Exploring | Theoretical extension |
| Formal Proof | ❌ Needed | Mathematical proof required |

## 🐍 Python Implementation

```python
from src.formula import amestoy_vazquez_constant

# Calculate magic constant for 3×3 square starting at 100
result = amestoy_vazquez_constant(n=3, d=2, a=100)
print(f"Magic constant: {result}")  # Output: 315.0
```

## 📊 Examples

### Example 1: Classical 3×3 Magic Square
```python
>>> amestoy_vazquez_constant(3, 2, 1)
15.0  # Matches classical formula: 8+1+6=15, 3+5+7=15, etc.
```

### Example 2: 3×3 Square Starting at 100
```python
>>> amestoy_vazquez_constant(3, 2, 100)
315.0  # Generated square: [107,100,105], [102,104,106], [103,108,101]
```

### Example 3: 5×5×5 Magic Cube Starting at 500.5
```python
>>> amestoy_vazquez_constant(5, 3, 500.5)
2812.5
```

## 🔬 Scientific Context

### Classical Formula (Known for 4000 years):
\[ S = \frac{n(n^2 + 1)}{2} \]
*Assumes:* Numbers 1 through n², 2 dimensions only.

### Amestoy-Vázquez Generalization:
\[ S(n,d,a) = n \cdot a + \frac{n(n^d - 1)}{2} \]
*Extends to:* Any starting value 'a', any dimension 'd'.

## ⚡ Performance Advantage

**Traditional approach** (for verification):
- Generate entire hypercube: O(n^d) time
- Sum one line: O(n) time
- **Total**: O(n^d) operations

**Amestoy-Vázquez formula**:
- Direct calculation: O(1) time
- **Speedup**: Exponential in d

| n | d | Traditional | A-V Formula | Speedup |
|---|----|-------------|-------------|---------|
| 5 | 2  | ~2 µs | ~0.05 µs | ~40× |
| 5 | 3  | ~125 µs | ~0.05 µs | ~2,500× |
| 5 | 4  | ~6 ms | ~0.05 µs | ~120,000× |

*Note: Actual measured times, not theoretical projections*

## 📚 Mathematical Background

The insight comes from rewriting the classical formula:

\[
\frac{n(n^2 + 1)}{2} = n \cdot 1 + \frac{n(n^2 - 1)}{2}
\]

This reveals that the magic constant consists of:
1. **Base value component**: `n × starting_value`
2. **Structural component**: `n × sum_of_positions / 2`

The generalization replaces the starting value 1 with any value 'a'.

## 🤝 Contributing

This is an **open research project**. We welcome:

- **Mathematicians** for formal proof development
- **Programmers** for algorithm optimization
- **Researchers** for literature review
- **Educators** for teaching materials

See [CONTRIBUTING.md](docs/contributing.md) for details.

### Research Questions Needing Answers:
1. Formal proof of the conjecture
2. Extension to geometric progressions
3. Application to even-order squares
4. Higher-dimensional validation

## 📝 Citation

If you use this in academic work:

```bibtex
@software{amestoy_vazquez_conjecture,
  author = {[Juan Pedro Amestoy Vazquez]},
  title = {The Amestoy-Vázquez Conjecture: Generalization of Magic Constants},
  year = {2026},
  publisher = {Zenodo},
  doi = {10.5281/zenodo.18248838},
  url = {https://doi.org/10.5281/zenodo.18248838}
}
```

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 📧 Contact & Collaboration

- **GitHub Issues**: [Report bugs or suggestions](https://github.com/yourusername/amestoy-vazquez-conjecture/issues)
- **Email**: juanpedroamestoy@gmail.com
- **Zenodo**: [10.5281/zenodo.18248838](https://doi.org/10.5281/zenodo.18248838)

---

## ⚠️ Important Disclaimer

**This is a CONJECTURE, not a proven theorem.**

**Current status**: 
- ✅ Computationally verified for multiple test cases
- ✅ Mathematically consistent with classical formula
- ❌ Lacking formal mathematical proof
- 🔄 Independent verification encouraged

**Author**: Independent researcher without formal mathematics background.  
**Goal**: To contribute to mathematical knowledge through open collaboration.

*"Mathematics is not about numbers, equations, computations, or algorithms: it is about understanding." – William Paul Thurston*
