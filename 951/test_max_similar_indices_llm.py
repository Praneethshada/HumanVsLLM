import pytest
from max_similar_indices import max_similar_indices

def test_basic_case():
    """Test basic case with same length lists and tuples"""
    list1 = [(1, 2), (3, 4), (5, 6)]
    list2 = [(2, 1), (1, 5), (4, 7)]
    expected = [(2, 2), (3, 5), (5, 7)]
    assert max_similar_indices(list1, list2) == expected

def test_single_element_tuples():
    """Test with single element tuples"""
    list1 = [(1,), (2,), (3,)]
    list2 = [(4,), (1,), (2,)]
    expected = [(4,), (2,), (3,)]
    assert max_similar_indices(list1, list2) == expected

def test_three_element_tuples():
    """Test with three element tuples"""
    list1 = [(1, 2, 3), (4, 5, 6)]
    list2 = [(3, 2, 1), (1, 6, 5)]
    expected = [(3, 2, 3), (4, 6, 6)]
    assert max_similar_indices(list1, list2) == expected

def test_different_length_lists():
    """Test when lists have different lengths"""
    list1 = [(1, 2), (3, 4), (5, 6)]
    list2 = [(2, 1), (1, 5)]  # Shorter list
    expected = [(2, 2), (3, 5)]
    assert max_similar_indices(list1, list2) == expected

def test_negative_numbers():
    """Test with negative numbers"""
    list1 = [(-1, -2), (-3, -4)]
    list2 = [(-2, -1), (-1, -5)]
    expected = [(-1, -1), (-1, -4)]
    assert max_similar_indices(list1, list2) == expected

def test_float_numbers():
    """Test with floating point numbers"""
    list1 = [(1.5, 2.7), (3.1, 4.9)]
    list2 = [(2.1, 1.8), (1.2, 5.1)]
    expected = [(2.1, 2.7), (3.1, 5.1)]
    assert max_similar_indices(list1, list2) == expected

def test_mixed_numbers():
    """Test with mixed integer and float numbers"""
    list1 = [(1, 2.5), (3.7, 4)]
    list2 = [(2.1, 2), (3, 4.5)]
    expected = [(2.1, 2.5), (3.7, 4.5)]
    assert max_similar_indices(list1, list2) == expected

def test_empty_lists():
    """Test with empty lists"""
    assert max_similar_indices([], []) == []
    assert max_similar_indices([(1, 2)], []) == []
    assert max_similar_indices([], [(1, 2)]) == []

def test_single_tuple_lists():
    """Test with single tuple in each list"""
    list1 = [(10, 20, 30)]
    list2 = [(5, 25, 15)]
    expected = [(10, 25, 30)]
    assert max_similar_indices(list1, list2) == expected

def test_identical_tuples():
    """Test when tuples are identical"""
    list1 = [(1, 2), (3, 4)]
    list2 = [(1, 2), (3, 4)]
    expected = [(1, 2), (3, 4)]
    assert max_similar_indices(list1, list2) == expected
