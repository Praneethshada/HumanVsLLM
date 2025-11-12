import pytest
from buggy_function import binomial_Coeff

def test_basic_values():
    assert binomial_Coeff(5, 2) == 10
    assert binomial_Coeff(4, 3) == 4
    assert binomial_Coeff(3, 2) == 3

def test_large_values():
    assert binomial_Coeff(14, 6) == 3003

def test_zero_case():
    assert binomial_Coeff(5, 0) == 1

def test_n_equals_k_case():
    assert binomial_Coeff(7, 7) == 1

def test_invalid_case():
    # k > n should return 0
    assert binomial_Coeff(3, 5) == 0

def test_small_cases():
    assert binomial_Coeff(2, 1) == 2
    assert binomial_Coeff(1, 0) == 1
