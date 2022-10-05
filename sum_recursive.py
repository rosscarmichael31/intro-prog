# Sum natural numbers up to n --> sum_n(10) = 10+9+8...+1

def summation(n):
    """
    Sum the natural numbers up to n.

    >>> summation(10)
    55
    >>> summation(0)
    0
    >>> summation(25)
    325
    """
    total = 0
    return total if n == 0 else n + summation(n-1)

if __name__ == "__main__":
    import doctest
    doctest.testmod()