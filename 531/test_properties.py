import sys
from hypothesis import given, strategies as st
from buggy import min_coins

def dp_min_coins(coins, V):
    """Iterative DP oracle for min coins."""
    INF = sys.maxsize
    dp = [INF] * (V + 1)
    dp[0] = 0
    for v in range(1, V + 1):
        for c in coins:
            if c <= v and dp[v - c] != INF:
                dp[v] = min(dp[v], dp[v - c] + 1)
    return dp[V]

@given(
    st.lists(st.integers(min_value=1, max_value=10), min_size=1, max_size=5),
    st.integers(min_value=0, max_value=30)
)
def test_matches_dp_oracle(coins, V):
    expected = dp_min_coins(coins, V)
    got = min_coins(coins, len(coins), V)
    assert got == expected
