import pytest
from buggy import left_rotate

def test_basic_examples():
    assert left_rotate("python", 2) == "thonpy"
    assert left_rotate("bigdata", 3) == "databig"
    assert left_rotate("hadoop", 1) == "adooph"

def test_extra_cases():
    assert left_rotate("abc", 0) == "abc"
    assert left_rotate("abc", 3) == "abc"
    assert left_rotate("abc", 5) == "cab"  # same as rotating by 2
    assert left_rotate("", 5) == ""
