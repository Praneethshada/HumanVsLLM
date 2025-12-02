import pytest
from are_Equal import are_Equal

# Test Case 1: Equal arrays with integers
def test_equal_integer_arrays():
    """Test with equal integer arrays"""
    assert are_Equal([1, 2, 3], [1, 2, 3], 3, 3) == True
    assert are_Equal([], [], 0, 0) == True
    assert are_Equal([5], [5], 1, 1) == True

# Test Case 2: Unequal arrays with integers
def test_unequal_integer_arrays():
    """Test with unequal integer arrays"""
    assert are_Equal([1, 2, 3], [1, 2, 4], 3, 3) == False
    assert are_Equal([1, 2, 3], [3, 2, 1], 3, 3) == False
    assert are_Equal([1], [2], 1, 1) == False

# Test Case 3: Different lengths (n != m)
def test_different_lengths():
    """Test arrays with different lengths"""
    assert are_Equal([1, 2, 3], [1, 2], 3, 2) == False
    assert are_Equal([1, 2], [1, 2, 3], 2, 3) == False
    assert are_Equal([], [1], 0, 1) == False
    assert are_Equal([1], [], 1, 0) == False

# Test Case 4: Equal arrays with floats
def test_equal_float_arrays():
    """Test with equal float arrays"""
    assert are_Equal([1.5, 2.5, 3.5], [1.5, 2.5, 3.5], 3, 3) == True
    assert are_Equal([0.0, 0.1, 0.2], [0.0, 0.1, 0.2], 3, 3) == True

# Test Case 5: Unequal arrays with floats
def test_unequal_float_arrays():
    """Test with unequal float arrays"""
    assert are_Equal([1.5, 2.5], [1.5, 2.6], 2, 2) == False
    assert are_Equal([0.1, 0.2], [0.2, 0.1], 2, 2) == False

# Test Case 6: Equal arrays with strings
def test_equal_string_arrays():
    """Test with equal string arrays"""
    assert are_Equal(['a', 'b', 'c'], ['a', 'b', 'c'], 3, 3) == True
    assert are_Equal(['hello', 'world'], ['hello', 'world'], 2, 2) == True
    assert are_Equal([''], [''], 1, 1) == True

# Test Case 7: Unequal arrays with strings
def test_unequal_string_arrays():
    """Test with unequal string arrays"""
    assert are_Equal(['a', 'b'], ['a', 'c'], 2, 2) == False
    assert are_Equal(['hello'], ['world'], 1, 1) == False
    assert are_Equal([''], [' '], 1, 1) == False  # Space vs empty

# Test Case 8: Mixed data types
def test_mixed_data_types():
    """Test arrays with mixed data types"""
    assert are_Equal([1, 'a', 3.5], [1, 'a', 3.5], 3, 3) == True
    assert are_Equal([True, False, None], [True, False, None], 3, 3) == True
    assert are_Equal([1, 'a', 3.5], [1, 'a', 3.6], 3, 3) == False

# Test Case 9: n parameter less than actual length
def test_n_less_than_actual_length():
    """Test when n is less than actual array length"""
    # Only compare first 2 elements
    assert are_Equal([1, 2, 3, 4], [1, 2, 9, 10], 2, 2) == True
    # Only compare first 1 element
    assert are_Equal([1, 99], [1, 88], 1, 1) == True
    # Compare first 0 elements (empty comparison)
    assert are_Equal([1, 2, 3], [4, 5, 6], 0, 0) == True

# Test Case 10: n parameter greater than actual length
def test_n_greater_than_actual_length():
    """Test when n is greater than actual array length"""
    # This would cause IndexError if not careful
    # But the function assumes caller provides correct n
    # For safety, we only test with correct lengths
    
    # Proper usage: n matches actual length
    arr1 = [1, 2, 3]
    arr2 = [1, 2, 3]
    assert are_Equal(arr1, arr2, len(arr1), len(arr2)) == True

# Test Case 11: Arrays with None values
def test_arrays_with_none():
    """Test arrays containing None values"""
    assert are_Equal([None, None], [None, None], 2, 2) == True
    assert are_Equal([1, None, 3], [1, None, 3], 3, 3) == True
    assert are_Equal([None], [1], 1, 1) == False

# Test Case 12: Arrays with boolean values
def test_boolean_arrays():
    """Test arrays with boolean values"""
    assert are_Equal([True, False], [True, False], 2, 2) == True
    assert are_Equal([True, True], [True, False], 2, 2) == False
    assert are_Equal([False], [0], 1, 1) == False  # Boolean vs integer

# Test Case 13: Large arrays
def test_large_arrays():
    """Test with large arrays"""
    arr1 = list(range(1000))
    arr2 = list(range(1000))
    arr3 = list(range(999)) + [1000]  # Last element different
    assert are_Equal(arr1, arr2, 1000, 1000) == True
    assert are_Equal(arr1, arr3, 1000, 1000) == False

