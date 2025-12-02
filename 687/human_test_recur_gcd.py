
from hypothesis import given, strategies as st
from bugged_recur_gcd import recur_gcd
import math


@given(st.integers(min_value=1, max_value=1000),
       st.integers(min_value=1, max_value=1000))
def test_divides_both_numbers(a, b):
    """GCD must divide both numbers"""
    result = recur_gcd(a, b)
    assert a % result == 0
    assert b % result == 0


@given(st.integers(min_value=1, max_value=100),
       st.integers(min_value=1, max_value=100))
def test_order_does_not_matter(a, b):
    """GCD(a,b) equals GCD(b,a)"""
    assert recur_gcd(a, b) == recur_gcd(b, a)


@given(st.integers(min_value=1, max_value=100),
       st.integers(min_value=1, max_value=100))
def test_matches_correct_gcd(a, b):
    """Result should match Python's math.gcd"""
    assert recur_gcd(a, b) == math.gcd(a, b)


@given(st.integers(min_value=1, max_value=50),
       st.integers(min_value=2, max_value=10))
def test_gcd_of_multiple(a, k):
    """GCD(a, k*a) should equal a"""
    assert recur_gcd(a, k * a) == a
