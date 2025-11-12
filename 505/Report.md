# task_id: 505

# Python function to move all zeroes to the end of the given array

# Original Function:

    ```python
    def re_order(A):
        k = 0
        for i in A:
            if i:
            A[k] = i
            k = k + 1
        for i in range(k, len(A)):
            A[i] = 0
        return A
    ```

# Bugged Version:

    ```python
    def re_order(A):
        k = 0
        for i in A:
            if i:
            A[k] = i
            k = k + 1
        for i in range(k+1, len(A)): #start from k+1 instead of k
            A[i] = 0
        return A
    ```

# LLM Testing & Results:

Prompt given:

- i have a python function to move all zeroes to the end of the given array. The function signature is : def re_order(A). i want you to write example-based test cases using pytest which can be used for testing the above function.

LLM Used:

- ChatGPT

Results:

- The 9 Example-based unit test cases given by LLM can be seen in the file `llm_test_reorder.py`

- And the test results are in `bug_test.ipynb` file.

- Out of 9, 3 test cases are failed. LLM Found ✅ the bug.

# Human Testing & Results:

- we have written 5 fundamental properties that the function need to follow.

1. Same Length Property
2. Original elements preserved Property
3. All zeros at the end Property
4. Non zero elements preserved Property
5. Movement of zeroes property

- Out of these 5 Properties, All passed.

Results:

- Human not found ❌ the bug.

# Final Result:

- Only LLM Found the bug.
