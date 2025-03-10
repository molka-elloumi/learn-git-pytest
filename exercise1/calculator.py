# Exercise 1: Basic Calculator Functions
from typing import Union

# Defining a Number type for cleaner type hints
Number = Union[int, float]


def add(a: Number, b: Number)-> Number:
   """
    Return the sum of a and b.

    Args:
        a: First number
        b: Second number

    Returns:
        The sum of a and b
    """
   return a + b


def subtract(a: Number, b: Number)-> Number :
   """
    Return the result of subtracting b from a.

    Args:
        a: First number
        b: Second number

    Returns:
        The result of a - b
    """
   return a - b


def multiply(a: Number, b: Number)-> Number :
    """
    Return the product of a and b.

    Args:
        a: First number
        b: Second number

    Returns:
        The product of a and b
    """
    return a * b

def divide(a: Number, b: Number) -> Number:
    """
    Return the result of dividing a by b.

    Args:
        a: First number (dividend)
        b: Second number (divisor)

    Returns:
        The result of a / b

    Raises:
        ValueError: If b is 0
    """
    if b == 0:
        raise ValueError("Cannot be divided by zero")
    return a / b
#tests
#apoint two random numbers
A = 22
B = 3.14
#start testing the functions
C = add (A,B)
print ("testing for addition",C)
D=subtract(A,B)
print("testing for substract",D)
E=multiply(A,B)
print("testing for multiply",E)
F=divide(A,B)
print("testing for division",F)
#testing all possible cases 
G=0
H=divide(A,G)
print ("testing for 0",H)