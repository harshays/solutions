# pentagon numbers
# first pj,pk pair has minimum D

def gen_pent(lim):
	return set(i*(3*i - 1)//2 for i in range(1,lim))

def check_pent(c,a=3,b=-1):
	c *=(-2)
	dis = ((b**2 - 4*a*c)**0.5)
	v1 = (-b + dis)/(2*a)
	v2 = v1 + dis/a
	for x in [v1,v2]:  
		if x > 0 and x == int(x): return True
	return False

pents = sorted(gen_pent(5000))
maxval = pents[-1]
for j in range(len(pents)):
	pj = pents[j]
	for k in range(j+1,len(pents)):
		pk = pents[k]
		s,d = pj + pk,abs(pk-pj)
		if s > maxval: continue
		if check_pent(s) == True and check_pent(d) == True: 
			print (pj,pk,s)
			print ('D:',d)
			exit(0)
