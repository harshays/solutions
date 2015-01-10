# combinatoric selections

factorial_cache = {0:1}
for x in range(1,101): factorial_cache[x] = factorial_cache[x-1]*x

def ncr(n,r): return factorial_cache[n]//(factorial_cache[r]*factorial_cache[n-r])

mil,values = 10**6, []
for n in range(23,101):
	for r in range(1,n):
		c_val = ncr(n,r)
		if c_val > mil: values.append(c_val)
print (len(values))