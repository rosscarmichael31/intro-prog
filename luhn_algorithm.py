def split(n):
    """
    Strip the last digit off a number and return both

    >>> split(12345)
    (5, 1234)
    """
    return n % 10, n // 10


def luhn(n):
    ...