def makelistsameline(strnos):
	return list(map(lambda x: int(x),strnos.split()))

def summ(arr,a,b): # a b inclusive
	tot = 0
	for x in range(a,b+1):
		tot+=arr[x]
	return tot

def check(arr):
	length = len(arr)
	if len(arr) == 1: return True
	elif len(arr) == 2: 
		if 0 in arr: return True 
		else: return False
	else:
		return chck(arr)

def chck(a):
	def c(a,b): return a == b
	l = len(a)
	x = 1
	s1 = a[0]
	s2 = summ(a,2,l-1)
	while x <= l - 2:
		if c(s1,s2) == True: return True
		x+=1
		s1+=a[x-1]
		s2-=a[x]
	return False

T  = int(input()) 
for x in range(T):
	N = int(input())
	a = makelistsameline(input())
	length = len(a)
	if check(a): print ("YES")
	else: print ("NO")


