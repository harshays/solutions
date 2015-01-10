# hackerRank sum 3

# length of highway and service lane is N units
# service lane consists of N segments of unit length with diff widths
# enter and exit from any segment
# enter segment i and exit statement j --> j > i >=0
# has to pass from all segments i to j to exit
# 1 width bike 2 width car 3 width truck
# width[] of length N where width of kth segment is width[k]
# width[k] = 1 only bike
# width[k] = 2 bike and car
# width[k] = 3 bike car or truck

# PS - given entry and exit point, output largest vehicle which can pass
# input - first line N (length) and T (number of test cases)
# then N numbers forming width array
# then T lines with width array on each line (i,j)

line1 = (input()).split()
N = int(line1[0])
T = int(line1[-1])

def makelist(strnos,N):
	strnos = strnos.split()
	widtharray = [] 
	for i in range(N):
		widtharray.append(int(strnos[i]))
	return widtharray

widtharray = makelist(input(), N)
testcases = []
for i in range(T):
	temp_test = input().split()
	temp_test = [int(temp_test[0]),int(temp_test[1])]
	testcases.append(temp_test)

# N and T done, widtharray done, testcases done
results3 = []
for x in testcases:
	i,j = x[0],x[1]
	temp_test = min(widtharray[i:(j+1)])
	results3.append(temp_test)

for x in results3:
	print (x)








