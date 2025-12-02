from hypothesis import given, strategies as st
from bugged_code import next_Perfect_Square
import math

# Strategy: test N between 0 and large numbers
ints = st.integers(min_value=0, max_value=10**6)

# def reference(N):
#     """Ground-truth implementation."""
#     root = math.isqrt(N)
#     return (root + 1)**2


# @given(ints)
# def test_matches_reference(N):
#     """
#     Property 1:
#     Must match the true mathematical definition.
#     """
#     assert next_Perfect_Square(N) == reference(N)


@given(ints)
def test_result_is_perfect_square(N):
    """
    Property 2:
    The result must itself be a perfect square.
    """
    sq = next_Perfect_Square(N)
    root = int(math.sqrt(sq))
    assert root * root == sq


@given(ints)
def test_result_greater_than_N(N):
    """
    Property 3:
    The returned square must be strictly greater than N.
    """
    sq = next_Perfect_Square(N)
    assert sq > N


@given(ints)
def test_no_intermediate_squares(N):
    """
    Property 4:
    There should be no perfect square between N and the returned value.
    """
    sq = next_Perfect_Square(N)
    root = int(math.sqrt(sq))
    prev_sq = (root - 1) ** 2
    assert prev_sq <= N < sq
