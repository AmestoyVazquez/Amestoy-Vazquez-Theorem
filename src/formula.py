"""
Amestoy-Vázquez Conjecture Implementation
Author: Juan Pedro Amestoy Vazquez
Email: juanpedroamestoy@gmail.com
"""

def amestoy_vazquez_constant(n: int, d: int, a: float) -> float:
    """
    Calculate magic constant using Amestoy-Vázquez formula.
    
    Formula: S(n,d,a) = n·a + n(n^d - 1)/2
    
    Parameters:
    -----------
    n : int
        Order of the hypercube
    d : int
        Number of dimensions (2 for square, 3 for cube, etc.)
    a : float
        Starting value of arithmetic progression
        
    Returns:
    --------
    float
        Magic constant
        
    Examples:
    ---------
    >>> amestoy_vazquez_constant(3, 2, 1)
    15.0
    
    >>> amestoy_vazquez_constant(5, 3, 500.5)
    2812.5
    
    >>> amestoy_vazquez_constant(4, 2, 50)
    230.0
    """
    return n * a + (n * (n**d - 1)) / 2


def classical_magic_constant(n: int) -> float:
    """
    Classical magic square formula (special case: d=2, a=1).
    
    Formula: S = n(n² + 1)/2
    
    Parameters:
    -----------
    n : int
        Order of magic square
        
    Returns:
    --------
    float
        Classical magic constant
    """
    return n * (n**2 + 1) / 2


def verify_classical_case(n: int) -> bool:
    """
    Verify that Amestoy-Vázquez reduces to classical formula.
    
    Parameters:
    -----------
    n : int
        Order to test
        
    Returns:
    --------
    bool
        True if formulas match
    """
    import math
    classical = classical_magic_constant(n)
    av = amestoy_vazquez_constant(n, 2, 1)
    return math.isclose(classical, av, rel_tol=1e-10)


if __name__ == "__main__":
    # Demo when run directly
    print("Amestoy-Vázquez Conjecture Demo")
    print("=" * 40)
    
    test_cases = [
        (3, 2, 1, 15.0),
        (3, 2, 100, 315.0),
        (5, 3, 500.5, 2812.5),
        (4, 2, 50, 230.0),
    ]
    
    for n, d, a, expected in test_cases:
        result = amestoy_vazquez_constant(n, d, a)
        status = "✓" if abs(result - expected) < 1e-10 else "✗"
        print(f"{status} S({n},{d},{a}) = {result}")
