from itertools import *

def check(no):
	primes = [2,3,5,7,11,13,17]
	for x in range(3,len(no)):
		prod = int((no[x-2])+(no[x-1])+(no[x]))
		if prod % (primes[x-3]) != 0: return False
	return True

a = ['0','1','2','3','4','5','6','7','8','9']
print (sum(list(map(int,([ ''.join(x) for x in permutations(a) if x[0] != '0' and check(x)])))))

