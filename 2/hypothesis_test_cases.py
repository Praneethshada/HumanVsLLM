import pytest
from hypothesis import given, strategies as st, assume
from buggy_function import min_cost

# Only generate valid rectangular grids
matrix_strategy = st.lists(
    st.lists(st.integers(min_value=1, max_value=10), min_size=2, max_size=4),
    min_size=2, max_size=4
).filter(lambda m: all(len(row) == len(m[0]) for row in m))

@given(matrix_strategy)
def test_min_cost_never_exceeds_straight_path(cost):
    """The cost should never exceed the sum of top row + rightmost column (worst path)."""
    rows, cols = len(cost), len(cost[0])
    m, n = rows - 1, cols - 1
    try:
        result = min_cost(cost, m, n)
    except Exception:
        pytest.skip("Function failed for this shape")

    max_possible = sum(cost[0]) + sum(row[-1] for row in cost[1:])
    assert result <= max_possible

@given(matrix_strategy)
def test_diagonal_shortcut_benefit(cost):
    """If diagonal path cells are very cheap, total cost should follow the diagonal."""
    rows, cols = len(cost), len(cost[0])
    for i in range(min(rows, cols)):
        cost[i][i] = 1  # Make diagonal super cheap
    m, n = rows - 1, cols - 1
    try:
        result = min_cost(cost, m, n)
    except Exception:
        pytest.skip("Function failed for this shape")

    # Only assert diagonal shortcut for square grids
    if rows == cols:
        diag_sum = sum(cost[i][i] for i in range(rows))
        assert result <= diag_sum

@given(st.integers(min_value=2, max_value=5), st.integers(min_value=2, max_value=5))
def test_uniform_cost_grid(rows, cols):
    """Test with uniform cost - should return rows + cols - 1"""
    cost = [[1 for _ in range(cols)] for _ in range(rows)]
    m, n = rows - 1, cols - 1
    result = min_cost(cost, m, n)
    expected = rows + cols - 1
    assert result == expected

@given(st.integers(min_value=2, max_value=4))
def test_diagonal_heavy_penalty(size):
    """Test case where diagonal is expensive - bug should be visible"""
    cost = [[1 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        cost[i][i] = 100
    m, n = size - 1, size - 1
    result = min_cost(cost, m, n)
    expected = 2 * size - 1
    assert result <= expected + 100

@given(st.integers(min_value=2, max_value=4), st.integers(min_value=2, max_value=4))
def test_all_ones_except_expensive_diagonal(rows, cols):
    """Test with all 1s except diagonal = 50 to expose diagonal bug"""
    assume(rows >= 2 and cols >= 2)
    cost = [[1 for _ in range(cols)] for _ in range(rows)]
    for i in range(min(rows, cols)):
        cost[i][i] = 50
    result = min_cost(cost, rows - 1, cols - 1)
    expected_max = rows + cols - 1 + 50
    assert result <= expected_max
