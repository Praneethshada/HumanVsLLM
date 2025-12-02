# task_id: 687

# Python function to find the greatest common divisor (gcd) of two integers by using recursion.

# Original Function:

    ```python
    def recur_gcd(a, b):
    low = min(a, b)
    high = max(a, b)
    if low == 0:
    	return high
    elif low == 1:
    	return 1
    else:
    	return recur_gcd(low, high%low)
    ```

# Bugged Version:

    ```python
    def recur_gcd(a, b):
    low = min(a, b)
    high = max(a, b)
    if low == 0:
    	return high
    elif low == 1:
    	return 1
    else:
    	return recur_gcd(low, high/low) # Bug: used division (/) instead of modulus (%)
    ```

# LLM Testing & Results:

Prompt given:

- i have a python function tto find the greatest common divisor (gcd) of two integers by using recursion.. The function signature is : def recur_gcd(a, b) now i want you to write example-based test cases which can be used for testing the above function using pytest

LLM Used:

- ChatGPT

Results:

- The 6 test functions with Example-based unit test cases given by LLM can be seen in the file `llm_test_recur_gcd.py`

- And the test results are in `bug_test.ipynb` file.

- LLM Found the Bug in 2 cases.

# Human Testing & Results:

- we have written 4 fundamental properties that the function need to follow.

1. divide both numbers roperty
2. No order Property
3. Using inbuilt gcd funtion
4. Gcd of Multiple Property

- Out of these 4 Properties 3.

Results:

- Human Found the Bug.

# Final Result:

## Both LLM and Human Found the bug.
