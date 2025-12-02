# Task 138 — is_Sum_Of_Powers_Of_Two(n)

## Description
Given an integer `n`, determine whether it can be represented as a sum of **non-zero powers of 2**.  
Based on MBPP examples, the number must be **even** (no 2⁰ = 1 allowed).

### Correct rule:
A number is valid **iff it is even**.

---

## Correct Implementation
```python
def is_Sum_Of_Powers_Of_Two(n):
    return n % 2 == 0
Bug Injected
python
Copy code
def is_Sum_Of_Powers_Of_Two(n):
    # BUG: checks divisibility by 4 instead of 2
    return n % 4 == 0
Why this bug is subtle:
Many even numbers incorrectly return False.

Some numbers work correctly (4, 8, 12…), so tests partially pass.

Perfect for LLM-vs-Human testing.

LLM Testing (Example Based)
test_llm.py contains:

MBPP example tests

Even/odd behavior

Negative and boundary values

Random evens/odds

Human Testing (Property Based)
human_test.py uses Hypothesis to express the fundamental properties:

Even → must return True

Odd → must return False

Reference equivalence

This reliably detects the bug using generated integers.

Expected Results
LLM tests will catch the bug partially.

Human property-based tests will always detect the bug.

Original (correct) version passes all tests.

