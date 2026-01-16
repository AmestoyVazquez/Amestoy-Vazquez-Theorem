"""
verification of the Amestoy-Vázquez  -  mathematical verification
"""
import numpy as np

def print_header(text):
    """Pretty print header"""
    print("\n" + "="*60)
    print(text)
    print("="*60)

def classical_formula(n):
    """The well-known magic square formula"""
    return n * (n**2 + 1) / 2

def amestoy_vazquez_formula(n, d, a):
    """Our proposed generalization"""
    return n * a + (n * (n**d - 1)) / 2

def generate_simple_magic_square(n, start=1):
    """
    Generate magic square using simple method for ODD n only
    Returns square AND its actual magic constant
    """
    if n % 2 == 0:
        return None, None  # Only works for odd n
    
    # Initialize
    square = [[0] * n for _ in range(n)]
    num = start
    
    # Start position (traditional Siamese method)
    i, j = 0, n // 2
    
    # Fill the square
    for _ in range(n * n):
        square[i][j] = num
        num += 1
        
        # Calculate next position
        next_i = (i - 1) % n
        next_j = (j + 1) % n
        
        # If cell is occupied, move down instead
        if square[next_i][next_j] != 0:
            i = (i + 1) % n
        else:
            i, j = next_i, next_j
    
    # Calculate actual magic constant (sum of first row)
    actual_constant = sum(square[0])
    
    return square, actual_constant

def verify_single_case(n, start):
    """Verify one specific case"""
    print(f"\nTesting n={n}, starting at {start}")
    print("-" * 40)
    
    # Generate actual magic square
    square, actual = generate_simple_magic_square(n, start)
    
    if square is None:
        print(f"  Skipping: n={n} is even (need odd for simple method)")
        return False
    
    # Calculate with our formula
    predicted = amestoy_vazquez_formula(n, d=2, a=start)
    
    # Classical formula (only for comparison when start=1)
    if start == 1:
        classical = classical_formula(n)
        print(f"  Classical formula: {classical}")
    
    # Display results
    print(f"  Actual constant:    {actual}")
    print(f"  Our prediction:     {predicted}")
    
    # Check match
    error = abs(actual - predicted)
    matches = error < 0.0001
    
    if matches:
        print(f"  Result: ✓ MATCH (error: {error:.10f})")
    else:
        print(f"  Result: ✗ NO MATCH (error: {error:.10f})")
    
    return matches

def main():
    """Main verification"""
    print_header("AMESTOY-VÁZQUEZ MATHEMATICAL VERIFICATION")
    print("Goal: Verify the generalization works mathematically")
    print("Method: Compare formula against ACTUAL magic squares\n")
    
    # Test cases
    test_cases = [
        (3, 1),     # Classical case - should match known formula
        (3, 100),   # Different starting point
        (3, -5),    # Negative numbers
        (5, 500.5), # Decimal starting point
        (7, 0),     # Starting at zero
        (9, 1000),  # Large starting value
    ]
    
    results = []
    
    for n, start in test_cases:
        success = verify_single_case(n, start)
        results.append(success)
    
    print_header("VERIFICATION SUMMARY")
    
    passed = sum(results)
    total = len(results)
    
    print(f"Passed: {passed}/{total} test cases")
    
    if passed == total:
        print("✓ All tests passed! The formula holds for tested cases.")
        print("\nNEXT STEP: Mathematical proof and extension to even n.")
    else:
        print("⚠ Some tests failed. Need to investigate.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
