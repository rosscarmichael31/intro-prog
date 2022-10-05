def heron_sqrt(x, guess=1, eps=0.000001):
    """
    Heron's method for calculating the square root.
    [Recursive version]
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

    
    if close_enough(x, guess, eps):
        return guess
    else:
        guess = average(x, guess)
        return heron_sqrt(x, guess) 

