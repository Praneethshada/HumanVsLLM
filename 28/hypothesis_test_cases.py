import pytest
from hypothesis import given, strategies as st
from buggy_function import binomial_Coeff

@given(st.integers(min_value=0, max_value=10), st.integers(min_value=0, max_value=10))
def test_symmetry_property(n, k):
    # C(n, k) == C(n, n-k)
    if k <= n:
        assert binomial_Coeff(n, k) == binomial_Coeff(n, n - k)

@given(st.integers(min_value=0, max_value=10), st.integers(min_value=0, max_value=10))
def test_zero_and_n_property(n, k):
    # C(n, 0) == C(n, n) == 1 for valid n
    if k == 0 and n >= 0:
        assert binomial_Coeff(n, k) == 1
    if n == k and n >= 0:
        assert binomial_Coeff(n, k) == 1

@given(st.integers(min_value=0, max_value=10), st.integers(min_value=0, max_value=10))
def test_invalid_case_returns_zero(n, k):
    # C(n, k) == 0 if k > n
    if k > n:
        assert binomial_Coeff(n, k) == 0
