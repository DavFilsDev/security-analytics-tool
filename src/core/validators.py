from .exceptions import CalculationError

def validate_numbers(*args: float) -> bool:
    """
    Validate that all inputs are numbers.
    
    Args:
        *args: Variable number of arguments to validate
    
    Returns:
        True if all arguments are valid numbers
    
    Raises:
        CalculationError: If any argument is not a number
    
    Examples:
        >>> validate_numbers(1, 2.5, 3)
        True
        >>> validate_numbers(1, "2")  # Raises CalculationError
    """
    for i, arg in enumerate(args):
        if not isinstance(arg, (int, float)):
            raise CalculationError(
                f"Argument at position {i} must be a number, got {type(arg).__name__}"
            )
    return True

def validate_positive(*args: float) -> bool:
    """
    Validate that all numbers are positive.
    
    Args:
        *args: Variable number of arguments to validate
    
    Returns:
        True if all arguments are positive
    
    Raises:
        CalculationError: If any argument is not positive
    """
    validate_numbers(*args)
    
    for i, arg in enumerate(args):
        if arg <= 0:
            raise CalculationError(
                f"Argument at position {i} must be positive, got {arg}"
            )
    return True

def validate_integer(*args: float) -> bool:
    """
    Validate that all numbers are integers.
    
    Args:
        *args: Variable number of arguments to validate
    
    Returns:
        True if all arguments are integers
    
    Raises:
        CalculationError: If any argument is not an integer
    """
    validate_numbers(*args)
    
    for i, arg in enumerate(args):
        if not isinstance(arg, int) or isinstance(arg, bool):
            raise CalculationError(
                f"Argument at position {i} must be an integer, got {type(arg).__name__}"
            )
    return True