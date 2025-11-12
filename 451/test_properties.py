import re
from hypothesis import given, strategies as st
from buggy import remove_whitespaces

# Any whitespace character (space, tab, newline, etc.) should disappear
@given(st.text())
def test_no_whitespace_in_output(s):
    out = remove_whitespaces(s)
    # Property: the output must contain no whitespace
    assert not re.search(r"\s", out)

@given(st.text())
def test_length_never_greater(s):
    # Property: removing whitespace can never make string longer
    out = remove_whitespaces(s)
    assert len(out) <= len(s)
