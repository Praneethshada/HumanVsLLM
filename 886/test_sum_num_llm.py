import pytest
from sum_num import sum_num

# Test Case 1: Basic integer average
def test_basic_integer_average():
    """Test with basic integer values"""
    assert sum_num([1, 2, 3, 4, 5]) == 3.0
    assert sum_num([10, 20, 30]) == 20.0
    assert sum_num([0, 10, 20]) == 10.0

# Test Case 2: Single element list
def test_single_element():
    """Test with single element list"""
    assert sum_num([5]) == 5.0
    assert sum_num([-3]) == -3.0
    assert sum_num([0]) == 0.0
    assert sum_num([7.5]) == 7.5

# Test Case 3: Empty list
def test_empty_list():
    """Test with empty list"""
    assert sum_num([]) == 0

# Test Case 4: Float numbers
def test_float_numbers():
    """Test with floating point numbers"""
    assert sum_num([1.5, 2.5, 3.5]) == 2.5
    assert sum_num([0.1, 0.2, 0.3, 0.4]) == 0.25
    assert sum_num([1.1, 2.2, 3.3]) == pytest.approx(2.2)

# Test Case 5: Mixed integers and floats
def test_mixed_numbers():
    """Test with mixed integer and float values"""
    assert sum_num([1, 2.5, 3, 4.5]) == 2.75
    assert sum_num([10, 20.0, 30]) == 20.0
    assert sum_num([0, 1.5, 3]) == 1.5

# Test Case 6: Negative numbers
def test_negative_numbers():
    """Test with negative values"""
    assert sum_num([-1, -2, -3]) == -2.0
    assert sum_num([-10, 0, 10]) == 0.0
    assert sum_num([-5, -3, -1]) == -3.0

# Test Case 7: Large numbers
def test_large_numbers():
    """Test with large numerical values"""
    assert sum_num([1000000, 2000000, 3000000]) == 2000000.0
    assert sum_num([999999, 999999, 999999]) == 999999.0
    assert sum_num([-1000000, 0, 1000000]) == 0.0

# Test Case 8: List with zeros
def test_with_zeros():
    """Test lists containing zeros"""
    assert sum_num([0, 0, 0, 0]) == 0.0
    assert sum_num([0, 5, 0]) == pytest.approx(1.6666666666666667)
    assert sum_num([0, 0, 10]) == pytest.approx(3.3333333333333335)

# Test Case 9: All same numbers
def test_all_same_numbers():
    """Test when all numbers are identical"""
    assert sum_num([7, 7, 7, 7, 7]) == 7.0
    assert sum_num([-3, -3, -3]) == -3.0
    assert sum_num([0, 0, 0, 0, 0, 0]) == 0.0
    assert sum_num([2.5, 2.5, 2.5]) == 2.5

# Test Case 10: Real-world examples
def test_real_world_examples():
    """Test with real-world-like data"""
    # Student grades
    grades = [85, 90, 78, 92, 88]
    assert sum_num(grades) == 86.6
    # Temperatures
    temps = [72.5, 73.0, 71.8, 74.2, 72.9]
    assert sum_num(temps) == pytest.approx(72.88)
    # Product prices
    prices = [10.99, 15.99, 12.49, 9.99]
    assert sum_num(prices) == 12.365

# Test Case 11: Two element lists
def test_two_elements():
    """Test lists with exactly two elements"""
    assert sum_num([1, 2]) == 1.5
    assert sum_num([0, 0]) == 0.0
    assert sum_num([-5, 5]) == 0.0
    assert sum_num([3.5, 4.5]) == 4.0

# Test Case 12: Three element lists
def test_three_elements():
    """Test lists with exactly three elements"""
    assert sum_num([1, 2, 3]) == 2.0
    assert sum_num([10, 20, 30]) == 20.0
    assert sum_num([-1, 0, 1]) == 0.0

# Test Case 13: Very small numbers
def test_very_small_numbers():
    """Test with very small numerical values"""
    assert sum_num([0.001, 0.002, 0.003]) == 0.002
    assert sum_num([1e-10, 2e-10, 3e-10]) == pytest.approx(2e-10)
    assert sum_num([-0.001, 0, 0.001]) == 0.0

# Test Case 14: Decimal precision
def test_decimal_precision():
    """Test decimal precision handling"""
    assert sum_num([1, 2, 3]) == 2.0  # Exact division
    assert sum_num([1, 2, 3, 4]) == 2.5  # Exact division
    assert sum_num([1, 2, 3, 4, 5, 6]) == 3.5  # Exact division
    assert sum_num([1, 1, 1, 2]) == 1.25  # Exact division

# Test Case 15: Even number of elements
def test_even_number_elements():
    """Test with even number of elements"""
    assert sum_num([1, 3, 5, 7]) == 4.0
    assert sum_num([2, 4, 6, 8, 10, 12]) == 7.0
    assert sum_num([-2, -1, 1, 2]) == 0.0

# Test Case 16: Odd number of elements
def test_odd_number_elements():
    """Test with odd number of elements"""
    assert sum_num([1, 2, 3]) == 2.0
    assert sum_num([5, 10, 15, 20, 25]) == 15.0
    assert sum_num([-3, -2, -1, 0, 1]) == -1.0

# Test Case 17: Sequential numbers
def test_sequential_numbers():
    """Test with sequential numbers"""
    # Numbers 1 through 5
    assert sum_num([1, 2, 3, 4, 5]) == 3.0
    # Numbers 10 through 14
    assert sum_num([10, 11, 12, 13, 14]) == 12.0
    # Negative sequence
    assert sum_num([-5, -4, -3, -2, -1]) == -3.0

# Test Case 18: Arithmetic progression
def test_arithmetic_progression():
    """Test with arithmetic progression"""
    # Common difference 2
    assert sum_num([2, 4, 6, 8, 10]) == 6.0
    # Common difference 3
    assert sum_num([3, 6, 9, 12]) == 7.5
    # Common difference -1
    assert sum_num([5, 4, 3, 2, 1]) == 3.0

# Test Case 19: Return type
def test_return_type():
    """Test that function returns correct type"""
    result = sum_num([1, 2, 3])
    assert isinstance(result, (int, float))
    
    result2 = sum_num([1.5, 2.5])
    assert isinstance(result2, float)
    
    result3 = sum_num([])
    assert isinstance(result3, int)  # Returns 0 for empty list

# Test Case 20: Large list
def test_large_list():
    """Test with a larger number of elements"""
    numbers = [1] * 100  # 100 ones
    assert sum_num(numbers) == 1.0
    
    numbers = list(range(1, 101))  # 1 to 100
    expected = (1 + 100) / 2  # Average of arithmetic series
    assert sum_num(numbers) == expected
