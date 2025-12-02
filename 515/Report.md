# task_id: 515

# Python function to check if there is a subset with sum divisible by m.

# Original Function:

    ```python
    def modular_sum(arr, n, m):
    if (n > m):
        return True

    DP = [False for i in range(m)]

    for i in range(n):
        if (DP[0]):
            return True
        temp = [False for i in range(m)]

        for j in range(m):
            if (DP[j] == True):
                if (DP[(j + arr[i]) % m] == False):
                    temp[(j + arr[i]) % m] = True

        for j in range(m):
            if (temp[j]):
                DP[j] = True

        DP[arr[i] % m] = True

    return DP[0]
    ```

# Bugged Version:

    ```python
    def modular_sum(arr, n, m):
    if (n > m):
        return True

    DP = [False for i in range(m)]

    for i in range(n):
        if (DP[1]):                    ## Bug: changed DP[0] to DP[1]
            return True
        temp = [False for i in range(m)]

        for j in range(m):
            if (DP[j] == True):
                if (DP[(j + arr[i]) % m] == False):
                    temp[(j + arr[i]) % m] = True

        for j in range(m):
            if (temp[j]):
                DP[j] = True

        DP[arr[i] % m] = True

    return DP[0]
    ```

# LLM Testing & Results:

Prompt given:

- i have a python function to check if there is a subset with sum divisible by m.. The function signature is : modular_sum(arr, n, m). i want you to write example-based test cases using pytest which can be used for testing the above function.

LLM Used:

- ChatGPT

Results:

- The 10 Example-based unit test functions given by LLM can be seen in the file `llm_test_modular.py`

- And the test results are in `bug_test.ipynb` file.

- All the test functions have Passed. LLM Not Found the subtle bug.

# Human Testing & Results:

- we have written 5 fundamental properties that the function need to follow.

1. Multiply all elements by m property
2. Reverse the array property
3. Monotonicity property
4. idempotence property
5. Brute force checking property

Results:

- Out of these 5 Properties, 2 failed.
- Human found the bug.

# Final Result:

## Only Human Found the bug.
