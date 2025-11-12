from bugged_code import is_undulating
from hypothesis import given, strategies as st

# Strategy: generate integer inputs
ints = st.integers(min_value=0, max_value=10**6)


@given(ints)
def test_short_numbers_false(n):
    """
    Property 1: Numbers with <= 2 digits cannot be undulating.
    Because at least 3 digits are needed to form an 'abab...' pattern.
    """
    if n <= 100:  # 0–99 → too short
        assert is_undulating(n) is False


@given(ints)
def test_valid_undulating_pattern(n):
    """
    Property 2: A number formed by alternating two distinct digits
    (like 121212 or 8989) must always return True.
    """
    # Build a simple alternating pattern: 121212
    a, b = 1, 2
    num = int("".join(str(a if i % 2 == 0 else b) for i in range(65)))
    assert is_undulating(num) is True


@given(ints)
def test_repeated(n):
    a=n%10
    a=str(a)
    a=a*9
    a=int(a)
    assert is_undulating(a) is True


@given(ints)
def test_consistency(n):
    if is_undulating(n) and len(str(n))>=4 :
        assert is_undulating(n//10) is True
    
