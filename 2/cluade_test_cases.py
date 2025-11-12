import pytest
from buggy_function import min_cost




class TestMinCost:
    """Test suite for min_cost function."""
    
    def test_single_cell_grid(self):
        """Test with a 1x1 grid (starting cell is also the destination)."""
        cost = [[5]]
        assert min_cost(cost, 0, 0) == 5
    
    def test_single_row_grid(self):
        """Test with a 1xN grid (can only move right)."""
        cost = [[1, 2, 3, 4]]
        assert min_cost(cost, 0, 3) == 10  # 1 + 2 + 3 + 4
    
    def test_single_column_grid(self):
        """Test with an Nx1 grid (can only move down)."""
        cost = [[1], [2], [3], [4]]
        assert min_cost(cost, 3, 0) == 10  # 1 + 2 + 3 + 4
    
    def test_2x2_grid_straight_path(self):
        """Test 2x2 grid where straight path is cheaper."""
        cost = [
            [1, 5],
            [5, 1]
        ]
        # Straight paths: right then down = 1+5+1 = 7, down then right = 1+5+1 = 7
        # Diagonal: 1+1 = 2
        assert min_cost(cost, 1, 1) == 2
    
    def test_2x2_grid_diagonal_cheaper(self):
        """Test 2x2 grid where diagonal path is cheaper than straight."""
        cost = [
            [1, 10],
            [10, 1]
        ]
        # Diagonal path: 1 + 1 = 2
        # Right then down: 1 + 10 + 1 = 12
        # Down then right: 1 + 10 + 1 = 12
        assert min_cost(cost, 1, 1) == 2
    
    def test_3x3_grid_diagonal_preferred(self):
        """Test 3x3 grid where diagonal moves are optimal."""
        cost = [
            [1, 100, 100],
            [100, 1, 100],
            [100, 100, 1]
        ]
        # Pure diagonal path: 1 + 1 + 1 = 3
        assert min_cost(cost, 2, 2) == 3
    
    def test_3x3_grid_mixed_path(self):
        cost = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        # One possible optimal path (diagonal): 1 + 5 + 9 = 15
        assert min_cost(cost, 2, 2) == 15
    
    def test_rectangular_grid_wide(self):
        """Test rectangular grid (wider than tall)."""
        cost = [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]
        ]
        # Diagonal (2 moves) + right (2 moves) = 5 cells = 5
        assert min_cost(cost, 2, 4) == 5
    
    def test_rectangular_grid_tall(self):
        """Test rectangular grid (taller than wide)."""
        cost = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        # Diagonal (2 moves) + down (2 moves) = 5 cells = 5
        assert min_cost(cost, 4, 2) == 5
    
    def test_larger_grid_uniform_cost(self):
        """Test larger grid with uniform costs."""
        cost = [[2] * 10 for _ in range(10)]
        # Diagonal moves: 10 moves total = 10 * 2 = 20
        assert min_cost(cost, 9, 9) == 20
    
    def test_larger_grid_varying_costs(self):
        """Test larger grid with varying costs."""
        cost = [
            [1, 5, 5, 5, 5],
            [5, 1, 5, 5, 5],
            [5, 5, 1, 5, 5],
            [5, 5, 5, 1, 5],
            [5, 5, 5, 5, 1]
        ]
        # Pure diagonal: 1 + 1 + 1 + 1 + 1 = 5
        assert min_cost(cost, 4, 4) == 5
    
    def test_destination_not_corner(self):
        """Test with destination that is not the bottom-right corner."""
        cost = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]
        # Path to (1, 2): could be 1 + 6 + 7 or 1 + 2 + 7 or diagonal variations
        assert min_cost(cost, 1, 2) == 10  # 1 + 2 + 7 or 1 + 6 + 7 (both = 10)
    
    def test_high_cost_cells(self):
        """Test with very high cost cells."""
        cost = [
            [1, 1000, 1],
            [1000, 1, 1000],
            [1, 1000, 1]
        ]
        # Optimal: 1 + 1 + 1 (diagonal path)
        assert min_cost(cost, 2, 2) == 3
    
    
    def test_zero_costs(self):
        """Test with zero costs."""
        cost = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        assert min_cost(cost, 2, 2) == 0
    
    
    def test_negative_row_index_raises_indexerror(self):
        """Test that negative row index raises IndexError."""
        cost = [[1, 2], [3, 4]]
        with pytest.raises(IndexError):
            min_cost(cost, -1, 1)
    
    def test_negative_col_index_raises_indexerror(self):
        """Test that negative column index raises IndexError."""
        cost = [[1, 2], [3, 4]]
        with pytest.raises(IndexError):
            min_cost(cost, 1, -1)
    
    def test_both_indices_out_of_bounds(self):
        """Test that both indices out of bounds raises IndexError."""
        cost = [[1, 2], [3, 4]]
        with pytest.raises(IndexError):
            min_cost(cost, 10, 10)
    
    def test_start_position_zero_zero(self):
        """Test that start position is always (0, 0)."""
        cost = [
            [10, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        # Must start at (0,0) with cost 10
        result = min_cost(cost, 2, 2)
        assert result >= 10  # Must include the starting cell
    
    def test_large_grid_performance(self):
        """Test with a larger grid to check performance."""
        size = 50
        cost = [[1] * size for _ in range(size)]
        # Diagonal path: 50 cells
        assert min_cost(cost, size - 1, size - 1) == size