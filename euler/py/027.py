# quadratic primes
# a and b -999 to 999

def f(x,a,b): return (x**2 + a*x + b)

def isprime(n):
	if n == 2 or n == 3: return True
	if n <= 1 or n%2 == 0 or n%3 == 0: return False
	for i in range(2,int(n**0.5)+1): 
		if n%i==0: return False
	return True

current_total = max_total = max_a = max_b = 0

for a in range(-999,1000):
	for b in range(-999,1000):
		current_total = n = 0
		while isprime(f(n,a,b)): n,current_total=n+1,n+1
		if current_total > max_total: max_a,max_b,max_total = a,b,current_total


print (max_a*max_b,max_total)
