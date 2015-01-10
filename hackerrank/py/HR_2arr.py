# Ai + Bi >= K

def main():
	def makelistsameline(strnos): return list(map(int,strnos.split()))
	T = int(input())
	for x in range(T):
		N,K = makelistsameline(input())
		a = makelistsameline(input())
		b = makelistsameline(input())
		if check(a,b,K) == True: print ("YES")
		else: print ("NO") 

def check(l1,l2,k):
	l1.sort()
	l2.sort(reverse=True)
	for a,b in zip(l1,l2):
		if a + b < k: return False
	return True

main()
