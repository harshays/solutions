# summation of primes

def erato_sum(lim):
	primes_sum = 0 
	multiples = set()
	for x in range(2,lim):
		if x not in multiples: primes_sum+=x
		for j in range(x*2,lim,x): multiples.add(j)
	return primes_sum

print (erato_sum(2000000))