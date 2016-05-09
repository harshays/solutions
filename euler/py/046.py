# goldbachs other conjecture
from math import sqrt
def isprime(n):
	if n == 2 or n == 3 or n == 5: return True
	if n%2 == 0 or n%3 == 0 or n%5 == 0: return False
	for i in range(2,int(n**0.5)+1): 
		if n%i==0: return False
	return True

def nextcompositeodd(initialval): #generator
	while True:
		if not isprime(initialval): yield initialval 
		initialval += 2

def check_goldbach(n):
	primes_till_n = (filter(isprime,range(2,n+1)))
	for x in primes_till_n:
		cval = (n - x)/2
		if sqrt(cval) == int(sqrt((n-x)/2)): return True
	return False

comgen = nextcompositeodd(11)
currentval = next(comgen)
while check_goldbach(currentval) == True:  currentval = next(comgen)
print (currentval)