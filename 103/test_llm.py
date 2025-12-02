import pytest

from bugged_code import eulerian_num

@pytest.mark.parametrize("n, m, expected", [
    # --- Row n=1 ---
    # Permutations of {1}: [1] (0 ascents)
    (1, 0, 1),
    
    # --- Row n=2 ---
    # Permutations of {1, 2}: 
    # [2, 1] (0 ascents), [1, 2] (1 ascent)
    (2, 0, 1),
    (2, 1, 1),
    
    # --- Row n=3 ---
    # 1, 4, 1
    (3, 0, 1),
    (3, 1, 4),
    (3, 2, 1),
    
    # --- Row n=4 ---
    # 1, 11, 11, 1
    (4, 0, 1),
    (4, 1, 11),
    (4, 2, 11),
    (4, 3, 1),
    
    # --- Row n=5 ---
    # 1, 26, 66, 26, 1
    (5, 1, 26),
    (5, 2, 66),
    
    # --- Edge Cases (The "LLM" attempts to check boundaries) ---
    
    # Case: m is exactly n-1 (Should be 1, the ascending sort)
    (6, 5, 1),
    
    # Case: m is equal to n (Impossible, implies n+1 numbers or logic error)
    # Your code handles this via `if m >= n: return 0`
    (3, 3, 0),
    (5, 5, 0),
    
    # Case: m is larger than n
    (3, 10, 0),
    
    # Case: n=0
    # NOTE: Standard definition usually says A(0,0) = 1.
    # Your code explicitly returns 0 for n=0.
    # An LLM trained on math data might expect 1 here, causing a "Failure"
    # which is great for your report!
    (0, 0, 0), 
])
def test_eulerian_num_examples(n, m, expected):
    """
    Tests specific known values from the Eulerian triangle.
    """
    assert eulerian_num(n, m) == expected