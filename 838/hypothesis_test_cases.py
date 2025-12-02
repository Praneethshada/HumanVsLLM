from hypothesis import given, strategies as st, assume
from buggy_function import min_Swaps

@given(st.text(alphabet='01', min_size=1, max_size=20))
def test_equal_strings_zero(s):
    """Equal strings should require 0 swaps"""
    assert min_Swaps(s, s) == 0

@given(st.text(alphabet='01', min_size=2, max_size=20))
def test_length_mismatch_fail(s):
    """Different length strings should return -1"""
    t = s + '0'
    result = min_Swaps(s, t)
    assert result == -1

@given(st.text(alphabet='01', min_size=2, max_size=20))
def test_swap_symmetry(s):
    """Swapping s to t should equal swapping t to s"""
    t = ''.join(reversed(s))
    if s != t:
        result1 = min_Swaps(s, t)
        result2 = min_Swaps(t, s)
        if result1 != -1 and result2 != -1:
            assert result1 == result2

@given(st.integers(min_value=1, max_value=10), st.integers(min_value=0, max_value=10))
def test_balanced_strings_zero_swaps(zeros, ones):
    """Strings with same count of 0s and 1s in same positions should need 0 swaps"""
    s = '0' * zeros + '1' * ones
    t = '0' * zeros + '1' * ones
    assert min_Swaps(s, t) == 0

@given(st.text(alphabet='01', min_size=2, max_size=15))
def test_result_is_non_negative_or_minus_one(s):
    """Result should always be non-negative or -1 for invalid cases"""
    t = ''.join(reversed(s))
    result = min_Swaps(s, t)
    assert result >= -1

@given(st.integers(min_value=2, max_value=10))
def test_alternating_pattern(n):
    """Test alternating patterns like 010101 to 101010 - exposes the bug"""
    assume(n >= 2)
    s = ('01' * n)[:n]
    t = ('10' * n)[:n]
    result = min_Swaps(s, t)
    if n % 2 == 0:
        expected = n // 2
    else:
        expected = (n + 1) // 2
    assert result == expected or result == expected + 1

@given(st.integers(min_value=2, max_value=10))
def test_all_zeros_to_mixed(n):
    """Test converting all zeros to mixed pattern"""
    assume(n % 2 == 0)
    s = '0' * n
    t = '01' * (n // 2)
    result = min_Swaps(s, t)
    expected = n // 2
    assert result == expected or result == expected + 1

@given(st.integers(min_value=3, max_value=10))
def test_odd_length_alternating_bug_case(n):
    """Specifically test odd-length patterns that trigger the bug"""
    assume(n % 2 == 1)
    s = '0' * ((n + 1) // 2) + '1' * (n // 2)
    t = '1' * (n // 2) + '0' * ((n + 1) // 2)
    result = min_Swaps(s, t)
    assert result >= 0 and result <= n
