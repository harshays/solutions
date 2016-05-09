# massa and stepping stones
# find all final values of treasure
# consecutive diff can be a or b 


# IO
T = int(input())  
testcases = [] # format --> [[n,a,b],[n,a,b]...] 

for c in range(T):
	n = int(input()) - 1 # of stones  excluding first 0
	a = int(input()) # diff 1
	b = int(input()) # diff 2
	onetest = [n,a,b]
	testcases.append(onetest)


#defs
def printlist(lst):
	ans = ''
	for x in lst:
		ans+=(str(x) + " ")
	return ans[:-1]

def allfinals(nab):
	n,a,b = nab 
	results = []
	for i in range(n)[::-1]:
		results.append(i*a + (n-i)*b)
	results.append(n*a)
	results = sorted(results)
	results = removeduplicate(results,what='list')
	return results

def removeduplicate(inp,what='string'): # type can also be 'list' 
	if what == 'string':	
		nondup = ''
		for x in inp:
			if x not in nondup: nondup+=x
		return nondup
	if what == 'list':
		nondup = [] 
		for x in inp:
			if x not in nondup: nondup.append(x)
		return nondup

#do
outlist = []
for eachtest in testcases:
	results = allfinals(eachtest)
	outlist.append(results)
    
for lst in outlist:
    print (printlist(lst))








