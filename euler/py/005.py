# smallest multiple
def euler(a,b):
	while b: a,b=b,a%b
	return a

r = list(range(1,21))
for x in range(1,len(r)): r[x]=(r[x]*r[x-1])//euler(r[x],r[x-1]) # gcd of a,b = a*b/lcm(a,b)
print (r[-1])