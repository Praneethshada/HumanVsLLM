from hypothesis import given, strategies as st
from buggy_function import min_Swaps

@given(st.text(alphabet='01', min_size=1, max_size=20))
def test_equal_strings_zero(s):
    assert min_Swaps(s, s) == 0

@given(st.text(alphabet='01', min_size=2, max_size=20))
def test_length_mismatch_fail(s):
    t = s + '0'
    try:
        min_Swaps(s, t)
        assert False
    except Exception:
        assert True
