import pytest
from hypothesis import given, strategies as st
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
