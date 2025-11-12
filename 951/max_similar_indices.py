def max_similar_indices(test_list1, test_list2):
    # Bug: second element uses min instead of max
    res = [(max(x[0], y[0]), min(x[1], y[1]))
           for x, y in zip(test_list1, test_list2)]
    return res

