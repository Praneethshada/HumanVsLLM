import pytest
from bugged_code import next_Perfect_Square

@pytest.mark.parametrize("N, expected", [

    # Provided MBPP examples
    (35, 36),
    (6, 9),
    (9, 16),

    # Numbers just below perfect squares
    (15, 16),
    (24, 25),
    (26, 36),

    # When N IS a perfect square → next square
    (1, 4),
    (4, 9),
    (16, 25),
    (81, 100),

    # Edge values
    (0, 1),
    (2, 4),
    (3, 4),
    (99, 100),

    # Larger values
    (1000, 1024),
    (1023, 1024),
])
def test_next_perfect_square_examples(N, expected):
    assert next_Perfect_Square(N) == expected
