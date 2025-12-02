
from hypothesis import given, strategies as st, assume
from bugged_modular import modular_sum


@given(st.lists(st.integers(min_value=1, max_value=50), min_size=1, max_size=15),
       st.integers(min_value=2, max_value=50))
def test_property_multiply(arr, m):
    """Multiplying all elements by m should always give True"""
    scaled_arr = [x * m for x in arr]
    n = len(scaled_arr)
    result = modular_sum(scaled_arr, n, m)

    assert result is True


@given(st.lists(st.integers(min_value=-100, max_value=100), min_size=1, max_size=15),
       st.integers(min_value=2, max_value=50))
def test_property_reverse(arr, m):
    """Result should be independent of element ordering"""
    n = len(arr)
    result_original = modular_sum(arr, n, m)
    result_reversed = modular_sum(arr[::-1], n, m)

    assert result_original == result_reversed


@given(st.lists(st.integers(min_value=-100, max_value=100), min_size=1, max_size=10),
       st.integers(min_value=2, max_value=50))
def test_property_idempotence(arr, m):
    """If solution exists, it still exists when we duplicate the array"""
    n = len(arr)
    result_original = modular_sum(arr, n, m)

    arr_doubled = arr + arr
    result_doubled = modular_sum(arr_doubled, len(arr_doubled), m)

    # True should stay True
    if result_original:
        assert result_doubled is True


@given(st.lists(st.integers(min_value=-100, max_value=100), min_size=1, max_size=10),
       st.integers(min_value=-100, max_value=100),
       st.integers(min_value=2, max_value=50))
def test_property_monotonicity(arr, new_element, m):
    """Adding an element to the array can only increase solution possibilities"""
    n = len(arr)
    result_before = modular_sum(arr, n, m)

    arr_after = arr + [new_element]
    result_after = modular_sum(arr_after, len(arr_after), m)

    # if solution is there, it will be after too
    if result_before:
        assert result_after is True


@given(st.lists(st.integers(min_value=-50, max_value=50), min_size=1, max_size=8),
       st.integers(min_value=2, max_value=30))
def test_property_brute_force(arr, m):
    """For small arrays, verify against exhaustive subset enumeration"""
    assume(len(arr) <= 8)

    n = len(arr)
    result = modular_sum(arr, n, m)

    # Brute force: check all non-empty subsets
    valid_subset = False
    for i in range(1, 2**n):
        subset_sum = sum(arr[j] for j in range(n) if i & (1 << j))
        if subset_sum % m == 0:
            valid_subset = True
            break

    assert result == valid_subset
