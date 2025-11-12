from hypothesis import given, strategies as st
from nCr_mod_p import nCr_mod_p

@given(st.integers(min_value=1, max_value=20), st.integers(min_value=0, max_value=10), st.integers(min_value=2, max_value=30))
def test_mod_range(n, r, p):
    if r > n: return
    val = nCr_mod_p(n, r, p)
    assert 0 <= val < p

@given(st.integers(min_value=0, max_value=20), st.integers(min_value=0, max_value=20), st.integers(min_value=2, max_value=50))
def test_nCr_properties(n, r, p):
    if r > n: return
    val1 = nCr_mod_p(n, r, p)
    val2 = nCr_mod_p(n, n - r, p)
    assert val1 == val2

@given(st.integers(min_value=0, max_value=20), st.integers(min_value=0, max_value=20), st.integers(min_value=2, max_value=50))
def test_edge_cases(n, r, p):
    if r > n: 
        assert nCr_mod_p(n, r, p) == 0
    elif r == 0 or r == n:
        assert nCr_mod_p(n, r, p) == 1
    else:
        val = nCr_mod_p(n, r, p)
        assert val >= 0

@given(st.integers(min_value=0, max_value=20), st.integers(min_value=0, max_value=20), st.integers(min_value=2, max_value=50))
def test_r_equal_1_or_n_minus_1(n, r, p):
    if n < 1: return
    if r == 1:
        assert nCr_mod_p(n, r, p) == n % p
    elif r == n - 1:
        assert nCr_mod_p(n, r, p) == n % p  
    else:
        val = nCr_mod_p(n, r, p)
        assert val >= 0

@given(st.integers(min_value=0, max_value=20), st.integers(min_value=0, max_value=20), st.integers(min_value=2, max_value=50))
def test_symmetric_property(n, r, p):
    if r > n: return
    val1 = nCr_mod_p(n, r, p)
    val2 = nCr_mod_p(n, n - r, p)
    assert val1 == val2
    
@given(st.integers(min_value=0, max_value=20), st.integers(min_value=0, max_value=20), st.integers(min_value=2, max_value=1000000007))
def test_large_prime_modulus(n, r, p):
    if r > n: return
    val = nCr_mod_p(n, r, p)
    assert 0 <= val < p
    