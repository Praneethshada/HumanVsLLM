import pytest
from buggy import min_coins
import sys

def test_examples_from_spec():
    assert min_coins([9, 6, 5, 1], 4, 11) == 2
    assert min_coins([4, 5, 6, 7, 8, 9], 6, 9) == 1
    assert min_coins([1, 2, 3], 3, 4) == 2

def test_simple_values():
    assert min_coins([1], 1, 0) == 0
    assert min_coins([1], 1, 3) == 3
    assert min_coins([2, 4], 2, 3) == sys.maxsize  # cannot make 3 from {2,4}
