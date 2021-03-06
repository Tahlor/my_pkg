"""Sample code of two simple functions to illustrate python package setup and test-driven development."""

# First code written for python package test.
def square(x):
    """Finds the square of the input.
    
    Args:
        x (float): The number to be squared.
    Returns:
        x2 (float): The squared number.
    """

    return x**2

# Second code written for test-driven development workflow.
def factorial(n):
    """Factorial calculates the factorial of the provided integer.
    Args:
        n (int): The value that the factorial will be computed from. 
    Returns:
        fact (int): The factorial of n. 
    Raises:
        ValueError: If n is not a non-negative integer.
    """

    if n < 0:
        raise ValueError("The input to factorial must be a non-negative integer.")

    if not isinstance(n,int):
        if int(n)==n:
            n = int(n)
        else:
            raise ValueError("The input to factorial must be a non-negative integer.")

    fact = 1
    for i in range(1,n+1):
        fact = i*fact

    return fact
