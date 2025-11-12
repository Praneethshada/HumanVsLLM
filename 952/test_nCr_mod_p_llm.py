import pytest
import math
from nCr_mod_p import nCr_mod_p

def test_llm_case_1():
    assert nCr_mod_p(10, 2, 13) == 6

def test_llm_case_2():
    assert nCr_mod_p(11, 3, 14) == 11

def test_llm_case_3():
    assert nCr_mod_p(18, 14, 19) == 1

def test_basic_combinations():
    """Test basic combination calculations"""
    # 5C2 = 10
    assert nCr_mod_p(5, 2, 1000000007) == 10
    # 7C3 = 35
    assert nCr_mod_p(7, 3, 1000000007) == 35
    # 10C5 = 252
    assert nCr_mod_p(10, 5, 1000000007) == 252

def test_edge_cases():
    """Test edge cases"""
    # nC0 = 1
    assert nCr_mod_p(5, 0, 1000000007) == 1
    # nCn = 1
    assert nCr_mod_p(5, 5, 1000000007) == 1
    # r > n should return 0
    assert nCr_mod_p(5, 6, 1000000007) == 0
    # r < 0 should return 0
    assert nCr_mod_p(5, -1, 1000000007) == 0

def test_small_prime_modulus():
    """Test with small prime modulus"""
    # 5C2 mod 7 = 10 mod 7 = 3
    assert nCr_mod_p(5, 2, 7) == 3
    # 7C3 mod 5 = 35 mod 5 = 0
    assert nCr_mod_p(7, 3, 5) == 0
    # 10C5 mod 11 = 252 mod 11 = 10
    assert nCr_mod_p(10, 5, 11) == 10

def test_large_prime_modulus():
    """Test with large prime modulus (common in competitive programming)"""
    p = 1000000007
    # 1000C500 mod p
    result = nCr_mod_p(1000, 500, p)
    assert 0 <= result < p
    # Verify it's correct by comparing with math.comb for small values
    assert nCr_mod_p(20, 10, p) == math.comb(20, 10) % p

def test_r_equal_1_or_n_minus_1():
    """Test cases where r = 1 or r = n-1"""
    # nC1 = n
    assert nCr_mod_p(10, 1, 1000000007) == 10
    # nC(n-1) = n
    assert nCr_mod_p(10, 9, 1000000007) == 10
    # With modulus
    assert nCr_mod_p(100, 1, 7) == 100 % 7
    assert nCr_mod_p(100, 99, 7) == 100 % 7

def test_symmetric_property():
    """Test that nCr = nC(n-r)"""
    n, p = 15, 1000000007
    for r in range(n + 1):
        assert nCr_mod_p(n, r, p) == nCr_mod_p(n, n - r, p)

def test_pascals_triangle_identity():
    """Test Pascal's triangle identity: nCr = (n-1)C(r-1) + (n-1)Cr"""
    n, p = 10, 1000000007
    for r in range(1, n):
        left = nCr_mod_p(n, r, p)
        right = (nCr_mod_p(n - 1, r - 1, p) + nCr_mod_p(n - 1, r, p)) % p
        assert left == right

def test_zero_and_small_values():
    """Test with zero and very small values"""
    # 0C0 = 1
    assert nCr_mod_p(0, 0, 1000000007) == 1
    # 1C0 = 1, 1C1 = 1
    assert nCr_mod_p(1, 0, 1000000007) == 1
    assert nCr_mod_p(1, 1, 1000000007) == 1
    # 2C1 = 2
    assert nCr_mod_p(2, 1, 1000000007) == 2

