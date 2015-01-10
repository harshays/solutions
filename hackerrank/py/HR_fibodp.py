def fib(lim):
	fib = [0,1]
	while fib[-1] <= lim:
		fib.append(fib[-1]+fib[-2])
		fib.append(fib[-1]+fib[-2])
	return fib[::-1]

T = int(input())
for x in range(T):
	k = int(input())
	if k in fib(k):
		print ('IsFibo')
	else:
		print ('IsNotFibo')

