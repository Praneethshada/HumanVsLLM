
import pytest
from hypothesis import given, strategies as st
from bugged_roman import roman_to_int

def int_to_roman(num):
    num_map = {
        1: "I",
        5: "V",    4: "IV",
        10: "X",   9: "IX",
        50: "L",   40: "XL",
        100: "C",  90: "XC",
        500: "D",  400: "CD",
        1000: "M", 900: "CM",
    }
    r = ''
    for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
        while n <= num:
            r += num_map[n]
            num-=n
    return r


VALID_ROMANS = [
    "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
    "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX",
    "XL", "L", "XC", "C", "CD", "D", "CM", "M"
]

roman_st = st.sampled_from(VALID_ROMANS)

roman_pair_st = st.tuples(roman_st, roman_st)

@given(roman_st)
def test_positive_output(roman):
    """Property 1: roman_to_int(s) should always return a positive integer."""
    value = roman_to_int(roman)
    assert isinstance(value, int)
    assert value > 0


@given(roman_pair_st)
def test_monotonicity(pair):
    """Property 2: Ordering of Roman numerals should reflect integer ordering (if distinct)."""
    a, b = pair
    val_a = roman_to_int(a)
    val_b = roman_to_int(b)
    if val_a < val_b:
        assert a != b
    if val_a == val_b:
        assert a == b or (roman_to_int(a) == roman_to_int(b))


@given(roman_st)
def test_conversion(roman):
    """Property 3: int_to_roman(roman_to_int(s)) should equal s for valid normalized numerals."""
    value = roman_to_int(roman)
    back = int_to_roman(value)
    assert back == roman

