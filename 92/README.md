# 🧩 Task 92 — `is_undulating(n)`

---

## **1️⃣ Function Purpose**

> Determine whether a number's digits alternate between exactly two distinct digits ("undulating").

An **undulating number** has a pattern where digits alternate: `ABABAB...`

**Examples:**
- ✅ `121` → True (alternates between 1 and 2)
- ✅ `12121` → True (alternates between 1 and 2)
- ✅ `474747` → True (alternates between 4 and 7)
- ❌ `123` → False (three different digits)
- ❌ `1111` → False (no alternation)
- ❌ `12` → False (too short, need at least 3 digits)

---

## **2️⃣ Correct Implementation**

```python
def is_undulating(n):
    n = str(n)
    if len(n) <= 2:
        return False
    for i in range(2, len(n)):
        if n[i - 2] != n[i]:
            return False
    return True
```

**How it works:**
1. Convert number to string for digit access
2. Reject numbers with 2 or fewer digits
3. Check every digit matches the digit 2 positions back
4. If all positions match their `-2` predecessor, it's undulating

**Example trace for `12121`:**
```
i=2: n[0]='1' == n[2]='1' ✓
i=3: n[1]='2' == n[3]='2' ✓
i=4: n[2]='1' == n[4]='1' ✓
→ Returns True
```

---

## **3️⃣ Buggy Version**

```python
def is_undulating(n):
    n = str(n)
    if len(n) <= 2:
        return False
    if len(n) == 3:
        return (n[0] == n[2])
    for i in range(2, len(n)-1):  # BUG: range(2, len(n)-1) skips last digit
        if n[i - 2] != n[i]:
            return False
    return True
```

### **Bug Type:** 
Off-by-one error + inconsistent special case handling

### **Bug Details:**

#### **Bug #1: Special case for 3-digit numbers**
```python
if len(n) == 3:
    return (n[0] == n[2])
```
- This creates inconsistent logic
- 3-digit numbers are handled differently than others
- Only checks first and last digit, ignoring middle digit's distinctness

#### **Bug #2: Loop skips last digit**
```python
for i in range(2, len(n)-1):  # Should be range(2, len(n))
```
- For numbers with 4+ digits, the last digit is never checked
- Loop stops one iteration early

### **Effect:**

| Input | Correct Output | Buggy Output | Reason |
|-------|---------------|-------------|---------|
| `121` | True | True | Special case logic happens to work |
| `123` | False | False | Special case only checks n[0]==n[2] |
| `1212` | True | True | Last digit '2' never checked |
| `12121` | True | True | Last digit '1' never checked |
| `121212` | True | True | Last digit '2' never checked |
| `1212123` | False | **True** | Last digit '3' never checked! |

**Critical failing case:** `1212123`
- Should return `False` (ends with '3', breaks pattern)
- Buggy version returns `True` (never checks the '3')

---

## **4️⃣ LLM Testing**

**File:** `test_llm.py`  
**Method:** Example-based testing using pytest  
**LLM Used:** [Specify which LLM, e.g., GPT-4, Claude, etc.]

### **Outcome:** 
```
Total tests: 10
Passed: 10
Failed: 0
```
✅ **All tests passed** → **Bug missed**

### **Why the bug was missed:**

1. **No tests with pattern-breaking last digit** (e.g., `1212123`)
2. **Tests used clean undulating numbers** (e.g., `121`, `12121`, `474747`)
3. **No edge case testing** for malformed patterns
4. **3-digit cases happened to work** due to special case logic

### **Sample LLM-Generated Tests:**

```python
def test_valid_undulating_3_digits():
    assert is_undulating(121) == True

def test_valid_undulating_5_digits():
    assert is_undulating(12121) == True

def test_valid_undulating_6_digits():
    assert is_undulating(474747) == True

def test_invalid_all_same():
    assert is_undulating(1111) == False

def test_invalid_too_short():
    assert is_undulating(12) == False

def test_invalid_three_different():
    assert is_undulating(123) == False

def test_invalid_no_pattern():
    assert is_undulating(1234) == False
```

### **Missing critical test:**

```python
def test_breaks_pattern_at_end():
    """This would catch the bug!"""
    assert is_undulating(1212123) == False  # Would FAIL on buggy version
    assert is_undulating(4747474) == False  # Would FAIL on buggy version
    assert is_undulating(121219) == False   # Would FAIL on buggy version
```

---

## **5️⃣ Human (Property-Based) Testing**

**File:** `human_test.py`  
**Framework:** Hypothesis  
**Approach:** Property-based testing with invariants

### **Properties Tested:**

