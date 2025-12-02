from hypothesis import given, strategies as st
from sum_num import sum_num
import math

# Strategy: Lists of integers, avoiding empty lists to prevent ZeroDivision in logic
# We select non-empty lists for the main math properties
non_empty_int_lists = st.lists(st.integers(min_value=-1000, max_value=1000), min_size=1)

@given(non_empty_int_lists)
def test_mean_is_within_bounds(numbers):
    """
    Property: The mean must always be between the min and max values of the list.
    """
    result = sum_num(numbers)
    
    # Calculate expected bounds
    minimum = min(numbers)
    maximum = max(numbers)
    
    assert minimum <= result <= maximum

@given(non_empty_int_lists)
def test_mean_reversibility(numbers):
    """
    Property: (mean * length) should be approximately equal to sum(numbers).
    This catches the integer division bug because the decimal part is lost.
    """
    result = sum_num(numbers)
    length = len(numbers)
    total_sum = sum(numbers)
    
    # Check if result * length is close to the sum
    # We use math.isclose to handle floating point noise, but our bug
    # causes a large deviation (integer truncation).
    assert math.isclose(result * length, total_sum, abs_tol=0.1), \
           f"Mean {result} * Len {length} != Sum {total_sum}"
    
@given(non_empty_int_lists)
def test_mean_of_identical_elements(numbers):
    """
    Property: If all elements are identical, the mean should equal that element.
    """
    if len(set(numbers)) == 1:  # All elements are the same
        expected_value = numbers[0]
        result = sum_num(numbers)
        assert result == expected_value, \
               f"Expected mean {expected_value} but got {result}"

@given(st.lists(st.integers(min_value=-1000, max_value=1000), min_size=0))
def test_empty_list(numbers):
    """
    Edge Case: An empty list should return 0.
    """
    if len(numbers) == 0:
        result = sum_num(numbers)
        assert result == 0, f"Expected mean 0 for empty list but got {result}"

@given(st.lists(st.integers(min_value=-1000, max_value=1000), min_size=2))
def test_mean_with_negatives_and_positives(numbers):
    """
    Property: The mean of a list with both negative and positive numbers
    should be between the min and max values.
    """
    result = sum_num(numbers)
    
    minimum = min(numbers)
    maximum = max(numbers)
    
    assert minimum <= result <= maximum

