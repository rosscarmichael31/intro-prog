from collections.abc import Iterable

def flatten(L):
    """
    Flatten a an arbritarily deep list using recursion.

    >>> flatten([1, 2, [3, 4, [5]], 6])
    [1, 2, 3, 4, 5, 6]
    """
    if L == []:
        return L

    if isinstance(L[0], Iterable):
        return flatten(L[0]) + flatten(L[1:])
    
    return L[:1] + flatten(L[1:])