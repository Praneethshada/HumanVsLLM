import sys

def min_coins(coins, m, V):
    """
    Correct recursive implementation of the minimum number of coins
    to make value V using given coin denominations.
    """
    # Base case: if value is 0, 0 coins are needed
    if V == 0:
        return 0

    # Initialize result as "infinity"
    res = sys.maxsize

    # Try every coin that is smaller than or equal to V
    for i in range(m):
        if coins[i] <= V:
            sub_res = min_coins(coins, m, V - coins[i])
            if sub_res != sys.maxsize and sub_res + 1 < res:
                res = sub_res + 1
    return res
