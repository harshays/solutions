# pearson product moment correaltion between PM,PC,MC --> PCM

# Input
# N students 
# N lines of M P C 

# output 2 dp
# f(MP)
# f(PC)
# f(CM)

N = int(input())

def pearson(listx,listy,n=N):
	sx = sum(listx)
	sy = sum(listy)
	sx2 = sum([x**2 for x in listx])
	sy2 = sum([y**2 for y in listy])
	sxy = 0
	for a,b in zip(listx,listy):
		sxy+=(a*b)
	pearnum = n*sxy - sx*sy
	peardenom = ((n*sx2 - (sx**2))**0.5)*((n*sy2 - sy**2)**0.5)
	return pearnum/peardenom

math,phy,chem = [[],[],[]]
for x in range(N):
	l = input().split()
	m,p,c = map((lambda x: int(x)),l)
	math.append(m)
	phy.append(p)
	chem.append(c)

mp = pearson(math,phy)
pc = pearson(phy,chem)
cm = pearson(chem,math)

for x in [mp,pc,cm]:
	print ('%.2f' %(x))
	

	