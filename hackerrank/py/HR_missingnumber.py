def main():
	def makelistsameline(strnos): return list(map(int,strnos.split()))
	N_a = int(input())
	a = makelistsameline(input())
	N_b = int(input())
	b = makelistsameline(input())
	l_a = len(a)
	l_b = len(b)
	final = []
	if N_a >= N_b: firstlst,secondlst = a,b
	else: firstlst,secondlst = b,a
	net = dict.fromkeys(firstlst,0)
	for x in firstlst:
		net[x]+=1
	for x in secondlst:
		net[x]-=1
	for x in net:
		if net[x] == 0: continue
		elif net[x] > 0:
			temp = [x]
			final.extend(temp)
	final2 = set()
	for x in final:
		if x not in final2:
			final2.add(x)
	for x in final2: print (x,end=" ")

main()



