l1 = input().split()
N = int(l1[0])
K = int(l1[1])

def makelistsameline(strnos):
	return list(map(lambda x: int(x),strnos.split()))

C = sorted(makelistsameline(input()))[::-1]

normal_cases = N//K
special_cases = N % K
C_copy = C

f_per_f = 0
total = 0

def allbuy(C,f):
	tt = 0
	for x in range(K):
		temp = (f+1)*C[x]
		tt += temp
	return tt

for x in range(normal_cases):
	total += allbuy(C,f_per_f)
	C = C[K:]
	f_per_f += 1

for x in C:
	total += (f_per_f+1)*x

print (total)






