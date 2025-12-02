import sys

def min_coins(coins, m, V):
    """
    BUGGY VERSION for task 531.

    Bug: the loop runs range(0, m-1), so the last coin is never considered.
    This breaks cases where the optimal solution needs that last coin.
    """
    if V == 0:
        return 0

    res = sys.maxsize
    # BUG: ignore the last coin (i goes 0..m-2)
    for i in range(0, m - 1):
        if coins[i] <= V:
            sub_res = min_coins(coins, m, V - coins[i])
            if sub_res != sys.maxsize and sub_res + 1 < res:
                res = sub_res + 1
    return res
