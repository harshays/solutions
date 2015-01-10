# largest decent no
# only 3 or 5 as digs
# number of time 3 appears div by 5
# no of times 5 appears div by 3
# T, T lines each with N (number of dig)
# if not possible, print -1 

def counter(string):
	c3,c5 = [0,0]
	for x in string:
		if x == '5': c5+=1
		else: c3+=1
	return [c3,c5]

def checkmod(string):
	modc = counter(string)
	if modc[0]%5==0 and modc[1]%3==0:
		return True
	else: return False

def change(string):
	l = len(string)
	no35 = counter(string)
	still5 = l - (no35[0]) - 5
	if still5 <= 0:  
		ans = (('3'*sum(no35)))
	else: 
		ans = (('5'*still5)+('3'*5)+('3'*no35[0]))
	return ans 



T = int(input())
for i in range(T):
	digs = int(input())
	initialno = '5'*digs
	last5 = len(initialno) - 1
	while  checkmod(initialno) != True:
		initialno = change(initialno)
		no3 = counter(initialno)[0]
		if no3 == digs:
			break
	no3 = counter(initialno)[0]
	if no3 % 5 != 0: return -1
	else: return initialno 





