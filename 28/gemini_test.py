import pytest
from buggy_function import binomial_Coeff
# Assume the function 'binomial_Coeff' is defined elsewhere and needs testing.
# def binomial_Coeff(n: int, k: int) -> int:
#     # ... implementation ...
#     pass


@pytest.mark.parametrize(
    "n, k, expected",
    [
        # --- Base Cases and Identities ---
        # 1. C(n, 0) = 1 (Selecting zero items)
        (5, 0, 1),
        (100, 0, 1),
        # 2. C(n, n) = 1 (Selecting all items)
        (5, 5, 1),
        (100, 100, 1),
        # 3. C(n, 1) = n (Selecting one item)
        (5, 1, 5),
        (10, 1, 10),
        # 4. C(n, n-1) = n (Selecting all but one item)
        (5, 4, 5),
        (10, 9, 10),

        # --- Standard Calculation Cases (Pascal's Triangle) ---
        # 5. C(5, 2) = 10
        (5, 2, 10),
        # 6. C(5, 3) = 10 (Symmetry check: C(n, k) = C(n, n-k))
        (5, 3, 10),
        # 7. C(10, 3) = (10*9*8)/(3*2*1) = 120
        (10, 3, 120),
        # 8. C(6, 3) = (6*5*4)/(3*2*1) = 20
        (6, 3, 20),
        # 9. Larger number
        # C(15, 5) = (15*14*13*12*11)/(5*4*3*2*1) = 3003
        (15, 5, 3003),
        # 10. Large input, small k
        (50, 2, 1225),  # (50 * 49) / 2 = 1225
        # 11. Large input, k close to n
        (50, 48, 1225), # C(50, 48) = C(50, 2) = 1225
        # 12. Larger result
        # C(20, 10) = 184756
        (20, 10, 184756),
    ]
)
def test_binomial_Coeff_correctness(n: int, k: int, expected: int):
    """Tests for correct calculation of binomial coefficients for valid inputs."""
    assert binomial_Coeff(n, k) == expected

# ---

def test_binomial_Coeff_minimum_case():
    """Tests the smallest possible valid inputs C(0, 0) = 1."""
    assert binomial_Coeff(0, 0) == 1

# ---

@pytest.mark.parametrize(
    "n, k",
    [
        # 1. k > n (k is out of range)
        (5, 6),
        (10, 11),
        (0, 1),
        # 2. k < 0 (k is negative)
        (5, -1),
        (10, -5),
    ]
)
def test_binomial_Coeff_invalid_k_zero(n: int, k: int):
    """
    Tests cases where k is invalid (k > n or k < 0).
    The expected behavior for these mathematical definitions is 0.
    A good implementation should handle this boundary condition gracefully.
    """
    # Mathematical definition: C(n, k) = 0 if k > n or k < 0
    assert binomial_Coeff(n, k) == 0

# ---

@pytest.mark.parametrize(
    "n, k",
    [
        # n < 0 (n is negative)
        (-1, 0),
        (-5, 2),
    ]
)
def test_binomial_Coeff_invalid_n_error(n: int, k: int):
    """
    Tests cases where n is negative.
    Since the specification implies standard integer inputs, an implementation
    might raise a ValueError or return 0, depending on the required behavior
    for negative n (often undefined or complex in basic combinatorial context).
    We test for a ValueError as it's common for invalid inputs.
    """
    # If the function is expected to raise an error for negative n:
    with pytest.raises(ValueError):
        binomial_Coeff(n, k)
    
    # If the function is expected to return 0 for negative n (less common):
    # assert binomial_Coeff(n, k) == 0