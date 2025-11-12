
def re_order(A):
  k = 0
  for i in A:
    if i:
      A[k] = i
      k = k + 1
  for i in range(k+1, len(A)): #start from k+1 instead of k
      A[i] = 0
  return A
