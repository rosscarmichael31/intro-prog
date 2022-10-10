from math import sqrt

def distance(route):
    """
    Compute the distance travelled along an arbritary list of 
    coordinate tuples, starting from the first and visting
    each one sequentially.

    >>> distance([(1,0), (1,1), (2,1)])
    2.0
    """
    distance = 0
    previous = route[0]

    for coord in route[1:]:
        distance += sqrt((coord[0]-previous[0])**2 + (coord[1]-previous[1])**2)
        previous = coord

    return distance 

route = [(1,0), (1,1), (2,1)]