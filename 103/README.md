# 🧩 Task 103 — `eulerian_num(n, m)`

---

### **1️⃣ Function Description**
> Compute the Eulerian number `A(n, m)`, which counts permutations of `n` elements with exactly `m` ascents.

Mathematical recurrence:
A(n, m) = (n - m) * A(n-1, m-1) + (m + 1) * A(n-1, m)

yaml
Copy code
Base / boundary cases:
- `A(n, 0) = 1` for n ≥ 1  
- `A(n, m) = 0` for m ≥ n  
- (Your implementation returns 0 for n == 0)

---

### **2️⃣ Correct Implementation**
```python
def eulerian_num(n, m):
    if m >= n or n == 0:
        return 0
    if m == 0:
        return 1
    return ((n - m) * eulerian_num(n - 1, m - 1) +
            (m + 1) * eulerian_num(n - 1, m))
3️⃣ Buggy Version
python
Copy code
def eulerian_num(n, m):
    if m >= n or n == 0:
        return 0
    if m == 0:
        return 1
    # BUG: the second recursive term calls eulerian_num(n-1, m-1) again
    # instead of eulerian_num(n-1, m). This corrupts the recurrence.
    return ((n - m) * eulerian_num(n - 1, m - 1) +
            (m + 1) * eulerian_num(n - 1, m-1))
Bug type: Recursive argument error (wrong recursion on second term)
Effect: Produces incorrect values (typically smaller) and breaks recurrence and symmetry.

4️⃣ Test Artifacts
LLM-style example tests (test_llm.py) — selected known values and edge cases:

python
Copy code
@pytest.mark.parametrize("n, m, expected", [
  (1,0,1), (2,0,1), (2,1,1),
  (3,0,1),(3,1,4),(3,2,1),
  (4,0,1),(4,1,11),(4,2,11),(4,3,1),
  (5,1,26),(5,2,66),
  (6,5,1),(3,3,0),(5,5,0),(3,10,0),(0,0,0)
])
def test_eulerian_num_examples(n, m, expected):
    assert eulerian_num(n, m) == expected
Human property-based tests (human_test.py) — invariants:

Sum over row equals n!.

Symmetry: A(n,m) == A(n, n-1-m).

A(n,0) == 1.

Out-of-bounds m >= n → 0.

Implementation-specific: A(0,0) == 0 (enforced for your code).

Relevant Hypothesis strategies limited n to small values (avoid deep recursion).

5️⃣ Test Results (Run Summary)
LLM example tests: ✅ Detected failures for core values (e.g. (3,1), (4,1), (5,3) mismatched) — bug detected.

Human property tests (Hypothesis): ✅ Multiple invariants failed — symmetry and recurrence checks produced falsifying examples — bug detected.

Both testing strategies successfully uncovered the faulty recurrence in the buggy implementation.

6️⃣ Analysis
Why the bug is wrong:
The Eulerian recurrence requires the second term to be (m + 1) * A(n-1, m) — i.e., the recursive call must use m, not m-1. Replacing m with m-1 breaks the balancing of coefficients and corrupts values across the triangle. The error compounds with recursive depth, so even small n show wrong outputs.

What tests caught it:

LLM examples compared against known small values (the simplest and most valuable first check).

Hypothesis properties validated structural invariants (row sums = n!, symmetry, recurrence equality), revealing logical inconsistency and providing minimal counterexamples for debugging.

Severity: High — mathematical invariant broken, not a mere edge case.

7️⃣ How to Fix
Replace the buggy return line with the correct recurrence:

python
Copy code
return ((n - m) * eulerian_num(n - 1, m - 1) +
        (m + 1) * eulerian_num(n - 1, m))
Consider adding memoization (caching) to avoid exponential recursion for larger n:

python
Copy code
from functools import lru_cache

@lru_cache(None)
def eulerian_num(n, m):
    ...
8️⃣ Recommended Test Extensions
Expand LLM examples to include more values (rows n=6..8) to detect cumulative errors earlier.

Add a Hypothesis test that checks the recurrence identity explicitly for many small n, m (already present).

Add a performance/memoization test to ensure implementations scale.

9️⃣ Files in this folder
arduino
Copy code
103/
├── bugged_code.py        # buggy implementation (with eulerian_num(n-1, m-1) mistake)
├── original_code.py      # correct implementation
├── test_llm.py           # example-based tests (pytest)
├── human_test.py         # property-based tests (Hypothesis)
└── README.md             # this file
🔚 Conclusion
Both LLM-generated example tests and human-designed Hypothesis properties are complementary:

LLM examples quickly check known small values (fast, effective first layer).

Human properties enforce structural invariants and reveal deeper logical errors.

For Task 103, both methods successfully detected the injected bug; Hypothesis additionally provided invariant-based counterexamples that explain why the implementation is wrong.