import pytest
from buggy import re_arrange_array

def test_mbpp_examples():
    # These are the original MBPP tests (good for sanity)
    assert re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) == [-1, -3, -7, 4, 5, 6, 2, 8, 9]
    assert re_arrange_array([12, -14, -26, 13, 15], 5) == [-14, -26, 12, 13, 15]
    assert re_arrange_array([10, 24, 36, -42, -39, -78, 85], 7) == [-42, -39, -78, 10, 24, 36, 85]

def test_additional_examples():
    # These look like “normal” tests an LLM might write
    assert re_arrange_array([], 0) == []
    assert re_arrange_array([1, 2, 3], 3) == [1, 2, 3]
    assert re_arrange_array([-1, -2, -3], 3) == [-1, -2, -3]
    assert re_arrange_array([0, -1, 2], 3) == [-1, 0, 2]
