import pytest
from bugged_code import is_undulating

@pytest.mark.parametrize("n, expected", [
    (1212121, True),   # Perfect alternating
    (1991, False),     # Not undulating
    (121, True),       # Small undulating
    (333, True),      # Repeated digits
    (2323, True),      # Alternating digits
    (123123, False),   # 3 distinct digits
    (454545, True),    # Alternating digits
    (9898, True),      # Alternating pattern
    (1221, False),     # Mirror pattern, not alternating
    (11, False),       # Too short
])
def test_is_undulating(n, expected):
    """
    Example-based LLM test cases for is_undulating().
    """
    assert is_undulating(n) == expected
