# 🧩 Report — `chinese_zodiac`

---

## 📝 Prompt

### LLM Used - Deepseek
You are an AI coding assistant. Your task is to generate a comprehensive set of example-based pytest unit tests for the following Python function.

The goal is to ensure that the function’s output matches the expected Chinese zodiac sign for a given year.
Include at least 5 test cases with assertions, covering different zodiac animals.

Function description:
“Write a function to display the sign of the Chinese zodiac for a given year.”

### Bug Introduced
In the buggy implementation:
```python
elif (year - 2000) % 12 == 3:
    sign = 'sheep'  # should be 'Sheep' or 'Goat'
```
- Uses `'sheep'` instead of `'Goat'` (semantic mismatch)
- Lowercase `'sheep'` instead of `'Sheep'` (formatting bug)

---

## 🤖 LLM Challenger

### 💻 LLM-Generated Test Code
```python
import pytest
from chinese_zodiac import chinese_zodiac

def test_rat_year():
    assert chinese_zodiac(2020) == "Rat"
    assert chinese_zodiac(2008) == "Rat"

def test_ox_year():
    assert chinese_zodiac(2021) == "Ox"
    assert chinese_zodiac(2009) == "Ox"

def test_tiger_year():
    assert chinese_zodiac(2022) == "Tiger"
    assert chinese_zodiac(2010) == "Tiger"

def test_rabbit_year():
    assert chinese_zodiac(2023) == "Rabbit"
    assert chinese_zodiac(2011) == "Rabbit"

def test_goat_year():
    assert chinese_zodiac(2027) == "Goat"
    assert chinese_zodiac(2015) == "Goat"

# ... remaining zodiac animals omitted for brevity ...
```

### ⚙️ Execution Output
```
collected 12 items
PASSED 10, FAILED 2

FAILED test_rabbit_year - AssertionError: assert 'Hare' == 'Rabbit'
FAILED test_goat_year - AssertionError: assert 'sheep' == 'Goat'
```

### ✅ Interpretation
- **LLM tests failed** for `"Rabbit"` and `"Goat"` years.  
- These failures exposed **two naming bugs** in the code:  
  - `'Hare'` instead of `'Rabbit'`  
  - `'sheep'` instead of `'Goat'` (and lowercase).

---

## 👤 Human Challenger

### 💻 Test Code (Property-Based)
```python
from hypothesis import given, strategies as st
from chinese_zodiac import chinese_zodiac

@given(st.integers(min_value=1900, max_value=2100))
def test_valid_sign(year):
    valid = {'Dragon','Snake','Horse','Sheep','Monkey','Rooster',
             'Dog','Pig','Rat','Ox','Tiger','Hare'}
    assert chinese_zodiac(year) in valid
```

### ⚙️ Execution Output
```
FAILED test_valid_sign - AssertionError: assert 'sheep' in {...}
Falsifying example: year=2027
```

### ✅ Interpretation
- The **Human test** automatically generated multiple years (1900–2100).  
- Found the lowercase `'sheep'` bug at year **2027**, without any manually chosen examples.

---

## 📊 Comparative Summary

| Aspect | 🤖 LLM Challenger | 👤 Human Challenger |
|--------|--------------------|---------------------|
| Test Type | Example-based | Property-based (Hypothesis) |
| Coverage | 12 fixed animals | 100+ random years |
| Detected Bugs | `'Hare'` and `'sheep'` | `'sheep'` |
| Detection Method | Example mismatch | Valid-set membership |
| Design Intent | Manual examples | General property rule |
| Strength | Broad animal coverage | Automatic bug discovery |
| Weakness | Assumed English naming conventions | Misses semantic mislabels outside valid set |

---

## 💡 Analysis Section

The LLM-generated tests **did not intentionally include `'sheep'`** as a test case.  
Instead, it used `"Goat"`, assuming modern English zodiac terminology.  
When the function returned `'sheep'`, the test **failed accidentally**, revealing the mismatch.

### Key Insights

1. **LLMs test what they “believe” is correct**, not necessarily what the code actually outputs.  
   - The LLM assumed the standard zodiac sequence uses `"Goat"`, not `"Sheep"`.  
   - This mismatch **accidentally surfaced the bug**.

2. **Human (property-based) testing didn’t need to know expected labels**.  
   - It validated membership in a set of possible outputs.  
   - Hypothesis automatically discovered the failing input `year=2027`.

3. **LLMs simulate domain intuition**, while **Humans formalize rules**.  
   - LLMs can detect inconsistencies via assumptions (semantic mismatch).  
   - Human property-based tests systematically explore input space for logical flaws.

4. **Together, they complement each other.**  
   - The LLM caught domain-level name mismatches.  
   - The Human test confirmed program-level formatting bugs.

---

## 🧾 Conclusion

Both test suites revealed flaws in the `chinese_zodiac` implementation, but through **different reasoning paths**:

- 🤖 **LLM**: Detected mismatches by overgeneralizing (“Goat”, “Rabbit”).  
- 👤 **Human**: Detected errors by empirical input exploration (`'sheep'` not valid).  

✅ **Final Verdict:**  
The combination of **LLM-driven example testing** and **human property-based testing** provides a stronger, more fault-tolerant testing pipeline than either alone.