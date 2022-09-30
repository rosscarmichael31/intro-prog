def heron_square(x, eps=0.000001):
    """
    Heron's method for calculating the square root.

    >>> heron_square(25)
    5.000000000053722 
    """  
    g = 1
    
    while not close_enough(x, g, eps):
        g = average(x, g)
    return g

def close_enough(x, g, eps):
    """
    Determine if the square of the guess is close enough
    to the original input.

    >>> close_enough(25, 5.000000000053722, 0.000001)
    True
    """
    return True if abs(g*g-x) < eps else False

def average(x, g):
    """
    Find the average of the input x and x/g.

    >>> average(25, 5.000000000053722)
    5.0
    """
    return 0.5 * (g + x/g)