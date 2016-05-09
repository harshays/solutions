# Highly divisible triangular number
from math import sqrt
def countDivisors(n):
        if n == 1: return 1
        divisors,divs = 2,[1,n]
        for i in range(2, int(sqrt(n)) + 1):
                if n % i == 0:
                        divs.append(i)
                        divs.append(n//i)
        return (len(set(divs)))

count = 1
triangle = 0
while True:
        triangle += count
        if(countDivisors(triangle) > 500):
                print (triangle)
                exit(0)
        count += 1
