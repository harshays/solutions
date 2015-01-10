def insertionsorted(a):
	for x in range(1,len(a)):
		key = a[x]
		y = x-1
		while (a[y] > key) and (y >= 0):
			a[y+1] = a[y]
			y-=1
		a[y+1]=key
		print (" ".join(map(str,a)))
		

def makelistsameline(strnos):
	return list(map(lambda x: int(x),strnos.split()))

N =int(input())
L = makelistsameline(input())
insertionsorted(L)
