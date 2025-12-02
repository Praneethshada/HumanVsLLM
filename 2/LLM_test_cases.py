import pytest
from buggy_function import min_cost

def test_single_cell():
    assert min_cost([[5]], 0, 0) == 5

def test_small_grid():
    cost = [
        [1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]
    ]
    # optimal path: 1 → 2 → 3 → 2 → 3 (total 8)
    assert min_cost(cost, 2, 2) == 8

def test_diagonal_cheaper():
    cost = [
        [1, 100, 100],
        [100, 1, 100],
        [100, 100, 1]
    ]
    # diagonal path 1→1→1 = 3
    assert min_cost(cost, 2, 2) == 3

def test_out_of_bounds():
    with pytest.raises(IndexError):
        min_cost([[1,2],[3,4]], 3, 0)

def test_empty_grid():
    with pytest.raises(ValueError):
        min_cost([], 0, 0)
