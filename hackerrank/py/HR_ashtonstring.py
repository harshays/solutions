# correct but too slow. need to know about suffix array N log N
import profile 
import timeit
def main():
	T = int(input())
	for x in range(T):
		s = input()
		i = int(input()) - 1
		print (substrings(s,i))

def substrings(s,index):
	l,l1 = len(s),[]
	for x in range(l):
		for i in range(1,l-x+1):
			temp = s[x:x+i]
			if temp in l1: continue
			else: l1.append(temp)
	return (''.join(sorted(l1)))[index]


profile.run('main()')
print (timeit.timeit('main()'))
