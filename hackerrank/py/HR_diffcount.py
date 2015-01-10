def makelistsameline(strnos): return list(map(int,strnos.split()))

def bs(key,arr): #sorted array only
	low, high = 0, len(arr) - 1
	while low <= high:
		mid = (low + high)//2
		if key > arr[mid]: low = mid+1
		elif key < arr[mid]: high = mid - 1
		else: return mid
	return -1

N,K = makelistsameline(input())
arr = makelistsameline(input())
arr.sort()

count = 0
for i in range(N):
	val = arr[i]
	diff1 = K + val
	if bs(diff1,arr) != -1 or bs(-diff1,arr) != -1: 
		# print (diff1,'-',val,'=',K)
		count += 1

print (count)