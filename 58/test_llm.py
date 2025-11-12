import pytest
from bugged_code import opposite_Signs


# --- Pytest Example-Based Test Cases ---
# Generated to cover typical, boundary, and tricky cases.
# These represent the LLM's example-based reasoning style.

@pytest.mark.parametrize("x, y, expected", [

    # Case 1: Basic True — one positive, one negative
    (1, -2, True),

    # Case 2: Basic True — negative, positive
    (-2, 2, True),

    # Case 3: Basic False — both positive
    (3, 2, False),

    # Case 4: Basic False — both negative
    (-10, -10, False),

    # Case 5: Edge — both zero (neither positive nor negative)
    (0, 0, False),

    # Case 6: Edge — zero and positive number (should be False)
    (0, 5, False),

    # Case 7: Edge — zero and negative number (should be False)
    (-5, 0, False),

    # Case 8: Random True — large positive and large negative
    (999, -888, True),

    # Case 9: Random False — both large positive
    (123456, 7890, False),

    # Case 10: Random False — both large negative
    (-123456, -7890, False),

    # Case 11: True — mixed signs, small magnitude
    (2, -1, True),

    # Case 12: False — both even and positive
    (4, 8, False),

    # Case 13: False — both odd and negative
    (-7, -5, False),

    # Case 14: Edge — one number extremely large, other small negative
    (10**9, -1, True),
])
def test_opposite_signs(x, y, expected):
    """
    LLM-style example-based testing for opposite_Signs(x, y).
    """
    assert opposite_Signs(x, y) == expected
