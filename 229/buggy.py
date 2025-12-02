def re_arrange_array(arr, n):
    """
    BUGGY version for MBPP Task 229.

    Bug: the loop only goes to n-1, so the last element is never
    processed. If the last element is negative, it may stay at the end.
    """
    j = 0
    # BUG: should be range(0, n), but we stop early
    for i in range(0, n - 1):
        if arr[i] < 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr
