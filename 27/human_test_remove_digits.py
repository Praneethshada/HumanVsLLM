import pytest, string
from hypothesis import given, strategies as st
from bugged_remove_digits import remove

list_of_strings_strategy = st.lists(st.text())


@given(list_of_strings_strategy)
def test_same_length(input_list):

    """
    Property 1: The output list should have the same number of strings
    as the input list.
    """
    result = remove(input_list)
    assert len(result) == len(input_list)

@given(list_of_strings_strategy)
def test_contain_no_digits(input_list):
    """
    Property 2: The core requirement. No string in the output list
    should contain any digit.
    """
    result = remove(input_list)
    for s in result:
        for char in s:
            assert char not in string.digits, f"Found digit '{char}' in output string '{s}'"

@given(list_of_strings_strategy)
def test_is_idempotent(input_list):
    """
    Property 3: remove(remove(x)) == remove(x)
    """
    result1 = remove(input_list)
    result2 = remove(result1)
    assert result1 == result2

@given(list_of_strings_strategy)
def test_preserves_non_digit(input_list):
    """
    Property 4: Compares the function's output to a golden implementation.
    """
    expected_output = []
    for s in input_list:
        expected_s = "".join(char for char in s if not char.isdigit())
        expected_output.append(expected_s)

    actual_output = remove(input_list)

    assert actual_output == expected_output
