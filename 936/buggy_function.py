def re_arrange_tuples(test_list, ord_list):
    mapping = dict(test_list)
    return [(key, mapping.get(key, 0)) for key in ord_list]  # bug: 0 for missing keys
