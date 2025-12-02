import pytest
from hypothesis import given, strategies as st, assume
from buggy_function import binomial_Coeff

@given(st.integers(min_value=0, max_value=10), st.integers(min_value=0, max_value=10))
def test_symmetry_property(n, k):
    """C(n, k) == C(n, n-k)"""
    if k <= n:
        assert binomial_Coeff(n, k) == binomial_Coeff(n, n - k)

@given(st.integers(min_value=0, max_value=10), st.integers(min_value=0, max_value=10))
def test_zero_and_n_property(n, k):
    """C(n, 0) == C(n, n) == 1 for valid n"""
    if k == 0 and n >= 0:
        assert binomial_Coeff(n, k) == 1
    if n == k and n >= 0:
        assert binomial_Coeff(n, k) == 1

@given(st.integers(min_value=0, max_value=10), st.integers(min_value=0, max_value=10))
def test_pascal_triangle_property(n, k):
    """C(n, k) = C(n-1, k-1) + C(n-1, k)"""
    if n >= 1 and 0 < k < n:
        assert binomial_Coeff(n, k) == binomial_Coeff(n - 1, k - 1) + binomial_Coeff(n - 1, k)

@given(st.integers(min_value=-10, max_value=-1), st.integers(min_value=0, max_value=5))
def test_negative_n_returns_minus_one(n, k):
    """Negative n should return -1 (documenting the bug)"""
    result = binomial_Coeff(n, k)
    assert result == -1

@given(st.integers(min_value=0, max_value=10), st.integers(min_value=-5, max_value=-1))
def test_negative_k_returns_minus_one(n, k):
    """Negative k should return -1 (documenting the bug)"""
    result = binomial_Coeff(n, k)
    assert result == -1

@given(st.integers(min_value=0, max_value=10), st.integers(min_value=11, max_value=20))
def test_k_greater_than_n(n, k):
    """C(n, k) should be 0 when k > n"""
    assume(k > n)
    assert binomial_Coeff(n, k) == 0

@given(st.integers(min_value=-5, max_value=-1), st.integers(min_value=-5, max_value=-1))
def test_both_negative(n, k):
    """Both negative should return -1 (bug behavior)"""
    result = binomial_Coeff(n, k)
    assert result == -1

@given(st.integers(min_value=0, max_value=15))
def test_diagonal_elements(n):
    """C(n, 1) should equal n"""
    if n >= 1:
        assert binomial_Coeff(n, 1) == n
