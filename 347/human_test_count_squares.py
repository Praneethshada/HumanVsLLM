from hypothesis import given, strategies as st, settings
import pytest
from bugged_count_squares import count_Squares


@given(st.integers(min_value=0, max_value=500), st.integers(min_value=0, max_value=500))
def test_commutative(m, n):
    assert count_Squares(m, n) == count_Squares(n, m)

@given(st.integers(min_value=1, max_value=500), st.integers(min_value=1, max_value=500))
def test_non_negative_integer(m, n):
    result = count_Squares(m, n)
    assert isinstance(result, int)
    assert result >= 0

@given(st.integers(min_value=0, max_value=120), st.integers(min_value=0, max_value=120))
@settings(max_examples=300)
def test_canonical_sum_identity_inline(m, n):
    total = 0
    limit = m if m < n else n
    k = 1
    while k <= limit:
        total += (m - k + 1) * (n - k + 1)
        k += 1
    assert count_Squares(m, n) == total

@given(
    st.integers(min_value=0, max_value=200),
    st.integers(min_value=0, max_value=200),
    st.integers(min_value=0, max_value=500) 
)
def test_monotonicity(m, k, n):
    m2 = m + k
    assert count_Squares(m2, n) >= count_Squares(m, n)


@given(st.integers(min_value=0, max_value=400))
def test_square_grid(k):
    expected = k * (k + 1) * (2 * k + 1) // 6
    assert count_Squares(k, k) == expected
