#!/usr/bin/py
# Head ends here
def lonelyinteger(b):
	b = sorted(b)
    if len(b) == 1: return b[0]
	for i in range(1,b):
		if b[i+1] != b[i]: 
			answer = b[i+1]
	return answer
# Tail starts here
if __name__ == '__main__':
    a = int(input())
    b = map(int, input().strip().split(" "))
    print(lonelyinteger(b))