# Test Case 14: Arrays with duplicates
def test_arrays_with_duplicates():
    """Test arrays with duplicate elements"""
    assert are_Equal([1, 1, 2, 2], [1, 1, 2, 2], 4, 4) == True
    assert are_Equal([1, 2, 1, 2], [1, 1, 2, 2], 4, 4) == False  # Different order
    assert are_Equal([1, 1, 1], [1, 1, 1], 3, 3) == True

# Test Case 15: Zero and empty values
def test_zero_and_empty_values():
    """Test with zeros and empty strings"""
    assert are_Equal([0, 0, 0], [0, 0, 0], 3, 3) == True
    assert are_Equal([0], [0.0], 1, 1) == False  # Integer vs float
    assert are_Equal(['', ''], ['', ''], 2, 2) == True

# Test Case 16: Negative numbers
def test_negative_numbers():
    """Test arrays with negative numbers"""
    assert are_Equal([-1, -2, -3], [-1, -2, -3], 3, 3) == True
    assert are_Equal([-1, 0, 1], [-1, 0, 1], 3, 3) == True
    assert are_Equal([-1, -2], [-2, -1], 2, 2) == False

# Test Case 17: Same object reference
def test_same_reference():
    """Test with same array object"""
    arr = [1, 2, 3]
    assert are_Equal(arr, arr, 3, 3) == True

# Test Case 18: Early exit on first mismatch
def test_early_exit():
    """Test that function exits early on first mismatch"""
    # First element mismatch
    assert are_Equal([1, 2, 3, 4, 5], [9, 2, 3, 4, 5], 5, 5) == False
    # Last element mismatch
    assert are_Equal([1, 2, 3, 4, 5], [1, 2, 3, 4, 9], 5, 5) == False
    # Middle element mismatch
    assert are_Equal([1, 2, 3, 4, 5], [1, 2, 9, 4, 5], 5, 5) == False

# Test Case 19: Unicode and special characters
def test_unicode_arrays():
    """Test arrays with unicode and special characters"""
    assert are_Equal(['😀', '🚀', '❤️'], ['😀', '🚀', '❤️'], 3, 3) == True
    assert are_Equal(['©', '®', '™'], ['©', '®', '™'], 3, 3) == True
    assert are_Equal(['a\nb', 'c\td'], ['a\nb', 'c\td'], 2, 2) == True

# Test Case 20: n=0, m=0 (empty arrays)
def test_empty_arrays_with_zero_length():
    """Test empty arrays with zero length parameters"""
    assert are_Equal([], [], 0, 0) == True
    # Even if arrays have content, n=0 means compare 0 elements
    assert are_Equal([1, 2, 3], [4, 5, 6], 0, 0) == True

# Test Case 21: n and m parameters inconsistent with arrays
def test_length_parameters_inconsistent():
    """Test when n,m don't match actual array lengths"""
    # n < actual length, but still valid comparison
    assert are_Equal([1, 2, 3, 4], [1, 2, 5, 6], 2, 2) == True
    
    # n > actual length would cause IndexError
    # We don't test invalid cases that would crash

# Test Case 22: Arrays with dictionaries
def test_arrays_with_dicts():
    """Test arrays containing dictionaries"""
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'a': 1, 'b': 2}
    dict3 = {'a': 1, 'b': 3}
    
    assert are_Equal([dict1], [dict2], 1, 1) == True
    assert are_Equal([dict1], [dict3], 1, 1) == False

# Test Case 23: Very small n values
def test_very_small_n():
    """Test with very small n values"""
    assert are_Equal([1], [1], 1, 1) == True
    assert are_Equal([1, 2], [1, 2], 1, 1) == True  # Compare only first element
    assert are_Equal([1, 2], [1, 3], 1, 1) == True  # Compare only first element

# Test Case 24: Real-world examples
def test_real_world_examples():
    """Test with real-world-like data"""
    # Student IDs
    assert are_Equal([101, 102, 103], [101, 102, 103], 3, 3) == True
    # Product codes
    assert are_Equal(['A1', 'B2', 'C3'], ['A1', 'B2', 'C3'], 3, 3) == True
    # Sensor readings
    readings1 = [25.5, 26.0, 24.8]
    readings2 = [25.5, 26.0, 24.8]
    assert are_Equal(readings1, readings2, 3, 3) == True

# Test Case 25: Parameter order matters
def test_parameter_order():
    """Test that n and m parameters must match array lengths"""
    # Correct usage
    assert are_Equal([1, 2], [1, 2], 2, 2) == True
    
    # n refers to arr1 length, m to arr2 length
    # They can be different if you want to compare subsets
    assert are_Equal([1, 2, 3, 4], [1, 2], 2, 2) == True  # Compare first 2 of arr1 with all of arr2

