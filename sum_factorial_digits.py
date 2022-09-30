from operator import mod, floordiv

def factorial(n):
    """
    Returns the factorial of n.

    >>> factorial(10)
    3628800
    """
    fact = 1
    for num in range(2, n+1):
        fact = fact * num

    return fact

def sum_digits(n):
    """
    Sum the digits of a number n.

    >>> sum_digits(12345)
    15
    """
    sum = 0
    while n > 0:
        d = mod(n, 10)   
        sum += d             
        n = floordiv(n, 10) 

    return sum


sum_digits(factorial(10))