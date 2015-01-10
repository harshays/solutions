
# gem stones
# element in 'a' to 'z'. more than once in single rock
# gem element if occurs at least once in every rock

# Input: 
# - N rocks 
# - next N lines: composition of rocks 

# OUTPUT:
# - print no of gem stones

N = int(input())

def getcases(N):
	testcases = [] 
	for x in range(N):
		temp_test = input()
		testcases.append(temp_test)
	return testcases

def removeduplicate(string):
	nondup = ''
	for x in string:
		if x not in nondup: nondup+=x
	return nondup

element = dict()
testcases = getcases(N)

firstrock = testcases[0]
musthaverocks = {} # list of must have elements
for x in firstrock:
	if x not in musthaverocks:
		musthaverocks[x] = 1
	else: pass

for rock in testcases[1:]:
	rock = removeduplicate(rock)
	for elem in rock:
		if elem in musthaverocks: musthaverocks[elem]+=1

gems = 0
for x in musthaverocks:
	if musthaverocks[x] ==  N:
		gems+=1

print (gems)


