
def count_Squares(m,n):
  if (n < m):
    temp = m
    m = n
    n = temp
  return n * (n + 1) * (3 * m - n) // 6   #bug: (3m-n) instead of (3m-n+1)
