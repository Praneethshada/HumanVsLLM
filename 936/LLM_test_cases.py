import pytest
from buggy_function import re_arrange_tuples

def test_basic_order():
    assert re_arrange_tuples([(4, 3), (1, 9), (2, 10), (3, 2)], [1, 4, 2, 3]) == [(1, 9), (4, 3), (2, 10), (3, 2)]

def test_duplicate_keys():
    # When duplicates appear, dict() drops one, which is a bug
    result = re_arrange_tuples([(3, 11), (3, 22), (4, 33)], [3, 4])
    assert result != [(3, 11), (4, 33)]  # Bug: only last (3, 22) retained

def test_missing_key():
    # Key missing in test_list should not cause missing or None value ideally
    result = re_arrange_tuples([(1, 5), (2, 6)], [1, 2, 3])
    assert result[-1] != (3, None)  # Bug: None should not appear

def test_correct_rearrangement():
    assert re_arrange_tuples([(6, 3), (3, 8), (5, 7), (2, 4)], [2, 5, 3, 6]) == [(2, 4), (5, 7), (3, 8), (6, 3)]

def test_empty_input():
    assert re_arrange_tuples([], []) == []