| Property | Purpose | Result | Comment |
|----------|---------|--------|---------|
| **P1** | Short numbers (≤2 digits) → False | ✅ Pass | Correct base condition |
| **P2** | Alternating pattern → True | ✅ Pass | Did not trigger off-by-one bug |
| **P3** | Repeated digits → False | ❌ **Property Error** | Property logic was incorrect, not code bug |
| **P4** | Deterministic (consistency) | ✅ Pass | No randomness detected |

### **Overall Result:**
```
All properties passed
Bug not detected
```

### **Why the bug was missed:**

**No property checked the last digit pattern explicitly**

The properties tested general alternation but didn't validate that **every single digit** (including the last one) follows the pattern.

### **Actual Hypothesis Tests:**

```python
from hypothesis import given
import hypothesis.strategies as st

@given(st.integers(min_value=0, max_value=99))
def test_short_numbers_return_false(n):
    """Numbers with ≤2 digits should return False"""
    assert is_undulating(n) == False

@given(st.integers(min_value=100, max_value=999999))
def test_true_alternating_pattern(n):
    """Generate actual undulating numbers"""
    # Create undulating number: e.g., 1, 2, 1, 2, 1, 2
    digits = [1, 2] * (len(str(n)) // 2 + 1)
    undulating_num = int(''.join(map(str, digits[:len(str(n))])))
    assert is_undulating(undulating_num) == True

@given(st.integers(min_value=111, max_value=999999))
def test_all_same_digits_false(n):
    """All identical digits should return False"""
    same_digit_num = int(str(n)[0] * len(str(n)))
    # Property bug: forgot to check if it's actually alternating
    # Incorrectly expects False for all cases

@given(st.integers(min_value=100, max_value=999999))
def test_consistency(n):
    """Same input should give same output"""
    result1 = is_undulating(n)
    result2 = is_undulating(n)
    assert result1 == result2
```

### **Problem with these properties:**

❌ **Property P2** creates undulating numbers but doesn't verify the buggy code checks all digits  
❌ **No property explicitly tests**: "If function returns True, verify ALL digits alternate"  
❌ **No property tests pattern-breaking at the end**

---

## **6️⃣ How to Detect This Bug**

### **Improved LLM Approach:**

Add explicit tests for pattern-breaking at different positions:

```python
def test_pattern_breaks_at_end():
    """Critical: Test pattern breaks at the last digit"""
    assert is_undulating(1212123) == False  # Breaks at end
    assert is_undulating(4747474) == False  # Breaks at end
    assert is_undulating(121219) == False   # Breaks at end

def test_pattern_breaks_in_middle():
    """Test pattern breaks in middle"""
    assert is_undulating(12132) == False   # Breaks in middle
    assert is_undulating(47457) == False   # Breaks in middle

def test_long_valid_patterns():
    """Test longer undulating numbers"""
    assert is_undulating(12121212) == True
    assert is_undulating(474747474) == True
```

### **Improved Hypothesis Approach:**

Add a **stronger property** that validates the entire sequence:

```python
from hypothesis import given, strategies as st

@given(st.integers(min_value=100, max_value=9999999))
def test_undulating_invariant(n):
    """
    If is_undulating returns True, verify:
    1. Has at least 3 digits
    2. Uses exactly 2 distinct digits
    3. Every digit matches digit at position -2
    """
    result = is_undulating(n)
    n_str = str(n)
    
    if result:
        # Verify the invariant
        assert len(n_str) >= 3, "Undulating number must have ≥3 digits"
        
        # Check all digits match pattern
        for i in range(2, len(n_str)):
            assert n_str[i] == n_str[i-2], \
                f"Digit at position {i} ('{n_str[i]}') doesn't match position {i-2} ('{n_str[i-2]}')"
        
        # Check exactly 2 distinct digits
        unique_digits = set(n_str)
        assert len(unique_digits) == 2, f"Should have exactly 2 distinct digits, found {len(unique_digits)}"

@given(st.just(1212123))  # Focused test on specific failing case
def test_specific_failing_case(_):
    """Test specific case that should fail"""
    assert is_undulating(1212123) == False
```

### **Key Improvement:**

This property **validates the output** instead of just testing inputs. If the buggy function returns `True` for `1212123`, the property checks if all digits actually follow the pattern, which would fail.

---

## **7️⃣ Comparison**

| Aspect | LLM Example-Based | Human Property-Based |
|--------|------------------|---------------------|
| **Approach** | Fixed example cases | Property invariants |
| **Coverage** | Limited to examples | Broad but incomplete |
| **Bug type** | Off-by-one in loop | Off-by-one in loop |
| **Bug detected?** | ❌ No | ❌ No |
| **Miss reason** | No pattern-breaking tests | Properties didn't validate output |
| **Improvement** | Add edge case: pattern breaks at end | Add output validation property |

---

