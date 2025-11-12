
import pytest
from hypothesis import given, strategies as st
from bugged_reorder import re_order

# Strategy: list of integers (can include zero and negative values)
@given(st.lists(st.integers(), max_size=100))
def test_length_is_preserved(A):
    """Property 1: The reordered list must have the same length as input."""
    result = re_order(A)
    assert len(result) == len(A)


@given(st.lists(st.integers(), max_size=100))
def test_all_original_elements_preserved(A):
    """Property 2: All elements except order of zeros should be preserved."""
    result = re_order(A)
    assert sorted(result) == sorted(A)


@given(st.lists(st.integers(), max_size=100))
def test_all_zeros_are_at_end(A):
    """All zeros, if present, should appear only at the end."""
    result = re_order(A)
    # Once a zero appears, there should be no non-zero after it
    seen_zero = False
    for x in result:
        if x == 0:
            seen_zero = True
        else:
            assert not seen_zero, f"Non-zero {x} found after zero in {result}"


@given(st.lists(st.integers(), max_size=100))
def test_order_of_non_zero_elements_preserved(A):
    """Order of non-zero elements must remain unchanged."""
    result = re_order(A)
    non_zero_original = [x for x in A if x != 0]
    non_zero_result = [x for x in result if x != 0]
    assert non_zero_original == non_zero_result


@given(st.lists(st.integers(), max_size=100))
def test_only_zeros_moved(A):
    """The only difference between input and output positions is the movement of zeros."""
    result = re_order(A)
    # Count of zeros should remain same
    assert A.count(0) == result.count(0)
