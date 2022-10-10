def summation(L):
    """
    >>> summation([[1, 2, 3], 4, 5, [[1], [2, [3, 4]]]])
    25
    >>> summation([[[[[1], 2], 3], 4], 5])
    15
    """
    if type(L) != list:
        return L
        
    if L == []:
        return 0
    
    return summation(L[0]) + summation(L[1:])


l = [1, 2, 3, 4, 5, 1, 2, 3, 4]
l1 = [[1, 2, 3], 4, 5, [[1], [2, [3, 4]]]]
summation([[[[[1], 2], 3], 4], 5])

assert summation(l) == summation(l1), "Reccursive sum failed!" 