from bugged_code import opposite_Signs
from hypothesis import given, strategies as st

# Generate small integer pairs
ints = st.integers(min_value=-1000, max_value=1000)

@given(ints, ints)
def test_symmetry(x, y):
    """Property 1: opposite_Signs(x, y) == opposite_Signs(y, x)"""
    assert opposite_Signs(x, y) == opposite_Signs(y, x)

@given(ints, ints)
def test_same_signs_false(x, y):
    """Property 2: If both have same sign, should return False."""
    if (x >= 0 and y >= 0) or (x <= 0 and y <= 0):
        assert opposite_Signs(x, y) is False

@given(ints, ints)
def test_opposite_signs_true(x, y):
    """Property 3: If one is positive and other negative, should return True."""
    if (x > 0 and y < 0) or (x < 0 and y > 0):
        assert opposite_Signs(x, y) is True

@given(ints)
def test_zero_not_opposite(x):
    """Property 4: Zero with any number is not opposite in sign."""
    assert opposite_Signs(0, x) is False
    assert opposite_Signs(x, 0) is False
