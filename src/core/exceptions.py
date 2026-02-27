"""
Custom exceptions for calculator operations.
"""

class CalculationError(Exception):
    """Base exception for all calculation errors."""
    pass

class DivisionByZeroError(CalculationError):
    """Raised when attempting to divide by zero."""
    pass

class InvalidInputError(CalculationError):
    """Raised when input validation fails."""
    pass

class OverflowError(CalculationError):
    """Raised when calculation results in overflow."""
    pass