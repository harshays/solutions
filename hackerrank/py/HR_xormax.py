#!/usr/bin/python3

def maxXor(l, r):
    max_val = -1
    for i in range(l, r+1):
        for j in range(l, r+1):
            cur_val = i ^ j
            if max_val < cur_val:
                max_val = cur_val
    return (max_val)
  

l = int(input())
r = int(input())
print (maxXor(l, r))