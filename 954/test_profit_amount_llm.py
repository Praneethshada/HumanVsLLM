import pytest
from profit_amount import profit_amount

# this test case will fail due to the introduced bug
# as this shows the positive profit but the bug i have introduced it will be loss   
def test_llm_case_1():
    assert profit_amount(1500,1200)==300

def test_llm_case_2():
    assert profit_amount(100,200)==None

def test_llm_case_3():
    assert profit_amount(2000,5000)==None

# Test Case 1: Basic profit scenario
def test_basic_profit():
    """Test when sale amount is greater than actual cost"""
    assert profit_amount(100, 150) == 50
    assert profit_amount(50, 75) == 25
    assert profit_amount(200, 250) == 50

# Test Case 2: No profit (break-even)
def test_no_profit_break_even():
    """Test when sale amount equals actual cost"""
    assert profit_amount(100, 100) is None
    assert profit_amount(50.5, 50.5) is None
    assert profit_amount(0, 0) is None

# Test Case 3: Loss scenario
def test_loss_scenario():
    """Test when sale amount is less than actual cost"""
    assert profit_amount(150, 100) is None
    assert profit_amount(75, 50) is None
    assert profit_amount(250, 200) is None

# Test Case 4: Decimal values
def test_decimal_values():
    """Test with decimal/fractional amounts"""
    assert profit_amount(10.5, 15.75) == 5.25
    assert profit_amount(7.25, 7.50) == 0.25
    assert profit_amount(99.99, 100.01) == 0.02

# Test Case 5: Edge cases
def test_edge_cases():
    """Test edge cases and boundaries"""
    assert profit_amount(0, 10) == 10  # Free item sold for profit
    assert profit_amount(10, 10.01) == 0.01  # Very small profit
    assert profit_amount(-10, 5) == 15  # Negative cost
    assert profit_amount(-20, -10) == 10  # Both negative

# Test Case 6: Integer and float mixed
def test_mixed_types():
    """Test with mixed integer and float inputs"""
    assert profit_amount(100, 150.5) == 50.5
    assert profit_amount(75.25, 100) == 24.75
    assert profit_amount(50.0, 75.0) == 25.0

# Test Case 7: Large numbers
def test_large_numbers():
    """Test with large numerical values"""
    assert profit_amount(1000000, 1500000) == 500000
    assert profit_amount(500.75, 1000.25) == 499.5
    assert profit_amount(0.01, 100.01) == 100.0

# Test Case 8: Zero and negative scenarios
def test_zero_negative():
    """Test zero and negative value scenarios"""
    assert profit_amount(0, 0) is None
    assert profit_amount(10, 0) is None
    assert profit_amount(-5, 0) == 5
    assert profit_amount(-10, -5) == 5

# Test Case 9: Rounding/precision scenarios
def test_precision_scenarios():
    """Test scenarios that might involve precision issues"""
    assert profit_amount(1.1, 2.2) == 1.1
    assert profit_amount(0.333, 0.666) == 0.333
    assert profit_amount(100.001, 100.002) == 0.001

# Test Case 10: Business logic scenarios
def test_business_scenarios():
    """Test realistic business scenarios"""
    # Retail scenario
    assert profit_amount(20, 35) == 15
    # Restaurant food cost
    assert profit_amount(3.50, 12.99) == 9.49
    # Real estate
    assert profit_amount(200000, 250000) == 50000