def sum_cubes(start, finish):
    """
    >>> sum_cubes(1, 4)
    100
    """
    total = 0
    counter = start
    while counter <= finish:
        total += pow(counter, 3)
        counter+=1

    return total