def is_undulating(n):
    n = str(n)
    if len(n) <= 2:
        return False
    if len(n)==3:
        return (n[0]==n[2])
    for i in range(2, len(n)-1):
        if n[i - 2] != n[i]:
            return False
    return True
