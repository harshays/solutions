# truncatable primes
from math import sqrt

def isprime(n):
	if n == 1: return False
	if n == 2 or n == 3 or n == 5: return True
	if n%3 == 0 or n%5 ==0: return False
	for i in range(2,int(sqrt(n))+1):
		if n%i==0: return False
	return True

def all_nos(n):
	if isprime(n) == False: return False
	lim = len(str(n)) -  1
	ans = [n]
	for x in range(lim):
		rem = n % 10**(x+1)
		if isprime(rem) == False: return False
		number = n // (10**(x+1))
		if isprime(number) == False: return False
	return True

no = 9
truncs = []
total = howmany = 0
while True:
	if all_nos(no): 
		total += no
		howmany += 1
	if (howmany == 11): break
	no+=2
print (total)


