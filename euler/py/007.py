# 10001th prime
def isprime(n):
    if n%2 == 0 or n%3 == 0: return False
    for i in range(2,int(n**0.5)+1): 
        if n%i==0: return False
    return True

primes, no = [2,3], 5

while len(primes)  <= 10000:
    if isprime(no) == True: primes.append(no)
    no += 1
assert (len(primes)) == 10001
print (primes[-1])

    
