# calc number of handshakes

T = int(input())
def getcases(N):
	testcases = [] 
	for x in range(N):
		temp_test = input()
		testcases.append(temp_test)
	return testcases
testcases = getcases(T)
testcases = map(lambda x: int(x), testcases)

for test in testcases:
	if test > 1:
		print (int((test*(test-1))/2))
	else: 
		print (0)
