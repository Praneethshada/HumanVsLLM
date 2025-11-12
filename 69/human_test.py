from bugged_code import is_sublist
import pytest
from hypothesis import given, strategies as st


# Strategy: generate general lists and sublists
lists_strategy = st.lists(st.integers(min_value=-1000, max_value=1000), min_size=0, max_size=100)
sublists_strategy = st.lists(st.integers(min_value=-1000, max_value=1000), min_size=0, max_size=100)


@given(lists_strategy)
def test_empty_sublist_true(l):
    """
    Property 1: Empty sublist should always return True.
    """
    assert is_sublist(l, []) is True


@given(lists_strategy)
def test_identical_list_true(l):
    """
    Property 2: Identical lists must always be sublists.
    """
    assert is_sublist(l, l) is True


@given(lists_strategy, sublists_strategy)
def test_longer_sublists_false(l, s):
    """
    Property 3: A sublist longer than the list cannot be a valid sublist.
    """
    if len(s) > len(l):
        assert is_sublist(l, s) is False



@given(lists_strategy)
def test_self_slices_are_sublists(l):
    """
    Property 4: Any contiguous slice of a list must be a sublist.
    """
    if len(l) >= 2:
        for start in range(len(l)):
            for end in range(start, len(l) + 1):
                s = l[start:end]
                assert is_sublist(l, s) is True


