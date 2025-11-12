import pytest
from hypothesis import given, strategies as st
from buggy_function import re_arrange_tuples

# Strategy to generate random tuples and order lists
tuple_strategy = st.lists(st.tuples(st.integers(min_value=1, max_value=5), st.integers(min_value=0, max_value=100)), min_size=1, max_size=5)
order_strategy = st.lists(st.integers(min_value=1, max_value=5), min_size=1, max_size=5)

@given(tuple_strategy, order_strategy)
def test_output_length_matches_order(test_list, ord_list):
    res = re_arrange_tuples(test_list, ord_list)
    assert len(res) == len(ord_list)

@given(tuple_strategy, order_strategy)
def test_all_keys_from_order_present(test_list, ord_list):
    res = re_arrange_tuples(test_list, ord_list)
    keys_in_result = [k for k, _ in res]
    # The result should preserve the order list exactly
    assert keys_in_result == ord_list

@given(tuple_strategy, order_strategy)
def test_no_none_values_in_result(test_list, ord_list):
    res = re_arrange_tuples(test_list, ord_list)
    # None values indicate missing mappings (bug)
    for _, val in res:
        assert val is not None
