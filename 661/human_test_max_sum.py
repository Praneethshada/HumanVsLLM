
from hypothesis import given, strategies as st, settings, assume
from bugged_max_sum import max_sum_of_three_consecutive


@given(st.lists(st.integers(min_value=1, max_value=100), min_size=1, max_size=20))
@settings(max_examples=100)
def test_result_with_total(arr):
    n = len(arr)
    result = max_sum_of_three_consecutive(arr, n)
    total = sum(arr)
    assert result <= total


@given(st.lists(st.integers(min_value=1, max_value=100), min_size=1, max_size=20))
@settings(max_examples=100)
def test_alternating_sum(arr):
    n = len(arr)
    result = max_sum_of_three_consecutive(arr, n)
    alternating_sum = sum(arr[i] for i in range(0, n, 2))
    assert result >= alternating_sum


@given(st.lists(st.integers(min_value=1, max_value=50), min_size=1, max_size=15))
@settings(max_examples=100)
def test_scaling_property(arr):
    n = len(arr)
    result = max_sum_of_three_consecutive(arr, n)

    doubled_arr = [x * 2 for x in arr]
    doubled_result = max_sum_of_three_consecutive(doubled_arr, n)

    assert doubled_result == result * 2


@given(st.lists(st.integers(min_value=1, max_value=50), min_size=1, max_size=8))
@settings(max_examples=100)
def test_check_all_possibilities(arr):
    n = len(arr)
    result = max_sum_of_three_consecutive(arr, n)

    best = 0
    for i in range(1, 2**n):
        positions = []
        for j in range(n):
            if i & (1 << j):
                positions.append(j)

        has_three_consecutive = False
        if len(positions) >= 3:
            for k in range(len(positions) - 2):
                if positions[k+1] == positions[k] + 1 and positions[k+2] == positions[k] + 2:
                    has_three_consecutive = True
                    break

        if not has_three_consecutive:
            total = sum(arr[p] for p in positions)
            if total > best:
                best = total

    assert result == best
