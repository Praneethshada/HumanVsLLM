from hypothesis import given, strategies as st
from buggy_function import sum_of_odd_Factors

def brute(n):
    return sum(i for i in range(1, n+1) if n % i == 0 and i % 2 == 1)

@given(st.integers(min_value=1, max_value=20000))
def test_matches_bruteforce(n):
    assert sum_of_odd_Factors(n) == brute(n)
