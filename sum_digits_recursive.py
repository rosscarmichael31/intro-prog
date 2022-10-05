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

def split(n):
    """
    Strip the last digit off a number and return both

    >>> split(12345)
    (5, 1234)
    """
    return n % 10, n // 10

def fact(n):
    """
    Returns the factorial of n.

    >>> fact(10)
    3628800
    """
    return 1 if n == 0 else n * fact(n-1)

def sum_digits(n, sum=0):
    """
    Sum the digits of a number n.

    >>> sum_digits(12345)
    15
    """

    if n == 0: 
        return sum
    else:
        last_digit, n = split(n)
        return sum_digits(n, sum + last_digit)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
