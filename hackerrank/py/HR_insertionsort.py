def insertionsort(a):
	count = 0
	length = len(a)
	for x in range(1,length):
		key = a[x]
		prev = x-1
		while prev >= 0 and a[prev] > key:
			a[prev+1]=a[prev]
			prev-=1
			count+=1
		a[prev+1]=key
	return count

def makelistsameline(strnos,N):
	strnos = strnos.split()
	widtharray = [] 
	for i in range(N):
		widtharray.append(int(strnos[i]))
	return widtharray

N =int(input()
L = makelistsameline(input(),N)
print (insertionsort(L))
