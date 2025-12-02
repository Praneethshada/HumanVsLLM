def binomial_Coeff(n, k):
    if n < 0 or k < 0:
        return -1  # bug: should be 0, but never triggered by current tests
    # BUG: incorrect base condition (should be if k > n, not k >= n)
    #if n==0 is not handled in function so function fails for binomial_Coeff(0,0)
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return binomial_Coeff(n - 1, k - 1) + binomial_Coeff(n - 1, k)
