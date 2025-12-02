import pytest
from hypothesis import given, strategies as st
import math

from bugged_code import eulerian_num
# --- Property-Based Tests ---

# Strategy: We limit n to ~12 because standard recursion without 
# memoization gets very slow for larger Eulerian numbers.
valid_n = st.integers(min_value=1, max_value=12)

@given(n=valid_n)
def test_sum_equals_factorial(n):
    """
    Property 1: The Law of Totality
    The sum of all Eulerian numbers in row 'n' must equal n!
    Formula: sum(A(n, m) for m in 0..n-1) == n!
    """
    # Calculate the sum of the row based on your function
    row_sum = sum(eulerian_num(n, m) for m in range(n))
    
    # Check against the mathematical ground truth
    assert row_sum == math.factorial(n)


@given(n=valid_n)
def test_symmetry(n):
    """
    Property 2: The Law of Symmetry
    The Eulerian triangle is palindromic.
    Formula: A(n, m) == A(n, n - 1 - m)
    """
    # We check every 'm' in the row to ensure the whole row is symmetric
    for m in range(n):
        left = eulerian_num(n, m)
        right = eulerian_num(n, n - 1 - m)
        assert left == right, f"Asymmetry found at n={n}: A({n},{m}) != A({n},{n-1-m})"


@given(n=valid_n)
def test_first_value_is_one(n):
    """
    Property 3: The Ascending Identity
    For any n >= 1, the number of permutations with 0 ascents is always 1
    (e.g., [1, 2, 3, 4] is the only one).
    """
    assert eulerian_num(n, 0) == 1


@given(
    n=st.integers(min_value=1, max_value=20),
    m=st.integers(min_value=1, max_value=20)
)
def test_out_of_bounds_is_zero(n, m):
    """
    Property 4: The Boundary Law
    If m >= n, the result must be 0 (you cannot have n ascents in a list of size n).
    """
    # We force m to be >= n for this test
    if m < n:
        m = n + m  # Make sure m is definitely >= n
        
    assert eulerian_num(n, m) == 0


@given(n=st.integers(min_value=0, max_value=0))
def test_zero_implementation_behavior(n):
    """
    Property 5: Implementation Constraint
    Verifies that your specific code returns 0 for n=0.
    (Note: Mathematically A(0,0) is often 1, but this test enforces 
    YOUR code's specific logic).
    """
    assert eulerian_num(0, 0) == 0