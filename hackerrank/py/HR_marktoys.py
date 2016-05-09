
def makelistsameline(strnos):
	return list(map(lambda x: int(x),strnos.split()))

N,K = makelistsameline(input())
toys = makelistsameline(input())
toys = sorted(toys)

maxtoys = 0
cost = 0

for x in range(len(toys)):
	cost+=(toys[x])
	if cost <= K: maxtoys+=1
	else: break


print (maxtoys)
