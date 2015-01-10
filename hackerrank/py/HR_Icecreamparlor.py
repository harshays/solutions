def find(tot,arr):
	for i in range(len(arr)):
		fval = arr[i]
		for j in range(i+1,len(arr)):
			if arr[j] + fval == tot:
				print (i+1,j+1)

T = int(input())
for x in range(T):
	m = int(input())
	n = int(input())
	arr = list(map(int,input().split()))
	find(m,arr)




