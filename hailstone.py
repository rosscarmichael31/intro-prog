def hailstone(n):
    if n % 2 ==0:
        return n // 2
    else:
        return 3 * n +1

def hailstone_count(n):
    count = 0 
    while n != 1:
        n = hailstone(n)
        count+=1
    return count

def hailstone_driver(start, finish):
    n = start

    while n <= finish:
        count = hailstone_count(n)
        print(n, count)
        n+=1