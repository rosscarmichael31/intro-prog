# 3. Higher order recursive function

def summation(n, func):
    """
    Higher order recursive function to express summation.
    """
    total = 0
    return total if n == 0 else func(n) + summation(n-1, func)
    



def sum_naturals(n):
    """
    >>> sum_naturals(5)
    15
    """
    return summation(n, lambda x: x)

def sum_squares(n):
    """
    >>> sum_squares(5)
    55
    """
    return summation(n, lambda x: x**2)

def sum_cubes(n):
    """
    >>> sum_cubes(5)
    225
    """
    return summation(n, lambda x: x**3)
    