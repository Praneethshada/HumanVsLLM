
import pytest
from buggy_function import binomial_Coeff




class TestBinomialCoeff:
    """Test cases for binomial_Coeff function"""
    
    # Basic/Edge Cases
    def test_choose_zero(self):
        """C(n, 0) should always equal 1"""
        assert binomial_Coeff(0, 0) == 1
        assert binomial_Coeff(5, 0) == 1
        assert binomial_Coeff(100, 0) == 1
    
    def test_choose_self(self):
        """C(n, n) should always equal 1"""
        assert binomial_Coeff(1, 1) == 1
        assert binomial_Coeff(5, 5) == 1
        assert binomial_Coeff(10, 10) == 1
    
    def test_choose_one(self):
        """C(n, 1) should equal n"""
        assert binomial_Coeff(1, 1) == 1
        assert binomial_Coeff(5, 1) == 5
        assert binomial_Coeff(10, 1) == 10
        assert binomial_Coeff(100, 1) == 100
    
    def test_choose_n_minus_one(self):
        """C(n, n-1) should equal n"""
        assert binomial_Coeff(5, 4) == 5
        assert binomial_Coeff(10, 9) == 10
        assert binomial_Coeff(20, 19) == 20
    
    # Small value tests
    def test_small_values(self):
        """Test known small binomial coefficients"""
        assert binomial_Coeff(2, 1) == 2
        assert binomial_Coeff(3, 1) == 3
        assert binomial_Coeff(3, 2) == 3
        assert binomial_Coeff(4, 2) == 6
        assert binomial_Coeff(5, 2) == 10
        assert binomial_Coeff(5, 3) == 10
    
    # Pascal's triangle values
    def test_pascals_triangle(self):
        """Test values from Pascal's triangle"""
        # Row 6: 1, 6, 15, 20, 15, 6, 1
        assert binomial_Coeff(6, 0) == 1
        assert binomial_Coeff(6, 1) == 6
        assert binomial_Coeff(6, 2) == 15
        assert binomial_Coeff(6, 3) == 20
        assert binomial_Coeff(6, 4) == 15
        assert binomial_Coeff(6, 5) == 6
        assert binomial_Coeff(6, 6) == 1
    
    def test_larger_values(self):
        """Test larger binomial coefficients"""
        assert binomial_Coeff(10, 5) == 252
        assert binomial_Coeff(20, 10) == 184756
        assert binomial_Coeff(15, 7) == 6435
        assert binomial_Coeff(12, 4) == 495
    
    # Symmetry property: C(n, k) = C(n, n-k)
    def test_symmetry_property(self):
        """C(n, k) should equal C(n, n-k)"""
        assert binomial_Coeff(10, 3) == binomial_Coeff(10, 7)
        assert binomial_Coeff(15, 5) == binomial_Coeff(15, 10)
        assert binomial_Coeff(20, 8) == binomial_Coeff(20, 12)
    
    # Pascal's identity: C(n, k) = C(n-1, k-1) + C(n-1, k)
    def test_pascals_identity(self):
        """Test Pascal's identity"""
        n, k = 10, 4
        assert binomial_Coeff(n, k) == binomial_Coeff(n-1, k-1) + binomial_Coeff(n-1, k)
        
        n, k = 15, 7
        assert binomial_Coeff(n, k) == binomial_Coeff(n-1, k-1) + binomial_Coeff(n-1, k)
    
    # Invalid input cases
    def test_k_greater_than_n(self):
        """C(n, k) should be 0 when k > n"""
        assert binomial_Coeff(5, 6) == 0
        assert binomial_Coeff(10, 15) == 0
    
    def test_negative_k(self):
        """C(n, k) should be 0 when k < 0"""
        assert binomial_Coeff(5, -1) == 0
        assert binomial_Coeff(10, -5) == 0
    
    def test_negative_n_positive_k(self):
        """Test behavior with negative n and positive k"""
        # This depends on implementation - may raise error or return 0
        # Adjust based on expected behavior
        with pytest.raises((ValueError, TypeError)):
            binomial_Coeff(-5, 2)
    
    # Stress tests
    def test_large_n_small_k(self):
        """Test large n with small k"""
        assert binomial_Coeff(100, 2) == 4950
        assert binomial_Coeff(50, 3) == 19600
    
    def test_moderate_values(self):
        """Test moderate n and k values"""
        assert binomial_Coeff(30, 15) == 155117520
        assert binomial_Coeff(25, 12) == 5200300
    
    # Type testing
    def test_return_type(self):
        """Result should be an integer"""
        result = binomial_Coeff(10, 5)
        assert isinstance(result, int)
    
    # Special mathematical properties
    def test_sum_of_row(self):
        """Sum of row n in Pascal's triangle equals 2^n"""
        n = 5
        row_sum = sum(binomial_Coeff(n, k) for k in range(n + 1))
        assert row_sum == 2**n
        
        n = 10
        row_sum = sum(binomial_Coeff(n, k) for k in range(n + 1))
        assert row_sum == 2**n


# Additional parametrized tests
@pytest.mark.parametrize("n,k,expected", [
    (0, 0, 1),
    (1, 0, 1),
    (1, 1, 1),
    (4, 0, 1),
    (4, 1, 4),
    (4, 2, 6),
    (4, 3, 4),
    (4, 4, 1),
    (7, 3, 35),
    (8, 4, 70),
    (13, 5, 1287),
])
def test_binomial_parametrized(n, k, expected):
    """Parametrized test for various known values"""
    assert binomial_Coeff(n, k) == expected


if __name__ == "__main__":
    pytest.main([__file__, "-v"])