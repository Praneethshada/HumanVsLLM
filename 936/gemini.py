import pytest
from buggy_function import re_arrange_tuples
from typing import List, Tuple, Any, Sequence

# Assuming the function 're_arrange_tuples' is imported or defined elsewhere.
# Signature: def re_arrange_tuples(test_list: List[Tuple[Any, Any]], ord_list: List[Any]) -> List[Tuple[Any, Any]]:


# --- Pytest Parametrize Tests (Explicit Cases) ---

@pytest.mark.parametrize(
    "test_list, ord_list, expected",
    [
        # 1. Basic Correctness (Unique Keys, Simple Reorder)
        ([(4, 3), (1, 9), (2, 10), (3, 2)], [1, 4, 2, 3], [(1, 9), (4, 3), (2, 10), (3, 2)]),
        # 2. Reordering to reverse the list
        ([(10, 'A'), (20, 'B'), (30, 'C')], [30, 20, 10], [(30, 'C'), (20, 'B'), (10, 'A')]),

        # 3. Duplicate Keys in ord_list (Value repetition)
        ([(5, 4), (2, 10), (3, 11), (4, 3)], [3, 4, 2, 3], [(3, 11), (4, 3), (2, 10), (3, 11)]),
        # 4. Duplicate keys in ord_list with different order
        ([(1, 'X'), (2, 'Y')], [2, 1, 2, 1], [(2, 'Y'), (1, 'X'), (2, 'Y'), (1, 'X')]),
        
        # 5. Duplicate Keys in test_list (Edge Case: Last value wins)
        # test_list becomes {1: 'C', 2: 'B'}.
        ([(1, 'A'), (2, 'B'), (1, 'C')], [2, 1], [(2, 'B'), (1, 'C')]),
        # 6. Duplicate Keys in test_list, last key is repeated in ord_list
        # test_list becomes {5: 'New', 3: 'Val1'}
        ([(5, 'Old'), (3, 'Val1'), (5, 'New')], [3, 5, 5], [(3, 'Val1'), (5, 'New'), (5, 'New')]),

        # 7. Edge Case: Empty ord_list
        ([(1, 10), (2, 20)], [], []),
        
        # 8. Non-integer Keys (String keys)
        ([('b', 2), ('a', 1)], ['a', 'b', 'a'], [('a', 1), ('b', 2), ('a', 1)]),
        # 9. Non-integer Keys (Float keys)
        ([(1.5, 'F'), (0.1, 'Z')], [0.1, 1.5, 0.1], [(0.1, 'Z'), (1.5, 'F'), (0.1, 'Z')]),

        # 10. Mixed Key/Value Types
        ([(True, 'Yes'), (None, 'No'), (10, 100)], [10, True, None], [(10, 100), (True, 'Yes'), (None, 'No')]),
        
        # 11. Large input test (simulated)
        # Ensures that order is maintained over a longer list
        ([(i, i*10) for i in range(100)], [50, 5, 99, 10], 
         [(50, 500), (5, 50), (99, 990), (10, 100)]),
    ]
)
def test_re_arrange_tuples_standard_cases(test_list: List, ord_list: List, expected: List):
    """Tests basic reordering, duplicate key repetition, and non-integer keys."""
    # The function is assumed to be globally available/imported
    result = re_arrange_tuples(test_list, ord_list)
    assert result == expected


def test_re_arrange_tuples_empty_list():
    """Test case where both lists are empty."""
    assert re_arrange_tuples([], []) == []


# --- Test for Assumption Violation (KeyError) ---

def test_re_arrange_tuples_key_not_found_error():
    """
    Tests the case where a key in ord_list does not exist in test_list.
    This verifies the behavior when the assumption 'all keys in ord_list exist in test_list' is broken.
    """
    test_list = [(1, 10), (2, 20)]
    ord_list = [1, 3, 2]  # Key 3 is missing

    with pytest.raises(KeyError):
        re_arrange_tuples(test_list, ord_list)

        
# --- Test Cases Provided by User (for verification) ---

def test_given_examples():
    """Tests the examples provided in the initial task description."""
    
    # Example 1
    test_list1 = [(4, 3), (1, 9), (2, 10), (3, 2)]
    ord_list1 = [1, 4, 2, 3]
    expected1 = [(1, 9), (4, 3), (2, 10), (3, 2)]
    assert re_arrange_tuples(test_list1, ord_list1) == expected1

    # Example 2 (Tests duplicate keys in ord_list)
    test_list2 = [(5, 4), (2, 10), (3, 11), (4, 3)]
    ord_list2 = [3, 4, 2, 3]
    expected2 = [(3, 11), (4, 3), (2, 10), (3, 11)]
    assert re_arrange_tuples(test_list2, ord_list2) == expected2
    
    # Example 3
    test_list3 = [(6, 3), (3, 8), (5, 7), (2, 4)]
    ord_list3 = [2, 5, 3, 6]
    expected3 = [(2, 4), (5, 7), (3, 8), (6, 3)]
    assert re_arrange_tuples(test_list3, ord_list3) == expected3