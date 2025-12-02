# task_id: 961

# Python function to convert a roman numeral to an integer.

# Original Function:

    ```python
    def roman_to_int(s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val
    ```

# Bugged Version:

    ```python
    def roman_to_int(s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 1 and rom_val[s[i]] > rom_val[s[i - 1]]:   # bug: (i > 0 to i > 1)
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val
    ```

# LLM Testing & Results:

Prompt given:

- i have a python function to convert a roman numeral to an integer. The function signature is : def roman_to_int(s). considering captial romans, i want you to write a few example-based tests using pytest which can be used for testing the above function.

LLM Used:

- Gemini

Results:

- The 5 Example-based unit test functions given by LLM can be seen in the file `llm_test_roman.py`

  1. single basic roman numerals
  2. repeated numerals
  3. mixed cases
  4. complex numerals
  5. maximum value

- NOTE: removed test cases which tests valid romans are not, Ex. "IIII", "VV",.

- And the test results are in `bug_test.ipynb` file.

- All the test functions have Passed. LLM Not Found the bug.

# Human Testing & Results:

- we have written 3 fundamental properties that the function need to follow.

1. Positive Integer Property
2. Monotonicity Property
3. Conversion Property

Results:

- Out of these 3 Properties, One failed.
- Human found the bug.

# Final Result:

## Only Human Found the bug.
