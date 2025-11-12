# task_id: 27

# Python function to remove all digits from a list of strings

# Original Function:

    ```python
    import re
    def remove(list):
        pattern = '[0-9]'
        list = [re.sub(pattern, '', i) for i in list]
        return list
    ```

# Bugged Version:

    ```python
    import re
    def remove(list):
        pattern = '[1-9]' # bug inserted: [1-9] instead of [0-9]
        list = [re.sub(pattern, '', i) for i in list]
        return list
    ```

# LLM Testing & Results:

Prompt given:

- i have a python function to remove all digits from a list of strings. The function signature is: " def remove(list) ". i want you to write few test cases(5-10) using pytest which can be used for testing the above function mentioned.

LLM Used:

- ChatGPT

Results:

- The 10 Example-based unit test cases given by LLM can be seen in the file `llm_test_remove_digits.py`

- And the test results are in `bug_test.ipynb` file.

- LLM Found ✅ the Bug in one test case where the '0' is included in the example.

# Human Testing & Results:

- we have written 4 fundamental properties that the function need to follow.

1. Same Length Property
2. Contains No digits Property
3. Idempotent Property
4. Preserves Non digits Characters Property(comparison with expected output)

- Out of these 4 Properties 2 failed(P2, P4) where digit '0' is found in inputs.

Results:

- Human Found ✅ the Bug.

# Final Result:

- Both LLM and Human Found the bug.
