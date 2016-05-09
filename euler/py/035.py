# circular primes

def circular(number):
	n = str(number)
	nn,n_l,all_n = n*2,len(n),[]
	return [int(nn[i:i+n_l]) for i in range(n_l)]

def isprime(number):
	if number % 3 == 0 or number % 5 == 0: return False
	for i in range(2,int(number**0.5)+1): 
	    if number%i==0: return False
	return True

primes = set(i for i in range(7,1000000,2) if isprime(i))

def check(lis):
	for no in lis:
		if no not in primes: return False
	return True

count = 13 # all primes < 100
for i in range(101,1000000,2):
	if check(circular(i)): count += 1

print (count)


