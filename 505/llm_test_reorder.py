
import pytest
from bugged_reorder import re_order

def test_all_zeroes():
    # All elements are zero — should remain unchanged
    assert re_order([0, 0, 0, 0]) == [0, 0, 0, 0]

def test_no_zeroes():
    # No zeroes — should remain unchanged
    assert re_order([1, 2, 3, 4]) == [1, 2, 3, 4]

def test_mixed_elements():
    # Typical case with zeroes in between
    assert re_order([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]

def test_zeroes_at_start():
    # Zeroes only at the start
    assert re_order([0, 0, 5, 6]) == [5, 6, 0, 0]

def test_zeroes_at_end():
    # Zeroes already at the end — should remain unchanged
    assert re_order([4, 5, 6, 0, 0]) == [4, 5, 6, 0, 0]

def test_single_element_zero():
    # Single element which is zero
    assert re_order([0]) == [0]

def test_single_element_non_zero():
    # Single element which is non-zero
    assert re_order([7]) == [7]

def test_empty_list():
    # Empty input should return empty output
    assert re_order([]) == []

def test_with_duplicates_and_zeroes():
    # Multiple duplicates and zeroes
    assert re_order([1, 0, 2, 0, 2, 0, 3]) == [1, 2, 2, 3, 0, 0, 0]
