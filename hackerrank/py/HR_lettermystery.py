# hackerRank sum 4

# changes all words to palindromes
# reduces val of letter by one
# can only be reduced to 'a'
# find the minimum no of reduced required to make a string palindromic

# input T - no of testcases
# T string, one each 

def palindrome(string):
	return string == string[::-1]

def reducebyone(letter):
	a2z = 'abcdefghijklmnopqrstuvwxyz'
	index = a2z.find(letter)
	if index == 0:
		return letter
	elif index > 0:
		return a2z[index-1]

# make input
T = int(input())
def makelist2(T):
	testcases = []
	for i in range(T):
		temp_test = (input())
		testcases.append(temp_test)
	return testcases
testcases = makelist2(T)

# abc --> abb --> aba
# abcd --> abcc abcb abca abba

# a[i] and a[len(a)-i] while i > len(a) - i 

# 'abcd'
def reduceto(l1,l2): #l1 > l2
	count = 0
	while l1 != l2:
		l1 = reduce(l1)
		count+=1
	return count

results4 = []
for string in testcases:
	length = len(string)
	stringcount = []
	for x in range(length >> 1):
		letter1 = string[x]
		letter2 = string[length - x - 1]
		if letter1 > letter2:
			stringcount.append(reduceto(letter1,letter2))
		elif letter1 < letter2:
			stringcount.append(reduceto(letter2,letter1))
		else: stringcount.append(0)
	results4.append(sum(stringcount))

for x in results4:
	print (x)
