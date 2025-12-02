
from bugged_modular import modular_sum


def test_single_element_divisible():
    arr = [5]
    n = 1
    m = 5
    # 5 % 5 == 0
    assert modular_sum(arr, n, m) is True


def test_single_element_not_divisible():
    arr = [3]
    n = 1
    m = 5
    assert modular_sum(arr, n, m) is False


def test_empty_array_no_subset():
    # Assuming non-empty subset requirement
    arr = []
    n = 0
    m = 7
    assert modular_sum(arr, n, m) is False


def test_all_zeros_always_divisible():
    # Any non-empty subset of zeros has sum 0 → divisible by any m
    arr = [0, 0, 0]
    n = 3
    m = 3
    assert modular_sum(arr, n, m) is True


def test_m_equals_one_always_true():
    # Any integer is divisible by 1
    arr = [7, 11, 13]
    n = 3
    m = 1
    assert modular_sum(arr, n, m) is True


def test_typical_true_subset():
    # 1 + 5 = 6, divisible by 6
    arr = [3, 1, 7, 5]
    n = 4
    m = 6
    assert modular_sum(arr, n, m) is True


def test_typical_false_subset():
    # No subset sums of [2,3,4] are divisible by 8
    arr = [2, 3, 4]
    n = 3
    m = 8
    assert modular_sum(arr, n, m) is False


def test_negative_numbers_allowed():
    # -1 + 2 + 3 = 4 → divisible by 4
    arr = [-1, 2, 3]
    n = 3
    m = 4
    assert modular_sum(arr, n, m) is True


def test_large_numbers_divisible():
    arr = [100_000_000, 200_000_000]
    n = 2
    m = 100
    assert modular_sum(arr, n, m) is True


def test_repeated_values_combination():
    # 4 + 4 + 2 = 10 → divisible by 10
    arr = [4, 4, 2]
    n = 3
    m = 10
    assert modular_sum(arr, n, m) is True


def test_all_same_not_divisible():
    # sums: 3, 6, 9 → none divisible by 7
    arr = [3, 3, 3]
    n = 3
    m = 7
    assert modular_sum(arr, n, m) is False


def test_minimal_pair_true():
    arr = [2, 3]
    n = 2
    m = 5
    # 2 + 3 = 5
    assert modular_sum(arr, n, m) is True
