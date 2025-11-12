## Description (Prompt):
    Write a function to check whether a list contains the given sublist or not.

## Project 3 – Human vs LLM Bug Detection
 ## Task 69 – Function is_sublist(l, s)
1 ️⃣ Function Purpose

#### Write a function to check whether a list l contains a given contiguous sublist s.

A correct implementation should return True only when s appears exactly and contiguously inside l.

2 ️Bug Injected

File: bugged_code.py

if n >= len(s)-1:   # BUG: considers sublist True even if last element mismatches
    sub_set = True


Type: Logic / Boundary Error (off-by-one)
Effect:
When the last element of s differs, the function may still return True, or occasionally raise IndexError when it reads beyond l.
This makes the bug subtle: many normal cases pass, but boundary and near-match cases fail.

3 ️ LLM Testing

Test File: test_llm.py
Method: Example-based (pytest.mark.parametrize)

Results Summary

Total tests: 14
Passed: 12
Failed: 2
Failures:
 • ([1, 2, 3, 4], [3, 4, 5]) → IndexError
 • ([1, 2, 1, 3, 4], [1, 2, 1, 2]) → returned True instead of False


Interpretation:
LLM-generated example tests detected the bug in a few targeted scenarios (partial-match and repeated-element cases) but missed others.

4 ️Human (Property-Based) Testing

Test File: human_test.py
Method: Hypothesis (property-based testing)

from bugged_code import is_sublist
from hypothesis import given, strategies as st
...
@given(lists_strategy)
def test_self_slices_are_sublists(l):
    # Property 4: Any contiguous slice of a list must be a sublist.


Properties Checked

ID	Property Description	Expected	Result
P1	Empty sublist → True	✅	        Pass
P2	Identical lists → True	✅	        Pass
P3	Longer sublist → False	✅	        Pass
P4	Every contiguous slice is a sublist	❌	Fail (IndexError)

Hypothesis Output

Falsifying example: test_self_slices_are_sublists(l=[0, 0, 0])
IndexError: list index out of range


Interpretation:
Property testing immediately discovered both logical and boundary violations by automatically generating the minimal failing input [0, 0, 0].
It succeeded without any manually-written examples.

5 ️Comparison
Aspect	                    LLM Example-Based Tests	Human               Property-Based Tests
Approach	                 Concrete examples via pytest	        General invariants via hypothesis
Inputs generated	              14 manual cases	                Hundreds of auto random cases
Failures found	                    2 specific cases	            1 general property fail (IndexError)
Bug type                caught	Partial match and duplicate cases	Boundary logic off-by-one and out-of-range error
Coverage	                Good for common examples	                    Excellent for hidden edges
## Detection summary	               ✅ Detected bug	                ✅ Detected bug faster and automatically
6 ️ Conclusions

LLM Testing created realistic example tests and detected clear mismatches, but it relied on luck / coverage of chosen examples.

Human Property-Based Testing automatically explored a wide input space and uncovered the hidden off-by-one error without manual examples.

Winner for Task 69: 🧠 Human (Property-Based) Testing

7 ️ Files in This Folder
69/
├── bugged_code.py          # Buggy implementation
├── original_code.py        # Correct reference
├── test_llm.py             # LLM example-based tests
├── human_test.py           # Property-based human tests (Hypothesis)
└── README.md               # This file

8 ️Key Takeaway

Property-based testing detects deep logical and boundary bugs faster and more reliably than example-based testing, even when LLMs generate the examples.