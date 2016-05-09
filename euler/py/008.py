# max product
nums=open("input/8input.txt",'r')
inp = ("".join(map(lambda x: (x[:-1]), [nums.readline() for x in range(20)])))

def product(lst,i):
	new_lst = lst[i:i+13]
	if '0' in new_lst: return 0
	lst = map(int,lst[i:i+13])
	prod = 1
	for x in lst: prod*=x
	return prod 

r = range(len(inp)-14)
prod = 1
for x in r:
	temp = product(inp,x)
	if temp > prod : prod = temp

print (prod)
