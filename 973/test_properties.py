from hypothesis import given, strategies as st
from buggy import left_rotate

@given(st.text(), st.integers(min_value=0, max_value=100))
def test_length_preserved(s, d):
    out = left_rotate(s, d)
    assert len(out) == len(s)

@given(st.text(min_size=1), st.integers(min_value=0, max_value=50))
def test_rotation_equivalence(s, d):
    out1 = left_rotate(left_rotate(s, d), d)
    out2 = left_rotate(s, 2*d)
    assert out1 == out2  # rotation composition property

@given(st.text(min_size=1))
def test_full_rotation_identity(s):
    out = left_rotate(s, len(s))
    assert out == s
