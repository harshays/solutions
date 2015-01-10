# TOO SLOW
# need to use DP -> ith iter = i-1 th iter - sum(arr) + arr[0]*len(arr)

def main():
	N = int(input())
	def makelistsameline(strnos): return list(map(int,strnos.split()))
	a = makelistsameline(input())
	print (maxval(a))

def maxval(a):
	l = len(a)
	ae = a*2
	def pmean(start,a=ae):
		#(a[start:start+l])
		mult = 1
		pm = 0
		for x in range(l):
			pm += (mult)*a[x+s]
			mult+=1
		return pm
	maximum = -(float('inf')) # important
	for s in range(l):
		temp = (pmean(start=s))
		if temp > maximum: maximum = temp 
	return maximum

def test():
	import random
	def randomarray(L,r=1000): return [random.randint(1,r) for x in range(L)]
	r = randomarray(10000)
	print (maxval(r))
		
		

main()

# slow for input array len > 5k