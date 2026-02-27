"""
Unit tests for core calculator operations.
"""

import pytest
from src.core.operations import add, subtract, multiply, divide
from src.core.exceptions import DivisionByZeroError, CalculationError

class TestCalculatorOperations:
    """Test suite for basic arithmetic operations."""
    
    # Addition Tests
    def test_add_positive_numbers(self):
        """Test addition with positive numbers."""
        assert add(2, 3) == 5
        assert add(10.5, 0.5) == 11.0
    
    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        assert add(-2, -3) == -5
        assert add(-5, 3) == -2
    
    def test_add_with_zero(self):
        """Test addition with zero."""
        assert add(0, 5) == 5
        assert add(5, 0) == 5
        assert add(0, 0) == 0
    
    # Subtraction Tests
    def test_subtract_positive_numbers(self):
        """Test subtraction with positive numbers."""
        assert subtract(5, 3) == 2
        assert subtract(10.5, 0.5) == 10.0
    
    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        assert subtract(-2, -3) == 1
        assert subtract(-5, 3) == -8
    
    def test_subtract_with_zero(self):
        """Test subtraction with zero."""
        assert subtract(5, 0) == 5
        assert subtract(0, 5) == -5
        assert subtract(0, 0) == 0
    
    # Multiplication Tests
    def test_multiply_positive_numbers(self):
        """Test multiplication with positive numbers."""
        assert multiply(4, 3) == 12
        assert multiply(2.5, 2) == 5.0
    
    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        assert multiply(-4, 3) == -12
        assert multiply(-2, -3) == 6
    
    def test_multiply_with_zero(self):
        """Test multiplication with zero."""
        assert multiply(5, 0) == 0
        assert multiply(0, 5) == 0
        assert multiply(0, 0) == 0
    
    # Division Tests
    def test_divide_positive_numbers(self):
        """Test division with positive numbers."""
        assert divide(10, 2) == 5.0
        assert divide(7, 2) == 3.5
    
    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        assert divide(-10, 2) == -5.0
        assert divide(-10, -2) == 5.0
    
    def test_divide_by_zero(self):
        """Test division by zero raises appropriate exception."""
        with pytest.raises(DivisionByZeroError) as exc_info:
            divide(5, 0)
        assert "Cannot divide by zero" in str(exc_info.value)
    
    def test_divide_result_types(self):
        """Test division returns float even with integer inputs."""
        result = divide(4, 2)
        assert isinstance(result, float)
        assert result == 2.0
    
    # Input Validation Tests
    def test_invalid_input_types(self):
        """Test that non-numeric inputs raise CalculationError."""
        with pytest.raises(CalculationError):
            add("2", 3)  # String input
        
        with pytest.raises(CalculationError):
            subtract(5, None)  # None input
        
        with pytest.raises(CalculationError):
            multiply([1, 2], 3)  # List input

# Run tests with: pytest tests/test_operations.py -v