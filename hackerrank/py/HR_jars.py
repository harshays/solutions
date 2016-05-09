# N empty jars l1
# M operations a b k l1
# M lines, each a b k

# normal way too slow. moving average required

# output - avg no of candies

f1 = input().split()
N, M = int(f1[0]),int(f1[1]) # N jars and M operations
ops = [] # M abk's
# a b k 
for i in range(M):
	f2 = input().split()
	a, b, k = int(f2[0]),int(f2[1]), int(f2[2])
	ops.append([a,b,k])

#jars = dict.fromkeys(range(1,N+1),0)

def perform(abk):
	a,b,k = abk
	temptot = (b-a+1)*k
	return temptot

total = 0 
for i in range(M):
	total+=(perform(ops[i]))

avg = ((str(total/N)).split('.'))[0]
print (avg)

