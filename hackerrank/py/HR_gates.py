def maxmin(arr,a,b):
	return (arr[b-1]-arr[a])
N = int(input())
K = int(input())
candy = []
for i in range(N):
	candy.append(int(input()))
candy = (sorted(candy))
minval = maxmin(candy,0,K)
print (minval)
for x in range(1,N-K):
	curval = maxmin(candy,x,K+x)
	print (curval)
	if curval < minval: minval = curval
print (minval)


# NICE SUM