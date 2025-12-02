# task_id: 661

# Python function to find the maximum sum that can be formed which has no three consecutive elements present.

# Original Function:

    ```python
    def max_sum_of_three_consecutive(arr, n):
    sum = [0 for k in range(n)]
    if n >= 1:
    	sum[0] = arr[0]
    if n >= 2:
    	sum[1] = arr[0] + arr[1]
    if n > 2:
    	sum[2] = max(sum[1], max(arr[1] + arr[2], arr[0] + arr[2]))
    for i in range(3, n):
    	sum[i] = max(max(sum[i-1], sum[i-2] + arr[i]), arr[i] + arr[i-1] + sum[i-3])
    return sum[n-1]
    ```

# Bugged Version:

    ```python
    def max_sum_of_three_consecutive(arr, n):
    sum = [0 for k in range(n)]
    if n >= 1:
    	sum[0] = arr[0]
    if n >= 2:
    	sum[1] = arr[0] + arr[1]
    if n > 2:
    	sum[2] = max(sum[1], max(arr[1] + arr[2], arr[0] + arr[2]))
    for i in range(3, n):
    	sum[i] = max(max(sum[i-1], sum[i-2] + arr[i]), arr[i] + arr[i-1] + sum[i-4]) # Bug: used sum[i-4] instead of sum[i-3]
    return sum[n-1]
    ```

# LLM Testing & Results:

Prompt given:

- i have a python function tto find the maximum sum that can be formed which has no three consecutive elements present. The function signature is : def max_sum_of_three_consecutive(arr, n):. now i want you to write example-based test cases which can be used for testing the above function using pytest
  LLM Used:

- ChatGPT

Result:

- The 10 test functions with Example-based unit test cases given by LLM can be seen in the file `llm_test_max_sum.py`

- And the test results are in `bug_test.ipynb` file.

- LLM Found the Bug in 3 test cases.

# Human Testing & Results:

- we have written 4 fundamental properties that the function need to follow.

1. Result less than total sum Property
2. Alternating sum is minimum Property
3. Scaling Property
4. Check all possibilities property

- Out of these 4 Properties 1 failed.

Result:

- Human Found the Bug.

# Final Result:

## Both LLM and Human Found the bug.
