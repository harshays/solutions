from itertools import combinations
def makelistsameline(strnos): return list(map(int,strnos.split()))

N = int(input())
ans = set()
arr = set(makelistsameline(input()))
for x in combinations(arr,3):
	if x not in ans and x[2] > x[1] > x[0]: ans.add(x)
print (len(ans))
