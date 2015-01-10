# reciprocal cycles
from decimal import *
getcontext().prec = 2000 # setting dp precision

def recurring_cyc(n):
	n_z = len(str(n)) - 1 # number of initial zeroes
	n = str((Decimal(1)/Decimal(n))).split('.')[1][n_z:]
	for i in range(1,len(n)):
		if (n[:i] == n[i:i*2]): return i
	return 0

curval = maxval = max_d = 0
for x in range(2,1000):
	curval = recurring_cyc(x)
	if curval > maxval: maxval,max_d = curval,x

print (maxval,max_d)