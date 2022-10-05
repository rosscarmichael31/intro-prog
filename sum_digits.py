# Intro to Programming
# Fall 2022
# Exercise 1 - sum of factorial digits


# n!, (pronounced "n factorial") of a positive integer n
# may be computed as n * (n-1) * (n-2) ... * 3 * 2 * 1
# For example, 10! = 10 * 9 * 8 ... * 3 * 2 * 1 = 3628800
#
# The sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27
#
# Please write a function sum_of_factorial_digits(n) which computes the
# sum of factorial digits for arbitrary positive integers n

from operator import mod, floordiv

def factorial(n):
    """
    Returns the factorial of n.

    >>> factorial(10)
    3628800
    """
    assert n > -1, "Enter a positive integer "
    fact = 1
    while n > 1:
        fact *= n
        n -= 1

    return fact

def sum_digits(n):
    """
    Sum the digits of a number n.

    >>> sum_digits(12345)
    15
    """
    sum = 0
    while n > 0:
        sum += mod(n, 10)         
        n = floordiv(n, 10) 

    return sum

if __name__ == "__main__":
    import doctest
    doctest.testmod()
