import pytest
from hypothesis import given, strategies as st, assume
from buggy_function import re_arrange_tuples

# Strategy to generate random tuples and order lists
tuple_strategy = st.lists(
    st.tuples(st.integers(min_value=1, max_value=5), st.integers(min_value=0, max_value=100)), 
    min_size=1, max_size=5
)
order_strategy = st.lists(st.integers(min_value=1, max_value=5), min_size=1, max_size=5)

@given(tuple_strategy, order_strategy)
def test_output_length_matches_order(test_list, ord_list):
    """Output length should match order list length"""
    res = re_arrange_tuples(test_list, ord_list)
    assert len(res) == len(ord_list)

@given(tuple_strategy, order_strategy)
def test_all_keys_from_order_present(test_list, ord_list):
    """Result should preserve the order list exactly"""
    res = re_arrange_tuples(test_list, ord_list)
    keys_in_result = [k for k, _ in res]
    assert keys_in_result == ord_list

@given(tuple_strategy, order_strategy)
def test_no_none_values_in_result(test_list, ord_list):
    """Result shouldn't have None values"""
    res = re_arrange_tuples(test_list, ord_list)
    for _, v in res:
        assert v is not None

@given(st.lists(st.tuples(st.integers(1, 5), st.integers(10, 100)), min_size=2, max_size=5))
def test_keys_only_from_test_list_correct_values(test_list):
    """When order list contains only keys from test_list, values should match"""
    keys = [k for k, _ in test_list]
    ord_list = keys[::-1]  # Reverse order
    res = re_arrange_tuples(test_list, ord_list)
    
    original_dict = dict(test_list)
    for key, value in res:
        assert key in original_dict
        # Should match original mapping
        assert value == original_dict[key]

@given(st.lists(st.tuples(st.integers(1, 3), st.integers(10, 100)), min_size=2, max_size=5))
def test_missing_keys_get_zero(test_list):
    """Test behavior when ord_list has keys not in test_list - documents bug"""
    existing_keys = list(set(k for k, _ in test_list))
    assume(len(existing_keys) > 0)
    
    missing_key = max(existing_keys) + 10  # Key that doesn't exist
    ord_list = existing_keys + [missing_key]
    
    res = re_arrange_tuples(test_list, ord_list)
    last_key, last_value = res[-1]
    
    assert last_key == missing_key
    # Bug: returns 0 for missing keys instead of raising error
    assert last_value == 0

@given(st.lists(st.tuples(st.integers(1, 5), st.integers(0, 100)), min_size=1, max_size=5))
def test_values_correctness_for_existing_keys(test_list):
    """Verify that existing keys map to correct values"""
    original_dict = dict(test_list)
    existing_keys = list(original_dict.keys())
    
    if len(existing_keys) > 0:
        res = re_arrange_tuples(test_list, existing_keys)
        
        for key, value in res:
            if key in original_dict:
                assert value == original_dict[key]

@given(st.lists(st.tuples(st.integers(1, 3), st.integers(1, 100)), min_size=2, max_size=4))
def test_mix_of_existing_and_missing_keys(test_list):
    """Test with both existing and non-existing keys"""
    original_dict = dict(test_list)
    existing_keys = list(original_dict.keys())
    
    assume(len(existing_keys) >= 2)
    
    # Mix: some existing, some missing
    missing_keys = [max(existing_keys) + i for i in range(1, 3)]
    ord_list = [existing_keys[0]] + missing_keys + [existing_keys[-1]]
    
    res = re_arrange_tuples(test_list, ord_list)
    
    for key, value in res:
        if key in original_dict:
            assert value == original_dict[key]
        else:
            # Bug: missing keys get 0
            assert value == 0
