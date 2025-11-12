
import pytest
from bugged_remove_digits import remove

def test_basic_strings():
    # removes digits from mixed strings
    assert remove(["abc123", "45de6", "7f8g9"]) == ["abc", "de", "fg"]

def test_no_digits():
    # strings without digits should remain unchanged
    assert remove(["hello", "world"]) == ["hello", "world"]

def test_all_digits():
    # strings with only digits become empty
    assert remove(["123", "456", "7890"]) == ["", "", ""]

def test_empty_strings():
    # empty strings stay empty
    assert remove(["", "abc", ""]) == ["", "abc", ""]

def test_mixed_case_and_special_chars():
    # digits are removed, other chars remain
    assert remove(["A1b2C3!", "99hello!!", "Te5st"]) == ["AbC!", "hello!!", "Test"]

def test_strings_with_spaces():
    # spaces should be preserved and order of non-digit chars retained
    assert remove(["12 a3b 45", "6c d7"]) == [" ab ", "c d"]

def test_unicode_characters():
    # digits should be removed even when string has emojis or unicode letters
    assert remove(["hi123😊", "🚀4space5"]) == ["hi😊", "🚀space"]

def test_single_string_in_list():
    # works for single element list
    assert remove(["abc123xyz"]) == ["abcxyz"]

def test_empty_list():
    # empty input list should return empty list
    assert remove([]) == []

def test_numbers_embedded_with_letters():
    # removes digits from middle, start, and end
    assert remove(["1a2b3c4d", "9end", "start8", "mid7dle"]) == ["abcd", "end", "start", "middle"]
