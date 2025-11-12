
import pytest
from bugged_roman import roman_to_int


def test_basic_roman_numerals():
    assert roman_to_int("I") == 1
    assert roman_to_int("V") == 5
    assert roman_to_int("X") == 10
    assert roman_to_int("L") == 50
    assert roman_to_int("C") == 100
    assert roman_to_int("D") == 500
    assert roman_to_int("M") == 1000

def test_repeated_numerals():
    assert roman_to_int("III") == 3
    assert roman_to_int("XX") == 20
    assert roman_to_int("CC") == 200
    assert roman_to_int("MMM") == 3000

def test_mixed_cases():
    assert roman_to_int("XIV") == 14
    assert roman_to_int("XXIX") == 29
    assert roman_to_int("LXXIX") == 79

def test_complex_numerals():
    assert roman_to_int("CCLXXXIX") == 289
    assert roman_to_int("MCMXCIV") == 1994
    assert roman_to_int("MMVIII") == 2008

def test_maximum_value():
    assert roman_to_int("MMMCMXCIX") == 3999  # Maximum standard Roman numeral
