import pytest
from buggy import reverse_vowels

def test_examples():
    assert reverse_vowels("Python") == "Python"
    assert reverse_vowels("USA") == "ASU"      # should FAIL with our bug
    assert reverse_vowels("ab") == "ab"

def test_more_edges():
    assert reverse_vowels("") == ""
    assert reverse_vowels("a") == "a"
    assert reverse_vowels("ae") == "ea"
    assert reverse_vowels("HELLO") == "HOLLE"  # should FAIL with our bug
