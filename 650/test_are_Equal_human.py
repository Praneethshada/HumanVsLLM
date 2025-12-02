from hypothesis import given, strategies as st
from are_Equal import are_Equal

# Strategy: Lists of integers
list_strategy = st.lists(st.integers(min_value=0, max_value=100))

@given(list_strategy, list_strategy)
def test_empty_lists(l1, l2):
    """
    Test that two empty lists are considered equal.
    """
    assert are_Equal([], [], 0, 0) == True, "Failed on empty lists"

@given(list_strategy, list_strategy)
def test_equality_property(l1, l2):
    """
    Property: are_Equal(l1, l2) must behave exactly like 
    sorted(l1) == sorted(l2).
    """
    # We must copy lists because the function sorts them in-place, modifying input
    l1_copy = l1.copy()
    l2_copy = l2.copy()
    
    # Ground Truth
    expected = sorted(l1) == sorted(l2)
    
    # Function Result
    result = are_Equal(l1_copy, l2_copy, len(l1), len(l2))
    
    assert result == expected, \
        f"Failed on l1={l1}, l2={l2}. Expected {expected}, Got {result}"
    
@given(list_strategy)
def test_identical_lists(l):
    """
    Test that two identical lists are considered equal.
    """
    l_copy = l.copy()
    assert are_Equal(l, l_copy, len(l), len(l_copy)) == True,f"Failed on identical lists: {l}"

@given(list_strategy, list_strategy)
def test_different_length_lists(l1, l2):
    """
    Test that lists of different lengths are not considered equal.
    """
    assume(len(l1) != len(l2))
    assert are_Equal(l1, l2, len(l1), len(l2)) == False,f"Failed on different length lists: {l1}, {l2}"
    
