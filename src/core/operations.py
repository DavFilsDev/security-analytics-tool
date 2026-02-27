from .exceptions import DivisionByZeroError
from .validators import validate_numbers

def add(a: float, b: float) -> float:
    """
    Addition operation (A1)
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Sum of a and b
    
    Examples:
        >>> add(2, 3)
        5
        >>> add(-1, 1)
        0
    """
    validate_numbers(a, b)
    return a + b

def subtract(a: float, b: float) -> float:
    """
    Subtraction operation (A2)
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Difference of a and b (a - b)
    
    Examples:
        >>> subtract(5, 3)
        2
        >>> subtract(1, 5)
        -4
    """
    validate_numbers(a, b)
    return a - b

def multiply(a: float, b: float) -> float:
    """
    Multiplication operation (A3)
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Product of a and b
    
    Examples:
        >>> multiply(4, 3)
        12
        >>> multiply(2.5, 2)
        5.0
    """
    validate_numbers(a, b)
    return a * b

def divide(a: float, b: float) -> float:
    """
    Division operation (A4)
    
    Args:
        a: First number (dividend)
        b: Second number (divisor)
    
    Returns:
        Quotient of a divided by b
    
    Raises:
        DivisionByZeroError: If b is zero
    
    Examples:
        >>> divide(10, 2)
        5.0
        >>> divide(7, 2)
        3.5
    """
    validate_numbers(a, b)
    
    if b == 0:
        raise DivisionByZeroError("Cannot divide by zero")
    
    return a / b

if __name__ == "__main__":
    print("// Calculator Operations Demo")
    print(f"Add 2 + 3 = {add(2, 3)}")
    print(f"Subtract 5 - 3 = {subtract(5, 3)}")
    print(f"Multiply 4 * 3 = {multiply(4, 3)}")
    print(f"Divide 10 / 2 = {divide(10, 2)}")
    
    try:
        divide(5, 0)
    except DivisionByZeroError as e:
        print(f"Error caught: {e}")