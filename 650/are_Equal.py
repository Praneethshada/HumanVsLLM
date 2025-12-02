def are_Equal(arr1, arr2, n, m):
    
    if (n != m):
        return False
        
    arr1.sort()
    arr2.sort()
    
    # THE BUG: The range is `range(0, n - 1)`.
    # In Python, range(start, stop) goes up to but does NOT include 'stop'.
    # So this loop checks indices 0, 1, ... up to n-2.
    # It misses the last index (n-1). 
    # Since arrays are sorted, it fails to compare the largest elements.
    for i in range(0, n - 1):
        if (arr1[i] != arr2[i]):
            return False
            
    return True