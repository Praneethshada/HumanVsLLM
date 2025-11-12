from hypothesis import given, strategies as st
from chinese_zodiac import chinese_zodiac

@given(st.integers(min_value=1900, max_value=2100))
def test_valid_sign(year):
    valid = {'Dragon','Snake','Horse','Sheep','Monkey','Rooster','Dog','Pig','Rat','Ox','Tiger','Hare'}
    assert chinese_zodiac(year) in valid

@given(st.integers(min_value=1900, max_value=2100))
def test_cycle_length(year):
    sign_current = chinese_zodiac(year)
    sign_next_cycle = chinese_zodiac(year + 12)
    assert sign_current == sign_next_cycle

