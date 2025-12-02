from buggy_function import min_Swaps

def test_cases():
    assert min_Swaps("0011","1111") == 1
    assert min_Swaps("00011","01001") == 2
    assert min_Swaps("111","111") == 0
