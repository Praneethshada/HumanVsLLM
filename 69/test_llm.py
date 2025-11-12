import pytest
from bugged_code import is_sublist

# --- Pytest Test Cases ---

# We use @pytest.mark.parametrize to run the *same test function*
# with many different inputs (l, s) and expected results.
# This is a very common and effective way to write example-based tests.

@pytest.mark.parametrize("l, s, expected", [
    
    # Case 1: Basic True - Sublist is in the middle
    ([1, 2, 3, 4, 5], [2, 3, 4], True),
    
    # Case 2: Basic False - Sublist is not present
    ([1, 2, 3, 4, 5], [2, 4, 5], False),
    
    # Case 3: Edge Case - Empty sublist (should always be True)
    ([1, 2, 3], [], True),
    
    # Case 4: Edge Case - Empty list, non-empty sublist
    ([], [1, 2], False),
    
    # Case 5: Edge Case - Both list and sublist are empty
    ([], [], True),
    
    # Case 6: True - Sublist is at the beginning
    ([1, 2, 3, 4, 5], [1, 2], True),
    
    # Case 7: True - Sublist is at the end
    ([1, 2, 3, 4, 5], [4, 5], True),
    
    # Case 8: True - Identical lists
    ([1, 2, 3], [1, 2, 3], True),
    
    # Case 9: False - Sublist is longer than the list
    ([1, 2, 3], [1, 2, 3, 4], False),
    
    # Case 10: False - Partial match at the end
    ([1, 2, 3, 4], [3, 4, 5], False),
    
    # Case 11: True - With repeated elements
    ([1, 2, 1, 2, 3], [1, 2, 3], True),
    
    # Case 12: False - Near match with repeated elements
    ([1, 2, 1, 3, 4], [1, 2, 1, 2], False),
    
    # Case 13: True - Using strings
    (['a', 'b', 'c', 'd'], ['b', 'c'], True),
    
    # Case 14: False - Elements present but not contiguous
    ([1, 2, 3, 4, 5], [1, 3, 5], False),
])
def test_is_sublist(l, s, expected):
    """
    Test the is_sublist function with various inputs.
    """
    assert is_sublist(l, s) == expected