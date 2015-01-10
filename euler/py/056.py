# max digital sum of a^b
def digitalsum(strno):
	s = 0
	for x in strno: s+=int(x)
	return s
print (max(map(digitalsum,map(str,[a**b for a in range(1,100) for b in range(1,100)]))))