#!/usr/bin/python3
import sys

def factorial(n):
    """
    Recursively calculates the factorial of a non-negative integer n.

    Parameters:
    n (int): A non-negative integer whose factorial is to be computed.

    Returns:
    int: The factorial of n.

    Example:
    factorial(5) -> 120
    """
    if n == 0:
        return 1  # Base case: 0! = 1
    else:
        return n * factorial(n - 1)  # Recursive case

# Retrieve the number from command-line arguments
f = factorial(int(sys.argv[1]))

# Print the result
print(f)
