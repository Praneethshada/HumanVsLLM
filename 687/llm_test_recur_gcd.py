import pytest
from bugged_recur_gcd import recur_gcd

def test_gcd_basic_numbers():
    assert recur_gcd(10, 5) == 5
    assert recur_gcd(14, 21) == 7
    assert recur_gcd(100, 80) == 20


def test_gcd_one_zero():
    # gcd(a, 0) should be |a|
    assert recur_gcd(12, 0) == 12
    assert recur_gcd(0, 15) == 15


def test_gcd_both_zero():
    # Some definitions return 0 for gcd(0,0)
    assert recur_gcd(0, 0) == 0


def test_gcd_coprime_numbers():
    assert recur_gcd(8, 15) == 1
    assert recur_gcd(35, 64) == 1


def test_gcd_commutativity():
    # gcd(a, b) == gcd(b, a)
    assert recur_gcd(27, 36) == recur_gcd(36, 27)


def test_gcd_large_values():
    assert recur_gcd(123456, 789012) == 12
