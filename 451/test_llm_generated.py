import pytest
from buggy import remove_whitespaces

def test_basic_examples():
    assert remove_whitespaces(" Google    Flutter ") == "GoogleFlutter"
    assert remove_whitespaces(" Google    Dart ") == "GoogleDart"
    assert remove_whitespaces(" iOS    Swift ") == "iOSSwift"

def test_hidden_cases():
    # tabs/newlines should also count as whitespace
    assert remove_whitespaces("Hello\tWorld") == "HelloWorld"
    assert remove_whitespaces("A\nB") == "AB"
    assert remove_whitespaces("  Mix \t of \n spaces ") == "Mixofspaces"
