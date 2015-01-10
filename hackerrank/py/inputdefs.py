import random
from timeit import timeit
def makelistsameline(strnos): return list(map(int,strnos.split()))

def palindrome(string): return string == string[::-1]

def inputgen(N): return " ".join(map(str,randomarray(N)))

def randomarray(L,r=1000): return [random.randint(1,r) for x in range(L)]

def pp(L): print (" ".join(map(str,L)))

def GCD(a,b):
	while a: a,b=a%b,a
	return b

def removeduplicate(inp,what='string'): # type can also be 'list' 
	k = list(set(inp))
	if what == 'string': return " ".join(k)
	elif what == 'list': return k

def substrings(s):
	l,l1 = len(s),[]
	for x in range(l):
		for i in range(1,l-x+1):
			temp = s[x:x+i]
			if temp in l1: continue
			else: l1.append(temp)
	return (sorted(l1))

def reducebyone(letter):
	a2z = 'abcdefghijklmnopqrstuvwxyz'
	index = a2z.find(letter)
	if index != 0:
		return a2z[index-1]
	else:
		return letter

def makelistperline(T): return [ input() for x in range(T)]


if __name__ == '__main__':
	print (help(set.add))
	





