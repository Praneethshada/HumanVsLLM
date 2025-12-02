import pytest
from bugged_max_sum import max_sum_of_three_consecutive

def test_single_element():
    assert max_sum_of_three_consecutive([5], 1) == 5


def test_two_elements():
    assert max_sum_of_three_consecutive([4, 7], 2) == 11


def test_three_elements_basic():
    # Best selection: take first and last elements
    assert max_sum_of_three_consecutive([3, 2, 5], 3) == 8


def test_four_elements():
    # Optimal: take elements at indices 0, 1, and 3
    arr = [1, 2, 3, 4]
    assert max_sum_of_three_consecutive(arr, 4) == 7


def test_five_elements():
    # Optimal: skip the middle element to maximize sum
    arr = [1, 2, 3, 4, 5]
    assert max_sum_of_three_consecutive(arr, 5) == 12


def test_uniform_array_length_six():
    # With all elements equal, should select 4 out of 6
    arr = [1, 1, 1, 1, 1, 1]
    assert max_sum_of_three_consecutive(arr, 6) == 4


def test_typical_case():
    # Should select largest values while respecting constraint
    arr = [3000, 2000, 1000, 3, 10]
    assert max_sum_of_three_consecutive(arr, 5) == 5010


def test_increasing_sequence():
    # Selection pattern for consecutive increasing numbers
    arr = [1, 2, 3, 4, 5, 6, 7]
    assert max_sum_of_three_consecutive(arr, 7) == 19


def test_large_values_at_end():
    # Should prioritize larger values at the end
    arr = [1, 1, 1, 100, 100]
    assert max_sum_of_three_consecutive(arr, 5) == 202


def test_alternating_high_low():
    # Pattern with alternating high and low values
    arr = [10, 1, 10, 1, 10, 1, 10]
    assert max_sum_of_three_consecutive(arr, 7) == 40
