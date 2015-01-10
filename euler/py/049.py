# prime permutations
from itertools import permutations

def isprime(n):
    if n%2 == 0 or n%3 == 0 or n%5 == 0: return False
    for i in range(2,int(n**0.5)+1): 
        if n%i==0: return False
    return True

def npr(number): return list(filter(isprime,[int(("".join(list(x)))) for x in permutations(str(number))]))
r = list(map(npr,filter(isprime,range(1001,10000,2))))

ans = set() 
for pperm in r:
	length = len(pperm)
	for i in range(length):
		for j in range(i+1,length):
			d = pperm[j]-pperm[i]
			for k in range(j+1,length):
				if pperm[k] - pperm[j] == d and pperm[k] != pperm[j] != pperm[i]: 
					a,b,c = pperm[i],pperm[j],pperm[k]
					ans.add("".join(list(map(str,sorted([a,b,c])))))
print (ans)


