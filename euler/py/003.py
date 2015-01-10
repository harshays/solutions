# largest prime factor

def factors(n):
	factors,d = [],2
	while n > 1:
		while n % d == 0:
			factors.append(d)
			n //= d 
		d+=1
		if d*d > n: # if a*b = n, min(a,b) <= sqrt(n) always.
			factors.append(n)
			break
	return factors[-1]

print (factors(600851475143))