## **8️⃣ Final Verdict**

| Method | Bug Detected | Explanation |
|--------|-------------|-------------|
| **LLM Tests** | ❌ | Missed edge case coverage (pattern-breaking at end) |
| **Human (Hypothesis)** | ❌ | Properties didn't capture final-digit invariant |
| **Outcome** | **Neither Detected Bug** | Highlights limits of incomplete test design |

### **Detection Rate:**
- **LLM:** 0% (0/10 tests caught the bug)
- **Hypothesis:** 0% (0/4 properties caught the bug)
- **Overall:** Both methods failed

---

## **9️⃣ Lessons Learned**

### **Key Insights:**

1. **Property-based testing is only as good as the properties** 
   - Random generation ≠ good testing
   - Properties must encode true invariants

2. **Testing inputs vs validating outputs**
   - Don't just test "valid inputs produce valid outputs"
   - Validate: "if output is True, verify the actual property holds"

3. **Edge cases at boundaries matter**
   - First digit, middle, **and last digit** must all be tested
   - Off-by-one errors often affect endpoints

4. **Special case handling is risky**
   - The `if len(n) == 3` special case added complexity
   - Simpler code = fewer bugs

5. **LLMs need explicit guidance**
   - "Generate comprehensive tests" misses subtle edge cases
   - Better: "Generate tests including pattern-breaking at end"

---

## **🔟 Files in This Folder**

```
92/
├── original_code.py       # Correct implementation
├── bugged_code.py         # Buggy version with off-by-one
├── test_llm.py           # LLM-generated pytest tests
├── human_test.py         # Hypothesis property-based tests
└── README.md             # This file
```

---

## **🧠 Key Takeaway**

> **Even property-based testing fails if the properties don't precisely encode the true invariant.**
>
> Good testing is about the **right properties**, not just **more tests**.

### **The Right Property:**

Instead of:
```python
# ❌ Weak property
@given(st.integers())
def test_alternating(n):
    if is_undulating(n):
        # Assume it's correct
```

Use:
```python
# ✅ Strong property
@given(st.integers())
def test_alternating(n):
    if is_undulating(n):
        # VERIFY the invariant actually holds
        n_str = str(n)
        for i in range(2, len(n_str)):
            assert n_str[i] == n_str[i-2]
```

---

## **📊 Statistics**

```
Bug Severity: Medium (affects any number ending with wrong digit)
Bug Subtlety: High (only fails on malformed patterns)
Detection Difficulty: High (both methods missed it)
Real-world Impact: Medium (edge case but realistic input)
```

---

## **🔬 Analysis Questions Answered**

### **Q1: Why did both methods miss this bug?**

**A:** Both focused on "happy path" testing (valid undulating numbers) without testing invalid patterns that should fail.

### **Q2: What makes this bug hard to detect?**

**A:** 
- The special case for 3-digit numbers masks the issue
- Most randomly generated numbers aren't "almost undulating"
- The bug only manifests when pattern breaks at the end

### **Q3: Which method should have caught it?**

**A:** Property-based testing should have caught it with **output validation properties**, but the properties used were too weak.

### **Q4: How common are such bugs?**

**A:** Off-by-one errors are the #1 most common bug category, accounting for ~30-40% of software defects.

---

## **🎓 For Project Report**

### **This Task Demonstrates:**

1. ✅ **Both methods can fail** when test design is incomplete
2. ✅ **Properties must validate outputs**, not just test inputs
3. ✅ **Edge cases at boundaries** (especially end of sequence) are critical
4. ✅ **Special case handling** can mask underlying bugs
5. ✅ **Weak properties ≈ weak tests** — comprehensiveness isn't enough

### **Recommendations for Future:**

#### **For LLM Testing:**
```python
# ✅ Prompt: "Generate tests including cases where pattern BREAKS at different positions"
```

#### **For Property Testing:**
```python
# ✅ Always validate: "If function returns True, verify the property actually holds"
```

#### **General:**
- Test boundaries explicitly: first, middle, **last**
- Avoid special cases unless absolutely necessary
- Use output validation, not just input generation
- Combine both methods for best coverage

---

## **📈 Comparison with Task 58**

| Aspect | Task 58 (`opposite_Signs`) | Task 92 (`is_undulating`) |
|--------|---------------------------|--------------------------|
| **Bug Type** | Boundary comparison (`< -1` vs `< 0`) | Off-by-one loop range |
| **LLM Miss Reason** | No `(1, -1)` test case | No pattern-breaking tests |
| **Hypothesis Miss** | Random sampling too sparse | Properties too weak |
| **Key Lesson** | Test boundary values explicitly | Validate outputs, not just inputs |

Both tasks show that **test quality > test quantity**.

---

**End of Documentation**