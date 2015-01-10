# Counting Sort, a fast way to sort lists where the elements have a small number
# of possible values, such as integers within a certain range. We will start
# with an easy task - counting

def makelistsameline(strnos):
	return list(map(lambda x: int(x),strnos.split()))

def pp(L):
	print (" ".join(map(str,L)))

N = int(input())
ar = makelistsameline(input())
mm = [min(ar),max(ar)]
count = dict.fromkeys(range(mm[0],mm[1]),0)

for x in ar:
	count[x]+=1
ordered = []
for no,times in tuple(count.items()):
	if times == 0: continue
	ordered.extend([no]*times)
x = len(ordered)//2
print (ordered[x])