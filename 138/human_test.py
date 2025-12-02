from hypothesis import given, strategies as st
from bugged_code import is_Sum_Of_Powers_Of_Two

# All integers in a reasonable range
ints = st.integers(min_value=-1000, max_value=1000)

def reference(n):
    """
    True iff n is even.
    """
    return n % 2 == 0


@given(ints)
def test_even_numbers_true(n):
    """
    Property 1:
    All even numbers should return True.
    """
    if n % 2 == 0:
        assert is_Sum_Of_Powers_Of_Two(n) == True


@given(ints)
def test_odd_numbers_false(n):
    """
    Property 2:
    All odd numbers should return False.
    """
    if n % 2 != 0:
        assert is_Sum_Of_Powers_Of_Two(n) == False


@given(ints)
def test_reference_equivalence(n):
    """
    Property 3:
    Must match the mathematical reference.
    """
    assert is_Sum_Of_Powers_Of_Two(n) == reference(n)
