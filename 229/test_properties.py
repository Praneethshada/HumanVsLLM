from hypothesis import given, strategies as st
from buggy import re_arrange_array

@given(st.lists(st.integers(min_value=-100, max_value=100), max_size=20))
def test_permutation_and_order(arr):
    # Make a copy because function mutates in place
    original = list(arr)
    result = re_arrange_array(original, len(original))

    # Property 1: multiset of elements is unchanged (permutation)
    assert sorted(result) == sorted(arr)

    # Property 2: all negative elements appear before all non-negative
    seen_non_negative = False
    for x in result:
        if x < 0:
            assert not seen_non_negative
        else:
            seen_non_negative = True
