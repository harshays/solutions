from fractions import gcd 
def subset(s):
	l = len(s)
	l1 = [] 
	for x in range(l):
		for i in range(1,l-x+1):
			temp = (s[x:x+i])
			temp.sort()
			if temp in l1: continue
			else: l1.append(temp)
	return l1

def gcd_final(lofl):
	def gcd_list(lst):
		l = len(lst)
		if l > 1:
			for x in range(1,l):
				a,b = lst[x-1],lst[x]
				if gcd(a,b) > 1: return False
			return True
		else:
			if lst[0] == 1: return True
			else: return False

	for lst in lofl:
		if gcd_list(lst) == True : return True
	return False

def makelistsameline(strnos): return list(map(int,strnos.split()))

def main():
	cases = int(input())
	for x in range(cases):
		N = int(input())
		a = makelistsameline(input())
		if gcd_final(subset(a)) == True: print ("YES")
		else: print ("NO")

main()


