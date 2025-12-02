import pytest
from bugged_code import is_Sum_Of_Powers_Of_Two

@pytest.mark.parametrize("n, expected", [
    # From MBPP
    (10, True),
    (7, False),
    (14, True),

    # Basic even/odd behavior
    (2, True),
    (4, True),
    (6, True),
    (8, True),
    (9, False),

    # Edge cases
    (0, True),   # 0 has no odd bit → treat as valid
    (1, False),  # 1 = 2^0 forbidden
    (-2, True),  # Even negative
    (-3, False), # Odd negative

    # Random even
    (22, True),
    (100, True),

    # Random odd
    (45, False),
    (99, False),
])
def test_sum_powers_of_two(n, expected):
    assert is_Sum_Of_Powers_Of_Two(n) == expected
