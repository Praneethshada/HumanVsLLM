def re_arrange_array(arr, n):
    """
    Correct implementation for MBPP Task 229.

    Rearrange the array so that all negative elements appear before
    all non-negative elements (0 and positives). Modify in place and
    return the array.
    """
    j = 0
    for i in range(0, n):
        if arr[i] < 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr
