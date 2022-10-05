def heron_sqrt(x, eps=0.000001):
    """
    Heron's method for calculating the square root.
    [Iterative version]
    """  
    def close_enough(x, guess, eps):
        """
        Determine if the square of the guess is close enough
        to the original input.
        """
        return abs(guess * guess - x) < eps

    def average(x, guess):
        """
        Find the average of the input x and x/g.
        """
        return 0.5 * (guess + x/guess)

    guess = 1
    
    while not close_enough(x, guess, eps):
        guess = average(x, guess)
    return guess

