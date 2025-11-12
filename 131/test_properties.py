from hypothesis import given, strategies as st
from buggy import reverse_vowels

V = set("aeiouAEIOU")
def is_vowel(c): return c in V

@given(st.text())
def test_length_preserved(s):
    out = reverse_vowels(s)
    assert len(out) == len(s)

@given(st.text())
def test_non_vowel_positions_unchanged(s):
    out = reverse_vowels(s)
    for i, ch in enumerate(s):
        if not is_vowel(ch):
            assert out[i] == ch

@given(st.text())
def test_double_application_is_identity(s):
    # reversing vowels twice should return the original string
    out = reverse_vowels(reverse_vowels(s))
    assert out == s
