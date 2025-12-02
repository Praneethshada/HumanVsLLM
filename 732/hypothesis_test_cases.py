import re
from hypothesis import given, strategies as st
from buggy_function import replace_specialchar

@given(st.text())
def test_no_forbidden_characters_left(s):
    result = replace_specialchar(s)
    assert not any(c in result for c in [' ', ',', '.'])

@given(st.text())
def test_replacement_counts(s):
    expected = re.sub("[ ,.]", ":", s)
    assert replace_specialchar(s).count(":") == expected.count(":")
