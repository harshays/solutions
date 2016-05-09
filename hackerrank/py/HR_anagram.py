string = input()
string = list(string)
count = dict.fromkeys(string,0)
for x in string:
	count[x]+=1
for x in count.keys():
	count[x] = count[x]%2
zero = 0
one = 0
for x in count.values():
	if x == 1: one+=1
	else: zero+=1

l = len(string)
# print (count)
# print (l)
# print ('zero',zero,'one',one)

if l%2 == 1:
	if one == 1:
		print ('YES')
	else: print ('NO')
else:
	if one == 0:
		print ("YES")
	else: 
		print ("NO")