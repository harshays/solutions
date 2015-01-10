from collections import defaultdict
from time import time

cache = {}

def collatz(n):
    global cache
    nc, c = n, 1
    while n != 1:
        if n in cache: 
            cache[nc] = cache[n] + c - 1
            return cache[n] + c - 1
        if n % 2 == 0: n = n//2
        else: n = 3*n + 1
        c += 1
    cache[nc] = c
    return c

def collatz_test(n):
    c = 1
    while n != 1:
        if n % 2 == 0: n = n//2
        else: n = 3*n + 1
        c += 1
    return c;

st = time()
maxval = [0,0] # [count, num]
for i in range(2,1000000):
    v = collatz(i)
    if v > maxval[0]: maxval = [v,i]
print maxval
print time()-st