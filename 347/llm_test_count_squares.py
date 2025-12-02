
import pytest
from bugged_count_squares import count_Squares


def test_square_1x1():
    # Only one square
    assert count_Squares(1, 1) == 1


def test_square_2x2():
    # 1x1 squares: 4, 2x2 squares: 1 → total = 5
    assert count_Squares(2, 2) == 5


def test_square_3x3():
    # 1x1: 9, 2x2: 4, 3x3: 1 → total = 14
    assert count_Squares(3, 3) == 14


def test_rectangle_2x3():
    # Formula sum of (m−k+1)(n−k+1) for k up to min(m,n)
    # k=1: 2*3 = 6
    # k=2: 1*2 = 2
    # total = 8
    assert count_Squares(2, 3) == 8


def test_rectangle_3x4():
    # k=1: 3*4 = 12
    # k=2: 2*3 = 6
    # k=3: 1*2 = 2
    # total = 20
    assert count_Squares(3, 4) == 20


def test_symmetry_property():
    # count_Squares(m, n) == count_Squares(n, m)
    assert count_Squares(4, 6) == count_Squares(6, 4)


def test_one_dimension_large():
    # 1 x N grid always has N squares
    assert count_Squares(1, 10) == 10
    assert count_Squares(10, 1) == 10


def test_zero_dimension():
    # Expected to be 0 squares if any side is zero
    assert count_Squares(0, 5) == 0
    assert count_Squares(5, 0) == 0


def test_large_square():
    # 4x4 → 1x1:16, 2x2:9, 3x3:4, 4x4:1 → total = 30
    assert count_Squares(4, 4) == 30
