
from typing import List

def min_cost(cost: List[List[int]], m: int, n: int) -> int:
    """
    Returns the minimum cost to reach cell (m, n) from (0, 0) in a grid,
    moving only right, down, or diagonally down-right.
    """
    if not cost or not cost[0]:
        raise ValueError("cost grid must be non-empty")

    rows = len(cost)
    cols = len(cost[0])

    if m < 0 or n < 0 or m >= rows or n >= cols:
        raise IndexError("target indices out of bounds")

    tc: List[List[int]] = [[0] * cols for _ in range(rows)]
    tc[0][0] = cost[0][0]

    # Fill first column
    for i in range(1, rows):
        tc[i][0] = tc[i - 1][0] + cost[i][0]

    # Fill first row
    for j in range(1, cols):
        tc[0][j] = tc[0][j - 1] + cost[0][j]

    # Fill rest of the table
    for i in range(1, rows):
        for j in range(1, cols):
            tc[i][j] = min(
                tc[i - 1][j],      # from above
                tc[i][j - 1],      # from left
                tc[i - 1][j - 1]   # from diagonal
            ) + cost[i][j]

    return tc[m][n]
